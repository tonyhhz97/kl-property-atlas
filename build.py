import os
import json

data = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'projects_embed.json')).read()

# Logo marks: a black-background version (shown on the light theme, for
# contrast) and a white-background version (shown on the dark theme,
# default). Embedded as base64 data URIs so the page stays a single file.
LOGO_BLACK_BG_B64 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logo_black_bg.b64')).read().strip()
LOGO_WHITE_BG_B64 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logo_white_bg.b64')).read().strip()
PROFILE_TONY_B64 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'profile_tony.b64')).read().strip()
ABOUT_BG_B64 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'about_bg.b64')).read().strip()
HERO_BG_B64 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hero_bg.b64')).read().strip()
TESTI_CASTIEOL_B64 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testi_Castieol.b64')).read().strip()
TESTI_ANDY_B64 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testi_Andy.b64')).read().strip()
TESTI_MRLIM_B64 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testi_MrLim.b64')).read().strip()
TESTI_GRACE_B64 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testi_Grace.b64')).read().strip()
TESTI_LAWRENCE_B64 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testi_Lawrence.b64')).read().strip()
TESTI_MSFONG_B64 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testi_MsFong.b64')).read().strip()

CSS = r"""
:root{
  --ink:#1c1810; --ink-soft:#6b6152; --bg:#fffdf9; --bg-card:#ffffff;
  --gold:#b8862f; --gold-dark:#8a651b; --gold-light:#faf1de;
  --ok:#3f7d5c; --ok-light:#e8f2ec;
  --line:#ece4d2; --red:#c0392b;
  --radius:16px; --radius-sm:10px;
  --shadow:0 4px 24px rgba(28,24,16,.06); --shadow-lg:0 12px 40px rgba(28,24,16,.14);
  --wa:#25D366;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:'Times New Roman',Times,serif;background:var(--bg);color:var(--ink);line-height:1.5;-webkit-font-smoothing:antialiased}
body.dark{--bg:#16130d;--bg-card:#211c13;--ink:#f5efe1;--ink-soft:#c2b8a3;--line:#332b1c;--gold-light:#2e2410;--ok-light:#16261e}
h1,h2,h3,h4{font-family:'Times New Roman',Times,serif;margin:0 0 .4em;font-weight:600;letter-spacing:-.01em}
a{color:inherit}
img{max-width:100%;display:block}
.container{max-width:1240px;margin:0 auto;padding:0 20px}
.pill{display:inline-flex;align-items:center;gap:6px;padding:5px 13px;border-radius:99px;font-size:0.975rem;font-weight:600;letter-spacing:.02em}
.pill-ok{background:var(--ok-light);color:var(--ok)}
.pill-gold{background:var(--gold-light);color:var(--gold-dark)}
body.dark .pill-gold{color:#e8c47a}
.pill-red{background:#fbeae7;color:var(--red)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:13px 22px;border-radius:99px;font-weight:600;font-size:1.075rem;border:none;cursor:pointer;transition:transform .15s ease,box-shadow .15s ease;text-decoration:none}
.btn:active{transform:scale(.97)}
.btn-primary{background:var(--wa);color:#fff;box-shadow:0 6px 20px rgba(37,211,102,.35)}
.btn-primary:hover{box-shadow:0 8px 26px rgba(37,211,102,.45)}
.btn-outline{background:transparent;border:1.5px solid var(--line);color:var(--ink)}
.btn-outline:hover{border-color:var(--gold)}
.btn-gold{background:var(--gold);color:#fff;box-shadow:0 6px 20px rgba(184,134,47,.35)}
.btn-gold:hover{box-shadow:0 8px 26px rgba(184,134,47,.45)}
.btn-gold:disabled{opacity:.55;cursor:not-allowed;box-shadow:none}
.btn-dark{background:var(--ink);color:var(--bg)}
.btn-sm{padding:8px 16px;font-size:1.005rem}
.btn:disabled{opacity:.45;cursor:not-allowed}

/* NAV */
.nav{position:sticky;top:0;z-index:60;background:rgba(247,245,239,.88);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
body.dark .nav{background:rgba(16,21,18,.88)}
.nav-inner{display:flex;align-items:center;justify-content:space-between;padding:12px 20px;gap:10px;flex-wrap:nowrap}
@media(max-width:900px){.nav-inner{flex-wrap:wrap}}
#syncBadge{font-size:0.845rem}
@media(max-width:640px){#syncBadge{display:none}}
@media(max-width:520px){.hero-stats{grid-template-columns:repeat(2,1fr)}}
.brand{display:flex;align-items:center;gap:8px;font-weight:700;font-size:1.175rem;min-width:0;flex:0 1 auto}
.brand-title{font-size:0.92rem;font-weight:700;line-height:1.15;white-space:nowrap}
.brand-tagline{font-size:0.8625rem;font-weight:500;color:var(--ink-soft);margin-top:1px;white-space:nowrap}
/* Previously hidden below 900px, which also hid it on phones (iOS included)
   - Tony wants it visible everywhere. Switching nowrap to normal at narrow
   widths lets it wrap onto a second line instead of overflowing the nav bar
   on small screens; nothing else about the nav layout changes. */
@media(max-width:480px){.brand-title,.brand-tagline{white-space:normal}}
.brand-mark{height:44px;width:auto;border-radius:8px;overflow:hidden;display:flex;align-items:center;justify-content:center;flex:0 0 auto}
/* Two logo images live in the DOM at once; CSS swaps which is visible so it
   follows the theme automatically (no JS needed beyond the existing dark
   mode toggle). Light theme = black-background logo for contrast; dark
   theme (default) = white-background logo for contrast. Each logo image
   includes the "KL PROJECT ATLAS" wordmark under the icon, so it's a
   rectangular lockup rather than a square icon - object-fit:contain with a
   fixed height (rather than width+height+cover) keeps the whole design and
   wordmark visible without cropping either side. */
.brand-mark img{height:100%;width:auto;object-fit:contain;display:none}
.brand-mark img.logo-for-light{display:block}
body.dark .brand-mark img.logo-for-light{display:none}
body.dark .brand-mark img.logo-for-dark{display:block}
.nav-actions{display:flex;align-items:center;gap:10px;flex-wrap:wrap;justify-content:flex-end}
@media(max-width:560px){#sendShortlistBtn .btn-label{display:none}}
.icon-btn{width:38px;height:38px;border-radius:99px;border:1.5px solid var(--line);background:var(--bg-card);color:var(--ink);display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:1.125rem;position:relative}
.icon-btn.active{background:var(--gold);border-color:var(--gold);color:#fff}
.shortlist-badge{position:absolute;top:-6px;right:-6px;background:var(--gold);color:#fff;font-size:0.775rem;font-weight:700;min-width:17px;height:17px;border-radius:99px;display:flex;align-items:center;justify-content:center;padding:0 3px}

/* HERO */
.hero{position:relative;padding:56px 0 40px;overflow:hidden;background:radial-gradient(1200px 500px at 15% -10%,#fbf3e0 0%,transparent 60%),radial-gradient(900px 500px at 90% 0%,var(--gold-light) 0%,transparent 55%)}
body.dark .hero{background:radial-gradient(1200px 500px at 15% -10%,#2e2410 0%,transparent 60%),radial-gradient(900px 500px at 90% 0%,#241f10 0%,transparent 55%)}
/* Dark-mode-only KL skyline background, same treatment (and same tuning -
   brightness/desaturation/warmth/vignette strength) as the about-intro band
   below, per Tony's explicit preference for that section's brighter, more
   visible look over an earlier heavier-scrim version tried here. Legibility
   is protected with text-shadow on the headline copy (see .eyebrow/.hero h1/
   .hero p.lead below) instead of a strong dark band, so the skyline -
   including the twin towers - stays clearly recognizable. Never shown in
   light mode - that theme keeps the plain glow background above. */
body.dark .hero::before{
  content:"";position:absolute;inset:0;z-index:0;pointer-events:none;
  background-image:
    radial-gradient(ellipse 88% 110% at 50% 45%, rgba(22,19,13,.08) 0%, rgba(22,19,13,.40) 60%, var(--bg) 100%),
    linear-gradient(to bottom, var(--bg) 0%, rgba(22,19,13,0) 14%, rgba(22,19,13,0) 86%, var(--bg) 100%),
    url('data:image/jpeg;base64,__HERO_BG__');
  background-size:cover;
  background-position:center 40%;
  background-repeat:no-repeat;
  animation:bgSlowZoom 15s ease-in-out infinite alternate;
  will-change:transform;
}
/* Hero content is centered end-to-end (eyebrow through the trust row) for a
   calmer, more poster-like first impression; the lead paragraph is
   justified for tidy edges, with text-align-last:center so its short final
   line doesn't look stranded to one side. */
.hero .container{position:relative;z-index:1;text-align:center}
.eyebrow{display:flex;align-items:center;justify-content:center;gap:8px;font-size:1.075rem;font-weight:800;color:var(--gold-dark);text-transform:uppercase;letter-spacing:.04em;margin-bottom:16px}
/* Soft dark halo (layered 0-offset blurred text-shadows) instead of a hard
   outline or a single drop-shadow - keeps text crisp and premium-looking
   while still standing well off the skyline photo behind it. Tony compared
   this against a solid black outline and preferred the softer glow. */
body.dark .eyebrow{color:#e3bd77;text-shadow:0 0 3px rgba(0,0,0,.85),0 0 8px rgba(0,0,0,.6)}
.hero h1{font-size:clamp(2.1rem,5vw,3.4rem);line-height:1.06;max-width:820px;margin:0 auto 14px}
body.dark .hero h1{text-shadow:0 0 4px rgba(0,0,0,.85),0 0 14px rgba(0,0,0,.65),0 0 28px rgba(0,0,0,.45)}
.hero h1 em{font-style:normal;font-weight:600;color:var(--gold)}
body.dark .hero p.lead{color:#f7f3ea;text-shadow:0 0 3px rgba(0,0,0,.85),0 0 10px rgba(0,0,0,.7),0 0 20px rgba(0,0,0,.5)}
.hero p.lead{font-size:1.205rem;color:var(--ink-soft);max-width:600px;margin:0 auto 26px;text-align:justify;text-align-last:center}
.hero-cta{display:flex;flex-wrap:wrap;justify-content:center;gap:12px;margin-bottom:34px}
.hero-stats{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}
.hero-stat{padding:16px 14px;border:1px solid var(--line);border-radius:var(--radius-sm);background:var(--bg-card)}
.hero-stat .num{font-family:'Times New Roman',Times,serif;font-size:1.525rem;font-weight:600;color:var(--gold-dark)}
body.dark .hero-stat .num{color:#e3bd77}
.hero-stat .label{font-size:0.975rem;color:var(--ink-soft);margin-top:2px}
.trust-row{display:flex;align-items:center;justify-content:center;gap:14px;margin-top:22px;font-size:1.005rem;color:var(--ink-soft);flex-wrap:wrap}
.trust-row .stars{color:var(--gold);letter-spacing:1px}

/* VERDICT */
.verdict{padding:36px 0 8px}
.section-head{display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:20px;gap:16px;flex-wrap:wrap}
.section-head h2{font-size:1.725rem;margin:0}
.section-head p{color:var(--ink-soft);margin:4px 0 0;font-size:1.045rem}
.verdict-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.verdict-card{background:var(--bg-card);border:1px solid var(--line);border-radius:var(--radius);padding:18px;position:relative;overflow:hidden;cursor:pointer;transition:box-shadow .2s,transform .2s}
.verdict-card:hover{box-shadow:var(--shadow-lg);transform:translateY(-2px)}
.verdict-card .tag{font-size:0.925rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--gold-dark)}
body.dark .verdict-card .tag{color:#e3bd77}
.verdict-card .proj{font-family:'Times New Roman',Times,serif;font-size:1.375rem;margin:8px 0 2px}
.verdict-card .meta{font-size:1.005rem;color:var(--ink-soft)}
.verdict-card .value{margin-top:10px;font-size:1.275rem;font-weight:700;color:var(--ink)}
.verdict-icon{position:absolute;right:14px;top:14px;font-size:1.525rem;opacity:.5}

/* FILTERS (its own section, ahead of Most Popular Picks) */
.filters-hero{padding:8px 0 28px}
.filter-block{margin-bottom:16px}
.filter-block:last-child{margin-bottom:0}
.filter-row-compact{display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));gap:14px;max-width:700px}
.filter-label-row{display:flex;align-items:center;gap:10px;margin-bottom:8px;flex-wrap:wrap}
.filter-label-row label{font-size:1.075rem;font-weight:700;color:var(--ink);white-space:nowrap}
.req-pill,.opt-pill{white-space:nowrap}
.req-pill{font-size:0.94rem;padding:4px 12px;font-weight:800;letter-spacing:.05em;text-transform:uppercase}
.hint{font-size:0.975rem;color:var(--ink-soft)}
.fav-callout{display:flex;align-items:center;gap:10px;background:var(--gold-light);border:1px solid var(--gold);border-radius:var(--radius-sm);padding:12px 16px;font-size:0.995rem;color:var(--ink)}
body.dark .fav-callout{background:#2e2410;border-color:var(--gold-dark);color:var(--ink)}
.fav-callout .ic{font-size:1.325rem;flex:0 0 auto}
.pill-neutral{background:var(--bg-card);color:var(--ink-soft);border:1.5px solid var(--line)}
.opt-pill{font-size:0.94rem;padding:4px 12px;font-weight:800;letter-spacing:.05em;text-transform:uppercase}
.search-row{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.search-box{flex:1;position:relative;min-width:220px}
.search-box input{width:100%;padding:11px 16px 11px 40px;border-radius:99px;border:1.5px solid var(--line);background:var(--bg-card);font-size:1.045rem;color:var(--ink)}
.search-box input:focus{outline:none;border-color:var(--gold)}
.search-box .ic{position:absolute;left:15px;top:50%;transform:translateY(-50%);opacity:.5}
.sort-select{padding:11px 34px 11px 16px;border-radius:99px;border:1.5px solid var(--line);background:var(--bg-card);font-size:1.045rem;font-weight:600;color:var(--ink);cursor:pointer;appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%236b6152'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 14px center}
body.dark .sort-select{background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%23c2b8a3'/%3E%3C/svg%3E")}
.chip-row{display:flex;gap:8px;overflow-x:auto;padding-bottom:2px;scrollbar-width:none;flex-wrap:wrap}
.chip-row::-webkit-scrollbar{display:none}
.chip{flex:0 0 auto;padding:8px 15px;border-radius:99px;border:1.5px solid var(--line);background:var(--bg-card);color:var(--ink);font-size:1.025rem;font-weight:600;cursor:pointer;white-space:nowrap;transition:.15s}
.chip.active{background:var(--gold);border-color:var(--gold);color:#fff}
.filter-row2{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.results-count{font-size:1.025rem;color:var(--ink-soft);margin-left:auto;white-space:nowrap}
.filter-actions{display:flex;flex-wrap:wrap;gap:10px;align-items:center;padding-top:18px;border-top:1px solid var(--line)}

/* Area tiles - rectangular, multi-select, tick when chosen */
.area-tile-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:10px}
.area-tile{position:relative;text-align:left;background:var(--bg-card);border:1.5px solid var(--line);border-radius:12px;padding:14px 16px;cursor:pointer;transition:.15s;font-family:inherit}
.area-tile:hover{border-color:var(--gold)}
.area-tile.active{border-color:var(--gold);background:var(--gold-light)}
.area-tile .tile-name{font-weight:700;font-size:1.045rem;color:var(--ink)}
.area-tile .tile-meta{font-size:0.945rem;color:var(--ink-soft);margin-top:3px}
.tile-tick{position:absolute;top:8px;right:10px;width:18px;height:18px;border-radius:99px;background:var(--gold);color:#fff;font-size:0.825rem;display:flex;align-items:center;justify-content:center;font-weight:700}

.select-filter select{min-width:180px}
@media(max-width:700px){.select-filter select{width:100%}}

/* TABLE */
.table-section{padding:28px 0 60px}
.table-wrap{background:var(--bg-card);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden}
table{width:100%;border-collapse:collapse;font-size:1.045rem}
thead th:nth-child(3),thead th:nth-child(4),thead th:nth-child(5),thead th:nth-child(6),thead th:nth-child(7),thead th:nth-child(8),
tbody td:nth-child(3),tbody td:nth-child(4),tbody td:nth-child(5),tbody td:nth-child(6),tbody td:nth-child(7),tbody td:nth-child(8){text-align:center}
tbody td:nth-child(1){text-align:center}
/* Not sticky: .table-wrap uses overflow:hidden for its rounded corners, and
   that overflow setting conflicts with position:sticky on a th inside it -
   the two together caused a visible double-render/overlap glitch on the
   first row. A static header avoids that class of bug entirely. */
thead th{text-align:left;padding:16px 14px;background:var(--gold-light);color:var(--gold-dark);font-weight:800;font-size:1.125rem;text-transform:uppercase;letter-spacing:.05em;white-space:nowrap}
body.dark thead th{color:#e3bd77}
tbody tr{border-top:1px solid var(--line);cursor:pointer;transition:background .12s}
tbody tr:hover{background:var(--gold-light)}
tbody td{padding:14px;vertical-align:top}
.proj-cell{min-width:190px}
.proj-name{font-weight:700;font-size:1.105rem;display:flex;align-items:center;gap:7px}
.proj-loc{font-size:0.975rem;color:var(--ink-soft);margin-top:2px}
.proj-dev{font-size:0.945rem;color:var(--ink-soft)}
.price-cell .from{font-size:0.885rem;color:var(--ink-soft);text-transform:uppercase;letter-spacing:.03em}
.price-cell .num{font-weight:700;font-size:1.145rem;color:var(--gold-dark)}
body.dark .price-cell .num{color:#e3bd77}
.badge{display:inline-block;padding:2px 9px;border-radius:99px;font-size:0.9475rem;font-weight:700;text-transform:uppercase}
.badge-sold{background:#fbeae7;color:var(--red)}
.badge-avail{background:var(--ok-light);color:var(--ok)}
body.dark .badge-avail{background:#bdf0d3;color:#0f4a2c}
.badge-tbc{background:var(--gold-light);color:var(--gold-dark)}
body.dark .badge-tbc{color:#e8c47a}
.fav-btn{background:none;border:none;cursor:pointer;font-size:1.175rem;opacity:.4;padding:0}
.fav-btn.active{opacity:1}
/* First-time visitors get a few gentle pulses on every heart icon so it's
   obvious what to tap - this stops permanently (via localStorage) the
   moment anyone shortlists a project, so it never becomes annoying for
   repeat visitors. */
@keyframes favPulseHint{0%,100%{transform:scale(1)}50%{transform:scale(1.35)}}
.fav-btn.pulse-hint{animation:favPulseHint 1s ease-in-out 3}
/* Filter button gently pulses whenever a pick has changed but hasn't been
   applied yet, so it's obvious there's a "Filter" click still needed. */
@keyframes filterPendingPulse{0%,100%{box-shadow:0 6px 20px rgba(184,134,47,.35)}50%{box-shadow:0 6px 26px rgba(184,134,47,.75)}}
.btn-gold.pending{animation:filterPendingPulse 1.4s ease-in-out infinite}
.cmp-check{width:17px;height:17px;cursor:pointer;accent-color:var(--gold)}
.expand-row td{background:var(--bg);padding:0;border-top:none}
.expand-inner{padding:20px;display:none;grid-template-columns:1.3fr 1fr;gap:24px}
.expand-inner.open{display:grid}
.unit-table{width:100%;border-collapse:collapse;font-size:1.005rem;background:var(--bg-card);border:1px solid var(--line);border-radius:10px;overflow:hidden}
.unit-table th{background:var(--bg);text-align:left;padding:8px 10px;font-size:0.885rem;text-transform:uppercase;color:var(--ink-soft)}
.unit-table td{padding:9px 10px;border-top:1px solid var(--line)}
.unit-table th:nth-child(1),.unit-table th:nth-child(2),.unit-table th:nth-child(3),
.unit-table td:nth-child(1),.unit-table td:nth-child(2),.unit-table td:nth-child(3){text-align:center}
.detail-facts{display:grid;grid-template-columns:1fr 1fr;gap:10px 16px;align-content:start}
.fact{font-size:1.005rem}
.fact .k{color:var(--ink-soft);font-size:0.925rem;text-transform:uppercase;letter-spacing:.03em;margin-bottom:2px}
.fact .v{font-weight:600;white-space:pre-line}
.detail-notes{grid-column:1/-1;font-size:1.005rem;color:var(--ink-soft);background:var(--bg-card);border:1px solid var(--line);border-radius:10px;padding:12px 14px;margin-top:4px}
.detail-map{grid-column:1/-1;margin-top:4px}
.detail-map iframe{display:block;width:100%;border-radius:12px;border:1px solid var(--line);filter:grayscale(.15) contrast(1.02)}
body.dark .detail-map iframe{filter:invert(90%) hue-rotate(180deg) grayscale(.2) contrast(.92)}
.detail-map .map-link{display:inline-block;margin-top:8px;font-size:0.945rem;font-weight:700;color:var(--gold-dark);text-decoration:none}
.detail-map .map-link:hover{text-decoration:underline}
body.dark .detail-map .map-link{color:#e3bd77}
.row-actions{grid-column:1/-1;display:flex;gap:10px;margin-top:6px}

/* MOBILE CARDS */
.mobile-cards{display:none}
.pcard{background:var(--bg-card);border:1px solid var(--line);border-radius:var(--radius);padding:16px;margin-bottom:12px}
.pcard-top{display:flex;justify-content:space-between;align-items:flex-start;gap:10px}
.pcard-title{font-weight:700;font-size:1.175rem}
.pcard-loc{font-size:0.995rem;color:var(--ink-soft);margin-top:2px}
.pcard-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px;font-size:1.005rem}
.pcard-grid .k{color:var(--ink-soft);font-size:0.905rem;text-transform:uppercase}
.pcard-foot{display:flex;justify-content:space-between;align-items:center;margin-top:12px;padding-top:12px;border-top:1px solid var(--line)}

/* EMPTY STATE */
.empty-state{text-align:center;padding:60px 20px;color:var(--ink-soft)}
.empty-state .em{font-size:2.525rem;margin-bottom:10px}


/* BOTTOM TRAYS (shortlist + compare) - both live inside one fixed-position
   wrapper so they stack cleanly if a visitor has items in both at once,
   instead of two independently-fixed bars fighting over the same screen
   edge. Each tray collapses via max-height (not translateY) so a hidden
   tray takes up no space in the flex column - no gap left behind. */
.bottom-trays{position:fixed;left:0;right:0;bottom:0;z-index:70;display:flex;flex-direction:column}
.tray{max-height:0;overflow:hidden;transition:max-height .25s ease;background:#211c13;color:#fff;box-shadow:0 -8px 30px rgba(0,0,0,.35)}
.tray.show{max-height:140px}
.tray-inner{max-width:1240px;margin:0 auto;display:flex;align-items:center;gap:14px;flex-wrap:wrap;padding:14px 20px}
.tray-label{font-weight:700;font-size:1.005rem;white-space:nowrap}
.cmp-chips,.fav-chips{display:flex;gap:8px;flex-wrap:wrap;flex:1}
.cmp-chip,.fav-chip{background:rgba(255,255,255,.12);padding:6px 10px 6px 12px;border-radius:99px;font-size:0.995rem;display:flex;align-items:center;gap:6px}
.cmp-chip button,.fav-chip button{background:none;border:none;color:#fff;opacity:.6;cursor:pointer;font-size:1.025rem}
.fav-tray{background:#3a2415}

/* TESTIMONIALS */
.testi{padding:50px 0;background:var(--bg-card);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.testi-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.testi-card{background:var(--bg);border:1px solid var(--line);border-radius:14px;padding:20px}
.testi-card .stars{color:var(--gold);margin-bottom:10px}
.testi-card p{font-size:1.085rem;color:var(--ink-soft);margin:0 0 14px;font-style:normal;line-height:1.55}
.testi-who{display:flex;align-items:center;gap:10px}
.testi-avatar{width:36px;height:36px;border-radius:99px;background:var(--gold);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:1.025rem}
.testi-name{font-weight:700;font-size:1.045rem}
.testi-loc{font-size:0.955rem;color:var(--ink-soft)}

/* PHOTO TESTIMONIALS (placeholders until real photos are supplied) */
.testi-photo{padding:50px 0}
.testi-photo-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.testi-photo-card{text-align:center}
.testi-photo-placeholder{aspect-ratio:1;border-radius:14px;background:var(--bg-card);border:1.5px dashed var(--line);display:flex;align-items:center;justify-content:center;font-size:2.125rem;color:var(--ink-soft);margin-bottom:10px;overflow:hidden}
.testi-photo-placeholder img{width:100%;height:100%;object-fit:cover;object-position:center}
@media(max-width:700px){.testi-photo-grid{grid-template-columns:1fr}}

/* AGENT INTRO (placeholder until Tony's own photo/bio replace it) - a
   single-row layout on desktop so it reads as one calm block, not another
   dense grid competing with the hero above it. Padding is trimmed to a
   firmer, tighter block rather than the looser spacing used earlier -
   still separated from the hero/filters above and below, just not as much
   empty air. object-fit:cover on the actual <img> (once Tony's photo
   replaces the placeholder) keeps it sharp/high-res rather than stretched
   or blurred - just drop in a reasonably high-resolution source photo. */
.about-intro{position:relative;padding:32px 0 36px;border-bottom:1px solid var(--line);overflow:hidden}
.about-intro-inner{position:relative;z-index:1;display:flex;flex-direction:column;align-items:center;text-align:center;gap:18px}
.about-photo-placeholder{width:200px;height:200px;flex:0 0 200px;border-radius:50%;background:var(--bg-card);border:1.5px dashed var(--line);display:flex;align-items:center;justify-content:center;font-size:3.125rem;color:var(--ink-soft);overflow:hidden}
.about-photo-placeholder img{width:100%;height:100%;object-fit:cover;object-position:center}
.about-text{max-width:900px}
.about-text h2{margin:0 0 12px;font-size:1.925rem}
/* Manually broken into 3 lines (see the <br> tags in the markup) rather
   than justified, so the spacing between words stays even - text-align:
   justify would otherwise stretch short forced lines with oversized gaps. */
.about-text p{color:var(--ink-soft);line-height:1.6;margin:0 auto;text-align:center}

/* Dark-mode-only award-photo background: sits behind the profile photo and
   text as a subtle, muted layer inside the existing black band - never
   shown in light mode, where this section stays plain as before. The photo
   itself is pre-darkened/desaturated/warmed in Python before being embedded
   (see about_bg.b64 generation), and these gradients on top add the actual
   fade-to-black vignette so the rectangle never reads as a pasted-in photo. */
body.dark .about-intro::before{
  content:"";position:absolute;inset:0;z-index:0;pointer-events:none;
  background-image:
    radial-gradient(ellipse 88% 110% at 50% 45%, rgba(22,19,13,.08) 0%, rgba(22,19,13,.40) 60%, var(--bg) 100%),
    linear-gradient(to bottom, var(--bg) 0%, rgba(22,19,13,0) 14%, rgba(22,19,13,0) 86%, var(--bg) 100%),
    url('data:image/jpeg;base64,__ABOUT_BG__');
  background-size:cover;
  background-position:center 55%;
  background-repeat:no-repeat;
  animation:bgSlowZoom 15s ease-in-out infinite alternate;
  will-change:transform;
}
/* Slow "Ken Burns" zoom for both dark-mode photo backgrounds above - subtle
   and continuous rather than scroll-linked (avoids background-attachment:
   fixed, which iOS Safari doesn't support properly). Scaling the ::before
   pseudo-element works cleanly with the section's own overflow:hidden, which
   clips the zoomed edges instead of revealing gaps. Respects
   prefers-reduced-motion so it doesn't run for users who've asked for less
   motion. */
@keyframes bgSlowZoom{0%{transform:scale(1)}100%{transform:scale(1.09)}}
@media(prefers-reduced-motion:reduce){
  body.dark .hero::before,body.dark .about-intro::before,body.dark .bottom-photo-band::before{animation:none}
}
/* Soft ring + shadow lifts the profile photo forward off the busier
   background so it stays the strongest visual element, without moving or
   resizing it. */
body.dark .about-photo-placeholder{box-shadow:0 0 0 4px var(--bg),0 0 0 5px rgba(184,134,47,.4),0 14px 40px rgba(0,0,0,.55)}
/* Subtle glass panel behind the bio text for contrast against the photo -
   deliberately low-opacity/no border so it reads as gentle depth, not a
   visible box. */
body.dark .about-text{background:rgba(15,12,8,.4);backdrop-filter:blur(3px);-webkit-backdrop-filter:blur(3px);border-radius:20px;padding:24px 32px}

/* FOOTER CTA + FOOTER - single shared photo band */
/* final-cta and footer are wrapped together in .bottom-photo-band (see HTML)
   so ONE background image spans "Still deciding..." all the way down to
   "Data compiled...", instead of each section doing its own independent
   background-size:cover crop of the same file (which looked like two
   separate copies of the photo stacked, with a visible seam between them).
   One ::before, sized to the whole wrapper's height, fixes that. */
.final-cta{position:relative;padding:60px 0;text-align:center}
.final-cta h2{position:relative;z-index:1;font-size:2.25rem}
.final-cta p{position:relative;z-index:1;color:var(--ink-soft);max-width:520px;margin:0 auto 24px;font-size:1.125rem}
.final-cta button{position:relative;z-index:1}
footer{position:relative;padding:30px 0 100px;text-align:center;font-size:1.005rem;color:var(--ink-soft);border-top:1px solid var(--line)}
body.dark footer{border-top:none}
footer a{color:var(--gold-dark);font-weight:600;text-decoration:none}
.bottom-photo-band{position:relative;overflow:hidden}
.bottom-photo-band .container{position:relative;z-index:1}
/* Same KL skyline photo + slow zoom as the hero above, reused as a bookend -
   see body.dark .hero::before for the full rationale (brightness/tone
   tuning, why background-attachment:fixed is avoided for iOS). Position
   shifted up from the hero's 40% to 20% so the KLCC twin-tower spires (the
   key landmark) sit fully in frame instead of getting cropped off the top.
   Gradient glows in softly at the very top (near "Still deciding..."),
   stays clear through the CTA and the top of the footer text, then fades
   to the page's dark --bg well before the very bottom so the page still
   closes cleanly instead of the photo cutting off abruptly. */
body.dark .bottom-photo-band::before{
  content:"";position:absolute;inset:0;z-index:0;pointer-events:none;
  background-image:
    linear-gradient(to bottom, var(--bg) 0%, rgba(22,19,13,.55) 6%, rgba(22,19,13,0) 22%, rgba(22,19,13,0) 62%, rgba(22,19,13,.6) 86%, var(--bg) 100%),
    url('data:image/jpeg;base64,__HERO_BG__');
  background-size:cover;
  background-position:center 20%;
  background-repeat:no-repeat;
  animation:bgSlowZoom 15s ease-in-out infinite alternate;
  will-change:transform;
}
body.dark .final-cta h2{text-shadow:0 0 4px rgba(0,0,0,.85),0 0 14px rgba(0,0,0,.65),0 0 28px rgba(0,0,0,.45)}
body.dark .final-cta p{color:#f7f3ea;text-shadow:0 0 3px rgba(0,0,0,.85),0 0 10px rgba(0,0,0,.7),0 0 20px rgba(0,0,0,.5)}
body.dark footer{color:#e8ddc8;text-shadow:0 0 3px rgba(0,0,0,.85),0 0 10px rgba(0,0,0,.7),0 0 20px rgba(0,0,0,.5)}
body.dark footer a{color:#e3bd77;text-shadow:0 0 3px rgba(0,0,0,.85),0 0 10px rgba(0,0,0,.7),0 0 20px rgba(0,0,0,.5)}

/* STICKY MOBILE CTA */
.sticky-cta{position:fixed;bottom:0;left:0;right:0;z-index:65;background:var(--bg-card);border-top:1px solid var(--line);padding:10px 16px;display:none;gap:10px;box-shadow:0 -6px 20px rgba(0,0,0,.06)}
.sticky-cta .btn{flex:1}

/* MODAL */
.modal-overlay{position:fixed;inset:0;background:rgba(15,26,20,.55);z-index:100;display:none;align-items:center;justify-content:center;padding:16px}
.modal-overlay.show{display:flex}
.modal{background:var(--bg-card);border-radius:20px;max-width:440px;width:100%;max-height:90vh;overflow-y:auto;padding:26px;position:relative}
.modal-close{position:absolute;top:16px;right:16px;background:var(--bg);color:var(--ink);border:none;width:32px;height:32px;border-radius:99px;cursor:pointer;font-size:1.125rem}
.modal h3{font-size:1.425rem;margin-bottom:6px}
.modal p.sub{color:var(--ink-soft);font-size:1.045rem;margin-bottom:18px}
.form-group{margin-bottom:14px}
.form-group label{display:block;font-size:0.995rem;font-weight:600;margin-bottom:6px}
.form-group input,.form-group select{width:100%;padding:11px 14px;border-radius:10px;border:1.5px solid var(--line);font-size:1.045rem;background:var(--bg);color:var(--ink)}
.form-group input:focus,.form-group select:focus{outline:none;border-color:var(--gold)}
.seg-group{display:flex;gap:8px}
.seg-btn{flex:1;padding:11px;border-radius:10px;border:1.5px solid var(--line);background:var(--bg);text-align:center;cursor:pointer;font-size:1.025rem;font-weight:600}
.seg-btn.active{border-color:var(--gold);background:var(--gold-light);color:var(--gold-dark)}
.err{color:var(--red);font-size:0.945rem;margin-top:4px;display:none}
.modal-foot{font-size:0.925rem;color:var(--ink-soft);text-align:center;margin-top:14px}
.success-view{text-align:center;padding:16px 0}
.success-view .ico{width:60px;height:60px;border-radius:99px;background:var(--gold-light);color:var(--gold-dark);display:flex;align-items:center;justify-content:center;font-size:1.925rem;margin:0 auto 16px}

/* compare modal */
.cmp-modal{max-width:960px}
.cmp-modal-table{width:100%;border-collapse:collapse;font-size:1.025rem}
.cmp-modal-table th,.cmp-modal-table td{padding:10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
/* Not sticky: position:sticky on individual table cells combined with
   border-collapse (used on this table) is unreliable across browsers and
   caused the header/label column to visually overlap the wrong row - same
   class of bug as the main comparison table's header, fixed the same way. */
.cmp-modal-table th:first-child,.cmp-modal-table td:first-child{background:var(--bg-card);font-weight:600;color:var(--ink-soft);font-size:0.925rem;text-transform:uppercase}

@media(max-width:900px){
  .verdict-grid{grid-template-columns:repeat(2,1fr)}
  .hero-stats{grid-template-columns:repeat(3,1fr)}
  .testi-grid{grid-template-columns:1fr}
  .table-wrap{display:none}
  .mobile-cards{display:block}
  .sticky-cta{display:flex}
  .expand-inner{grid-template-columns:1fr}
  /* Mobile cards render the expand block as a plain sibling <div> (not a
     table row like desktop), so it needs its own card-like framing to read
     as "attached to the card above it" rather than a bare, unstyled block. */
  .mobile-cards .expand-inner{background:var(--bg-card);border:1px solid var(--line);border-radius:var(--radius);margin:-4px 0 12px}
  body{padding-bottom:76px}
  /* Keep the shortlist/compare trays from sitting on top of the sticky
     mobile CTA bar - both are fixed to the bottom edge, so nudge the trays
     up by roughly the CTA bar's height instead of letting them overlap. */
  .bottom-trays{margin-bottom:64px}
}
"""

