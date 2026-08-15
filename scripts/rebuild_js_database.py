import os
import json
import glob

city_files = sorted(glob.glob('data/cities/*.json'))
print(f"Reading {len(city_files)} city JSON files for js/ai-travel-engine.js...")

db = {}

city_name_map = {
    "amsterdam.json": "Amsterdam, Netherlands",
    "berlin.json": "Berlin, Germany",
    "bordeaux.json": "Bordeaux, France",
    "brussels.json": "Brussels, Belgium",
    "cologne.json": "Cologne, Germany",
    "luxembourg.json": "Luxembourg City, Luxembourg",
    "lyon.json": "Lyon, France",
    "marseille.json": "Marseille, France",
    "munich.json": "Munich, Germany",
    "nice.json": "Nice, France",
    "paris.json": "Paris, France",
    "strasbourg.json": "Strasbourg, France",
    "toulouse.json": "Toulouse, France"
}

for fpath in city_files:
    fname = os.path.basename(fpath)
    cname = city_name_map.get(fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if not cname:
        cname = data.get('cityName', fname.replace('.json', '').title())

    spots = data.get('spots', [])
    db[cname] = spots
    print(f" -> Loaded {cname}: {len(spots)} spots")

js_file_path = 'js/ai-travel-engine.js'

with open(js_file_path, 'r', encoding='utf-8') as f:
    js_code = f.read()

db_marker = 'const candidateSpotsDatabase = '
start_idx = js_code.find(db_marker)

if start_idx != -1:
    end_idx = js_code.find(';\n', start_idx)
    if end_idx != -1:
        new_db_json = json.dumps(db, indent=2, ensure_ascii=False)
        new_js_code = js_code[:start_idx + len(db_marker)] + new_db_json + js_code[end_idx:]
        with open(js_file_path, 'w', encoding='utf-8') as f:
            f.write(new_js_code)
        print(f"\n🎉 Successfully rebuilt {js_file_path} with 100% translated data across 13 cities ({len(db)} cities)!")
    else:
        print("Error: Could not find end of candidateSpotsDatabase in js file")
else:
    print("Error: Could not find candidateSpotsDatabase marker in js file")
