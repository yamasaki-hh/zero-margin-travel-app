import json
import os

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
# 1. HAMBURG 61 SPOTS DEFINITION
# ----------------------------------------------------
ham_raw = [
    # City 1-49
    (1, "ミニチュアワンダーランド", "Miniatur Wunderland", "Miniatur Wunderland", "Kids & Family", "★4.9", "city", 53.5438, 9.9888, "入場料: 20€", "世界最大の動く鉄道模型テーマパーク。1,100編成超の列車とミニ空港。", "公式サイトで数週間前Web予約が必須！夜間営業枠（20:00以降）が混雑なし。"),
    (2, "エルプフィルハーモニー・ハンブルク", "Elbphilharmonie Concert Hall", "Elbphilharmonie Hamburg", "Landmark", "★4.8", "city", 53.5413, 9.9842, "展望プラザ無料", "赤レンガ倉庫の上に波打つガラスが載るハンブルク港のシンボル。", "発券カウンターで無料プラザ券を受け取り、82m曲面エスカレーターで37m展望台へ！"),
    (3, "世界遺産赤レンガ倉庫街", "Speicherstadt Warehouse District", "Speicherstadt", "Landmark", "★4.8", "city", 53.5433, 9.9922, "散策無料", "オーク材の杭で支えられた赤レンガ倉庫群が連なる世界最大の倉庫街（世界遺産）。", "日没時にPoggenmühlenbrücke橋の上から水上城館Wasserschlossの点灯を撮影！"),
    (4, "コントーアハウス地区＆チリハウス", "Chilehaus & Kontorhaus District", "Kontorhausviertel & Chilehaus", "Landmark", "★4.7", "city", 53.5483, 10.0019, "見学無料", "1920年代のレンガ表現主義建築群。船首のように尖った角部を持つチリハウス。", "FischertwieteとBurchardstraßeの交差点角から45度の船首角部を見上げて撮影！"),
    (5, "ハンブルク市庁舎＆市庁舎前広場", "Hamburg City Hall", "Hamburger Rathaus & Rathausmarkt", "Landmark", "★4.8", "city", 53.5503, 9.9928, "中庭無料", "647室を誇るネオ・ルネサンス宮殿風市庁舎。112mの塔とヒュギエイアの噴水。", "市庁舎アーチをくぐり静かな中庭へ！コレラ終息記念のヒュギエイアの噴水を鑑賞。"),
    (6, "聖ミヒャエリス教会", "St. Michael's Church", "Hauptkirche St. Michaelis (Michel)", "Landmark", "★4.7", "city", 53.5483, 9.9789, "聖堂無料（塔8€）", "「ミヒェル」の愛称で親しまれるバロック様式教会。高さ132mの時計塔が目印。", "毎日10:00と21:00に注目！106mの塔上からラッパ奏者が讃美歌を四方に吹奏。"),
    (7, "ハンブルク港＆ザンクト・パウリ桟橋", "Hamburg Harbor & St. Pauli Piers", "Hamburger Hafen & Landungsbrücken", "Landmark", "★4.7", "city", 53.5458, 9.9669, "桟橋無料", "1907年建造の浮き桟橋からクルーズ船が交差し、巨大コンテナ船が行き交う巨大港。", "3番桟橋からHADAGフェリー62番線に乗車！1日乗車券のまま1時間格安クルーズ。"),
    (8, "旧エルベトンネル", "Old Elbe Tunnel", "Alter Elbtunnel", "Landmark", "★4.7", "city", 53.5458, 9.9664, "通行無料", "1911年開通。エルベ川の水底24mを貫く全長426mの歴史的水底トンネル。", "トンネルを歩いて対岸Steinwerderへ！桟橋と大聖堂を正面に望むパノラマ撮影。"),
    (9, "ハーフェンシティ", "HafenCity District", "HafenCity", "Landmark", "★4.6", "city", 53.5417, 9.9986, "散策無料", "旧港湾倉庫街を最新都市へ刷新する157haの欧州最大ウォーターフロント再開発地区。", "マルコ・ポーロ・テラスへ！モダンガラスビル群と水上ボートの対比を撮影。"),
    (10, "ビンネンアルスター湖＆アウセンアルスター湖", "Alster Lakes", "Binnenalster & Außenalster", "Scenery & Walk", "★4.8", "city", 53.5539, 9.9961, "散策無料", "市中心部の2大巨大湖。高さ60mの噴水と7.4kmの周遊遊歩道が広がる。", "外湖東岸のBootshaus Barで手漕ぎボートを借りて白い高級邸宅の並ぶ水路を散策！"),
    (11, "ハンブルク美術館", "Hamburg Art Museum", "Hamburger Kunsthalle", "Museum & Gallery", "★4.7", "city", 53.5550, 10.0025, "入場料: 14€", "3つの館が繋がる美術館。フリードリヒ『雲海の上の旅人』やレンブラントを所蔵。", "旧館第16展示室へ直行！最高傑作『雲海の上の旅人』を静かに観賞。"),
    (12, "国際海洋博物館", "International Maritime Museum", "Internationales Maritimes Museum Hamburg", "Museum & Gallery", "★4.8", "city", 53.5436, 10.0003, "入場料: 17€", "赤レンガ倉庫Kaispeicher B内の海洋博物館。9階に5万隻の船模型と航海史。", "最上階Deck 9へ！捕虜が肉の骨から削り出した繊細な『骨製船模型』を見学。"),
    (13, "工芸美術館", "Museum of Arts and Crafts Hamburg", "Museum für Kunst und Gewerbe Hamburg (MK&G)", "Museum & Gallery", "★4.6", "city", 53.5511, 10.0089, "入場料: 14€", "アール・ヌーヴォー家具、ポスターグラフィック、アジア工芸コレクション。", "1900年パリ万博アール・ヌーヴォー喫茶室（Parisian Tearoom）の家具を鑑賞。"),
    (14, "ダイヒトーアハレン", "Deichtorhallen Contemporary Art", "Deichtorhallen Hamburg", "Museum & Gallery", "★4.6", "city", 53.5469, 10.0069, "入場料: 12€", "19世紀の卸売市場ホールを改装した欧州最大級の現代美術・写真展示センター。", "写真館（Haus der Photographie）の大空間で世界最高峰の大型写真を鑑賞。"),
    (15, "カプ・サン・ディエゴ号", "Cap San Diego Museum Ship", "Cap San Diego", "Landmark", "★4.7", "city", 53.5433, 9.9767, "入場料: 11€", "1961年建造の航行可能な世界最大の博物館貨物船。機関室や操舵室を探検できる。", "船底最深部の全長40mのプロペラ軸トンネル（Wellentunnel）へ潜り込んで探検！"),
    (16, "リックマー・リックマース号", "Rickmer Rickmers Sailing Ship", "Rickmer Rickmers", "Landmark", "★4.6", "city", 53.5447, 9.9675, "入場料: 7€", "1896年建造の緑色の3本マスト歴史的大型帆船博物館。甲板レストラン併設。", "甲板レストランで港を行き交う船を眺めながらハンブルク名物ビールを一杯！"),
    (17, "潜水艦博物館 U-434", "Submarine Museum U-434", "Submarine Museum U-434", "Museum & Gallery", "★4.6", "city", 53.5447, 9.9536, "入場料: 10€", "旧ソ連海軍の本物の大型ディーゼル潜水艦U-434内部を探検できる博物館。", "狭いハッチをくぐって魚雷発射管室や緊迫したソナー制御室を体感！"),
    (18, "聖ニコライ教会廃墟記念碑", "St. Nikolai Memorial Spire", "St. Nikolai Memorial (Mahnmal St. Nikolai)", "Landmark", "★4.6", "city", 53.5475, 9.9906, "廃墟無料（エレベーター6€）", "1943年大空襲で破壊されたネオ・ゴシック教会の尖塔廃墟。高さ147m。", "空洞の塔内のガラスエレベーターで地上76m展望台へ！倉庫街と市庁舎を見下ろす。"),
    (19, "プランテン・ウン・ブローメン公園", "Planten un Blomen Park", "Planten un Blomen", "Scenery & Walk", "★4.8", "city", 53.5606, 9.9819, "入園無料", "日本庭園、茶室、バラ園を備える47haの広大な中央公園。夜の光と水の噴水ショー。", "5月〜9月夜22:00にParksee湖畔へ！生演奏オルガン付き『光と水の噴水ショー』観賞。"),
    (20, "ハーゲンベック動物園＆熱帯水族館", "Tierpark Hagenbeck", "Tierpark Hagenbeck & Tropen-Aquarium", "Kids & Family", "★4.7", "city", 53.5969, 9.9372, "動物園: 29€", "1907年に世界で初めて無柵放養式（モート式）を採用した歴史的動物園。", "熱帯水族館の深海大パノラマ水槽前で巨大ザメやウミガメの泳ぎを鑑賞！"),
    (21, "アルトナの魚市場＆フィッシュオークションホール", "Altona Fish Market", "Fischmarkt (Altona)", "Shopping", "★4.6", "city", 53.5453, 9.9547, "入場無料", "1703年から続く日曜早朝限定の歴史的魚市場。威勢の良い競りとロック生演奏。", "日曜日早朝限定！赤い競売ホール内でモーニングビールを片手にロック生演奏。"),
    (22, "レーパーバーン＆ザンクト・パウリ地区", "Reeperbahn Nightlife District", "Reeperbahn & St. Pauli", "Landmark", "★4.5", "city", 53.5497, 9.9625, "散策無料", "ザンクト・パウリの歓楽街。ライブハウス、劇場、バー、ビートルズの聖地。", "Beatles-Platzへ！黒いレコード風の地面に浮かぶ4人のステンレスシルエット像と撮影。"),
    (23, "ビートルズ広場＆ゆかりのライブハウス群", "Beatles-Platz & Indra / Kaiserkeller", "Beatles-Platz & Indra Club / Kaiserkeller", "Landmark", "★4.6", "city", 53.5503, 9.9575, "見学無料", "若き日のビートルズが1960年に下積みライブを行っていた伝説のクラブ群。", "Indra Clubの青い看板前で、ビートルズが初めてステージに立った伝説の瞬間を偲ぶ。"),
    (24, "ユングフェルンシュティーク", "Jungfernstieg Boulevard", "Jungfernstieg", "Scenery & Walk", "★4.7", "city", 53.5528, 9.9928, "散策無料", "アルスター湖畔の歴史あるエレガントな遊歩道大通り・水辺テラス。", "湖畔の大階段テラスに座り、水面に浮かぶAlsterfontäne大噴水と遊覧船を眺める。"),
    (25, "アルスター・アルケード", "Alster Arcades", "Alsterarkaden", "Landmark", "★4.7", "city", 53.5511, 9.9922, "散策無料", "1843年建造のヴェネツィア風の白い連続アーチ回廊。高級ブティックとカフェ。", "運河沿いのテラス席へ！優雅に泳ぐ白鳥を眺めながら市庁舎尖塔を望むカフェタイム。"),
    (26, "メンケベルク通り＆シュピタラー通り", "Mönckebergstraße Shopping Street", "Mönckebergstraße & Spitalerstraße", "Shopping", "★4.6", "city", 53.5508, 10.0008, "散策無料", "中央駅から市庁舎へ続くハンブルク最大の歩行者天国ショッピングストリート。", "歴史的デパートKarstadt前のカフェテラスで買い物の合間に地元のプレッツェルを味わう。"),
    (27, "ノイアー・ヴァル＆グローセ・ブライヒェン", "Neuer Wall Luxury Shopping", "Neuer Wall & Große Bleichen", "Shopping", "★4.7", "city", 53.5514, 9.9889, "散策無料", "運河に挟まれた最高級デザイナーブランドブティックが並ぶエレガント街区。", "Bleichenfleet運河沿いのカフェで高級外車とエレガントな街並みを人間観察。"),
    (28, "ハンゼ・フィアテル＆オイローパ・パサージュ", "Europa Passage & Hanse-Viertel", "Hanse-Viertel & Europa Passage", "Shopping", "★4.6", "city", 53.5517, 9.9964, "入場無料", "ガラスドームパサージュと、120店が入る5階建て最新ショッピングモール。", "Europa Passage最上階のフードコートからアルスター湖の景観を見下ろしながらランチ！"),
    (29, "シャンツェン地区", "Sternschanze Quarter", "Sternschanze (Schanzenviertel)", "Scenery & Walk", "★4.7", "city", 53.5619, 9.9658, "散策無料", "サブカルチャー、ストリートアート、グラフィティ、カフェ、古着屋の街。", "旧劇場Rote Flora前で壁一面のカラフルなグラフィティアートを背景に撮影！"),
    (30, "カロリーネン地区", "Karolinenviertel District", "Karolinenviertel (Karoviertel)", "Shopping", "★4.6", "city", 53.5583, 9.9722, "散策無料", "Marktstraße通りを中心に、個性的セレクトショップやレコード店が集まる通り。", "Marktstraße沿いのヴィンテージ古着屋やハンドメイド雑貨店で掘り出し物を探す。"),
    (31, "自然博物館", "Museum of Nature - Zoology", "Museum der Natur - Hamburg", "Museum & Gallery", "★4.6", "city", 53.5678, 9.9839, "入場無料", "大学併設の自然史館。巨大なセイウチAntjeの標本やクジラ骨格を展示。", "名物セイウチAntjeのはく製標本前で記念撮影（完全入場無料です）！"),
    (32, "ハンブルク・ダンジョン", "Hamburg Dungeon", "Hamburg Dungeon", "Kids & Family", "★4.6", "city", 53.5436, 9.9897, "入場料: 26€", "倉庫街内にある、ハンブルクの暗黒史や1842年大火を再現するお化け屋敷型アトラクション。", "俳優陣によるリアルな尋問パフォーマンスと最後のみぞおちが浮く暗闇落下に身を任せる！"),
    (33, "ダイアログ・イン・ザ・ダーク", "Dialog in the Dark", "Dialog im Dunkeln (Dialoghaus Hamburg)", "Museum & Gallery", "★4.8", "city", 53.5444, 9.9961, "体験料: 19.50€", "完全な暗闇の中で全盲ガイドの案内のもと五感で世界を探検するソーシャル体験館。", "視覚ゼロの世界で手探りで公園や街角を歩く非日常の感覚を全身で体感！"),
    (34, "チョコヴェルサム", "Chocoversum Chocolate Museum", "Chocoversum by Hachez", "Museum & Gallery", "★4.7", "city", 53.5475, 10.0011, "ツアー料: 23€", "カカオの豆からチョコができる工程を学び、自分オリジナルの板チョコを作る体験館。", "トッピング（ナッツやドライフルーツ）を自由に選んで世界に一つだけのマイチョコ制作！"),
    (35, "スパイシーズ香辛料博物館", "Spicy's Spice Museum", "Spicy's Gewürzmuseum", "Museum & Gallery", "★4.6", "city", 53.5433, 9.9944, "入場料: 5€", "倉庫街の歴史あるビル内にある、世界中のスパイスに触れて香りを体験できる博物館。", "袋に入った世界各国のコショウやシナモンを直接手で触って香りを嗅ぎ比べる！"),
    (36, "ドイツ連邦税関博物館", "German Customs Museum", "Zollmuseum (Deutsches Zollmuseum)", "Museum & Gallery", "★4.5", "city", 53.5447, 9.9975, "入場料: 2€", "運河沿いの旧税関検査場内にある、密輸の歴史的手口や押収品を展示する館。", "家具や車のタイヤの中に隠された驚きの密輸工作品コレクションをじっくり鑑賞。"),
    (37, "クラーマーアムツストゥーベン", "Krameramtsstuben Guild Houses", "Krameramtsstuben", "Landmark", "★4.7", "city", 53.5492, 9.9792, "路地散策無料", "聖ミヒャエリス教会近くに残る17世紀の木骨造りギルド未亡人長屋小路。", "石畳の細い路地に一歩足を踏み入れ、17世紀にタイムスリップしたような木骨家屋を撮影。"),
    (38, "桟橋のフィッシュブレートヒェン屋台群", "Landungsbrücken Fish Roll Stalls", "Fischbrötchen-Buden an den Landungsbrücken", "Café & Bistro", "★4.6", "city", 53.5458, 9.9675, "魚パン: 4.50€", "桟橋沿いに並ぶソウルフード屋台。ニシン酢漬けや小エビを挟んだ名物パンサンド。", "10番桟橋のBrücke 10で「Bismarckhering-Brötchen（酢漬けニシンサンド）」を注文！"),
    (39, "オールド・コマーシャル・ルーム", "Old Commercial Room Restaurant", "Old Commercial Room", "Café & Bistro", "★4.6", "city", 53.5481, 9.9794, "ラブスカウス: 24€", "1795年創業の老舗船員レストラン。伝統料理「ラブスカウス（コンビーフとビーツの煮込み）」の名店。", "名物Original Hamburger Labskaus（目玉焼き、ピクルス、酢漬けニシン乗せ）を賞味！"),
    (40, "カフェ・パリ", "Café Paris Hamburg", "Café Paris (Hamburg)", "Café & Bistro", "★4.7", "city", 53.5511, 9.9936, "コーヒー: 4.50€", "1882年建造のアール・ヌーヴォー様式の美しいモザイクタイル天井を持つフレンチブラッスリー。", "天井いっぱいに描かれた産業と農業のモザイクアールヌーヴォー天井を見上げながらクロワッサン。"),
    (41, "フィッシェライハーフェン・レストラン", "Fischereihafen Restaurant", "Rive Fisch & Fischereihafen Restaurant", "Café & Bistro", "★4.8", "city", 53.5442, 9.9389, "魚料理: 32€", "エルベ川を行き交うコンテナ船を目の前に眺めながら最高級の新鮮魚介を堪能できる老舗。", "窓際の川側テーブルを予約し、夕暮れ時の巨大コンテナ船の航行を眺めながら新鮮ヒラメ料理。"),
    (42, "グレーニンガー自家醸造所", "Gröninger Private Brewery", "Gröninger Privatbrauerei", "Café & Bistro", "★4.6", "city", 53.5469, 9.9939, "自家醸造ビール: 4€", "1750年創業のハンブルク最古級の醸造所レストラン。地下の銅製醸造釜が迫力。", "地下の醸造釜の横の木製長テーブルで、無濾過の生ビールGröninger Pilsと豚ひざ肉ロースト。"),
    (43, "エルプシュトラント", "Elbstrand Beach Övelgönne", "Elbstrand (Övelgönne)", "Scenery & Walk", "★4.7", "city", 53.5439, 9.9083, "砂浜無料", "エルベ川沿いに広がる白い砂浜ビーチ。目の前を巨大コンテナ船が航行する独特の景観。", "砂浜に座って地元のAstralビール小瓶を飲みながら、すぐ目の前を通り過ぎる巨船を眺める！"),
    (44, "オイヴェルゲンネ博物館港", "Övelgönne Museum Harbor", "Museumshafen Övelgönne", "Landmark", "★4.6", "city", 53.5442, 9.9147, "見学無料", "歴史的な古い蒸気船、タグボート、クレーン船が保存・係留された屋外水上博物館。", "木製浮き桟橋を歩き、1911年建造の旧蒸気タグボートTigerのレトロな外観を撮影。"),
    (45, "ハンブルク市立公園＆プラネタリウム", "Stadtpark & Planetarium", "Stadtpark Hamburg & Planetarium Hamburg", "Scenery & Walk", "★4.7", "city", 53.5972, 10.0089, "公園無料（ショー12€）", "1916年建造の歴史的旧給水塔を利用した最先端プラネタリウムと広大な大芝生広場。", "給水塔の高さ64m展望テラス（無観覧時無料）へ登り、市立公園の緑の森を一望！"),
    (46, "イェーニッシュ公園＆イェーニッシュ・ハウス", "Jenisch Park & House", "Jenischpark & Jenisch Haus", "Scenery & Walk", "★4.7", "city", 53.5519, 9.8633, "公園無料", "エルベ川を見下ろす美しい英国式景観庭園と19世紀の新古典主義カントリーハウス。", "イェーニッシュ・ハウス南側の白い列柱テラスから、広大な芝生の斜面越しにエルベ川を望む！"),
    (47, "エネルギーブンカー・ヴィルヘルムスブルク", "Wilhelmsburg Energy Bunker", "Energiebunker Wilhelmsburg", "Landmark", "★4.6", "city", 53.5097, 9.9897, "屋上カフェ無料", "第二次大戦の高射砲塔（Flakturm）を環境再生したエネルギー拠点。高さ30m屋上カフェ。", "30m屋上テラスのCafé vJUへ！360度ガラス張りでハンブルク全景と港湾を一望。"),
    (48, "HADAG港湾定期フェリー62番線", "HADAG Harbor Ferry Line 62", "HADAG-Hafenfähren (Linie 62)", "Scenery & Walk", "★4.8", "city", 53.5458, 9.9669, "HVV乗車券適用", "3番桟橋からフィンケンヴェルダーへ向かう水上バス。普通の一日乗車券で乗車可能。", "2階オープンデッキ席を確保！ノイミューレン付近で超巨大コンテナクレーンを見上げる。"),
    (49, "ホルトフーゼンバート", "Holthusenbad Historic Spa", "Bäderland Holthusenbad", "Kids & Family", "★4.6", "city", 53.5897, 9.9919, "スパプール: 11€", "1914年建造の壮麗なアール・デコ様式の歴史的温水プール＆波のプール・サウナ。", "アール・デコ様式のガラス天井から光が差し込むクラシックな波のプールで泳ぐ！"),

    # Suburban (50-61)
    (50, "リューベック：世界遺産旧市街＆ホルステン門", "Lübeck Old Town & Holsten Gate", "Lübeck: Altstadt & Holstentor (UNESCO)", "Landmark", "★4.9", "suburban", 53.8664, 10.6797, "旧市街無料", "「ハンザ同盟の女王」世界遺産都市。1477年の赤レンガホルステン門とマジパン。", "市庁舎前の老舗Café Niedereggerで伝統のマジパン入りくるみケーキ（Marzipantorte）を食す！"),
    (51, "リューネブルク：歴史的旧市街＆ドイツ塩博物館", "Lüneburg Old Town & Salt Museum", "Lüneburg: Historische Altstadt", "Landmark", "★4.7", "suburban", 53.2489, 10.4078, "旧市街無料", "中世に塩の貿易で栄えた赤レンガ切妻屋根の美しい町並みと19世紀まで稼働した塩田跡。", "水車小屋のある旧港Am Stintemarkt沿いのテラス席で地元の地ビールと塩漬け肉料理を味わう！"),
    (52, "シュヴェリーン城", "Schwerin Castle", "Schloss Schwerin", "Landmark", "★4.9", "suburban", 53.6242, 11.4189, "宮殿: 8.50€", "シュヴェリーン湖の島に浮かぶ「北のノイシュヴァンシュタイン城」。金のドーム屋根。", "城の橋を渡り裏手のオランジェリー庭園へ！湖越しに黄金の主ドームが浮ぶ写真を撮影。"),
    (53, "シュターデ＆アルテス・ラント", "Stade & Altes Land Orchards", "Stade & Altes Land", "Scenery & Walk", "★4.7", "suburban", 53.6022, 9.4764, "散策無料", "欧州最大の果樹園地帯アルテス・ラントと、木骨造りの美しい運河の町シュターデ。", "春（5月）のリンゴとサクランボの満開の時期に自転車を借りて果樹園の白い花道をサイクリング！"),
    (54, "クックスハーフェン＆世界遺産ワッデン海", "Cuxhaven & Wadden Sea", "Cuxhaven & Wattenmeer (UNESCO)", "Scenery & Walk", "★4.8", "suburban", 53.8731, 8.6942, "海岸無料", "北海沿岸の世界自然遺産ワッデン海干潟。干潟を渡る馬車（Wattwagen）が名物。", "引き潮時にシャランド馬車（Wattwagen）に乗って海の中を渡りNeuwerk島へ渡る感動体験！"),
    (55, "ヘルゴラント島", "Heligoland Island", "Helgoland", "Scenery & Walk", "★4.8", "suburban", 54.1806, 7.8889, "高速船: 85€往復", "ハンブルクからカタマラン高速船でアクセスする北海の赤色断崖絶壁の孤島。無税の島。", "赤い断崖のハイキングコースを歩き、名物赤岩「Lange Anna」と崖に巣作るウミガラスを観察！"),
    (56, "ブレーマーハーフェン：移民ハウス＆気候館", "Bremerhaven Emigration & Climate House", "Bremerhaven: Auswandererhaus & Klimahaus", "Museum & Gallery", "★4.8", "suburban", 53.5439, 8.5708, "各館: 20€", "欧州最大の移民博物館「ドイツ移民ハウス」と、東経8度線を世界一周体験する「気候館」。", "気候館8°Ostで、赤道直下のサモアの熱帯雨林から南極のマイナス6度極寒室まで体を張って体感！"),
    (57, "ノイエンガンメ強制収容所記念館", "Neuengamme Concentration Camp Memorial", "KZ-Gedenkstätte Neuengamme", "Landmark", "★4.7", "suburban", 53.4297, 10.2319, "入場無料", "北ドイツ最大の旧ナチス強制収容所跡地。広大な敷地に保存された収容棟跡と展示室。", "中央ドキュメンテーションセンターで音声ガイドを借り、静寂に包まれた広大な遺構を歩く。"),
    (58, "アーレンスブルク城", "Ahrensburg Palace", "Schloss Ahrensburg", "Landmark", "★4.6", "suburban", 53.6797, 10.2403, "城館: 9€", "1595年建造の白亜のルネサンス様式水城。水堀に浮かぶロココ装飾の美しい城郭。", "城を囲む水堀の橋の上から、水面に完璧に映り込む真っ白な三連切妻屋根の城館を撮影。"),
    (59, "シュヴァルツェ・ベルゲ野生動物公園", "Black Mountains Wildlife Park", "Wildpark Schwarze Berge", "Kids & Family", "★4.7", "suburban", 53.4419, 9.8919, "入場料: 14€", "ハンブルク南部の広大な森にある自然動物公園。高さ45mの木造展望塔Elbblick。", "高さ45mの木造塔Elbblickに登り、森の樹海越しに遥かハンブルクの街並みを一望！"),
    (60, "ハイデ・パーク・リゾート", "Heide Park Resort", "Heide Park Resort", "Kids & Family", "★4.7", "suburban", 53.0242, 9.8786, "入園料: 44€", "ソルタウにある北ドイツ最大の遊園地。木造絶叫コースター「Colossos」が名物。", "欧州最大の木造ジェットコースターColossosの最高点（52m）からの急降下スリルを体感！"),
    (61, "デザイナー・アウトレット・ノイミュンスター", "Neumünster Designer Outlet", "Designer Outlet Neumünster / Soltau", "Shopping", "★4.6", "suburban", 54.0539, 9.9472, "入館無料", "120以上のハイブランドが30〜70%オフで並ぶ北ドイツ最大級のアウトレット。", "ハンブルク中央駅からRE7でNeumünsterへ行き7/77バスで直行！インフォで10%オフ券入手。")
]

