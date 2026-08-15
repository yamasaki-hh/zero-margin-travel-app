# Zero-Margin Travel App - Version Changelog

All notable changes and release checkpoints for the Zero-Margin Travel App will be documented in this file.

---

## 🏷️ [v3.2.0] - 2026-08-15 (Original Strawberry Elephant Mascot Integration)

### 🎨 Mascot Branding Integration
- **Original Mascot Extraction**: Extracted and recreated the user's original hybrid mascot character (Strawberry Elephant head with green dragon/dinosaur body 🍓🐉) into high-resolution transparent vector/PNG web assets (`assets/mascot.png`).
- **Navbar Integration**: Replaced text placeholder with interactive mascot icon in the main top header with micro-animations.
- **Hero Section Companion Badge**: Added interactive mascot travel buddy welcome badge with floating bounce animation (`floatBounce`).
- **Cache Busters**: Updated version parameters in `index.html` to `v=68.0`.

---

## 🏷️ [v3.1.0] - 2026-08-15 (Global Kids & Family Category Strict Curation)

### 🧹 Quality & Categorization Enhancements
- **Strict Kids Category Filtering**: Removed all general cafes, bistros, bakeries, food markets, fine art museums, adult monuments, and generic walking spots from the `kids: true` tag across all 12 European cities.
- **Dedicated Family Standards**: Restricted `kids: true` exclusively to Zoos, Aquariums, Theme Parks, Interactive/Experiential Museums (Science, Miniature, Cinema, Chocolate), Puppet Theaters, Major Playground/Splash Parks, and Iconic Family Landmarks (Eiffel Tower).
- **Scaled City Ratios (Paris Upper Limit = 13)**:
  - **Paris**: 13 spots (Disneyland, Cité des Sciences, Zoo, Aquarium, Eiffel, Luxembourg, Choco-Story)
  - **Bordeaux**: 7 spots (Water Mirror, Cap Sciences, Zoo, Arcachon Dune, Bassins des Lumières, Jardin Public, Accro-Batches)
  - **Lyon**: 6 spots (Miniature Museum, Mini World, Aquarium, Planetarium, Guignol Puppets, Parc de la Tête d'Or)
  - **Marseille**: 6 spots (Cosquer Cave, Prado Beach Park, Magic Park Land, Figuerolles Farm, Parc Borély, Petit Train)
  - **Nice**: 5 spots (Monaco Aquarium, Paillon Marine Playground, Parc Phoenix Zoo, Glacier Fenocchio, Castle Hill Waterfall)
  - **Strasbourg**: 6 spots (Europa-Park, Le Vaisseau Science Center, Écomusée d'Alsace, Stork Sanctuary, Tomi Ungerer Museum, Citadelle Park)
  - **Amsterdam**: 3 spots | **Berlin**: 3 spots | **Munich**: 2 spots | **Brussels**: 2 spots | **Luxembourg**: 2 spots | **Cologne**: 1 spot
- **Cache Busters**: Updated version parameters in `index.html` to `v=67.0`.

---

## 🏷️ [v3.0.0] - 2026-08-14 (Marseille City Database Release - 43 Curated Spots)

### 🌟 Major Milestone Reached
- **Created Marseille City Database Module** (`data/cities/marseille.json`): Added 43 curated, verified ★4.5+ attractions across 5 core categories (`Landmark`, `Museum & Gallery`, `Café & Bistro`, `Scenery & Walk`, `Kids & Family`).
  - **Landmarks (11 spots)**: Basilique Notre-Dame de la Garde, Vieux-Port de Marseille & Ombrière, Cathédrale de la Major, Fort Saint-Jean, Fort Saint-Nicolas, Palais Longchamp, Cité Radieuse Le Corbusier, Abbaye Saint-Victor, Orange Vélodrome Stadium, Château d'If, Château de la Buzine.
  - **Museums & Galleries (9 spots)**: MuCEM, Grotte Cosquer (Cosquer Méditerranée), Musée d'Histoire de Marseille, Musée des Beaux-Arts, Musée Cantini, MAC, Muséum d'Histoire Naturelle, Friche la Belle de Mai, Musée de la Faïence (Château Borély).
  - **Cafés & Dining (8 spots)**: Chez Fonfon (Vallon des Auffes), Le Miramar, Marché aux Poissons du Vieux-Port, Marché de Noailles, Four des Navettes, La Samaritaine & Café de la Banque, Maison de la Boule & Savonneries, L'Épuisette.
  - **Scenery & Walks (9 spots)**: Le Panier, Vallon des Auffes, Corniche du Président Kennedy, Cours Julien, Vieille Charité, Place aux Huiles & Cours Estienne-d'Orves, Parc National des Calanques, Îles du Frioul, Les Goudes & Cap Croisette.
  - **Kids & Family (6 spots)**: Parc Borély & Jardin Botanique, Le Petit Train de Marseille, Croisières du Vieux-Port, Plage du Prado, Magic Park Land, Parc de Figuerolles.
- **Wikipedia Resolver Pipeline**: Resolved 14 Wikipedia thumbnail images and exact Haversine coordinates for Marseille, expanding the global spots database to **371 total spots across 12 Western European cities**.
- **Cache Busters**: Updated version parameters in `index.html` to `v=66.0`.

---

## 🏷️ [v2.9.0] - 2026-08-14 (Bordeaux City Database Release - 40 Curated Spots)

### 🌟 Features Added
- **Created Bordeaux City Database Module** (`data/cities/bordeaux.json`): Added 40 curated, verified ★4.5+ attractions across 5 core categories (`Landmark`, `Museum & Gallery`, `Café & Bistro`, `Scenery & Walk`, `Kids & Family`).
  - **Landmarks (11 spots)**: Place de la Bourse & Miroir d'eau, Grand Théâtre de Bordeaux, Cathédrale Saint-André & Tour Pey-Berland, Porte Cailhau, Grosse Cloche, Basilique Saint-Michel, Monument aux Girondins, Palais Gallien, Pont de Pierre, Château de Roquetaillade, Château de La Brède.
  - **Museums & Galleries (8 spots)**: Cité du Vin, Bassins des Lumières, Musée d'Aquitaine, Musée des Beaux-Arts, CAPC Musée d'Art Contemporain, MADD, Musée Mer Marine, Musée National des Douanes.
  - **Cafés & Dining (7 spots)**: Marché des Capucins, Brasserie Bordelaise, Canelé Baillardran & La Toque Cuivrée, Le Bar à Vin (CIVB), Café Français, L'Entrecôte Bordeaux, Grand Cru Wineries (Saint-Émilion, Médoc).
  - **Scenery & Walks (8 spots)**: Quartier Saint-Pierre, Quartier des Chartrons, Les Quais de Bordeaux, Rue Sainte-Catherine, Place des Quinconces, Darwin Eco-Système, Saint-Émilion Medieval Village (UNESCO), Dune du Pilat & Arcachon Bay.
  - **Kids & Family (6 spots)**: Jardin Public & Muséum de Bordeaux, Cap Sciences, Bordeaux River Cruise / Bat3, Parc Bordelais, Zoo de Bordeaux-Pessac, La Forêt des Accro-Batches.
- **Wikipedia Resolver Pipeline**: Resolved 11 Wikipedia thumbnail images and exact Haversine coordinates for Bordeaux, expanding the global spots database to **328 total spots across 11 Western European cities**.
- **Cache Busters**: Updated version parameters in `index.html` to `v=65.0`.

---

## 🏷️ [v2.8.0] - 2026-08-14 (Strasbourg City Database Release - 45 Curated Spots)

### 🌟 Features Added
- **Created Strasbourg City Database Module** (`data/cities/strasbourg.json`): Added 45 curated, verified ★4.5+ attractions across 5 core categories (`Landmark`, `Museum & Gallery`, `Café & Bistro`, `Scenery & Walk`, `Kids & Family`).
  - **Landmarks (13 spots)**: Strasbourg Cathedral, Barrage Vauban, Ponts Couverts, Palais Rohan, Maison Kammerzell, Place Kléber, Place Gutenberg, European Parliament, Palais du Rhin, Église Saint-Thomas, Église Saint-Paul, Château du Haut-Kœnigsbourg, Mont Sainte-Odile Monastery.
  - **Museums & Galleries (9 spots)**: Musée Alsacien, Musée de l'Œuvre Notre-Dame, Musée des Beaux-Arts, Musée des Arts Décoratifs, MAMCS, Musée Tomi Ungerer, Musée Historique, Château Musée Vodou, Musée Lalique.
  - **Cafés & Dining (8 spots)**: Cave Historique des Hospices de Strasbourg, Maison des Tanneurs, Winstub Chez Yvonne, Winstub Le Tire-Bouchon, Pâtisserie Christian, Kugelhopf Bakeries, Brasserie Les Haras, Route des Vins d'Alsace Wineries.
  - **Scenery & Walks (9 spots)**: La Petite France, La Grande Île (UNESCO), Quartier Neustadt, Quai des Bateliers, Lycée des Pontonniers, Krutenau District, Batorama Boat Tour, Obernai, Riquewihr & Kaysersberg.
  - **Kids & Family (6 spots)**: Parc de l'Orangerie & Stork Sanctuary, Le Vaisseau Science Center, Parc de la Citadelle, Jardin des Deux Rives, Écomusée d'Alsace, Europa-Park.
- **Wikipedia Resolver Pipeline**: Resolved 15 Wikipedia thumbnail images and exact Haversine coordinates for Strasbourg, expanding the global spots database to **288 total spots across 10 Western European cities**.
- **Cache Busters**: Updated version parameters in `index.html` to `v=64.0`.

---

## 🏷️ [v2.7.0] - 2026-08-14 (Lyon City Database Release - 46 Curated Spots)

### 🌟 Features Added
- **Created Lyon City Database Module** (`data/cities/lyon.json`): Added 46 curated, verified ★4.5+ attractions across 5 core categories (`Landmark`, `Museum & Gallery`, `Café & Bistro`, `Scenery & Walk`, `Kids & Family`).
  - **Landmarks (10 spots)**: Basilique Notre-Dame de Fourvière, Cathédrale Saint-Jean-Baptiste, Ancient Theatre of Fourvière, Place Bellecour, Place des Terreaux & Bartholdi Fountain, Grand Hôtel-Dieu, Amphitheatre of the Three Gauls, Église Saint-Nizier, La Tourette Monastery, Château de Rochetaillée.
  - **Museums & Galleries (12 spots)**: Musée des Beaux-Arts, Musée des Confluences, Cinema and Miniature Museum, Institut Lumière, Gadagne Museum, Musée des Tissus, Museum of Printing, Lugdunum Museum, CHRD, macLYON, Tony Garnier Urban Museum, Clément Ader Aviation Museum.
  - **Cafés & Dining (8 spots)**: Les Halles de Lyon Paul Bocuse, Historic Bouchons (Café des Fédérations), Cité Internationale de la Gastronomie, La Maison Sève, Maison Bernachon, Café Comptoir Abel, Brasserie Georges, Restaurant Paul Bocuse.
  - **Scenery & Walks (11 spots)**: Vieux Lyon & Secret Traboules, Croix-Rousse Hill, Cour des Voraces, Fresque des Lyonnais, Mur des Canuts, Passerelle Saint-Georges, Saône & Rhône Promenade, Jardin des Curiosités, Confluence Waterfront, Île Barbe, Medieval Village of Pérouges.
  - **Kids & Family (5 spots)**: Parc de la Tête d'Or, Théâtre Guignol de Lyon, Aquarium de Lyon, Mini World Lyon, Planétarium de Vaulx-en-Velin.
- **Wikipedia Resolver Pipeline**: Resolved 18 Wikipedia thumbnail images and exact Haversine coordinates for Lyon, expanding the global spots database to 243 total spots across 9 Western European cities.
- **Cache Busters**: Updated version parameters in `index.html` to `v=63.0`.

---

## 🏷️ [v2.6.0] - 2026-08-14 (100% Global English UI Unification Release)

### 🌟 UI/UX & Localization Unification
- **100% English UI Translation**: Converted all remaining Japanese UI labels, tags, dropdown options, section headers, badges, button texts, inputs, filter chips, and modal overlays into clean, professional, high-converting English across the entire platform.
- **Form Controls & Dropdowns**:
  - `Country:` (`France`, `Germany`, `Netherlands`, `Belgium`, `Luxembourg`)
  - `City:` (`Paris`, `Nice & Côte d'Azur`, `Berlin`, `Cologne`, `Munich`, `Amsterdam`, `Brussels`, `Luxembourg`)
  - `Area Zone:` (`✨ All Spots (City + Suburban)`, `🏙️ City Center Spots`, `🏞️ Suburban & Day Trips`)
  - `Return Hotel / Stay:` (`Optional — Appended as final destination to Route A & B`)
- **Category Filter Chips & View Mode**:
  - Filter Chips: `🏛️ Landmarks`, `🎨 Museums`, `☕ Cafés & Dining`, `🌆 Scenery & Walks`, `🧸 Kids & Family`
  - View Mode Bar: `📱 View Mode:` | `⚡ Compact List (Fast)` | `🖼️ Visual Cards (Photos)`
- **Dynamic Route Badges & Items**:
  - Route A/B Badges: `📍 Selected`, `✨ AI Pick`, `🏞️ Suburban`, `🏙️ City Center`, `🏨 Return Hotel`
  - Time-of-Day Slots: `🌅 Sightseeing`, `☕ Café Break`, `🍷 Dinner`, `🌙 Night Scenery`
- **Cache Busters**: Bumped version parameters in `index.html` to `v=62.0`.

---

## 🏷️ [v2.5.0] - 2026-08-14 (Added 6 Nice Suburban Riviera Landmarks Release)

### 🌟 Features Added
- **Added 6 Requested Riviera & Suburban Spots to Nice Module** (`data/cities/nice.json`):
  1. **Musée Picasso (Antibes)** (`suburban`, `Museum & Gallery`, `★4.6`, Entry: €8) - Picasso's former seaside atelier in Château Grimaldi.
  2. **Casino de Monte-Carlo** (`suburban`, `Landmark`, `★4.7`, Tour: €18) - Charles Garnier's famed Belle Époque gambling hall in Monaco.
  3. **Basilique Saint-Michel Archange & Menton Old Town** (`suburban`, `Landmark`, `★4.7`, Free) - Menton's iconic 17th-century Baroque bell tower & pastel old town.
  4. **Le Sentier du Littoral (Cap d'Antibes)** (`suburban`, `Scenery & Walk`, `★4.8`, Free) - 5km coastal cliffside trail around Cap d'Antibes.
  5. **Abbaye de Lérins (Saint-Honorat Island)** (`suburban`, `Landmark`, `★4.7`, Ferry: €16) - 5th-century Cistercian island monastery off Cannes.
  6. **Fort du Mont Alban** (`suburban`, `Landmark`, `★4.6`, Free) - 1560 hilltop military fortress offering views over Nice & Villefranche.
- **Wikipedia Resolver Pipeline**: Resolved Wikipedia thumbnail images and exact Haversine coordinates for all 36 Nice spots.

---

## 🏷️ [v2.4.1] - 2026-08-14 (Fix City Dropdown Initial Population & HTML Fallback Option Release)

### 🌟 Fixes
- **HTML Select Initial Option**: Added `<option value="Nice, France">🇫🇷 ニース (Nice & Côte d'Azur)</option>` directly inside `<select id="aiPlanDestination">` in `index.html`.
- **Automatic Load Synchronization**: Updated `window.addEventListener('load')` in `index.html` to trigger `window.AITravelEngine.onCountryChange()`, ensuring the city dropdown is dynamically populated on page boot without requiring the user to switch country selections.
- **Selection Preservation**: Updated `onCountryChange()` logic to preserve selected city values when populating options.

---

## 🏷️ [v2.4.0] - 2026-08-14 (Nice & Côte d'Azur 30 Curated Spots Release)

### 🌟 Summary
- **Added Nice & Côte d'Azur (ニース & コート・ダジュール) Module**:
  - Created `data/cities/nice.json` with 30 curated attractions across all 5 core categories:
    - **Landmark**: Castle Hill (Colline du Château), Place Masséna, St. Nicholas Russian Cathedral, Cathédrale Sainte-Réparate, Éze Village, Villa Ephrussi de Rothschild, Prince's Palace of Monaco.
    - **Museum & Gallery**: Musée Marc Chagall, Musée Matisse, MAMAC, Villa Masséna, Musée des Beaux-Arts, Villa Kérylos, Fondation Maeght.
    - **Café & Bistro**: Cours Saleya Market, Glacier Fenocchio, Chez René Socca, Le Plongeoir, Grand Café de Turin.
    - **Scenery & Walk**: Promenade des Anglais, Vieux Nice (Old Town), Port Lympia, Mont Boron Forest Park, Cap de Nice Coastal Path, Villefranche-sur-Mer, Saint-Paul-de-Vence.
    - **Kids & Family**: Promenade du Paillon, Parc Phœnix, Oceanographic Museum of Monaco.
- **Location Zone Filtering**: Categorized into `city` (inside Nice) and `suburban` (Éze, Saint-Jean-Cap-Ferrat, Villefranche, Saint-Paul-de-Vence, Monaco).
- **Wikipedia Resolver Pipeline**: Resolved Wikipedia thumbnail images and exact Haversine lat/lng coordinates for all 30 spots.

---

## 🏷️ [v2.3.0] - 2026-08-14 (Purge Redundant Transit Badges & Alternative Maps Link Release)

### 🌟 Summary
- **Purged Alternative Maps App Links**: Removed redundant `🔗 Alternative Google Maps App Path Link` buttons from Route A and Route B cards.
- **Purged Transit / Driving Mode Badges**: Deleted unnecessary `🚆 Transit Mode` / `🚗 Driving Mode` badge labels in Route A and Route B card headers.
- **Ultra-Clean Single CTA Result Card**: Each route card now presents exactly ONE primary, high-visibility button: `🗺️ Open Route in Google Maps (N Destinations) ↗`.

---

## 🏷️ [v2.2.0] - 2026-08-14 (Complete Removal of Hotel Cards & Unified Custom Return Hotel for Route A & B Release)

### 🌟 Summary
- **Removed All Hotel Candidate Cards**: Cleaned out all 17 hotel cards across all city JSON modules (`data/cities/*.json`), restoring Step 2 grid to 100% pure Sightseeing Landmarks, Cafes, Bistros, and Night Scenery (161 spots).
- **Unified Custom Return Hotel Logic**:
  - **If User Inputs Hotel (e.g. "Ritz Paris" or "My Airbnb")**: Appended as the final destination stop for **BOTH Route A and Route B**.
  - **If Left Blank**: No hotel is appended to either route; routes terminate naturally at their last sightseeing/dining spot.

---

## 🏷️ [v2.1.0] - 2026-08-14 (Iconic Paris 5-Star Palace Hotels & Hotel Tag Release)

### 🌟 Summary
- **11 Legendary Paris Palace Hotels**: Added iconic 5-star palace hotels in Paris as candidate spot cards in Step 2:
  1. `Ritz Paris (Hotel)` — Place Vendôme
  2. `Le Meurice (Hotel)` — Rue de Rivoli / Tuileries
  3. `Hôtel Plaza Athénée (Hotel)` — Avenue Montaigne / Dior
  4. `Four Seasons Hotel George V (Hotel)` — Avenue George V
  5. `Le Bristol Paris (Hotel)` — Rue du Faubourg Saint-Honoré
  6. `Hôtel de Crillon (Hotel)` — Place de la Concorde
  7. `Shangri-La Paris (Hotel)` — Avenue d'Iéna / Eiffel View
  8. `The Peninsula Paris (Hotel)` — Avenue Kléber
  9. `La Réserve Paris (Hotel)` — Avenue Gabriel
  10. `Mandarin Oriental, Paris (Hotel)` — Rue Saint-Honoré
  11. `Prince de Galles (Hotel)` — Avenue George V / Art Deco
- **Category Tag & Badge**: Added `Hotel & Stay` category with `🏨 Hotel` badge.
- **100% English Language**: All names, descriptions, prices, and location details formatted strictly in English.

---

## 🏷️ [v2.0.0] - 2026-08-14 (Premium Hero Copy & 3-Step Flow Marketing Copy Release)

### 🌟 Summary
- **Hero Headline Update**:
  - Main Title: `Explore Europe Smarter with Instant Google Maps Routes.`
  - Highlight Subtitle: `Curated ★4.5+ spots. Zero planning fatigue.`
  - Body Copy: `Pick your must-visit landmarks, bistros, and gems — get ready-to-use multi-stop Google Maps navigation in seconds.`
- **Interactive Planner Header**:
  - Title: `Build Your Custom Day in 3 Simple Steps`
- **3-Step Flow Headlines**:
  - **Step 1**: `Step 1: Choose Destination — Select your country & city`
  - **Step 2**: `Step 2: Pick Your Spots — Handpick your favorites from Verified ★4.5+ places`
  - **Step 3**: `Step 3: Launch in Maps — Choose Route A (Selected only) or Route B (Curated full-day loop)`

---

## 🏷️ [v1.9.0] - 2026-08-14 (Complete Gemini API Key UI Removal & 100% Standalone Free Architecture Release)

### 🌟 Summary
- **Gemini API Key UI Removal**: Removed `🔑 Config Gemini API Key` button from top Navbar and sticky mobile bottom bar.
- **100% Standalone Client Engine**: Cleaned up `configureGeminiKey` and legacy API key prompt code.
- **Instant 0ms Instant Load**: App relies 100% on pre-baked, verified, ★4.5+ curated spots across all 7 city modules (168 candidate spots). Zero setup friction for end users!

---

## 🏷️ [v1.8.0] - 2026-08-14 (Human Daily Travel Rhythm Sorter & Non-Consecutive Dining Release)

### 🌟 Summary
- **Eliminated Consecutive Food/Drink Stops**: Prevented back-to-back Café (#7) and Dinner (#8) stops in Route B.
- **Human Daily Travel Rhythm Sorter**:
  - **Morning Sightseeing Phase (Stops 1–3)**: Museums, Palaces, Cathedrals.
  - **Mid-Day Lunch & Café Break (Stop 4)**: Placed right in the middle of the day (~13:30–15:30)!
  - **Late Afternoon Sightseeing Phase (Stops 5–7)**: Landmarks, Parks, Shopping, Galleries.
  - **Evening Dinner Phase (Stop 8)**: Fine Bistros & Gourmet Restaurants (~18:30–20:30).
  - **Night Scenery & Evening Walk (Stop 9)**: River Walks & Illuminated Night Scenery.
  - **Return Hotel (Stop 10)**: Final Hotel destination.
- **Geographical Distance (導線) Optimization**: Each sub-phase remains strictly sorted by nearest-neighbor geographical distance!

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