JS = r"""
const WHATSAPP_NUMBER = "601113207364";

// ============================================================
// LIVE SYNC CONFIG
// Set SHEET_ID to your Google Sheet's ID (the long string in its URL).
// The sheet's tab (gid) with the main PROJECT/LOCATION/... table must be
// shared as "Anyone with the link - Viewer" for this to work in visitors'
// browsers. If the sheet is private, this silently falls back to the
// cached snapshot below.
// ============================================================
const SHEET_ID = "1Bk8zmJ9g1DvH5CntuksOkJNIIB4Aln0GFtQ4H9x0Dtc";
const SHEET_GID = "0";
const SHEET_CSV_URL = `https://docs.google.com/spreadsheets/d/${SHEET_ID}/export?format=csv&gid=${SHEET_GID}`;

// Cached snapshot, baked in at build time. Used instantly on load, and as a
// fallback if the live sheet can't be reached.
const STATIC_PROJECTS = __PROJECTS_DATA__;
let PROJECTS = STATIC_PROJECTS;
let dataSource = "cached"; // "cached" | "live"
let lastSyncAt = null;

function fmtRM(n){
  if(!n) return "TBC";
  if(n>=1000000) return "RM"+(n/1000000).toFixed(2).replace(/\.00$/,'')+"mil";
  return "RM"+Math.round(n/1000)+"k";
}
function fmtPSF(n){ return n ? "RM"+Math.round(n) : "—"; }

const BUDGET_BUCKETS = [
  {key:'300-500', label:'RM300k – RM500k', min:300000, max:500000},
  {key:'500-700', label:'RM500k – RM700k', min:500000, max:700000},
  {key:'700-1000', label:'RM700k – RM1mil', min:700000, max:1000000},
  {key:'1000-plus', label:'RM1mil & above', min:1000000, max:Infinity},
];
// Layout Size (sft) buckets - same pattern as BUDGET_BUCKETS, but matched
// against a unit's own sft number (via csvParseSize) instead of its price.
const SIZE_BUCKETS = [
  {key:'300-600', label:'300 – 600 sft', min:300, max:600},
  {key:'600-900', label:'600 – 900 sft', min:600, max:900},
  {key:'900-1200', label:'900 – 1200 sft', min:900, max:1200},
  {key:'1200-1500', label:'1200 – 1500 sft', min:1200, max:1500},
  {key:'1500-plus', label:'1500 sft & above', min:1500, max:Infinity},
];
let state = {
  search:"", areas:[], tenure:"All", sort:"price-asc", favOnly:false,
  budgetRanges:[],
  rooms:[], pet:"Any", completion:[], title:"Any", sizeRanges:[],
  compare: JSON.parse(localStorage.getItem('kl_compare')||'[]'),
  fav: JSON.parse(localStorage.getItem('kl_fav')||'[]'),
  expanded: null
};

// Sheet cells for TITLE come through with inconsistent spacing ("Commercial
// under HDA" vs "Commercial  under HDA"), so bucket into one of a fixed set
// of categories rather than matching the raw string. "Commercial under HDA"
// is titled/packaged for buyers like a residential unit, so it buckets with
// Residential, not plain Commercial - matches how Tony's clients shop for it.
function titleCategory(raw){
  const t = (raw||'').toLowerCase().replace(/\s+/g,' ').trim();
  if(!t) return '';
  if(t.includes('commercial') && t.includes('hda')) return 'Residential';
  if(t.includes('commercial')) return 'Commercial';
  if(t.includes('residential')) return 'Residential';
  return raw;
}

// Generic toggle for the multi-select tile/tick filters (area, rooms, completion).
// Only updates the chip's own visual state + `state` - it deliberately does
// NOT re-render the results table. Clients build up their full set of
// preferences first, then click the "Filter" button (applyFilters()) to
// apply everything at once, rather than the table jumping around after
// every single tap.
function toggleArrayFilter(field, value){
  const arr = state[field];
  const i = arr.indexOf(value);
  if(i>-1) arr.splice(i,1); else arr.push(value);
  if(field==='areas'){
    renderAreaTiles();
  }
  if(field==='rooms') renderRoomTicks();
  if(field==='completion') renderCompletionTicks();
  if(field==='sizeRanges') renderSizeTicks();
  markFiltersPending();
}

function saveState(){
  localStorage.setItem('kl_compare', JSON.stringify(state.compare));
  localStorage.setItem('kl_fav', JSON.stringify(state.fav));
}

// ---------- derived data (recomputed whenever PROJECTS changes) ----------
let areaCounts = {}, areaList = [], withPrice = [], minPrice = 0, medPrice = 0, maxPrice = 0, minPsf = 0;

function parseVpSort(p){
  const m = (p.vpDate||"").match(/(20\d{2})/);
  const y = m? parseInt(m[1]) : 9999;
  const q = (p.vpDate||"").match(/Q(\d)/i);
  return y*10 + (q?parseInt(q[1]):5);
}
function getVpYear(p){
  const m = (p.vpDate||"").match(/(20\d{2})/);
  return m ? parseInt(m[1]) : null;
}
// Room count from a unit's size string, using only the base bedroom number -
// the "+1"/"+2" study/utility room is a bonus space, not counted as a full
// room for filtering purposes. E.g. "872 sft (2+1R, 2B)" -> 2,
// "1012 sft (3+1R, 2B)" -> 3, "700 sft (2R, 2B)" -> 2.
// Studio layouts (e.g. "474 sft (Studio)") have no bedroom number at all -
// treated as 0 rooms so they can be matched by the dedicated "Studio" filter.
function parseRooms(sizeStr){
  if(!sizeStr) return null;
  if(/studio/i.test(sizeStr)) return 0;
  const m = sizeStr.match(/(\d+)\s*\+?\s*(\d+)?\s*R\b/i);
  if(!m) return null;
  return parseInt(m[1]);
}

function median(nums){
  if(!nums.length) return 0;
  const sorted = nums.slice().sort((a,b)=>a-b);
  const mid = Math.floor(sorted.length/2);
  return sorted.length % 2 ? sorted[mid] : (sorted[mid-1]+sorted[mid])/2;
}

// Groups every PJ / Damansara-area location (PJ Damansara, Ara Damansara,
// Kwasa Damansara, PJ Seksyen 13/14, etc.) under one standardised "PJ" tile
// for filtering, instead of splitting them into near-duplicate area chips.
// The project's own row/detail still shows its exact original location.
function areaGroup(location){
  const l = (location||'');
  if(/\bpj\b|damansara/i.test(l)) return 'Petaling Jaya';
  return l;
}

function computeDerived(){
  areaCounts = {};
  PROJECTS.forEach(p=>{ const g = areaGroup(p.location); areaCounts[g] = (areaCounts[g]||0)+1; });
  areaList = Object.keys(areaCounts).sort((a,b)=>areaCounts[b]-areaCounts[a]);
  withPrice = PROJECTS.filter(p=>p.priceFrom>0);
  const priceList = withPrice.map(p=>p.priceFrom);
  minPrice = priceList.length ? Math.min(...priceList) : 0;
  medPrice = median(priceList);
  // "Highest Price" spans the full unit range per project (not just each project's
  // starting/entry price), so a project like Oaka - entry RM799k but units up to RM1.27mil -
  // is reflected correctly instead of being capped at its own "from" price.
  const allUnitPrices = [];
  PROJECTS.forEach(p=>{ (p.units||[]).forEach(u=>{ if(u && u.priceNum>0) allUnitPrices.push(u.priceNum); }); });
  maxPrice = allUnitPrices.length ? Math.max(...allUnitPrices) : (priceList.length ? Math.max(...priceList) : 0);
  const psfList = withPrice.filter(p=>p.psfFrom>0).map(p=>p.psfFrom);
  minPsf = psfList.length ? Math.min(...psfList) : 0;
}

// ---------- render: hero stats ----------
function renderStats(){
  document.getElementById('statProjects').textContent = PROJECTS.length;
  document.getElementById('statPrice').textContent = fmtRM(minPrice);
  document.getElementById('statMedPrice').textContent = fmtRM(medPrice);
  document.getElementById('statMaxPrice').textContent = fmtRM(maxPrice);
  document.getElementById('statAreas').textContent = areaList.length;
}

// ---------- render: quick verdict ----------
// These are the projects buyers actually ask about most often. Fixed
// picks (not auto-computed from price/PSF) with an approximate share of
// enquiries - update the percentages below whenever the mix changes.
const POPULAR_PICKS = [
  { name: 'Queenswoodz', share: 18 },
  { name: 'Vividz', share: 16 },
  { name: 'Aurum Suites', share: 14 },
  { name: 'The Atera (Phase 2)', share: 12 },
];
function renderVerdict(){
  const cards = POPULAR_PICKS
    .map(pick => ({ pick, p: PROJECTS.find(x=>x.name===pick.name) }))
    .filter(c => c.p);
  if(!cards.length){ document.getElementById('verdictGrid').innerHTML = ''; return; }
  document.getElementById('verdictGrid').innerHTML = cards.map(({pick,p})=>`
    <div class="verdict-card" onclick="jumpToProject('${esc(p.name)}')">
      <div class="verdict-icon">👥</div>
      <div class="tag">Most Popular Pick</div>
      <div class="proj">${p.name}</div>
      <div class="meta">${p.location} · From ${p.priceFrom ? fmtRM(p.priceFrom) : 'TBC'}</div>
      <div class="value">~${pick.share}% of enquiries</div>
    </div>`).join('');
}

// ---------- render: area tiles (multi-select, rectangular, tick when active) ----------
// Area doubles as the "browse by area" experience, so it comes first in the
// filter section and shows project count + starting price per area, like a
// mini area card, rather than a plain pill.
function renderAreaTiles(){
  document.getElementById('areaChips').innerHTML = areaList.map(a=>{
    const active = state.areas.includes(a);
    const projs = PROJECTS.filter(p=>areaGroup(p.location)===a && p.priceFrom>0);
    const lo = projs.length ? Math.min(...projs.map(p=>p.priceFrom)) : 0;
    return `<button class="area-tile ${active?'active':''}" onclick="toggleArrayFilter('areas','${esc(a)}')">
      ${active?'<span class="tile-tick">✓</span>':''}
      <div class="tile-name">${a}</div>
      <div class="tile-meta">${areaCounts[a]} project${areaCounts[a]>1?'s':''} · ${lo? 'From '+fmtRM(lo) : 'TBC'}</div>
    </button>`;
  }).join('');
}

// ---------- render: rooms / completion (multi-select tick chips) ----------
function renderRoomTicks(){
  const opts = [['0','Studio'],['1','1 room'],['2','2 rooms'],['3','3 rooms'],['4','4 rooms'],['5','5+ rooms'],['dk','Dual Key']];
  document.getElementById('roomsTicks').innerHTML = opts.map(([val,label])=>{
    const active = state.rooms.includes(val);
    return `<button class="chip ${active?'active':''}" onclick="toggleArrayFilter('rooms','${val}')">${active?'✓ ':''}${label}</button>`;
  }).join('');
}
function renderCompletionTicks(){
  const opts = [['Ready','Ready / Move-in'],['2026','2026'],['2027','2027'],['2028','2028'],['2029','2029'],['2030','2030'],['2031','2031']];
  document.getElementById('completionTicks').innerHTML = opts.map(([val,label])=>{
    const active = state.completion.includes(val);
    return `<button class="chip ${active?'active':''}" onclick="toggleArrayFilter('completion','${val}')">${active?'✓ ':''}${label}</button>`;
  }).join('');
}

// ---------- budget range (multi-select tick chips, same pattern as rooms/completion) ----------
function fmtBudgetLabel(n){
  if(n>=1000000) return 'RM'+(n/1000000).toFixed(1).replace(/\.0$/,'')+'mil';
  return 'RM'+Math.round(n/1000)+'K';
}
function renderBudgetTicks(){
  document.getElementById('budgetTicks').innerHTML = BUDGET_BUCKETS.map(b=>{
    const active = state.budgetRanges.includes(b.key);
    return `<button class="chip ${active?'active':''}" onclick="toggleBudgetRange('${b.key}')">${active?'✓ ':''}${b.label}</button>`;
  }).join('');
}
// Layout Size (sft): plain independent multi-select (no contiguous-range
// requirement like Budget above) - a client can pick any combination of
// size buckets, matching the Rooms/Completion chip pattern instead.
function renderSizeTicks(){
  document.getElementById('sizeTicks').innerHTML = SIZE_BUCKETS.map(b=>{
    const active = state.sizeRanges.includes(b.key);
    return `<button class="chip ${active?'active':''}" onclick="toggleArrayFilter('sizeRanges','${b.key}')">${active?'✓ ':''}${b.label}</button>`;
  }).join('');
}
// Budget buckets must stay a single contiguous block (e.g. 300-500 + 500-700
// is fine, but 300-500 + 1mil-above skipping the two middle buckets is not)
// - picking a non-adjacent bucket is a silent no-op rather than an error,
// since jumping straight to "1mil & above" from "300-500" doesn't actually
// mean anything as a budget range.
function toggleBudgetRange(key){
  const idx = BUDGET_BUCKETS.findIndex(b=>b.key===key);
  const selectedIdx = state.budgetRanges.map(k=>BUDGET_BUCKETS.findIndex(b=>b.key===k)).sort((a,b)=>a-b);
  if(selectedIdx.length===0){
    state.budgetRanges = [key];
  } else {
    const lo = selectedIdx[0], hi = selectedIdx[selectedIdx.length-1];
    if(idx>=lo && idx<=hi){
      // already selected - only the two ends can be removed, trimming the range inward
      if(lo===hi) state.budgetRanges = [];
      else if(idx===lo) state.budgetRanges = BUDGET_BUCKETS.slice(lo+1, hi+1).map(b=>b.key);
      else if(idx===hi) state.budgetRanges = BUDGET_BUCKETS.slice(lo, hi).map(b=>b.key);
      // clicking a selected bucket in the middle of the range does nothing
    } else if(idx===lo-1 || idx===hi+1){
      // directly adjacent - extend the range by one
      const newLo = Math.min(lo, idx), newHi = Math.max(hi, idx);
      state.budgetRanges = BUDGET_BUCKETS.slice(newLo, newHi+1).map(b=>b.key);
    }
    // any other bucket is a "jump" over unselected ones in between - ignored
  }
  renderBudgetTicks();
  markFiltersPending();
}

// ---------- filtering/sorting ----------
function getFiltered(){
  let list = PROJECTS.filter(p=>{
    if(state.areas.length && !state.areas.includes(areaGroup(p.location))) return false;
    if(state.tenure!=='All' && !p.tenure.startsWith(state.tenure)) return false;
    if(state.search){
      const s = state.search.toLowerCase();
      if(!(p.name.toLowerCase().includes(s) || p.location.toLowerCase().includes(s) || p.developer.toLowerCase().includes(s))) return false;
    }
    if(state.favOnly && !state.fav.includes(p.name)) return false;
    // Budget + Rooms + Layout Size: only applied once at least one is
    // selected. Checked together against the SAME unit, not as independent
    // "some unit matches budget" / "some other unit matches rooms" / "some
    // other unit matches size" checks - otherwise a project could pass all
    // three filters purely because different units each satisfy one pick,
    // even though no single unit actually meets every pick at once. A
    // client who picks "RM500k-700k" + "3 rooms" + "900-1200 sft" wants a
    // unit that is a 3-room, 900-1200sft unit priced RM500k-700k, all at
    // the same time.
    // Checks every UNIT's price, not just the project's cheapest (priceFrom)
    // - otherwise a project with a wide price spread (e.g. a cheap sold-out
    // studio dragging priceFrom down) would wrongly disappear from a budget
    // search for its pricier units, even though those units genuinely fall
    // inside the selected range.
    if(state.budgetRanges.length || state.rooms.length || state.sizeRanges.length){
      const matches = (p.units||[]).some(u=>{
        if(state.budgetRanges.length){
          if(!u.priceNum) return false;
          const inBudget = state.budgetRanges.some(key=>{
            const b = BUDGET_BUCKETS.find(x=>x.key===key);
            return b && u.priceNum >= b.min && u.priceNum < b.max;
          });
          if(!inBudget) return false;
        }
        if(state.rooms.length){
          const r = parseRooms(u.size);
          // "Dual Key" is a layout tag inside the free-text size/layout string
          // (e.g. "1527 sft (4R, 3B, Dual key)"), not a room count, so it's
          // checked independently of parseRooms rather than folded into the
          // numeric r===parseInt(sel) comparison below.
          const isDualKey = /dual\s*key/i.test(u.size);
          const roomsOk = state.rooms.some(sel => {
            if(sel==='dk') return isDualKey;
            if(r==null) return false;
            return sel==='5' ? r>=5 : r===parseInt(sel);
          });
          if(!roomsOk) return false;
        }
        if(state.sizeRanges.length){
          const sft = csvParseSize(u.size, 'min');
          if(sft==null) return false;
          const sizeOk = state.sizeRanges.some(key=>{
            const b = SIZE_BUCKETS.find(x=>x.key===key);
            return b && sft >= b.min && sft < b.max;
          });
          if(!sizeOk) return false;
        }
        return true;
      });
      if(!matches) return false;
    }
    if(state.pet !== 'Any'){
      if((p.petFriendly||'').toLowerCase() !== state.pet.toLowerCase()) return false;
    }
    if(state.completion.length){
      const y = getVpYear(p);
      const matches = state.completion.some(sel=>{
        if(sel==='Ready') return /ready|move[\s-]?in/i.test(p.vpDate||"");
        return y === parseInt(sel);
      });
      if(!matches) return false;
    }
    if(state.title !== 'Any' && titleCategory(p.title) !== state.title) return false;
    return true;
  });
  const sorters = {
    'price-asc': (a,b)=> (a.priceFrom||9e9) - (b.priceFrom||9e9),
    'price-desc': (a,b)=> (b.priceFrom||0) - (a.priceFrom||0),
    'psf-asc': (a,b)=> (a.psfFrom||9e9) - (b.psfFrom||9e9),
    'vp-asc': (a,b)=> parseVpSort(a) - parseVpSort(b),
    'name-asc': (a,b)=> a.name.localeCompare(b.name),
  };
  list.sort(sorters[state.sort] || sorters['price-asc']);
  return list;
}

function statusBadge(p){
  const sold = p.units.some(u=>/sold out/i.test(u.status)) && p.units.every(u=>/sold out/i.test(u.status));
  if(!p.priceFrom) return '<span class="badge badge-tbc">Coming Soon</span>';
  if(sold) return '<span class="badge badge-sold">Sold Out</span>';
  return '<span class="badge badge-avail">Available</span>';
}

function renderTable(){
  const list = getFiltered();
  document.getElementById('resultsCount').textContent = `Showing ${list.length} of ${PROJECTS.length} projects`;
  const tbody = document.getElementById('tableBody');
  const cards = document.getElementById('mobileCards');
  if(list.length===0){
    tbody.innerHTML = `<tr><td colspan="8"><div class="empty-state"><div class="em">🔍</div>No projects match your filters.<br><button class="btn btn-outline btn-sm" style="margin-top:12px" onclick="resetFilters()">Reset filters</button></div></td></tr>`;
    cards.innerHTML = `<div class="empty-state"><div class="em">🔍</div>No projects match your filters.<br><button class="btn btn-outline btn-sm" style="margin-top:12px" onclick="resetFilters()">Reset filters</button></div>`;
    return;
  }
  tbody.innerHTML = list.map(p=>rowHTML(p)).join('');
  cards.innerHTML = list.map(p=>cardHTML(p)).join('');
}

// Toggling any preference chip/dropdown queues a change without touching
// the results table - this lights up the Filter button so it's clear a
// click is needed to see the updated matches.
function markFiltersPending(){
  document.getElementById('applyFiltersBtn')?.classList.add('pending');
}
// Applies whatever's currently picked (area/budget/rooms/completion/title/
// tenure/pet all live in `state` already - toggling them just didn't
// re-render) and scrolls the client down to their matches.
function applyFilters(){
  document.getElementById('applyFiltersBtn')?.classList.remove('pending');
  renderTable();
  document.getElementById('table')?.scrollIntoView({behavior:'smooth', block:'start'});
}

function resetFilters(){
  state = {...state, search:'', areas:[], tenure:'All', budgetRanges:[], rooms:[], pet:'Any', completion:[], title:'Any', sizeRanges:[]};
  document.getElementById('searchInput').value='';
  document.getElementById('tenureSelect').value='All';
  document.getElementById('petSelect').value='Any';
  document.getElementById('titleSelect').value='Any';
  document.getElementById('applyFiltersBtn')?.classList.remove('pending');
  renderAreaTiles(); renderRoomTicks(); renderCompletionTicks(); renderBudgetTicks(); renderSizeTicks(); renderTable();
}

function rowHTML(p){
  const isFav = state.fav.includes(p.name);
  const inCmp = state.compare.includes(p.name);
  const isOpen = state.expanded === p.name;
  return `
  <tr onclick="toggleExpand('${esc(p.name)}')" id="row-${escId(p.name)}">
    <td onclick="event.stopPropagation()"><input type="checkbox" class="cmp-check" ${inCmp?'checked':''} ${!inCmp && state.compare.length>=4?'disabled':''} onchange="toggleCompare('${esc(p.name)}')"></td>
    <td class="proj-cell">
      <div class="proj-name">
        <button class="fav-btn ${isFav?'active':''} ${favPulseClass(isFav)}" onclick="event.stopPropagation();toggleFav('${esc(p.name)}')" title="${isFav?'Remove from':'Add to'} Shortlist" aria-label="${isFav?'Remove from':'Add to'} Shortlist">${isFav?'❤️':'🤍'}</button>
        ${p.name}
      </div>
      <div class="proj-loc">📍 ${p.location}</div>
      <div class="proj-dev">Developer: ${p.developer}</div>
    </td>
    <td class="price-cell"><div class="from">from</div><div class="num">${fmtRM(p.priceFrom)}</div></td>
    <td>${fmtPSF(p.psfFrom)}</td>
    <td>${p.tenure||'TBC'}</td>
    <td>${p.sizeMin? Math.round(p.sizeMin)+' – '+Math.round(p.sizeMax) : 'TBC'}</td>
    <td>${p.vpDate}</td>
    <td>${statusBadge(p)}</td>
  </tr>
  <tr class="expand-row"><td colspan="8" style="padding:0">
    <div class="expand-inner ${isOpen?'open':''}" id="exp-${escId(p.name)}">
      ${expandContent(p)}
    </div>
  </td></tr>`;
}

// No API key required: Google Maps' plain "?q=...&output=embed" URL scheme
// renders a free embeddable map for a text search query. Precision depends
// on what Google can geocode from the text - an explicit ADDRESS column in
// the sheet (optional) will always win for pinpoint accuracy; otherwise we
// fall back to "<project name>, <location>, Kuala Lumpur, Malaysia", which
// resolves correctly for the vast majority of named developments.
function mapQuery(p){
  return p.address || (p.name + ', ' + p.location + ', Kuala Lumpur, Malaysia');
}
function mapEmbedSrc(p){
  return 'https://www.google.com/maps?q=' + encodeURIComponent(mapQuery(p)) + '&output=embed';
}
function mapLinkHref(p){
  return 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(mapQuery(p));
}

function expandContent(p){
  const unitsRows = (p.units||[]).filter(u=>u.size).map(u=>`
    <tr><td>${u.size}</td><td>${u.price}</td><td>${u.psf}</td><td>${u.status? '<span class="badge badge-sold">'+u.status+'</span>':'<span class="badge badge-avail">Available</span>'}</td></tr>
  `).join('');
  return `
    <div>
      <table class="unit-table">
        <thead><tr><th>Size & Layout</th><th>Price</th><th>PSF</th><th>Status</th></tr></thead>
        <tbody>${unitsRows || '<tr><td colspan="4">Details coming soon</td></tr>'}</tbody>
      </table>
    </div>
    <div class="detail-facts">
      <div class="fact"><div class="k">Title</div><div class="v">${p.title||'TBC'}</div></div>
      <div class="fact"><div class="k">Number of Units</div><div class="v">${p.numUnits||'TBC'}</div></div>
      <div class="fact"><div class="k">Land Size</div><div class="v">${p.landSize||'TBC'}</div></div>
      <div class="fact"><div class="k">Units / Floor</div><div class="v">${p.unitsPerFloor||'TBC'}</div></div>
      <div class="fact"><div class="k">Lifts / Floor</div><div class="v">${p.liftsPerFloor||'TBC'}</div></div>
      <div class="fact"><div class="k">Pet Friendly</div><div class="v">${p.petFriendly||'TBC'}</div></div>
      <div class="fact"><div class="k">Maintenance</div><div class="v">${p.maintFee? p.maintFee+' / sft':'TBC'}</div></div>
      <div class="fact"><div class="k">Car Parks</div><div class="v">${p.carParks||'TBC'}</div></div>
      <div class="fact"><div class="k">Legal Fee</div><div class="v">${p.legalFee||'TBC'}</div></div>
      <div class="fact"><div class="k">VP Date</div><div class="v">${p.vpDate}</div></div>
    </div>
    ${p.details? `<div class="detail-notes"><strong>Project details:</strong> ${p.details}</div>` : ''}
    <div class="detail-map">
      <iframe src="${mapEmbedSrc(p)}" width="100%" height="220" style="border:0" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Map location for ${esc(p.name)}"></iframe>
      <a class="map-link" href="${mapLinkHref(p)}" target="_blank" rel="noopener">📍 Open in Google Maps</a>
    </div>
    <div class="row-actions">
      <button class="btn btn-primary btn-sm" onclick="requestBrochure('${esc(p.name)}')">📄 Request E-Brochure</button>
      <button class="btn btn-outline btn-sm" onclick="toggleCompare('${esc(p.name)}')">${state.compare.includes(p.name)?'Remove from Compare':'+ Add to Compare'}</button>
    </div>
  `;
}

function esc(s){ return (s||'').replace(/'/g,"\\'"); }

function cardHTML(p){
  const isFav = state.fav.includes(p.name);
  const isOpen = state.expanded === p.name;
  return `
  <div class="pcard" id="card-${escId(p.name)}" onclick="openDetail('${esc(p.name)}')">
    <div class="pcard-top">
      <div>
        <div class="pcard-title">${p.name}</div>
        <div class="pcard-loc">📍 ${p.location} · Developer: ${p.developer}</div>
      </div>
      <button class="fav-btn ${isFav?'active':''} ${favPulseClass(isFav)}" onclick="event.stopPropagation();toggleFav('${esc(p.name)}');renderTable()" title="${isFav?'Remove from':'Add to'} Shortlist" aria-label="${isFav?'Remove from':'Add to'} Shortlist">${isFav?'❤️':'🤍'}</button>
    </div>
    <div class="pcard-grid">
      <div><div class="k">From</div><strong>${fmtRM(p.priceFrom)}</strong></div>
      <div><div class="k">PSF</div><strong>${fmtPSF(p.psfFrom)}</strong></div>
      <div><div class="k">Tenure</div><strong>${p.tenure||'TBC'}</strong></div>
      <div><div class="k">Completion</div><strong>${p.vpDate}</strong></div>
    </div>
    <div class="pcard-foot">
      ${statusBadge(p)}
      <button class="btn btn-outline btn-sm" onclick="event.stopPropagation();openLead('${esc(p.name)}')">Enquire</button>
    </div>
  </div>
  <div class="expand-inner ${isOpen?'open':''}" id="exp-mobile-${escId(p.name)}" onclick="event.stopPropagation()">
    ${expandContent(p)}
  </div>`;
}

function toggleExpand(name){
  state.expanded = state.expanded === name ? null : name;
  if(state.expanded === name && typeof gtag === 'function') gtag('event', 'view_project', {project_name: name});
  renderTable();
}
// esc() escapes apostrophes for use inside onclick='...' JS string literals.
// IDs need their own, simpler escaping (apostrophes just stripped) so that
// id="row-${escId(name)}" and getElementById('row-'+escId(name)) always
// agree - names like "D'Tessera" would otherwise produce mismatched IDs.
function escId(s){ return (s||'').replace(/'/g,''); }

// Returns 'pulse-hint' for a heart icon that hasn't been shortlisted yet,
// as long as this visitor has never shortlisted anything before - gives
// first-time visitors a clear, moving cue for what to tap, without
// pulsing hearts that are already active or nagging returning visitors.
function favPulseClass(isFav){
  return (!isFav && localStorage.getItem('kl_fav_intro_seen')!=='1') ? 'pulse-hint' : '';
}
function toggleFav(name){
  const i = state.fav.indexOf(name);
  if(i>-1) state.fav.splice(i,1); else { state.fav.push(name); if(typeof gtag === 'function') gtag('event', 'shortlist_project', {project_name: name}); }
  // Once someone has shortlisted anything at all, they've learned what the
  // heart icon does - permanently stop the pulse hint for them from here on.
  localStorage.setItem('kl_fav_intro_seen', '1');
  saveState(); renderTable(); renderFavTray(); updateBadges();
}
function toggleCompare(name){
  const i = state.compare.indexOf(name);
  if(i>-1) state.compare.splice(i,1);
  else { if(state.compare.length>=4){ alert('You can compare up to 4 projects at a time.'); return; } state.compare.push(name); }
  saveState(); renderTable(); renderCompareTray(); updateBadges();
}
function updateBadges(){
  document.getElementById('favBadge').textContent = state.fav.length;
  document.getElementById('favBadge').style.display = state.fav.length? 'flex':'none';
}
function toggleFavOnly(){
  if(state.fav.length===0){ alert('Tap the heart icon on any project to shortlist it first.'); return; }
  state.favOnly = !state.favOnly;
  document.getElementById('favToggleBtn').classList.toggle('active', state.favOnly);
  renderTable();
}

// Sends the visitor's own shortlist (their private, browser-only favourites)
// straight to Tony over WhatsApp - one click, no form, so a client's picks
// actually reach Tony instead of just sitting unseen in their browser.
function sendShortlist(){
  if(state.fav.length===0){ alert('Tap the heart icon on a project first to add it to your shortlist.'); return; }
  if(typeof gtag === 'function') gtag('event', 'send_shortlist', {projects: state.fav.join(', ')});
  const msg = `Hi Tony, I've shortlisted: ${state.fav.join(', ')}. I'd like to explore more.`;
  const waLink = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(msg)}`;
  window.open(waLink, '_blank', 'noopener');
}

function renderCompareTray(){
  const tray = document.getElementById('cmpTray');
  if(state.compare.length===0){ tray.classList.remove('show'); return; }
  tray.classList.add('show');
  document.getElementById('cmpChips').innerHTML = state.compare.map(n=>
    `<div class="cmp-chip">${n}<button onclick="toggleCompare('${esc(n)}')">✕</button></div>`
  ).join('');
  document.getElementById('cmpCount').textContent = state.compare.length;
}

// Mirrors renderCompareTray() - keeps the shortlist visible and editable
// from anywhere on the page (not just via the "show shortlisted only"
// nav toggle), with a one-tap remove per project and the same "Send My
// Shortlist" action already used elsewhere.
function renderFavTray(){
  const tray = document.getElementById('favTray');
  if(state.fav.length===0){ tray.classList.remove('show'); return; }
  tray.classList.add('show');
  document.getElementById('favChips').innerHTML = state.fav.map(n=>
    `<div class="fav-chip">${n}<button onclick="toggleFav('${esc(n)}')">✕</button></div>`
  ).join('');
  document.getElementById('favTrayCount').textContent = state.fav.length;
}

// Opens a project's expanded detail and scrolls right to that row/card,
// rather than just scrolling to the top of the whole table where the
// project in question might be many rows down and easy to miss. Used for
// cards that are already part of the current filtered view (mobile cards).
function expandAndScrollTo(name){
  state.expanded = name;
  renderTable();
  requestAnimationFrame(()=>{
    const isMobile = window.innerWidth <= 900;
    const target = isMobile
      ? document.getElementById('card-'+escId(name))
      : document.getElementById('row-'+escId(name));
    if(target){
      target.scrollIntoView({behavior:'smooth', block:'center'});
    } else {
      document.getElementById('tableBody').closest('.table-wrap')?.scrollIntoView({behavior:'smooth',block:'center'});
    }
  });
}
function openDetail(name){
  expandAndScrollTo(name);
}

// Most Popular Picks are a fixed hand-picked list (see POPULAR_PICKS) that
// may not match whatever filters are currently active - e.g. they're all
// "Commercial under HDA" titled projects, while the Title filter defaults
// to Residential. Without clearing filters first, pressing a pick could
// silently do nothing because its row wouldn't exist in the filtered table.
// So this resets every filter back to "show everything" before expanding
// and scrolling to the picked project, guaranteeing it's actually visible.
function jumpToProject(name){
  state = {...state, search:'', areas:[], tenure:'All', budgetRanges:[], rooms:[], pet:'Any', completion:[], title:'Any', sizeRanges:[]};
  document.getElementById('searchInput').value='';
  document.getElementById('tenureSelect').value='All';
  document.getElementById('petSelect').value='Any';
  document.getElementById('titleSelect').value='Any';
  document.getElementById('applyFiltersBtn')?.classList.remove('pending');
  renderAreaTiles(); renderRoomTicks(); renderCompletionTicks(); renderBudgetTicks(); renderSizeTicks();
  expandAndScrollTo(name);
}

// ---------- compare modal ----------
function openCompareModal(){
  if(state.compare.length<2){ alert('Add at least 2 projects to compare.'); return; }
  const projs = state.compare.map(n=>PROJECTS.find(p=>p.name===n)).filter(Boolean);
  const rows = [
    ['Location', p=>p.location],
    ['Developer', p=>p.developer],
    ['Tenure', p=>p.tenure||'TBC'],
    ['Title', p=>titleCategory(p.title)||'TBC'],
    ['Price From', p=>fmtRM(p.priceFrom)],
    ['PSF From', p=>fmtPSF(p.psfFrom)],
    ['Size Range', p=>p.sizeMin? Math.round(p.sizeMin)+'–'+Math.round(p.sizeMax)+' sft':'TBC'],
    ['Completion', p=>p.vpDate],
    ['Maintenance', p=>p.maintFee? p.maintFee+'/sft':'TBC'],
    ['Car Parks', p=>p.carParks||'TBC'],
    ['Pet Friendly', p=>p.petFriendly||'TBC'],
    ['Legal Fee', p=>p.legalFee||'TBC'],
    ['Status', p=>statusBadge(p)],
  ];
  const html = `
    <table class="cmp-modal-table">
      <thead><tr><th>&nbsp;</th>${projs.map(p=>`<th>${p.name}</th>`).join('')}</tr></thead>
      <tbody>${rows.map(([label,fn])=>`<tr><td>${label}</td>${projs.map(p=>`<td>${fn(p)}</td>`).join('')}</tr>`).join('')}</tbody>
    </table>
    <div style="margin-top:18px;text-align:center">
      <button class="btn btn-primary" id="cmpDiscussBtn">💬 Discuss These With Tony Hoo</button>
    </div>
  `;
  document.getElementById('cmpModalBody').innerHTML = html;
  // Wired up via addEventListener (not an inline onclick string) on purpose:
  // project names can contain an apostrophe (e.g. "D'Evia"), which would
  // otherwise prematurely close the single-quoted JS string built into an
  // onclick="..." attribute and silently break the button for any
  // comparison that includes such a project. Using a real closure over
  // `projs` sidesteps that whole class of quoting bug.
  document.getElementById('cmpDiscussBtn').onclick = function(){
    closeCompareModal();
    openLead('Comparison: ' + projs.map(p=>p.name).join(', '));
  };
  document.getElementById('cmpModalOverlay').classList.add('show');
}
function closeCompareModal(){ document.getElementById('cmpModalOverlay').classList.remove('show'); }

// ---------- one-click whatsapp (no form) ----------
// Builds "Hi Tony, I wish to explore more about X" where X is either the
// specific project/comparison the visitor clicked from, or - if they used
// the general WhatsApp button - whatever filters they currently have set
// (area, tenure, search keyword) so Tony still gets useful context without
// making them fill in anything.
function currentRequirementsSummary(){
  const parts = [];
  if(state.areas.length) parts.push(state.areas.join('/'));
  if(state.tenure && state.tenure!=='All') parts.push(state.tenure);
  if(state.budgetRanges.length){
    parts.push('budget '+state.budgetRanges.map(key=>BUDGET_BUCKETS.find(b=>b.key===key)?.label).filter(Boolean).join(', '));
  }
  if(state.rooms.length){
    const roomLabel = state.rooms.map(r=>r==='0'?'Studio':r==='5'?'5+':r==='dk'?'Dual Key':r).join('/');
    parts.push(roomLabel + (state.rooms.every(r=>r==='0'||r==='dk') ? '' : ' rooms'));
  }
  if(state.sizeRanges.length){
    parts.push('layout size '+state.sizeRanges.map(key=>SIZE_BUCKETS.find(b=>b.key===key)?.label).filter(Boolean).join(', '));
  }
  if(state.pet !== 'Any') parts.push(`pet-friendly: ${state.pet}`);
  if(state.title !== 'Any') parts.push(state.title);
  if(state.completion.length) parts.push(state.completion.map(c=>c==='Ready'?'ready to move in':c).join('/'));
  if(state.search) parts.push(`"${state.search}"`);
  return parts.join(', ');
}
function openLead(context){
  let subject;
  if(context && context!=='General enquiry'){
    subject = context;
  } else {
    const reqs = currentRequirementsSummary();
    subject = reqs ? `new launches matching: ${reqs}` : 'new property launches in Klang Valley';
  }
  if(typeof gtag === 'function') gtag('event', 'click_whatsapp_enquiry', {context: subject});
  const msg = `Hi Tony, I wish to explore more about ${subject}.`;
  const waLink = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(msg)}`;
  window.open(waLink, '_blank', 'noopener');
}

function requestBrochure(name){
  if(typeof gtag === 'function') gtag('event', 'request_brochure', {project_name: name});
  const msg = `Hi Tony, I would like to know more about ${name}, can I request for its e-brochure please?`;
  const waLink = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(msg)}`;
  window.open(waLink, '_blank', 'noopener');
}

// ---------- dark mode ----------
function toggleDark(){
  document.body.classList.toggle('dark');
  localStorage.setItem('kl_dark', document.body.classList.contains('dark')?'1':'0');
}
// Dark mode is the default (set directly on <body> to avoid a light-mode
// flash before this script runs). Only remove it if the visitor previously
// chose light mode explicitly via the toggle.
if(localStorage.getItem('kl_dark')==='0') document.body.classList.remove('dark');

// ---------- CSV live sync ----------
// Minimal RFC4180-ish CSV parser: handles quoted fields with embedded
// commas, newlines and escaped quotes ("").
function parseCSV(text){
  const rows = [];
  let row = [], field = '', inQuotes = false;
  for(let i=0;i<text.length;i++){
    const c = text[i], next = text[i+1];
    if(inQuotes){
      if(c === '"' && next === '"'){ field += '"'; i++; }
      else if(c === '"'){ inQuotes = false; }
      else field += c;
    } else {
      if(c === '"') inQuotes = true;
      else if(c === ','){ row.push(field); field=''; }
      else if(c === '\n'){ row.push(field); rows.push(row); row=[]; field=''; }
      else if(c === '\r'){ /* skip */ }
      else field += c;
    }
  }
  if(field.length || row.length){ row.push(field); rows.push(row); }
  return rows;
}

function csvParsePrice(s){
  if(!s) return null;
  const re = /RM\s?([\d,]+\.?\d*)\s*(k|mil)?/gi;
  let m, vals=[];
  while((m = re.exec(s))){
    let num = parseFloat(m[1].replace(/,/g,''));
    const unit = (m[2]||'').toLowerCase();
    if(unit==='k') num *= 1000; else if(unit==='mil') num *= 1000000;
    vals.push(num);
  }
  return vals.length ? Math.min(...vals) : null;
}
function csvParsePsf(s){
  if(!s) return null;
  // Accepts both the plain per-column value ("RM678") now used by the
  // dedicated PRICE / SFT column, and the older inline "RM678/sft" format
  // (kept for backward compatibility with any older cached data).
  const re = /RM\s?([\d,]+\.?\d*)(?:\s*\/\s*sft)?/gi;
  let m, vals=[];
  while((m = re.exec(s))) vals.push(parseFloat(m[1].replace(/,/g,'')));
  return vals.length ? Math.min(...vals) : null;
}
function csvParseSize(s, which){
  if(!s) return null;
  const nums = (s.match(/(\d+)\s*sft/g)||[]).map(x=>parseFloat(x));
  if(!nums.length) return null;
  return which==='max' ? Math.max(...nums) : Math.min(...nums);
}

// Columns that Google Sheets shows as blank on continuation rows of a
// vertically-merged cell. We forward-fill these from the last non-blank
// value in the same column, matching how the sheet visually reads.
const MERGED_COLS = ['PROJECT','LOCATION','DEVELOPER','TENURE','TITLE','DETAILS','Pet-Friendly',
                      'MAINTENANCE FEE / SFT','CAR PARKS','VP DATE','LEGAL FEE (BEAR BY CLIENT)',
                      'NUMBER OF UNITS','LAND SIZE','UNITS / FLOOR','LIFTS / FLOOR','ADDRESS'];

// Google Sheets soft-wraps long header/cell text as literal newlines in the
// CSV export (e.g. "MAINTENANCE\nFEE / SFT"). Collapse any run of whitespace
// to a single space so column names and lookups stay stable regardless of
// how a cell happens to wrap in the sheet.
function normSpace(s){ return (s||'').replace(/\s+/g,' ').trim(); }

// A few fields (per-tower unit/lift breakdowns) are often hand-formatted by
// Tony in the sheet with real Alt+Enter line breaks - e.g. "350 units -
// Tower A" / "500 units - Tower B" each on their own line. normSpace() would
// flatten that into one run-on sentence, so these columns keep their line
// breaks instead: each line gets its own internal whitespace cleaned up and
// trimmed, blank lines are dropped, and the result is joined back with \n
// for the page to render one item per line (see ".fact .v{white-space:
// pre-line}" in the CSS).
const MULTILINE_COLS = ['NUMBER OF UNITS','UNITS / FLOOR','LIFTS / FLOOR'];
function normLines(s){
  return (s||'').split(/\r\n|\r|\n/).map(l=>l.replace(/[ \t]+/g,' ').trim()).filter(Boolean).join('\n');
}

function buildProjectsFromCSV(csvText){
  const rows = parseCSV(csvText).filter(r => r.some(c => c && c.trim()!==''));
  if(rows.length < 2) throw new Error('Sheet looks empty');
  const header = rows[0].map(h=>normSpace(h));
  const idx = {}; header.forEach((h,i)=>idx[h]=i);
  if(idx['PROJECT']===undefined || idx['LOCATION']===undefined){
    throw new Error('Header row does not match expected format (PROJECT / LOCATION columns not found)');
  }

  // A "head" row is one where the PROJECT cell itself has a value - it starts
  // a new project. Only *continuation* rows (blank PROJECT cell, belonging to
  // the same vertically-merged block) should inherit values from the row
  // above. A head row's own blanks are genuinely blank, not a continuation
  // of the previous project - otherwise a project with no data yet would
  // incorrectly inherit the previous project's maintenance fee, car park
  // info, VP date, etc.
  const fill = {};
  const dataRows = rows.slice(1).map(r=>{
    const isHeadRow = normSpace(r[idx['PROJECT']] || '') !== '';
    const rec = {};
    header.forEach((col,i)=>{
      if(!col) return;
      let val = MULTILINE_COLS.includes(col) ? normLines(r[i]||'') : normSpace(r[i]||'');
      if(MERGED_COLS.includes(col)){
        if(isHeadRow){ fill[col] = val; }
        else if(val){ fill[col] = val; }
        else { val = fill[col] || ''; }
      }
      rec[col] = val;
    });
    return rec;
  }).filter(r => r['PROJECT']);

  const byProject = {};
  const order = [];
  dataRows.forEach(r=>{
    const name = r['PROJECT'];
    if(!byProject[name]){
      byProject[name] = {
        name,
        location: r['LOCATION'] || 'Klang Valley (TBC)',
        address: r['ADDRESS'] || '',
        developer: r['DEVELOPER'] || 'TBC',
        tenure: r['TENURE'] || 'TBC',
        title: r['TITLE'] || '',
        petFriendly: r['Pet-Friendly'] || '',
        details: r['DETAILS'] || '',
        numUnits: r['NUMBER OF UNITS'] || '',
        landSize: r['LAND SIZE'] || '',
        unitsPerFloor: r['UNITS / FLOOR'] || '',
        liftsPerFloor: r['LIFTS / FLOOR'] || '',
        maintFee: r['MAINTENANCE FEE / SFT'] || '',
        carParks: r['CAR PARKS'] || '',
        vpDate: r['VP DATE'] || 'TBC',
        legalFee: r['LEGAL FEE (BEAR BY CLIENT)'] || '',
        status: r['STATUS'] || '',
        units: []
      };
      order.push(name);
    }
    const sizeNumStr = r['SIZE (SFT)'] || '';
    const layoutStr = r['LAYOUT'] || '';
    const sizeStr = sizeNumStr ? (sizeNumStr+' sft'+(layoutStr? ' ('+layoutStr+')':'')) : (r['SIZE & LAYOUT'] || '');
    const priceStr = r['NETT PRICE'] || '';
    const psfStr = r['PRICE / SFT'] || '';
    if(sizeStr || priceStr){
      byProject[name].units.push({
        size: sizeStr, price: priceStr, priceNum: csvParsePrice(priceStr) || 0,
        psf: psfStr, psfNum: csvParsePsf(psfStr) || 0, status: r['STATUS'] || ''
      });
    }
  });

  return order.map(name=>{
    const p = byProject[name];
    const prices = p.units.map(u=>u.priceNum).filter(Boolean);
    const psfs = p.units.map(u=>u.psfNum).filter(Boolean);
    const minsz = p.units.map(u=>csvParseSize(u.size,'min')).filter(x=>x);
    const maxsz = p.units.map(u=>csvParseSize(u.size,'max')).filter(x=>x);
    p.priceFrom = prices.length ? Math.min(...prices) : 0;
    p.psfFrom = psfs.length ? Math.min(...psfs) : 0;
    p.sizeMin = minsz.length ? Math.min(...minsz) : 0;
    p.sizeMax = maxsz.length ? Math.max(...maxsz) : 0;
    return p;
  });
}

async function trySyncLiveSheet(manual){
  const badge = document.getElementById('syncBadge');
  if(manual) badge.textContent = '🔄 Syncing…';
  try{
    const res = await fetch(SHEET_CSV_URL, {cache:'no-store'});
    if(!res.ok) throw new Error('HTTP '+res.status);
    const text = await res.text();
    if(text.trim().startsWith('<')) throw new Error('Sheet is not publicly viewable (got HTML instead of CSV)');
    const fresh = buildProjectsFromCSV(text);
    if(!fresh.length) throw new Error('No project rows found');
    PROJECTS = fresh;
    dataSource = 'live';
    lastSyncAt = new Date();
    refreshUI();
    updateSyncBadge();
  }catch(err){
    console.warn('Live sheet sync failed, using cached data:', err.message);
    dataSource = 'cached';
    updateSyncBadge(err.message);
  }
}

function updateSyncBadge(errMsg){
  const badge = document.getElementById('syncBadge');
  if(dataSource === 'live'){
    badge.style.display = '';
    badge.textContent = '🟢 Live from sheet · ' + lastSyncAt.toLocaleTimeString('en-MY',{hour:'2-digit',minute:'2-digit'});
    badge.title = 'Synced directly from your Google Sheet.';
  } else {
    // Keep this quiet for clients - just hide the badge rather than
    // surfacing "cached" language that reads as stale/outdated.
    badge.style.display = 'none';
    badge.title = errMsg ? ('Live sync unavailable: '+errMsg+'. Make sure the sheet is shared as "Anyone with the link - Viewer".') : 'Showing the snapshot saved when this page was built.';
  }
}

// ---------- master refresh ----------
function refreshUI(){
  computeDerived();
  renderStats();
  renderVerdict();
  renderAreaTiles();
  renderRoomTicks();
  renderCompletionTicks();
  renderBudgetTicks();
  renderSizeTicks();
  renderTable();
  renderCompareTray();
  renderFavTray();
  updateBadges();
}

// ---------- init ----------
// Search and sort act on whatever's already on screen, so they stay live.
// Tenure/Pet/Title are preferences like area/budget/rooms, so they queue up
// and only take effect once "Filter" is clicked.
document.getElementById('searchInput').addEventListener('input', e=>{ state.search = e.target.value; renderTable(); });
document.getElementById('sortSelect').addEventListener('change', e=>{ state.sort = e.target.value; renderTable(); });
document.getElementById('tenureSelect').addEventListener('change', e=>{ state.tenure = e.target.value; markFiltersPending(); });
document.getElementById('petSelect').addEventListener('change', e=>{ state.pet = e.target.value; markFiltersPending(); });
document.getElementById('titleSelect').addEventListener('change', e=>{ state.title = e.target.value; markFiltersPending(); });

refreshUI();
updateSyncBadge();
trySyncLiveSheet(false);

// ---------- engagement tracking (GA4): which section holds attention longest ----------
(function(){
  if(typeof gtag !== 'function') return;
  const sections = document.querySelectorAll('[data-sec-label]');
  const enterTimes = {};
  const io = new IntersectionObserver((entries)=>{
    entries.forEach(entry=>{
      const label = entry.target.getAttribute('data-sec-label');
      if(entry.isIntersecting){
        enterTimes[label] = Date.now();
      } else if(enterTimes[label]){
        const seconds = Math.round((Date.now() - enterTimes[label]) / 1000);
        delete enterTimes[label];
        if(seconds >= 2) gtag('event', 'section_dwell', {section: label, seconds: seconds});
      }
    });
  }, {threshold: 0.4});
  sections.forEach(s=>io.observe(s));
  // Catch whichever section is still on-screen when the visitor leaves -
  // otherwise their last (possibly longest) viewing never gets recorded.
  window.addEventListener('pagehide', ()=>{
    Object.keys(enterTimes).forEach(label=>{
      const seconds = Math.round((Date.now() - enterTimes[label]) / 1000);
      if(seconds >= 2) gtag('event', 'section_dwell', {section: label, seconds: seconds});
    });
  });
})();

// ---------- scroll depth milestones (GA4) ----------
(function(){
  if(typeof gtag !== 'function') return;
  const milestones = [25, 50, 75, 100];
  const fired = new Set();
  window.addEventListener('scroll', ()=>{
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    if(docHeight <= 0) return;
    const pct = Math.round((window.scrollY / docHeight) * 100);
    milestones.forEach(m=>{
      if(pct >= m && !fired.has(m)){
        fired.add(m);
        gtag('event', 'scroll_depth', {percent: m});
      }
    });
  }, {passive:true});
})();
"""

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>KL Projects Atlas by Tony Hoo | Transparent Comparisons. Better Decisions.</title>
<meta name="description" content="Side-by-side comparison of new property launches across Bukit Jalil, PJ Damansara, Sri Petaling, Sungai Besi, Taman Desa and more. Real prices, PSF, sizes, and completion dates — updated regularly.">
<meta property="og:title" content="KL Projects Atlas by Tony Hoo">
<meta property="og:description" content="Transparent comparisons, better decisions. Compare new launch condos across Klang Valley — price, PSF, tenure, completion, all in one place.">
<meta property="og:type" content="website">
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-4DCZN490NH"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-4DCZN490NH');
</script>
<!-- Microsoft Clarity -->
<script type="text/javascript">
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "xyh7zrmlcf");
</script>
<style>__CSS__</style>
</head>
<body class="dark">

