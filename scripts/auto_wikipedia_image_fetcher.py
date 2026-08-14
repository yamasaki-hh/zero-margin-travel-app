#!/usr/bin/env python3
"""
Zero-Margin Travel App - Ultra-Simple Wikipedia Image Resolver Pipeline
Clean, Robust, High-Coverage Architecture using Official Wikipedia REST Summary APIs
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
    'User-Agent': 'ZeroMarginTravelApp/7.0 (https://github.com/yamasaki-hh/zero-margin-travel-app; contact@yamasaki-travel.org)'
}

CITY_DEFAULT_LANG = {
    'Paris': 'fr',
    'Berlin': 'de',
    'Amsterdam': 'nl',
    'Brussels': 'fr',
    'Luxembourg': 'fr',
    'Cologne': 'de',
    'Munich': 'de'
}

# Wikipedia Article Title Slugs (Clean, direct Wikipedia API keys)
SPOT_WIKI_SLUGS = {
    # Paris
    'Eiffel Tower': [('fr', 'Tour_Eiffel'), ('en', 'Eiffel_Tower')],
    'Arc de Triomphe': [('fr', 'Arc_de_triomphe_de_l%27%C3%89toile'), ('en', 'Arc_de_Triomphe')],
    'Sainte-Chapelle': [('fr', 'Sainte-Chapelle'), ('en', 'Sainte-Chapelle')],
    'Sacré-Cœur Basilica & Montmartre': [('fr', 'Basilique_du_Sacr%C3%A9-C%C5%93ur_de_Montmartre'), ('en', 'Sacr%C3%A9-C%C5%93ur%2C_Paris')],
    'Notre-Dame Cathedral': [('fr', 'Cath%C3%A9drale_Notre-Dame_de_Paris'), ('en', 'Notre-Dame_de_Paris')],
    'Palais-Royal Courtyard & Gardens': [('fr', 'Palais-Royal'), ('en', 'Palais-Royal')],
    'Panthéon Paris': [('fr', 'Panth%C3%A9on_%28Paris%29'), ('en', 'Panth%C3%A9on')],
    'Jardin du Luxembourg': [('fr', 'Jardin_du_Luxembourg'), ('en', 'Jardin_du_Luxembourg')],
    'Opéra Garnier (Palais Garnier)': [('fr', 'Op%C3%A9ra_Garnier'), ('en', 'Palais_Garnier')],
    'Pont Alexandre III': [('fr', 'Pont_Alexandre-III'), ('en', 'Pont_Alexandre_III')],
    'Les Invalides & Napoleon\'s Tomb': [('fr', 'H%C3%B4tel_des_Invalides'), ('en', 'Les_Invalides')],
    'Pont des Arts': [('fr', 'Pont_des_Arts_%28Paris%29'), ('en', 'Pont_des_Arts')],
    'Catacombes de Paris': [('fr', 'Catacombes_de_Paris'), ('en', 'Paris_Catacombs')],
    'Louvre Museum & Glass Pyramid': [('fr', 'Mus%C3%A9e_du_Louvre'), ('en', 'Louvre')],
    'Musée d\'Orsay': [('fr', 'Mus%C3%A9e_d%27Orsay'), ('en', 'Mus%C3%A9e_d%27Orsay')],
    'Musée de l\'Orangerie': [('fr', 'Mus%C3%A9e_de_l%27Orangerie'), ('en', 'Mus%C3%A9e_de_l%27Orangerie')],
    'Centre Pompidou': [('fr', 'Centre_Georges-Pompidou'), ('en', 'Centre_Pompidou')],
    'Musée Rodin': [('fr', 'Mus%C3%A9e_Rodin'), ('en', 'Mus%C3%A9e_Rodin')],
    'Musée Picasso Paris': [('fr', 'Mus%C3%A9e_Picasso_%28Paris%29'), ('en', 'Mus%C3%A9e_Picasso')],
    'Musée Carnavalet': [('fr', 'Mus%C3%A9e_Carnavalet'), ('en', 'Mus%C3%A9e_Carnavalet')],
    'Café de Flore': [('fr', 'Caf%C3%A9_de_Flore'), ('en', 'Caf%C3%A9_de_Flore')],
    'Les Deux Magots': [('fr', 'Les_Deux_Magots'), ('en', 'Les_Deux_Magots')],
    'Le Procope': [('fr', 'Caf%C3%A9_Procope'), ('en', 'Caf%C3%A9_Procope')],
    'Le Train Bleu': [('fr', 'Le_Train_Bleu_%28restaurant%29'), ('en', 'Le_Train_Bleu_%28restaurant%29')],
    'Bouillon Chartier': [('fr', 'Bouillon_Chartier'), ('en', 'Bouillon_Chartier')],
    'Palace of Versailles (Château de Versailles)': [('fr', 'Ch%C3%A2teau_de_Versailles'), ('en', 'Palace_of_Versailles')],
    'Place de la Concorde & Champs-Élysées': [('fr', 'Place_de_la_Concorde'), ('en', 'Place_de_la_Concorde')],
    'Conciergerie': [('fr', 'Conciergerie'), ('en', 'Conciergerie')],
    'Place des Vosges': [('fr', 'Place_des_Vosges'), ('en', 'Place_des_Vosges')],
    'Musée Marmottan Monet': [('fr', 'Mus%C3%A9e_Marmottan_Monet'), ('en', 'Mus%C3%A9e_Marmottan_Monet')],
    'Fondation Louis Vuitton': [('fr', 'Fondation_Louis-Vuitton'), ('en', 'Fondation_Louis_Vuitton')],
    'Musée de Cluny (Middle Ages)': [('fr', 'Mus%C3%A9e_de_Cluny'), ('en', 'Mus%C3%A9e_de_Cluny')],
    'Musée du Quai Branly': [('fr', 'Mus%C3%A9e_du_Quai_Branly_-_Jacques-Chirac'), ('en', 'Mus%C3%A9e_du_quai_Branly')],
    'Covered Passages (Galerie Vivienne)': [('fr', 'Galerie_Vivienne'), ('en', 'Galerie_Vivienne')],
    'Galeries Lafayette Haussmann': [('fr', 'Galeries_Lafayette_Haussmann'), ('en', 'Galeries_Lafayette')],
    'Seine River Cruise (Bateaux-Mouches)': [('fr', 'Bateaux-mouches'), ('en', 'Bateaux_Mouches')],
    'Canal Saint-Martin': [('fr', 'Canal_Saint-Martin'), ('en', 'Canal_Saint-Martin')],

    # Berlin
    'Brandenburg Gate': [('de', 'Brandenburger_Tor'), ('en', 'Brandenburg_Gate')],
    'Reichstag Building Dome': [('de', 'Reichstagsgeb%C3%A4ude'), ('en', 'Reichstag_building')],
    'East Side Gallery Berlin Wall': [('de', 'East_Side_Gallery'), ('en', 'East_Side_Gallery')],
    'Berlin Cathedral (Berliner Dom)': [('de', 'Berliner_Dom'), ('en', 'Berlin_Cathedral')],
    'Charlottenburg Palace': [('de', 'Schloss_Charlottenburg'), ('en', 'Charlottenburg_Palace')],
    'Holocaust Memorial': [('de', 'Denkmal_f%C3%BCr_die_ermordeten_Juden_Europas'), ('en', 'Memorial_to_the_Murdered_Jews_of_Europe')],
    'Gendarmenmarkt Square': [('de', 'Gendarmenmarkt'), ('en', 'Gendarmenmarkt')],
    'Victory Column (Siegessäule)': [('de', 'Siegess%C3%A4ule_%28Berlin%29'), ('en', 'Berlin_Victory_Column')],
    'Berlin TV Tower (Fernsehturm)': [('de', 'Berliner_Fernsehturm'), ('en', 'Fernsehturm_Berlin')],
    'Checkpoint Charlie': [('de', 'Checkpoint_Charlie'), ('en', 'Checkpoint_Charlie')],
    'Kaiser Wilhelm Memorial Church': [('de', 'Kaiser-Wilhelm-Ged%C3%A4chtniskirche'), ('en', 'Kaiser_Wilhelm_Memorial_Church')],
    'Tiergarten Park': [('de', 'Gro%C3%9Fer_Tiergarten'), ('en', 'Tiergarten')],
    'Hackesche Höfe': [('de', 'Hackesche_H%C3%B6fe'), ('en', 'Hackesche_H%C3%B6fe')],
    'Museum Island Berlin': [('de', 'Museumsinsel_%28Berlin%29'), ('en', 'Museum_Island')],
    'Pergamon Museum': [('de', 'Pergamonmuseum'), ('en', 'Pergamon_Museum')],
    'Neues Museum (Nefertiti Bust)': [('de', 'Neues_Museum_%28Berlin%29'), ('en', 'Neues_Museum')],
    'Jewish Museum Berlin': [('de', 'J%C3%BCdisches_Museum_Berlin'), ('en', 'Jewish_Museum_Berlin')],
    'Hamburger Bahnhof': [('de', 'Hamburger_Bahnhof_%E2%80%93_Nationalgalerie_der_Gegenwart'), ('en', 'Hamburger_Bahnhof')],
    'Topography of Terror': [('de', 'Topographie_des_Terrors'), ('en', 'Topography_of_Terror')],
    'DDR Museum': [('de', 'DDR_Museum'), ('en', 'DDR_Museum')],

    # Amsterdam
    'Rijksmuseum': [('nl', 'Rijksmuseum_Amsterdam'), ('en', 'Rijksmuseum')],
    'Van Gogh Museum': [('nl', 'Van_Gogh_Museum'), ('en', 'Van_Gogh_Museum')],
    'Anne Frank House': [('nl', 'Anne_Frank_Huis'), ('en', 'Anne_Frank_House')],
    'Zaanse Schans Windmills': [('nl', 'Zaanse_Schans'), ('en', 'Zaanse_Schans')],
    'Vondelpark': [('nl', 'Vondelpark'), ('en', 'Vondelpark')],
    'Royal Palace of Amsterdam': [('nl', 'Paleis_op_de_Dam'), ('en', 'Royal_Palace_of_Amsterdam')],
    'Oude Kerk': [('nl', 'Oude_Kerk_%28Amsterdam%29'), ('en', 'Oude_Kerk_%28Amsterdam%29')],
    'Begijnhof Courtyard': [('nl', 'Begijnhof_%28Amsterdam%29'), ('en', 'Begijnhof%2C_Amsterdam')],
    'Bloemenmarkt (Floating Flower Market)': [('nl', 'Bloemenmarkt_%28Amsterdam%29'), ('en', 'Bloemenmarkt')],
    'Stedelijk Museum Amsterdam': [('nl', 'Stedelijk_Museum_Amsterdam'), ('en', 'Stedelijk_Museum_Amsterdam')],
    'Rembrandt House Museum': [('nl', 'Museum_Het_Rembrandthuis'), ('en', 'Rembrandt_House_Museum')],
    'NEMO Science Museum': [('nl', 'NEMO_%28Amsterdam%29'), ('en', 'NEMO_Science_Museum')],
    'MOCO Museum': [('nl', 'Moco_Museum'), ('en', 'MOCO_Museum')],
    'Brouwerij \'t IJ': [('nl', 'Brouwerij_%27t_IJ'), ('en', 'Brouwerij_%27t_IJ')],

    # Brussels
    'Grand-Place': [('fr', 'Grand-Place_de_Bruxelles'), ('en', 'Grand_Place')],
    'Royal Gallery of Saint-Hubert': [('fr', 'Galeries_royales_Saint-Hubert'), ('en', 'Royal_Galaxies_of_Saint-Hubert')],
    'Atomium': [('fr', 'Atomium'), ('en', 'Atomium')],
    'St. Michael & St. Gudula Cathedral': [('fr', 'Cath%C3%A9drale_Saints-Michel-et-Gudule_de_Bruxelles'), ('en', 'Cathedral_of_St._Michael_and_St._Gudula')],
    'Mont des Arts': [('fr', 'Mont_des_Arts'), ('en', 'Mont_des_Arts')],
    'Cinquantenaire Arch & Park': [('fr', 'Parc_du_Cinquantenaire'), ('en', 'Parc_du_Cinquantenaire')],
    'Manneken Pis': [('fr', 'Manneken-Pis'), ('en', 'Manneken_Pis')],
    'Magritte Museum': [('fr', 'Mus%C3%A9e_Magritte'), ('en', 'Magritte_Museum')],

    # Luxembourg
    'Bock Casemates': [('fr', 'Casemates_du_Bock'), ('en', 'Bock_%28Luxembourg%29')],
    'Chemin de la Corniche': [('fr', 'Chemin_de_la_Corniche_%28Luxembourg%29'), ('en', 'Chemin_de_la_Corniche')],
    'Grund Valley District': [('fr', 'Grund_%28Luxembourg%29'), ('en', 'Grund_%28Luxembourg%29')],
    'Grand Ducal Palace': [('fr', 'Palais_grand-ducal'), ('en', 'Grand_Ducal_Palace%2C_Luxembourg')],
    'Notre-Dame Cathedral Luxembourg': [('fr', 'Cath%C3%A9drale_Notre-Dame_de_Luxembourg'), ('en', 'Notre-Dame_Cathedral%2C_Luxembourg')],
    'Mudam Luxembourg': [('fr', 'Mus%C3%A9e_d%27art_moderne_Grand-Duc_Jean'), ('en', 'Mudam')],
    'MNHA Museum': [('fr', 'Mus%C3%A9e_national_d%27histoire_et_d%27art'), ('en', 'National_Museum_of_History_and_Art')],

    # Cologne
    'Cologne Cathedral (Kölner Dom)': [('de', 'K%C3%B6lner_Dom'), ('en', 'Cologne_Cathedral')],
    'Hohenzollern Bridge (Love Locks)': [('de', 'Hohenzollernbr%C3%BCcke'), ('en', 'Hohenzollern_Bridge')],
    'Great St. Martin Church': [('de', 'Gro%C3%9F_St._Martin'), ('en', 'Great_St._Martin_Church%2C_Cologne')],
    'Cologne Chocolate Museum': [('de', 'Imhoff-Schokoladenmuseum'), ('en', 'Imhoff-Schokoladenmuseum')],
    'Museum Ludwig': [('de', 'Museum_Ludwig'), ('en', 'Museum_Ludwig')],

    # Munich
    'Marienplatz & New Town Hall': [('de', 'Neues_Rathaus_%28M%C3%BCnchen%29'), ('en', 'Marienplatz')],
    'English Garden & Eisbachwave': [('de', 'Englischer_Garten_%28M%C3%BCnchen%29'), ('en', 'Englischer_Garten')],
    'Nymphenburg Palace': [('de', 'Schloss_Nymphenburg'), ('en', 'Nymphenburg_Palace')],
    'Munich Residenz': [('de', 'M%C3%BCnchner_Residenz'), ('en', 'Munich_Residenz')],
    'Frauenkirche (Cathedral of Our Dear Lady)': [('de', 'Frauenkirche_%28M%C3%BCnchen%29'), ('en', 'Munich_Frauenkirche')],
    'BMW Welt & BMW Museum': [('de', 'BMW_Welt'), ('en', 'BMW_Welt')],
    'Deutsches Museum': [('de', 'Deutsches_Museum'), ('en', 'Deutsches_Museum')],
    'Pinakothek Museums (Alte & Neue)': [('de', 'Alte_Pinakothek'), ('en', 'Alte_Pinakothek')],
    'Viktualienmarkt': [('de', 'Viktualienmarkt'), ('en', 'Viktualienmarkt')],
    'Neuschwanstein Castle Day Trip': [('de', 'Schloss_Neuschwanstein'), ('en', 'Neuschwanstein_Castle')]
}

def is_valid_thumbnail(url):
    if not url: return False
    l = url.lower()
    return not ('.svg' in l or 'logo' in l or 'flag' in l or 'blason' in l or 'map' in l or 'carte' in l or 'coat_of_arms' in l)

def fetch_wiki_summary_photo(lang, slug):
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

def run_simple_resolver_pipeline(js_file_path):
    print("🚀 Launching Ultra-Simple Wikipedia REST API Resolver Pipeline...")
    with open(js_file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    db_match = re.search(r'const candidateSpotsDatabase = (\{[\s\S]*?\n\};)', code)
    if not db_match:
        print("❌ Error: candidateSpotsDatabase not found in JS file!")
        return

    db_json_str = db_match.group(1).rstrip(';')
    db_data = json.loads(db_json_str)

    photo_cnt = 0
    fallback_cnt = 0

    for city, spots in db_data.items():
        clean_city = city.split(',')[0].strip()
        default_lang = CITY_DEFAULT_LANG.get(clean_city, 'en')
        print(f"\n📍 City: {city} ({len(spots)} spots)...")
        
        for spot in spots:
            name = spot['name']
            slug_candidates = SPOT_WIKI_SLUGS.get(name, [])
            
            # Auto fallback slug generation if not explicitly in map
            if not slug_candidates:
                clean_name = name.split(' (')[0].strip().replace(' ', '_')
                slug_candidates = [(default_lang, urllib.parse.quote(clean_name)), ('en', urllib.parse.quote(clean_name))]
                
            photo_url = ""
            matched_lang = ""
            for lang, slug in slug_candidates:
                photo_url = fetch_wiki_summary_photo(lang, slug)
                if photo_url:
                    matched_lang = lang
                    break
                time.sleep(0.01)

            if photo_url:
                spot['image'] = photo_url
                spot['hasWiki'] = True
                photo_cnt += 1
                print(f"  ✅ [Summary {matched_lang}] \"{name}\" -> {photo_url[:60]}...")
            else:
                spot['image'] = ""
                spot['hasWiki'] = False
                fallback_cnt += 1
                print(f"  🏷️ [Category Header Box] \"{name}\"")
                
            time.sleep(0.01)

    new_db_json = json.dumps(db_data, indent=2, ensure_ascii=False)
    new_code = code[:db_match.start(1)] + new_db_json + ';\n' + code[db_match.end(1):]

    with open(js_file_path, 'w', encoding='utf-8') as f:
        f.write(new_code)

    print("\n=======================================================")
    print(f"🎉 ULTRA-SIMPLE PIPELINE COMPLETED SUCCESSFULLY!")
    print(f"   - Verified Wikipedia Summary Photos: {photo_cnt} spots")
    print(f"   - Category Header Box Fallbacks (0% Mismatch): {fallback_cnt} spots")
    print(f"   - Total Spots Processed: {photo_cnt + fallback_cnt}")
    print("=======================================================")

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    js_path = os.path.join(script_dir, '..', 'js', 'ai-travel-engine.js')
    run_simple_resolver_pipeline(js_path)
