# 📘 Spot Database Architecture & Complete Quality Control Rulebook
**Document Version**: `v3.0.0` (Complete Master Systemic Edition - 2026-08-15)  
**File Location**: `docs/SPOT_DATABASE_RULES.md`  
**Automated Rule Location**: `.agents/rules/spot_database_rules.md`

---

## 🎯 目的（Purpose）
今後、何千・何万件と新しい都市や観光スポットがアプリに追加されても、データの品質劣化、英語漏れ、翻訳表示のアンバランス、タグ誤設定（Kids過剰流入等）、画像未反映（Wikipedia連携失敗）、UIレイアウト要素の破綻が**二度と発生しないよう、すべてのデータベース構築・自動検証・画像パイプライン項目を完備したマスタールールブック**です。

---

## 📜 14大厳格品質管理チェックリスト（The 14 Master Principles）

### 1. 🌐 全6言語対応「現地語＋翻訳名」ハイブリッド名称基準（Universal Hybrid Name Standard）
旅行者が現地で「Google Maps」「Uber」「標識」「紙の地図」で場所を照合できるよう、全6言語（日・英・西・中・仏・独）において**現地オリジナル名**と**各言語の翻訳名**をセットで保持します。

* **JSONデータ構造基準 (`data/cities/*.json`)**:
  - `name_ja`: `現地名（日本語名称）` （例: `Pont des Arts（ポン・デ・ザール）`, `Basilique Notre-Dame de Fourvière（フルヴィエール ノートルダム大聖堂）`）
  - `name_en`: `現地名 (English Name)` （例: `Basilique Notre-Dame de Fourvière (Fourvière Basilica)`）
  - `name_es`: `現地名 (Nombre en español)` （例: `Basilique Notre-Dame de Fourvière (Basílica de Fourvière)`）
  - `name_zh`: `現地名 (中文名称)` （例: `Basilique Notre-Dame de Fourvière (富维耶圣母院)`）
  - `name_fr`: `現地名 (Nom en français)`
  - `name_de`: `現地名 (Deutscher Name)`
* **例外規定（Smart Fallback）**:
  - 現地名と翻訳名が完全一致・または同一スペルの場合（例: ドイツの `Brandenburger Tor`）は、二重表記にせず単一表記（`Brandenburger Tor`）とします。

---

### 2. 📸 Wikipedia自動画像取得・検証パイプライン（Universal Wikipedia Photo Pipeline）
* **全角・半角カッコの完全正規化除去**:
  - Wikipedia API検索用スラグ生成時、`re.sub(r'[\(\（].*?[\)\）]', '', name)` を使用し、全角 `（` および半角 `(` のカッコ内補足文字を100%除去します。
  - スラグ生成には `name_de` / `name_en` / `name_fr` の純粋な現地語名称を優先使用します。
* **多言語フォールバックチェーン**:
  - `de.wikipedia.org` ➔ `en.wikipedia.org` ➔ `fr.wikipedia.org` ➔ `nl.wikipedia.org` ➔ `ja.wikipedia.org` の順でREST API（`api/rest_v1/page/summary/<slug>`）を検索し、有効なサムネイル画像URL（`image`）を自動バインドします。
* **ビルドパイプライン直元化**:
  - スポット追加・更新時、`rebuild_js_database.py` 実行時に `auto_wikipedia_image_fetcher.py` が自動で前処理として走り、画像未取得スポットをゼロにします。

---

### 3. 🚫 概要欄（desc）とワンポイント解説（tip）の重複完全排除（0% Overlap Rule）
* **概要欄（`desc`）**: どのような場所か、歴史的・建築的価値（基本情報1〜2文）。
* **ワンポイント解説（`tip`）**: **概要欄の内容・名称・基本説明を1文字も重複・再掲しない！** 現地での「具体的で実践的な裏技・コツ」のみ。

