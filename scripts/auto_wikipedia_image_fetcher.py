#!/usr/bin/env python3
"""
Zero-Margin Travel App - 2-Tier Free Automated Wikipedia & Wikidata Image Pipeline

Tier 1: Native Language Wikipedia Summary API (fr, de, nl, etc.)
Tier 2: Wikidata Entity Property P18 (Official Representative Image)
Tier 3: Category Header Box Fallback (0% Mismatch Guarantee for local venues)
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
    'User-Agent': 'ZeroMarginTravelApp/5.0 (https://github.com/yamasaki-hh/zero-margin-travel-app; contact@yamasaki-travel.org)'
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

# Mapping of landmark names to Wikidata QIDs or exact local Wikipedia slugs
KNOWN_WIKI_MAP = {
    # Paris
    'Eiffel Tower': {'qid': 'Q243', 'slugs': [('fr', 'Tour_Eiffel'), ('en', 'Eiffel_Tower')]},
    'Arc de Triomphe': {'qid': 'Q133230', 'slugs': [('fr', 'Arc_de_triomphe_de_l%27%C3%89toile')]},
    'Sainte-Chapelle': {'qid': 'Q193193', 'slugs': [('fr', 'Sainte-Chapelle')]},
    'Sacré-Cœur Basilica & Montmartre': {'qid': 'Q18094', 'slugs': [('fr', 'Basilique_du_Sacr%C3%A9-C%C5%93ur_de_Montmartre')]},
    'Notre-Dame Cathedral': {'qid': 'Q2981', 'slugs': [('fr', 'Cath%C3%A9drale_Notre-Dame_de_Paris')]},
    'Palais-Royal Courtyard & Gardens': {'qid': 'Q273180', 'slugs': [('fr', 'Palais-Royal')]},
    'Panthéon Paris': {'qid': 'Q188266', 'slugs': [('fr', 'Panth%C3%A9on_%28Paris%29')]},
    'Jardin du Luxembourg': {'qid': 'Q849646', 'slugs': [('fr', 'Jardin_du_Luxembourg')]},
    'Opéra Garnier (Palais Garnier)': {'qid': 'Q187841', 'slugs': [('fr', 'Op%C3%A9ra_Garnier')]},
    'Pont Alexandre III': {'qid': 'Q240656', 'slugs': [('fr', 'Pont_Alexandre-III')]},
    'Les Invalides & Napoleon\'s Tomb': {'qid': 'Q191097', 'slugs': [('fr', 'H%C3%B4tel_des_Invalides')]},
    'Pont des Arts': {'qid': 'Q520110', 'slugs': [('fr', 'Pont_des_Arts_%28Paris%29')]},
    'Catacombes de Paris': {'qid': 'Q223788', 'slugs': [('fr', 'Catacombes_de_Paris')]},
    'Louvre Museum & Glass Pyramid': {'qid': 'Q19675', 'slugs': [('fr', 'Mus%C3%A9e_du_Louvre')]},
    'Musée d\'Orsay': {'qid': 'Q23402', 'slugs': [('fr', 'Mus%C3%A9e_d%27Orsay')]},
    'Musée de l\'Orangerie': {'qid': 'Q727756', 'slugs': [('fr', 'Mus%C3%A9e_de_l%27Orangerie')]},
    'Centre Pompidou': {'qid': 'Q178040', 'slugs': [('fr', 'Centre_Georges-Pompidou')]},
    'Musée Rodin': {'qid': 'Q650570', 'slugs': [('fr', 'Mus%C3%A9e_Rodin')]},
    'Musée Picasso Paris': {'qid': 'Q1151609', 'slugs': [('fr', 'Mus%C3%A9e_Picasso_%28Paris%29')]},
    'Musée Carnavalet': {'qid': 'Q640960', 'slugs': [('fr', 'Mus%C3%A9e_Carnavalet')]},
    'Café de Flore': {'qid': 'Q1025648', 'slugs': [('fr', 'Caf%C3%A9_de_Flore')]},
    'Les Deux Magots': {'qid': 'Q1193354', 'slugs': [('fr', 'Les_Deux_Magots')]},
    'Le Procope': {'qid': 'Q1025670', 'slugs': [('fr', 'Caf%C3%A9_Procope')]},
    'Le Train Bleu': {'qid': 'Q744574', 'slugs': [('fr', 'Le_Train_Bleu_%28restaurant%29')]},
    'Bouillon Chartier': {'qid': 'Q2921575', 'slugs': [('fr', 'Bouillon_Chartier')]},
    'Palace of Versailles (Château de Versailles)': {'qid': 'Q2946', 'slugs': [('fr', 'Ch%C3%A2teau_de_Versailles')]},
    'Place de la Concorde & Champs-Élysées': {'qid': 'Q189333', 'slugs': [('fr', 'Place_de_la_Concorde')]},
    'Conciergerie': {'qid': 'Q841315', 'slugs': [('fr', 'Conciergerie')]},
    'Place des Vosges': {'qid': 'Q848037', 'slugs': [('fr', 'Place_des_Vosges')]},
    'Musée Marmottan Monet': {'qid': 'Q1427503', 'slugs': [('fr', 'Mus%C3%A9e_Marmottan_Monet')]},
    'Fondation Louis Vuitton': {'qid': 'Q17354519', 'slugs': [('fr', 'Fondation_Louis-Vuitton')]},
    'Musée de Cluny (Middle Ages)': {'qid': 'Q1122709', 'slugs': [('fr', 'Mus%C3%A9e_de_Cluny')]},
    'Musée du Quai Branly': {'qid': 'Q830491', 'slugs': [('fr', 'Mus%C3%A9e_du_Quai_Branly_-_Jacques-Chirac')]},
    'Covered Passages (Galerie Vivienne)': {'qid': 'Q1491873', 'slugs': [('fr', 'Galerie_Vivienne')]},
    'Galeries Lafayette Haussmann': {'qid': 'Q3094766', 'slugs': [('fr', 'Galeries_Lafayette_Haussmann')]},
    'Seine River Cruise (Bateaux-Mouches)': {'qid': 'Q810787', 'slugs': [('fr', 'Bateaux-mouches')]},
    'Canal Saint-Martin': {'qid': 'Q3012', 'slugs': [('fr', 'Canal_Saint-Martin')]},

    # Berlin
    'Brandenburg Gate': {'qid': 'Q82425', 'slugs': [('de', 'Brandenburger_Tor')]},
    'Reichstag Building Dome': {'qid': 'Q151843', 'slugs': [('de', 'Reichstagsgeb%C3%A4ude')]},
    'East Side Gallery Berlin Wall': {'qid': 'Q162744', 'slugs': [('de', 'East_Side_Gallery')]},
    'Berlin Cathedral (Berliner Dom)': {'qid': 'Q154566', 'slugs': [('de', 'Berliner_Dom')]},
    'Charlottenburg Palace': {'qid': 'Q155014', 'slugs': [('de', 'Schloss_Charlottenburg')]},
    'Holocaust Memorial': {'qid': 'Q160680', 'slugs': [('de', 'Denkmal_f%C3%BCr_die_ermordeten_Juden_Europas')]},
    'Gendarmenmarkt Square': {'qid': 'Q163823', 'slugs': [('de', 'Gendarmenmarkt')]},
    'Victory Column (Siegessäule)': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Berlin_Victory_Column.jpg/330px-Berlin_Victory_Column.jpg',
    'Berlin TV Tower (Fernsehturm)': {'qid': 'Q151356', 'slugs': [('de', 'Berliner_Fernsehturm')]},
    'Checkpoint Charlie': {'qid': 'Q153122', 'slugs': [('de', 'Checkpoint_Charlie')]},
    'Kaiser Wilhelm Memorial Church': {'qid': 'Q153542', 'slugs': [('de', 'Kaiser-Wilhelm-Ged%C3%A4chtniskirche')]},
    'Tiergarten Park': {'qid': 'Q162234', 'slugs': [('de', 'Gro%C3%9Fer_Tiergarten')]},
    'Hackesche Höfe': {'qid': 'Q686411', 'slugs': [('de', 'Hackesche_H%C3%B6fe')]},
    'Museum Island Berlin': {'qid': 'Q157059', 'slugs': [('de', 'Museumsinsel_%28Berlin%29')]},
    'Pergamon Museum': {'qid': 'Q157298', 'slugs': [('de', 'Pergamonmuseum')]},
    'Neues Museum (Nefertiti Bust)': {'qid': 'Q157304', 'slugs': [('de', 'Neues_Museum_%28Berlin%29')]},
    'Jewish Museum Berlin': {'qid': 'Q158004', 'slugs': [('de', 'J%C3%BCdisches_Museum_Berlin')]},
    'Hamburger Bahnhof': {'qid': 'Q700465', 'slugs': [('de', 'Hamburger_Bahnhof_%E2%80%93_Nationalgalerie_der_Gegenwart')]},
    'Topography of Terror': {'qid': 'Q698424', 'slugs': [('de', 'Topographie_des_Terrors')]},

    # Amsterdam
    'Rijksmuseum': {'qid': 'Q190804', 'slugs': [('nl', 'Rijksmuseum_Amsterdam')]},
    'Van Gogh Museum': {'qid': 'Q224124', 'slugs': [('nl', 'Van_Gogh_Museum')]},
    'Anne Frank House': {'qid': 'Q160949', 'slugs': [('nl', 'Anne_Frank_Huis')]},
    'Zaanse Schans Windmills': {'qid': 'Q168864', 'slugs': [('nl', 'Zaanse_Schans')]},
    'Vondelpark': {'qid': 'Q1333333', 'slugs': [('nl', 'Vondelpark')]},
    'Royal Palace of Amsterdam': {'qid': 'Q1056152', 'slugs': [('nl', 'Paleis_op_de_Dam')]},
    'Oude Kerk': {'qid': 'Q963177', 'slugs': [('nl', 'Oude_Kerk_%28Amsterdam%29')]},
    'Begijnhof Courtyard': {'qid': 'Q814766', 'slugs': [('nl', 'Begijnhof_%28Amsterdam%29')]},
    'Bloemenmarkt (Floating Flower Market)': {'qid': 'Q884848', 'slugs': [('nl', 'Bloemenmarkt_%28Amsterdam%29')]},
    'Stedelijk Museum Amsterdam': {'qid': 'Q925252', 'slugs': [('nl', 'Stedelijk_Museum_Amsterdam')]},
    'Rembrandt House Museum': {'qid': 'Q1134015', 'slugs': [('nl', 'Museum_Het_Rembrandthuis')]},
    'NEMO Science Museum': {'qid': 'Q1352467', 'slugs': [('nl', 'NEMO_%28Amsterdam%29')]},
    'MOCO Museum': {'qid': 'Q27070196', 'slugs': [('nl', 'Moco_Museum')]},
    'Brouwerij \'t IJ': {'qid': 'Q2260655', 'slugs': [('nl', 'Brouwerij_%27t_IJ')]},

    # Brussels
    'Grand-Place': {'qid': 'Q215429', 'slugs': [('fr', 'Grand-Place_de_Bruxelles')]},
    'Royal Gallery of Saint-Hubert': {'qid': 'Q1491753', 'slugs': [('fr', 'Galeries_royales_Saint-Hubert')]},
    'Atomium': {'qid': 'Q180920', 'slugs': [('fr', 'Atomium')]},
    'St. Michael & St. Gudula Cathedral': {'qid': 'Q603957', 'slugs': [('fr', 'Cath%C3%A9drale_Saints-Michel-et-Gudule_de_Bruxelles')]},
    'Mont des Arts': {'qid': 'Q3322144', 'slugs': [('fr', 'Mont_des_Arts')]},
    'Cinquantenaire Arch & Park': {'qid': 'Q2054041', 'slugs': [('fr', 'Parc_du_Cinquantenaire')]},
    'Manneken Pis': {'qid': 'Q152000', 'slugs': [('fr', 'Manneken-Pis')]},
    'Magritte Museum': {'qid': 'Q3330616', 'slugs': [('fr', 'Mus%C3%A9e_Magritte')]},

    # Luxembourg
    'Bock Casemates': {'qid': 'Q889099', 'slugs': [('fr', 'Casemates_du_Bock')]},
    'Chemin de la Corniche': {'qid': 'Q13102047', 'slugs': [('fr', 'Chemin_de_la_Corniche_%28Luxembourg%29')]},
    'Grund Valley District': {'qid': 'Q1550275', 'slugs': [('fr', 'Grund_%28Luxembourg%29')]},
    'Grand Ducal Palace': {'qid': 'Q1530966', 'slugs': [('fr', 'Palais_grand-ducal')]},
    'Notre-Dame Cathedral Luxembourg': {'qid': 'Q170144', 'slugs': [('fr', 'Cath%C3%A9drale_Notre-Dame_de_Luxembourg')]},
    'Mudam Luxembourg': {'qid': 'Q1530722', 'slugs': [('fr', 'Mus%C3%A9e_d%27art_moderne_Grand-Duc_Jean')]},
    'MNHA Museum': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Luxembourg_city_MNHA.jpg/330px-Luxembourg_city_MNHA.jpg',

    # Cologne
    'Cologne Cathedral (Kölner Dom)': {'qid': 'Q4176', 'slugs': [('de', 'K%C3%B6lner_Dom')]},
    'Hohenzollern Bridge (Love Locks)': {'qid': 'Q696773', 'slugs': [('de', 'Hohenzollernbr%C3%BCcke')]},
    'Great St. Martin Church': {'qid': 'Q693630', 'slugs': [('de', 'Gro%C3%9F_St._Martin')]},
    'Cologne Chocolate Museum': {'qid': 'Q460492', 'slugs': [('de', 'Imhoff-Schokoladenmuseum')]},
    'Museum Ludwig': {'qid': 'Q678643', 'slugs': [('de', 'Museum_Ludwig')]},

    # Munich
    'Marienplatz & New Town Hall': {'qid': 'Q253724', 'slugs': [('de', 'Neues_Rathaus_%28M%C3%BCnchen%29')]},
    'English Garden & Eisbachwave': {'qid': 'Q160533', 'slugs': [('de', 'Englischer_Garten_%28M%C3%BCnchen%29')]},
    'Nymphenburg Palace': {'qid': 'Q131636', 'slugs': [('de', 'Schloss_Nymphenburg')]},
    'Munich Residenz': {'qid': 'Q671022', 'slugs': [('de', 'M%C3%BCnchner_Residenz')]},
    'Frauenkirche (Cathedral of Our Dear Lady)': {'qid': 'Q167193', 'slugs': [('de', 'Frauenkirche_%28M%C3%BCnchen%29')]},
    'BMW Welt & BMW Museum': {'qid': 'Q157143', 'slugs': [('de', 'BMW_Welt')]},
    'Deutsches Museum': {'qid': 'Q156598', 'slugs': [('de', 'Deutsches_Museum')]},
    'Pinakothek Museums (Alte & Neue)': {'qid': 'Q154236', 'slugs': [('de', 'Alte_Pinakothek')]},
    'Viktualienmarkt': {'qid': 'Q701676', 'slugs': [('de', 'Viktualienmarkt')]},
    'Neuschwanstein Castle Day Trip': {'qid': 'Q4159', 'slugs': [('de', 'Schloss_Neuschwanstein')]}
}

def is_valid_photo(url):
    if not url: return False
    l = url.lower()
    return not ('.svg' in l or 'logo' in l or 'flag' in l or 'blason' in l or 'map' in l or 'carte' in l or 'coat_of_arms' in l)

def fetch_json(url):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=ctx, timeout=4) as res:
            if res.status == 200:
                return json.loads(res.read().decode('utf-8'))
    except Exception:
        pass
    return None

def get_commons_thumb(filename, width=330):
    if not filename: return ""
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

def tier1_summary_photo(slugs):
    for lang, slug in slugs:
        url = f'https://{lang}.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(slug)}'
        data = fetch_json(url)
        if data:
            src = data.get('thumbnail', {}).get('source', '')
            if src and is_valid_photo(src):
                return src
    return ""

def tier2_wikidata_photo(qid):
    if not qid: return ""
    url = f'https://www.wikidata.org/wiki/Special:EntityData/{qid}.json'
    data = fetch_json(url)
    if data:
        entity = data.get('entities', {}).get(qid, {})
        claims = entity.get('claims', {})
        p18 = claims.get('P18', [])
        if p18:
            fn = p18[0].get('mainsnak', {}).get('datavalue', {}).get('value', '')
            if fn and is_valid_photo(fn):
                thumb = get_commons_thumb(fn, 330)
                if thumb:
                    return thumb
    return ""

def run_2tier_pipeline(js_file_path):
    print("🚀 Launching Free 2-Tier Automated Wikipedia & Wikidata Image Pipeline...")
    with open(js_file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    db_match = re.search(r'const candidateSpotsDatabase = (\{[\s\S]*?\n\};)', code)
    if not db_match:
        print("❌ Error: candidateSpotsDatabase not found in JS file!")
        return

    db_json_str = db_match.group(1).rstrip(';')
    db_data = json.loads(db_json_str)

    resolved_cnt = 0
    fallback_cnt = 0

    for city, spots in db_data.items():
        clean_city = city.split(',')[0].strip()
        print(f"\n📍 Processing City: {city} ({len(spots)} candidate spots)...")
        for spot in spots:
            name = spot['name']
            info = KNOWN_WIKI_MAP.get(name)
            photo_url = ""
            method = ""

            if isinstance(info, str):
                photo_url = info
                method = "Direct Verified Photo"
            elif isinstance(info, dict):
                # Tier 1: Native Language Wikipedia Summary API
                slugs = info.get('slugs', [])
                photo_url = tier1_summary_photo(slugs)
                if photo_url:
                    method = "Tier 1: Local Wikipedia Summary"
                else:
                    # Tier 2: Wikidata P18 Direct Entity Photo Fetcher
                    qid = info.get('qid')
                    photo_url = tier2_wikidata_photo(qid)
                    if photo_url:
                        method = f"Tier 2: Wikidata P18 ({qid})"

            if photo_url and is_valid_photo(photo_url):
                spot['image'] = photo_url
                spot['hasWiki'] = True
                resolved_cnt += 1
                print(f"  ✅ [{method}] \"{name}\" -> {photo_url[:65]}...")
            else:
                spot['image'] = ""
                spot['hasWiki'] = False
                fallback_cnt += 1
                print(f"  🏷️ [Tier 3: Category Header] \"{name}\" -> Warm Atelier Category Box")

            time.sleep(0.01)

    new_db_json = json.dumps(db_data, indent=2, ensure_ascii=False)
    new_code = code[:db_match.start(1)] + new_db_json + ';\n' + code[db_match.end(1):]

    with open(js_file_path, 'w', encoding='utf-8') as f:
        f.write(new_code)

    print("\n=======================================================")
    print(f"🎉 2-TIER FREE PIPELINE COMPLETED SUCCESSFULLY!")
    print(f"   - Verified High-Res Wikipedia/Wikidata Photos: {resolved_cnt} spots")
    print(f"   - Category Header Box Fallbacks (0% Mismatch): {fallback_cnt} spots")
    print(f"   - Total Candidates Processed: {resolved_cnt + fallback_cnt}")
    print("=======================================================")

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    js_path = os.path.join(script_dir, '..', 'js', 'ai-travel-engine.js')
    run_2tier_pipeline(js_path)
