import json
import os

# Helper generator to construct clean spot data
def make_spot(id_prefix, num, name_ja_str, name_en_str, name_de_str, cat, rating, zone, lat, lng, price_ja, desc_ja, tip_ja):
    return {
        "id": f"{id_prefix}_{num}",
        "name": f"{name_de_str}（{name_ja_str}）",
        "category": cat,
        "rating": rating,
        "locationZone": zone,
        "lat": lat,
        "lng": lng,
        "kids": True,
        "rain": "Museum" in cat or "Landmark" in cat,
        "shopping": cat == "Shopping",
        "free": "無料" in price_ja or "Free" in price_ja,
        "desc_en": f"{name_en_str} in {zone.capitalize()} district.",
        "desc_ja": desc_ja,
        "desc_es": f"{name_en_str} destacado en la ciudad.",
        "desc_zh": f"位于当地的知名景点 {name_ja_str}。",
        "desc_fr": f"{name_en_str} remarquable à visiter.",
        "de": f"{name_de_str} im Stadtgebiet.",
        "tip_en": f"💡 {tip_ja}",
        "tip_ja": f"💡 {tip_ja}",
        "tip_es": f"💡 {tip_ja}",
        "tip_zh": f"💡 {tip_ja}",
        "tip_fr": f"💡 {tip_ja}",
        "tip_de": f"💡 {tip_ja}",
        "price_en": price_ja,
        "price_ja": price_ja,
        "price_es": price_ja,
        "price_zh": price_ja,
        "price_fr": price_ja,
        "price_de": price_ja,
        "name_en": name_en_str,
        "name_ja": f"{name_de_str}（{name_ja_str}）",
        "name_es": name_en_str,
        "name_zh": name_ja_str,
        "name_fr": name_en_str,
        "name_de": name_de_str
    }

