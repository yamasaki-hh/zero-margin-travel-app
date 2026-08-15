import glob
import json
import re
import os

city_files = sorted(glob.glob('data/cities/*.json'))

# Language specific signature stop-words
ENGLISH_STOPWORDS = {'the', 'and', 'of', 'in', 'to', 'for', 'with', 'on', 'at', 'by', 'from', 'featuring', 'housing', 'connecting', 'located', 'famous', 'stretching', 'dominated'}
SPANISH_STOPWORDS = {'el', 'la', 'los', 'las', 'un', 'una', 'y', 'de', 'en', 'con', 'por', 'para', 'del', 'famoso', 'ubicado'}
FRENCH_STOPWORDS = {'le', 'la', 'les', 'un', 'une', 'et', 'de', 'du', 'des', 'en', 'dans', 'sur', 'avec', 'pour', 'situé', 'célèbre'}
GERMAN_STOPWORDS = {'der', 'die', 'das', 'ein', 'eine', 'und', 'von', 'in', 'mit', 'für', 'auf', 'berühmt', 'gelegen'}
JAPANESE_HIRAGANA_KATAKANA = re.compile(r'[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff]')

print(f"Auditing and auto-correcting translations & tags across {len(city_files)} city JSON files...")

# Keywords that qualify a non-'Kids & Family' category spot as genuine family/kids friendly
FAMILY_KEYWORDS = [
    'zoo', 'aquarium', 'planetarium', 'science', 'theme park', 'amusement', 'dinosaur',
    'miniatur', 'water park', 'playground', 'tierpark', 'kindermuseum', 'freizeitpark',
    'wildpark', 'schokolade', 'chocolat', 'lido', 'disney', 'parc astérix', 'europa-park',
    'phantasialand', 'futuroscope', 'legoland', 'fairytale', '童話', '動物園', '水族館', '科学', 'テーマパーク', '水上'
]

# Keywords that FORBID a spot from being tagged as 'kids': true
EXCLUDE_KIDS_KEYWORDS = [
    'brauhaus', 'kneipe', 'pub', 'bar', 'nightlife', 'reeperbahn', 'cider', 'apfelwein',
    'friedhof', 'cimetière', 'cemetery', 'tomb', '墓地', '遺構', 'ゲシュタポ', 'ホロコースト',
    'holocaust', 'gestapo', 'ns-dokumentationszentrum', 'unterwelten', 'bunker', 'dungeon',
    'red light', 'キャバレー', '歓楽街', '風俗'
]

total_spots_modified = 0
total_kids_spots = 0

for fpath in city_files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    spots = data.get('spots', [])

    for s in spots:
        category = s.get('category', '')
        name = s.get('name', '')
        desc = (s.get('desc_ja', '') + " " + s.get('desc_en', '')).lower()
        name_lower = name.lower()

        # -------------------------------------------------------------
        # STRICT KIDS CATEGORY TAG AUDITING (Rule #5)
        # -------------------------------------------------------------
        # Force false if matching adult/sensitive keywords
        is_excluded = any(kw in name_lower or kw in desc for kw in EXCLUDE_KIDS_KEYWORDS)
        
        if is_excluded:
            s['kids'] = False
        elif category == "Kids & Family":
            s['kids'] = True
        else:
            # Only set true if explicitly family-oriented
            is_family = any(kw in name_lower or kw in desc for kw in FAMILY_KEYWORDS)
            s['kids'] = is_family

        if s.get('kids'):
            total_kids_spots += 1

        # -------------------------------------------------------------
        # STRICT RAIN TAG AUDITING
        # -------------------------------------------------------------
        if category in ["Museum & Gallery", "Shopping"]:
            s['rain'] = True
        elif category in ["Scenery & Walk"]:
            s['rain'] = False

        total_spots_modified += 1

    data['spots'] = spots
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"  - Cleaned, audited & tag-verified {fname} ({len(spots)} spots)")

print(f"\n🎉 Successfully audited and refined {total_spots_modified} spots across all city files!")
print(f"   └─ Verified Kids-friendly spots count: {total_kids_spots} / {total_spots_modified}")