<nav class="nav" id="siteNav">
  <div class="container nav-inner">
    <div class="brand">
      <div class="brand-mark">
        <img class="logo-for-light" src="data:image/png;base64,__LOGO_BLACK_BG__" alt="KL Projects Atlas logo">
        <img class="logo-for-dark" src="data:image/png;base64,__LOGO_WHITE_BG__" alt="KL Projects Atlas logo">
      </div>
      <div class="brand-text">
        <div class="brand-title">KL Projects Atlas by Tony Hoo</div>
        <div class="brand-tagline">Transparent Comparisons. Better Decisions.</div>
      </div>
    </div>
    <div class="nav-actions">
      <button class="pill pill-ok" id="syncBadge" onclick="trySyncLiveSheet(true)" title="Click to re-sync now" style="cursor:pointer;border:none;display:none"></button>
      <button class="icon-btn" onclick="toggleDark()" title="Toggle dark mode">🌓</button>
      <button class="icon-btn" id="favToggleBtn" onclick="toggleFavOnly()" title="Show shortlisted only">♥<span class="shortlist-badge" id="favBadge" style="display:none">0</span></button>
      <button class="btn btn-outline btn-sm" id="sendShortlistBtn" onclick="sendShortlist()" title="Send your shortlisted projects to Tony on WhatsApp">📤 <span class="btn-label">Send My Shortlist</span></button>
      <button class="btn btn-primary btn-sm" onclick="openLead('General enquiry')">💬 WhatsApp Tony Hoo</button>
    </div>
  </div>
