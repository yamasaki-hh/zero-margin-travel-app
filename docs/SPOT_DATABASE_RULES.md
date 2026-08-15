# 📘 Spot Database Architecture & Quality Control Rulebook
**Document Version**: `v1.0.0` (2026-08-15)  
**File Location**: `docs/SPOT_DATABASE_RULES.md`  
**Automated Rule Location**: `.agents/rules/spot_database_rules.md`

---

## 🎯 目的（Purpose）
今後、何千・何万件と新しい都市や観光スポットがアプリに追加されても、データの品質劣化、英語漏れ、翻訳表示のアンバランス、UIレイアウト要素の重複破綻が**二度と発生しないよう、厳格なデータ構造基準と自動検証ルールを明文化・全自動ガード化**するものです。

---

## 📜 5大基本原則（The 5 Core Principles）

### 原則 1: 🌐 全6言語対応「現地語＋翻訳名」ハイブリッド名称基準（Universal Hybrid Name Rule）
旅行者が現地で「Google Map」「Uber」「標識」「紙の地図」で場所を検索・照合できるよう、全言語表示において**現地オリジナル名**と**ユーザー言語での翻訳補足**をセットで保持します。

* **JSONデータ構造基準 (`data/cities/*.json`)**:
  - `name_en`: `現地名 (English Name)` （例: `Basilique Notre-Dame de Fourvière (Fourvière Basilica)`）
  - `name_ja`: `現地名（日本語名称）` （例: `Basilique Notre-Dame de Fourvière（フルヴィエール ノートルダム大聖堂）`）
  - `name_es`: `現地名 (Nombre en español)` （例: `Basilique Notre-Dame de Fourvière (Basílica de Fourvière)`）
  - `name_zh`: `現地名 (中文名称)` （例: `Basilique Notre-Dame de Fourvière (富维耶圣母院)`）
  - `name_fr`: `現地名 (Nom en français)`
  - `name_de`: `現地名 (Deutscher Name)`
* **例外規定（Smart Fallback）**:
  - 現地名と翻訳名が完全一致・または同一スペルの場合（例: ドイツの `Brandenburger Tor`）は、二重表記にならず単一表記（`Brandenburger Tor`）とします。

---

### 原則 2: 🚫 概要欄（desc）とワンポイント解説（tip）の重複完全排除（0% Overlap Rule）
* **概要欄（`desc`）**: スポットの歴史背景、建築様式、基本的概要のみ（1〜2文）。
* **ワンポイント解説（`tip`）**: **概要欄の内容・名称・説明を1文字も重複・再掲しない！** 現地で即座に役立つ実践的な「裏技・コツ」のみ。
  - 🎟️ **チケット予約のコツ**: 「公式サイトで要2〜4週間前事前日時指定予約」「ミュージアムパス対象」等
  - 📸 **撮影・ベストタイム**: 「日没後のブルーアワー」「無料展望エレベーターの場所」「〇〇橋の上から見上げると絶景」等
  - 👚 **服装・持ち物・気温注意**: 「地下防空壕内は年中10℃なので夏でも厚手の上着が必須」「教会内は露出NG」等
  - 🍽️ **名物グルメ・ペアリング・注文口令**: 「売店で〇〇を注文する口令」「テイクアウトして隣の公園で食べるのが地元流」等
  - 💡 **特段のTipsがない場合**: 空文字 `""` とし、UI側でスマート非表示。

---

### 原則 3: 🔴 赤バツ閉じるボタン（✕）の枠外独立配置基準（Outer Modal Close Rule）
* モーダル内の写真、Wikipediaリンクタグ、評価バッジ（★）との物理的衝突を防ぐため、`.modal-close` ボタンは**必ずモーダルカードの枠外右上（外側上部）**へ退避配置する。
* **CSS基準**:
  - `.modal-content` に `position: relative !important; overflow: visible !important;` を指定。
  - `.modal-close` に `position: absolute; top: -18px; right: -12px; z-index: 150;` （モバイルレスポンシブ時 `top: -20px; right: -4px;`）を指定。
  - タップ領域（Hitbox）は最低 44px × 44px を厳格維持。

---

### 原則 4: 🛡️ 3層コンプライアンス・全自動ビルドガード（3-Layer Compliance Guard）
`scripts/rebuild_js_database.py` 実行時に、以下の3層ガードが全スポット・全言語データを自動検証します。エラー検出時はビルドを自動停止します。

1. **Layer 1: 英語未翻訳リークガード (English Leak Guard)**
   - 非英語（ja, es, zh, fr, de）のフィールドに英語原文がそのまま残留していないかを検証。
2. **Layer 2: 多言語ストップワード解析ガード (Multi-Language Stopword Analysis Guard)**
   - 各言語の文法ストップワード（es: `el, de, en`, fr: `le, du, des`, de: `der, und, in`, ja: ひらがな・カタカナ・漢字の存在）を自然言語解析し、偽装された英語原文を自動検出。
3. **Layer 3: 多言語ハイブリッド名称検証ガード (Multilingual Hybrid Name Guard)**
   - `name_ja` や各言語名に現地名および翻訳名が正しくカッコ付き等で格納されているかを検証。

---

### 原則 5: 📦 バージョン管理・キャッシュバスター厳守（Cache Buster Policy）
* 新しい都市・スポットの追加、またはデータの更新時は、必ず `index.html` 内のスクリプトタグパラメータ（`?v=XX.0`）をインクリメント（加算）し、ブラウザキャッシュによる新旧データの不整合を100%防止する。

---

## 📂 保管場所と参照ファイル（File Inventory）

| 役割 | パス | 説明 |
| :--- | :--- | :--- |
| 📖 **公式ルールブック（人間用）** | `docs/SPOT_DATABASE_RULES.md` | 本ドキュメント（全体仕様書） |
| 🤖 **AI・エージェント用自動参照ルール** | `.agents/rules/spot_database_rules.md` | 次回以降のAIセッションで自動読み込みされる行動規範 |
| 🛡️ **自動検証ビルドスクリプト** | `scripts/rebuild_js_database.py` | 3層ガードを搭載したデータベース統合スクリプト |
| 🧹 **全言語ハイブリッド自動補正** | `scripts/make_all_names_hybrid.py` | 全都市データの名称を6言語ハイブリッド化するスクリプト |

---
**Zero-Margin Travel App Development Core Guidelines**