# ----------------------------------------------------
# FRANKFURT 61 SPOTS DEFINITION
# ----------------------------------------------------
ffm_raw = [
    # City (1-45)
    (1, "レーマー広場＆旧市庁舎レーマー", "Römerberg & City Hall", "Römerberg & Rathaus Römer", "Landmark", "★4.8", "city", 50.1103, 8.6821, "見学無料", "木骨造りの旧市庁舎レーマーと正義の女神像の噴水が立つ歴史的広場。", "早朝8:30前に訪問すると観光客の映り込みなしで撮影可能！"),
    (2, "聖バルトロメウス大聖堂", "Frankfurt Cathedral", "Kaiserdom St. Bartholomäus", "Landmark", "★4.7", "city", 50.1106, 8.6853, "聖堂無料（塔3.50€）", "神聖ローマ皇帝の戴冠式が行われた赤砂岩のゴシック大聖堂。", "328段の急階段を登ってDomturm展望台へ！広場の赤屋根が見下ろせます。"),
    (3, "ゲーテハウス＆ドイツ・ロマン派博物館", "Goethe House & Museum", "Goethe-Haus", "Museum & Gallery", "★4.6", "city", 50.1114, 8.6775, "入場料: 10€", "文豪ゲーテが生まれ育った18世紀の邸宅。『若きウェルテルの悩み』の書斎。", "3階の立ち机（Schreibzimmer）で傑作が生まれた歴史空間を観察！"),
    (4, "シュテーデル美術館", "Städel Museum", "Städel Museum", "Museum & Gallery", "★4.8", "city", 50.1031, 8.6742, "入場料: 16€", "欧州700年の美術殿堂。フェルメール『地理学者』やモネを所蔵。", "地下新館Gartenhallenへ！芝生の丸天窓から注ぐ自然光でモダンアート鑑賞。"),
    (5, "マインタワー", "Main Tower Observatory", "Main Tower", "Landmark", "★4.7", "city", 50.1114, 8.6722, "入場料: 9€", "金融街に立つ高さ200mの摩天楼。地上198mのオープンエア屋上展望台。", "日没の30分前に入場するのが黄金法則！夕焼けから夜景の変化を撮影。"),
    (6, "アイゼルナー・シュテグ鉄橋", "Iron Footbridge", "Eiserner Steg", "Landmark", "★4.6", "city", 50.1086, 8.6817, "通行無料", "1869年建造のマイン川に架かる歩行者専用鉄橋。愛の南京錠が並ぶ。", "橋の中央部から北側を振り返り、旧市街屋根と高層ビル群の対比を撮影！"),
    (7, "聖パウロ教会", "St. Paul's Church", "Paulskirche", "Landmark", "★4.5", "city", 50.1111, 8.6808, "入場無料", "1848年にドイツ初の自由選挙による国民議会が開かれた民主主義の揺籃。", "2階の円形本会議堂へ！壁面を囲む33mの巨幅壁画『民衆の代表者の行進』を鑑賞。"),
    (8, "アルテ・オーパー旧オペラ座", "Old Opera House", "Alte Oper", "Landmark", "★4.7", "city", 50.1158, 8.6719, "広場無料", "1880年建造のネオ・ルネサンス様式の旧オペラ座。美しい大噴水が象徴。", "オペラ広場の噴水前カフェで休憩！黄金像が点灯する夕暮れ時が映えます。"),
    (9, "パルメンガルテン植物園", "Palmengarten Botanical Garden", "Palmengarten", "Scenery & Walk", "★4.7", "city", 50.1239, 8.6575, "入場料: 7€", "1869年建造の鉄とガラスの大温室パルメンハウスを中心とする22haの植物園。", "大温室パルメンハウス内部へ！20℃以上に保たれた熱帯密林と滝を体感。"),
    (10, "フランクフルト歴史博物館", "Frankfurt History Museum", "Historisches Museum Frankfurt", "Museum & Gallery", "★4.7", "city", 50.1097, 8.6828, "入場料: 12€", "中世建築と最新の現代翼が融合した都市史博物館。800年の歩みを展示。", "新館2階の3D都市模型へ！ボタン操作で時代ごとに街並みが点灯変形。"),
    (11, "リービークハウス彫刻美術館", "Liebieghaus Sculpture Museum", "Liebieghaus Skulpturensammlung", "Museum & Gallery", "★4.7", "city", 50.1022, 8.6725, "入場料: 12€", "19世紀の邸宅を利用した彫刻専門館。5000年にわたる世界の彫刻を所蔵。", "バラ園に囲まれた庭園の中庭で大理石彫刻を静かに観賞。"),
    (12, "応用工芸博物館", "Museum of Applied Arts", "Museum Angewandte Kunst", "Museum & Gallery", "★4.5", "city", 50.1064, 8.6811, "入場料: 12€", "リチャード・マイヤー設計の白亜の建築。工芸、デザイン、ファッションを展示。", "マイヤー設計の自然光が差し込む白い回廊建築自体を写真に収めるのが秘訣。"),
    (13, "ドイツ映画博物館", "DFF - German Film Institute & Film Museum", "Deutsches Filminstitut & Filmmuseum", "Museum & Gallery", "★4.6", "city", 50.1053, 8.6781, "入場料: 10€", "映画の誕生から最新特撮CGまでの歴史と体験型セットを展示。", "映画特撮グリーンバック体験コーナーでSF映画の主人公になりきって動画撮影！"),
    (14, "フランクフルト現代美術館", "Museum of Modern Art", "Museum für Moderne Kunst (MMK)", "Museum & Gallery", "★4.6", "city", 50.1117, 8.6847, "入場料: 12€", "「ケーキの一切れ」と称される三角形の斬新な現代美術殿堂。", "ハンス・ホライン設計の鋭角な三角形吹き抜け空間を見上げて撮影。"),
    (15, "シルン美術館", "Schirn Kunsthalle Frankfurt", "Schirn Kunsthalle Frankfurt", "Museum & Gallery", "★4.6", "city", 50.1106, 8.6839, "入場料: 14€", "レーマー広場隣の企画展専門の近代・現代美術アトリウム館。", "ガラスドームのグランドロビー通路から旧市街へ抜ける光のアングルが綺麗。"),
    (16, "博物館河岸エリア", "Museumsufer River Bank", "Museumsufer", "Scenery & Walk", "★4.8", "city", 50.1044, 8.6778, "散策無料", "マイン川南岸沿いに13の世界的美術館・博物館が立ち並ぶ文化エリア。", "毎月第2土日の古本・骨董蚤の市（Flohmarkt）に合わせて川沿いを散策！"),
    (17, "クラインマルクトハレ屋内市場", "Kleinmarkthalle Market", "Kleinmarkthalle", "Shopping", "★4.7", "city", 50.1119, 8.6833, "入場無料", "150以上の店舗が集結する1954年開業の歴史的屋内食品市場。", "1階肉屋Schreiberで熱々のフライシュヴルスト（特大ソーセージ€3.50）を食す！"),
    (18, "新旧市街", "New Old Town", "Neue Altstadt", "Landmark", "★4.7", "city", 50.1108, 8.6836, "散策無料", "戦災で失われた中世・ルネサンスの木骨造り街並みを精密再建したエリア。", "小路Hühnermarkt中央へ！黄金の秤の館Goldene Waageの張り出し彫刻が見事。"),
    (19, "ザクセンハウゼン地区＆居酒屋街", "Sachsenhausen Cider District", "Sachsenhausen", "Café & Bistro", "★4.6", "city", 50.1039, 8.6908, "散策無料", "マイン川南岸の石畳居酒屋街。素焼き壺ベンベルで注ぐ名物リンゴ酒の名所。", "老舗Zum Gemalten Hausの長ベンチで炭酸水割りリンゴ酒と緑ソースカツを食す！"),
    (20, "ザクセンハウゼンの歴史的アプフェルヴァイン酒場群", "Historic Apple Wine Taverns", "Zur Sonne / Zum Gemalten Haus / Atschel", "Café & Bistro", "★4.7", "city", 50.1033, 8.6914, "リンゴ酒: 3€", "18世紀から続く老舗リンゴ酒場。木製ベンチと特製グラフィック壁画が特徴。", "相席の木製テーブルで地元の常連客と乾杯（Prost）するのが流儀！"),
    (21, "ツァイル通り＆マイツァイル", "Zeil Shopping Street & MyZeil", "Zeil & MyZeil", "Shopping", "★4.6", "city", 50.1147, 8.6828, "散策無料", "フランクフルト最大の歩行者天国ショッピング街と渦巻きガラスビルMyZeil。", "MyZeil内にある欧州最長級の46m直通エスカレーターで最上階へ一気に昇る！"),
    (22, "ゲーテ通り", "Goethestraße Luxury Street", "Goethestraße", "Shopping", "★4.6", "city", 50.1136, 8.6756, "散策無料", "シャネルやルイ・ヴィトンなど世界最高峰ハイブランドが並ぶ高級ブティック街。", "落ち着いた美しい夕暮れ時に街灯が点灯する街並みをウィンドーショッピング。"),
    (23, "フレスガス通り", "Fressgass Culinary Street", "Große Bockenheimer Straße (Fressgass)", "Café & Bistro", "★4.6", "city", 50.1144, 8.6747, "散策無料", "「大食い街（Fressgass）」の愛称を持つ高級デリカテッセンやカフェが連なる通り。", "デリカテッセンMeyerの屋外テラスで新鮮なチーズとワインでランチタイム。"),
    (24, "ハウプトヴァッヘ広場＆聖カタリーナ教会", "Hauptwache Square & St. Catherine's", "Hauptwache & Katharinenkirche", "Landmark", "★4.6", "city", 50.1136, 8.6789, "見学無料", "1730年建造の旧警備所バロック建築と中心街のランドマーク広場。", "旧警備所カフェCafé Hauptwacheのバロック建築テラス席から広場人間観察。"),
    (25, "マイン川河岸遊歩道", "Main River Promenade", "Mainufer-Promenade", "Scenery & Walk", "★4.8", "city", 50.1067, 8.6792, "散策無料", "両岸に芝生とポプラ並木が続く市民の憩いのリバーサイドプロムナード。", "夕刻に芝生に座って、マイン川越しに摩天楼群が夕日に染まるシルエットを鑑賞！"),
    (26, "フランクフルト動物園", "Frankfurt Zoo", "Zoo Frankfurt", "Kids & Family", "★4.6", "city", 50.1158, 8.7033, "入場料: 12€", "1858年開園の歴史ある都市型動物園。夜行性動物館 Grzimek-Haus が有名。", "暗闇の夜行性動物館Grzimek-Hausで活発に動くツチブタやアイアイを観察！"),
    (27, "ゼンケンベルク自然博物館", "Senckenberg Natural History Museum", "Senckenberg Naturmuseum", "Museum & Gallery", "★4.7", "city", 50.1175, 8.6517, "入場料: 12€", "欧州最大級の自然史館。ディプロドクスやティラノサウルスの全身骨格標本。", "第1ホールへ直行！巨大ディプロドクスとステゴサウルスの本物化石を見上げる。"),
    (28, "フランクフルト証券取引所", "Frankfurt Stock Exchange", "Frankfurter Wertpapierbörse (Börse)", "Landmark", "★4.6", "city", 50.1153, 8.6781, "広場無料", "世界有数の取引所。建物の前には強気（ブル）と弱気（ベア）の銅像が立つ。", "📸 雄牛（Bull）と熊（Bear）のブロンズ像の間に立ち、株高を祈願して写真撮影！"),
    (29, "巨大ユーロマーク像", "Euro Sculpture", "Euro-Skulptur (Willy-Brandt-Platz)", "Landmark", "★4.5", "city", 50.1092, 8.6739, "見学無料", "旧ECB本部の前に立つ高さ14mの青と黄色の巨大ユーロマーク（€）ネオン像。", "📸 日没後の夜間訪問がおすすめ！青い€と周囲の12個の黄色い星がネオン点灯。"),
    (30, "オイローパフィアテル＆スカイライン・プラザ", "Europaviertel & Skyline Plaza", "Europaviertel & Skyline Plaza", "Shopping", "★4.5", "city", 50.1108, 8.6522, "入場無料", "新開発地区オイローパフィアテルの大型ショッピングモール。屋上庭園が広い。", "モール最上階の屋上庭園Skyline Gardenへ！摩天楼ビル群を背景に芝生で休憩。"),
    (31, "グリューネブルク公園＆フランクフルト植物園", "Grüneburgpark & Botanical Garden", "Grüneburgpark", "Scenery & Walk", "★4.7", "city", 50.1264, 8.6625, "散策無料", "29haの広大な英国式風景庭園。広大な芝生と樹齢数百年の大木が並ぶ。", "公園北側の韓国庭園（Koreanischer Garten）でアジアンな木造楼閣と池を散策。"),
    (32, "ハーフェンパーク＆オストパーク", "Hafenpark & Ostpark", "Hafenpark & Ostpark", "Scenery & Walk", "★4.6", "city", 50.1103, 8.7019, "散策無料", "マイン川東部の最新スポーツ公園。スケートパークやクライミング壁を完備。", "川沿いのウッドデッキベンチからECB新本部ビルの斬新な二重ガラス塔を見上げる！"),
    (33, "欧州中央銀行新本部ビル", "European Central Bank Headquarters", "Europäische Zentralbank (ECB / EZB)", "Landmark", "★4.7", "city", 50.1103, 8.7025, "外観無料", "コープ・ヒンメルブラウ設計の高さ185mのねじれた二重ガラス張り摩天楼。", "ハーフェンパーク側の広場からガラス塔が交差して見える未来的なアングルを撮影。"),
    (34, "ユダヤ博物館", "Jewish Museum Frankfurt", "Jüdisches Museum Frankfurt", "Museum & Gallery", "★4.7", "city", 50.1067, 8.6733, "入場料: 12€", "ロスチャイルド宮殿を利用したドイツ最古の独立系ユダヤ歴史文化博物館。", "新館アトリウムの光溢れる図書カフェでユダヤの伝統菓子とコーヒーを楽しむ。"),
    (35, "ユーデンガッセ博物館", "Museum Judengasse", "Museum Judengasse", "Museum & Gallery", "★4.6", "city", 50.1139, 8.6886, "入場料: 6€", "1462年に設置された欧州最古のユダヤ人ゲットー（居住区）基礎遺構を展示。", "発掘された18世紀のユダヤ住居の地下石造り基礎と井戸を間近で観察！"),
    (36, "エッシェンハイマー塔", "Eschenheim Tower", "Eschenheimer Turm", "Landmark", "★4.6", "city", 50.1172, 8.6797, "外観無料", "1428年建造の高さ47mの中世の城門塔。尖塔と丸い側塔が完全に残る。", "塔の1階に入っているレストランカフェTurmで中世の石壁に囲まれてディナー！"),
    (37, "カフェ・ハウプトヴァッヘ", "Café Hauptwache", "Café Hauptwache", "Café & Bistro", "★4.5", "city", 50.1136, 8.6786, "コーヒー: 4€", "1730年のバロック様式旧警備所建物を利用したフランクフルト最古級カフェ。", "テラス席で名物Apple Wine Cake（アップルワインケーキ）とコーヒーを味わう！"),
    (38, "ヴァッカーズ・カフェ", "Wacker's Kaffee", "Wacker's Kaffee", "Café & Bistro", "★4.7", "city", 50.1133, 8.6778, "エスプレッソ: 2.50€", "1914年創業の老舗自社焙煎コーヒーショップ。地元民が立ち飲む名店。", "店頭の立ち飲みカウンターで煎りたてエスプレッソと出来立てクロワッサンを注文！"),
    (39, "ロールベルク展望公園", "Lohrberg Park", "Lohrberg (Lohrpark)", "Scenery & Walk", "★4.8", "city", 50.1472, 8.7236, "入園無料", "市内北東部の丘にあるぶどう畑と展望公園。フランクフルト全景を見渡せる。", "レストハウスLohrbärg-Schänkeのテラスから自家製自家栽培ワインと摩天楼夕景を楽しむ！"),
    (40, "ニッツァ庭園", "Nizza Gardens", "Nizza Gärten", "Scenery & Walk", "★4.6", "city", 50.1061, 8.6739, "散策無料", "マイン川北岸の微気候を利用した4.5haの地中海風庭園。地中海植物が茂る。", "川沿いの椰子の木やオリーブの木の小道を歩き南仏リゾート気分を味わう！"),
    (41, "レプシュトックバート", "Rebstockbad Water Park", "Rebstockbad", "Kids & Family", "★4.5", "city", 50.1136, 8.6219, "プール: 12€", "大きな波のプール、巨大ウォータースライダー、大型サウナを備えた温水プール。", "屋外の温水プールエリアからフランクフルトの摩天楼ビル群を眺めて泳ぐ！"),
    (42, "エクスペリミンタ科学館", "Experiminta ScienceCenter", "Experiminta ScienceCenter", "Kids & Family", "★4.6", "city", 50.1172, 8.6475, "入場料: 12€", "130以上の体験型物理・数学実験ステーションを備えた参加型科学館。", "巨大なシャボン玉の膜の中に自分自身が入るシャボン玉体験コーナーで撮影！"),
    (43, "聖書体験博物館", "Bibelhaus Experience Museum", "Bibelhaus Erlebnis Museum", "Museum & Gallery", "★4.5", "city", 50.1058, 8.6772, "入場料: 7€", "古代ノアの箱舟の木造模型や古代パレスチナの住居を五感で体験する博物館。", "古代の織り機や石臼を使った小麦粉挽き体験にチャレンジ！"),
    (44, "ダイアログ・ミュージアム", "DialogMuseum", "DialogMuseum", "Museum & Gallery", "★4.8", "city", 50.1103, 8.6947, "体験料: 17€", "視覚障害者のガイドとともに暗黒の暗闇空間を五感で探検する体験館。", "完全な暗闇の中で音と手触りだけでカフェ注文するダークバー体験が衝撃的！"),
    (45, "エッベルヴァイ・エクスプレス", "Ebbelwei-Express Tram", "Historische Straßenbahn Frankfurt", "Kids & Family", "★4.6", "city", 50.1119, 8.6886, "乗車券: 8€", "1977年から運航するレトロ市電。リンゴ酒とプレッツェルを車内で味わう。", "週末限定運行！チケット（€8）に小瓶リンゴ酒とプレッツェル袋がセット。"),

    # Suburban (46-61)
    (46, "リューデスハイム＆つぐみ横丁", "Rüdesheim Rhine Valley", "Rüdesheim am Rhein & Drosselgasse", "Landmark", "★4.8", "suburban", 49.9786, 7.9222, "街散策無料", "世界遺産ライン渓谷の拠点。144mの狭い路地にワイン酒場が並ぶつぐみ横丁。", "2人乗りオープンロープウェイでブドウ畑の上空を空中散歩！記念碑からの見下ろし絶景。"),
    (47, "エルツ城＆ライン川古城群", "Eltz Castle", "Burg Eltz", "Landmark", "★4.9", "suburban", 50.2053, 7.3364, "入場料: 14€", "森の奥深くに佇む12世紀の中世の古城。33代800年にわたり所有される無破壊の城。", "駐車場からの坂道を下る途中の曲がり角がベストアングル！絵はがきビューを撮影。"),
    (48, "マインツ：大聖堂＆グーテンベルク博物館", "Mainz Cathedral & Museum", "Mainz: Dom St. Martin & Gutenberg-Museum", "Landmark", "★4.7", "suburban", 49.9989, 8.2739, "博物館: 5€", "千年以上の歴史を誇る大聖堂と活版印刷発明者グーテンベルクの博物館。", "グーテンベルク博物館の地下金庫室へ！1450年代の本物『グーテンベルク聖書』原本を閲覧。"),
    (49, "ヴィースバーデン：クアハウス＆ネロベルク登山鉄道", "Wiesbaden Kurhaus & Nerobergbahn", "Wiesbaden: Kurhaus & Nerobergbahn", "Landmark", "★4.7", "suburban", 50.0847, 8.2436, "水力鉄道: 5€", "高級温泉保養都市。1907年建造の壮麗なクアハウスと水重力式ネロベルク登山鉄道。", "1888年開業の水重力式ネロベルク登山鉄道（Nerobergbahn）に乗って頂上展望台へ！"),
    (50, "インゲルハイムのカール大帝宮殿跡", "Ingelheim Imperial Palace", "Kaiserpfalz Ingelheim", "Landmark", "★4.5", "suburban", 49.9753, 8.0558, "見学無料", "800年頃にカール大帝（シャルルマーニュ）が建設した伝説の帝国居城遺跡。", "北門（Heidesheimer Tor）の半円形石造りアーチ門の下で中世古代遺構を撮影！"),
    (51, "クロンベルク城＆クロンベルク旧市街", "Kronberg Castle & Old Town", "Burg Kronberg & Kronberg im Taunus", "Landmark", "★4.6", "suburban", 50.1808, 8.5081, "城入場: 6€", "タウヌス山麓の木骨造り旧市街と13世紀の城塞。見張り塔からのビューが素晴らしい。", "高さ44mの城の見張り塔（Keep）に登り、遠くフランクフルトの摩天楼天际線を遠望！"),
    (52, "グローサー・フェルトベルク最高峰", "Großer Feldberg Summit", "Großer Feldberg (Taunus)", "Scenery & Walk", "★4.7", "suburban", 50.2319, 8.4583, "散策無料", "タウヌス山脈の最高峰（標高878m）。山頂に通信塔と大パノラマ展望台が立つ。", "山頂レストランFeldberghofの屋外ベンチで特製ソーセージを食べながらライン平野を一望！"),
    (53, "ヘッセンパーク野外博物館", "Hessenpark Open-Air Museum", "Freilichtmuseum Hessenpark", "Museum & Gallery", "★4.7", "suburban", 50.2758, 8.5283, "入場料: 11€", "ヘッセン州各地から移築された100棟以上の歴史的木骨造り農家や風車を集めた野外館。", "伝統のパン焼き小屋（Backhaus）で薪窯で焼き上げられた熱々の農家パンを購入！"),
    (54, "ザールブルク・ローマ軍砦遺跡", "Saalburg Roman Fort", "Römerkastell Saalburg", "Landmark", "★4.7", "suburban", 50.2711, 8.5667, "入場料: 7€", "ユネスコ世界遺産「ローマ帝国の国境線（リメス）」上に完全再建されたローマ軍砦。", "ローマ軍兵士の完全復元された宿舎や浴場を見学後、ローマ風カフェTabernaでハーブスパイスパンを試食！"),
    (55, "バート・ホムブルク：クアパーク＆城館", "Bad Homburg Kurpark & Palace", "Bad Homburg: Kurpark & Schloss", "Landmark", "★4.7", "suburban", 50.2272, 8.6186, "公園無料", "タイ王室寄贈のタイ風東屋やエリザベート源泉がある欧州屈指の歴史的スパ公園。", "クアパーク内の鮮やかなタイ式東屋（Siamesischer Tempel）の前で異国情緒あふれる写真を撮影！"),
    (56, "タウヌス・ヴンダーラント", "Taunus Wunderland Amusement Park", "Taunus Wunderland", "Kids & Family", "★4.5", "suburban", 50.1264, 8.1189, "入園料: 29.50€", "タウヌスの森に囲まれたファミリー向け大型テーマパーク。水上コースターが人気。", "恐竜エリアDino-Parkで原寸大の動くT-レックスと家族記念撮影！"),
    (57, "オペル動物園", "Opel-Zoo Kronberg", "Opel-Zoo (Kronberg)", "Kids & Family", "★4.7", "suburban", 50.1897, 8.4986, "入場料: 16€", "ヘッセン州で唯一ゾウを飼育する広大な自然動物園。アフリカサバンナエリアが広い。", "高台のサバンナ観察デッキからキリンとゾウが一緒に歩く大自然アングルを撮影！"),
    (58, "エバーバッハ修道院", "Eberbach Abbey", "Kloster Eberbach", "Landmark", "★4.8", "suburban", 50.0425, 8.0461, "入場料: 12€", "1136年創建のシトー会修道院。映画『薔薇の名前』のロケ地で銘醸ワイン醸造所。", "17世紀の超巨大木製ワイン圧搾機を見学後、直営ショップでリースリング白ワインを試飲！"),
    (59, "ダルムシュタット：マチルダの丘", "Darmstadt Mathildenhöhe", "Darmstadt: Mathildenhöhe (UNESCO)", "Landmark", "★4.7", "suburban", 49.8769, 8.6675, "敷地無料", "ユネスコ世界遺産のユーゲントシュティール芸術家村。結婚記念塔とロシア教会が象徴。", "5本の指の形をした結婚記念塔のテラスへ！プラタナス木立と金色のロシア教会を見下ろす。"),
    (60, "フランケンシュタイン城", "Frankenstein Castle", "Burg Frankenstein", "Landmark", "★4.6", "suburban", 49.7936, 8.6683, "城散策無料", "メアリー・シェリーの小説『フランケンシュタイン』の着想源とされる13世紀の城塞廃墟。", "城壁の展望台からダルムシュタット市街を見下ろし、ハロウィン時期のホラーイベントをチェック！"),
    (61, "ヴェルトハイム・ビレッジ", "Wertheim Village Outlet", "Wertheim Village", "Shopping", "★4.6", "suburban", 49.7719, 9.5772, "入館無料", "フランクフルトから1時間。110以上のデザイナーブランドが最大60%オフのアウトレット。", "フランクフルト中央駅から直行運行する公式シャトルバスShopping Expressで快適アクセス！")
]

# Generate full list
ffm_spots = []
for item in ffm_raw:
    ffm_spots.append(make_spot("f", item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11]))

with open("data/cities/frankfurt.json", "w", encoding="utf-8") as f:
    json.dump({"cityName": "Frankfurt, Germany", "spots": ffm_spots}, f, ensure_ascii=False, indent=2)

print(f"🎉 Successfully built data/cities/frankfurt.json with ALL {len(ffm_spots)} SPOTS!")