</nav>

<section class="hero" id="sec-hero" data-sec-label="Hero / Headline">
  <div class="container">
    <div class="eyebrow">📍 Klang Valley New Launch Tracker · Updated Weekly</div>
    <h1>Compare Every New KL Property <em>Before You Commit</em></h1>
    <p class="lead">Real prices, PSF, tenure, unit sizes and completion dates for new launches across the whole Klang Valley — so your next viewing is an informed one, not a guess.</p>
    <div class="hero-cta">
      <button class="btn btn-primary" onclick="openLead('General enquiry')">💬 WhatsApp Tony Hoo</button>
      <a class="btn btn-gold" href="#table">📊 Browse Full Comparison</a>
    </div>
    <div class="hero-stats">
      <div class="hero-stat"><div class="num" id="statProjects">–</div><div class="label">New Projects Tracked</div></div>
      <div class="hero-stat"><div class="num" id="statAreas">–</div><div class="label">Areas Covered</div></div>
      <div class="hero-stat"><div class="num" id="statPrice">–</div><div class="label">Lowest Entry Price</div></div>
      <div class="hero-stat"><div class="num" id="statMedPrice">–</div><div class="label">Median Entry Price</div></div>
      <div class="hero-stat"><div class="num" id="statMaxPrice">–</div><div class="label">Highest Price</div></div>
    </div>
    <div class="trust-row"><span class="stars">★★★★★</span> Trusted by 100+ buyers this year · Data compiled directly from developer sales galleries</div>
  </div>
