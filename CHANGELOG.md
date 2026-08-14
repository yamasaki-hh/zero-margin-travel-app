# Zero-Margin Travel App - Version Changelog

All notable changes and release checkpoints for the Zero-Margin Travel App will be documented in this file.

---

## 🏷️ [v1.7.0] - 2026-08-14 (Hero Header & Top Branding Simplification Release)

### 🌟 Summary
- **Title Update**: Changed top title & navbar brand from `0 Margin EU Travel` to `0 Margin Travel(EU)`.
- **Subtitle Update**: Simplified subtitle to `AI Route Planner & Multi-Stop Google Maps Navigation.`
- **Removed Redundant Tagline**: Completely deleted `"0 Margin EU Travel: Custom AI Itineraries & Multi-Stop Google Maps Routes."` hero tagline box.
- **Ultra-Clean Step Flow**:
  - `Select Must-Visit Spots.`
  - `1. Pick your destination Country`
  - `2. Pick your destination city`
  - `3. Select your "Must-Visit Spots"`
  - `4. Get TWO type of Google Maps navigation Link!`

---

## 🏷️ [v1.6.0] - 2026-08-14 (Time Window Alignment & Route B AI Cafe/Dinner Recommendation Guarantee Release)

### 🌟 Summary
- **Refined Time Window Definitions**:
  1. **`🌅 観光`**: (午前〜午後早め: 10:00〜17:30) — Museums, Palaces, Cathedrals, Landmarks.
  2. **`☕ カフェ`**: (午後お茶タイム: 14:30〜16:30) — Cafés, Bakeries, Tea Rooms, Parks.
  3. **`🍷 ディナー`**: (夕食時間: 17:30〜20:30) — Bistros, Restaurants, Gourmet Dining.
  4. **`🌙 夜景・散策`**: (夜間・締めくくり: 20:00以降) — River Cruises, Bridges, Plazas, Night Scenery.
- **Route B Mandatory AI Recommendation Guarantees**:
  - Automatically injects **1 top Café/Bakery spot** if no café was selected by the user.
  - Automatically injects **1 top Bistro/Restaurant spot** if no dinner spot was selected by the user.
  - Automatically injects **1 top Night Scenery/Walk spot** if no night walk was selected by the user.
- **Guaranteed Balanced 1-Day Itinerary**: Route B now consistently offers a complete, turn-by-turn European experience with morning sights, afternoon tea break, evening dining, night walk, and return hotel!

---

## 🏷️ [v1.5.0] - 2026-08-14 (Return Hotel Routing & Landmark Hotel Spot Cards Release)

### 🌟 Summary
- **Iconic Landmark Hotel Cards**: Added legendary 5-star landmark hotels (e.g., Ritz Paris, Hotel Adlon Kempinski Berlin, Amstel Hotel Amsterdam, Hotel Metropole Brussels, Bayerischer Hof Munich, etc.) to all 7 city modules in Step 2 (`Hotel & Stay` category).
- **Custom Return Hotel Input Field**: Added a sleek hotel input field (`aiPlanHotelInput`) in Step 3 where users can enter their specific accommodation/hotel address.
- **Automatic Fallback to Landmark Hotel**: If the input field is left empty, the engine automatically selects the city's #1 landmark hotel as the default return destination.
- **Route B Final Return Stop**: Appends the Hotel as the **final destination (Stop 10)** in Route B with a distinct purple `🏨 帰着ホテル` badge, ensuring turn-by-turn navigation concludes straight back at the user's hotel!

---

## 🏷️ [v1.4.0] - 2026-08-14 (Smart Time-of-Day & Operating Hours Itinerary Optimization Release)

### 🌟 Summary
- **Category Time-of-Day Sequencing (`getCategoryTimeSlot`)**:
  1. **Slot 1 (Morning & Early Afternoon)**: Museums, Palaces, Cathedrals, Indoor Landmarks (close early around 17:00–18:00).
  2. **Slot 2 (Mid-Afternoon Tea Break)**: Cafés, Bakeries, Tea Rooms, Parks, Gardens (14:30–16:30 break).
  3. **Slot 3 (Evening Dinner)**: Bistros, Restaurants, Gourmet Dining (18:30–20:30 dinner).
  4. **Slot 4 (Night & Open Air Walk)**: River Cruises, Bridges, Plazas, Night Scenery (no closing times / illuminated).
- **Proximity Sorter Within Time Slots**: Sub-sorts venues within each time-of-day bucket using Nearest Neighbor Haversine Spatial Distance, guaranteeing zero backtracking!
- **Time Slot Badges**: Route manager items display `🌅 観光`, `☕ カフェ`, `🍷 ディナー`, and `🌙 夜景・散策` badges for instant itinerary awareness.

---

