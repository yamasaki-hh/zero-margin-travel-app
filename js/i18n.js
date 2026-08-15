/* ==========================================================================
   0 Margin Travel — i18n Multilingual Dictionary & Engine (v4.0.0)
   Supported Languages: EN (Default), JA, ES, ZH, FR, DE
   ========================================================================== */

const I18nEngine = {
  currentLang: 'en',

  supportedLanguages: [
    { code: 'en', label: '🇬🇧 English' },
    { code: 'ja', label: '🇯🇵 日本語' },
    { code: 'es', label: '🇪🇸 Español' },
    { code: 'zh', label: '🇨🇳 中文 (简体)' },
    { code: 'fr', label: '🇫🇷 Français' },
    { code: 'de', label: '🇩🇪 Deutsch' }
  ],

  translations: {
    en: {
      "nav.title": "0 Margin Travel(EU)",
      "nav.badge": "Western Europe & Benelux",
      "hero.badge": "Hi! I'm your Travel Buddy 🍓🐉 — Let's plan your route!",
      "hero.title": "Explore Europe Smarter with Instant Google Maps Routes.",
      "hero.tagline": "Curated ★4.5+ spots. Zero planning fatigue.",
      "hero.subtitle": "Pick your must-visit landmarks, bistros, and gems — get ready-to-use multi-stop Google Maps navigation in seconds.",
      "hero.cta": "🗺️ Create Custom Travel Route",
      "planner.tape": "Interactive Route Planner",
      "planner.title": "Build Your Custom Day in 3 Simple Steps",
      "planner.subtitle": "Handpick your favorites from ★4.5+ verified places and launch ready-to-use multi-stop Google Maps navigation in 1 click!",
      "step1.title": "1️⃣ Step 1: Choose Destination — Select your country & city",
      "label.country": "Country:",
      "label.city": "City:",
      "label.areaZone": "Area Zone:",
      "area.all": "🌐 All Areas (City & Suburban)",
      "area.city": "🏛️ City Center Only",
      "area.suburban": "🏞️ Suburban & Day Trips Only",
      "step2.title": "2️⃣ Step 2: Must-Visit Spots — Select up to 8 places",
      "filter.all": "✨ ALL",
      "filter.landmark": "🏛️ Landmarks",
      "filter.museum": "🎨 Museums",
      "filter.cafe": "☕ Cafés & Dining",
      "filter.scenery": "🌆 Scenery & Walks",
      "filter.kids": "🧸 Kids & Family",
      "view.label": "📱 View Mode:",
      "view.matching": "matching",
      "view.compact": "⚡ Compact List (Fast)",
      "view.grid": "🖼️ Visual Cards (Photos)",
      "badge.mustVisit": "Must-Visit",
      "badge.suburban": "Suburban",
      "badge.city": "City Center",
      "badge.rating": "Rating",
      "badge.price": "Price / Fee",
      "badge.selected": "Selected:",
      "badge.maxNotice": "(Max 8 Must-Visit Spots)",
      "step3.title": "3️⃣ Step 3: Departure & Return Hotel (Optional)",
      "label.startLoc": "Departure Location (Hotel / Station):",
      "placeholder.startLoc": "e.g., Ritz Paris / Gare du Nord (Leave blank if not needed)",
      "label.returnLoc": "Return Location (Hotel / Station):",
      "placeholder.returnLoc": "e.g., Hotel Mercure / Airport (Leave blank if not needed)",
      "btn.generate": "🚀 Generate Optimized Routes (Route A & B)",
      "btn.generating": "⚡ Calculating Optimal Google Maps Route...",
      "results.title": "🗺️ Your Optimized Travel Routes",
      "results.routeA": "📍 Route A: Sequential Geographic Order",
      "results.routeB": "📍 Route B: Category-Balanced Order",
      "btn.launchMaps": "🗺️ Open Multi-Stop Google Maps Navigation",
      "btn.viewDetails": "ℹ️ Spot Details",
      "modal.close": "Close",
      "modal.insiderTip": "💡 Insider Tip:",
      "modal.historicalContext": "📜 Historical Background:",
      "footer.tagline": "Connecting Global Travelers with Local Companions at 0% Commission."
    },
    ja: {
      "nav.title": "0 Margin Travel(EU)",
      "nav.badge": "西欧＆ベネルクス",
      "hero.badge": "こんにちは！旅のパートナー 🍓🐉 です！一緒にルートを作りましょう！",
      "hero.title": "Google Maps最適化ルートで欧州をスマートに旅しよう。",
      "hero.tagline": "厳選★4.5+スポット。事前調べる手間はゼロへ。",
      "hero.subtitle": "行きたい名所・カフェ・絶景を選ぶだけ。数秒でそのまま使えるGoogle Mapsマルチストップナビが完成。",
      "hero.cta": "🗺️ カスタムルートを作成する",
      "planner.tape": "インタラクティブ・ルートプランナー",
      "planner.title": "簡単3ステップで理想の1日を作成",
      "planner.subtitle": "検証済み★4.5+の名所からお気に入気を選び、1クリックでGoogle Mapsマルチストップナビを起動！",
      "step1.title": "1️⃣ ステップ1: 目的地を選択 — 国と都市を選んでください",
      "label.country": "国:",
      "label.city": "都市:",
      "label.areaZone": "エリアゾーン:",
      "area.all": "🌐 全エリア（市内＆郊外日帰り）",
      "area.city": "🏛️ 市内中心部のみ",
      "area.suburban": "🏞️ 郊外・日帰りスポットのみ",
      "step2.title": "2️⃣ ステップ2: 必須訪問スポット — 最大8箇所まで選択",
      "filter.all": "✨ すべて",
      "filter.landmark": "🏛️ 名所・史跡",
      "filter.museum": "🎨 美術館・博物館",
      "filter.cafe": "☕ カフェ・グルメ",
      "filter.scenery": "🌆 景観・街歩き",
      "filter.kids": "🧸 キッズ＆ファミリー",
      "view.label": "📱 表示モード:",
      "view.matching": "該当",
      "view.compact": "⚡ リスト表示（高速）",
      "view.grid": "🖼️ 写真カード表示",
      "badge.mustVisit": "訪問必須",
      "badge.suburban": "郊外",
      "badge.city": "市内",
      "badge.rating": "評価",
      "badge.price": "料金目安",
      "badge.selected": "選択中:",
      "badge.maxNotice": "(最大8箇所まで)",
      "step3.title": "3️⃣ ステップ3: 出発地＆帰着ホテル設定（任意）",
      "label.startLoc": "出発地点（ホテル / 駅）:",
      "placeholder.startLoc": "例: リッツ・パリ / パリ北駅 (未入力でも可)",
      "label.returnLoc": "帰着地点（ホテル / 駅）:",
      "placeholder.returnLoc": "例: メルキュールホテル / 空港 (未入力でも可)",
      "btn.generate": "🚀 最適化ルート（ルートA・B）を生成",
      "btn.generating": "⚡ Google Maps最適化ルートを計算中...",
      "results.title": "🗺️ あなたの最適化ルート",
      "results.routeA": "📍 ルートA: 地理的効率順（移動時間最短）",
      "results.routeB": "📍 ルートB: カテゴリ分散順（バランス重視）",
      "btn.launchMaps": "🗺️ Google Mapsマルチストップナビを開く",
      "btn.viewDetails": "ℹ️ スポット詳細",
      "modal.close": "閉じる",
      "modal.insiderTip": "💡 ワンポイント解説:",
      "modal.historicalContext": "📜 歴史的背景:",
      "footer.tagline": "手数料0%で世界中の旅行者と現地ガイドをつなぐ旅のツール。"
    },
    es: {
      "nav.title": "0 Margin Travel(EU)",
      "nav.badge": "Europa Occidental y Benelux",
      "hero.badge": "¡Hola! Soy tu compañero de viaje 🍓🐉 — ¡Planifiquemos tu ruta!",
      "hero.title": "Explora Europa de forma más inteligente con rutas instantáneas de Google Maps.",
      "hero.tagline": "Lugares seleccionados ★4.5+. Cero fatiga de planificación.",
      "hero.subtitle": "Elige tus monumentos, bistrós y joyas imprescindibles: obtén navegación multidesplazamiento de Google Maps en segundos.",
      "hero.cta": "🗺️ Crear Ruta Personalizada",
      "planner.tape": "Planificador de Rutas Interactivo",
      "planner.title": "Construye tu Día Personalizado en 3 Pasos",
      "planner.subtitle": "Elige tus favoritos de lugares verificados ★4.5+ y lanza la navegación multidesplazamiento de Google Maps en 1 clic.",
      "step1.title": "1️⃣ Paso 1: Elige Destino — Selecciona país y ciudad",
      "label.country": "País:",
      "label.city": "Ciudad:",
      "label.areaZone": "Zona:",
      "area.all": "🌐 Todas las Áreas (Centro y Suburbios)",
      "area.city": "🏛️ Solo Centro Ciudad",
      "area.suburban": "🏞️ Solo Suburbios y Excursiones",
      "step2.title": "2️⃣ Paso 2: Lugares Imprescindibles — Selecciona hasta 8 lugares",
      "filter.all": "✨ TODOS",
      "filter.landmark": "🏛️ Monumentos",
      "filter.museum": "🎨 Museos",
      "filter.cafe": "☕ Cafés y Gastronomía",
      "filter.scenery": "🌆 Paisajes y Paseos",
      "filter.kids": "🧸 Niños y Familia",
      "view.label": "📱 Modo de Vista:",
      "view.matching": "coincidentes",
      "view.compact": "⚡ Lista Compacta (Rápida)",
      "view.grid": "🖼️ Tarjetas Visuales (Fotos)",
      "badge.mustVisit": "Imprescindible",
      "badge.suburban": "Suburbano",
      "badge.city": "Centro",
      "badge.rating": "Valoración",
      "badge.price": "Precio",
      "badge.selected": "Seleccionados:",
      "badge.maxNotice": "(Máximo 8 lugares)",
      "step3.title": "3️⃣ Paso 3: Salida y Hotel de Regreso (Opcional)",
      "label.startLoc": "Lugar de Salida (Hotel / Estación):",
      "placeholder.startLoc": "Ej., Ritz Paris / Estación del Norte (Opcional)",
      "label.returnLoc": "Lugar de Regreso (Hotel / Estación):",
      "placeholder.returnLoc": "Ej., Hotel Mercure / Aeropuerto (Opcional)",
      "btn.generate": "🚀 Generar Rutas Optimizadas (Ruta A y B)",
      "btn.generating": "⚡ Calculando Ruta Optimizada de Google Maps...",
      "results.title": "🗺️ Tus Rutas Optimizadas",
      "results.routeA": "📍 Ruta A: Orden Geográfico Secuencial",
      "results.routeB": "📍 Ruta B: Orden Equilibrado por Categoría",
      "btn.launchMaps": "🗺️ Abrir Navegación en Google Maps",
      "btn.viewDetails": "ℹ️ Detalles del Lugar",
      "modal.close": "Cerrar",
      "modal.insiderTip": "💡 Consejo Experto:",
      "modal.historicalContext": "📜 Contexto Histórico:",
      "footer.tagline": "Conectando viajeros mundiales con guías locales al 0% de comisión."
    },
    zh: {
      "nav.title": "0 Margin Travel(EU)",
      "nav.badge": "西欧与比荷卢",
      "hero.badge": "你好！我是你的旅行伙伴 🍓🐉 — 一起规划路线吧！",
      "hero.title": "使用 Google Maps 智能路线，轻松探索欧洲。",
      "hero.tagline": "精选 ★4.5+ 景点。零行程规划负担。",
      "hero.subtitle": "挑选您必去的地标、餐厅与绝景 — 数秒内即可生成可直接使用的 Google Maps 多停靠点导航。",
      "hero.cta": "🗺️ 创建自定义旅行路线",
      "planner.tape": "互动式路线规划器",
      "planner.title": "只需3个简单步骤，打造专属的一天",
      "planner.subtitle": "从已验证的 ★4.5+ 景点中挑选最爱，一键启动 Google Maps 多停靠点导航！",
      "step1.title": "1️⃣ 步骤 1: 选择目的地 — 选择国家与城市",
      "label.country": "国家:",
      "label.city": "城市:",
      "label.areaZone": "区域:",
      "area.all": "🌐 所有区域 (市区与郊区日游)",
      "area.city": "🏛️ 仅限市中心",
      "area.suburban": "🏞️ 仅限郊区与一日游",
      "step2.title": "2️⃣ 步骤 2: 必游景点 — 最多选择8个地点",
      "filter.all": "✨ 全部",
      "filter.landmark": "🏛️ 地标名胜",
      "filter.museum": "🎨 博物馆",
      "filter.cafe": "☕ 咖啡与美食",
      "filter.scenery": "🌆 散步与风光",
      "filter.kids": "🧸 亲子与家庭",
      "view.label": "📱 视图模式:",
      "view.matching": "匹配",
      "view.compact": "⚡ 紧凑列表 (快速)",
      "view.grid": "🖼️ 照片卡片",
      "badge.mustVisit": "必游景点",
      "badge.suburban": "郊区",
      "badge.city": "市中心",
      "badge.rating": "评分",
      "badge.price": "门票 / 费用",
      "badge.selected": "已选择:",
      "badge.maxNotice": "(最多选择 8 个)",
      "step3.title": "3️⃣ 步骤 3: 出发地与返回酒店 (可选)",
      "label.startLoc": "出发地点 (酒店 / 车站):",
      "placeholder.startLoc": "例如: Ritz Paris / 巴黎北站 (留空亦可)",
      "label.returnLoc": "返回地点 (酒店 / 车站):",
      "placeholder.returnLoc": "例如: Hotel Mercure / 机场 (留空亦可)",
      "btn.generate": "🚀 生成优化路线 (路线 A 与 B)",
      "btn.generating": "⚡ 正在计算 Google Maps 最佳路线...",
      "results.title": "🗺️ 您的专属优化路线",
      "results.routeA": "📍 路线 A: 地理顺序优化 (用时最少)",
      "results.routeB": "📍 路线 B: 类别均衡优化 (体验丰富)",
      "btn.launchMaps": "🗺️ 打开 Google Maps 多停靠点导航",
      "btn.viewDetails": "ℹ️ 景点详情",
      "modal.close": "关闭",
      "modal.insiderTip": "💡 游玩贴士:",
      "modal.historicalContext": "📜 历史背景:",
      "footer.tagline": "以 0% 佣金连接全球旅行者与当地伙伴。"
    },
    fr: {
      "nav.title": "0 Margin Travel(EU)",
      "nav.badge": "Europe de l'Ouest & Benelux",
      "hero.badge": "Salut! Je suis votre compagnon de voyage 🍓🐉 — Planifions votre itinéraire!",
      "hero.title": "Explorez l'Europe plus intelligemment avec des itinéraires Google Maps instantanés.",
      "hero.tagline": "Lieux sélectionnés ★4.5+. Zéro fatigue de planification.",
      "hero.subtitle": "Choisissez vos monuments, bistrots et pépites — obtenez une navigation Google Maps multi-arrêts en quelques secondes.",
      "hero.cta": "🗺️ Créer un itinéraire personnalisé",
      "planner.tape": "Planificateur d'itinéraire interactif",
      "planner.title": "Créez votre journée personnalisée en 3 étapes",
      "planner.subtitle": "Sélectionnez vos lieux vérifiés ★4.5+ préférés et lancez la navigation Google Maps multi-arrêts en 1 clic!",
      "step1.title": "1️⃣ Étape 1: Choisissez la destination — Sélectionnez votre pays et ville",
      "label.country": "Pays:",
      "label.city": "Ville:",
      "label.areaZone": "Zone:",
      "area.all": "🌐 Toutes les zones (Centre & Banlieue)",
      "area.city": "🏛️ Centre-ville uniquement",
      "area.suburban": "🏞️ Banlieue & Excursions uniquement",
      "step2.title": "2️⃣ Étape 2: Lieux incontournables — Choisissez jusqu'à 8 lieux",
      "filter.all": "✨ TOUS",
      "filter.landmark": "🏛️ Monuments",
      "filter.museum": "🎨 Musées",
      "filter.cafe": "☕ Cafés & Gastronomie",
      "filter.scenery": "🌆 Promenades & Paysages",
      "filter.kids": "🧸 Enfants & Famille",
      "view.label": "📱 Mode d'affichage:",
      "view.matching": "correspondants",
      "view.compact": "⚡ Liste compacte (Rapide)",
      "view.grid": "🖼️ Cartes visuelles (Photos)",
      "badge.mustVisit": "Incontournable",
      "badge.suburban": "Banlieue",
      "badge.city": "Centre-ville",
      "badge.rating": "Note",
      "badge.price": "Prix / Tarif",
      "badge.selected": "Sélectionnés:",
      "badge.maxNotice": "(Max 8 lieux)",
      "step3.title": "3️⃣ Étape 3: Départ et hôtel de retour (Optionnel)",
      "label.startLoc": "Lieu de départ (Hôtel / Gare):",
      "placeholder.startLoc": "ex., Ritz Paris / Gare du Nord (Optionnel)",
      "label.returnLoc": "Lieu de retour (Hôtel / Gare):",
      "placeholder.returnLoc": "ex., Hôtel Mercure / Aéroport (Optionnel)",
      "btn.generate": "🚀 Générer les itinéraires optimisés (Route A & B)",
      "btn.generating": "⚡ Calcul de l'itinéraire Google Maps en cours...",
      "results.title": "🗺️ Vos itinéraires optimisés",
      "results.routeA": "📍 Route A: Ordre géographique séquentiel",
      "results.routeB": "📍 Route B: Ordre équilibré par catégorie",
      "btn.launchMaps": "🗺️ Ouvrir la navigation Google Maps multi-arrêts",
      "btn.viewDetails": "ℹ️ Détails du lieu",
      "modal.close": "Fermer",
      "modal.insiderTip": "💡 Conseil pratique:",
      "modal.historicalContext": "📜 Contexte historique:",
      "footer.tagline": "Connecter les voyageurs du monde entier avec des guides locaux à 0% de commission."
    },
    de: {
      "nav.title": "0 Margin Travel(EU)",
      "nav.badge": "Westeuropa & Benelux",
      "hero.badge": "Hallo! Ich bin dein Reisebegleiter 🍓🐉 — Lass uns deine Route planen!",
      "hero.title": "Entdecke Europa smarter mit sofortigen Google Maps Routen.",
      "hero.tagline": "Kuratierte ★4.5+ Orte. Null Planungsstress.",
      "hero.subtitle": "Wähle deine Lieblings-Sehenswürdigkeiten, Bistros und Geheimtipps — erhalte in Sekundenschnelle eine gebrauchsfertige Google Maps Navigation mit mehreren Stopps.",
      "hero.cta": "🗺️ Eigene Route erstellen",
      "planner.tape": "Interaktiver Routenplaner",
      "planner.title": "Erstelle deinen perfekten Tag in 3 einfachen Schritten",
      "planner.subtitle": "Wähle deine Favoriten aus geprüften ★4.5+ Orten und starte die Google Maps Mehr-Stopp-Navigation mit 1 Klick!",
      "step1.title": "1️⃣ Schritt 1: Ziel wählen — Wähle Land & Stadt",
      "label.country": "Land:",
      "label.city": "Stadt:",
      "label.areaZone": "Bereich:",
      "area.all": "🌐 Alle Bereiche (Zentrum & Umgebung)",
      "area.city": "🏛️ Nur Stadtzentrum",
      "area.suburban": "🏞️ Nur Umgebung & Tagesausflüge",
      "step2.title": "2️⃣ Schritt 2: Highlights — Wähle bis zu 8 Orte",
      "filter.all": "✨ ALLE",
      "filter.landmark": "🏛️ Sehenswürdigkeiten",
      "filter.museum": "🎨 Museen",
      "filter.cafe": "☕ Cafés & Gastronomie",
      "filter.scenery": "🌆 Spaziergänge & Aussichten",
      "filter.kids": "🧸 Kinder & Familie",
      "view.label": "📱 Ansicht:",
      "view.matching": "passend",
      "view.compact": "⚡ Kompaktliste (Schnell)",
      "view.grid": "🖼️ Fotokarten",
      "badge.mustVisit": "Top-Highlight",
      "badge.suburban": "Umgebung",
      "badge.city": "Stadtzentrum",
      "badge.rating": "Bewertung",
      "badge.price": "Preis / Eintritt",
      "badge.selected": "Ausgewählt:",
      "badge.maxNotice": "(Maximal 8 Orte)",
      "step3.title": "3️⃣ Schritt 3: Start- & Rückkehr-Hotel (Optional)",
      "label.startLoc": "Startort (Hotel / Bahnhof):",
      "placeholder.startLoc": "z. B. Ritz Paris / Nordbahnhof (Optional)",
      "label.returnLoc": "Rückkehrort (Hotel / Bahnhof):",
      "placeholder.returnLoc": "z. B. Hotel Mercure / Flughafen (Optional)",
      "btn.generate": "🚀 Optimierte Routen erstellen (Route A & B)",
      "btn.generating": "⚡ Berechne Google Maps Route...",
      "results.title": "🗺️ Deine optimierten Routen",
      "results.routeA": "📍 Route A: Geografisch optimale Reihenfolge",
      "results.routeB": "📍 Route B: Ausgewogene Kategorie-Reihenfolge",
      "btn.launchMaps": "🗺️ Google Maps Navigation mit Stopps öffnen",
      "btn.viewDetails": "ℹ️ Details anzeigen",
      "modal.close": "Schließen",
      "modal.insiderTip": "💡 Geheimtipp:",
      "modal.historicalContext": "📜 Historischer Hintergrund:",
      "footer.tagline": "Verbindet Reisende weltweit mit lokalen Begleitern bei 0% Provision."
    }
  },

  init() {
    // Detect stored language or browser language
    const saved = localStorage.getItem('0mt_lang');
    if (saved && this.translations[saved]) {
      this.currentLang = saved;
    } else {
      const browserLang = (navigator.language || 'en').slice(0, 2).toLowerCase();
      if (this.translations[browserLang]) {
        this.currentLang = browserLang;
      } else {
        this.currentLang = 'en';
      }
    }
    this.applyLanguage(this.currentLang);
  },

  setLanguage(lang) {
    if (!this.translations[lang]) return;
    this.currentLang = lang;
    localStorage.setItem('0mt_lang', lang);
    this.applyLanguage(lang);

    // Trigger re-render of candidate spots in active language
    if (window.AITravelEngine) {
      window.AITravelEngine.renderCandidateSpots();
    }
  },

  getText(key) {
    const langDict = this.translations[this.currentLang] || this.translations.en;
    return langDict[key] || this.translations.en[key] || key;
  },

  applyLanguage(lang) {
    const langDict = this.translations[lang] || this.translations.en;
    
    // Update elements with data-i18n attribute
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if (langDict[key]) {
        el.innerHTML = langDict[key];
      }
    });

    // Update input placeholders with data-i18n-placeholder
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
      const key = el.getAttribute('data-i18n-placeholder');
      if (langDict[key]) {
        el.setAttribute('placeholder', langDict[key]);
      }
    });

    // Update active state in language selector dropdown
    const langSelect = document.getElementById('globalLanguageSelect');
    if (langSelect) {
      langSelect.value = lang;
    }
  }
};

window.I18nEngine = I18nEngine;
document.addEventListener('DOMContentLoaded', () => {
  I18nEngine.init();
});