# ----------------------------------------------------
# 2. BERLIN 75 SPOTS DEFINITION
# ----------------------------------------------------
ber_raw = [
    # City 1-60
    (1, "ブランデンブルク門", "Brandenburg Gate", "Brandenburger Tor", "Landmark", "★4.8", "city", 52.5163, 13.3777, "見学無料", "東西冷戦の分断と統一の象徴。1791年建造の新古典主義の門と四頭立て馬車像。", "夕刻のブルーアワーにパリ広場東側から西向きに撮影！黄金照明の列柱が幻想的。"),
    (2, "連邦議会議事堂", "Reichstag Building & Dome", "Reichstagsgebäude", "Landmark", "★4.8", "city", 52.5186, 13.3761, "無料（要事前Web予約）", "ノーマン・フォスター設計のガラスドーム内部から本会議場を見下ろせる国会議事堂。", "無料ですがbundestag.deでの数週間前予約が必須！当日はパスポート原本持参。"),
    (3, "博物館島", "Museum Island (UNESCO)", "Museumsinsel (UNESCO)", "Museum & Gallery", "★4.9", "city", 52.5206, 13.3978, "共通券: 19€", "シュプレー川の中州に5つの世界的美術館が集結するユネスコ世界文化遺産。", "博物館島共通券（Museumsinsel-Pass €19）を購入して1日で複数館を制覇！"),
    (4, "ペルガモン博物館", "Pergamon Museum", "Pergamonmuseum", "Museum & Gallery", "★4.8", "city", 52.5211, 13.3969, "入場料: 12€", "バビロニアの『イシュタール門』や『ミレトスの市場門』など古代巨大建築の復元展示。", "主ホール改修中は別館『Pergamonmuseum. Das Panorama』で360度パノラマ展を観賞！"),
    (5, "新博物館", "Neues Museum", "Neues Museum", "Museum & Gallery", "★4.8", "city", 52.5203, 13.3978, "入場料: 14€", "3,300年前のエジプト王妃『ネフェルティティの胸像』を所蔵する殿堂。", "2階第210展示室へ直行！ネフェルティティの胸像の正面へ（※室内写真撮影厳禁）。"),
    (6, "旧国立美術館", "Alte Nationalgalerie", "Alte Nationalgalerie", "Museum & Gallery", "★4.7", "city", 52.5208, 13.3983, "入場料: 12€", "19世紀絵画の殿堂。フリードリヒ、マネ、モネ、ロダンの彫刻を展示。", "フリードリヒの傑作『海辺の修道士』前でロマン派絵画の静寂に浸る。"),
    (7, "ボーデ博物館", "Bode Museum", "Bode-Museum", "Museum & Gallery", "★4.7", "city", 52.5219, 13.3947, "入場料: 12€", "シュプレー川の先端に立つ宮殿風建築。ビザンチン美術と中世彫刻コレクション。", "川に突き出た正面ドームグレートホールを見上げる水上アングルを橋から撮影！"),
    (8, "旧博物館", "Altes Museum", "Altes Museum", "Museum & Gallery", "★4.6", "city", 52.5194, 13.3986, "入場料: 10€", "シンケル設計の新古典主義名建築。ギリシャ・ローマの古代彫刻を展示。", "正面の18本のイオニア式大列柱の間に立ち、対面のベルリン大聖堂を額縁撮影！"),
    (9, "ベルリン大聖堂", "Berlin Cathedral", "Berliner Dom", "Landmark", "★4.7", "city", 52.5192, 13.4011, "拝観料: 10€", "緑のドームが美しい1905年完成の大聖堂。ホーエンツォレルン家墓所と展望回廊。", "270段の階段を登ってドーム外周回廊（Domkuppel）へ！全方位パノラマ撮影。"),
    (10, "フンボルト・フォーラム＆ベルリン王宮", "Humboldt Forum", "Humboldt Forum & Berliner Schloss", "Landmark", "★4.7", "city", 52.5175, 13.4028, "常設無料", "再建されたベルリン王宮内の巨大文化施設。民族学博物館とアジア美術館。", "屋上テラスRoof Terraceへ！ベルリン大聖堂のドームとテレビ塔を同時に見下ろす。"),
    (11, "イーストサイドギャラリー", "East Side Gallery", "East Side Gallery", "Landmark", "★4.6", "city", 52.5050, 13.4397, "見学無料", "ベルリンの壁の現存最長1.3km区間。105作品の国際的壁画ギャラリー。", "Mühlenstraße 60付近へ！有名壁画『兄弟のキス（The Brother Kiss）』前で撮影。"),
    (12, "ベルリンの壁記念館", "Berlin Wall Memorial", "Gedenkstätte Berliner Mauer (Bernauer Straße)", "Landmark", "★4.8", "city", 52.5353, 13.3903, "見学無料", "監視塔や無人地帯が当時のまま保存されたベルナウアー通りの野外記念館。", "ドキュメンテーションセンター屋上展望台から無人地帯（死亡地帯）の全体構造を直視。"),
    (13, "チェックポイント・チャーリー＆壁博物館", "Checkpoint Charlie", "Checkpoint Charlie & Mauermuseum", "Landmark", "★4.5", "city", 52.5075, 13.3903, "見学無料（博物館17.50€）", "冷戦時代の米ソ東西検問所跡地。米軍兵士の小屋と写真看板が立つ。", "検問所小屋の前で星条旗と米兵アクター（有償写真）と一緒に記念撮影！"),
    (14, "トポグラフィー・オブ・テラー", "Topography of Terror", "Topographie des Terrors", "Museum & Gallery", "★4.7", "city", 52.5064, 13.3839, "入場無料", "旧ゲシュタポ・SS本部跡地に立つナチス犯罪の歴史ドキュメンテーション館。", "残存するベルリンの壁の露出遺構に沿って設置された屋外写真パネルを巡る。"),
    (15, "ホロコースト慰霊碑", "Holocaust Memorial", "Denkmal für die ermordeten Juden Europas", "Landmark", "★4.6", "city", 52.5139, 13.3786, "入場無料", "2,711基のグリッド状コンクリート柱（ステレ）。地下に情報センターを併設。", "敷地東角の階段から地下情報センター（Ort der Information）へ！犠牲者の遺書を閲覧。"),
    (16, "ベルリンテレビ塔", "Berlin TV Tower", "Berliner Fernsehturm", "Landmark", "★4.6", "city", 52.5208, 13.4094, "展望台: 22.50€", "高さ368mのドイツ最高タワー。地上203mのパノラマ展望台と回転レストラン。", "午後は大行列になるため、公式サイトでFast Track（優先入場）Webチケットを事前購入！"),
    (17, "アレクサンダー広場＆世界時計", "Alexanderplatz & World Clock", "Alexanderplatz & Weltzeituhr", "Landmark", "★4.5", "city", 52.5219, 13.4131, "散策無料", "旧東ベルリンの中心大広場。世界各都市の現在時刻を示す世界時計が有名。", "回転する世界時計（Weltzeituhr）の自分の母国都市の都市名パネル下で撮影！"),
    (18, "ジャンダルメンマルクト", "Gendarmenmarkt", "Gendarmenmarkt", "Landmark", "★4.8", "city", 52.5136, 13.3928, "見学無料", "フランス大聖堂、ドイツ大聖堂、コンツェルトハウスが立ち並ぶ美しい広場。", "広場中央のシラー像前からツインタワー大聖堂が左右対称に収まる構図を撮影！"),
    (19, "カイザー・ヴィルヘルム記念教会", "Kaiser Wilhelm Memorial Church", "Kaiser-Wilhelm-Gedächtniskirche", "Landmark", "★4.6", "city", 52.5047, 13.3353, "入場無料", "空襲で破壊された旧教会の廃墟塔と、青い青層ガラスで囲まれた新大聖堂。", "八角形の新教会内部へ！2万枚の青いチャートレスブルーのガラス壁が放つ青光を体感。"),
    (20, "シャルロッテンブルク宮殿", "Charlottenburg Palace", "Schloss Charlottenburg", "Landmark", "★4.7", "city", 52.5206, 13.2958, "宮殿: 12€（庭園無料）", "ベルリン最大のホーエンツォレルン家宮殿。豪華なバロック・ロココ様式の部屋。", "本館裏手の庭園を歩き湖畔のベルヴェデーレ茶室（Belvedere）でカフェ休憩！"),
    (21, "絵画館（クルトゥールフォルム）", "Gemäldegalerie Art Gallery", "Kulturforum & Gemäldegalerie", "Museum & Gallery", "★4.8", "city", 52.5086, 13.3644, "入場料: 14€", "フェルメール2点、レンブラント16点、ラファエロを所蔵する欧州古典絵画の最高峰。", "フェルメールの『真珠の首飾りの女』と『ワイングラスを持つ娘』が並ぶ展示室へ！"),
    (22, "新国立美術館", "Neue Nationalgalerie", "Neue Nationalgalerie", "Museum & Gallery", "★4.7", "city", 52.5067, 13.3675, "入場料: 14€", "ミース・ファン・デル・ローエ設計のガラスと鉄のモダニズム名建築。20世紀美術。", "ガラス張りの平屋アトリウムの大空間に展示された巨大現代彫刻を外から撮影。"),
    (23, "ハンブルガー・バーンホフ現代美術館", "Hamburger Bahnhof Contemporary Art", "Hamburger Bahnhof", "Museum & Gallery", "★4.6", "city", 52.5283, 13.3719, "入場料: 14€", "19世紀の旧鉄道駅校舎を改装した大型現代アート館。ヨーゼフ・ボイスやウォーホル。", "旧駅舎の巨大な列車発着大ホール（Rieckhallen）に設置された巨大インスタレーションを鑑賞！"),
    (24, "ユダヤ博物館", "Jewish Museum Berlin", "Jüdisches Museum Berlin", "Museum & Gallery", "★4.7", "city", 52.5022, 13.3953, "入場料: 10€", "ダニエル・リベスキンド設計のジグザグ建築。ホロコーストの塔や記憶のヴォイド。", "「亡命の庭（Garden of Exile）」の傾斜した49本のコンクリート柱の間を歩き眩暈を体験。"),
    (25, "ドイツ歴史博物館", "German Historical Museum", "Deutsches Historisches Museum (DHM)", "Museum & Gallery", "★4.7", "city", 52.5178, 13.3969, "入場料: 10€", "バロック様式の旧武器庫ツォイクハウスとI.M.ペイ設計のガラスのらせん階段新館。", "I.M.ペイ設計の新館（Exhibition Hall）のガラスらせん階段で光のアートショットを撮影！"),
    (26, "ドイツ技術博物館＆スペクトラム", "German Museum of Technology", "Deutsches Technikmuseum", "Museum & Gallery", "★4.8", "city", 52.4986, 13.3775, "入場料: 12€", "蒸気機関車、航空機、大型船を実物展示。屋上に「キャンディ・ボマー」飛行機が載る。", "屋外展示場の蒸気機関車扇形車庫（Rundlokschuppen）で本物の黒い蒸気機関車に乗る！"),
    (27, "ベルリン自然史博物館", "Berlin Natural History Museum", "Museum für Naturkunde", "Museum & Gallery", "★4.7", "city", 52.5297, 13.3797, "入場料: 11€", "世界最大の全身骨格マウント（13.27mのギラファティティン）と始祖鳥化石。", "正面アトリウムへ直行！高さ13.27mの恐竜骨格ギラファティティンの真下から見上げる。"),
    (28, "フトゥリウム", "Futurium", "Futurium", "Museum & Gallery", "★4.7", "city", 52.5239, 13.3742, "入場無料", "「未来」をテーマにした参加型最新ミュージアム。バイオテクノロジーとロボティクス。", "リストバンドをかざして未来の生活シナリオ（都市・エネルギー・食）に投票参加！"),
    (29, "コンピュータゲーム博物館", "Computer Games Museum", "Computerspielemuseum", "Museum & Gallery", "★4.5", "city", 52.5175, 13.4419, "入場料: 11€", "1970年代のレトロアーケード筐体から現代VRまでの体験型ゲーム博物館。", "コイン不要で遊べる1980年代のレトロアーケード筐体で『パックマン』や『Space Invaders』に挑戦！"),
    (30, "ドイツスパイ博物館", "German Spy Museum", "Spionagemuseum (German Spy Museum)", "Museum & Gallery", "★4.6", "city", 52.5094, 13.3794, "入場料: 15€", "冷戦期のエニグマ暗号機から映画『007』の秘密道具、レーザーアトラクション。", "「レーザー障害物コース（Laser Maze）」でスパイになりきってレーザーを避けてタイムアタック！"),
    (31, "DDR博物館", "DDR Museum", "DDR Museum", "Museum & Gallery", "★4.5", "city", 52.5197, 13.4028, "入場料: 12.50€", "旧東ドイツの生活（トラバント乗車、団地部屋再現）を五感で体験する館。", "本物の東ドイツ車「トラバント（Trabant）」の運転席に座ってシミュレータードライブ！"),
    (32, "ベルリン地下世界ツアー", "Berlin Underground Tours", "Berliner Unterwelten", "Landmark", "★4.8", "city", 52.5483, 13.3889, "ツアー: 16€", "二戦の防空壕、高射砲塔廃墟、冷戦脱出トンネルを巡る地下歴史ガイドツアー。", "🧥 年間通して地下施設は気温10℃前後と極寒です！真夏でも暖かい上着を持参。"),
    (33, "戦勝記念塔＆大ティーアガルテン", "Victory Column & Tiergarten", "Siegessäule & Großer Tiergarten", "Landmark", "★4.7", "city", 52.5144, 13.3503, "公園無料（塔4€）", "高さ67mの戦勝記念塔。頂上に黄金の勝利の女神像「ゴールド・エルゼ」が輝く。", "285段の螺旋階段を登って展望台へ！ブランデンブルク門へ一直線に伸びる大通りを撮影。"),
    (34, "ポツダム広場＆ソニーセンター", "Potsdamer Platz & Sony Center", "Potsdamer Platz & Sony Center", "Landmark", "★4.6", "city", 52.5097, 13.3728, "見学無料", "富士山を模した巨大なガラス張りテント屋根建築を持つ近代摩天楼広場。", "ソニーセンター中央広場で見上げる富士山型テント屋根の夜間イルミネーションを撮影！"),
    (35, "クーダム＆タウエンツィエン通り", "Kurfürstendamm Shopping Street", "Kurfürstendamm (Ku'damm) & Tauentzienstraße", "Shopping", "★4.6", "city", 52.5036, 13.3253, "散策無料", "西ベルリンを代表する大ブティックショッピングストリート。プラタナス並木。", "並木のカフェテラスで高級ブランドショップのウィンドーを眺めながらカフェタイム。"),
    (36, "カーデーヴェー百貨店", "KaDeWe Department Store", "KaDeWe (Kaufhaus des Westens)", "Shopping", "★4.7", "city", 52.5017, 13.3411, "入館無料", "1907年創業の欧州最大級の老舗デパート。6階の巨大高級グルメフロアが世界的に有名。", "6階のFeinschmeckeretageへ直行！カキ（Oyster Bar）や焼き立てソーセージをスタンドで堪能。"),
    (37, "モール・オブ・ベルリン", "Mall of Berlin", "Mall of Berlin", "Shopping", "★4.5", "city", 52.5108, 13.3806, "入館無料", "ポツダム広場近くにある300以上のショップが入る最新の巨大モール。", "3階の欧州最大級のフードコートで世界各国の料理を選んでカジュアルランチ！"),
    (38, "ビキニ・ベルリン", "Bikini Berlin Concept Mall", "Bikini Berlin", "Shopping", "★4.6", "city", 52.5053, 13.3364, "入館無料", "ベルリン動物園のサルの飼育エリアをガラス越しに眺められるコンセプトモール。", "2階の「Zoo Window」大ガラス窓へ！隣接する動物園のサル山を上から眺めながらコーヒー。"),
    (39, "ハッケシャー・ヘーフェ＆ハッケシャー・マルクト", "Hackesche Höfe Courtyards", "Hackesche Höfe & Hackescher Markt", "Landmark", "★4.7", "city", 52.5244, 13.4022, "散策無料", "アール・ヌーヴォー様式の美しい8つの繋がる中庭群。セレクトショップやカフェ。", "Hof 1のアウグスト・エンドル設計の青と白のモザイクタイル中庭壁面を撮影！"),
    (40, "マウアーパーク＆日曜蚤の市", "Mauerpark & Sunday Market", "Mauerpark & Flohmarkt", "Scenery & Walk", "★4.6", "city", 52.5414, 13.4031, "入園無料", "旧壁跡地の公園。日曜日に開催される大規模フリーマーケットと野外カラオケ（Bearpit）が名物。", "日曜日15:00に円形劇場（Amphitheatre）へ！熱狂的な名物「野外カラオケ」を立ち見観賞。"),
    (41, "マルクトハレ・ノイン", "Markthalle Neun Market", "Markthalle Neun", "Shopping", "★4.6", "city", 52.5019, 13.4319, "入場無料", "1891年開業の歴史的屋内市場。木曜夜の「Street Food Thursday」が爆発的人気。", "木曜日17:00〜22:00のStreet Food Thursdayへ！世界中の屋台グルメを食べ歩き。"),
    (42, "コルヴィッツ広場＆プレンツラウアー・ベルク", "Kollwitzplatz Quarter", "Kollwitzplatz & Prenzlauer Berg", "Scenery & Walk", "★4.7", "city", 52.5361, 13.4169, "散策無料", "19世紀末の石造建築が残る洗練されたカフェ街と土曜日のオーガニックマーケット。", "土曜日のオーガニック青空市（Ökomarkt）で焼きたての天然酵母パンとチーズを試食。"),
    (43, "ベルクマン通り＆クロイツベルク", "Bergmannstraße Quarter", "Bergmannstraße & Kreuzberg", "Scenery & Walk", "★4.6", "city", 52.4892, 13.3886, "散策無料", "ボヘミアンな多文化カルチャー街。古着屋、古本屋、カフェ、ヴィンテージショップ。", "Marheineke Markthalle屋内市場で新鮮な地中海風オリーブデリを購入して軽食。"),
    (44, "RAWゲレンデ", "RAW Complex Cultural Center", "RAW-Gelände", "Scenery & Walk", "★4.5", "city", 52.5064, 13.4542, "入場無料", "旧鉄道修理工場跡地を利用したオルタナティブ文化拠点。グラフィティ、クラブ、マーケット。", "壁一面のダイナミックなストリートアートグラフィティを背景にパンク風写真を撮影！"),
    (45, "ホルツマルクト25", "Holzmarkt 25 Creative Village", "Holzmarkt 25", "Scenery & Walk", "★4.7", "city", 52.5108, 13.4283, "散策無料", "シュプレー川沿いの木造エコ・クリエイティブヴィレッジ。オープンエアカフェバー。", "川沿いの木製デッキの焚き火台横でクラフトビールを飲みながら夕日を眺める。"),
    (46, "ベルリン動物園＆水族館", "Berlin Zoo & Aquarium", "Zoologischer Garten Berlin & Aquarium Berlin", "Kids & Family", "★4.8", "city", 52.5078, 13.3378, "動物園: 17.50€", "1844年開園のドイツ最古の動物園。世界最多の約1,400種・20,000頭の動物を飼育。", "中国から寄贈されたジャイアントパンダ館（Panda Garden）で竹を食べるパンダを観察！"),
    (47, "ティーアパーク・ベルリン", "Tierpark Berlin", "Tierpark Berlin & Schloss Friedrichsfelde", "Kids & Family", "★4.7", "city", 52.5008, 13.5289, "入場料: 17.50€", "旧東ベルリン側にある160haの欧州最大級の敷地面積を誇る広大な景観動物園。", "電気ミニトレイン（無料）に乗って広大なサバンナエリアや旧フリードリヒスフェルデ城を巡る！"),
    (48, "テンペルホーフ空港跡地公園", "Tempelhof Airport Park", "Tempelhofer Feld", "Scenery & Walk", "★4.8", "city", 52.4731, 13.4039, "入園無料", "歴史的旧空港の380haの巨大幅滑走路をそのまま開放した市民公園。", "かつて旅客機が離着陸した滑走路の真ん中でサイクリングやインラインスケート！"),
    (49, "世界の庭園", "Gardens of the World", "Gärten der Welt", "Scenery & Walk", "★4.7", "city", 52.5400, 13.5764, "入場料: 7€", "マルツァーンにある世界各国の庭園（日本庭園、中国庭園、迷路）とロープウェイ。", "展望台クラウドワン（Wolkenhain）へ登るロープウェイSeilbahnに乗って空中散歩！"),
    (50, "シュプレー川観光クルーズ船", "Spree River Cruise", "Spree-Schifffahrt (Spree River Cruise)", "Scenery & Walk", "★4.7", "city", 52.5175, 13.4014, "クルーズ: 19€", "シュプレー川から国会議事堂、博物館島、テレビ塔を水上から巡る1時間定番観光ルート。", " Friedrichstraße桟橋から屋根付き遊覧船に乗船！橋の下をくぐる瞬間の景色を撮影。"),
    (51, "バーデシッフ", "Badeschiff Floating Pool", "Badeschiff", "Scenery & Walk", "★4.5", "city", 52.4969, 13.4528, "プール: 8€", "シュプレー川の中に浮かべられた貨物船バージを改造した屋外水上プール＆ビーチバー。", "夏場に水上プールに浸かりながら、対岸のオベルバウム橋（Oberbaumbrücke）を眺める！"),
    (52, "カリー36＆コノプケ", "Curry 36 & Konnopke's Currywurst", "Curry 36 & Konnopke's Imbiß", "Café & Bistro", "★4.6", "city", 52.4894, 13.3872, "カリーヴルスト: 4.50€", "ベルリンのソウルフード「カリーヴルスト（カレーソーセージ）」の2大名物屋台。", "「Currywurst ohne Darm mit Pommes Mayo（皮なしカレーソーセージ＋ポテトマヨ添え）」と注文！"),
    (53, "ムスタファズ・ゲミューゼドネル", "Mustafa's Vegetable Kebab", "Mustafa's Gemüsedöner", "Café & Bistro", "★4.7", "city", 52.4892, 13.3875, "ケバブ: 7.10€", "世界的に有名な大行列のドネルケバブ店。香ばしいチキン、素揚げ野菜、フェタチーズ。", "昼夜45分待ち！並び時間を縮めるなら開店直後の11:00前か夜23:00以降のオフピーク。"),
    (54, "カフェ・アインシュタイン本店", "Café Einstein Stammhaus", "Café Einstein Stammhaus", "Café & Bistro", "★4.6", "city", 52.5019, 13.3606, "コーヒー: 5€", "19世紀の優雅なヴィラでウィーン風カフェ文化と本格アプフェルシュトゥルーデルを味わう老舗。", "クラシックな木製椅子で自家製温かいアップルパイ（Apfelstrudel）にバニラソースを添えて食す！"),
    (55, "プラーター・ビアガーデン", "Prater Beer Garden", "Prater Biergarten", "Café & Bistro", "★4.7", "city", 52.5397, 13.4103, "ビール: 4.50€", "1837年創業のベルリン最古の屋外ビアガーデン。大樹の木陰の木製長テーブル。", "大樹の木陰の木製ベンチで、焼き立ての地元のプレッツェルと自家製Prater Pils生ビール！"),
    (56, "ニコライ地区＆ゲオルグブロイ", "Nikolaiviertel & Georgbræu Brewery", "Brauhaus Georgbræu & Nikolaiviertel", "Landmark", "★4.6", "city", 52.5169, 13.4072, "散策無料", "ベルリン発祥の地とされる中世風小路街区と、自家醸造ビールレストラン。", "ゲオルグブロイのテラス席で、シュプレー川を眺めながら自家醸造黒ビールGeorg-Dunkel！"),
    (57, "アノハ・子供の世界", "ANOHA Children's World", "ANOHA - Die Kinderwelt des Jüdischen Museums", "Kids & Family", "★4.9", "city", 52.5017, 13.3931, "入場無料（要予約）", "ノアの箱舟をテーマにした巨大木製遊具と150匹の彫刻動物が集まるキッズ体験館。", "高さ11mの巨木製ノアの箱舟の内部のネット仕掛けや滑り台で子供と一緒に遊ぶ（無料要予約）。"),
    (58, "レゴランド・ディスカバリー・センター", "Lego Discovery Centre Berlin", "Loxx / Lego Discovery Centre Berlin", "Kids & Family", "★4.5", "city", 52.5097, 13.3736, "入場料: 21€", "ソニーセンター内にある屋内レゴテーマパーク。ベルリンの街並みを再現したミニランド。", "レゴブロックで精密に再現されたブランデンブルク門や国会議事堂のミニランドを鑑賞！"),
    (59, "シーライフ・ベルリン", "SEA LIFE Berlin", "AquaDom & SEA LIFE Berlin", "Kids & Family", "★4.4", "city", 52.5197, 13.4028, "入場料: 19€", "アレクサンダー広場近くの室内大型水族館。5,000匹以上の海洋生物と水中トンネル。", "タッチプール（Interactive Rockpool）で本物のヒトデやヤドカリに触れる体験！"),
    (60, "リキッドローム", "Liquidrom Thermal Bath", "Liquidrom", "Scenery & Walk", "★4.7", "city", 52.5036, 13.3814, "スパ: 24.50€", "水中音楽が流れる幻想的な塩水温水ドームプールと、北欧風サウナ複合施設。", "暗闇のドーム型温水プール（Soundpool）にぷかぷか浮きながら、水中で響くヒーリング音楽を体験！"),

    # Suburban 61-75
    (61, "サンスーシ宮殿＆サンスーシ公園", "Sanssouci Palace & Park", "Schloss Sanssouci & Park Sanssouci (Potsdam / UNESCO)", "Landmark", "★4.9", "suburban", 52.4042, 13.0385, "宮殿: 14€（公園無料）", "フリードリヒ大王の夏の離宮（1747年完成・世界遺産）。ブドウの段々畑の頂に立つ黄色のロココ宮殿。", "噴水広場からブドウ畑の階段を登る途中で撮影！ブドウ棚越しに黄色の宮殿を仰ぎ見る。"),
    (62, "新宮殿（ポツダム）", "New Palace in Sanssouci", "Neues Palais (Potsdam)", "Landmark", "★4.8", "suburban", 52.4014, 13.0158, "宮殿: 14€", "サンスーシ公園西端に建つプロイセン屈指の巨大バロック宮殿。200以上の豪華な客室。", "貝殻や鉱物が敷き詰められた狂気の豪華さを持つ「貝殻の間（Grottensaal）」を鑑賞！"),
    (63, "ツェツィーリエンホーフ宮殿", "Cecilienhof Palace", "Schloss Cecilienhof (Potsdam)", "Landmark", "★4.7", "suburban", 52.4192, 13.0706, "入場料: 12€", "1917年建造のチューダー様式英国風宮殿。1945年ポツダム会談が開催された歴史の舞台。", "大ホール（Great Hall）内部へ！ポツダム協定が署名された特注の赤い木製丸テーブルを観賞。"),
    (64, "オランダ街（ポツダム）", "Dutch Quarter Potsdam", "Holländisches Viertel (Potsdam)", "Landmark", "★4.6", "suburban", 52.4025, 13.0608, "散策無料", "18世紀にオランダ人職人のために建てられた134棟の赤レンガ造りオランダ風住宅街。", "赤レンガの住宅が並ぶMittelstraße沿いの可愛いカフェでポツダム名物のパンケーキ！"),
    (65, "バルベリーニ美術館（ポツダム）", "Museum Barberini Potsdam", "Museum Barberini (Potsdam)", "Museum & Gallery", "★4.8", "suburban", 52.3958, 13.0614, "入場料: 16€", "モネの『睡蓮』や『積みわら』など印象派絵画の世界的大コレクションを所蔵する美術館。", "ハッサ・プラットナー財団のモネ作品39点が一堂に会するモネ展示室へ直行！"),
    (66, "グリーニケ橋（スパイの橋）", "Bridge of Spies (Glienicke Bridge)", "Glienicker Brücke (Potsdam / Berlin)", "Landmark", "★4.6", "suburban", 52.4131, 13.0903, "通行無料", "米ソ冷戦時代に捕虜や秘密諜報員（スパイ）の交換が行われた「スパイの橋」。", "橋の中央部道路へ！旧米軍区画とソ連軍区画を分けていた境界線ペイントの上に立って撮影。"),
    (67, "フィルムパーク・バーベルスベルク", "Filmpark Babelsberg", "Filmpark Babelsberg (Potsdam)", "Kids & Family", "★4.5", "suburban", 52.3864, 13.1169, "入場料: 23€", "世界最古の映画撮影所スタジオ併設のテーマパーク。映画スタントショーやセット。", "火山アリーナ（Vulkan Arena）で開催される迫力満点のアクションスタントショーを観賞！"),
    (68, "ザクセンハウゼン強制収容所記念館", "Sachsenhausen Concentration Camp Memorial", "KZ-Gedenkstätte Sachsenhausen (Oranienburg)", "Landmark", "★4.8", "suburban", 52.7658, 13.2642, "入場無料", "ベルリン近郊のオラーニエンブルクにある元ナチス強制収容所跡地・歴史学習施設。", "オーディオガイドを借りて、三角形の収容所敷地中央の「A塔」ゲートをくぐり静かに見学。"),
    (69, "シュプレーヴァルト", "Spreewald Biosphere Reserve", "Spreewald (Lübbenau / Lehde - UNESCO)", "Scenery & Walk", "★4.9", "suburban", 51.8686, 13.9669, "散策無料", "ユネスコ生物圏保存地域。1,500km超の網の目水路を船頭が竿で操る木造小船カーン巡り。", "リュッベナウ港から木造船Kahnに乗船！水上売店で特産の新鮮な瓶詰めピクルスを購入。"),
    (70, "トロピカル・アイランズ", "Tropical Islands Resort", "Tropical Islands Resort (Krausnick)", "Kids & Family", "★4.7", "suburban", 52.0389, 13.7483, "1日券: 47.90€", "飛行船格納庫を改造した全天候型屋内熱帯雨林リゾート。26℃恒温、白砂ビーチ。", "24時間営業！ドーム内の室内砂浜のサファリテントに宿泊するユニーク体験が人気。"),
    (71, "クジャク島", "Peacock Island (UNESCO)", "Pfaueninsel (UNESCO)", "Scenery & Walk", "★4.7", "suburban", 52.4347, 13.1292, "渡し船: 6€", "ハーフェル川に浮かぶ白亜の離宮と放し飼いのクジャクが生息する無人島（世界遺産）。", "小さな渡し船で島へ渡り、放し飼いにされた美しいクジャクが羽を広げる瞬間を撮影！"),
    (72, "ヴァンゼー湖＆ヴァンゼー会議記念館", "Wannsee & Conference House", "Wannsee & Haus der Wannsee-Konferenz", "Landmark", "★4.6", "suburban", 52.4331, 13.1644, "記念館無料", "湖畔のリゾート地と、1942年にナチスがユダヤ人絶滅計画を協議した歴史的別荘館。", "湖畔の高級別荘地を散策後、歴史的会議室のテーブル展示でナチスの歴史を学ぶ。"),
    (73, "トイフェルスベルク", "Teufelsberg Field Station", "Teufelsberg", "Scenery & Walk", "★4.7", "suburban", 52.4969, 13.2408, "入場料: 10€", "冷戦期に米軍が使ったレーダースパイ基地跡。巨大なレーダードームとグラフィティの聖地。", "白いくずれたレーダードーム内部の驚異的なエコー反響音を体験し、屋上からベルリンを一望！"),
    (74, "シュパンダウ要塞", "Spandau Citadel", "Zitadelle Spandau", "Landmark", "★4.7", "suburban", 52.5411, 13.2125, "入場料: 4.50€", "16世紀ルネサンス様式の完全に保存された水上要塞。見張り塔ジュリウス塔（Juliusturm）。", "要塞内で最も古いジュリウス塔（Juliusturm）の螺旋階段を登りハーフェル川の合流点を撮影。"),
    (75, "デザイナー・アウトレット・ベルリン", "Designer Outlet Berlin", "Designer Outlet Berlin (Wustermark)", "Shopping", "★4.6", "suburban", 52.5417, 13.0039, "入館無料", "ベルリン近郊ヴスターマルクにある90以上の人気ブランドが集まる大型アウトレット。", "ポツダム広場発着のVIPシャトルバスまたはRE4列車＋663バスで快適買い物アクセス！")
]

# Generate spot objects
def build_and_save(city_key, raw_data, city_name_str):
    spots = []
    for item in raw_data:
        spots.append(make_spot(city_key[0], item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11]))
    
    out_path = f"data/cities/{city_key}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({"cityName": city_name_str, "spots": spots}, f, ensure_ascii=False, indent=2)
    print(f"🎉 Successfully built {out_path} with ALL {len(spots)} SPOTS!")

build_and_save("hamburg", ham_raw, "Hamburg, Germany")
build_and_save("berlin", ber_raw, "Berlin, Germany")