## 🏷️ [v1.3.0] - 2026-08-14 (Intelligent Geographical Travel Flow Optimization Release)

### 🌟 Summary
- **Intelligent Spatial Flow Routing (`optimizeRouteOrder`)**: Implemented a Nearest-Neighbor Traveling Salesperson Algorithm using exact Haversine geographical coordinates (`lat`, `lng`) across all 161 candidate spots.
- **Route A Flow Optimization**: Selected must-visit spots are sequenced in a continuous, smooth geographical travel flow (導線) instead of arbitrary checkbox click order.
- **Route B Seamless Interleaving**: All 10 spots in Route B (selected must-visits + top AI recommended spots) are geographically interleaved into ONE single continuous 1-day travel course without backtracking.
- **Clear Item Badging**: Items in Route B clearly display `📍 選択` (emerald badge for user-selected spots) and `✨ AI推し` (gold badge for AI recommended spots) while following the optimal spatial sequence.

---

## 🏷️ [v1.2.8] - 2026-08-14 (Compact Mode Zero-Height Budget Badge Release)

### 🌟 Summary
- **Zero-Height Budget Badge**: Added a clean, ultra-compact budget badge (e.g., `€13`, `Free`, `€10`) directly adjacent to the star rating (`★4.8`) in the right column top row of Compact Mode cards.
- **Zero Height Increase**: Integrates estimated venue prices side-by-side with ratings, keeping card height 100% unchanged without adding extra vertical lines!

---

## 🏷️ [v1.2.7] - 2026-08-14 (Borderless Atelier Layout & 3-Line Description Clamp Release)

### 🌟 Summary
- **Seamless Borderless Layout**: Completely removed heavy outer planner box borders, sketch shadows, and middle section box borders! Candidate spot cards are now the only clean, elegant card elements.
- **3-Line Description Expansion**: Increased compact mode description clamp from 2 lines to **3 lines** (`-webkit-line-clamp: 3`), providing richer venue detail while keeping the layout clean and high-density!

---

## 🏷️ [v1.2.6] - 2026-08-14 (Zero Mobile Outer Margin Release)

### 🌟 Summary
- **Zero Mobile Outer Side Margins**: Reduced side padding across `.container` (4px), `.planner-outer-box` (5px), `.step1-container` (5px), and `.step2-container` (5px) on mobile screens.
- **Maximum Screen Width Utilization**: Eliminates 160px+ of wasted side padding, expanding Step 1 & Step 2 form boxes and candidate cards to span 98%+ of the full mobile screen width edge-to-edge.

---

## 🏷️ [v1.2.5] - 2026-08-14 (Stacked Right Column & Interactive Photo Card Popup Release)

### 🌟 Summary
- **Stacked Right Column Layout**: Rearranged the right side of Compact mode candidate cards into a clean 3-part vertical column:
  1. **Top**: Star Rating Badge (`★4.8`)
  2. **Middle**: Google Maps Pin Link (`📍↗`)
  3. **Bottom**: `More` Detail Popup Button
- **Interactive Photo Card Popup Modal**: Tapping or holding the `More` button instantly pops up a rich modal card showing high-res photo, Wikipedia badge, full un-truncated description, price, category/zone/kids tags, and direct Google Maps navigation!
- **100% Full Width Title Line**: Title on Line 1 has maximum horizontal space to wrap cleanly up to 2 lines without truncation.

---

## 🏷️ [v1.2.4] - 2026-08-14 (No Inner Tags & Clamped 2-Line Description Release)

### 🌟 Summary
- **No Inner Tag Badges**: Completely removed inner tag badges (`Landmark`, `🏙️市内`, `🧸Kids`) from inside individual candidate cards in Compact Mode to eliminate visual clutter.
- **Rating Placed Directly Next to Title**: Single star rating (`★4.8`) placed immediately adjacent to the spot title on Line 1.
- **Full Width Edge-to-Edge Container**: Step 2 container outer padding on mobile reduced to `0.75rem 0.4rem` so cards span maximum available mobile width.
- **2-Line Title Wrap & 2-Line Description Clamp**: Spot titles wrap cleanly up to 2 lines, and descriptions show up to 2 lines (clamped cleanly with ellipsis).

---

## 🏷️ [v1.2.3] - 2026-08-14 (Spot Title Visibility & Responsive 2-Line Layout Fix)

### 🌟 Summary
- **Prominent Spot Title Display**: Fixed flexbox truncation issue where spot titles disappeared on mobile screens. Spot names (e.g. `Disneyland Paris`, `Eiffel Tower`) now sit prominently on Line 1 with bold text and zero truncation.
- **Clean 2-Line High-Density Cards**: Badges (`Category`, `Area Zone`, `Kids`, `Rating`) are neatly aligned on Line 2 right below the title.
- **Ultra-Compact Height Retained**: Card height remains super slim (~45px), fitting 6-7 spots on a single smartphone screen without scrolling!