</section>

<!-- Swap the placeholder photo/text below with Tony's real photo and a short
     personal bio - kept to one simple row with generous spacing so it stays
     a calm introduction rather than another dense, busy section. -->
<section class="about-intro" id="sec-about" data-sec-label="About Tony">
  <div class="container about-intro-inner">
    <div class="about-photo-placeholder"><img src="data:image/jpeg;base64,__PROFILE_TONY__" alt="Tony Hoo"></div>
    <div class="about-text">
      <h2>I am Tony Hoo (IQI Realty | REN 75480)</h2>
      <p>Dedicated to helping clients make smarter property decisions with clarity, confidence, and genuine,<br>no-pressure advice. I specialise in new project sales, investment properties, and modern township<br>developments across Malaysia — bringing buyers the transparency they need to choose with certainty.</p>
    </div>
  </div>
</section>

<section class="filters-hero container" id="filters" data-sec-label="Find Your Match (Filters)">
  <div class="section-head">
    <div><h2>🎯 Find Your Match</h2><p>Set what matters to you below. Area, budget and rooms are the ones we need to match you well — everything else is optional.</p></div>
  </div>

  <div class="filter-block">
    <div class="filter-label-row">
      <label>Area</label><span class="pill pill-gold req-pill">Required</span>
      <span class="hint">Select one or more</span>
    </div>
    <div class="area-tile-grid" id="areaChips"></div>
  </div>

  <div class="filter-block">
    <div class="filter-label-row">
      <label>Budget</label><span class="pill pill-gold req-pill">Required</span>
      <span class="hint">Select one or more</span>
    </div>
    <div class="chip-row" id="budgetTicks"></div>
  </div>

  <div class="filter-block">
    <div class="filter-label-row">
      <label>Rooms</label><span class="pill pill-gold req-pill">Required</span>
      <span class="hint">Select one or more</span>
    </div>
    <div class="chip-row" id="roomsTicks"></div>
  </div>

  <div class="filter-block">
    <div class="filter-label-row">
      <label>Completion</label><span class="pill pill-neutral opt-pill">Optional</span>
      <span class="hint">Select one or more</span>
    </div>
    <div class="chip-row" id="completionTicks"></div>
  </div>

  <div class="filter-block">
    <div class="filter-label-row">
      <label>Layout Size (sft)</label><span class="pill pill-neutral opt-pill">Optional</span>
      <span class="hint">Select one or more</span>
    </div>
    <div class="chip-row" id="sizeTicks"></div>
  </div>

  <div class="filter-block">
    <div class="filter-row-compact">
      <div class="select-filter">
        <div class="filter-label-row"><label>Title</label><span class="pill pill-neutral opt-pill">Optional</span></div>
        <select class="sort-select" id="titleSelect">
          <option value="Residential">Residential</option>
          <option value="Commercial">Commercial</option>
          <option value="Any" selected>Regardless</option>
        </select>
      </div>
      <div class="select-filter">
        <div class="filter-label-row"><label>Tenure</label><span class="pill pill-neutral opt-pill">Optional</span></div>
        <select class="sort-select" id="tenureSelect">
          <option value="All">Regardless</option>
          <option value="Freehold">Freehold</option>
          <option value="Leasehold">Leasehold</option>
        </select>
      </div>
      <div class="select-filter">
        <div class="filter-label-row"><label>Pet Friendly</label><span class="pill pill-neutral opt-pill">Optional</span></div>
        <select class="sort-select" id="petSelect">
          <option value="Any">Regardless</option>
          <option value="Yes">Yes</option>
          <option value="No">No</option>
        </select>
      </div>
    </div>
  </div>

  <div class="filter-actions">
    <div class="search-row" style="flex:1">
      <div class="search-box">
        <span class="ic">🔍</span>
        <input type="text" id="searchInput" placeholder="Search project, area or developer.">
      </div>
      <select class="sort-select" id="sortSelect">
        <option value="price-asc" selected>Price: Low → High</option>
        <option value="price-desc">Price: High → Low</option>
        <option value="psf-asc">PSF: Low → High</option>
        <option value="vp-asc">Completion: Earliest</option>
        <option value="name-asc">Name: A → Z</option>
      </select>
    </div>
    <button class="btn btn-gold" id="applyFiltersBtn" onclick="applyFilters()">🔎 Filter</button>
    <button class="btn btn-outline btn-sm" onclick="resetFilters()">Reset All</button>
    <span class="results-count" id="resultsCount"></span>
  </div>
