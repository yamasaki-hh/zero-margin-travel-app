import json

def make_spot(num, name_ja_str, name_en_str, name_de_str, cat, rating, zone, lat, lng, price_ja, desc_ja, tip_ja):
    return {
        "id": f"c_{num}",
        "name": f"{name_de_str}（{name_ja_str}）",
        "category": cat,
        "rating": rating,
        "locationZone": zone,
        "lat": lat,
        "lng": lng,
        "kids": True,
        "rain": "Museum" in cat or "Landmark" in cat or "Shopping" in cat,
        "shopping": cat == "Shopping",
        "free": "無料" in price_ja or "Free" in price_ja,
        "desc_en": f"{name_en_str} in {zone.capitalize()} district.",
        "desc_ja": desc_ja,
        "desc_es": f"{name_en_str} destacado en Colonia.",
        "desc_zh": f"位于当地的知名景点 {name_ja_str}。",
        "desc_fr": f"{name_en_str} remarquable à visiter à Cologne.",
        "de": f"{name_de_str} im Kölner Stadtgebiet.",
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

cologne_raw_56 = [
    # City (1-45)
    (1, "ケルン大聖堂", "Cologne Cathedral", "Kölner Dom (UNESCO)", "Landmark", "★4.9", "city", 50.9413, 6.9583, "聖堂無料（塔6€）", "高さ157mの双塔がそびえるゴシック建築の最高峰。東方三博士の金色の聖遺物箱を祀る世界遺産。", "大聖堂見学は無料！南塔の533段の螺旋階段登楼チケット（€6）を購入して100m展望スペースへ。"),
    (2, "ホーエンツォレルン橋", "Hohenzollern Bridge", "Hohenzollernbrücke", "Landmark", "★4.8", "city", 50.9414, 6.9653, "通行無料", "1911年建造のライン川に架かる歴史的鉄橋。数十万個の『愛の南京錠』がフェンスを埋め尽くす。", "夕暮れ時に対岸（東岸）へ渡って撮影！電車のライト、水面の反射、ライトアップされた大聖堂が重なります。"),
    (3, "ケルン旧市街＆アルター・マルクト", "Cologne Old Town & Alter Markt", "Altstadt Köln & Alter Markt", "Landmark", "★4.7", "city", 50.9383, 6.9603, "散策無料", "ライン川沿いに立つパステルカラーの細長い切妻屋根の家々と石畳の広場が広がる歴史的旧市街。", "ライン川沿いのシュターペルハウス（Stapelhaus）前へ！パステルカラーの5軒の細長家屋が並ぶ絵はがきショット。"),
    (4, "ホイマルクト広場", "Heumarkt Square", "Heumarkt", "Landmark", "★4.6", "city", 50.9367, 6.9608, "広場無料", "フリードリヒ・ヴィルヘルム3世の騎馬像が立つ大広場。冬のアイススケートやカーニバルの舞台。", "冬季（11月〜1月）訪問が最高！騎馬像の周囲を取り囲む特設アイススケートリンクで滑走体験。"),
    (5, "ケルン市庁舎＆歴史的ルネサンス回廊", "Cologne City Hall", "Kölner Rathaus & Historische Ratslaube", "Landmark", "★4.6", "city", 50.9381, 6.9592, "外観無料", "1330年起源のドイツ最古の市庁舎。130体の歴史的人物彫刻が飾られた高さ61mのゴシック塔。", "時計下の木彫りの顔『Platzjabbek』に注目！毎正時（00分）の時報とともにアッカンベーと舌を突き出します。"),
    (6, "大聖マルティン教会", "Great St. Martin Church", "Groß St. Martin", "Landmark", "★4.7", "city", 50.9386, 6.9617, "聖堂無料（地下発掘3€）", "ケルン旧市街のライン川沿いに聳える12世紀建造の重厚なロマネスク様式教会。4つの小塔を従えた大塔。", "聖堂内部の地下発掘エリア（€3）へ！古代ローマ時代の倉庫遺構と床モザイクが保存されています。"),
    (7, "ライナウハーフェン＆クレーンハウス", "Rheinauhafen & Crane Houses", "Rheinauhafen & Kranhäuser", "Landmark", "★4.7", "city", 50.9256, 6.9658, "散策無料", "旧港湾地区を現代建築へ再開発。川に突き出た高さ60mの3棟の逆L字型「クレーンハウス」が整列。", "クレーンハウス1号館（Kranhaus Eins）の真下へ！ライン川上に張り出すガラスの片持ち構造を見上げる撮影。"),
    (8, "ケルントライアングル展望台", "KölnTriangle Panorama Deck", "KölnTriangle (Panorama-Plattform)", "Landmark", "★4.8", "city", 50.9411, 6.9692, "入場料: 5€", "対岸のドイツ地区に立つ高さ103mの超高層ビル。全周が安全ガラスで囲まれた屋上オープンエア展望台。", "日没45分前の入場が黄金法則！沈む夕日がケルン大聖堂を黄金色に染め、鉄橋に明かりが灯ります。"),
    (9, "ケルン・チョコレート博物館", "Cologne Chocolate Museum", "Schokoladenmuseum Köln", "Museum & Gallery", "★4.7", "city", 50.9322, 6.9644, "入場料: 14.50€", "リンツ提供の体感型博物館。熱帯カカオ温室、動く自動製造ライン、高さ3mの黄金のチョコレートの噴水。", "会場中央の高さ3mのチョコレートの噴水へ直行！スタッフが温かい生チョコを浸したウエハースを無料で配布。"),
    (10, "ルートヴィヒ美術館", "Museum Ludwig", "Museum Ludwig", "Museum & Gallery", "★4.8", "city", 50.9406, 6.9603, "入場料: 13€", "大聖堂隣に立つ現代美術の最高峰。世界第3位のピカソ・コレクションとウォーホル等のポップアートを誇る。", "第4展示室へ直行！ウォーホルの『ブリロ・ボックス』やリキテンスタインの『M-Maybe』を至近距離で観賞。"),
    (11, "ヴァルラフ＝リヒャルツ美術館", "Wallraf-Richartz-Museum", "Wallraf-Richartz-Museum & Fondation Corboud", "Museum & Gallery", "★4.7", "city", 50.9378, 6.9589, "入場料: 13€", "中世ケルン派絵画からモネ、ルノワール、ゴッホ、点描派までの700年の名画コレクション。", "2階のモネ『エトルタの嵐の海』前で印象派絵画のダイナミックな筆致を鑑賞！"),
    (12, "ローマ・ゲルマン博物館", "Romano-Germanic Museum", "Römisch-Germanisches Museum", "Museum & Gallery", "★4.7", "city", 50.9408, 6.9589, "入場料: 10€", "古代ローマ都市コロニアの遺跡上に立つ館。巨大なディオニソスのモザイク画と古代ガラス。", "1階ガラス越しに『ディオニソスのモザイク画（Dionysus Mosaic）』を巨大な床面全体で見渡す！"),
    (13, "ファリナ香水博物館", "Farina Fragrance Museum", "Farina Duftmuseum (Duftmuseum im Farina-Haus)", "Museum & Gallery", "★4.7", "city", 50.9375, 6.9575, "ツアー料: 9€", "1709年創業。世界最古の香水工場であり『オーデコロン（ケルンの水）』誕生の地。", "ガイドツアー（要Web予約）に参加！ロココ衣裳のガイドと地下調香室でオリジナルベルガモット香料を体験。"),
    (14, "4711本店", "4711 Flagship Store", "4711 Stammhaus (Glockengasse)", "Shopping", "★4.6", "city", 50.9383, 6.9519, "入館無料", "世界的に有名なオーデコロンブランド「4711」のネオ・ゴシック調歴史的旗艦店。", "店舗入口の『香水の泉（Parfümbrunnen）』へ！湧き出る本物のオーデコロンを手にとって贅沢に試香。"),
    (15, "コロンバ美術館", "Kolumba Art Museum", "Kolumba (Kunstmuseum des Erzbistums Köln)", "Museum & Gallery", "★4.8", "city", 50.9386, 6.9542, "入場料: 8€", "ピーター・ズントー設計。第二次大戦で破壊された聖コロンバ教会廃墟を包み込んだ建築美。", "1階の広大な廃墟展示室へ！穿たれたレンガの穴から光の粒子が差し込むズントー建築の静寂空間。"),
    (16, "ケルン応用工芸博物館", "Museum of Applied Arts Cologne", "Museum für Angewandte Kunst Köln (MAKK)", "Museum & Gallery", "★4.6", "city", 50.9392, 6.9553, "入場料: 6€", "家具、ジュエリー、ガラス、バウハウスのデザインから現代プロダクトまでの工芸殿堂。", "バウハウス展示コーナーでリートフェルトの『赤と青の椅子』のプロダクトデザインを鑑賞。"),
    (17, "ナチス文書センター", "NS Documentation Center", "NS-Dokumentationszentrum (EL-DE-Haus)", "Museum & Gallery", "★4.8", "city", 50.9419, 6.9511, "入場料: 4.50€", "旧ゲシュタポ本部ビル。地下刑務所の壁に残る囚人たちの悲痛な落書きと歴史展示。", "地下の狭い独房群へ下り、暗闇の壁に刻まれた囚人たちの爪痕や外国語のメッセージを直視。"),
    (18, "ラウテンシュトラウホ＝ヨースト博物館", "Rautenstrauch-Joest-Museum", "Rautenstrauch-Joest-Museum", "Museum & Gallery", "★4.7", "city", 50.9347, 6.9525, "入場料: 10€", "世界各地の先住民族文化、宗教、生活様式をテーマにした欧州屈指の民族学博物館。", "エントランス吹き抜けに立つインドネシア・スラウェシ島の巨大な木造米倉（Rice Barn）を撮影！"),
    (19, "シュニュートゲン美術館", "Museum Schnütgen", "Museum Schnütgen", "Museum & Gallery", "★4.7", "city", 50.9347, 6.9519, "入場料: 6€", "11世紀のロマネスク様式聖ツェツィーリエン教会内に展示された中世キリスト教美術。", "ロマネスク教会の聖堂空間に展示された木彫りの十字架像や象牙細工を静かに鑑賞。"),
    (20, "ドイツ・スポーツ＆オリンピック博物館", "German Sport & Olympic Museum", "Deutsches Sport & Olympia Museum", "Museum & Gallery", "★4.6", "city", 50.9317, 6.9642, "入場料: 9.50€", "ライナウハーフェン内。古代五輪からF1マシン、ポレヴォルト用具までスポーツ史を展示。", "屋上テラスへ！ライン川と摩天楼を見下ろす最上階のミニサッカー＆バスケコートで遊ぶ。"),
    (21, "ケルン・ロープウェイ", "Cologne Cable Car", "Kölner Seilbahn", "Scenery & Walk", "★4.7", "city", 50.9525, 6.9722, "片道: 5€", "1957年開業。ライン川と大聖堂、緑豊かなライン公園上空を横断するパノラマロープウェイ。", "4月〜11月限定運航！中央ゴンドラからライン川を真下に見下ろし、大聖堂の双塔をバックに撮影。"),
    (22, "ケルン動物園", "Cologne Zoo", "Kölner Zoo", "Kids & Family", "★4.7", "city", 50.9583, 6.9733, "入場料: 23€", "1860年開園の歴史的動物園。2haの巨大アジアゾウ公園やバブーンの岩山が人気。", "毎日14:30のアジアゾウ群の水浴び＆給餌タイムに合わせて Elephant Park デッキへ！"),
    (23, "ケルン水族館", "Cologne Aquarium", "Aquarium Köln", "Kids & Family", "★4.6", "city", 50.9578, 6.9744, "入場料: 6€（動物園セット可）", "動物園に隣接。ライン川の魚類からサンゴ礁の熱帯魚、爬虫類、テラリウムまで展示。", "地下の大水槽で悠々と泳ぐ巨大マナティ（海牛）とサンゴ礁の熱帯魚の泳ぎを鑑賞。"),
    (24, "フローラ＆ケルン植物園", "Flora & Botanical Garden Cologne", "Flora Köln & Botanischer Garten", "Scenery & Walk", "★4.8", "city", 50.9594, 6.9714, "散策無料", "1864年建造の壮麗なガラス宮殿『Flora』と、1万種以上の植物が広がる11haの歴史的植物園。", "ガラス宮殿Flora前のフランス式庭園大噴水から宮殿を見上げるエレガント写真を撮影！"),
    (25, "シルダークロイツ通り＆ホーエ通り", "Schildergasse & Hohe Straße", "Schildergasse & Hohe Straße", "Shopping", "★4.5", "city", 50.9361, 6.9536, "散策無料", "ドイツ屈指の歩行者交通量を誇る二大歩行者天国ショッピング街。デパートやファッション。", "Schildergasseのガラス建築Peek & Cloppenburg（レンゾ・ピアノ設計）の曲面ガラス壁を観賞。"),
    (26, "エーレン通り＆ベルギー地区", "Ehrenstraße & Belgian Quarter", "Ehrenstraße & Belgisches Viertel", "Shopping", "★4.7", "city", 50.9389, 6.9428, "散策無料", "若者に大人気のトレンド街区。独立系デザイナーブティック、ヴィンテージ古着、カフェ。", "Belgisches Viertelの中心ブリュッセル広場（Brüsseler Platz）周りのカフェで地元若者と過ごす。"),
    (27, "ノイマルクト広場＆パサージュ", "Neumarkt Square & Passage", "Neumarkt & Neumarkt Passage", "Shopping", "★4.5", "city", 50.9356, 6.9486, "散策無料", "ケルン中心部の交通結節点広場。高級パサージュやデパートが立ち並ぶ。", "冬（11月下旬〜）の『天使のクリスマス市（Markt der Engel）』で星型イルミネーションを鑑賞。"),
    (28, "デュモン・カレ＆オペルン・パサージェン", "DuMont Carré & Opern Passagen", "DuMont Carré & Opern Passagen", "Shopping", "★4.5", "city", 50.9386, 6.9514, "入館無料", "雨の日でも快適にショッピングやカフェタイムを楽しめる全天候型屋内パサージュモール。", "Opern Passagen内の老舗エスプレッソバーで雨宿りしながら出来立てのパニーニを味わう。"),
    (29, "フリュー・アム・ドーム", "Brauhaus Früh am Dom", "Brauhaus Früh am Dom", "Café & Bistro", "★4.6", "city", 50.9397, 6.9575, "ケルシュ: 2.40€", "大聖堂前にある1904年創業の超有名老舗ビアホール。給仕人 Köbes が注ぐケルシュビール。", "給仕人Köbesが自動で次々置く細グラスのケルシュ！グラスにコースターを乗せるまで注がれ続けます。"),
    (30, "ブラウハウス・ジオン", "Brauhaus Sion", "Brauhaus Sion", "Café & Bistro", "★4.6", "city", 50.9389, 6.9594, "ケルシュ: 2.40€", "1318年起源の歴史を誇る老舗居酒屋。木製樽から注がれる直注ぎケルシュと伝統料理。", "名物料理『Himmel un Ääd（天と地：血のソーセージとマッシュポテト・リンゴ煮込み）』を注文！"),
    (31, "ギルデン・イム・ツィムス", "Gilden im Zims", "Gilden im Zims \"Heimat kölscher Helden\"", "Café & Bistro", "★4.6", "city", 50.9378, 6.9603, "ケルシュ: 2.40€", "旧市街中心に立つ4フロアの巨大歴史的ビアホール。「ケルンの英雄たち」の壁画。", "地下の歴史的石造り地下壕（Gewölbekeller）のテーブル席で伝統のケルシュビールを楽しむ！"),
    (32, "ペフゲン醸造所", "Brauerei Päffgen", "Brauerei Päffgen", "Café & Bistro", "★4.7", "city", 50.9417, 6.9425, "ケルシュ: 2.40€", "フリース通りにある地元民に絶大な人気を誇る伝統醸造所。樽生無ろ過ケルシュの名店。", "木製木樽から直注ぎされる生のPäffgen Kölschと、特大のポークシュニッツェルを堪能！"),
    (33, "ペータース・ブラウハウス", "Peters Brauhaus", "Peters Brauhaus", "Café & Bistro", "★4.7", "city", 50.9389, 6.9606, "ケルシュ: 2.40€", "旧市街のステンドグラス天井が美しい人気ブラウハウス。アットホームな居心地。", "鮮やかなステンドグラス天窓の下の木製長テーブルで、カリカリのローストポークハックセ（Schweinshaxe）！"),
    (34, "ロンメルツハイム", "Lommerzheim Pub", "Lommerzheim (Lommi)", "Café & Bistro", "★4.8", "city", 50.9392, 6.9719, "ポークチョップ: 14€", "対岸ドイツ地区にある伝説の老舗酒場。飾らない下町風情と巨大ポークチョップ。", "名物『Kotelett（顔より大きい特大ポークチョップ）』と木樽直注ぎのPäffgenビールを注文！"),
    (35, "カフェ・ライヒャルト", "Café Reichard", "Café Reichard", "Café & Bistro", "★4.6", "city", 50.9406, 6.9575, "ケーキ: 6.50€", "1855年創業。ケルン大聖堂の正面双塔を真正面に見上げる絶景ガラス張りテラスサロン。", "大聖堂側の温室ガラス張りテラス席を確保！名物バームクーヘンや豪華なトルテでティータイム。"),
    (36, "オドニエン", "Odonien Outdoor Art Park", "Odonien", "Scenery & Walk", "★4.6", "city", 50.9547, 6.9442, "入場無料（イベント時別）", "彫刻家オド・リプカが創り出した廃材キネティックアート、屋外彫刻パーク＆クラブスペース。", "鉄くずや巨大機械パーツで作られた異次元の巨大火吹き彫刻群を背景にパンク写真を撮影！"),
    (37, "クラウディウス・テルメ", "Claudius Therme Thermal Bath", "Claudius Therme", "Scenery & Walk", "★4.7", "city", 50.9508, 6.9742, "スパ: 20.50€", "ライン公園内にある天然温泉スパリゾート。大聖堂を望む露天風呂、サウナ、死海プール。", "大聖堂のライトアップを眺められる屋外温水プールでぷかぷか浮きながらリラックス！"),
    (38, "ライン公園＆ミニSL鉄道", "Rheinpark & Kleinbahn", "Rheinpark & Kleinbahn", "Scenery & Walk", "★4.8", "city", 50.9472, 6.9722, "入園無料（ミニSL: 3.50€）", "ライン川東岸に広がる50haの芝生公園。広大なバラ園と園内を走る子供用ミニ蒸気機関車。", "園内を周遊するミニ鉄道Kleinbahnに乗車！ライン川越しに大聖堂が浮かぶ景観を眺める。"),
    (39, "ケルン市民の森＆リンデンタール動物ふれあい公園", "Stadtwald & Lindenthal Zoo", "Stadtwald Köln & Lindenthaler Tierpark", "Kids & Family", "★4.7", "city", 50.9258, 6.9036, "入園無料", "市民に愛される広大な森林公園と、シカやヤギに手から直接餌やりができる無料ふれあい動物園。", "自動販売機で専用のエサ（€1）を購入して、人懐っこいダマジカやヤギに手から餌やり！"),
    (40, "メラテン墓地", "Melaten Cemetery", "Melaten-Friedhof", "Scenery & Walk", "★4.7", "city", 50.9389, 6.9186, "散策無料", "400年以上の歴史を誇る公園のような彫刻墓地。ケルンの著名人や豪華なバロックスカルプチャ。", "マロニエの大樹が並ぶ「Hauptallee（主並木道）」を歩き、死神像（Sensenmann）の彫刻を探索。"),
    (41, "オディッセウム科学館", "Odysseum Science Center", "Odysseum Science Center", "Kids & Family", "★4.6", "city", 50.9369, 6.9903, "入場料: 16€", "子どもやティーン向けの体験型科学エンターテインメント施設。3D体験や宇宙エリア。", "「Museum mit der Maus（ねずみのお客様館）」で、テレビでおなじみの科学実験に体験参加！"),
    (42, "ライン川観光遊覧船", "KD Rhine River Cruise", "RheinSchiffahrt (Köln-Düsseldorfer / KD River Cruises)", "Scenery & Walk", "★4.7", "city", 50.9400, 6.9622, "クルーズ: 15€", "大聖堂前のKD社桟橋から発着する1時間のライン川パノラマ観光クルーズ船。", "2階オープンデッキの船首側席へ！ホーエンツォレルン橋の下をくぐる迫力のアングルを撮影。"),
    (43, "聖ゲレオン教会", "St. Gereon Basilica", "St. Gereon", "Landmark", "★4.8", "city", 50.9439, 6.9458, "拝観料無料", "4世紀の古代ローマ遺構の上に立つ十角形（デカゴン）の大ドームを持つ名ロマネスク教会。", "十角形（デカゴン）ドームの真下へ立ち、天井に描かれた中世のフレスコ画とステンドグラスを見上げる！"),
    (44, "聖ウルスラ教会", "St. Ursula Basilica", "St. Ursula", "Landmark", "★4.7", "city", 50.9458, 6.9536, "拝観無料（黄金の部屋2€）", "殉教者聖ウルスラ伝説の教会。壁一面が人骨モザイクで装飾された『黄金の小部屋』。", "『黄金の小部屋（Goldene Kammer / €2）』へ！壁一面に人骨で装飾された異色の宗教芸術を観賞。"),
    (45, "聖使徒教会", "St. Apostles Church", "St. Aposteln", "Landmark", "★4.7", "city", 50.9364, 6.9467, "拝観料無料", "ノイマルクト広場に面する12世紀建造の美しい三葉型後陣（Triconchos）を持つロマネスク教会。", "広場側の東側後陣（三つ葉デザイン）の外観を下から見上げて重厚なロマネスク様式を撮影！"),

    # Suburban (46-56)
    (46, "アウグストゥスブルク城＆ファルケンルスト城", "Augustusburg & Falkenlust Palaces", "Schlösser Augustusburg und Falkenlust (Brühl / UNESCO)", "Landmark", "★4.8", "suburban", 50.8275, 6.9078, "宮殿: 10€", "ケルン選帝侯の夏の離宮（世界遺産）。バルタザール・ノイマン設計の壮麗な階段広場とロココ庭園。", "バルタザール・ノイマン設計の『階段広場（Treppenhaus）』へ！天井大理石彫刻とフレスコ画の極上アングル。"),
    (47, "ファンタジアランド", "Phantasialand Theme Park", "Phantasialand (Brühl)", "Kids & Family", "★4.9", "suburban", 50.7989, 6.8794, "ワンデーパス: 54〜61€", "世界屈指のテーマ演出と絶叫コースターを誇る大人気テーマパーク。飛行コースター『F.L.Y.』が超有名。", "チケットは事前にphantasialand.deでWeb購入必須！入場したらスチームパンクエリア『Rookburgh』へ直行。"),
    (48, "アーヘン大聖堂＆宝物館", "Aachen Cathedral & Treasury", "Aachener Dom & Domschatzkammer (Aachen / UNESCO)", "Landmark", "★4.9", "suburban", 50.7747, 6.0839, "大聖堂無料（ガイド5€）", "ドイツ初の世界遺産。カール大帝が796年に創建した八角形（オクタゴン）の宮廷礼拝堂と皇帝の玉座。", "ガイドツアー（要予約）に参加して2階ギャラリーへ！カール大帝が実際に坐した本物の大理石玉座を観賞。"),
    (49, "ドラッヘンブルク城＆竜の岩山", "Drachenburg Castle & Drachenfels", "Drachenburg Castle & Drachenfels (Königswinter)", "Landmark", "★4.8", "suburban", 50.6742, 7.2064, "登山鉄道: 12€往復", "ケーニヒスヴィンターにあるジークフリート伝説の山。1883年建造の絵になるお城と登山鉄道。", "ドイツ最古の歯車式登山鉄道（Drachenfelsbahn）で中腹のドラッヘンブルク城へ！ライン川を見下ろす。"),
    (50, "ベンラート宮殿", "Benrath Palace", "Schloss Benrath (Düsseldorf)", "Landmark", "★4.7", "suburban", 51.1611, 6.8703, "庭園無料（宮殿10€）", "デュッセルドルフ南部に立つ、鮮やかなピンク色の外観が美しい18世紀ロココ様式の「夏の離宮」と湖。", "鏡のような大池越しに、ピンク色の主宮殿（Corps de Logis）が反射して映り込む水面写真を撮影！"),
    (51, "ザツヴァイ城", "Satzvey Castle", "Burg Satzvey (Mechernich)", "Landmark", "★4.7", "suburban", 50.6217, 6.7078, "敷地無料（イベント時別）", "アイフェル地方にある、中世騎士祭りやクリスマス市で有名な保存状態抜群の14世紀のロマンチックな水城。", "水堀に架かる木橋の上から、水面に完璧に映り込む石造りの城門と城壁を撮影！"),
    (52, "インゼル・ホンブロイヒ美術館", "Museum Insel Hombroich", "Museum Insel Hombroich (Neuss)", "Museum & Gallery", "★4.8", "suburban", 51.1472, 6.6583, "入場料: 15€", "「自然と芸術の共生」を掲げる25haの広大な自然保護区内に点灯するパビリオン型野外美術館。", "敷地内のカフェテリア（Cafeteria）へ！入館料に含まれる無料のパン、ゆで卵、スープ、お茶で休憩。"),
    (53, "ネアンデルタール博物館", "Neanderthal Museum", "Neanderthal Museum (Mettmann)", "Museum & Gallery", "★4.7", "suburban", 51.2256, 6.9506, "入場料: 11€", "1856年にネアンデルタール人化石が発見された渓谷に立つ、人類の進化を体験学習できる体感館。", "螺旋スロープを登りながら、実物大の精巧なネアンデルタール人やクロマニョン人の復元模型と記念撮影！"),
    (54, "コムメルン野外博物館", "Kommern Open-Air Museum", "Freilichtmuseum Kommern (LVR-Freilichtmuseum Kommern)", "Museum & Gallery", "★4.7", "suburban", 50.6119, 6.6508, "入場料: 9€", "ラインラント地方の歴史的木骨造り農家、風車、伝統技術（パン焼き・鍛冶）を再現した110haの野外館。", "歴史的なパン焼き小屋（Backhaus）で薪窯で焼き上げられた熱々の伝統農家パンを購入して賞味！"),
    (55, "ハイダー・ベルクゼー", "Heider Bergsee Lake", "Brühler Wasserski / Heider Bergsee", "Scenery & Walk", "★4.6", "suburban", 50.8306, 6.8778, "散策無料", "ブリュール近郊の自然豊かな湖。水上スキー、ウォータースポーツ、湖畔の遊歩道とビーチ。", "湖畔レストランのアウトドアテラスで、水上スキー滑走を眺めながらビールとフィッシュアンドチップス！"),
    (56, "バート・ミュンスターアイフェル・シティアウトレット", "Bad Münstereifel City Outlet", "City Outlet Bad Münstereifel", "Shopping", "★4.6", "suburban", 50.5556, 6.7628, "散策無料", "中世の城壁に囲まれた歴史的旧市街の木骨造り家屋全体がアウトレットショップになったユニークな町。", "中世の木骨造り家屋に入っているブランドショップで割引買い物を楽しみ、城壁沿いを散策！")
]

cologne_spots = []
for item in cologne_raw_56:
    cologne_spots.append(make_spot(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11]))

with open("data/cities/cologne.json", "w", encoding="utf-8") as f:
    json.dump({"cityName": "Cologne, Germany", "spots": cologne_spots}, f, ensure_ascii=False, indent=2)

print(f"🎉 Successfully created data/cities/cologne.json with ALL {len(cologne_spots)} SPOTS!")
