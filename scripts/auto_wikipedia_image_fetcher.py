#!/usr/bin/env python3
"""
Zero-Margin Travel App - Universal City-Modular Wikipedia Image Pipeline (v3.0.0)
100% Robust Parenthesis Normalization & Multi-Language Wikipedia API Resolution
"""

import urllib.request
import json
import urllib.parse
import ssl
import time
import glob
import os
import re

ctx = ssl._create_unverified_context()
HEADERS = {
    'User-Agent': 'ZeroMarginTravelApp/17.0 (https://github.com/zeromargin-travel/zero-margin-travel-app; contact@zeromargin-travel.org)'
}

def clean_title(raw_title):
    if not raw_title:
        return ""
    # Strip fullwidth （...） and halfwidth (...) parenthetical text
    cleaned = re.sub(r'[\(\（].*?[\)\）]', '', raw_title).strip()
    return cleaned

def fetch_wiki_summary(lang, slug):
    if not slug:
        return ""
    encoded_slug = urllib.parse.quote(slug.replace(' ', '_'))
    url = f'https://{lang}.wikipedia.org/api/rest_v1/page/summary/{encoded_slug}'
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=ctx, timeout=3) as res:
            if res.status == 200:
                data = json.loads(res.read().decode('utf-8'))
                src = data.get('thumbnail', {}).get('source', '')
                if src and ('upload.wikimedia.org' in src or 'http' in src):
                    return src
    except Exception:
        pass
    return ""

def resolve_spot_image(spot):
    # Candidate titles to search Wikipedia
    candidates = []
    
    # 1. DE name if available
    name_de = clean_title(spot.get('name_de', ''))
    if name_de:
        candidates.append(('de', name_de))
        candidates.append(('en', name_de))
    
    # 2. EN name if available
    name_en = clean_title(spot.get('name_en', ''))
    if name_en:
        candidates.append(('en', name_en))
        candidates.append(('de', name_en))
    
    # 3. FR name if available
    name_fr = clean_title(spot.get('name_fr', ''))
    if name_fr:
        candidates.append(('fr', name_fr))

    # 4. Fallback to general clean name
    name_gen = clean_title(spot.get('name', ''))
    if name_gen:
        candidates.append(('de', name_gen))
        candidates.append(('en', name_gen))
        candidates.append(('fr', name_gen))
        candidates.append(('nl', name_gen))

    # Perform lookup
    for lang, title in candidates:
        img_url = fetch_wiki_summary(lang, title)
        if img_url:
            return img_url

    return ""

def process_all_city_modules(data_cities_dir, js_file_path):
    print("🚀 Running Universal Wikipedia Image Pipeline (v3.0.0)...")
    json_files = sorted(glob.glob(os.path.join(data_cities_dir, '*.json')))
    
    if not json_files:
        print(f"❌ No city JSON files found in {data_cities_dir}")
        return

    aggregated_db = {}
    total_photos = 0
    total_fallbacks = 0

    for jf in json_files:
        filename = os.path.basename(jf)
        with open(jf, 'r', encoding='utf-8') as f:
            city_data = json.load(f)

        city_name = city_data.get('cityName', filename.replace('.json', '').title())
        spots = city_data.get('spots', [])
        print(f"\n📍 Processing City Module: {city_name} ({len(spots)} spots)...")

        city_photo_cnt = 0
        city_fallback_cnt = 0

        for spot in spots:
            # If spot already has a valid image, verify or keep it
            existing_img = spot.get('image', '')
            if existing_img and 'wikimedia.org' in existing_img:
                spot['hasWiki'] = True
                city_photo_cnt += 1
                total_photos += 1
                continue

            # Fetch image via Wikipedia API
            photo_url = resolve_spot_image(spot)
            if photo_url:
                spot['image'] = photo_url
                spot['hasWiki'] = True
                city_photo_cnt += 1
                total_photos += 1
            else:
                spot['image'] = ""
                spot['hasWiki'] = False
                city_fallback_cnt += 1
                total_fallbacks += 1
                
            time.sleep(0.005)

        city_data['spots'] = spots
        city_data['spotCount'] = len(spots)

        with open(jf, 'w', encoding='utf-8') as f:
            json.dump(city_data, f, indent=2, ensure_ascii=False)

        aggregated_db[city_name] = spots
        print(f"   └─ Module Result: {city_photo_cnt} verified photos, {city_fallback_cnt} fallbacks")

    print("\n=======================================================")
    print(f"🎉 UNIVERSAL WIKIPEDIA PHOTO PIPELINE COMPLETE!")
    print(f"   - Total Verified Wikipedia Photos: {total_photos} spots")
    print(f"   - Total Fallbacks: {total_fallbacks} spots")
    print(f"   - Total System Spots: {total_photos + total_fallbacks}")
    print("=======================================================")

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    cities_dir = os.path.join(base_dir, '..', 'data', 'cities')
    js_path = os.path.join(base_dir, '..', 'js', 'ai-travel-engine.js')
    process_all_city_modules(cities_dir, js_path)
