#!/usr/bin/env python3
"""
Regenerates games/solar-system-game.html with hand-crafted CSS planets.
No external images — every planet is drawn with radial/linear gradients.
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT  = ROOT / "games" / "solar-system-game.html"

# ── Read the current file and keep everything that doesn't change ──
src = OUT.read_text(encoding="utf-8")

# ──────────────────────────────────────────────
#  A.  PLANET CSS  (inserted before </style>)
# ──────────────────────────────────────────────
PLANET_CSS = r"""
/* ═══════════════════════════════════════════
   CSS PLANET ART  —  no external images
═══════════════════════════════════════════ */
.planet-art{border-radius:50%;position:relative;flex-shrink:0;display:block;}
.planet-art.pop{animation:planetPop 0.4s cubic-bezier(0.175,0.885,0.32,1.275);}
@keyframes planetPop{0%{transform:scale(0.55) rotate(-8deg);}70%{transform:scale(1.18) rotate(3deg);}100%{transform:scale(1) rotate(0);}}
.planet-art.flash{animation:planetFlash 0.6s ease;}
@keyframes planetFlash{0%{filter:brightness(1);}35%{filter:brightness(1.65) drop-shadow(0 0 22px rgba(247,201,72,1));}100%{filter:brightness(1);}}
/* sizes */
.planet-lg{width:min(160px,62%);aspect-ratio:1;box-shadow:0 8px 28px rgba(0,0,0,0.45);margin:4px auto;}
.planet-sm{width:115px;height:115px;box-shadow:0 4px 14px rgba(0,0,0,0.4);}