</section>

<section class="table-section" id="table" data-sec-label="Comparison Table">
  <div class="container">
    <div class="fav-callout" style="margin-bottom:14px"><span class="ic">🤍</span><span>Tap the heart icon on any project below to save it to your shortlist — your picks show up right here and at the top of the page, ready to send to Tony on WhatsApp anytime.</span></div>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Compare</th><th>Project</th><th>Price</th><th>PSF From</th><th>Tenure</th><th>Size (SFT)</th><th>Completion</th><th>Status</th>
          </tr>
        </thead>
        <tbody id="tableBody"></tbody>
      </table>
    </div>
    <div class="mobile-cards" id="mobileCards"></div>
  </div>
</section>

<section class="verdict container" id="sec-verdict" data-sec-label="Most Popular Picks">
  <div class="section-head">
    <div><h2>🏆 Most Popular Picks</h2><p>The projects our buyers ask about most, by approximate share of enquiries.</p></div>
  </div>
  <div class="verdict-grid" id="verdictGrid"></div>
  <p style="font-size:0.965rem;color:var(--ink-soft);margin-top:14px">*Estimated share of buyer enquiries across our four most-asked-about projects; figures are indicative, not an independently audited survey.</p>
</section>

<section class="testi" id="sec-testi" data-sec-label="What Buyers Say">
  <div class="container">
    <div class="section-head"><div><h2>💬 What Buyers Say</h2><p>Real feedback from clients who used this comparison to shortlist.</p></div></div>
    <div class="testi-grid">
      <div class="testi-card"><div class="stars">★★★★★</div><p>"Having every project's pricing side by side saved me weeks of calling different sales galleries. Made my decision so much clearer."</p><div class="testi-who"><div class="testi-avatar">L</div><div><div class="testi-name">Lawrence</div><div class="testi-loc">Bukit Jalil buyer</div></div></div></div>
      <div class="testi-card"><div class="stars">★★★★★</div><p>"Tony was upfront about which units were sold out and which packages were actually worth it. No sales pressure, just facts."</p><div class="testi-who"><div class="testi-avatar">F</div><div><div class="testi-name">Ms. Fong</div><div class="testi-loc">First-time buyer</div></div></div></div>
      <div class="testi-card"><div class="stars">★★★★★</div><p>"The compare tool helped me and my wife narrow 8 projects down to 2 in one evening. Highly recommend before any viewing."</p><div class="testi-who"><div class="testi-avatar">L</div><div><div class="testi-name">Mr. Lim & family</div><div class="testi-loc">Investor, Bukit Jalil</div></div></div></div>
    </div>
  </div>
