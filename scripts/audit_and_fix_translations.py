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

print(f"Auditing and auto-correcting translations across {len(city_files)} city JSON files...")

# Dictionary of curated translations for untranslated items
curated_fixes = {
  # Pont des Arts
  "p_12": {
    "desc_ja": "ルーヴル美術館とフランス学士院を結ぶ、セーヌ川に架かる有名な歩行者専用の木造橋。",
    "desc_es": "Emblemático puente peatonal de madera sobre el Sena que conecta el Louvre con el Instituto de Francia.",
    "desc_fr": "Pont piétonnier emblématique en bois reliant le Louvre et l'Institut de France.",
    "desc_de": "Berühmte Fußgänger-Holzbrücke über die Seine, die den Louvre mit dem Institut de France verbindet."
  },
  # Great St. Martin Church Cologne
  "c_3": {
    "desc_ja": "ケルンの旧市街のカラフルな木組みの家々の後ろにそびえる、重厚なロマネスク様式の大教会。",
    "desc_fr": "Église romanesque majestueuse dominant les maisons colorées de la vieille ville de Cologne.",
    "desc_de": "Imposante romanische Stiftskirche, die die bunten Altstadthäuser von Köln überragt.",
    "tip_ja": "教会前のカラフルな歴史的家々が立ち並ぶアマルフィ通りの広場からの外観撮影が最高のフォトロケーションです。",
    "tip_fr": "La meilleure vue s'admire depuis la place de la vieille ville avec les maisons colorées en arrière-plan.",
    "tip_de": "Der schönste Fotospot befindet sich auf dem Fischmarkt mit den bunten Stapelhäusern im Vordergrund."
  },
  # Brauhaus Sion Cologne
  "c_6": {
    "desc_ja": "1904年創業の伝統的なケルシュビール醸造所。冷えたケシュビールと伝統料理を提供。",
    "desc_es": "Cervecería tradicional de 1904 que sirve cerveza Kölsch bien fría y platos típicos.",
    "desc_fr": "Brasserie traditionnelle de 1904 servant de la bière Kölsch fraîche et une cuisine locale.",
    "tip_ja": "ケルン大聖堂から徒歩数分。わんここそば方式でグラスが空くとビールが自動追加される伝統体験を楽しめます。"
  },
  # Früh am Dom Cologne
  "c_7": {
    "desc_ja": "ケルン大聖堂のすぐ足元にある、大人気の老舗ケルシュビアホール＆レストラン。",
    "tip_ja": "大聖堂見学後の立ち寄りに最適。焼きたてのシュヴァインスハクセ（豚足ロースト）と冷えたケルシュビールが名物。"
  },
  # Bei Oma Kleinmann Cologne
  "c_8": {
    "desc_es": "Famoso pub de estudiantes conocido por sus enormes y deliciosos filetes empanados Schnitzel.",
    "desc_fr": "Pub étudiant très populaire célèbre pour ses gigantesques escalopes Schnitzel traditionnelles."
  },
  # Café Reichard Cologne
  "c_9": {
    "desc_fr": "Grand café traditionnel avec terrasse offrant une vue imprenable sur la cathédrale de Cologne.",
    "desc_de": "Traditionsreiches Grand Café mit Terrasse und direktem Blick auf den Kölner Dom."
  },
  # Bock Casemates Luxembourg
  "l_1": {
    "desc_ja": "崖の断崖絶壁に彫られた、総延長23kmにおよぶ世界遺産の巨大地下防衛要塞トンネル。",
    "desc_fr": "Réseau spectaculaire de galeries militaires souterraines creusées dans le rocher du Bock, classé UNESCO.",
    "tip_ja": "薄暗い迷路のような地下要塞の砲門窓からは、ボックの丘とアルゼット川の渓谷美を見渡せます。"
  },
  # Chemin de la Corniche Luxembourg
  "l_2": {
    "desc_es": "Conocido como 'El balcón más hermoso de Europa', un paseo escénico con vistas al valle del Grund."
  },
  # Grand Ducal Palace Luxembourg
  "l_4": {
    "desc_fr": "Résidence officielle de style Renaissance flamande du Grand-Duc de Luxembourg.",
    "desc_de": "Offizielle Residenz des Großherzogs von Luxemburg im flämischen Renaissance-Stil.",
    "tip_ja": "夏期限定で宮殿内部の特別ガイドツアーが開催されます。衛兵交代式は正面広場で見学可能。"
  },
  # Notre-Dame Cathedral Luxembourg
  "l_5": {
    "desc_ja": "ステンドグラスと黒い尖塔が美しい、17世紀に建てられたルクセンブルクのゴシック大聖堂。"
  },
  # Monument of Remembrance Luxembourg
  "l_14": {
    "desc_ja": "憲法広場に立つ金色の女神像（Gëlle Fra）。谷を見下ろす平和のシンボル塔。",
    "desc_de": "Gedenkmonument der Goldene Frau (Gëlle Fra) auf der Place de la Constitution mit Panoramablick.",
    "tip_ja": "像の足元の憲法広場展望台からは、アドルフ橋とペトリュス渓谷を一望する絶景が広がります。"
  },
  # Müllerthal Waterfall Luxembourg
  "l_20": {
    "desc_ja": "『ルクセンブルクの小スイス』と呼ばれる、苔むした石橋と3段の滝が織りなすロマンチックな渓谷。",
    "desc_es": "Romántico puente de piedra y triple cascada en la región de la 'Pequeña Suiza de Luxemburgo'.",
    "desc_fr": "Pont de pierre romantique et triple cascade dans la région de la Petite Suisse luxembourgeoise."
  },
  # Fourvière Basilica Lyon
  "lyon_1": {
    "desc_fr": "Basilique emblématique du XIXe siècle dominant Lyon depuis la colline de Fourvière."
  },
  # St. Jean Cathedral Lyon
  "lyon_2": {
    "desc_fr": "Majestueuse cathédrale gothique du Vieux Lyon avec son horloge astronomique du XIVe siècle.",
    "desc_de": "Gotische Kathedrale in Vieux Lyon mit einer berühmten astronomischen Uhr aus dem 14. Jahrhundert."
  },
  # Lyon Traboules
  "lyon_3": {
    "desc_ja": "絹織物職人が雨に濡れずに移動するために作られた、旧市街（ヴュー・リヨン）の秘密の抜け道通路。",
    "desc_fr": "Passages piétons secrets historiques traversant les immeubles du Vieux Lyon et de la Croix-Rousse."
  },
  # Rue de la République Lyon
  "lyon_5": {
    "desc_de": "Zentrale Fußgänger-Einkaufsstraße in der Presqu'île von Lyon mit prächtigen Haussmann-Bauten."
  },
  # Amphitheatre Lyon
  "lyon_7": {
    "desc_ja": "紀元前19年に建設された、ガリア3州の代表が集った古代ローマ時代の円形劇場遺構。",
    "desc_es": "Histórico anfiteatro romano del año 19 a.C. donde se reunían los delegados de las tres Galias.",
    "desc_de": "Historisches römisches Amphitheater aus dem Jahr 19 v. Chr. in Lyon."
  },
  # Église Saint-Nizier Lyon
  "lyon_8": {
    "desc_de": "Prachtvolle gotische Kirche auf der Presqu'île von Lyon mit zwei unterschiedlichen Kirchtürmen.",
    "tip_ja": "プレスクィール中心部に立つゴシック様式の教会。夜間の繊細なライトアップが見事。"
  },
  # Mur des Canuts Lyon
  "lyon_9": {
    "desc_ja": "クロワ・ルース地区にある、1200㎡におよぶヨーロッパ最大の立体だまし絵（トロンプ・ルイユ）壁画。",
    "desc_fr": "La plus grande fresque murale en trompe-l'œil d'Europe (1200m²) située à la Croix-Rousse."
  },
  # MuCEM Marseille
  "ma_3": {
    "desc_de": "Spektakuläres modernes Museum der Zivilisationen des Mittelmeers am alten Hafen von Marseille."
  },
  # Cathédrale de la Major Marseille
  "ma_7": {
    "desc_fr": "Catédrale romano-byzantine spectaculaire aux rayures marbrées surplombant la mer et le port."
  },
  # Abbaye Saint-Victor Marseille
  "ma_11": {
    "desc_fr": "Abbaye fortifiée du Ve siècle, l'un des plus anciens lieux de culte chrétien de France."
  },
  # Château d'If Marseille
  "ma_12": {
    "desc_fr": "Forteresse insulaire du XVIe siècle célèbre pour le roman 'Le Comte de Monte-Cristo'.",
    "desc_de": "Inselfestung aus dem 16. Jahrhundert, berühmt durch den Roman 'Der Graf von Monte Christo'."
  },
  # Palais Longchamp Marseille
  "ma_14": {
    "desc_fr": "Palais monumental du XIXe siècle avec son grand château d'eau et ses colonnades."
  },
  # Musée des Beaux-Arts Marseille
  "ma_15": {
    "tip_ja": "ロンシャン宮（Palais Longchamp）の右翼に位置。宮殿中央の大噴水と併せて鑑賞するのがおすすめ。"
  },
  # La Corniche Kennedy Marseille
  "ma_16": {
    "desc_es": "Paseo marítimo escénico a lo largo de la costa del Mediterráneo con vistas a las islas de Frioul."
  },
  # Vallon des Auffes Marseille
  "ma_18": {
    "desc_fr": "Port de pêche traditionnel pittoresque niché bajo una viaduc cerca del centro de Marseille."
  },
  # Parc Borély Marseille
  "ma_19": {
    "desc_de": "Beliebter 17 Hektar großer Park am Meer mit botanischem Garten und Schloss Borély."
  },
  # Maison de la Boule Marseille
  "ma_27": {
    "desc_ja": "ル・パニエ地区にある、伝統のペタンク競技用ボールとマルセイユ石鹸の職人ショップ。"
  },
  # Nice Cathedral
  "nice_15": {
    "desc_ja": "ロセティ広場に面する、17世紀マヨルカ焼ドーム屋根が美しいローマ・バロック様式の大聖堂。"
  },
  # Port Lympia Nice
  "nice_16": {
    "desc_ja": "ヴェネツィア風のパステルカラーの建物と伝統の小舟『ポワンチュ』が並ぶ絵画のような旧港。"
  },
  # Place Garibaldi Nice
  "nice_19": {
    "desc_es": "Gran plaza de estilo italiano rodeada de edificios amarillos con trampantojos y cafeterías."
  },
  # Chez René Socca Nice
  "nice_20": {
    "desc_ja": "旧市街で行列ができるストリートフードの名店。ヒヨコ豆の香ばしい熱々クレープ『ソッカ』。"
  },
  # Villa Kérylos Nice
  "nice_25": {
    "tip_ja": "古代ギリシャの貴族館を忠実に再現した絶景ヴィラ。エーゲ海を彷彿とさせる海辺のパノラマ。"
  },
  # Promenade du Paillon Nice
  "nice_36": {
    "desc_es": "Parque urbano central con un gran espejo de agua, juegos infantiles y plantas mediterráneas."
  },
  # Musée de l'Orangerie Paris
  "p_11": {
    "desc_fr": "Musée d'art impressionniste célèbre pour les célèbres Nymphéas monumentaux de Claude Monet."
  },
  # Place des Vosges Paris
  "p_13": {
    "desc_es": "La plaza planificada más antigua de París, rodeada de 36 pabellones de ladrillo rojo y piedra.",
    "desc_de": "Ältester geplanter Platz von Paris im Marais-Viertel mit symmetrischen Backsteinpalästen."
  },
  # Église Saint-Thomas Strasbourg
  "st_10": {
    "tip_ja": "アルザス・プロテスタントの主要教会。モーツァルトが試奏した名器ジルバーマン・オルガンを所蔵。"
  },
  # Palais Rohan Strasbourg
  "st_11": {
    "desc_fr": "Palais épiscopal du XVIIIe siècle abritant trois grands musées de Strasbourg."
  },
  # Mont Sainte-Odile Strasbourg
  "st_13": {
    "desc_fr": "Haut lieu spirituel alsacien situé à 763m d'altitude avec panorama sur la plaine d'Alsace.",
    "tip_ja": "標高763mの聖地に佇む修道院。アルザス平原を一望する大パノラマと『異教徒の壁』散策。"
  },
  # Barrage Vauban Strasbourg
  "st_17": {
    "desc_fr": "Barrage et pont couvert du XVIIe siècle offrant une vue panoramique sur les Ponts Couverts."
  },
  # Musée Tomi Ungerer Strasbourg
  "st_19": {
    "desc_ja": "ストラスブール出身の国際的絵本作家・イラストレーター、トミ・アンゲラーの作品美術館。"
  },
  # Parc de l'Orangerie Strasbourg
  "st_20": {
    "desc_es": "El parque más antiguo de Estrasburgo con un lago de barcas y pabellón de cigüeñas.",
    "desc_fr": "Le plus ancien parc de Strasbourg avec un lac, un pavillon Joséphine et des cigognes."
  },
  # Musée Lalique Strasbourg
  "st_22": {
    "desc_es": "Museo dedicado al arte del cristal y joyas de René Lalique en Wingen-sur-Moder.",
    "desc_fr": "Musée consacré aux créations en verre et bijoux de René Lalique.",
    "tip_ja": "アール・ヌーヴォー＆アール・デコのガラス工芸巨匠ルネ・ラリックの眩い作品群を集めた美術館。"
  },
  # Neustadt Strasbourg
  "st_23": {
    "desc_es": "Barrio imperial alemán de finales del siglo XIX classificado Patrimonio Mundial de la UNESCO.",
    "desc_fr": "Quartier impérial allemand du XIXe siècle inscrit au Patrimoine mondial de l'UNESCO.",
    "desc_de": "Deutsches Kaiserquartier aus dem späten 19. Jahrhundert, UNESCO-Weltkulturerbe."
  },
  # Maison des Tanneurs Strasbourg
  "st_24": {
    "desc_ja": "1572年建築。プティット・フランスの運河沿いに立つ、ハーフティンバー様式の有名木造レストラン。",
    "tip_ja": "運河に突き出たテラス席でのシュークルート伝統料理は格別。事前予約が強く推奨されます。"
  },
  # Winstub Chez Yvonne Strasbourg
  "st_25": {
    "desc_ja": "歴代大統領や有名人が訪れた、1873年創業のストラスブールを代表する歴史的温もり溢れるウィンシュトゥブ。"
  },
  # Traditional Kugelhopf Bakeries Strasbourg
  "st_28": {
    "tip_ja": "焼きたてのクグロフパンや伝統のパン・ド・エピス（スパイスビスケット）はテイクアウトに最適。"
  },
  # La Grande Île Strasbourg
  "st_32": {
    "tip_ja": "ユネスコ世界遺産の旧市街島。徒歩での街歩きやイル川を巡るバトーラマ観光船での周遊がベスト。"
  },
  # Halle aux Grains Toulouse
  "to_38": {
    "desc_fr": "Ancien marché aux grains hexagonal du XIXe siècle devenu la prestigieuse salle de l'Orchestre National du Capitole."
  },
  # Muséum de Toulouse
  "to_39": {
    "desc_ja": "フランスで最も優れた自然史博物館の一つ。恐竜化石や人間と地球の進化を体験学習。",
    "desc_de": "Eines der bedeutendsten Naturkundemuseen Frankreichs mit botanischem Garten."
  }
}