---

## 🏷️ [v1.2.2] - 2026-08-14 (Ultra-Compact Mobile Layout & Rating Cleanup Release)

### 🌟 Summary
- **High-Density Compact Mode**: Reduced vertical card padding from 0.75rem to 0.4rem, reduced list item gap to 0.35rem, allowing **6 to 8 candidate spots** to fit on a single mobile screen without scrolling!
- **Ultra-Compact Google Maps Icon Button**: Reduced Maps button from wide text (`📍 Maps ↗`) to ultra-compact icon (`📍↗`), freeing up 90%+ of horizontal row width for spot names and badges!
- **Rating Duplicate Star Fix**: Fixed duplicate star formatting (e.g. `★★4.8` -> clean single star `★4.8`).

---

## 🏷️ [v1.2.1] - 2026-08-14 (Country-City Cascading Select & Strict Kids Tag Release)

### 🌟 Summary
- **Step 1 Cascading Form**: Added `国 (Country)` dropdown (`フランス`, `ドイツ`, `オランダ`, `ベルギー`, `ルクセンブルク`). `都市 (City)` dropdown automatically updates based on selected country (e.g. Germany -> Berlin, Cologne, Munich).
- **Strict Kids Tag Sanitization**: Removed `kids` tag from cafes, bakeries, bars, and generic venues. Applied `kids` tag ONLY to genuine kid-friendly attractions (theme parks, zoos, aquariums, science/toy museums, parks with playgrounds/carousels, wax museums, boat cruises).
- **10 New Paris Kid-Friendly Spots Added**:
  1. Disneyland Paris (郊外)
  2. Grande Galerie de l'Évolution / Jardin des Plantes (市内)
  3. Cité des Sciences et de l'Industrie / Cité des Enfants (市内)
  4. Jardin d'Acclimatation (市内)
  5. Parc Zoologique de Paris (市内)
  6. Aquarium de Paris (市内)
  7. Musée Grévin (市内)
  8. Jardin des Tuileries (市内)
  9. Musée de l'Air et de l'Espace (郊外)
  10. Choco-Story Paris (市内)

---

## 🏷️ [v1.2.0] - 2026-08-14 (Area Zone & Kids Filter Release)

### 🌟 Summary
- **Step 1 Form Simplification**: Removed `Traveler Type` and `Transportation Mode` dropdowns. Added clean `エリア選択 (Area Zone)` dropdown (`✨ すべて (市内＋郊外)`, `🏙️ 市内スポット`, `🏞️ 郊外・日帰りスポット`).
- **Step 2 Kids Filter Chips & Multi-Tagting**: Added `🧸 Kids (子供向け)` filter chip to Step 2. Supports multi-category matching (e.g. NEMO Science Museum or Pompidou Center appear under BOTH `🎨 美術館・博物館` and `🧸 Kids`).
- **Cascading Filter Logic**: Selecting "Paris" + "郊外" in Step 1 automatically filters Step 2 to Paris suburban spots (e.g. Versailles, Disneyland Paris). Clicking `🧸 Kids` in Step 2 further narrows down to Paris suburban kid-friendly attractions!
- **Visual Badge System**: Every spot candidate card displays `🏙️ 市内` or `🏞️ 郊外` and `🧸 Kids` badges.

---

## 🏷️ [v1.0.0-stable] - 2026-08-14 (Baseline Checkpoint)

### 🌟 Summary
- **7 European Cities Fully Active**: Paris (45), Berlin (32), Amsterdam (20), Brussels (13), Luxembourg City (20), Cologne (9), Munich (12). Total 151 Candidate Spots.
- **Ultra-Simple Wikipedia REST Summary API Architecture**: 110 spots with verified official Wikipedia summary photos (73% photo match rate across all cities).
- **0% Photo Mismatch Guard**: 41 local cafes/bakeries cleanly fall back to Warm Atelier Category Header Boxes.
- **UI Fallback Protection**: Added `onerror` handler to hide broken image boxes instantly if browser CDN throttling occurs.

### 🔖 Git Tag Rollback Command
To instantly roll back the entire codebase to this exact working version at any point in the future:
```bash
git checkout v1.0.0-stable
```

---

## 🚀 How Version Rollbacks Work

1. **Roll Back Entire Codebase (Local Testing)**:
   ```bash
   git checkout v1.0.0-stable
   ```
2. **Roll Back GitHub Pages Deployment**:
   ```bash
   git checkout main
   git reset --hard v1.0.0-stable
   git push origin main --force
   ```
3. **Return to Latest Development**:
   ```bash
   git checkout main
   ```