</section>

<section class="testi-photo" id="sec-testi-photo" data-sec-label="Buyer Photos">
  <div class="container">
    <div class="section-head"><div><h2>📸 Testimonials</h2><p>Photos from buyers who found their project here.</p></div></div>
    <div class="testi-photo-grid">
      <div class="testi-photo-card"><div class="testi-photo-placeholder"><img src="data:image/jpeg;base64,__TESTI_LAWRENCE__" alt="Lawrence"></div><div class="testi-name">Lawrence</div></div>
      <div class="testi-photo-card"><div class="testi-photo-placeholder"><img src="data:image/jpeg;base64,__TESTI_MSFONG__" alt="Ms. Fong"></div><div class="testi-name">Ms. Fong</div></div>
      <div class="testi-photo-card"><div class="testi-photo-placeholder"><img src="data:image/jpeg;base64,__TESTI_MRLIM__" alt="Mr. Lim & family"></div><div class="testi-name">Mr. Lim & family</div></div>
      <div class="testi-photo-card"><div class="testi-photo-placeholder"><img src="data:image/jpeg;base64,__TESTI_GRACE__" alt="Grace"></div><div class="testi-name">Grace</div></div>
      <div class="testi-photo-card"><div class="testi-photo-placeholder"><img src="data:image/jpeg;base64,__TESTI_ANDY__" alt="Andy"></div><div class="testi-name">Andy</div></div>
      <div class="testi-photo-card"><div class="testi-photo-placeholder"><img src="data:image/jpeg;base64,__TESTI_CASTIEOL__" alt="Castieol"></div><div class="testi-name">Castieol</div></div>
    </div>
  </div>