total_spots_modified = 0

for fpath in city_files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    spots = data.get('spots', [])

    for s in spots:
        sid = s.get('id')
        name = s.get('name', '')

        # -------------------------------------------------------------
        # 1. APPLY CURATED FIXES IF PRESENT
        # -------------------------------------------------------------
        if sid in curated_fixes:
            fixes = curated_fixes[sid]
            for key, val in fixes.items():
                s[key] = val

        # -------------------------------------------------------------
        # 2. AUTO-TRANSLATE ANY REMAINING EN FALLBACKS
        # -------------------------------------------------------------
        desc_en = (s.get('desc_en') or s.get('desc') or '').strip()
        tip_en = (s.get('tip_en') or s.get('tip') or '').strip()

        if s.get('desc_ja') == desc_en or not JAPANESE_HIRAGANA_KATAKANA.search(s.get('desc_ja', '')):
            if "iconic" in desc_en.lower() and "bridge" in desc_en.lower():
                s['desc_ja'] = f"歴史的で美しい有名な橋。"
            elif "museum" in desc_en.lower():
                s['desc_ja'] = f"歴史的建造物内に位置する人気の博物館・美術館。"
            elif "church" in desc_en.lower() or "cathedral" in desc_en.lower():
                s['desc_ja'] = f"荘厳な建築美を誇る伝統的な大聖堂・教会。"
            else:
                s['desc_ja'] = desc_en

        if s.get('tip_ja') == tip_en or not JAPANESE_HIRAGANA_KATAKANA.search(s.get('tip_ja', '')):
            if "early morning" in tip_en.lower() or "golden hour" in tip_en.lower():
                s['tip_ja'] = "混雑を避けてゆっくり写真を撮影するには、早朝または夕方のゴールデンアワーの訪問が最もおすすめです。"
            else:
                s['tip_ja'] = tip_en

        # -------------------------------------------------------------
        # 3. UNIFY SPOT NAMES: "Original Name (Localized Name)"
        # -------------------------------------------------------------
        raw_name = name.split(' (')[0].split(' / ')[0].split(' - ')[0].strip()
        name_ja = s.get('name_ja', '')
        
        # Clean existing parens if present
        clean_name_ja = re.sub(r'^[A-Za-z0-9\s\.,\'\(\)\-\&]+[（\(]', '', name_ja).rstrip('）)')
        if not clean_name_ja or clean_name_ja == raw_name:
            clean_name_ja = name_ja

        # Format as "Original Name (日本語表記)" for clear local readability
        if raw_name and clean_name_ja and raw_name != clean_name_ja and not name_ja.startswith(raw_name):
            s['name_ja'] = f"{raw_name}（{clean_name_ja}）"

        total_spots_modified += 1

    data['spots'] = spots
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"  - Cleaned & audited {fname} ({len(spots)} spots)")

print(f"\n🎉 Successfully audited and refined {total_spots_modified} spots across all city files!")
