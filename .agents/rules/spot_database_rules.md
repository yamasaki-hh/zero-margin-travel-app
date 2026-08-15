# Spot Database Naming, UI Layout, & Quality Control Rules

1. **Universal Multilingual Hybrid Name Rule**:
   - Every spot name across all 6 supported languages (`name_en`, `name_ja`, `name_es`, `name_zh`, `name_fr`, `name_de`) must preserve the `Original Local Name (Localized Translated Name)` for non-native languages.
   - Example: `Basilique Notre-Dame de Fourvière (Fourvière Basilica)` for EN, `Basilique Notre-Dame de Fourvière（フルヴィエール ノートルダム大聖堂）` for JA, `Basilique Notre-Dame de Fourvière (富维耶圣母院)` for ZH.

2. **Description vs Insider Tip 0% Overlap Rule**:
   - `desc` contains basic architectural/historical facts.
   - `tip` contains ZERO overlapping text or name restatements; only actionable practical secrets (🎟️ Tickets, 📸 Photospots/timing, 👚 Dress/weather, 🍽️ Food pairings).

3. **Modal Close Button UI Layout**:
   - `.modal-close` must sit strictly outside and above the modal photo container (`top: -18px; right: -12px;`) to prevent collision with rating badges (`★`).

4. **3-Layer Compliance Guard Enforcement**:
   - Always run `python3 scripts/rebuild_js_database.py` to verify Layer 1 (Identity), Layer 2 (Multi-Language Stopword Analysis), and Layer 3 (Multilingual Hybrid Name Guard).