#### 💡 ワンポイント解説（tip）の推奨カテゴリー
- 🎟️ **チケット予約のコツ**: 「公式サイトで要2〜4週間前事前日時指定予約」「ミュージアムパス対象」等
- 📸 **撮影・ベストタイム**: 「夕暮れの何時にどこから撮ると一番綺麗」「無料エレベーターの場所」「〇〇橋の上からの見上げアングル」等
- 👚 **服装・持ち物・気温注意**: 「教会内部は肩・膝の露出NG」「地下防空壕や要塞内は夏でも冷えるので羽織る上着が必須」等
- 🍽️ **周辺のグルメ・ペアリング・注文口令**: 「売店で〇〇を注文する口令」「テイクアウトして隣の公園で食べるのが地元の定番」等
- 💡 **その他有益情報**: 上記カテゴリーに当てはまらない現地特有の知識。

---

### 4. 💡 Tipが無いスポットのスマート省略（Smart Empty Tip Handling）
* 特段の裏技や実用Tipsが存在しないスポットは、無理に一般的な説明を書かず `tip: ""`（空文字）とします。
* UIレンダリングエンジンは、`tip` が空の場合、カードおよびモーダル内のワンポイント解説枠を**枠ごとスマートに完全非表示**にします。

---

### 5. 🏷️ カテゴリ・属性タグの厳格除外チェック（Strict Category & Tag Auditing）
誤ったフィルタータグ設定によるユーザーの混乱を完全に防ぎます。

* **👶 Kids (ファミリー向け)**:
  - **原則**: スポット生成時にデフォルトで `"kids": true` をハードコード設定することを**固く禁止**します。
  - **真判定条件**: `category == "Kids & Family"` であるスポット、または名称・概要欄に明確な子供/ファミリー向け要素（動物園、水族館、科学館、テーマパーク、恐竜・ミニチュア館、温水プール、遊具公園）を含む場合のみ `true` とします。
  - **偽判定条件（強制除外）**: 大衆居酒屋（Brauhaus / Apfelwein-Kneipen）、歓楽街（Reeperbahn）、墓地（Melaten-Friedhof）、戦災・ホロコースト追悼施設（NS-Dokumentationszentrum, ゲシュタポ跡地, 壁の記念館）、高級ブティック街は**必ず `"kids": false`** とします。
* **🛍️ Shopping (ショッピング)**: 居酒屋・レストランを完全除外。歴史的市場、パサージュ、デパート、アウトレットのみ。
* **☔ Rainy Day (雨天対応)**: 屋外の橋、公園、オープン広場、船上クルーズを完全除外。100%屋根のある屋内施設のみ。
* **🆓 Free (入場無料)**: 有料チケットが義務付けられている施設を完全除外。敷地・広場・聖堂無料のみ。

* 🛍️ **Shopping タグ**: 純粋なカフェ・レストラン・飲食店を厳格除外。歴史的市場（Markthalle）、パサージュ、百貨店、セレクトショップのみ許可。
* ☔ **Rainy Day (Rain) タグ**: 橋、公園、屋外広場、シュプレー川/セーヌ川クルーズ船等の屋外スポットを厳格除外。完全屋内施設（美術館・博物館・大聖堂内部等）のみ許可。
* 🆓 **Free タグ**: 100%有料の施設を厳格除外。入場無料の公園・広場・教会・常設展無料施設のみ許可。

---

### 5. 🌍 6言語全完訳・アルファベット圏英語漏れ検知（6-Language Full Translation Assurance）
* 全6言語（日・英・西・中・仏・独）すべての `name` / `desc` / `tip` / `price` フィールドが正しく格納されているか検証。
* **アルファベット圏（フランス語・スペイン語・ドイツ語）での英語原文放置の完全検知**:
  - `rebuild_js_database.py` 内のストップワード解析エンジン（Spanish/French/German Stopword Analyzer）により、英語原文がそのまま残されているケースを自動検出してビルドを遮断。

---

