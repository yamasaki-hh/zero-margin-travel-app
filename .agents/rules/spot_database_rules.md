# Spot Database Architecture & Quality Control Master Rules

1. **Universal Multilingual Hybrid Name Standard**:
   - Every spot name across all 6 supported languages (`name_en`, `name_ja`, `name_es`, `name_zh`, `name_fr`, `name_de`) must preserve `Original Local Name (Localized Name)` for non-native languages.
   - Example: `Pont des Arts（ポン・デ・ザール）` for JA, `Basilique Notre-Dame de Fourvière (Fourvière Basilica)` for EN, `Basilique Notre-Dame de Fourvière (富维耶圣母院)` for ZH.

2. **Description vs Insider Tip 0% Overlap Rule**:
   - `desc`: Basic architectural, historical facts (1-2 sentences).
   - `tip`: ZERO overlapping text or name restatements. Practical insider secrets only:
     - 🎟️ Ticket booking tricks & mandatory free web registrations
     - 📸 Photospots, angles, & blue hour timing
     - 👚 Dress code, gear, & cold bunker/crypt weather warnings
     - 🍽️ Food pairings, local market snacks, & ordering phrases
     - 💡 Useful secrets outside standard categories
   - If no practical tips exist, set `tip: ""` for smart component hiding.

3. **Strict Category & Tag Auditing**:
   - 🛍️ **Shopping**: Strictly exclude pure cafes/restaurants. Historical market halls, arcades, department stores, and boutiques only.
   - ☔ **Rainy Day**: Strictly exclude outdoor bridges, parks, open squares, and river cruises. 100% covered indoor venues only.
   - 🆓 **Free**: Strictly exclude venues with mandatory entrance fees. Free parks, squares, open churches, and free permanent exhibitions only.

4. **6-Language Full Translation & English Leak Prevention**:
   - Verify `name`, `desc`, `tip`, and `price` across 6 languages. Use natural language stopword analyzers to detect untranslated English text in ES, FR, and DE.

5. **Hybrid Pricing Accuracy**:
   - Use hybrid pricing strings for venues with free grounds but paid interiors (e.g. `Palace: €17 (Gardens Free)` / `宮殿: 17ユーロ（庭園無料）`).

6. **GPS Precision, Asset Verification, & Zoning**:
   - Verify exact `lat` and `lng` coordinates.
   - Verify `image` / `wikiImage` asset status to eliminate dead 404 links.
   - Tag `locationZone` correctly as `city` or `suburban`.

7. **Modal Close Button UI Layout**:
   - `.modal-close` must sit strictly outside and above the modal photo container (`top: -18px; right: -12px;` / mobile `top: -20px; right: -4px;`) to prevent collision with rating badges (`★`).

8. **3-Layer Compliance & Build Guard Enforcement**:
   - Always run `python3 scripts/rebuild_js_database.py` to verify Layer 1 (Identity), Layer 2 (Multi-Language Stopword Analysis), and Layer 3 (Multilingual Hybrid Name Guard).

9. **Cache Busters & Deployment Protocol**:
   - Bump script versions in `index.html` (`?v=XX.0`), log release in `CHANGELOG.md`, and commit/push to GitHub main for instant GitHub Pages deployment.
