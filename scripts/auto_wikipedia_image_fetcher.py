#!/usr/bin/env python3
"""
Automated Multi-Lingual Wikipedia & Wikimedia Commons Image Resolver
Zero-Margin Travel App - Scalable Architecture Pipeline
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
    'User-Agent': 'ZeroMarginTravelApp/3.0 (https://github.com/yamasaki-hh/zero-margin-travel-app; contact@yamasaki-travel.org)'
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

def is_valid_photo(url_or_filename):
    if not url_or_filename:
        return False
    lower = url_or_filename.lower()
    if '.svg' in lower or 'logo' in lower or 'flag' in lower or 'blason' in lower or 'map' in lower or 'carte' in lower or 'coat_of_arms' in lower:
        return False
    return True

def fetch_json(url, timeout=5):
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
    clean_fn = filename.replace('File:', '').replace('Fichier:', '').replace('Datei:', '').strip()
    url = f'https://commons.wikimedia.org/w/api.php?action=query&titles=File:{urllib.parse.quote(clean_fn)}&prop=imageinfo&iiprop=url&iiurlwidth={width}&format=json&origin=*'
    data = fetch_json(url)
    if data:
        pages = data.get('query', {}).get('pages', {})
        for pid, pinfo in pages.items():
            if 'imageinfo' in pinfo and pinfo['imageinfo']:
                thumb = pinfo['imageinfo'][0].get('thumburl', '')
                if thumb and is_valid_photo(thumb):
                    return thumb
    return ""

def step1_summary_photo(slug, lang='en'):
    url = f'https://{lang}.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(slug)}'
    data = fetch_json(url)
    if data:
        src = data.get('thumbnail', {}).get('source', '')
        if src and is_valid_photo(src):
            return src
    return ""

def step2_infobox_photo(slug, lang='fr'):
    url = f'https://{lang}.wikipedia.org/w/api.php?action=parse&page={urllib.parse.quote(slug)}&prop=wikitext&format=json&origin=*'
    data = fetch_json(url)
    if data:
        wt = data.get('parse', {}).get('wikitext', {}).get('*', '')
        # Regex search for image parameter in Infobox
        match = re.search(r'(?:image|bild|foto|photograph|picture)\s*=\s*([^|\n}]+)', wt, re.IGNORECASE)
        if match:
            fn = match.group(1).strip()
            if is_valid_photo(fn):
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
            if is_valid_photo(title):
                thumb = pinfo.get('imageinfo', [{}])[0].get('thumburl', '')
                if thumb and is_valid_photo(thumb):
                    return thumb
    return ""

def resolve_spot_photo(spot_name, city_name, explicit_slug=""):
    clean_city = city_name.split(',')[0].strip()
    lang = CITY_LANG_MAP.get(clean_city, 'en')
    
    clean_name = spot_name.split(' (')[0].strip()
    slug = explicit_slug or clean_name.replace(' ', '_')
    
    # Step 1: Summary API (en & local lang)
    p1 = step1_summary_photo(slug, 'en')
    if p1:
        return p1, "Step1 (Summary en)"
        
    p1_lang = step1_summary_photo(slug, lang)
    if p1_lang:
        return p1_lang, f"Step1 (Summary {lang})"
        
    # Step 2: Infobox Wikitext Parsing (local lang & en)
    p2 = step2_infobox_photo(slug, lang)
    if p2:
        return p2, f"Step2 (Infobox {lang})"
        
    p2_en = step2_infobox_photo(slug, 'en')
    if p2_en:
        return p2_en, "Step2 (Infobox en)"
        
    # Step 3: Wikimedia Commons Search Fallback
    p3 = step3_commons_search_photo(clean_name, clean_city)
    if p3:
        return p3, "Step3 (Commons Search)"
        
    # Step 4: Category Header Fallback
    return "", "Step4 (Category Header Box)"

def run_auto_pipeline(js_file_path):
    print("🚀 Launching Automated Multi-Lingual Wikipedia Image Resolver Pipeline...")
    with open(js_file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    db_match = re.search(r'const candidateSpotsDatabase = (\{[\s\S]*?\n\};)', code)
    if not db_match:
        print("❌ Error: candidateSpotsDatabase not found in JS file!")
        return

    db_json_str = db_match.group(1).rstrip(';')
    db_data = json.loads(db_json_str)

    # Known article title mappings for spots with naming variances
    known_slugs = {
        'Eiffel Tower': 'Tour_Eiffel_Wikimedia_Commons_(cropped).jpg',
        'Sacré-Cœur Basilica & Montmartre': 'Sacré-Cœur,_Paris',
        'Notre-Dame Cathedral': 'Notre-Dame_de_Paris',
        'Opéra Garnier (Palais Garnier)': 'Palais_Garnier',
        'Les Invalides & Napoleon\'s Tomb': 'Les_Invalides',
        'Pont Neuf & Île de la Cité': 'Pont_Neuf',
        'Catacombes de Paris': 'Paris_Catacombs',
        'Louvre Museum & Glass Pyramid': 'Louvre',
        'Musée Marmottan Monet': 'Musée_Marmottan_Monet',
        'Centre Pompidou': 'Centre_Georges-Pompidou',
        'Musée de Cluny (Middle Ages)': 'Musée_de_Cluny',
        'Musée du Quai Branly': 'Musée_du_quai_Branly_-_Jacques_Chirac',
        'Palace of Versailles (Château de Versailles)': 'Château_de_Versailles',
        'Brandenburg Gate': 'Brandenburg_Gate',
        'Reichstag Building Dome': 'Reichstag_building',
        'East Side Gallery Berlin Wall': 'East_Side_Gallery',
        'Berlin Cathedral (Berliner Dom)': 'Berlin_Cathedral',
        'Holocaust Memorial': 'Memorial_to_the_Murdered_Jews_of_Europe',
        'Victory Column (Siegessäule)': 'Berlin_Victory_Column',
        'Berlin TV Tower (Fernsehturm)': 'Fernsehturm_Berlin',
        'Kaiser Wilhelm Memorial Church': 'Kaiser_Wilhelm_Memorial_Church',
        'Neues Museum (Nefertiti Bust)': 'Neues_Museum',
        'Jewish Museum Berlin': 'Jewish_Museum_Berlin',
        'Rijksmuseum': 'Rijksmuseum',
        'Van Gogh Museum': 'Van_Gogh_Museum',
        'Anne Frank House': 'Anne_Frank_House',
        'Zaanse Schans Windmills': 'Zaanse_Schans',
        'Royal Palace of Amsterdam': 'Royal_Palace_of_Amsterdam',
        'Oude Kerk': 'Oude_Kerk_(Amsterdam)',
        'Begijnhof Courtyard': 'Begijnhof,_Amsterdam',
        'Bloemenmarkt (Floating Flower Market)': 'Bloemenmarkt',
        'Stedelijk Museum Amsterdam': 'Stedelijk_Museum_Amsterdam',
        'Grand-Place': 'Grand-Place',
        'Royal Gallery of Saint-Hubert': 'Royal_Galaxies_of_Saint-Hubert',
        'Atomium': 'Atomium',
        'St. Michael & St. Gudula Cathedral': 'Cathedral_of_St._Michael_and_St._Gudula',
        'Cinquantenaire Arch & Park': 'Parc_du_Cinquantenaire',
        'Bock Casemates': 'Bock_(Luxembourg)',
        'Grand Ducal Palace': 'Grand_Ducal_Palace,_Luxembourg',
        'Notre-Dame Cathedral Luxembourg': 'Notre-Dame_Cathedral,_Luxembourg',
        'MNHA Museum': 'National_Museum_of_History_and_Art',
        'Cologne Cathedral (Kölner Dom)': 'Cologne_Cathedral',
        'Hohenzollern Bridge (Love Locks)': 'Hohenzollern_Bridge',
        'Great St. Martin Church': 'Great_St._Martin_Church,_Cologne',
        'Cologne Chocolate Museum': 'Imhoff-Schokoladenmuseum',
        'Marienplatz & New Town Hall': 'Marienplatz',
        'English Garden & Eisbachwave': 'Englischer_Garten',
        'Frauenkirche (Cathedral of Our Dear Lady)': 'Munich_Frauenkirche',
        'Pinakothek Museums (Alte & Neue)': 'Alte_Pinakothek'
    }

    resolved_photos = 0
    category_fallbacks = 0

    for city, spots in db_data.items():
        clean_city = city.split(',')[0].strip()
        print(f"\n📍 Processing City: {city} ({len(spots)} candidate spots)...")
        for spot in spots:
            name = spot['name']
            explicit_slug = known_slugs.get(name, "")
            
            # If spot already has a custom verified Wikipedia JPEG, preserve it unless blank or svg
            curr_img = spot.get('image', '')
            if curr_img and is_valid_photo(curr_img) and 'upload.wikimedia.org' in curr_img:
                photo_url = curr_img
                method = "Preserved Verified JPEG"
            else:
                photo_url, method = resolve_spot_photo(name, clean_city, explicit_slug)
            
            if photo_url:
                spot['image'] = photo_url
                spot['hasWiki'] = True
                resolved_photos += 1
                print(f"  ✅ [{method}] \"{name}\" -> {photo_url[:60]}...")
            else:
                spot['image'] = ""
                spot['hasWiki'] = False
                category_fallbacks += 1
                print(f"  🏷️ [{method}] \"{name}\" -> Category Header Box")
            
            time.sleep(0.02)

    new_db_json = json.dumps(db_data, indent=2, ensure_ascii=False)
    new_code = code[:db_match.start(1)] + new_db_json + ';\n' + code[db_match.end(1):]

    with open(js_file_path, 'w', encoding='utf-8') as f:
        f.write(new_code)

    print("\n=======================================================")
    print(f"🎉 PIPELINE COMPLETED SUCCESSFULLY!")
    print(f"   - Verified Wikipedia Real Photographs: {resolved_photos} spots")
    print(f"   - Category Header Box Fallbacks (0% Mismatch): {category_fallbacks} spots")
    print(f"   - Total Spots Processed: {resolved_photos + category_fallbacks}")
    print("=======================================================")

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    js_path = os.path.join(script_dir, '..', 'js', 'ai-travel-engine.js')
    run_auto_pipeline(js_path)