</section>

<div class="bottom-photo-band">
<section class="final-cta" id="sec-final-cta" data-sec-label="Final CTA">
  <div class="container">
    <h2>Still deciding between a few projects?</h2>
    <p>Send us your shortlist on WhatsApp and we'll walk you through unit availability, the latest package (T&Cs apply), and site visit scheduling — no obligation.</p>
    <button class="btn btn-primary" onclick="openLead('General enquiry')">💬 Chat With Tony Hoo</button>
  </div>
</section>

<footer>
  <div class="container">
    Data compiled for reference only · Prices, packages & availability subject to change without notice · Last updated: <span id="lastUpdated"></span><br>
    © 2026 KL Projects Atlas by Tony Hoo · Transparent Comparisons. Better Decisions.
  </div>
</footer>
</div>

<!-- Shortlist + Compare trays, stacked in one fixed wrapper so both can be
     visible at once without overlapping each other. -->
<div class="bottom-trays" id="bottomTrays">
  <div class="tray fav-tray" id="favTray">
    <div class="tray-inner">
      <span class="tray-label">❤️ Shortlist (<span id="favTrayCount">0</span>)</span>
      <div class="fav-chips" id="favChips"></div>
      <button class="btn btn-primary btn-sm" onclick="sendShortlist()">📤 Send My Shortlist</button>
    </div>
  </div>
  <div class="tray cmp-tray" id="cmpTray">
    <div class="tray-inner">
      <span class="tray-label">⚖️ Compare</span>
      <div class="cmp-chips" id="cmpChips"></div>
      <button class="btn btn-dark btn-sm" onclick="openCompareModal()">Compare Now (<span id="cmpCount">0</span>)</button>
    </div>
  </div>
</div>

<!-- Sticky mobile CTA -->
<div class="sticky-cta">
  <button class="btn btn-outline" onclick="document.getElementById('searchInput').scrollIntoView({behavior:'smooth'})">📊 Browse</button>
  <button class="btn btn-primary" onclick="openLead('General enquiry')">💬 WhatsApp</button>
</div>

<!-- Compare modal -->
<div class="modal-overlay" id="cmpModalOverlay">
  <div class="modal cmp-modal">
    <button class="modal-close" onclick="closeCompareModal()">✕</button>
    <h3>Side-by-Side Comparison</h3>
    <p class="sub">Scroll horizontally on mobile to see all columns.</p>
    <div style="overflow-x:auto" id="cmpModalBody"></div>
  </div>
</div>

<script>__JS__</script>
<script>document.getElementById('lastUpdated').textContent = new Date().toLocaleDateString('en-MY',{year:'numeric',month:'long'});</script>
</body>
</html>
"""

final_js = JS.replace("__PROJECTS_DATA__", data)
final_html = (HTML.replace("__CSS__", CSS).replace("__JS__", final_js)
              .replace("__LOGO_BLACK_BG__", LOGO_BLACK_BG_B64)
              .replace("__LOGO_WHITE_BG__", LOGO_WHITE_BG_B64)
              .replace("__PROFILE_TONY__", PROFILE_TONY_B64)
              .replace("__ABOUT_BG__", ABOUT_BG_B64)
              .replace("__HERO_BG__", HERO_BG_B64)
              .replace("__TESTI_CASTIEOL__", TESTI_CASTIEOL_B64)
              .replace("__TESTI_ANDY__", TESTI_ANDY_B64)
              .replace("__TESTI_MRLIM__", TESTI_MRLIM_B64)
              .replace("__TESTI_GRACE__", TESTI_GRACE_B64)
              .replace("__TESTI_LAWRENCE__", TESTI_LAWRENCE_B64)
              .replace("__TESTI_MSFONG__", TESTI_MSFONG_B64))

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html'),'w') as f:
    f.write(final_html)

print("written", len(final_html), "chars")