/* ── SUN ── */
.planet-sun{background:radial-gradient(circle at 36% 30%,#fff9c4,#ffeb3b 22%,#ff9800 55%,#e65100);overflow:visible;box-shadow:0 0 36px 16px rgba(255,155,0,0.55),0 0 72px 38px rgba(255,90,0,0.28);animation:sunPulse 2.5s ease-in-out infinite alternate;}
@keyframes sunPulse{from{box-shadow:0 0 36px 16px rgba(255,155,0,0.55),0 0 72px 38px rgba(255,90,0,0.28);}to{box-shadow:0 0 58px 28px rgba(255,175,0,0.75),0 0 110px 56px rgba(255,90,0,0.42);}}

/* ── MERCURY ── grey rocky with craters */
.planet-mercury{background:radial-gradient(circle at 38% 30%,#d8d4cf,#a09890 38%,#736860 68%,#4c413c);}
.planet-mercury::after{content:'';position:absolute;inset:0;border-radius:50%;
  background:
    radial-gradient(circle 9% at 26% 36%,rgba(0,0,0,0.22) 0%,rgba(0,0,0,0.05) 55%,transparent 100%),
    radial-gradient(circle 5% at 64% 24%,rgba(0,0,0,0.18) 0%,rgba(0,0,0,0.04) 55%,transparent 100%),
    radial-gradient(circle 6% at 72% 65%,rgba(0,0,0,0.14) 0%,rgba(0,0,0,0.03) 55%,transparent 100%),
    radial-gradient(circle 4% at 50% 72%,rgba(0,0,0,0.12) 0%,transparent 100%),
    radial-gradient(circle 3% at 38% 55%,rgba(0,0,0,0.1) 0%,transparent 100%);}

/* ── VENUS ── pale gold with cloud streaks */
.planet-venus{background:radial-gradient(circle at 38% 30%,#fffde7,#f9e236 28%,#f0b800 58%,#c48d00);overflow:hidden;}
.planet-venus::after{content:'';position:absolute;inset:0;border-radius:50%;
  background:
    repeating-linear-gradient(-14deg,
      transparent 0px,transparent 14px,
      rgba(255,255,255,0.12) 14px,rgba(255,255,255,0.12) 22px,
      transparent 22px,transparent 32px,
      rgba(200,180,0,0.09) 32px,rgba(200,180,0,0.09) 40px);}

/* ── EARTH ── blue oceans + green continents */
.planet-earth{background:radial-gradient(circle at 38% 30%,#e3f2fd,#42a5f5 26%,#1565c0 60%,#0d47a1);}
.planet-earth::after{content:'';position:absolute;inset:0;border-radius:50%;
  background:
    radial-gradient(ellipse 46% 28% at 58% 46%,#43a047 0%,#2e7d32 55%,transparent 65%),
    radial-gradient(ellipse 22% 16% at 26% 60%,#66bb6a 0%,transparent 65%),
    radial-gradient(ellipse 16% 12% at 74% 28%,#388e3c 0%,transparent 65%),
    radial-gradient(ellipse 10% 22% at 16% 35%,#4caf50 0%,transparent 65%),
    radial-gradient(ellipse 8%  14% at 82% 58%,#2e7d32 0%,transparent 65%);}

/* ── MARS ── red with polar ice cap + subtle dust */
.planet-mars{background:radial-gradient(circle at 38% 30%,#ffcbb8,#e64a19 38%,#b71c1c 66%,#880e0e);}
.planet-mars::before{content:'';position:absolute;inset:0;border-radius:50%;
  background:repeating-linear-gradient(-8deg,
    transparent 0px,transparent 22px,
    rgba(180,60,15,0.12) 22px,rgba(180,60,15,0.12) 30px);}
.planet-mars::after{content:'';position:absolute;top:4%;left:26%;right:26%;height:11%;border-radius:50%;
  background:radial-gradient(ellipse at 50% 60%,rgba(255,255,255,0.85),rgba(200,220,255,0.4) 70%,transparent);}

/* ── JUPITER ── banded orange-brown + Red Spot */
.planet-jupiter{background:radial-gradient(circle at 38% 30%,#ffe0b2,#ff9800 30%,#e65100 62%,#bf360c);overflow:hidden;}
.planet-jupiter::before{content:'';position:absolute;inset:0;border-radius:50%;
  background:
    repeating-linear-gradient(6deg,
      transparent 0px,transparent 10px,
      rgba(120,45,5,0.32) 10px,rgba(120,45,5,0.32) 18px,
      transparent 18px,transparent 26px,
      rgba(80,30,5,0.18) 26px,rgba(80,30,5,0.18) 34px,
      transparent 34px,transparent 44px,
      rgba(160,80,20,0.22) 44px,rgba(160,80,20,0.22) 52px);}
.planet-jupiter::after{content:'';position:absolute;width:21%;height:13%;border-radius:50%;
  background:radial-gradient(circle at 40% 45%,#ef5350,#b71c1c 60%,#7f0000);
  top:52%;left:61%;box-shadow:0 0 10px 3px rgba(220,20,20,0.45);}

/* ── SATURN body ── golden banded */
.planet-saturn{background:radial-gradient(circle at 38% 30%,#fff9c4,#ffcc02 30%,#f0a500 60%,#c07800);}
.planet-saturn::before{content:'';position:absolute;inset:0;border-radius:50%;
  background:repeating-linear-gradient(4deg,
    transparent 0px,transparent 12px,
    rgba(160,100,10,0.22) 12px,rgba(160,100,10,0.22) 20px,
    transparent 20px,transparent 28px,
    rgba(100,60,5,0.12) 28px,rgba(100,60,5,0.12) 36px);}

/* ── SATURN RING wrapper ── */
.planet-saturn-wrap{position:relative;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.planet-saturn-wrap.sz-lg{width:min(270px,88%);margin:4px auto;}
.planet-saturn-wrap.sz-sm{width:200px;margin:0 auto;}
.planet-saturn-wrap .planet-art{position:relative;z-index:10;}
.planet-saturn-ring{
  position:absolute;
  left:0;right:0;
  margin:0 auto;
  width:100%;height:42%;
  border-radius:50%;
  border-style:solid;
  transform:rotateX(74deg);
  pointer-events:none;
  z-index:5;
}
.sz-lg .planet-saturn-ring{
  border-width:13px;
  border-color:rgba(218,182,65,0.78);
  box-shadow:
    inset 0 0 0 7px rgba(195,155,50,0.3),
    0 0 0 7px rgba(190,150,45,0.28),
    0 0 0 15px rgba(162,125,38,0.16);
}
.sz-sm .planet-saturn-ring{
  border-width:8px;
  border-color:rgba(218,182,65,0.78);
  box-shadow:inset 0 0 0 5px rgba(195,155,50,0.3),0 0 0 5px rgba(190,150,45,0.28);
}

/* ── URANUS ── pale cyan-green, tilted ring hint */
.planet-uranus{background:radial-gradient(circle at 38% 30%,#e0f7fa,#80deea 33%,#26c6da 62%,#00838f);}
.planet-uranus::before{content:'';position:absolute;left:10%;right:10%;top:20%;bottom:20%;
  border-radius:50%;border:3px solid rgba(180,240,248,0.3);transform:rotate(98deg);}
.planet-uranus::after{content:'';position:absolute;inset:0;border-radius:50%;
  background:repeating-linear-gradient(94deg,
    transparent 0px,transparent 18px,
    rgba(255,255,255,0.06) 18px,rgba(255,255,255,0.06) 26px);}

/* ── NEPTUNE ── deep blue + faint storm spot */
.planet-neptune{background:radial-gradient(circle at 38% 30%,#b3e5fc,#1e88e5 36%,#0d47a1 66%,#1a237e);}
.planet-neptune::before{content:'';position:absolute;inset:0;border-radius:50%;
  background:repeating-linear-gradient(18deg,
    transparent 0px,transparent 16px,
    rgba(100,180,255,0.1) 16px,rgba(100,180,255,0.1) 24px);}
.planet-neptune::after{content:'';position:absolute;width:22%;height:16%;top:44%;left:58%;
  border-radius:50%;background:rgba(210,230,255,0.22);}

/* ── MOON ── grey with impact craters */
.planet-moon{background:radial-gradient(circle at 38% 30%,#f0f0ee,#c0bdb9 38%,#9e9e9e 64%,#757575);}
.planet-moon::before{content:'';position:absolute;inset:0;border-radius:50%;
  background:
    radial-gradient(ellipse 80% 30% at 50% 80%,rgba(0,0,0,0.12) 0%,transparent 100%),
    radial-gradient(ellipse 60% 25% at 35% 70%,rgba(100,100,100,0.08) 0%,transparent 100%);}
.planet-moon::after{content:'';position:absolute;inset:0;border-radius:50%;
  background:
    radial-gradient(circle 8%  at 30% 40%,rgba(70,70,70,0.22) 0%,rgba(70,70,70,0.05) 60%,transparent 100%),
    radial-gradient(circle 5%  at 58% 24%,rgba(70,70,70,0.18) 0%,rgba(70,70,70,0.04) 60%,transparent 100%),
    radial-gradient(circle 7%  at 70% 64%,rgba(70,70,70,0.14) 0%,rgba(70,70,70,0.03) 60%,transparent 100%),
    radial-gradient(circle 4%  at 44% 72%,rgba(70,70,70,0.12) 0%,transparent 100%),
    radial-gradient(circle 3%  at 76% 44%,rgba(70,70,70,0.10) 0%,transparent 100%),
    radial-gradient(circle 5%  at 20% 60%,rgba(70,70,70,0.12) 0%,transparent 100%),
    radial-gradient(circle 3%  at 84% 30%,rgba(70,70,70,0.09) 0%,transparent 100%);}

/* ── PLUTO ── brownish with heart-shaped bright region */
.planet-pluto{background:radial-gradient(circle at 38% 30%,#d7ccc8,#a1887f 36%,#795548 66%,#4e342e);}
.planet-pluto::after{content:'';position:absolute;width:36%;height:38%;top:22%;left:28%;
  border-radius:42% 58% 52% 48% / 46% 44% 56% 54%;
  background:radial-gradient(ellipse at 50% 55%,rgba(255,210,170,0.48),rgba(220,180,130,0.22) 60%,transparent);}
"""

# Insert PLANET_CSS before </style>
src = src.replace("</style>", PLANET_CSS + "\n</style>", 1)

# ──────────────────────────────────────────────
#  B.  CARDS DATA — remove img: fields, keep type/label/f
# ──────────────────────────────────────────────
NEW_CARDS = r"""var cards=[
  {e:"\u2600\uFE0F",n:"Sun",     type:"star",       label:"\u2B50 Star \u00B7 Centre of Solar System",
   f:"The Sun is a giant star made of super-hot gas! It gives light and warmth to all planets. About one million Earths could fit inside the Sun \u2014 it is enormous!"},
  {e:"\u26AB",      n:"Mercury", type:"rocky",       label:"\uD83E\uDEA8 Rocky \u00B7 1st Planet",
   f:"Mercury is the smallest planet and the fastest mover \u2014 it zooms around the Sun in just 88 days! Despite being closest to the Sun, Venus is actually hotter!"},
  {e:"\uD83D\uDFE1",n:"Venus",   type:"rocky",       label:"\uD83D\uDD25 Rocky \u00B7 2nd Planet",
   f:"Venus is the hottest planet at 465\u00B0C \u2014 hot enough to melt lead! It spins backwards compared to most planets and is covered in thick poisonous clouds!"},
  {e:"\uD83C\uDF0D",n:"Earth",   type:"rocky",       label:"\uD83C\uDF0A Rocky \u00B7 3rd Planet \u00B7 Our Home",
   f:"Earth is our home \u2014 the only planet with liquid water, air to breathe and living things! It has one moon and is about 4.5 billion years old!"},
  {e:"\uD83D\uDD34",n:"Mars",    type:"rocky",       label:"\uD83C\uDFDC\uFE0F Rocky \u00B7 4th Planet",
   f:"Mars is the Red Planet because its soil is full of iron rust! It has the tallest volcano \u2014 Olympus Mons is 3 times taller than Mount Everest!"},
  {e:"\uD83D\uDFE4",n:"Jupiter", type:"gas-giant",   label:"\uD83D\uDC51 Gas Giant \u00B7 5th \u00B7 Largest",
   f:"Jupiter is the biggest planet \u2014 over 1,300 Earths can fit inside! Its Great Red Spot is a storm that has been raging for more than 350 years!"},
  {e:"\uD83E\uDE90",n:"Saturn",  type:"gas-giant",   label:"\uD83D\uDC8D Gas Giant \u00B7 6th \u00B7 Rings",
   f:"Saturn has beautiful rings made of billions of ice and rock chunks! It is so light it could actually float on water \u2014 if there were an ocean big enough!"},
  {e:"\uD83D\uDD35",n:"Uranus",  type:"ice-giant",   label:"\u2744\uFE0F Ice Giant \u00B7 7th Planet",
   f:"Uranus spins on its side like a rolling ball! Scientists think a giant collision tipped it over billions of years ago. It has 13 rings and 27 known moons!"},
  {e:"\uD83C\uDF00",n:"Neptune", type:"ice-giant",   label:"\uD83C\uDF2C\uFE0F Ice Giant \u00B7 8th Planet",
   f:"Neptune is the farthest planet and the windiest place in the Solar System \u2014 winds reach 2,100 km/h! One Neptune year lasts 165 Earth years!"},
  {e:"\uD83C\uDF15",n:"Moon",    type:"satellite",   label:"\uD83C\uDF0D Earth\u2019s Moon",
   f:"The Moon is Earth\u2019s only natural satellite! Neil Armstrong was the first human to walk on it in 1969. The Moon\u2019s gravity controls our ocean tides every day!"},
  {e:"\uD83C\uDF17",n:"Pluto",   type:"dwarf",       label:"\uD83E\uDDE3 Dwarf Planet",
   f:"Pluto was the 9th planet until 2006 when scientists reclassified it as a dwarf planet. It is smaller than our Moon and lives far out in the icy Kuiper Belt!"}
];"""

# Replace the old cards array (use lambda to avoid re interpreting \u escapes)
old_cards_pat = re.compile(r'var cards=\[.*?\];', re.DOTALL)
src = old_cards_pat.sub(lambda m: NEW_CARDS, src, count=1)

# ──────────────────────────────────────────────
#  C.  JS — makePlanet helper + updated renderAll
# ──────────────────────────────────────────────
MAKE_PLANET_JS = r"""
var PLANET_KEY={
  "Sun":"sun","Mercury":"mercury","Venus":"venus","Earth":"earth","Mars":"mars",
  "Jupiter":"jupiter","Saturn":"saturn","Uranus":"uranus","Neptune":"neptune",
  "Moon":"moon","Pluto":"pluto"
};
function makePlanet(name,sz){
  var key=PLANET_KEY[name]||name.toLowerCase();
  var szcls="planet-"+sz;
  var pid=sz==="sm"?" id=\"screenEmojiEl\"":"";
  if(key==="saturn"){
    return '<div class="planet-saturn-wrap sz-'+sz+'"><div class="planet-art planet-saturn '+szcls+'"'+pid+'></div><div class="planet-saturn-ring"></div></div>';
  }
  return '<div class="planet-art planet-'+key+' '+szcls+'"'+pid+'></div>';
}
"""

NEW_RENDER_ALL = r"""function renderAll(){
  var card=cards[idx],total=cards.length;
  var cf=document.getElementById("cardFace");
  var pDiv=makePlanet(card.n,"lg");
  cf.innerHTML=pDiv;
  var inner=cf.firstChild;
  if(inner){inner.classList.remove("pop");void inner.offsetWidth;inner.classList.add("pop");}
  document.getElementById("cardName").textContent=card.n;
  document.getElementById("cardNum").textContent=(idx+1)+" / "+total;
  var dp=document.getElementById("cardPill");dp.textContent=card.label;dp.className="card-pill "+card.type;
  document.getElementById("screenFace").innerHTML=makePlanet(card.n,"sm");
  document.getElementById("screenName").textContent=card.n;
  var sb=document.getElementById("screenBadge");sb.textContent=card.label;sb.className="scrn-badge-pill "+card.type;
  document.getElementById("screenFact").textContent=card.f;
  document.getElementById("progFg").style.width=((idx+1)/total*100)+"%";
  document.getElementById("progTxt").textContent="Card "+(idx+1)+" of "+total;
  buildGrille(false);
}"""

# Insert makePlanet before the filter block
src = src.replace(
    "\nvar ALL_CARDS=cards.slice();",
    "\n" + MAKE_PLANET_JS + "\nvar ALL_CARDS=cards.slice();",
    1
)

# Replace old renderAll (use lambda to avoid re interpreting backslash escapes)
old_render = re.compile(r'function renderAll\(\)\{.*?\}', re.DOTALL)
src = old_render.sub(lambda m: NEW_RENDER_ALL, src, count=1)

# Remove now-unused imgFail / imgFailScreen (they reference img.dataset.e)
# Keep them as harmless stubs so nothing breaks if called
src = src.replace(
    'function imgFail(img){var d=document.createElement("div");d.className="card-emoji-big pop";d.textContent=img.dataset.e;img.replaceWith(d);}',
    'function imgFail(img){/* no-op: CSS planets used */}'
)
src = src.replace(
    'function imgFailScreen(img){var d=document.createElement("div");d.className="scrn-emoji";d.id="screenEmojiEl";d.textContent=img.dataset.e;img.replaceWith(d);}',
    'function imgFailScreen(img){/* no-op: CSS planets used */}'
)

# ──────────────────────────────────────────────
#  D.  WRITE
# ──────────────────────────────────────────────
OUT.write_text(src, encoding="utf-8")
print(f"  OK  solar-system-game.html  ({len(src):,} chars)")
print("Done!")
