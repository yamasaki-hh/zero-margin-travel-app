#!/usr/bin/env python3
"""
Automated Multi-Lingual Wikipedia & Wikimedia Commons Image Resolver
Zero-Margin Travel App - Scalable Architecture Pipeline with Live HTTP 200 Verification
"""

import urllib.request
import json
import urllib.parse
import ssl
import time
import re
import os

ctx = ssl._create_unverified_context()
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

CITY_LANG_MAP = {
    'Paris': 'fr',
    'Berlin': 'de',
    'Amsterdam': 'nl',
    'Brussels': 'fr',
    'Luxembourg': 'fr',
    'Cologne': 'de',
    'Munich': 'de'
}

def is_valid_photo_format(url_or_filename):
    if not url_or_filename:
        return False
    lower = url_or_filename.lower()
    if '.svg' in lower or 'logo' in lower or 'flag' in lower or 'blason' in lower or 'map' in lower or 'carte' in lower or 'coat_of_arms' in lower:
        return False
    return True

def is_url_live(url):
    if not url or not url.startswith('http'):
        return False
    try:
        req = urllib.request.Request(url, headers=HEADERS, method='HEAD')
        with urllib.request.urlopen(req, context=ctx, timeout=3) as res:
            return res.status == 200
    except Exception:
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, context=ctx, timeout=3) as res:
                return res.status == 200
        except Exception:
            return False

def fetch_json(url, timeout=4):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=ctx, timeout=timeout) as res:
            if res.status == 200:
                return json.loads(res.read().decode('utf-8'))
    except Exception:
        pass
    return None

def get_commons_thumb(filename, width=330):
    if not filename:
        return ""
    clean_fn = filename.replace('File:', '').replace('Fichier:', '').replace('Datei:', '').replace('Afbeelding:', '').strip()
    url = f'https://commons.wikimedia.org/w/api.php?action=query&titles=File:{urllib.parse.quote(clean_fn)}&prop=imageinfo&iiprop=url&iiurlwidth={width}&format=json&origin=*'
    data = fetch_json(url)
    if data:
        pages = data.get('query', {}).get('pages', {})
        for pid, pinfo in pages.items():
            if 'imageinfo' in pinfo and pinfo['imageinfo']:
                thumb = pinfo['imageinfo'][0].get('thumburl', '')
                if thumb and is_valid_photo_format(thumb) and is_url_live(thumb):
                    return thumb
    return ""

def step1_summary_photo(slug, lang='en'):
    url = f'https://{lang}.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(slug)}'
    data = fetch_json(url)
    if data:
        src = data.get('thumbnail', {}).get('source', '')
        if src and is_valid_photo_format(src) and is_url_live(src):
            return src
    return ""

def step2_infobox_photo(slug, lang='fr'):
    url = f'https://{lang}.wikipedia.org/w/api.php?action=parse&page={urllib.parse.quote(slug)}&prop=wikitext&format=json&origin=*'
    data = fetch_json(url)
    if data:
        wt = data.get('parse', {}).get('wikitext', {}).get('*', '')
        match = re.search(r'(?:image|bild|foto|photograph|picture|afbeelding)\s*=\s*([^|\n}]+)', wt, re.IGNORECASE)
        if match:
            fn = match.group(1).strip()
            if is_valid_photo_format(fn):
                thumb = get_commons_thumb(fn, 330)
                if thumb:
                    return thumb
    return ""

def step3_commons_search_photo(spot_name, city_name):
    query = f"{spot_name} {city_name} building facade"
    url = f'https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(query)}&gsrnamespace=6&prop=imageinfo&iiprop=url&iiurlwidth=330&gslimit=5&format=json&origin=*'
    data = fetch_json(url)
    if data:
        pages = data.get('query', {}).get('pages', {})
        for pid, pinfo in pages.items():
            title = pinfo.get('title', '')
            if is_valid_photo_format(title):
                thumb = pinfo.get('imageinfo', [{}])[0].get('thumburl', '')
                if thumb and is_valid_photo_format(thumb) and is_url_live(thumb):
                    return thumb
    return ""

def run_auto_pipeline(js_file_path):
    print("🚀 Running Scalable Automated Multi-Lingual Wikipedia Image Resolver Pipeline...")
    with open(js_file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    db_match = re.search(r'const candidateSpotsDatabase = (\{[\s\S]*?\n\};)', code)
    if not db_match:
        print("❌ Error: candidateSpotsDatabase not found in JS file!")
        return

    db_json_str = db_match.group(1).rstrip(';')
    db_data = json.loads(db_json_str)

    photo_count = 0
    fallback_count = 0

    for city, spots in db_data.items():
        clean_city = city.split(',')[0].strip()
        lang = CITY_LANG_MAP.get(clean_city, 'en')
        for spot in spots:
            name = spot['name']
            curr_img = spot.get('image', '')
            
            # If spot already has a verified, live 200 OK JPEG URL, preserve it!
            if curr_img and is_valid_photo_format(curr_img) and is_url_live(curr_img):
                photo_url = curr_img
                method = "Live 200 OK Preserved"
            else:
                clean_name = name.split(' (')[0].strip()
                slug = clean_name.replace(' ', '_')
                
                # Step 1: Summary API (en -> local lang)
                photo_url = step1_summary_photo(slug, 'en') or step1_summary_photo(slug, lang)
                method = f"Step1 Summary ({lang})"
                
                # Step 2: Infobox Wikitext Parser
                if not photo_url:
                    photo_url = step2_infobox_photo(slug, lang) or step2_infobox_photo(slug, 'en')
                    method = f"Step2 Infobox ({lang})"
                    
                # Step 3: Commons Search Fallback
                if not photo_url:
                    photo_url = step3_commons_search_photo(clean_name, clean_city)
                    method = "Step3 Commons Search"
                    
                # Step 4: Category Header Box Fallback
                if not photo_url:
                    method = "Step4 Category Header Box"

            if photo_url and is_valid_photo_format(photo_url):
                spot['image'] = photo_url
                spot['hasWiki'] = True
                photo_count += 1
                print(f"  ✅ [{method}] \"{name}\" -> {photo_url[:65]}...")
            else:
                spot['image'] = ""
                spot['hasWiki'] = False
                fallback_count += 1
                print(f"  🏷️ [{method}] \"{name}\" -> Category Header Box Fallback")

    new_db_json = json.dumps(db_data, indent=2, ensure_ascii=False)
    new_code = code[:db_match.start(1)] + new_db_json + ';\n' + code[db_match.end(1):]

    with open(js_file_path, 'w', encoding='utf-8') as f:
        f.write(new_code)

    print("\n=======================================================")
    print(f"🎉 PIPELINE COMPLETED SUCCESSFULLY!")
    print(f"   - Verified Live 200 OK Real Photographs: {photo_count} spots")
    print(f"   - Category Header Box Fallbacks (0% Mismatch): {fallback_count} spots")
    print(f"   - Total Spots Processed: {photo_count + fallback_count}")
    print("=======================================================")

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    js_path = os.path.join(script_dir, '..', 'js', 'ai-travel-engine.js')
    run_auto_pipeline(js_path)
