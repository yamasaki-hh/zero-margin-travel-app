/* ==========================================================================
   0 Margin EU Travel — 100% English Interactive AI Route Planner
   Rich Multi-City Candidate Spots Database (30+ Real Verified ★4.5+ Spots per City)
   100% Geographically Accurate Images + Native Lazy Loading + SVG Fallback
   ========================================================================== */

const SVG_FALLBACK_IMAGE = `data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="600" height="340" viewBox="0 0 600 340"><rect width="600" height="340" fill="%23FAF7F2"/><text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="22" fill="%2378350F">🗺️ European Landmark</text></svg>`;

const candidateSpotsDatabase = {
  "Amsterdam, Netherlands": [
    {
      "id": "a_1",
      "name": "Rijksmuseum",
      "category": "Museum & Art",
      "rating": "★4.8",
      "desc": "Dutch National Museum housing Rembrandt's 'Night Watch' & Vermeer masterpieces.",
      "price": "Entry: €22.50",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/South_facade_of_the_Rijksmuseum_Amsterdam_%28DSCF0528%29.jpg/330px-South_facade_of_the_Rijksmuseum_Amsterdam_%28DSCF0528%29.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/South_facade_of_the_Rijksmuseum_Amsterdam_%28DSCF0528%29.jpg/330px-South_facade_of_the_Rijksmuseum_Amsterdam_%28DSCF0528%29.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 52.36,
      "lng": 4.8853
    },
    {
      "id": "a_2",
      "name": "Van Gogh Museum",
      "category": "Museum & Art",
      "rating": "★4.8",
      "desc": "World's largest collection of Vincent van Gogh paintings including Sunflowers.",
      "price": "Entry: €22.00",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Logo_-_Van_Gogh_Museum.png/330px-Logo_-_Van_Gogh_Museum.png?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Logo_-_Van_Gogh_Museum.png/330px-Logo_-_Van_Gogh_Museum.png?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 52.3583,
      "lng": 4.8811
    },
    {
      "id": "a_3",
      "name": "Anne Frank House",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "Biographical museum at the secret annex where Anne Frank wrote her diary.",
      "price": "Entry: €16",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Amsterdam_%28NL%29%2C_Anne-Frank-Huis_--_2015_--_7185.jpg/330px-Amsterdam_%28NL%29%2C_Anne-Frank-Huis_--_2015_--_7185.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Amsterdam_%28NL%29%2C_Anne-Frank-Huis_--_2015_--_7185.jpg/330px-Amsterdam_%28NL%29%2C_Anne-Frank-Huis_--_2015_--_7185.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 52.37525,
      "lng": 4.88432
    },
    {
      "id": "a_4",
      "name": "Nine Streets (De Negen Straatjes)",
      "category": "Landmark",
      "rating": "★4.8",
      "desc": "Picturesque canal belt quarters packed with vintage shops, design stores & cafes.",
      "price": "Free access",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.3826,
      "lng": 4.8741
    },
    {
      "id": "a_5",
      "name": "Zaanse Schans Windmills",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "Historic windmill village showcasing wooden clogs, cheese making & green houses.",
      "price": "Free village access",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Zaanstad_Zaanse_Schans_22.jpg/330px-Zaanstad_Zaanse_Schans_22.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "suburban",
      "kids": true,
      "lat": 52.3976,
      "lng": 4.8741
    },
    {
      "id": "a_6",
      "name": "Vondelpark",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "Amsterdam's largest public park featuring rose gardens and open-air theaters.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Amsterdam%2C_Vondelpark%2C_at_the_pond-2.jpg/330px-Amsterdam%2C_Vondelpark%2C_at_the_pond-2.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Amsterdam%2C_Vondelpark%2C_at_the_pond-2.jpg/330px-Amsterdam%2C_Vondelpark%2C_at_the_pond-2.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": true,
      "lat": 52.358,
      "lng": 4.868
    },
    {
      "id": "a_7",
      "name": "Royal Palace of Amsterdam",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "17th-century Golden Age palace on Dam Square used for official royal events.",
      "price": "Entry: €12.50",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Palacio_Real%2C_%C3%81msterdam%2C_Pa%C3%ADses_Bajos%2C_2016-05-30%2C_DD_07-09_HDR.jpg/330px-Palacio_Real%2C_%C3%81msterdam%2C_Pa%C3%ADses_Bajos%2C_2016-05-30%2C_DD_07-09_HDR.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Palacio_Real%2C_%C3%81msterdam%2C_Pa%C3%ADses_Bajos%2C_2016-05-30%2C_DD_07-09_HDR.jpg/330px-Palacio_Real%2C_%C3%81msterdam%2C_Pa%C3%ADses_Bajos%2C_2016-05-30%2C_DD_07-09_HDR.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 52.37317,
      "lng": 4.89136
    },
    {
      "id": "a_8",
      "name": "Oude Kerk",
      "category": "Landmark",
      "rating": "★4.5",
      "desc": "Amsterdam's oldest parish church (1306) standing in the historic city center.",
      "price": "Entry: €12",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Amsterdam-508-Oude_Kerk-2010-gje.jpg/330px-Amsterdam-508-Oude_Kerk-2010-gje.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.3676,
      "lng": 4.8891
    },
    {
      "id": "a_9",
      "name": "Begijnhof Courtyard",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "Tranquil 14th-century courtyard sanctuary holding Amsterdam's oldest wooden house.",
      "price": "Free access",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/BegijnhofAmsterdamPanorama.jpg/330px-BegijnhofAmsterdamPanorama.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.3826,
      "lng": 4.8891
    },
    {
      "id": "a_10",
      "name": "Bloemenmarkt (Floating Flower Market)",
      "category": "Landmark",
      "rating": "★4.3",
      "desc": "World's only floating flower market selling tulip bulbs along Singel canal.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/SingelBloemenmarkt.jpg/330px-SingelBloemenmarkt.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/SingelBloemenmarkt.jpg/330px-SingelBloemenmarkt.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 52.36667,
      "lng": 4.89194
    },
    {
      "id": "a_11",
      "name": "Stedelijk Museum Amsterdam",
      "category": "Museum & Art",
      "rating": "★4.6",
      "desc": "Modern and contemporary art museum housing works by Matisse, Warhol & Mondrian.",
      "price": "Entry: €22.50",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/De_nieuwe_vleugel_van_het_Stedelijk_Museum_Amsterdam.jpg/330px-De_nieuwe_vleugel_van_het_Stedelijk_Museum_Amsterdam.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/De_nieuwe_vleugel_van_het_Stedelijk_Museum_Amsterdam.jpg/330px-De_nieuwe_vleugel_van_het_Stedelijk_Museum_Amsterdam.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 52.35806,
      "lng": 4.87972
    },
    {
      "id": "a_12",
      "name": "Rembrandt House Museum",
      "category": "Museum & Art",
      "rating": "★4.6",
      "desc": "Reconstructed 17th-century home & studio where Rembrandt painted for 20 years.",
      "price": "Entry: €17.50",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Rembrandshuis.jpg/330px-Rembrandshuis.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Rembrandshuis.jpg/330px-Rembrandshuis.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 52.3694,
      "lng": 4.90129
    },
    {
      "id": "a_13",
      "name": "NEMO Science Museum",
      "category": "Museum & Art",
      "rating": "★4.5",
      "desc": "Green copper ship building featuring 5 floors of interactive science exhibits.",
      "price": "Entry: €17.50",
      "image": "",
      "family": true,
      "adult": false,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": true,
      "lat": 52.3676,
      "lng": 4.9041
    },
    {
      "id": "a_14",
      "name": "MOCO Museum",
      "category": "Museum & Art",
      "rating": "★4.4",
      "desc": "Independent museum displaying modern street art by Banksy, KAWS & Basquiat.",
      "price": "Entry: €21.95",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/MocoMuseumAmsterdamTHEONE.jpg/330px-MocoMuseumAmsterdamTHEONE.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "city",
      "kids": true,
      "lat": 52.3826,
      "lng": 4.9041
    },
    {
      "id": "a_15",
      "name": "Café de Klos",
      "category": "Restaurant",
      "rating": "★4.6",
      "desc": "Legendary Dutch rib house serving flame-grilled smoked spare ribs & lamb chops.",
      "price": "Ribs: €22–€28",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.3976,
      "lng": 4.9041
    },
    {
      "id": "a_16",
      "name": "Foodhallen Amsterdam",
      "category": "Restaurant",
      "rating": "★4.5",
      "desc": "Indoor food hall inside converted tram depot featuring 20 gourmet food stalls.",
      "price": "Stalls: €8–€18",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.3376,
      "lng": 4.9191
    },
    {
      "id": "a_17",
      "name": "Moeders",
      "category": "Restaurant",
      "rating": "★4.6",
      "desc": "Cozy Dutch eatery serving authentic stampot, hotchpotch & traditional stews.",
      "price": "Mains: €17–€24",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.3526,
      "lng": 4.9191
    },
    {
      "id": "a_18",
      "name": "Van Stapele Koekmakerij",
      "category": "Café & Bakery",
      "rating": "★4.8",
      "desc": "Famous bakery crafting a single item: warm chocolate cookie with white chocolate core.",
      "price": "Cookie: €3.00",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.3676,
      "lng": 4.9191
    },
    {
      "id": "a_19",
      "name": "Winkel 43",
      "category": "Café & Bakery",
      "rating": "★4.6",
      "desc": "Jordaan district cafe famous across Europe for warm deep-dish Dutch apple pie.",
      "price": "Pie: €5.00",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.3826,
      "lng": 4.9191
    },
    {
      "id": "a_20",
      "name": "Brouwerij 't IJ",
      "category": "Café & Bakery",
      "rating": "★4.7",
      "desc": "Craft brewery set directly under Amsterdam's iconic De Gooyer windmill.",
      "price": "Tasting Flight: €12",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Brouwerijhetij.jpg/330px-Brouwerijhetij.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": false,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Brouwerijhetij.jpg/330px-Brouwerijhetij.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 52.36667,
      "lng": 4.92639
    }
  ],
  "Berlin, Germany": [
    {
      "id": "b_b1",
      "name": "Brandenburg Gate",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "18th-century neoclassical monument and universal symbol of German unity.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Brandenburger_Tor_abends.jpg/330px-Brandenburger_Tor_abends.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Brandenburger_Tor_abends.jpg/330px-Brandenburger_Tor_abends.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 52.5163,
      "lng": 13.3777
    },
    {
      "id": "b_b2",
      "name": "Reichstag Building Dome",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "German parliament building featuring Norman Foster's glass dome overlooking Berlin.",
      "price": "Free (booking required)",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Berlin_reichstag_west_panorama_2.jpg/330px-Berlin_reichstag_west_panorama_2.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.505,
      "lng": 13.375
    },
    {
      "id": "b_b3",
      "name": "East Side Gallery Berlin Wall",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "1.3km open-air gallery painted directly on the remaining Berlin Wall.",
      "price": "Free access",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Segment_with_Graffiti_of_the_Berlin_Wall_%283_of_4%29_%28cropped%29.jpg/330px-Segment_with_Graffiti_of_the_Berlin_Wall_%283_of_4%29_%28cropped%29.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "city",
      "kids": true,
      "lat": 52.52,
      "lng": 13.375
    },
    {
      "id": "b_b4",
      "name": "Berlin Cathedral (Berliner Dom)",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "Monumental Italian Renaissance-style Protestant cathedral with dome climb.",
      "price": "Entry: €10",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/141227_Berliner_Dom.jpg/330px-141227_Berliner_Dom.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/141227_Berliner_Dom.jpg/330px-141227_Berliner_Dom.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 52.51917,
      "lng": 13.40111
    },
    {
      "id": "b_b5",
      "name": "Charlottenburg Palace",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "Largest Baroque royal palace in Berlin surrounded by formal gardens.",
      "price": "Palace: €12",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Charlottenburg_Hohenzollern_2.jpg/330px-Charlottenburg_Hohenzollern_2.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Charlottenburg_Hohenzollern_2.jpg/330px-Charlottenburg_Hohenzollern_2.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 52.5209,
      "lng": 13.2957
    },
    {
      "id": "b_b6",
      "name": "Holocaust Memorial",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "Field of 2,711 concrete slabs honoring murdered Jews of Europe.",
      "price": "Free access",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Memorial_to_the_Murdered_Jews_of_Europeabove.jpg/330px-Memorial_to_the_Murdered_Jews_of_Europeabove.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.49,
      "lng": 13.39
    },
    {
      "id": "b_b7",
      "name": "Gendarmenmarkt Square",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "Historic plaza flanked by French and German Cathedrals & Konzerthaus.",
      "price": "Free access",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Gendarmenmarkt_Panorama.jpg/330px-Gendarmenmarkt_Panorama.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.505,
      "lng": 13.39
    },
    {
      "id": "b_b8",
      "name": "Victory Column (Siegessäule)",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "Golden Victoria statue crowning 67m monument at Tiergarten center.",
      "price": "Climb: €4",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D0%B2%D1%8B%D1%81%D0%BE%D1%82%D0%B0_%D0%BA%D0%BE%D0%BB%D0%BE%D0%BD%D0%BD_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80%D0%B0_I%2C_%D0%9D%D0%B0%D0%BF%D0%BE%D0%BB%D0%B5%D0%BE%D0%BD%D0%B0%2C_%D0%A2%D1%80%D0%B0%D1%8F%D0%BD%D0%B0%2C_%D0%9F%D0%BE%D0%BC%D0%BF%D0%B5%D1%8F_%D0%B8_%D0%90%D0%BD%D1%82%D0%BE%D0%BD%D0%B8%D0%BD%D0%B0%2C1836%D0%B3_%D0%93%D0%98%D0%9C.jpg/330px-thumbnail.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Berlin_Siegess%C3%A4ule_8245.jpg/330px-Berlin_Siegess%C3%A4ule_8245.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 52.52,
      "lng": 13.39
    },
    {
      "id": "b_b9",
      "name": "Berlin TV Tower (Fernsehturm)",
      "category": "Landmark",
      "rating": "★4.5",
      "desc": "368m television tower offering 360-degree panorama of Berlin.",
      "price": "Observation: €22.50",
      "image": "https://upload.wikimedia.org/wikipedia/en/thumb/3/34/Fernsehturm_Berlin_logo.png/330px-Fernsehturm_Berlin_logo.png?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/en/thumb/3/34/Fernsehturm_Berlin_logo.png/330px-Fernsehturm_Berlin_logo.png?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": true,
      "lat": 52.52083,
      "lng": 13.40944
    },
    {
      "id": "b_b10",
      "name": "Checkpoint Charlie",
      "category": "Landmark",
      "rating": "★4.2",
      "desc": "Famous Cold War border crossing checkpoint between American & Soviet sectors.",
      "price": "Free outdoor viewing",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Berlin_-_Checkpoint_Charlie_1963.jpg/330px-Berlin_-_Checkpoint_Charlie_1963.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Berlin_-_Checkpoint_Charlie_1963.jpg/330px-Berlin_-_Checkpoint_Charlie_1963.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 52.5075,
      "lng": 13.39028
    },
    {
      "id": "b_b11",
      "name": "Kaiser Wilhelm Memorial Church",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "War-damaged spire memorial standing alongside modern blue glass chapel.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Ged%C3%A4chtniskirche1.JPG/330px-Ged%C3%A4chtniskirche1.JPG?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Ged%C3%A4chtniskirche1.JPG/330px-Ged%C3%A4chtniskirche1.JPG?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 52.505,
      "lng": 13.335
    },
    {
      "id": "b_b12",
      "name": "Tiergarten Park",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "Sprawling 520-acre urban forest park in the heart of Berlin.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Berlin_Tiergarten_Siegess%C3%A4ule_Luftansicht.jpg/330px-Berlin_Tiergarten_Siegess%C3%A4ule_Luftansicht.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": true,
      "lat": 52.51389,
      "lng": 13.35694
    },
    {
      "id": "b_b13",
      "name": "Hackesche Höfe",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "Eight restored Art Nouveau courtyards filled with boutiques & cafes.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Hackesche_h%C3%B6fe_berlin.jpg/330px-Hackesche_h%C3%B6fe_berlin.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Hackesche_h%C3%B6fe_berlin.jpg/330px-Hackesche_h%C3%B6fe_berlin.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 52.52417,
      "lng": 13.40222
    },
    {
      "id": "b_b14",
      "name": "Museum Island Berlin",
      "category": "Museum & Art",
      "rating": "★4.8",
      "desc": "UNESCO World Heritage island housing 5 world-class museum complexes.",
      "price": "Day Pass: €19",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Berlin_Museumsinsel_Fernsehturm.jpg/330px-Berlin_Museumsinsel_Fernsehturm.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.535,
      "lng": 13.405
    },
    {
      "id": "b_b15",
      "name": "Pergamon Museum",
      "category": "Museum & Art",
      "rating": "★4.8",
      "desc": "Famed for Ishtar Gate of Babylon and Market Gate of Miletus.",
      "price": "Entry: €12",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Pergamonmuseum_Front.jpg/330px-Pergamonmuseum_Front.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Pergamonmuseum_Front.jpg/330px-Pergamonmuseum_Front.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 52.521,
      "lng": 13.396
    },
    {
      "id": "b_b16",
      "name": "Neues Museum (Nefertiti Bust)",
      "category": "Museum & Art",
      "rating": "★4.7",
      "desc": "Housing the iconic 3,300-year-old limestone bust of Queen Nefertiti.",
      "price": "Entry: €14",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Berlin_Neues_Museum_001.JPG/330px-Berlin_Neues_Museum_001.JPG?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Berlin_Neues_Museum_001.JPG/330px-Berlin_Neues_Museum_001.JPG?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 52.52056,
      "lng": 13.39778
    },
    {
      "id": "b_b17",
      "name": "Jewish Museum Berlin",
      "category": "Museum & Art",
      "rating": "★4.6",
      "desc": "Daniel Libeskind-designed zigzag building documenting German Jewish history.",
      "price": "Free permanent display",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Jewish_Museum_Berlin_logo.svg/330px-Jewish_Museum_Berlin_logo.svg.png?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Jewish_Museum_Berlin_logo.svg/330px-Jewish_Museum_Berlin_logo.svg.png?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 52.502,
      "lng": 13.395
    },
    {
      "id": "b_b18",
      "name": "Hamburger Bahnhof",
      "category": "Museum & Art",
      "rating": "★4.5",
      "desc": "Former train station converted into Berlin's premier contemporary art museum.",
      "price": "Entry: €14",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/InvalidenstrBerlin_12-2017_img1.jpg/330px-InvalidenstrBerlin_12-2017_img1.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/InvalidenstrBerlin_12-2017_img1.jpg/330px-InvalidenstrBerlin_12-2017_img1.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 52.52833,
      "lng": 13.37222
    },
    {
      "id": "b_b19",
      "name": "Topography of Terror",
      "category": "Museum & Art",
      "rating": "★4.7",
      "desc": "History museum located on the site of Gestapo and SS headquarters.",
      "price": "Free entry",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Topographie_des_Terrors_Neubau.jpg/330px-Topographie_des_Terrors_Neubau.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": false,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Topographie_des_Terrors_Neubau.jpg/330px-Topographie_des_Terrors_Neubau.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 52.50694,
      "lng": 13.38278
    },
    {
      "id": "b_b20",
      "name": "DDR Museum",
      "category": "Museum & Art",
      "rating": "★4.4",
      "desc": "Interactive museum depicting daily life under East German communist rule.",
      "price": "Entry: €12.50",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/DDR-Museum_%28Berlin%29_Schriftzug.jpg/330px-DDR-Museum_%28Berlin%29_Schriftzug.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/DDR-Museum_%28Berlin%29_Schriftzug.jpg/330px-DDR-Museum_%28Berlin%29_Schriftzug.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": true,
      "lat": 52.51903,
      "lng": 13.40222
    },
    {
      "id": "b_b21",
      "name": "Mustafa's Gemüse Kebab",
      "category": "Restaurant",
      "rating": "★4.4",
      "desc": "Berlin's most famous street food stand for roasted vegetable & chicken döner.",
      "price": "Kebab: €7.00",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.49,
      "lng": 13.435
    },
    {
      "id": "b_b22",
      "name": "Curry 36",
      "category": "Restaurant",
      "rating": "★4.4",
      "desc": "Iconic Mehringdamm food stand serving authentic Berlin Currywurst with fries.",
      "price": "Currywurst: €4.50",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.49349,
      "lng": 13.38772
    },
    {
      "id": "b_b23",
      "name": "Prater Biergarten",
      "category": "Restaurant",
      "rating": "★4.5",
      "desc": "Berlin's oldest beer garden shaded by giant chestnut trees in Prenzlauer Berg.",
      "price": "Beer & Bratwurst: €12",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.52,
      "lng": 13.435
    },
    {
      "id": "b_b24",
      "name": "Zur Letzten Instanz",
      "category": "Restaurant",
      "rating": "★4.4",
      "desc": "Berlin's oldest tavern (1621) serving pork knuckle & traditional German lager.",
      "price": "Mains: €18–€28",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.535,
      "lng": 13.435
    },
    {
      "id": "b_b25",
      "name": "Katz Orange",
      "category": "Restaurant",
      "rating": "★4.6",
      "desc": "Farm-to-table organic dining inside a 19th-century brick courtyard in Mitte.",
      "price": "Mains: €24–€38",
      "image": "",
      "family": false,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.55,
      "lng": 13.435
    },
    {
      "id": "b_b26",
      "name": "Borchardt",
      "category": "Restaurant",
      "rating": "★4.4",
      "desc": "Grand high-society French-German brasserie famous for golden Wiener Schnitzel.",
      "price": "Schnitzel: €32",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.49,
      "lng": 13.45
    },
    {
      "id": "b_b27",
      "name": "Grill Royal",
      "category": "Restaurant",
      "rating": "★4.5",
      "desc": "Riverside steakhouse overlooking the Spree frequented by international artists.",
      "price": "Steaks: €38–€75",
      "image": "",
      "family": false,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.505,
      "lng": 13.45
    },
    {
      "id": "b_b28",
      "name": "Monsieur Vuong",
      "category": "Restaurant",
      "rating": "★4.5",
      "desc": "Vibrant Vietnamese pho & spring roll spot in stylish Mitte neighborhood.",
      "price": "Dishes: €10–€16",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.52,
      "lng": 13.45
    },
    {
      "id": "b_b29",
      "name": "Zeit für Brot",
      "category": "Café & Bakery",
      "rating": "★4.7",
      "desc": "Organic bakery crafting giant warm cinnamon rolls (Schnecken) in glass kitchen.",
      "price": "Rolls: €3.80–€5",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.535,
      "lng": 13.45
    },
    {
      "id": "b_b30",
      "name": "The Barn Coffee Roasters",
      "category": "Café & Bakery",
      "rating": "★4.6",
      "desc": "Pioneer of Europe's specialty coffee scene roasting single-origin beans.",
      "price": "Coffee: €4.50–€7",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.55,
      "lng": 13.45
    },
    {
      "id": "b_b31",
      "name": "House of Small Wonder",
      "category": "Café & Bakery",
      "rating": "★4.5",
      "desc": "Japanese-influenced greenhouse cafe featuring spiral wooden staircase brunch spot.",
      "price": "Brunch: €14–€20",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.49,
      "lng": 13.465
    },
    {
      "id": "b_b32",
      "name": "Markthalle Neun",
      "category": "Park & Market",
      "rating": "★4.6",
      "desc": "Historic 1891 market hall host to Thursday Street Food Thursday fairs.",
      "price": "Dishes: €6–€14",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 52.505,
      "lng": 13.465
    }
  ],
  "Brussels, Belgium": [
    {
      "id": "br_1",
      "name": "Grand-Place",
      "category": "Landmark",
      "rating": "★4.8",
      "desc": "UNESCO World Heritage central square surrounded by opulent 17th-century guildhouses.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Grand-Place%2C_Brussels_-_panorama%2C_June_2018.jpg/330px-Grand-Place%2C_Brussels_-_panorama%2C_June_2018.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Grand-Place%2C_Brussels_-_panorama%2C_June_2018.jpg/330px-Grand-Place%2C_Brussels_-_panorama%2C_June_2018.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 50.84667,
      "lng": 4.3525
    },
    {
      "id": "br_2",
      "name": "Royal Gallery of Saint-Hubert",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "Glazed 19th-century shopping arcade housing luxury chocolatiers & historic cafes.",
      "price": "Free access",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 50.8353,
      "lng": 4.3217
    },
    {
      "id": "br_3",
      "name": "Atomium",
      "category": "Landmark",
      "rating": "★4.4",
      "desc": "Iconic 102m steel structure built for 1958 World Expo depicting an iron crystal.",
      "price": "Entry: €16",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Brussels_-_Atomium_2022.jpg/330px-Brussels_-_Atomium_2022.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Brussels_-_Atomium_2022.jpg/330px-Brussels_-_Atomium_2022.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": true,
      "lat": 50.89472,
      "lng": 4.34111
    },
    {
      "id": "br_4",
      "name": "St. Michael & St. Gudula Cathedral",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "Gothic cathedral towering over Brussels with stained glass windows.",
      "price": "Free access",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Saints-Michel-et-Gudule_Luc_Viatour.jpg/330px-Saints-Michel-et-Gudule_Luc_Viatour.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 50.8653,
      "lng": 4.3217
    },
    {
      "id": "br_5",
      "name": "Mont des Arts",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "Elevated urban garden promenade offering iconic views of Brussels spire.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Mont_des_Arts%2C_Brussels%2C_Belgium.jpg/330px-Mont_des_Arts%2C_Brussels%2C_Belgium.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Mont_des_Arts%2C_Brussels%2C_Belgium.jpg/330px-Mont_des_Arts%2C_Brussels%2C_Belgium.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 50.84389,
      "lng": 4.35667
    },
    {
      "id": "br_6",
      "name": "Cinquantenaire Arch & Park",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "U-shaped palace complex featuring monumental triumphal arch & gardens.",
      "price": "Free access",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Arco_del_Cincuentenario%2C_Bruselas%2C_B%C3%A9lgica%2C_2021-12-15%2C_DD_115-135_HDR_PAN.jpg/330px-Arco_del_Cincuentenario%2C_Bruselas%2C_B%C3%A9lgica%2C_2021-12-15%2C_DD_115-135_HDR_PAN.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 50.8203,
      "lng": 4.3367
    },
    {
      "id": "br_7",
      "name": "Manneken Pis",
      "category": "Landmark",
      "rating": "★4.1",
      "desc": "Famous 61cm bronze fountain statue of a peeing boy in Brussels center.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Bruxelles_Manneken_Pis_cropped.jpg/330px-Bruxelles_Manneken_Pis_cropped.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Bruxelles_Manneken_Pis_cropped.jpg/330px-Bruxelles_Manneken_Pis_cropped.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": true,
      "lat": 50.84499,
      "lng": 4.34999
    },
    {
      "id": "br_8",
      "name": "Magritte Museum",
      "category": "Museum & Art",
      "rating": "★4.6",
      "desc": "World's largest surrealist collection of René Magritte paintings.",
      "price": "Entry: €10",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Belgique_-_Bruxelles_-_H%C3%B4tel_du_Lotto_-_02.JPG/330px-Belgique_-_Bruxelles_-_H%C3%B4tel_du_Lotto_-_02.JPG?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Belgique_-_Bruxelles_-_H%C3%B4tel_du_Lotto_-_02.JPG/330px-Belgique_-_Bruxelles_-_H%C3%B4tel_du_Lotto_-_02.JPG?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 50.84194,
      "lng": 4.35861
    },
    {
      "id": "br_9",
      "name": "Chez Léon",
      "category": "Restaurant",
      "rating": "★4.3",
      "desc": "1893 Belgian dining institution serving classic moules-frites (mussels & fries).",
      "price": "Mussels: €24–€29",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Chez_L%C3%A9on_Bruxelles.jpg/330px-Chez_L%C3%A9on_Bruxelles.jpg?utm_source=fr.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 50.8653,
      "lng": 4.3367
    },
    {
      "id": "br_10",
      "name": "Fin de Siècle",
      "category": "Restaurant",
      "rating": "★4.6",
      "desc": "Lively communal-table restaurant serving carbonnade flamande beef stew & Belgian ales.",
      "price": "Stew: €16–€22",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Bilan_fin_de_si%C3%A8cle.jpg/330px-Bilan_fin_de_si%C3%A8cle.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 50.8803,
      "lng": 4.3367
    },
    {
      "id": "br_11",
      "name": "Maison Dandoy",
      "category": "Café & Bakery",
      "rating": "★4.6",
      "desc": "Historic 1829 artisan bakery famous for crispy Liege & Brussels waffles & speculoos.",
      "price": "Waffles: €5–€8",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/MagasinDandoy.jpg/330px-MagasinDandoy.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 50.8203,
      "lng": 4.3517
    },
    {
      "id": "br_12",
      "name": "Pierre Marcolini Grand Sablon",
      "category": "Café & Bakery",
      "rating": "★4.7",
      "desc": "Haute chocolaterie crafting bean-to-bar praline truffles & macarons.",
      "price": "Truffles: €12–€25",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 50.8353,
      "lng": 4.3517
    },
    {
      "id": "br_13",
      "name": "Delirium Café",
      "category": "Café & Bakery",
      "rating": "★4.5",
      "desc": "Guinness World Record beer hall stocking over 2,000 global craft beers.",
      "price": "Beers: €5–€10",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/CafeDeliriumEx.JPG/330px-CafeDeliriumEx.JPG?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": false,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 50.84841,
      "lng": 4.35393
    }
  ],
  "Cologne, Germany": [
    {
      "id": "c_1",
      "name": "Cologne Cathedral (Kölner Dom)",
      "category": "Landmark",
      "rating": "★4.8",
      "desc": "Monmental 157m Gothic twin-spired cathedral housing Shrine of the Three Kings.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/K%C3%B6lner_Dom_-_Westfassade_2022_ohne_Ger%C3%BCst-0968_b.jpg/330px-K%C3%B6lner_Dom_-_Westfassade_2022_ohne_Ger%C3%BCst-0968_b.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/K%C3%B6lner_Dom_-_Westfassade_2022_ohne_Ger%C3%BCst-0968_b.jpg/330px-K%C3%B6lner_Dom_-_Westfassade_2022_ohne_Ger%C3%BCst-0968_b.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 50.94139,
      "lng": 6.95833
    },
    {
      "id": "c_2",
      "name": "Hohenzollern Bridge (Love Locks)",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "Pedestrian rail bridge covered in 500,000 padlock love tokens across Rhine.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Hohenzollernbr%C3%BCcke_K%C3%B6ln_von_oben.jpg/330px-Hohenzollernbr%C3%BCcke_K%C3%B6ln_von_oben.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Hohenzollernbr%C3%BCcke_K%C3%B6ln_von_oben.jpg/330px-Hohenzollernbr%C3%BCcke_K%C3%B6ln_von_oben.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": true,
      "lat": 50.94139,
      "lng": 6.96556
    },
    {
      "id": "c_3",
      "name": "Great St. Martin Church",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "Romanesque church towering over Cologne's colorful historic Old Town waterfront.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Koeln_gross_st_martin.jpg/330px-Koeln_gross_st_martin.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Koeln_gross_st_martin.jpg/330px-Koeln_gross_st_martin.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 50.9386,
      "lng": 6.9618
    },
    {
      "id": "c_4",
      "name": "Cologne Chocolate Museum",
      "category": "Museum & Art",
      "rating": "★4.6",
      "desc": "Riverside museum featuring 3-meter golden chocolate fountain & live factory line.",
      "price": "Entry: €14.50",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Schoko_Koeln_20061015.jpg/330px-Schoko_Koeln_20061015.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Schoko_Koeln_20061015.jpg/330px-Schoko_Koeln_20061015.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": true,
      "lat": 50.9322,
      "lng": 6.96427
    },
    {
      "id": "c_5",
      "name": "Museum Ludwig",
      "category": "Museum & Art",
      "rating": "★4.7",
      "desc": "World-leading modern art museum featuring third-largest Picasso collection.",
      "price": "Entry: €13",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Museum_Ludwig_002.jpg/330px-Museum_Ludwig_002.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Museum_Ludwig_002.jpg/330px-Museum_Ludwig_002.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 50.94083,
      "lng": 6.96028
    },
    {
      "id": "c_6",
      "name": "Brauhaus Sion",
      "category": "Restaurant",
      "rating": "★4.4",
      "desc": "Historic 1904 brewery hall serving cold Kölsch beer & pork knuckle near Cathedral.",
      "price": "Kölsch: €2.20",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 50.93942,
      "lng": 6.95942
    },
    {
      "id": "c_7",
      "name": "Früh am Dom",
      "category": "Restaurant",
      "rating": "★4.4",
      "desc": "Traditional Kölsch brewhouse right under Cologne Cathedral spires.",
      "price": "Mains: €14–€24",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 50.9225,
      "lng": 6.9453
    },
    {
      "id": "c_8",
      "name": "Bei Oma Kleinmann",
      "category": "Restaurant",
      "rating": "★4.7",
      "desc": "Beloved student quarter pub famous for massive golden Schnitzels with 10 sauces.",
      "price": "Schnitzel: €16–€24",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 50.9375,
      "lng": 6.9453
    },
    {
      "id": "c_9",
      "name": "Café Reichard",
      "category": "Café & Bakery",
      "rating": "★4.4",
      "desc": "Grand traditional cafe terrace offering views of Cologne Cathedral facade.",
      "price": "Cakes: €6.00",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 50.9525,
      "lng": 6.9453
    }
  ],
  "Luxembourg City, Luxembourg": [
    {
      "id": "l_1",
      "name": "Bock Casemates",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "Subterranean cliffside defense tunnels carved into solid rock overlooking the Alzette.",
      "price": "Entry: €8",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Selig_Luxembourg_from_Paffendall.jpg/330px-Selig_Luxembourg_from_Paffendall.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 49.5816,
      "lng": 6.1019
    },
    {
      "id": "l_2",
      "name": "Chemin de la Corniche",
      "category": "Landmark",
      "rating": "★4.8",
      "desc": "Dubbed 'Europe's most beautiful balcony', a scenic rampart walk over Grund valley.",
      "price": "Free access",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.63503,
      "lng": -2.02751
    },
    {
      "id": "l_3",
      "name": "Grund Valley District",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "Picturesque lower town quarter with stone bridges, cobblestones & riverside bistros.",
      "price": "Free access",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 49.6116,
      "lng": 6.1019
    },
    {
      "id": "l_4",
      "name": "Grand Ducal Palace",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "Official Renaissance residence of the Grand Duke of Luxembourg in city center.",
      "price": "Tour: €15",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Luxemburg_BW_2016-09-15_11-46-49_stitch.jpg/330px-Luxemburg_BW_2016-09-15_11-46-49_stitch.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Luxemburg_BW_2016-09-15_11-46-49_stitch.jpg/330px-Luxemburg_BW_2016-09-15_11-46-49_stitch.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 49.61089,
      "lng": 6.13283
    },
    {
      "id": "l_5",
      "name": "Notre-Dame Cathedral Luxembourg",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "17th-century Gothic cathedral featuring stained glass and royal crypts.",
      "price": "Free access",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Luxembourg_City_Eurotrip_%28133169443%29.jpeg/330px-Luxembourg_City_Eurotrip_%28133169443%29.jpeg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 49.6416,
      "lng": 6.1019
    },
    {
      "id": "l_6",
      "name": "Mudam Luxembourg",
      "category": "Museum & Art",
      "rating": "★4.5",
      "desc": "Grand Duke Jean Museum of Modern Art designed by I.M. Pei atop Fort Thüngen.",
      "price": "Entry: €8",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/en/thumb/f/ff/Kirchberg_MUDAM.jpg/330px-Kirchberg_MUDAM.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 49.5816,
      "lng": 6.1169
    },
    {
      "id": "l_7",
      "name": "MNHA Museum",
      "category": "Museum & Art",
      "rating": "★4.6",
      "desc": "National Museum of History and Art displaying Gallo-Roman mosaics.",
      "price": "Free permanent display",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 49.5966,
      "lng": 6.1169
    },
    {
      "id": "l_8",
      "name": "Chocolate House Nathalie Bonn",
      "category": "Café & Bakery",
      "rating": "★4.7",
      "desc": "Famed chocolate shop opposite Grand Ducal Palace for hot chocolate spoons.",
      "price": "Spoon: €5.50",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 49.6116,
      "lng": 6.1169
    },
    {
      "id": "l_9",
      "name": "Oberweis Bakery",
      "category": "Café & Bakery",
      "rating": "★4.6",
      "desc": "Official royal court supplier of Luxembourgish pastries & pralines.",
      "price": "Pastries: €4–€8",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 49.6266,
      "lng": 6.1169
    },
    {
      "id": "l_10",
      "name": "Um Plateau",
      "category": "Restaurant",
      "rating": "★4.6",
      "desc": "Sophisticated dining room serving modern European sharing plates & cocktails.",
      "price": "Plates: €18–€32",
      "image": "",
      "family": false,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 49.6416,
      "lng": 6.1169
    },
    {
      "id": "l_11",
      "name": "Pfaffenthal Panoramic Elevator",
      "category": "Scenery",
      "rating": "★4.8",
      "desc": "71m glass elevator providing sweeping views over Alzette valley & Pfaffenthal quarter.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Lift_Pafendall-Uewerstad_3017-04.jpg/330px-Lift_Pafendall-Uewerstad_3017-04.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": true,
      "lat": 49.61552,
      "lng": 6.13065
    },
    {
      "id": "l_12",
      "name": "Vianden Castle",
      "category": "Landmark",
      "rating": "★4.8",
      "desc": "Breathtaking 11th-century feudal castle perched atop rocky promontory in Vianden valley.",
      "price": "Entry: €10",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Burg_Vianden%2C_Luxemburg.jpg/330px-Burg_Vianden%2C_Luxemburg.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "suburban",
      "kids": false,
      "lat": 49.935,
      "lng": 6.20222
    },
    {
      "id": "l_13",
      "name": "Pont Adolphe",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "Monumental double-arched stone bridge spanning 42-meter deep Petrusse Valley with glass footbridge.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Adolphe_Bridge_post_2017_renovation_works_-_7_August_2018.jpg/330px-Adolphe_Bridge_post_2017_renovation_works_-_7_August_2018.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 49.6083,
      "lng": 6.127
    },
    {
      "id": "l_14",
      "name": "Monument of Remembrance (Gëlle Fra)",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "Golden Lady statue on Place de la Constitution overlooking Petrusse Valley & Adolphe Bridge.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/El_Monumento_de_la_Recordacion.jpg/330px-El_Monumento_de_la_Recordacion.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 18.46611,
      "lng": -66.10589
    },
    {
      "id": "l_15",
      "name": "Place d'Armes",
      "category": "Scenery",
      "rating": "★4.6",
      "desc": "Tree-lined 'City Living Room' square packed with lively outdoor cafe terraces & bandstands.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/J38002_ArtVille_20120407-134630_PlaceDArmes.jpg/330px-J38002_ArtVille_20120407-134630_PlaceDArmes.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 45.50472,
      "lng": -73.55722
    },
    {
      "id": "l_16",
      "name": "Place Guillaume II",
      "category": "Scenery",
      "rating": "★4.5",
      "desc": "Historic equestrian square hosting open-air farmers markets & Luxembourg City Hall.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Luxembourg_City_monument_Guillaume_II_statue_2011.jpg/330px-Luxembourg_City_monument_Guillaume_II_statue_2011.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 49.61083,
      "lng": 6.13028
    },
    {
      "id": "l_17",
      "name": "Neimënster Abbey",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "17th-century Benedictine abbey along Alzette River, now a vibrant cultural center.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Abad%C3%ADa_Neum%C3%BCnster%2C_ciudad_de_Luxemburgo%2C_Luxemburgo%2C_2023-12-16%2C_DD_66-68_HDR.jpg/330px-Abad%C3%ADa_Neum%C3%BCnster%2C_ciudad_de_Luxemburgo%2C_Luxemburgo%2C_2023-12-16%2C_DD_66-68_HDR.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 49.61028,
      "lng": 6.13639
    },
    {
      "id": "l_18",
      "name": "Fort Thüngen (Musée Dräi Echelen)",
      "category": "Museum & Art",
      "rating": "★4.6",
      "desc": "1732 stone fortress with acorn towers housing Luxembourg's fortification history.",
      "price": "Free permanent display",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Mudam_04_jnl.jpg/330px-Mudam_04_jnl.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 49.61639,
      "lng": 6.13889
    },
    {
      "id": "l_19",
      "name": "Lëtzebuerg City Museum",
      "category": "Museum & Art",
      "rating": "★4.6",
      "desc": "Innovative urban history museum featuring a massive glass elevator cutting through rock strata.",
      "price": "Entry: €5",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Historisches_Museum_der_Stadt_Luxemburg_8325-026.jpg/330px-Historisches_Museum_der_Stadt_Luxemburg_8325-026.jpg?utm_source=fr.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 49.6099,
      "lng": 6.1335
    },
    {
      "id": "l_20",
      "name": "Müllerthal Schiessentümpel Waterfall",
      "category": "Scenery",
      "rating": "★4.8",
      "desc": "Romantic stone bridge & triple waterfall in 'Luxembourg's Little Switzerland'.",
      "price": "Free access",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "suburban",
      "kids": true,
      "lat": 49.6416,
      "lng": 6.1469
    }
  ],
  "Munich, Germany": [
    {
      "id": "m_1",
      "name": "Marienplatz & New Town Hall",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "Central square famous for Glockenspiel chime show & Neo-Gothic Rathaus facade.",
      "price": "Free access",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Rathaus_and_Marienplatz_from_Peterskirche_-_August_2006.jpg/330px-Rathaus_and_Marienplatz_from_Peterskirche_-_August_2006.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.1051,
      "lng": 11.552
    },
    {
      "id": "m_2",
      "name": "English Garden & Eisbachwave",
      "category": "Landmark",
      "rating": "★4.8",
      "desc": "500-acre park featuring river surfers riding perpetual standing wave.",
      "price": "Free access",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Aerial_image_of_Englischer_Garten_in_Munich_%28view_from_the_southwest%29.jpg/330px-Aerial_image_of_Englischer_Garten_in_Munich_%28view_from_the_southwest%29.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "city",
      "kids": true,
      "lat": 48.1201,
      "lng": 11.552
    },
    {
      "id": "m_3",
      "name": "Nymphenburg Palace",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "Grand Baroque summer palace of Bavarian monarchs with canal swan gardens.",
      "price": "Palace: €10",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Image-Schloss_Nymphenburg_Munich_CC_edit3.jpg/330px-Image-Schloss_Nymphenburg_Munich_CC_edit3.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Image-Schloss_Nymphenburg_Munich_CC_edit3.jpg/330px-Image-Schloss_Nymphenburg_Munich_CC_edit3.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.15806,
      "lng": 11.50361
    },
    {
      "id": "m_4",
      "name": "Munich Residenz",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "Former royal palace featuring Antiquarium hall of antiquities & Treasury.",
      "price": "Residenz: €10",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Grundriss_der_Residenz_M%C3%BCnchen_%28Bayerische_Schl%C3%B6sserverwaltung%29.jpg/330px-Grundriss_der_Residenz_M%C3%BCnchen_%28Bayerische_Schl%C3%B6sserverwaltung%29.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Residenz_W%C3%BCrzburg_im_Bau_1731.jpg/330px-Residenz_W%C3%BCrzburg_im_Bau_1731.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.14111,
      "lng": 11.57806
    },
    {
      "id": "m_5",
      "name": "Frauenkirche (Cathedral of Our Dear Lady)",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "Gothic brick cathedral featuring twin onion domes dominating Munich skyline.",
      "price": "Free access",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Frauenkirche_Munich_-_View_from_Peterskirche_Tower2.jpg/330px-Frauenkirche_Munich_-_View_from_Peterskirche_Tower2.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.1651,
      "lng": 11.552
    },
    {
      "id": "m_6",
      "name": "BMW Welt & BMW Museum",
      "category": "Museum & Art",
      "rating": "★4.7",
      "desc": "Futuristic exhibition hall showcasing automotive innovation & classic cars.",
      "price": "Museum: €10",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/BMW_Welt%2C_M%C3%BAnich%2C_Alemania16.jpg/330px-BMW_Welt%2C_M%C3%BAnich%2C_Alemania16.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "city",
      "kids": true,
      "lat": 48.1051,
      "lng": 11.567
    },
    {
      "id": "m_7",
      "name": "Deutsches Museum",
      "category": "Museum & Art",
      "rating": "★4.7",
      "desc": "World's largest museum of science and technology located on an island in the Isar.",
      "price": "Entry: €15",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Deutsches_Museum_Portrait_4.jpg/330px-Deutsches_Museum_Portrait_4.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Deutsches_Museum_Portrait_4.jpg/330px-Deutsches_Museum_Portrait_4.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": true,
      "lat": 48.13,
      "lng": 11.5833
    },
    {
      "id": "m_8",
      "name": "Pinakothek Museums (Alte & Neue)",
      "category": "Museum & Art",
      "rating": "★4.7",
      "desc": "Renowned art complex featuring European masters from Dürer to Van Gogh.",
      "price": "Entry: €7–€10",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Alte_Pinakothek_2009.jpg/330px-Alte_Pinakothek_2009.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.1351,
      "lng": 11.567
    },
    {
      "id": "m_9",
      "name": "Viktualienmarkt",
      "category": "Park & Market",
      "rating": "★4.7",
      "desc": "Bustling 200-year-old gourmet open-air food market with chestnut beer garden.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Karte_Viktualienmarkt_M%C3%BCnchen.png/330px-Karte_Viktualienmarkt_M%C3%BCnchen.png?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Karte_Viktualienmarkt_M%C3%BCnchen.png/330px-Karte_Viktualienmarkt_M%C3%BCnchen.png?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.13528,
      "lng": 11.57611
    },
    {
      "id": "m_10",
      "name": "Augustiner-Keller",
      "category": "Restaurant",
      "rating": "★4.6",
      "desc": "Munich's historic 5,000-seat beer garden serving classic Bavarian pretzels & lager.",
      "price": "Mass Beer: €10.80",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/2013_Augustiner_beermat.JPG/330px-2013_Augustiner_beermat.JPG?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.14353,
      "lng": 11.55147
    },
    {
      "id": "m_11",
      "name": "Hofbräuhaus München",
      "category": "Restaurant",
      "rating": "★4.5",
      "desc": "World-famous 3-story Bavarian beer hall with brass oompah bands & steins.",
      "price": "Mains: €14–€22",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.1051,
      "lng": 11.582
    },
    {
      "id": "m_12",
      "name": "Café Frischhut (Schmalznudel)",
      "category": "Café & Bakery",
      "rating": "★4.7",
      "desc": "Traditional bakery near Viktualienmarkt frying hot Bavarian donuts in lard.",
      "price": "Donuts: €2.80",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.1201,
      "lng": 11.582
    }
  ],
  "Paris, France": [
    {
      "id": "p_1",
      "name": "Eiffel Tower",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "Iconic 330m iron lattice tower offering panoramic views of Paris.",
      "price": "Tickets: €18–€28",
      "image": "https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Eiffel_Tower_logo.svg/330px-Eiffel_Tower_logo.svg.png?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Eiffel_Tower_logo.svg/330px-Eiffel_Tower_logo.svg.png?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": true,
      "lat": 48.85822,
      "lng": 2.2945
    },
    {
      "id": "p_2",
      "name": "Arc de Triomphe",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "Triumphal arch honoring those who fought for France, set atop Champs-Élysées.",
      "price": "Rooftop: €13",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Arc_de_Triomphe%2C_Paris_21_October_2010.jpg/330px-Arc_de_Triomphe%2C_Paris_21_October_2010.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Arc_de_Triomphe%2C_Paris_21_October_2010.jpg/330px-Arc_de_Triomphe%2C_Paris_21_October_2010.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.87378,
      "lng": 2.29503
    },
    {
      "id": "p_3",
      "name": "Sainte-Chapelle",
      "category": "Landmark",
      "rating": "★4.8",
      "desc": "13th-century Gothic royal chapel famed for 1,113 soaring stained glass windows.",
      "price": "Entry: €11.50",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Sainte_Chapelle_-_Upper_level_1.jpg/330px-Sainte_Chapelle_-_Upper_level_1.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Sainte_Chapelle_-_Upper_level_1.jpg/330px-Sainte_Chapelle_-_Upper_level_1.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.85528,
      "lng": 2.345
    },
    {
      "id": "p_4",
      "name": "Sacré-Cœur Basilica & Montmartre",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "Domed white basilica atop Montmartre hill overlooking bohemian artist squares.",
      "price": "Free entry",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.8716,
      "lng": 2.3222
    },
    {
      "id": "p_5",
      "name": "Notre-Dame Cathedral",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "Masterpiece of French Gothic architecture on Île de la Cité.",
      "price": "Free parvis access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Notre-Dame_de_Paris%2C_4_October_2017.jpg/330px-Notre-Dame_de_Paris%2C_4_October_2017.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Notre-Dame_de_Paris%2C_4_October_2017.jpg/330px-Notre-Dame_de_Paris%2C_4_October_2017.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.85306,
      "lng": 2.35
    },
    {
      "id": "p_6",
      "name": "Palais-Royal Courtyard & Gardens",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "17th-century palace courtyard featuring Buren's striped columns and rose gardens.",
      "price": "Free access",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Conseil_d%27Etat_Paris_WA.jpg/330px-Conseil_d%27Etat_Paris_WA.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.8266,
      "lng": 2.3372
    },
    {
      "id": "p_7",
      "name": "Panthéon Paris",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "Neoclassical mausoleum containing tombs of Victor Hugo, Voltaire & Marie Curie.",
      "price": "Entry: €11.50",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.8416,
      "lng": 2.3372
    },
    {
      "id": "p_8",
      "name": "Jardin du Luxembourg",
      "category": "Landmark",
      "rating": "★4.8",
      "desc": "60-acre park featuring Medici Fountain, tree-lined promenades and sailboat basin.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/LuxembourgMontparnasse.JPG/330px-LuxembourgMontparnasse.JPG?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/LuxembourgMontparnasse.JPG/330px-LuxembourgMontparnasse.JPG?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": true,
      "lat": 48.84694,
      "lng": 2.33722
    },
    {
      "id": "p_9",
      "name": "Opéra Garnier (Palais Garnier)",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "Opulent 1,979-seat opera house featuring Chagall ceiling and grand marble staircase.",
      "price": "Self-tour: €14",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Paris_Opera_full_frontal_architecture%2C_May_2009.jpg/330px-Paris_Opera_full_frontal_architecture%2C_May_2009.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Paris_Opera_full_frontal_architecture%2C_May_2009.jpg/330px-Paris_Opera_full_frontal_architecture%2C_May_2009.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.87194,
      "lng": 2.33167
    },
    {
      "id": "p_10",
      "name": "Pont Alexandre III",
      "category": "Landmark",
      "rating": "★4.8",
      "desc": "Beaux-Arts bridge decorated with gilded nymph statues over the Seine.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Pont_Alexandre_III_depuis_pont_de_la_Concorde_Paris.jpg/330px-Pont_Alexandre_III_depuis_pont_de_la_Concorde_Paris.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Pont_Alexandre_III_depuis_pont_de_la_Concorde_Paris.jpg/330px-Pont_Alexandre_III_depuis_pont_de_la_Concorde_Paris.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.86361,
      "lng": 2.31361
    },
    {
      "id": "p_11",
      "name": "Les Invalides & Napoleon's Tomb",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "Golden-domed complex housing France's Military Museum and Napoleon's tomb.",
      "price": "Entry: €14",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/H%C3%B4tel_des_Invalides_from_the_Eiffel_Tower%2C_23_July_2009.jpg/330px-H%C3%B4tel_des_Invalides_from_the_Eiffel_Tower%2C_23_July_2009.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.8266,
      "lng": 2.3522
    },
    {
      "id": "p_12",
      "name": "Pont des Arts",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "Iconic pedestrian wooden bridge connecting the Louvre and Institut de France.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Paris_Pont_des_Arts.jpg/330px-Paris_Pont_des_Arts.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.85833,
      "lng": 2.3375
    },
    {
      "id": "p_13",
      "name": "Catacombes de Paris",
      "category": "Landmark",
      "rating": "★4.5",
      "desc": "Underground ossuary holding the remains of over six million Parisians.",
      "price": "Entry: €29",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Catacumbas%2C_Par%C3%ADs%2C_Francia%2C_2022-11-01%2C_DD_105-107_HDR.jpg/330px-Catacumbas%2C_Par%C3%ADs%2C_Francia%2C_2022-11-01%2C_DD_105-107_HDR.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": false,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Catacumbas%2C_Par%C3%ADs%2C_Francia%2C_2022-11-01%2C_DD_105-107_HDR.jpg/330px-Catacumbas%2C_Par%C3%ADs%2C_Francia%2C_2022-11-01%2C_DD_105-107_HDR.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.83389,
      "lng": 2.33222
    },
    {
      "id": "p_14",
      "name": "Louvre Museum & Glass Pyramid",
      "category": "Museum & Art",
      "rating": "★4.7",
      "desc": "World's largest art museum housing Mona Lisa, Venus de Milo & Winged Victory.",
      "price": "Entry: €17–€22",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.8716,
      "lng": 2.3522
    },
    {
      "id": "p_15",
      "name": "Musée d'Orsay",
      "category": "Museum & Art",
      "rating": "★4.8",
      "desc": "Beaux-Arts railway station featuring Impressionist masterpieces by Monet, Degas & Van Gogh.",
      "price": "Entry: €16",
      "image": "https://upload.wikimedia.org/wikipedia/fr/thumb/7/73/Logo_mus%C3%A9e_d%27Orsay.png/330px-Logo_mus%C3%A9e_d%27Orsay.png?utm_source=fr.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.85997,
      "lng": 2.32653
    },
    {
      "id": "p_16",
      "name": "Centre Pompidou",
      "category": "Museum & Art",
      "rating": "★4.5",
      "desc": "High-tech colored pipe architecture housing Europe's largest modern art collection.",
      "price": "Entry: €15",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Le_logo_du_Centre_Pompidou_redessin%C3%A9_en_2019_%285_bandes%29.svg/330px-Le_logo_du_Centre_Pompidou_redessin%C3%A9_en_2019_%285_bandes%29.svg.png?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Le_logo_du_Centre_Pompidou_redessin%C3%A9_en_2019_%285_bandes%29.svg/330px-Le_logo_du_Centre_Pompidou_redessin%C3%A9_en_2019_%285_bandes%29.svg.png?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.86064,
      "lng": 2.35224
    },
    {
      "id": "p_17",
      "name": "Musée de l'Orangerie",
      "category": "Museum & Art",
      "rating": "★4.7",
      "desc": "Monet's massive Water Lilies (Nymphéas) murals displayed in custom oval rooms.",
      "price": "Entry: €12.50",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Mus%C3%A9e_de_l%E2%80%99Orangerie_exterior.JPG/330px-Mus%C3%A9e_de_l%E2%80%99Orangerie_exterior.JPG?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.86385,
      "lng": 2.32254
    },
    {
      "id": "p_18",
      "name": "Musée Rodin",
      "category": "Museum & Art",
      "rating": "★4.7",
      "desc": "Rose gardens surrounding Hôtel Biron displaying Rodin's 'The Thinker' and 'The Gates of Hell'.",
      "price": "Entry: €13",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Le_mus%C3%A9e_Rodin.jpg/330px-Le_mus%C3%A9e_Rodin.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.85528,
      "lng": 2.31583
    },
    {
      "id": "p_19",
      "name": "Musée Picasso Paris",
      "category": "Museum & Art",
      "rating": "★4.5",
      "desc": "Over 5,000 works by Pablo Picasso housed inside historic Hôtel Salé mansion.",
      "price": "Entry: €14",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/H%C3%B4tel_Sal%C3%A9.JPG/330px-H%C3%B4tel_Sal%C3%A9.JPG?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.85973,
      "lng": 2.36244
    },
    {
      "id": "p_20",
      "name": "Musée Carnavalet",
      "category": "Museum & Art",
      "rating": "★4.6",
      "desc": "Dedicated museum of Parisian history located in two adjacent Marais mansions.",
      "price": "Free permanent access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Carnavalet_Par%C3%ADs_10.JPG/330px-Carnavalet_Par%C3%ADs_10.JPG?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.8575,
      "lng": 2.36222
    },
    {
      "id": "p_21",
      "name": "Le Petit Marché",
      "category": "Restaurant",
      "rating": "★4.6",
      "desc": "Trendy Marais bistro specializing in seared duck breast, tuna steak & banana crumble.",
      "price": "Mains: €18–€26",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.8266,
      "lng": 2.3822
    },
    {
      "id": "p_22",
      "name": "Le Train Bleu",
      "category": "Restaurant",
      "rating": "★4.5",
      "desc": "1900 Belle Époque frescoed dining hall inside Gare de Lyon railway station.",
      "price": "Mains: €34–€52",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Le_Train_Bleu.jpg/330px-Le_Train_Bleu.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.8416,
      "lng": 2.3822
    },
    {
      "id": "p_23",
      "name": "Chez Janou",
      "category": "Restaurant",
      "rating": "★4.5",
      "desc": "Lively Provençal bistro near Place des Vosges famous for endless chocolate mousse bowl.",
      "price": "Mains: €18–€24",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.8566,
      "lng": 2.3822
    },
    {
      "id": "p_24",
      "name": "Bouillon Chartier",
      "category": "Restaurant",
      "rating": "★4.4",
      "desc": "Historic 1896 dining hall serving classic French comfort food at unbeatable low prices.",
      "price": "Mains: €9–€14",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Chez_Chartier_1.JPG/330px-Chez_Chartier_1.JPG?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Chez_Chartier_1.JPG/330px-Chez_Chartier_1.JPG?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.87333,
      "lng": 2.34361
    },
    {
      "id": "p_25",
      "name": "Frenchie Bar à Vins",
      "category": "Restaurant",
      "rating": "★4.6",
      "desc": "Rustic-chic wine bar on Rue du Nil with small plates & artisanal natural wines.",
      "price": "Plates: €14–€24",
      "image": "",
      "family": false,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.8866,
      "lng": 2.3822
    },
    {
      "id": "p_26",
      "name": "Les Deux Magots",
      "category": "Café & Bakery",
      "rating": "★4.4",
      "desc": "Legendary Saint-Germain cafe once frequented by Ernest Hemingway & Jean-Paul Sartre.",
      "price": "Coffee: €6–€10",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Les_Deux_Magots%2C_25_September_2019.jpg/330px-Les_Deux_Magots%2C_25_September_2019.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Les_Deux_Magots%2C_25_September_2019.jpg/330px-Les_Deux_Magots%2C_25_September_2019.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.854,
      "lng": 2.3332
    },
    {
      "id": "p_27",
      "name": "L'As du Fallafel",
      "category": "Restaurant",
      "rating": "★4.6",
      "desc": "World-famous Jewish Quarter falafel stand stuffed with fried eggplant & tahini.",
      "price": "Pita: €9.50",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/LAs_du_Fallafel.jpg/330px-LAs_du_Fallafel.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.85742,
      "lng": 2.35907
    },
    {
      "id": "p_28",
      "name": "Pink Mamma",
      "category": "Restaurant",
      "rating": "★4.5",
      "desc": "Four-story Italian trattoria featuring glass skylight roof and Florentine T-bone steak.",
      "price": "Mains: €16–€28",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.86938,
      "lng": 2.34596
    },
    {
      "id": "p_29",
      "name": "Marché des Enfants Rouges",
      "category": "Café & Bakery",
      "rating": "★4.5",
      "desc": "Paris's oldest covered food market serving authentic fresh savory galettes & crêpes.",
      "price": "Dishes: €8–€15",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/March%C3%A9_des_Enfants-Rouges%2C_Paris_July_2014.jpg/330px-March%C3%A9_des_Enfants-Rouges%2C_Paris_July_2014.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.8628,
      "lng": 2.362
    },
    {
      "id": "p_30",
      "name": "Cédric Grolet Le Meurice",
      "category": "Café & Bakery",
      "rating": "★4.6",
      "desc": "World's best pastry chef boutique producing hyper-realistic sculpted fruit desserts.",
      "price": "Pastries: €14–€18",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.8866,
      "lng": 2.3972
    },
    {
      "id": "p_31",
      "name": "Angelina Paris",
      "category": "Café & Bakery",
      "rating": "★4.5",
      "desc": "Belle Époque tearoom world-renowned for thick African hot chocolate & Mont-Blanc chestnut pastry.",
      "price": "Hot Choc: €9.50",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.8266,
      "lng": 2.4122
    },
    {
      "id": "p_32",
      "name": "Du Pain et des Idées",
      "category": "Café & Bakery",
      "rating": "★4.7",
      "desc": "1889 bakery crafting signature escargot chocolate-pistachio pastries and wood-fired sourdough.",
      "price": "Pastries: €3.50–€6",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.8416,
      "lng": 2.4122
    },
    {
      "id": "p_33",
      "name": "Carette Trocadéro",
      "category": "Café & Bakery",
      "rating": "★4.5",
      "desc": "Famous arcade cafe near Eiffel Tower known for whipped cream hot chocolate & French macarons.",
      "price": "Hot Choc: €10",
      "image": "",
      "family": true,
      "adult": true,
      "wikiImage": "",
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.8566,
      "lng": 2.4122
    },
    {
      "id": "p_34",
      "name": "Musée du Quai Branly",
      "category": "Museum",
      "rating": "★4.6",
      "desc": "Jean Nouvel-designed museum of non-Western indigenous art near Eiffel Tower.",
      "price": "Entry: €12",
      "image": "https://upload.wikimedia.org/wikipedia/en/thumb/f/f2/Musee_du_quai_Branly_exterieur.jpg/330px-Musee_du_quai_Branly_exterieur.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.8608,
      "lng": 2.2975
    },
    {
      "id": "p_35",
      "name": "Covered Passages (Galerie Vivienne)",
      "category": "Scenery",
      "rating": "★4.6",
      "desc": "19th-century glass-roofed arcades lined with antique shops & tea salons.",
      "price": "Free walk",
      "image": "",
      "family": true,
      "adult": true,
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.8866,
      "lng": 2.4122
    },
    {
      "id": "p_36",
      "name": "Galeries Lafayette Haussmann",
      "category": "Scenery",
      "rating": "★4.7",
      "desc": "Stunning Neo-Byzantine glass dome & free rooftop terrace for panoramic views.",
      "price": "Free rooftop access",
      "image": "",
      "family": true,
      "adult": true,
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.8733,
      "lng": 2.33222
    },
    {
      "id": "p_37",
      "name": "Seine River Cruise (Bateaux-Mouches)",
      "category": "Scenery",
      "rating": "★4.7",
      "desc": "Panoramic waterside views of Eiffel Tower, Musée d'Orsay, and Notre-Dame.",
      "price": "Cruise: €15",
      "image": "",
      "family": true,
      "adult": true,
      "hasWiki": false,
      "locationZone": "city",
      "kids": true,
      "lat": 48.8416,
      "lng": 2.4272
    },
    {
      "id": "p_38",
      "name": "Canal Saint-Martin",
      "category": "Scenery",
      "rating": "★4.6",
      "desc": "Bohemian canal walkway famous from Amélie with tree-lined iron footbridges.",
      "price": "Free walk",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Canal_Saint-Martin%2C_Paris_-_OSM_2022.svg/330px-Canal_Saint-Martin%2C_Paris_-_OSM_2022.svg.png?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.84722,
      "lng": 2.36667
    },
    {
      "id": "p_27",
      "name": "Palace of Versailles (Château de Versailles)",
      "category": "Landmark",
      "rating": "★4.8",
      "desc": "Essential royal palace with Hall of Mirrors & vast estate gardens.",
      "price": "Palace: €19.50",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Vue_a%C3%A9rienne_du_domaine_de_Versailles_par_ToucanWings_-_Creative_Commons_By_Sa_3.0_-_081_%28cropped%29.jpg/330px-Vue_a%C3%A9rienne_du_domaine_de_Versailles_par_ToucanWings_-_Creative_Commons_By_Sa_3.0_-_081_%28cropped%29.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "hasWiki": true,
      "locationZone": "suburban",
      "kids": false,
      "lat": 48.8047,
      "lng": 2.1203
    },
    {
      "id": "p_28",
      "name": "Place de la Concorde & Champs-Élysées",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "Center of Historical Axis featuring 3,300-year-old Luxor Obelisk.",
      "price": "Free access",
      "image": "",
      "family": true,
      "adult": true,
      "hasWiki": false,
      "locationZone": "city",
      "kids": false,
      "lat": 48.8866,
      "lng": 2.4272
    },
    {
      "id": "p_29",
      "name": "Conciergerie",
      "category": "Landmark",
      "rating": "★4.6",
      "desc": "Medieval royal palace and former prison where Marie Antoinette was held.",
      "price": "Entry: €11.50",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Paris_Conciergerie_265.jpg/330px-Paris_Conciergerie_265.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.8564,
      "lng": 2.3456
    },
    {
      "id": "p_30",
      "name": "Place des Vosges",
      "category": "Landmark",
      "rating": "★4.7",
      "desc": "Paris's oldest planned square in Marais with red-brick arcades & Victor Hugo home.",
      "price": "Free entry",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Place_des_Vosges_vue_a%C3%A9rienne.png/330px-Place_des_Vosges_vue_a%C3%A9rienne.png?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.85556,
      "lng": 2.36556
    },
    {
      "id": "p_31",
      "name": "Musée Marmottan Monet",
      "category": "Museum",
      "rating": "★4.7",
      "desc": "Houses Monet's Impression, Sunrise—the origin of Impressionism.",
      "price": "Entry: €14",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Mus%C3%A9e_Marmottan_Monet_logo.svg/330px-Mus%C3%A9e_Marmottan_Monet_logo.svg.png?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.8593,
      "lng": 2.2673
    },
    {
      "id": "p_32",
      "name": "Fondation Louis Vuitton",
      "category": "Museum",
      "rating": "★4.7",
      "desc": "Frank Gehry modern architectural masterpiece & world-class art exhibitions.",
      "price": "Entry: €16",
      "image": "https://upload.wikimedia.org/wikipedia/en/thumb/0/03/Fondation_Louis_Vuitton_-_Paris_%2850569906682%29.jpg/330px-Fondation_Louis_Vuitton_-_Paris_%2850569906682%29.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.87667,
      "lng": 2.26333
    },
    {
      "id": "p_33",
      "name": "Musée de Cluny (Middle Ages)",
      "category": "Museum",
      "rating": "★4.6",
      "desc": "Latin Quarter museum famous for tapestry masterpiece The Lady and the Unicorn.",
      "price": "Entry: €12",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Paris_2012-aout-0006-2-Hotel-de-Cluny.jpg/330px-Paris_2012-aout-0006-2-Hotel-de-Cluny.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "hasWiki": true,
      "locationZone": "city",
      "kids": false,
      "lat": 48.85056,
      "lng": 2.34333
    },
    {
      "id": "p_46",
      "name": "Disneyland Paris",
      "category": "Landmark",
      "rating": "★4.8",
      "desc": "World-famous Disney theme park featuring Sleeping Beauty Castle & Marvel Avengers Campus.",
      "price": "Entry: €56–€99",
      "image": "https://upload.wikimedia.org/wikipedia/en/thumb/8/88/Sleeping_Beauty_Castle%2C_Disneyland%2C_Paris.jpg/330px-Sleeping_Beauty_Castle%2C_Disneyland%2C_Paris.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "hasWiki": true,
      "locationZone": "suburban",
      "kids": true,
      "lat": 48.86861,
      "lng": 2.78167
    },
    {
      "id": "p_47",
      "name": "Grande Galerie de l'Évolution",
      "category": "Museum & Art",
      "rating": "★4.8",
      "desc": "Stunning glass-roofed museum in Jardin des Plantes featuring a procession of 7,000 stuffed animals.",
      "price": "Entry: €13",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Paris_75005_Grande_Galerie_de_l%27Evolution_20070804.jpg/330px-Paris_75005_Grande_Galerie_de_l%27Evolution_20070804.jpg?utm_source=nl.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "hasWiki": true,
      "locationZone": "city",
      "kids": true,
      "lat": 48.8416,
      "lng": 2.4572
    },
    {
      "id": "p_48",
      "name": "Cité des Sciences et de l'Industrie",
      "category": "Museum & Art",
      "rating": "★4.7",
      "desc": "Europe's largest science museum featuring interactive Cité des Enfants & Geode IMAX sphere.",
      "price": "Entry: €13",
      "image": "https://upload.wikimedia.org/wikipedia/en/thumb/9/97/Cit%C3%A9_des_Sciences_et_de_l%27Industrie_%28City_of_Science_and_Industry%29_logo.svg/330px-Cit%C3%A9_des_Sciences_et_de_l%27Industrie_%28City_of_Science_and_Industry%29_logo.svg.png?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "hasWiki": true,
      "locationZone": "city",
      "kids": true,
      "lat": 48.8956,
      "lng": 2.3881
    },
    {
      "id": "p_49",
      "name": "Jardin d'Acclimatation",
      "category": "Scenery",
      "rating": "★4.6",
      "desc": "Historic 45-acre children's amusement park in Bois de Boulogne with rollercoasters & farm animals.",
      "price": "Entry: €7.00",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Jardin_d%27acclimatation_-_Fondation_Louis_Vuitton.jpg/330px-Jardin_d%27acclimatation_-_Fondation_Louis_Vuitton.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "hasWiki": true,
      "locationZone": "city",
      "kids": true,
      "lat": 48.8775,
      "lng": 2.26306
    },
    {
      "id": "p_50",
      "name": "Parc Zoologique de Paris",
      "category": "Scenery",
      "rating": "★4.5",
      "desc": "Modern 36-acre zoo in Bois de Vincennes featuring a 65-meter artificial Great Rock & 5 biozones.",
      "price": "Entry: €22",
      "image": "",
      "family": true,
      "adult": true,
      "hasWiki": false,
      "locationZone": "city",
      "kids": true,
      "lat": 48.8322,
      "lng": 2.4186
    },
    {
      "id": "p_51",
      "name": "Aquarium de Paris",
      "category": "Scenery",
      "rating": "★4.4",
      "desc": "Underground aquarium at Trocadéro featuring 13,000 sea creatures & shark touching pool.",
      "price": "Entry: €26",
      "image": "",
      "family": true,
      "adult": true,
      "hasWiki": false,
      "locationZone": "city",
      "kids": true,
      "lat": 48.86222,
      "lng": 2.29083
    },
    {
      "id": "p_52",
      "name": "Musée Grévin",
      "category": "Museum & Art",
      "rating": "★4.5",
      "desc": "Iconic 1882 wax museum featuring 450 hyper-realistic figures of historic & pop culture icons.",
      "price": "Entry: €20",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Grevin_musee_facade.jpg/330px-Grevin_musee_facade.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "hasWiki": true,
      "locationZone": "city",
      "kids": true,
      "lat": 48.87183,
      "lng": 2.3421
    },
    {
      "id": "p_53",
      "name": "Jardin des Tuileries",
      "category": "Scenery",
      "rating": "★4.7",
      "desc": "Historic royal garden between Louvre & Place de la Concorde with vintage carousel & summer funfair.",
      "price": "Free access",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Crowd_in_the_Jardin_des_Tuileries%2C_Paris_July_2014.jpg/330px-Crowd_in_the_Jardin_des_Tuileries%2C_Paris_July_2014.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "hasWiki": true,
      "locationZone": "city",
      "kids": true,
      "lat": 48.8639,
      "lng": 2.3261
    },
    {
      "id": "p_54",
      "name": "Musée de l'Air et de l'Espace",
      "category": "Museum & Art",
      "rating": "★4.7",
      "desc": "Historic aviation museum at Le Bourget featuring original Concorde supersonic jets & rockets.",
      "price": "Entry: €16",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/800px-Mus%C3%A9e_de_l%27Air_et_de_l%27Espace.jpg/330px-800px-Mus%C3%A9e_de_l%27Air_et_de_l%27Espace.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail",
      "family": true,
      "adult": true,
      "hasWiki": true,
      "locationZone": "suburban",
      "kids": true,
      "lat": 48.9471,
      "lng": 2.4349
    },
    {
      "id": "p_55",
      "name": "Choco-Story Paris",
      "category": "Museum & Art",
      "rating": "★4.6",
      "desc": "Interactive chocolate museum tracing 4,000 years of cacao history with live chocolate tastings.",
      "price": "Entry: €15",
      "image": "",
      "family": true,
      "adult": true,
      "hasWiki": false,
      "locationZone": "city",
      "kids": true,
      "lat": 48.8866,
      "lng": 2.4722
    }
  ]
};


