### 6. 🎟️ ハイブリッド料金表記の正確化（Hybrid Pricing Accuracy）
* 「庭園・敷地散策は無料だが、宮殿・館内は有料」といったスポットの料金表記を統一化。
  - 例: `Palace: €17 (Gardens Free)` / `宮殿: 17ユーロ（庭園無料）` / `Palacio: 17€ (Jardines gratis)`

---

### 7. 📍 位置情報（GPS座標）精度チェック（GPS Coordinate Precision）
* ルート検索、地図描画、距離計算エンジンが正常に動作するよう、全スポットに正確な `lat`（緯度）および `lng`（経度）を小数点第4位精度で格納。

---

### 8. 🖼️ 画像・Wikipedia連携チェック（Image & Wikipedia Asset Verification）
* スポットの画像URL（`image` / `wikiImage`）が正常なWikipedia REST APIサムネイルまたはローカルアセットを指しているか確認し、404デッドリンクを100%排除。

---

### 9. 🗺️ エリア区分チェック（Zoning Verification）
* 各スポットが `locationZone: "city"`（市内中心部）または `locationZone: "suburban"`（近郊・郊外日帰り）に正しくカテゴリ分けされているかを検証。

---

### 10. 🔴 赤バツ閉じるボタン（✕）の枠外独立配置基準（Outer Close Button Standard）
* モーダル内の写真、Wikipediaリンクタグ、評価バッジ（★）との物理的衝突を防ぐため、`.modal-close` ボタンは**必ずモーダルカードの枠外右上（外側上部）**へ退避配置する。
* **CSS基準**:
  - `.modal-content` に `position: relative !important; overflow: visible !important;`
  - `.modal-close` に `position: absolute; top: -18px; right: -12px; z-index: 150;` （モバイルレスポンシブ時 `top: -20px; right: -4px;`）
  - タップ領域（Hitbox）は最低 44px × 44px を厳格維持。

---

### 11. 🛡️ 3層コンプライアンス・全自動ビルド検証（3-Layer Guard Pipeline）
`scripts/rebuild_js_database.py` 実行時に、以下の3層ガードが全都市・全言語データを自動検証します。エラー検出時はビルドを自動停止します。

1. **Layer 1: 英語未翻訳リークガード**: 非英語フィールドへの英語原文残留を検知。
2. **Layer 2: 多言語自然言語ストップワード解析ガード**: 欧州言語間での英語原文の放置・隠蔽を言語学的に検出。
3. **Layer 3: 多言語ハイブリッド名称検証ガード**: 全6言語の `name` フィールドに「現地名（翻訳名）」形式が維持されているかを自動チェック。

---

### 12. 📦 キャッシュバスター＆本番デプロイフロー（Cache Buster & Release Workflow）
* 新都市・スポットの追加および変更時は、必ず以下の一連の手順を漏れなく実行する。
  1. `python3 scripts/rebuild_js_database.py` で3層ガードを通過して `js/ai-travel-engine.js` を再構築。
  2. `index.html` 内のスクリプトバージョン（`?v=XX.0`）を繰り上げ。
  3. `CHANGELOG.md` にバージョン番号と変更内容を記録。
  4. Git commit & `git push origin main` で GitHub Pages へ本番即時デプロイ。

---

## 📂 保管場所と参照ファイル（File Inventory）

| 役割 | パス | 説明 |
| :--- | :--- | :--- |
| 📖 **公式マスタールールブック（人間用）** | `docs/SPOT_DATABASE_RULES.md` | 本ドキュメント（完全版仕様書） |
| 🤖 **AIエージェント用自動参照ルール** | `.agents/rules/spot_database_rules.md` | AIが起動時に自動読み込みする行動規範 |
| 🛡️ **3層自動検証ビルドスクリプト** | `scripts/rebuild_js_database.py` | 3層ガードを搭載したデータベース統合スクリプト |
| 🧹 **全言語ハイブリッド自動補正** | `scripts/make_all_names_hybrid.py` | 全都市データの名称を6言語ハイブリッド化するスクリプト |

---
**Zero-Margin Travel App Development Core Guidelines — Master Version**
