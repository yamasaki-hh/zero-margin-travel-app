#!/usr/bin/env python3
"""
Zero-Margin Travel App - Universal City-Modular Wikipedia Image Pipeline
100% Equal, Generic, Modular Architecture for All Cities
"""

import urllib.request
import json
import urllib.parse
import ssl
import time
import glob
import os

ctx = ssl._create_unverified_context()
HEADERS = {
    'User-Agent': 'ZeroMarginTravelApp/8.0 (https://github.com/zeromargin-travel/zero-margin-travel-app; contact@zeromargin-travel.org)'
}

def is_valid_thumbnail(url):
    return bool(url)

def fetch_wiki_summary(lang, slug):
    url = f'https://{lang}.wikipedia.org/api/rest_v1/page/summary/{slug}'
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=ctx, timeout=3) as res:
            if res.status == 200:
                data = json.loads(res.read().decode('utf-8'))
                src = data.get('thumbnail', {}).get('source', '')
                if src and is_valid_thumbnail(src):
                    return src
    except Exception:
        pass
    return ""

def process_all_city_modules(data_cities_dir, js_file_path):
    print("🚀 Running Universal City-Modular Wikipedia Resolver...")
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
            name = spot.get('name', '')
            clean_name = name.split(' (')[0].strip().replace(' ', '_')
            encoded_slug = urllib.parse.quote(clean_name)

            # Try English Wikipedia first, then native language if slug contains accents
            photo_url = fetch_wiki_summary('en', encoded_slug)
            if not photo_url and ('%' in encoded_slug or len(clean_name) != len(clean_name.encode('ascii', 'ignore'))):
                photo_url = fetch_wiki_summary('fr', encoded_slug) or fetch_wiki_summary('de', encoded_slug) or fetch_wiki_summary('nl', encoded_slug)

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
                
            time.sleep(0.01)

        city_data['spots'] = spots
        city_data['spotCount'] = len(spots)

        with open(jf, 'w', encoding='utf-8') as f:
            json.dump(city_data, f, indent=2, ensure_ascii=False)

        aggregated_db[city_name] = spots
        print(f"   └─ Module Result: {city_photo_cnt} photos, {city_fallback_cnt} fallbacks")

    # Update aggregated database in js/ai-travel-engine.js
    if os.path.exists(js_file_path):
        with open(js_file_path, 'r', encoding='utf-8') as f:
            js_code = f.read()

        db_marker = 'const candidateSpotsDatabase = '
        start_idx = js_code.find(db_marker)
        if start_idx != -1:
            end_idx = js_code.find(';\n', start_idx)
            if end_idx != -1:
                new_db_json = json.dumps(aggregated_db, indent=2, ensure_ascii=False)
                new_js_code = js_code[:start_idx + len(db_marker)] + new_db_json + js_code[end_idx:]
                with open(js_file_path, 'w', encoding='utf-8') as f:
                    f.write(new_js_code)
                print(f"\n✅ Successfully updated {js_file_path} with aggregated city modules!")

    print("\n=======================================================")
    print(f"🎉 UNIVERSAL CITY-MODULAR PIPELINE FINISHED!")
    print(f"   - Total Verified Wikipedia Photos: {total_photos} spots")
    print(f"   - Total Category Header Box Fallbacks: {total_fallbacks} spots")
    print(f"   - Total Spots Across All Modules: {total_photos + total_fallbacks}")
    print("=======================================================")

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    cities_dir = os.path.join(base_dir, '..', 'data', 'cities')
    js_path = os.path.join(base_dir, '..', 'js', 'ai-travel-engine.js')
    process_all_city_modules(cities_dir, js_path)