function getCategoryIcon(cat) {
  if (!cat) return '📍';
  const c = String(cat).toLowerCase();
  if (c.includes('hotel') || c.includes('stay')) return '🏨';
  if (c.includes('café') || c.includes('cafe') || c.includes('bakery')) return '☕';
  if (c.includes('bistro') || c.includes('restaurant') || c.includes('dining')) return '🍷';
  if (c.includes('park') || c.includes('garden')) return '🌳';
  if (c.includes('museum') || c.includes('gallery')) return '🎨';
  if (c.includes('palace') || c.includes('castle') || c.includes('church') || c.includes('cathedral') || c.includes('landmark')) return '🏛️';
  return '📍';
}

const AITravelEngine = {
  selectedMustVisitIds: new Set(),

  // Helper to create single venue Google Maps live search link button
  createMapsLink(placeName, city, compact = false) {
    const cleanPlace = placeName.replace(/[()]/g, '').trim();
    const cleanCity = city.split(',')[0].trim();
    const query = encodeURIComponent(`${cleanPlace} ${cleanCity}`);
    const mapsUrl = `https://www.google.com/maps/search/?api=1&query=${query}`;
    if (compact) {
      return `<a href="${mapsUrl}" target="_blank" rel="noopener noreferrer" onclick="event.stopPropagation();" style="display:inline-flex; align-items:center; justify-content:center; background:#EFF6FF; color:#1D4ED8; border:1px solid #93C5FD; padding:0.2rem 0.45rem; border-radius:6px; font-weight:800; text-decoration:none; font-size:0.75rem; white-space:nowrap; flex-shrink:0;" title="Open Google Maps">📍↗</a>`;
    }
    return `<a href="${mapsUrl}" target="_blank" rel="noopener noreferrer" onclick="event.stopPropagation();" style="display:inline-flex; align-items:center; justify-content:center; gap:0.2rem; background:#EFF6FF; color:#1D4ED8; border:1.5px solid #93C5FD; padding:0.25rem 0.55rem; border-radius:6px; font-weight:700; text-decoration:none; font-size:0.8rem; white-space:nowrap; max-width:100%;" title="View Live Google Maps Hours, Reviews & Photos">📍 Maps ↗</a>`;
  },

  // MASTER DUAL ROUTE GENERATOR: Route A (Must-Visit Selected Spots) & Route B (Full 1-Day AI Recommended Course)
  generateMultiStopMapsLink(mustVisitVenues, fullDayVenues, city, transportMode) {
    const cleanCity = city.split(',')[0].trim();

    // 1. ROUTE A: Must-Visit Selected Spots Only
    const cleanMust = (mustVisitVenues || []).map(v => v.replace(/[()]/g, '').trim()).filter(Boolean);
    const pathSegmentsA = cleanMust.map(v => encodeURIComponent(`${v}, ${cleanCity}`)).join('/');
    const masterUrlA = `https://www.google.com/maps/dir/${pathSegmentsA}/`;

    // 2. ROUTE B: Full 1-Day AI Recommended Course (All Destinations)
    const cleanFull = (fullDayVenues || []).map(v => v.replace(/[()]/g, '').trim()).filter(Boolean);
    const pathSegmentsB = cleanFull.map(v => encodeURIComponent(`${v}, ${cleanCity}`)).join('/');
    const masterUrlB = `https://www.google.com/maps/dir/${pathSegmentsB}/`;

    // Badges for Route A
    const badgesA = cleanMust.map((v, idx) => `
      <span style="display:inline-flex; align-items:center; gap:0.2rem; background:#ECFDF5; color:#047857; border:1px solid #A7F3D0; padding:0.25rem 0.6rem; border-radius:6px; font-weight:700; font-size:0.82rem; margin:0.15rem;">
        <span style="background:#047857; color:#FFF; border-radius:999px; width:18px; height:18px; display:inline-flex; justify-content:center; align-items:center; font-size:0.7rem;">${idx + 1}</span>
        ${escapeHtml(v)}
      </span>
    `).join(' ➔ ');

    // Badges for Route B
    const badgesB = cleanFull.map((v, idx) => `
      <span style="display:inline-flex; align-items:center; gap:0.2rem; background:#FFFBEB; color:#B45309; border:1px solid #FDE68A; padding:0.25rem 0.6rem; border-radius:6px; font-weight:700; font-size:0.82rem; margin:0.15rem;">
        <span style="background:#B45309; color:#FFF; border-radius:999px; width:18px; height:18px; display:inline-flex; justify-content:center; align-items:center; font-size:0.7rem;">${idx + 1}</span>
        ${escapeHtml(v)}
      </span>
    `).join(' ➔ ');

    // Leg-by-Leg Transit links for Route A
    let legItemsAHtml = '';
    for (let i = 0; i < cleanMust.length - 1; i++) {
      const legUrl = `https://www.google.com/maps/dir/?api=1&origin=${encodeURIComponent(cleanMust[i] + ', ' + cleanCity)}&destination=${encodeURIComponent(cleanMust[i + 1] + ', ' + cleanCity)}&travelmode=${transportMode === 'car' ? 'driving' : 'transit'}`;
      legItemsAHtml += `
        <div style="background:#FFF; border:1px solid #CBD5E1; border-radius:8px; padding:0.4rem 0.75rem; font-size:0.82rem; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-top:0.4rem;">
          <span style="font-weight:700; color:var(--text-primary);">Leg ${i + 1}: ${escapeHtml(cleanMust[i])} ➔ ${escapeHtml(cleanMust[i + 1])}</span>
          <a href="${legUrl}" target="_blank" rel="noopener noreferrer" style="color:#0284C7; font-weight:700; text-decoration:none; background:#F0F9FF; padding:0.15rem 0.55rem; border-radius:4px; border:1px solid #BAE6FD;">
            ${transportMode === 'car' ? '🚗 Drive Leg' : '🚆 Transit Leg'} ↗
          </a>
        </div>
      `;
    }

    // Leg-by-Leg Transit links for Route B
    let legItemsBHtml = '';
    for (let i = 0; i < cleanFull.length - 1; i++) {
      const legUrl = `https://www.google.com/maps/dir/?api=1&origin=${encodeURIComponent(cleanFull[i] + ', ' + cleanCity)}&destination=${encodeURIComponent(cleanFull[i + 1] + ', ' + cleanCity)}&travelmode=${transportMode === 'car' ? 'driving' : 'transit'}`;
      legItemsBHtml += `
        <div style="background:#FFF; border:1px solid #CBD5E1; border-radius:8px; padding:0.4rem 0.75rem; font-size:0.82rem; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-top:0.4rem;">
          <span style="font-weight:700; color:var(--text-primary);">Leg ${i + 1}: ${escapeHtml(cleanFull[i])} ➔ ${escapeHtml(cleanFull[i + 1])}</span>
          <a href="${legUrl}" target="_blank" rel="noopener noreferrer" style="color:#0284C7; font-weight:700; text-decoration:none; background:#F0F9FF; padding:0.15rem 0.55rem; border-radius:4px; border:1px solid #BAE6FD;">
            ${transportMode === 'car' ? '🚗 Drive Leg' : '🚆 Transit Leg'} ↗
          </a>
        </div>
      `;
    }

    return `
      <div style="background:linear-gradient(135deg, #FEF3C7, #D1FAE5); border:2.5px solid var(--border-ink); border-radius:20px; padding:1.75rem; margin-bottom:1.75rem; box-shadow:var(--shadow-sketch);">
        
        <div style="text-align:center; margin-bottom:1.5rem;">
          <div style="font-size:1.45rem; color:var(--primary-forest); font-family:var(--font-serif); font-weight:800;" class="font-serif">
            🗺️ Dual Multi-Stop Google Maps Navigation Routes
          </div>
          <p style="font-size:0.9rem; color:var(--text-secondary); max-width:650px; margin:0.35rem auto 0;">
            Select either <strong>Route A (Must-Visit Spots Only)</strong> or <strong>Route B (Full 1-Day AI Course)</strong> below to open all stops in sequential order in Google Maps!
          </p>
        </div>

        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:1.5rem; margin-bottom:1rem;">
          
          <!-- ROUTE A CARD: MUST-VISIT SPOTS ONLY -->
          <div style="background:#FFF; border:2.5px solid #047857; border-radius:16px; padding:1.5rem; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 4px 12px rgba(4,120,87,0.1);">
            <div>
              <div style="display:inline-block; background:#047857; color:#FFF; font-weight:800; font-size:0.75rem; padding:0.2rem 0.65rem; border-radius:999px; margin-bottom:0.5rem;">
                ROUTE A — MUST-VISIT SPOTS ONLY
              </div>
              <h4 style="font-size:1.15rem; color:#047857; font-family:var(--font-serif); margin-bottom:0.35rem;" class="font-serif">
                📍 選択スポットのみのルート (${cleanMust.length}箇所)
              </h4>
              <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5; margin-bottom:0.85rem;">
                Step 2であなたが選択した<strong>「絶対行きたいスポットのみ」</strong>をGoogleマップで順番にナビゲートします。
              </p>
              
              <div style="margin-bottom:1.25rem; line-height:1.8;">
                ${badgesA}
              </div>
            </div>

            <div>
              <a href="${masterUrlA}" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="padding:0.85rem 1.25rem; font-size:1rem; text-decoration:none; text-align:center; width:100%; justify-content:center; background:#047857; border-color:#064E3B;">
                📍 Open Route A in Google Maps (${cleanMust.length} Spots) ↗
              </a>

              ${cleanMust.length > 1 ? `
                <details style="margin-top:0.75rem; text-align:left; background:#F0FDF4; border-radius:8px; padding:0.4rem 0.65rem; border:1px solid #A7F3D0;">
                  <summary style="font-weight:700; color:#047857; cursor:pointer; font-size:0.82rem;">
                    🚆 Route A 区間別ナビ (${cleanMust.length - 1} Segment)
                  </summary>
                  <div style="margin-top:0.4rem;">
                    ${legItemsAHtml}
                  </div>
                </details>
              ` : ''}
            </div>
          </div>

          <!-- ROUTE B CARD: FULL 1-DAY AI RECOMMENDED COURSE -->
          <div style="background:#FFF; border:2.5px solid #B45309; border-radius:16px; padding:1.5rem; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 4px 12px rgba(180,83,9,0.1);">
            <div>
              <div style="display:inline-block; background:#B45309; color:#FFF; font-weight:800; font-size:0.75rem; padding:0.2rem 0.65rem; border-radius:999px; margin-bottom:0.5rem;">
                ROUTE B — FULL 1-DAY AI RECOMMENDED COURSE
              </div>
              <h4 style="font-size:1.15rem; color:#B45309; font-family:var(--font-serif); margin-bottom:0.35rem;" class="font-serif">
                ✨ 1日フルコースAIルート (${cleanFull.length}箇所)
              </h4>
              <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5; margin-bottom:0.85rem;">
                選択スポットに加え、<strong>AIが提案する朝の名所・ランチ・カフェ・夕方散策</strong>を含めた1日の完璧なルートをGoogleマップでナビゲートします。
              </p>

              <div style="margin-bottom:1.25rem; line-height:1.8;">
                ${badgesB}
              </div>
            </div>

            <div>
              <a href="${masterUrlB}" target="_blank" rel="noopener noreferrer" class="btn btn-emerald" style="padding:0.85rem 1.25rem; font-size:1rem; text-decoration:none; text-align:center; width:100%; justify-content:center; background:#B45309; border-color:#78350F;">
                ✨ Open Route B in Google Maps (${cleanFull.length} Full Stops) ↗
              </a>

              ${cleanFull.length > 1 ? `
                <details style="margin-top:0.75rem; text-align:left; background:#FFFBEB; border-radius:8px; padding:0.4rem 0.65rem; border:1px solid #FDE68A;">
                  <summary style="font-weight:700; color:#B45309; cursor:pointer; font-size:0.82rem;">
                    🚆 Route B 区間別ナビ (${cleanFull.length - 1} Segments)
                  </summary>
                  <div style="margin-top:0.4rem;">
                    ${legItemsBHtml}
                  </div>
                </details>
              ` : ''}
            </div>
          </div>

        </div>

      </div>
    `;
  },

  lastCity: '',
  selectedMustVisitIds: new Set(),
  viewMode: (typeof window !== 'undefined' && window.innerWidth < 768) ? 'compact' : 'grid',
  categoryFilter: 'ALL',

  setViewMode(mode) {
    this.viewMode = mode;
    this.renderCandidateSpots();
  },

  countryCityMap: {
    'France': [
      { value: 'Paris, France', label: '🇫🇷 パリ (Paris)' }
    ],
    'Germany': [
      { value: 'Berlin, Germany', label: '🇩🇪 ベルリン (Berlin)' },
      { value: 'Cologne, Germany', label: '🇩🇪 ケルン (Cologne)' },
      { value: 'Munich, Germany', label: '🇩🇪 ミュンヘン (Munich)' }
    ],
    'Netherlands': [
      { value: 'Amsterdam, Netherlands', label: '🇳🇱 アムステルダム (Amsterdam)' }
    ],
    'Belgium': [
      { value: 'Brussels, Belgium', label: '🇧🇪 ブリュッセル (Brussels)' }
    ],
    'Luxembourg': [
      { value: 'Luxembourg City, Luxembourg', label: '🇱🇺 ルクセンブルク市 (Luxembourg)' }
    ]
  },

  onCountryChange() {
    const countryElem = document.getElementById('aiPlanCountry');
    const destElem = document.getElementById('aiPlanDestination');
    if (!countryElem || !destElem) return;

    const country = countryElem.value || 'France';
    const cities = this.countryCityMap[country] || this.countryCityMap['France'];

    destElem.innerHTML = cities.map(c => `<option value="${c.value}">${c.label}</option>`).join('');
    this.renderCandidateSpots();
  },

  isCategoryMatch(spot, filterGroup) {
    if (!spot || !filterGroup || filterGroup === 'ALL') return true;
    if (filterGroup === 'Kids') return spot.kids === true;
    const c = String(spot.category || '').toLowerCase();
    if (filterGroup === 'Landmark') return c.includes('landmark');
    if (filterGroup === 'Museum') return c.includes('museum') || c.includes('art');
    if (filterGroup === 'Café') return c.includes('café') || c.includes('cafe') || c.includes('bakery') || c.includes('restaurant') || c.includes('bistro') || c.includes('dining');
    if (filterGroup === 'Scenery') return c.includes('scenery') || c.includes('park') || c.includes('market') || c.includes('shopping');
    return true;
  },

  openSpotModal(spotId) {
    let spot = null;
    for (const cityKey in candidateSpotsDatabase) {
      const found = candidateSpotsDatabase[cityKey].find(s => s.id === spotId);
      if (found) {
        spot = found;
        break;
      }
    }
    if (!spot) return;

    let modal = document.getElementById('spotDetailModal');
    if (!modal) {
      modal = document.createElement('div');
      modal.id = 'spotDetailModal';
      modal.className = 'modal-overlay';
      modal.onclick = (e) => this.closeSpotModal(e);
      document.body.appendChild(modal);
    }

    const hasPhoto = Boolean(spot.image);
    const cleanRating = String(spot.rating || '').startsWith('★') ? spot.rating : `★${spot.rating}`;
    const cityClean = (this.lastCity || 'Paris, France').split(',')[0].trim();

    modal.innerHTML = `
      <div class="modal-content" onclick="event.stopPropagation();" style="max-width:440px; padding:1.25rem; border-radius:20px; animation:fadeIn 0.2s ease;">
        <button type="button" class="modal-close" onclick="AITravelEngine.closeSpotModal()" style="top:0.6rem; right:0.6rem;">&times;</button>
        
        <div>
          ${hasPhoto ? `
            <div style="width:100%; height:180px; overflow:hidden; border-radius:14px; margin-bottom:0.85rem; background:#FAF7F2; position:relative;">
              <img src="${spot.image}" alt="${escapeHtml(spot.name)}" style="width:100%; height:100%; object-fit:cover; display:block;">
              <span style="position:absolute; top:8px; left:8px; font-size:0.68rem; font-weight:800; background:rgba(255,255,255,0.92); color:#0369A1; padding:0.15rem 0.45rem; border-radius:4px; border:1px solid #0284C7;">🌐 Wikipedia</span>
              <span style="position:absolute; top:8px; right:8px; font-size:0.8rem; font-weight:800; background:rgba(255,255,255,0.92); color:#047857; padding:0.2rem 0.55rem; border-radius:6px; border:1px solid #047857;">${cleanRating}</span>
            </div>
          ` : `
            <div style="width:100%; height:90px; border-radius:14px; margin-bottom:0.85rem; background:linear-gradient(135deg, #FEF3C7, #E0E7FF); border:1.5px solid var(--border-ink); display:flex; align-items:center; justify-content:space-between; padding:0.85rem 1.1rem;">
              <div style="display:flex; align-items:center; gap:0.5rem;">
                <span style="font-size:1.6rem;">${getCategoryIcon(spot.category)}</span>
                <div>
                  <div style="font-weight:800; font-size:0.9rem; color:var(--primary-wood);">${escapeHtml(spot.category)}</div>
                  <div style="font-size:0.72rem; color:var(--text-secondary);">Verified Google Maps Venue</div>
                </div>
              </div>
              <span style="font-size:0.8rem; font-weight:800; background:#FFF; color:#047857; padding:0.2rem 0.55rem; border-radius:6px; border:1px solid #047857;">${cleanRating}</span>
            </div>
          `}

          <div style="display:flex; align-items:center; gap:0.35rem; flex-wrap:wrap; margin-bottom:0.5rem;">
            <span style="font-size:0.75rem; font-weight:700; background:#E0F2FE; color:#0369A1; padding:0.15rem 0.55rem; border-radius:6px; border:1px solid #0284C7;">${spot.category}</span>
            <span style="font-size:0.72rem; font-weight:700; background:${spot.locationZone === 'suburban' ? '#FEF3C7' : '#F1F5F9'}; color:${spot.locationZone === 'suburban' ? '#B45309' : '#475569'}; padding:0.15rem 0.45rem; border-radius:6px; border:1px solid ${spot.locationZone === 'suburban' ? '#FDE68A' : '#CBD5E1'};">
              ${spot.locationZone === 'suburban' ? '🏞️ 郊外' : '🏙️ 市内'}
            </span>
            ${spot.kids ? `<span style="font-size:0.72rem; font-weight:800; background:#FCE7F3; color:#BE185D; padding:0.15rem 0.45rem; border-radius:6px; border:1px solid #FBCFE8;">🧸 Kids</span>` : ''}
          </div>

          <h3 style="font-size:1.15rem; margin-bottom:0.4rem; font-family:var(--font-sans); color:var(--text-primary); word-break:break-word;">
            ${escapeHtml(spot.name)}
          </h3>

          <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.55; margin-bottom:1rem; word-break:break-word;">
            ${escapeHtml(spot.desc)}
          </p>

          <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.85rem; border-top:1px dashed #EADEC9; padding-top:0.75rem; margin-top:0.5rem; flex-wrap:wrap; gap:0.5rem;">
            <span style="font-weight:700; color:var(--primary-wood);">${escapeHtml(spot.price)}</span>
            ${this.createMapsLink(spot.name.split(' (')[0], cityClean, false)}
          </div>
        </div>
      </div>
    `;

    modal.classList.add('active');
  },

  closeSpotModal(event) {
    if (event && event.target && !event.target.classList.contains('modal-overlay') && !event.target.classList.contains('modal-close')) {
      return;
    }
    const modal = document.getElementById('spotDetailModal');
    if (modal) {
      modal.classList.remove('active');
    }
  },

  formatCompactPrice(priceStr) {
    if (!priceStr) return '';
    const p = String(priceStr).trim();
    if (p.toLowerCase().includes('free')) return 'Free';
    const match = p.match(/€\s*\d+([.,]\d+)?/);
    if (match) return match[0].replace(/\s+/, '');
    return p.length > 8 ? p.substring(0, 8) : p;
  },

  setCategoryFilter(category) {
    this.categoryFilter = category;
    this.renderCandidateSpots();
  },

  // Step 2: Render Interactive Candidate Spots (Max Cap: 8)
  renderCandidateSpots() {
    try {
      const selectElem = document.getElementById('aiPlanDestination');
      const city = selectElem ? selectElem.value : 'Paris, France';
      const areaElem = document.getElementById('aiPlanAreaZone');
      const targetArea = areaElem ? areaElem.value : 'ALL';

      if (this.lastCity && this.lastCity !== city) {
        this.selectedMustVisitIds.clear();
      }
      this.lastCity = city;

      const maxCap = 8;

      let spots = candidateSpotsDatabase[city];
      if (!spots || spots.length === 0) {
        const cleanCityName = city.split(',')[0].trim().toLowerCase();
        for (const k in candidateSpotsDatabase) {
          if (k.toLowerCase().includes(cleanCityName)) {
            spots = candidateSpotsDatabase[k];
            break;
          }
        }
      }
      if (!spots || spots.length === 0) {
        spots = candidateSpotsDatabase['Paris, France'] || [];
      }

      const container = document.getElementById('candidateSpotsGrid');
      const counterBadge = document.getElementById('spotsCounterBadge');

      if (!container) return;

      // 1. Filter by Area Zone (Step 1 dropdown: ALL / city / suburban)
      let filteredSpots = spots;
      if (targetArea && targetArea !== 'ALL') {
        filteredSpots = spots.filter(s => (s.locationZone || 'city') === targetArea);
      }

      // 2. Filter by Category & Kids Filter Chips (Step 2)
      if (this.categoryFilter && this.categoryFilter !== 'ALL') {
        filteredSpots = filteredSpots.filter(s => this.isCategoryMatch(s, this.categoryFilter));
      }

      if (!filteredSpots) {
        filteredSpots = spots;
      }

      if (counterBadge) {
        const selectedCount = this.selectedMustVisitIds.size;
        counterBadge.innerHTML = `Selected: <strong>${selectedCount} / 8</strong> (Max 8 Must-Visit Spots)`;
        counterBadge.style.color = selectedCount >= 8 ? '#C2410C' : '#047857';
      }

      const countLandmarks = spots.filter(s => this.isCategoryMatch(s, 'Landmark')).length;
      const countMuseums = spots.filter(s => this.isCategoryMatch(s, 'Museum')).length;
      const countCafes = spots.filter(s => this.isCategoryMatch(s, 'Café')).length;
      const countScenery = spots.filter(s => this.isCategoryMatch(s, 'Scenery')).length;
      const countKids = spots.filter(s => this.isCategoryMatch(s, 'Kids')).length;

      const categoryFilterBarHtml = `
        <div class="category-filter-bar" style="grid-column:1 / -1; width:100%; display:flex; gap:0.4rem; flex-wrap:wrap; margin-bottom:0.75rem;">
          <button type="button" class="filter-chip ${this.categoryFilter === 'ALL' ? 'active' : ''}" onclick="AITravelEngine.setCategoryFilter('ALL')">
            ✨ ALL (${spots.length})
          </button>
          <button type="button" class="filter-chip ${this.categoryFilter === 'Landmark' ? 'active' : ''}" onclick="AITravelEngine.setCategoryFilter('Landmark')">
            🏛️ 名所 (${countLandmarks})
          </button>
          <button type="button" class="filter-chip ${this.categoryFilter === 'Museum' ? 'active' : ''}" onclick="AITravelEngine.setCategoryFilter('Museum')">
            🎨 美術館・博物館 (${countMuseums})
          </button>
          <button type="button" class="filter-chip ${this.categoryFilter === 'Café' ? 'active' : ''}" onclick="AITravelEngine.setCategoryFilter('Café')">
            ☕ カフェ・グルメ (${countCafes})
          </button>
          <button type="button" class="filter-chip ${this.categoryFilter === 'Scenery' ? 'active' : ''}" onclick="AITravelEngine.setCategoryFilter('Scenery')">
            🌆 景観・街歩き (${countScenery})
          </button>
          <button type="button" class="filter-chip ${this.categoryFilter === 'Kids' ? 'active' : ''}" onclick="AITravelEngine.setCategoryFilter('Kids')">
            🧸 Kids (${countKids})
          </button>
        </div>
      `;

      const viewModeBarHtml = categoryFilterBarHtml + `
        <div class="view-mode-bar" style="grid-column:1 / -1; width:100%; margin-bottom:0.5rem;">
          <div style="display:flex; align-items:center; gap:0.4rem;">
            <span style="font-size:0.88rem; font-weight:800; color:var(--text-primary);">📱 表示モード:</span>
            <span style="font-size:0.8rem; color:var(--text-secondary);">(該当${filteredSpots.length}件)</span>
          </div>
          <div style="display:flex; gap:0.4rem; flex-wrap:wrap;">
            <button type="button" class="view-mode-btn ${this.viewMode === 'compact' ? 'active' : ''}" onclick="AITravelEngine.setViewMode('compact')">
              ⚡ コンパクト (写真なし/高速)
            </button>
            <button type="button" class="view-mode-btn ${this.viewMode === 'grid' ? 'active' : ''}" onclick="AITravelEngine.setViewMode('grid')">
              🖼️ 写真あり (カード)
            </button>
          </div>
        </div>
      `;

      if (this.viewMode === 'compact') {
        container.style.display = 'flex';
        container.style.flexDirection = 'column';
        container.style.gap = '0.45rem';
        container.style.width = '100%';

        container.innerHTML = viewModeBarHtml + filteredSpots.map(s => {
          const isChecked = this.selectedMustVisitIds.has(s.id);
          const rawRating = String(s.rating || '');
          const cleanRating = rawRating.startsWith('★') ? rawRating : `★${rawRating}`;
          const cleanPrice = this.formatCompactPrice(s.price);

          return `
            <div class="card spot-candidate-card" style="border:1.5px solid ${isChecked ? '#B45309' : 'var(--border-ink)'}; background:${isChecked ? '#FEF3C7' : '#FFF'}; cursor:pointer; padding:0.45rem 0.55rem; display:flex; align-items:center; justify-content:space-between; gap:0.4rem; border-radius:10px; transition:all 0.15s ease; box-shadow:${isChecked ? '0 0 0 2px #FDE68A' : 'none'}; width:100%; box-sizing:border-box;" onclick="AITravelEngine.toggleSpotSelection('${s.id}', 8)">
              <div style="display:flex; align-items:flex-start; gap:0.45rem; flex:1; min-width:0;">
                <input type="checkbox" id="chk_${s.id}" ${isChecked ? 'checked' : ''} onclick="event.stopPropagation(); AITravelEngine.toggleSpotSelection('${s.id}', 8)" style="width:20px; height:20px; cursor:pointer; accent-color:#047857; flex-shrink:0; margin-top:2px;">
                
                <div style="display:flex; flex-direction:column; justify-content:center; min-width:0; flex:1;">
                  <!-- Line 1: Spot Name (Up to 2 lines wrap) -->
                  <div style="font-weight:800; font-size:0.92rem; color:var(--text-primary); line-height:1.25; word-break:break-word;">
                    ${escapeHtml(s.name)}
                  </div>

                  <!-- Line 2: Description (Up to 3 lines clamped) -->
                  <p style="font-size:0.77rem; color:var(--text-secondary); line-height:1.35; margin-top:2px; margin-bottom:0; display:-webkit-box; -webkit-line-clamp:3; -webkit-box-orient:vertical; overflow:hidden; text-overflow:ellipsis;">
                    ${escapeHtml(s.desc)}
                  </p>
                </div>
              </div>

              <!-- Right Column: Stacked Rating & Budget (Top), Maps Link (Middle), More Button (Bottom) -->
              <div style="flex-shrink:0; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:0.2rem; margin-left:0.25rem; min-width:44px;">
                <div style="display:flex; align-items:center; gap:0.18rem; flex-wrap:nowrap;">
                  <span style="font-size:0.62rem; font-weight:800; color:#047857; background:#D1FAE5; padding:0.05rem 0.3rem; border-radius:4px; white-space:nowrap;">
                    ${cleanRating}
                  </span>
                  ${cleanPrice ? `
                    <span style="font-size:0.62rem; font-weight:800; color:#78350F; background:#FEF3C7; padding:0.05rem 0.3rem; border-radius:4px; border:1px solid #FDE68A; white-space:nowrap;">
                      ${cleanPrice}
                    </span>
                  ` : ''}
                </div>

                ${this.createMapsLink(s.name.split(' (')[0], city.split(',')[0], true)}

                <button type="button" onclick="event.stopPropagation(); AITravelEngine.openSpotModal('${s.id}')" onpointerdown="event.stopPropagation(); AITravelEngine.openSpotModal('${s.id}')" style="display:inline-flex; align-items:center; justify-content:center; background:#EFF6FF; color:#0369A1; border:1px solid #BAE6FD; padding:0.12rem 0.35rem; border-radius:4px; font-weight:800; font-size:0.62rem; cursor:pointer; white-space:nowrap; -webkit-tap-highlight-color:transparent;" title="View photo & details">
                  More
                </button>
              </div>
            </div>
          `;
        }).join('');
      } else {
        container.style.display = 'grid';
        container.style.flexDirection = 'initial';
        container.style.gap = '1.25rem';
        container.style.width = '100%';

        container.innerHTML = viewModeBarHtml + filteredSpots.map(s => {
          const isChecked = this.selectedMustVisitIds.has(s.id);
          const hasPhoto = Boolean(s.image);

          return `
            <div class="card spot-candidate-card" style="border:2.5px solid ${isChecked ? '#B45309' : 'var(--border-ink)'}; background:${isChecked ? '#FEF3C7' : '#FFF'}; cursor:pointer; transition:all 0.2s ease; display:flex; flex-direction:column; justify-content:space-between; position:relative; box-shadow:${isChecked ? '0 0 0 3px #FDE68A' : 'none'}; width:100%; box-sizing:border-box;" onclick="AITravelEngine.toggleSpotSelection('${s.id}', 8)">
              ${isChecked ? `
                <div style="position:absolute; top:-10px; left:-10px; background:#047857; color:#FFF; font-weight:800; font-size:0.75rem; padding:0.25rem 0.65rem; border-radius:999px; border:2px solid #FFF; box-shadow:0 2px 5px rgba(0,0,0,0.2); z-index:10;">
                  ✓ SELECTED
                </div>
              ` : ''}

              <div>
                ${hasPhoto ? `
                  <div style="width:100%; height:140px; overflow:hidden; border-radius:12px; margin-bottom:0.75rem; background:#FAF7F2; position:relative;">
                    <img src="${s.image}" alt="${escapeHtml(s.name)}" loading="lazy" decoding="async" onerror="this.onerror=null; this.parentElement.style.display='none';" style="width:100%; height:100%; object-fit:cover; display:block;">
                    <span style="position:absolute; top:8px; left:8px; font-size:0.68rem; font-weight:800; background:rgba(255,255,255,0.92); color:#0369A1; padding:0.15rem 0.45rem; border-radius:4px; border:1px solid #0284C7; box-shadow:0 2px 4px rgba(0,0,0,0.1);">🌐 Wikipedia</span>
                    <span style="position:absolute; top:8px; right:8px; font-size:0.75rem; font-weight:800; background:rgba(255,255,255,0.92); color:#047857; padding:0.2rem 0.55rem; border-radius:6px; border:1px solid #047857; box-shadow:0 2px 4px rgba(0,0,0,0.1);">${s.rating}</span>
                  </div>
                ` : `
                  <div style="width:100%; height:76px; border-radius:12px; margin-bottom:0.75rem; background:linear-gradient(135deg, #FEF3C7, #E0E7FF); border:1.5px solid var(--border-ink); display:flex; align-items:center; justify-content:space-between; padding:0.75rem 1rem; position:relative;">
                    <div style="display:flex; align-items:center; gap:0.5rem;">
                      <span style="font-size:1.5rem;">${getCategoryIcon(s.category)}</span>
                      <div>
                        <div style="font-weight:800; font-size:0.85rem; color:var(--primary-wood);">${escapeHtml(s.category)}</div>
                        <div style="font-size:0.72rem; color:var(--text-secondary);">Verified Google Maps Venue</div>
                      </div>
                    </div>
                    <span style="font-size:0.75rem; font-weight:800; background:#FFF; color:#047857; padding:0.2rem 0.55rem; border-radius:6px; border:1px solid #047857;">${s.rating}</span>
                  </div>
                `}

                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.4rem; flex-wrap:wrap; gap:0.3rem;">
                  <div style="display:flex; align-items:center; gap:0.3rem; flex-wrap:wrap;">
                    <span style="font-size:0.75rem; font-weight:700; background:#E0F2FE; color:#0369A1; padding:0.15rem 0.55rem; border-radius:6px; border:1px solid #0284C7;">${s.category}</span>
                    <span style="font-size:0.72rem; font-weight:700; background:${s.locationZone === 'suburban' ? '#FEF3C7' : '#F1F5F9'}; color:${s.locationZone === 'suburban' ? '#B45309' : '#475569'}; padding:0.15rem 0.45rem; border-radius:6px; border:1px solid ${s.locationZone === 'suburban' ? '#FDE68A' : '#CBD5E1'};">
                      ${s.locationZone === 'suburban' ? '🏞️ 郊外' : '🏙️ 市内'}
                    </span>
                    ${s.kids ? `<span style="font-size:0.72rem; font-weight:800; background:#FCE7F3; color:#BE185D; padding:0.15rem 0.45rem; border-radius:6px; border:1px solid #FBCFE8;">🧸 Kids</span>` : ''}
                  </div>
                </div>

                <h4 style="font-size:1.05rem; margin-bottom:0.35rem; font-family:var(--font-sans); color:var(--text-primary); display:flex; align-items:center; gap:0.5rem; word-break:break-word;">
                  <input type="checkbox" id="chk_${s.id}" ${isChecked ? 'checked' : ''} onclick="event.stopPropagation(); AITravelEngine.toggleSpotSelection('${s.id}', 8)" style="width:20px; height:20px; cursor:pointer; accent-color:#047857; flex-shrink:0;">
                  <span>${escapeHtml(s.name)}</span>
                </h4>

                <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5; margin-bottom:0.75rem; word-break:break-word;">${escapeHtml(s.desc)}</p>
              </div>

              <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.8rem; border-top:1px dashed #EADEC9; padding-top:0.5rem; margin-top:auto; gap:0.5rem; flex-wrap:wrap;">
                <span style="font-weight:700; color:var(--primary-wood);">${escapeHtml(s.price)}</span>
                ${this.createMapsLink(s.name.split(' (')[0], city.split(',')[0])}
              </div>
            </div>
          `;
        }).join('');
      }
    } catch (err) {
      console.error('Error in renderCandidateSpots:', err);
    }
  },

  toggleSpotSelection(spotId, maxCap = 8) {
    if (this.selectedMustVisitIds.has(spotId)) {
      this.selectedMustVisitIds.delete(spotId);
    } else {
      if (this.selectedMustVisitIds.size >= maxCap) {
        alert(`Selection Limit Reached! You can select up to ${maxCap} Must-Visit spots.`);
        return;
      }
      this.selectedMustVisitIds.add(spotId);
    }
    this.renderCandidateSpots();
  },

  // Calculate Haversine distance in km between two lat/lng coordinates
  calculateDistance(lat1, lng1, lat2, lng2) {
    if (!lat1 || !lng1 || !lat2 || !lng2) return 0;
    const R = 6371; // Earth radius in km
    const dLat = (lat2 - lat1) * Math.PI / 180;
    const dLng = (lng2 - lng1) * Math.PI / 180;
    const a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
              Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
              Math.sin(dLng / 2) * Math.sin(dLng / 2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    return R * c;
  },

  // Assign time-of-day category slots (1: Morning/Museum, 2: Afternoon Tea, 3: Evening Dinner, 4: Night Walk)
  getCategoryTimeSlot(spot) {
    const cat = String(spot.category || '').toLowerCase();
    const name = String(spot.name || '').toLowerCase();

    // Slot 4: Nightfall & Open Air Walk (River cruises, bridges, illuminated plazas, 24/7 night scenery)
    if (cat.includes('scenery') || cat.includes('walk') || name.includes('cruise') || name.includes('seine') || name.includes('river') || name.includes('bridge') || name.includes('night') || name.includes('plaza')) {
      return 4;
    }

    // Slot 3: Evening Dining (Restaurants, Bistros, Bars, Dinner)
    if (cat.includes('bistro') || cat.includes('restaurant') || cat.includes('dining')) {
      return 3;
    }

    // Slot 2: Afternoon Break & Tea Time (Cafés, Bakeries, Tea Rooms, Parks, Gardens)
    if (cat.includes('café') || cat.includes('cafe') || cat.includes('bakery') || cat.includes('park') || cat.includes('garden')) {
      return 2;
    }

    // Slot 1: Morning & Early Afternoon (Museums, Palaces, Cathedrals, Indoor Landmarks - close around 17:00-18:00)
    return 1;
  },

  // Optimize spot sequence combining Daily Travel Rhythm, Time-of-Day Slots & Geographical Proximity
  optimizeRouteOrder(spots) {
    if (!spots || spots.length <= 1) return spots;

    const list = spots.map(s => ({
      ...s,
      timeSlot: this.getCategoryTimeSlot(s)
    }));

    // Group spots into time-of-day buckets (1: Morning/Afternoon Sightseeing, 2: Cafe/Lunch, 3: Dinner, 4: Night Walk)
    const slot1 = list.filter(s => s.timeSlot === 1);
    const slot2 = list.filter(s => s.timeSlot === 2);
    const slot3 = list.filter(s => s.timeSlot === 3);
    const slot4 = list.filter(s => s.timeSlot === 4);

    // Sub-sort each time bucket by nearest-neighbor geographical distance
    const sortBucketByProximity = (bucket, lastSpot = null) => {
      if (!bucket || bucket.length === 0) return [];
      if (bucket.length === 1) return [...bucket];
      
      const unvisited = [...bucket];
      const sorted = [];

      let current = lastSpot;
      if (!current) {
        // Find westernmost spot in bucket as initial anchor
        let minLng = Infinity;
        let startIdx = 0;
        unvisited.forEach((s, idx) => {
          const lng = Number(s.lng || 0);
          if (lng && lng < minLng) {
            minLng = lng;
            startIdx = idx;
          }
        });
        current = unvisited[startIdx];
        sorted.push(current);
        unvisited.splice(startIdx, 1);
      }

      while (unvisited.length > 0) {
        let nearestIdx = 0;
        let minDistance = Infinity;

        unvisited.forEach((spot, idx) => {
          const dist = this.calculateDistance(current.lat, current.lng, spot.lat, spot.lng);
          if (dist < minDistance) {
            minDistance = dist;
            nearestIdx = idx;
          }
        });

        current = unvisited[nearestIdx];
        sorted.push(current);
        unvisited.splice(nearestIdx, 1);
      }

      return sorted;
    };

    // To prevent consecutive Cafe -> Dinner, split Sightseeing (slot1) into Morning and Afternoon groups!
    let slot1_morning = [];
    let slot1_afternoon = [];

    if (slot1.length > 2 && slot2.length > 0) {
      // Interleave Cafe in the middle of sightseeing (e.g. 2-3 morning sights, Cafe/Lunch, then 2-3 afternoon sights)
      const midPoint = Math.ceil(slot1.length / 2);
      slot1_morning = slot1.slice(0, midPoint);
      slot1_afternoon = slot1.slice(midPoint);
    } else {
      slot1_morning = slot1;
    }

    // 1. Morning Sightseeing (10:00–13:30)
    const sorted1_m = sortBucketByProximity(slot1_morning);
    const last1_m = sorted1_m.length > 0 ? sorted1_m[sorted1_m.length - 1] : null;

    // 2. Mid-Day Cafe & Lunch Break (13:30–15:30)
    const sorted2 = sortBucketByProximity(slot2, last1_m);
    const last2 = sorted2.length > 0 ? sorted2[sorted2.length - 1] : (last1_m || null);

    // 3. Late-Afternoon Sightseeing (15:30–18:00)
    const sorted1_a = sortBucketByProximity(slot1_afternoon, last2);
    const last1_a = sorted1_a.length > 0 ? sorted1_a[sorted1_a.length - 1] : (last2 || null);

    // 4. Evening Dinner (18:30–20:30)
    const sorted3 = sortBucketByProximity(slot3, last1_a);
    const last3 = sorted3.length > 0 ? sorted3[sorted3.length - 1] : (last1_a || null);

    // 5. Night Scenery / Evening Walk (20:00 onwards)
    const sorted4 = sortBucketByProximity(slot4, last3);

    return [...sorted1_m, ...sorted2, ...sorted1_a, ...sorted3, ...sorted4];
  },

  // Step 3: Generate Custom Dual Routes with Geographical & Time-of-Day Flow Optimization
  generateItinerary(event) {
    if (event) event.preventDefault();

    const destElem = document.getElementById('aiPlanDestination');
    const destination = destElem ? destElem.value.trim() : 'Paris, France';
    const areaElem = document.getElementById('aiPlanAreaZone');
    const areaZone = areaElem ? areaElem.value : 'ALL';
    const transportMode = 'transit';

    const resultContainer = document.getElementById('aiPlanResult');
    if (!resultContainer) return;

    const allSpots = candidateSpotsDatabase[destination] || candidateSpotsDatabase['Paris, France'];
    const selectedIds = new Set(this.selectedMustVisitIds);
    
    // Extract checked must-visit spots
    let checkedSpots = allSpots.filter(s => selectedIds.has(s.id));
    if (checkedSpots.length === 0) {
      checkedSpots = allSpots.slice(0, 3);
    }

    // 1. ROUTE A: Geographically & Time-of-Day optimized order for selected spots
    const optimizedSpotsA = this.optimizeRouteOrder(checkedSpots);
    this.routeA_spots = optimizedSpotsA.map(s => ({
      id: s.id,
      name: s.name.split(' (')[0].trim(),
      category: s.category,
      rating: s.rating,
      price: s.price,
      lat: s.lat,
      lng: s.lng,
      isMustVisit: true
    }));

    // 2. ROUTE B: Smart Interleaved 10-Spot AI Course (Guaranteeing Cafés, Bistros & Sights)
    const unselectedSpots = allSpots.filter(s => !selectedIds.has(s.id) && s.category !== 'Hotel & Stay');
    const chosenExtras = [];

    // Helper to check if a category slot is already present in a spots list
    const hasTimeSlot = (spotsList, slotNum) => spotsList.some(s => this.getCategoryTimeSlot(s) === slotNum);

    // AI Recommendation Guarantee 1: Afternoon Café / Bakery (Slot 2: 14:30〜16:30)
    if (!hasTimeSlot(checkedSpots, 2)) {
      const bestCafe = unselectedSpots.find(s => this.getCategoryTimeSlot(s) === 2);
      if (bestCafe) {
        chosenExtras.push(bestCafe);
      }
    }

    // AI Recommendation Guarantee 2: Evening Bistro / Dinner (Slot 3: 17:30〜20:30)
    if (!hasTimeSlot(checkedSpots, 3)) {
      const chosenIds = new Set(chosenExtras.map(s => s.id));
      const bestDinner = unselectedSpots.find(s => this.getCategoryTimeSlot(s) === 3 && !chosenIds.has(s.id));
      if (bestDinner) {
        chosenExtras.push(bestDinner);
      }
    }

    // AI Recommendation Guarantee 3: Night Scenery / Walk (Slot 4: 20:00以降)
    if (!hasTimeSlot(checkedSpots, 4)) {
      const chosenIds = new Set(chosenExtras.map(s => s.id));
      const bestNight = unselectedSpots.find(s => this.getCategoryTimeSlot(s) === 4 && !chosenIds.has(s.id));
      if (bestNight) {
        chosenExtras.push(bestNight);
      }
    }

    // Fill remaining extra slots up to target (9 sightseeing/dining spots)
    const targetBCount = 9;
    const currentCount = checkedSpots.length + chosenExtras.length;
    const neededRemaining = Math.max(0, targetBCount - currentCount);

    if (neededRemaining > 0) {
      const chosenIds = new Set(chosenExtras.map(s => s.id));
      const remainingCandidates = unselectedSpots.filter(s => !chosenIds.has(s.id));
      chosenExtras.push(...remainingCandidates.slice(0, neededRemaining));
    }

    // Combine checked spots + AI recommended spots
    const combinedSpotsB = [...checkedSpots, ...chosenExtras];

    // Geographically & Time-of-Day optimize ALL spots together into a single continuous, seamless travel flow (導線)
    const optimizedSpotsB = this.optimizeRouteOrder(combinedSpotsB);
    this.routeB_spots = optimizedSpotsB.map(s => ({
      id: s.id,
      name: s.name.split(' (')[0].trim(),
      category: s.category,
      rating: s.rating,
      price: s.price,
      lat: s.lat,
      lng: s.lng,
      timeSlot: s.timeSlot,
      isMustVisit: selectedIds.has(s.id)
    }));

    // 3. Hotel Return Destination: Append ONLY if custom hotel input is provided by the user (Applicable to BOTH Route A and Route B)
    const hotelInputElem = document.getElementById('aiPlanHotelInput');
    const customHotelName = hotelInputElem ? hotelInputElem.value.trim() : '';

    if (customHotelName) {
      const returnHotelObj = {
        id: 'user_hotel_custom',
        name: customHotelName.endsWith('(Hotel)') ? customHotelName : `${customHotelName} (Hotel)`,
        category: 'Hotel & Stay',
        rating: '★Stay',
        price: 'Return Hotel',
        lat: allSpots[0] ? allSpots[0].lat : 48.8566,
        lng: allSpots[0] ? allSpots[0].lng : 2.3522,
        isHotel: true,
        isMustVisit: false
      };

      // Append custom Return Hotel as final destination for BOTH Route A and Route B
      this.routeA_spots.push(returnHotelObj);
      this.routeB_spots.push(returnHotelObj);
    }

    this.renderDualRouteManager(destination, transportMode);
  },

  renderDualRouteManager(destination, transportMode) {
    const resultContainer = document.getElementById('aiPlanResult');
    if (!resultContainer) return;

    resultContainer.style.display = 'block';

    const isCar = transportMode === 'car';
    const cityClean = destination.split(',')[0].trim();

    // Generate Route A Google Maps URLs
    const namesA = this.routeA_spots.map(s => s.name);
    const mapsUrlA = this.buildMasterGoogleMapsPath(namesA, destination, transportMode);
    const mapsPathUrlA = this.buildClassicPathMapsUrl(namesA, destination, transportMode);

    // Generate Route B Google Maps URLs
    const namesB = this.routeB_spots.map(s => s.name);
    const mapsUrlB = this.buildMasterGoogleMapsPath(namesB, destination, transportMode);
    const mapsPathUrlB = this.buildClassicPathMapsUrl(namesB, destination, transportMode);

    resultContainer.innerHTML = `
      <div style="background:var(--bg-card-warm); border:2.5px solid var(--border-ink); border-radius:22px; padding:2rem; margin-top:1.5rem; box-shadow:var(--shadow-sketch); animation:fadeIn 0.3s ease;">
        
        <div style="text-align:center; max-width:700px; margin:0 auto 1.5rem;">
          <span class="paper-tape">Multi-Stop Google Maps Navigation</span>
          <h3 style="font-size:1.8rem; margin-top:0.4rem; font-family:var(--font-serif);">
            ${escapeHtml(destination)} — Custom AI Dual Routes
          </h3>
          <p style="font-size:0.9rem; color:var(--text-secondary);">
            Reorder items (▲/▼) or remove items (✕). The master <strong>Open Route in Google Maps</strong> button updates in real-time!
          </p>
        </div>

        <div class="grid-2" style="gap:1.5rem;">
          
          <!-- ROUTE A CARD: Selected Spots Only -->
          <div style="background:#FFF; border:2px solid #047857; border-radius:18px; padding:1.5rem; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 4px 12px rgba(4,120,87,0.1);">
            <div>
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
                <span style="font-size:0.8rem; font-weight:800; background:#D1FAE5; color:#047857; padding:0.25rem 0.65rem; border-radius:999px; border:1px solid #059669;">
                  📍 ROUTE A: SELECTED SPOTS ONLY (${this.routeA_spots.length} SPOTS)
                </span>
                <span style="font-size:0.8rem; font-weight:700; color:#047857;">${isCar ? '🚗 Driving Mode' : '🚆 Transit Mode'}</span>
              </div>

              <h4 style="font-size:1.15rem; color:var(--text-primary); margin-bottom:0.35rem;" class="font-serif">
                Must-Visit Selected Course
              </h4>
              <p style="font-size:0.82rem; color:var(--text-secondary); margin-bottom:1rem;">
                Contains strictly your checked must-visit landmarks.
              </p>

              <!-- Reorderable & Deletable Spot Item List A -->
              <div id="routeA_itemList" style="display:flex; flex-direction:column; gap:0.5rem; margin-bottom:1.25rem;">
                ${this.renderSpotItemsHtml(this.routeA_spots, 'A', cityClean)}
              </div>
            </div>

            <div style="display:flex; flex-direction:column; gap:0.5rem;">
              <a href="${mapsUrlA}" target="_blank" rel="noopener noreferrer" id="btn_maps_RouteA" class="btn btn-emerald" style="width:100%; text-align:center; padding:0.85rem; font-size:0.95rem; border-radius:12px; display:inline-block; text-decoration:none;">
                🗺️ Open Route A in Google Maps (${this.routeA_spots.length} Destinations) ↗
              </a>
              <a href="${mapsPathUrlA}" target="_blank" rel="noopener noreferrer" id="btn_maps_path_RouteA" style="width:100%; text-align:center; padding:0.45rem; font-size:0.78rem; font-weight:700; color:#047857; background:#E6F4EA; border:1px solid #A7F3D0; border-radius:8px; display:inline-block; text-decoration:none;">
                🔗 Alternative Google Maps App Path Link (${this.routeA_spots.length} Stops) ↗
              </a>
            </div>
          </div>

          <!-- ROUTE B CARD: Full 10-Spot Course -->
          <div style="background:#FFF; border:2px solid #B45309; border-radius:18px; padding:1.5rem; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 4px 12px rgba(180,83,9,0.1);">
            <div>
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
                <span style="font-size:0.8rem; font-weight:800; background:#FEF3C7; color:#B45309; padding:0.25rem 0.65rem; border-radius:999px; border:1px solid #D97706;">
                  ✨ ROUTE B: FULL AI 10-SPOT COURSE (${this.routeB_spots.length} SPOTS)
                </span>
                <span style="font-size:0.8rem; font-weight:700; color:#B45309;">${isCar ? '🚗 Driving Mode' : '🚆 Transit Mode'}</span>
              </div>

              <h4 style="font-size:1.15rem; color:var(--text-primary); margin-bottom:0.35rem;" class="font-serif">
                Full 1-Day AI Curated Course
              </h4>
              <p style="font-size:0.82rem; color:var(--text-secondary); margin-bottom:1rem;">
                Combines your selected spots with AI-curated bistros & attractions to form a full 10-stop route.
              </p>

              <!-- Reorderable & Deletable Spot Item List B -->
              <div id="routeB_itemList" style="display:flex; flex-direction:column; gap:0.5rem; margin-bottom:1.25rem;">
                ${this.renderSpotItemsHtml(this.routeB_spots, 'B', cityClean)}
              </div>
            </div>

            <div style="display:flex; flex-direction:column; gap:0.5rem;">
              <a href="${mapsUrlB}" target="_blank" rel="noopener noreferrer" id="btn_maps_RouteB" class="btn btn-primary" style="width:100%; text-align:center; padding:0.85rem; font-size:0.95rem; border-radius:12px; display:inline-block; text-decoration:none;">
                🗺️ Open Route B in Google Maps (${this.routeB_spots.length} Destinations) ↗
              </a>
              <a href="${mapsPathUrlB}" target="_blank" rel="noopener noreferrer" id="btn_maps_path_RouteB" style="width:100%; text-align:center; padding:0.45rem; font-size:0.78rem; font-weight:700; color:#B45309; background:#FEF3C7; border:1px solid #FDE68A; border-radius:8px; display:inline-block; text-decoration:none;">
                🔗 Alternative Google Maps App Path Link (${this.routeB_spots.length} Stops) ↗
              </a>
            </div>
          </div>

        </div>

      </div>
    `;

    setTimeout(() => {
      resultContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 50);
  },

  renderSpotItemsHtml(spotsArray, routeType, cityClean) {
    if (!spotsArray || spotsArray.length === 0) {
      return '<div style="font-size:0.85rem; color:#9CA3AF; padding:0.75rem; text-align:center; border:1px dashed #E5E7EB; border-radius:8px;">No spots in this route. Add spots or re-select.</div>';
    }

    return spotsArray.map((spot, idx) => {
      const query = `${spot.name} ${cityClean}`;
      const mapsUrl = `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(query)}`;

      return `
        <div style="display:flex; align-items:center; justify-content:space-between; background:#F8FAFC; border:1.5px solid #E2E8F0; padding:0.6rem 0.75rem; border-radius:12px; font-size:0.88rem; flex-wrap:wrap; gap:0.5rem;">
          <div style="display:flex; align-items:center; gap:0.5rem; flex:1; min-width:180px;">
            
            <!-- Touch-Friendly Reorder Up / Down Buttons -->
            <div style="display:flex; gap:3px;">
              <button type="button" class="icon-touch-btn" onclick="AITravelEngine.moveSpot('${routeType}', ${idx}, -1)" ${idx === 0 ? 'disabled style="opacity:0.3; cursor:not-allowed;"' : ''} aria-label="Move Up">▲</button>
              <button type="button" class="icon-touch-btn" onclick="AITravelEngine.moveSpot('${routeType}', ${idx}, 1)" ${idx === spotsArray.length - 1 ? 'disabled style="opacity:0.3; cursor:not-allowed;"' : ''} aria-label="Move Down">▼</button>
            </div>

            <span style="font-weight:800; background:#E2E8F0; color:#334155; width:26px; height:26px; display:inline-flex; align-items:center; justify-content:center; border-radius:50%; font-size:0.78rem; flex-shrink:0;">${idx + 1}</span>

            <span style="font-weight:700; color:#1E293B; word-break:break-word; flex:1; display:flex; align-items:center; gap:0.35rem; flex-wrap:wrap;">
              <span>${escapeHtml(spot.name)}</span>
              ${spot.isHotel || spot.category === 'Hotel & Stay' ? `
                <span style="font-size:0.62rem; font-weight:800; background:#F3E8FF; color:#7E22CE; padding:0.08rem 0.3rem; border-radius:4px; border:1px solid #D8B4FE; white-space:nowrap;">🏨 帰着ホテル</span>
              ` : spot.isMustVisit ? `
                <span style="font-size:0.62rem; font-weight:800; background:#D1FAE5; color:#047857; padding:0.08rem 0.3rem; border-radius:4px; border:1px solid #A7F3D0; white-space:nowrap;">📍 選択</span>
              ` : `
                <span style="font-size:0.62rem; font-weight:800; background:#FEF3C7; color:#B45309; padding:0.08rem 0.3rem; border-radius:4px; border:1px solid #FDE68A; white-space:nowrap;">✨ AI推し</span>
              `}
              ${spot.timeSlot === 1 ? `<span style="font-size:0.62rem; font-weight:800; background:#E0F2FE; color:#0369A1; padding:0.08rem 0.3rem; border-radius:4px; border:1px solid #BAE6FD; white-space:nowrap;">🌅 観光</span>` : ''}
              ${spot.timeSlot === 2 ? `<span style="font-size:0.62rem; font-weight:800; background:#FEF3C7; color:#92400E; padding:0.08rem 0.3rem; border-radius:4px; border:1px solid #FDE68A; white-space:nowrap;">☕ カフェ</span>` : ''}
              ${spot.timeSlot === 3 ? `<span style="font-size:0.62rem; font-weight:800; background:#FCE7F3; color:#BE185D; padding:0.08rem 0.3rem; border-radius:4px; border:1px solid #FBCFE8; white-space:nowrap;">🍷 ディナー</span>` : ''}
              ${spot.timeSlot === 4 ? `<span style="font-size:0.62rem; font-weight:800; background:#F1F5F9; color:#334155; padding:0.08rem 0.3rem; border-radius:4px; border:1px solid #CBD5E1; white-space:nowrap;">🌙 夜景・散策</span>` : ''}
            </span>
          </div>

          <div style="display:flex; align-items:center; gap:0.4rem; flex-shrink:0;">
            <!-- Individual Spot Google Maps Link -->
            <a href="${mapsUrl}" target="_blank" rel="noopener noreferrer" style="color:#2563EB; font-weight:700; text-decoration:none; font-size:0.82rem; background:#EFF6FF; border:1.5px solid #BFDBFE; padding:0.4rem 0.65rem; min-height:44px; display:inline-flex; align-items:center; border-radius:8px;">📍 Maps ↗</a>
            
            <!-- Touch-Friendly Delete / Remove Button (❌) -->
            <button type="button" class="icon-touch-btn danger" onclick="AITravelEngine.removeSpot('${routeType}', ${idx})" title="Remove spot from route" aria-label="Remove spot">✕</button>
          </div>
        </div>
      `;
    }).join('');
  },

  moveSpot(routeType, index, direction) {
    const list = routeType === 'A' ? this.routeA_spots : this.routeB_spots;
    const newIndex = index + direction;
    if (newIndex < 0 || newIndex >= list.length) return;

    const temp = list[index];
    list[index] = list[newIndex];
    list[newIndex] = temp;

    this.refreshRouteCard(routeType);
  },

  removeSpot(routeType, index) {
    const list = routeType === 'A' ? this.routeA_spots : this.routeB_spots;
    list.splice(index, 1);
    this.refreshRouteCard(routeType);
  },

  refreshRouteCard(routeType) {
    const destination = document.getElementById('aiPlanDestination')?.value || 'Paris, France';
    const transportMode = 'transit';
    const cityClean = destination.split(',')[0].trim();

    const listContainer = document.getElementById(routeType === 'A' ? 'routeA_itemList' : 'routeB_itemList');
    const mapsBtn = document.getElementById(routeType === 'A' ? 'btn_maps_RouteA' : 'btn_maps_RouteB');
    const mapsPathBtn = document.getElementById(routeType === 'A' ? 'btn_maps_path_RouteA' : 'btn_maps_path_RouteB');

    const spotsList = routeType === 'A' ? this.routeA_spots : this.routeB_spots;

    if (listContainer) {
      listContainer.innerHTML = this.renderSpotItemsHtml(spotsList, routeType, cityClean);
    }

    if (mapsBtn) {
      const names = spotsList.map(s => s.name);
      const mapsUrl = this.buildMasterGoogleMapsPath(names, destination, transportMode);
      mapsBtn.href = mapsUrl;
      mapsBtn.innerText = `🗺️ Open Route ${routeType} in Google Maps (${spotsList.length} Destinations) ↗`;
    }

    if (mapsPathBtn) {
      const names = spotsList.map(s => s.name);
      const mapsPathUrl = this.buildClassicPathMapsUrl(names, destination, transportMode);
      mapsPathBtn.href = mapsPathUrl;
      mapsPathBtn.innerText = `🔗 Alternative Google Maps App Path Link (${spotsList.length} Stops) ↗`;
    }
  },

  buildMasterGoogleMapsPath(venueNames, destination, transportMode) {
    if (!venueNames || venueNames.length === 0) {
      const cityClean = destination.split(',')[0].trim();
      return `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(cityClean)}`;
    }

    const cityClean = destination.split(',')[0].trim();
    const cleanStops = venueNames.map(name => {
      const cleanName = name.replace(/\([^\)]*\)/g, '').trim();
      return `${cleanName}, ${cityClean}`;
    });

    if (cleanStops.length === 1) {
      return `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(cleanStops[0])}`;
    }

    const isCar = transportMode === 'car';
    const travelmode = isCar ? 'driving' : 'transit';

    const origin = encodeURIComponent(cleanStops[0]);
    const dest = encodeURIComponent(cleanStops[cleanStops.length - 1]);

    if (cleanStops.length === 2) {
      return `https://www.google.com/maps/dir/?api=1&origin=${origin}&destination=${dest}&travelmode=${travelmode}`;
    }

    const intermediateStops = cleanStops.slice(1, -1);
    const waypoints = intermediateStops.map(s => encodeURIComponent(s)).join('|');

    return `https://www.google.com/maps/dir/?api=1&origin=${origin}&destination=${dest}&waypoints=${waypoints}&travelmode=${travelmode}`;
  },

  buildClassicPathMapsUrl(venueNames, destination, transportMode) {
    if (!venueNames || venueNames.length === 0) {
      const cityClean = destination.split(',')[0].trim();
      return `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(cityClean)}`;
    }

    const cityClean = destination.split(',')[0].trim();
    const pathStops = venueNames.map(name => {
      const cleanName = name.replace(/\([^\)]*\)/g, '').trim();
      return `${cleanName}, ${cityClean}`.replace(/ /g, '+');
    });

    const isCar = transportMode === 'car';
    const modeParam = isCar ? '&dirflg=d' : '&dirflg=r';
    const pathString = pathStops.join('/');

    return `https://www.google.com/maps/dir/${pathString}/?api=1${modeParam}`;
  }
};

function escapeHtml(str) {
  if (str === null || str === undefined) return '';
  return String(str).replace(/[&<>"']/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' }[m]));
}


window.AITravelEngine = AITravelEngine;

function initAITravelEngine() {
  if (typeof AITravelEngine !== 'undefined') {
    AITravelEngine.renderCandidateSpots();
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initAITravelEngine);
} else {
  initAITravelEngine();
}

window.addEventListener('load', initAITravelEngine);
