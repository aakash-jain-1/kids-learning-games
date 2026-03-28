#!/usr/bin/env python3
"""
Writes solar-system-game.html, dinosaurs-game.html, weather-game.html
in flashcard style (matching flashcards-game.html).
Uses str.replace() with CAPITALS placeholders — avoids ANY conflict with JS/CSS braces.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
GAMES = ROOT / "games"

# ──────────────────────────────────────────────────────────────
# BASE CSS  — placeholders are all-caps words, order-safe
# Replace in order: ACCENTGLOW→ACCENTDARK→ACCENTLIGHT→ACCENTDIM
#   →ACCENTTEXT→ACCENT  (longest first within each group)
# Same rule for SCREENGLOW2→SCREENGLOW, HBTNBG→BTNSHADOW→BTNTEXT→BTNBG
# ──────────────────────────────────────────────────────────────
BASE_CSS = r"""
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box;}
*{-webkit-tap-highlight-color:transparent;user-select:none;touch-action:manipulation;}
body{font-family:'Comic Sans MS','Chalkboard SE',cursive,Arial,sans-serif;height:100dvh;overflow:hidden;}
.layout{display:flex;height:100dvh;}
.left-pane{width:50%;background:LEFTBG;display:flex;flex-direction:column;align-items:center;padding:20px 16px 22px;gap:14px;overflow:hidden;}
.left-top{width:100%;display:flex;align-items:center;justify-content:space-between;}
.back-link{color:rgba(255,255,255,0.7);text-decoration:none;font-size:0.85em;background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.2);padding:6px 14px;border-radius:50px;transition:0.25s;}
.back-link:hover{background:rgba(255,255,255,0.22);color:#fff;}
.left-heading{color:rgba(255,255,255,0.45);font-size:0.78em;letter-spacing:3px;text-transform:uppercase;}
.cat-bar{display:flex;flex-wrap:wrap;gap:7px;justify-content:center;width:100%;}
.cat-btn{background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.18);color:rgba(255,255,255,0.75);font-size:0.78em;font-weight:bold;padding:6px 13px;border-radius:50px;cursor:pointer;font-family:inherit;transition:0.22s;}
.cat-btn:hover{background:rgba(255,255,255,0.22);color:#fff;}
.cat-btn.active{background:linear-gradient(135deg,ACCENTDARK,ACCENT);color:ACCENTTEXT;border-color:transparent;box-shadow:0 4px 14px ACCENTGLOW;}
.deck-area{position:relative;flex:1;display:flex;align-items:center;justify-content:center;}
.ghost{position:absolute;width:min(400px,42vw,calc(62dvh * 0.727));aspect-ratio:400/550;height:auto;border-radius:26px;background:GHOSTBG;border:2px solid rgba(255,255,255,0.08);box-shadow:0 8px 24px rgba(0,0,0,0.5);}
.ghost::before{content:'';position:absolute;inset:14px;border:1.5px solid rgba(255,255,255,0.07);border-radius:18px;}
.ghost:nth-child(1){transform:rotate(8deg) translate(40px,16px);opacity:0.45;z-index:1;}
.ghost:nth-child(2){transform:rotate(5deg) translate(25px,9px);opacity:0.62;z-index:2;}
.ghost:nth-child(3){transform:rotate(2deg) translate(11px,4px);opacity:0.82;z-index:3;}
.top-card{position:relative;z-index:10;width:min(400px,42vw,calc(62dvh * 0.727));aspect-ratio:400/550;height:auto;border-radius:26px;background:linear-gradient(145deg,#ffffff 0%,#f0f4ff 100%);border:3px solid rgba(255,255,255,0.9);box-shadow:0 24px 60px rgba(0,0,0,0.55),0 4px 16px rgba(0,0,0,0.3);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;cursor:pointer;transition:transform 0.2s,box-shadow 0.2s;}
.top-card:hover{transform:translateY(-6px) rotate(-1deg);box-shadow:0 32px 70px rgba(0,0,0,0.6);}
.top-card:active{transform:translateY(-2px) scale(0.98);}
.card-num-badge{position:absolute;top:12px;right:14px;font-size:0.72em;color:rgba(80,100,160,0.6);font-weight:bold;}
.card-cat-badge{position:absolute;bottom:12px;font-size:0.62em;color:rgba(80,100,160,0.55);text-align:center;padding:0 12px;}
.card-emoji-big{font-size:clamp(4em,9vmin,9.5em);line-height:1;filter:drop-shadow(0 4px 8px rgba(0,0,0,0.18));}
.card-emoji-big.pop,.card-img.pop{animation:emojiPop 0.4s cubic-bezier(0.175,0.885,0.32,1.275);}
@keyframes emojiPop{0%{transform:scale(0.55) rotate(-8deg);}70%{transform:scale(1.18) rotate(3deg);}100%{transform:scale(1) rotate(0);}}
.card-img{width:88%;max-width:320px;height:auto;max-height:360px;object-fit:contain;filter:drop-shadow(0 6px 18px rgba(0,0,0,0.18));}
.card-name-big{font-size:2.4em;font-weight:bold;color:#1a2a4a;}
.card-pill{font-size:0.72em;padding:4px 14px;border-radius:50px;font-weight:bold;}
.card-pill.carnivore{background:#ff5252;color:#fff;}.card-pill.herbivore{background:#4caf50;color:#fff;}.card-pill.omnivore{background:#ff9800;color:#fff;}
.card-pill.spring{background:#66bb6a;color:#fff;}.card-pill.summer{background:#ffa726;color:#1a1a1a;}.card-pill.autumn{background:#ef6c00;color:#fff;}.card-pill.winter{background:#42a5f5;color:#fff;}.card-pill.any{background:#ab47bc;color:#fff;}
.deck-nav{display:flex;gap:14px;width:100%;justify-content:center;}
.nav-btn{flex:1;max-width:120px;background:rgba(255,255,255,0.12);border:2px solid rgba(255,255,255,0.3);color:#fff;font-size:1em;font-weight:bold;padding:12px 0;border-radius:50px;cursor:pointer;font-family:inherit;transition:0.22s;}
.nav-btn:hover{background:rgba(255,255,255,0.25);transform:translateY(-2px);}
.nav-btn:active{transform:translateY(0);}
.prog-strip{width:100%;}
.prog-bg{background:rgba(255,255,255,0.12);border-radius:50px;height:8px;overflow:hidden;}
.prog-fg{height:100%;background:linear-gradient(90deg,ACCENT,ACCENTLIGHT);border-radius:50px;transition:width 0.5s ease;}
.prog-txt{color:rgba(255,255,255,0.4);font-size:0.72em;text-align:center;margin-top:5px;}
.right-pane{flex:1;background:linear-gradient(140deg,#ffecd2 0%,#fcb69f 100%);display:flex;align-items:center;justify-content:center;padding:24px;position:relative;overflow-y:auto;overflow-x:hidden;}
.right-pane::before{content:'';position:absolute;inset:0;z-index:0;background-image:radial-gradient(rgba(0,0,0,0.07) 1px,transparent 1px);background-size:22px 22px;}
.machine{position:relative;z-index:1;background:MACHINEBG;border-radius:28px;padding:22px 24px 26px;width:100%;max-width:370px;box-shadow:0 0 0 3px rgba(255,255,255,0.08),0 28px 70px rgba(0,0,0,0.5),inset 0 1px 0 rgba(255,255,255,0.1);display:flex;flex-direction:column;align-items:center;gap:16px;}
.machine-plate{background:PLATEBG;border-radius:8px;padding:7px 22px;color:rgba(255,255,255,0.5);font-size:0.62em;letter-spacing:5px;text-transform:uppercase;border:1px solid rgba(255,255,255,0.1);box-shadow:inset 0 1px 3px rgba(0,0,0,0.4);}
.machine-screen{width:100%;background:#000;border-radius:16px;padding:16px 14px 14px;border:4px solid #0a0a0a;box-shadow:inset 0 0 28px SCREENGLOW,0 4px 12px rgba(0,0,0,0.5);display:flex;flex-direction:column;align-items:center;gap:7px;position:relative;overflow:hidden;}
.machine-screen::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 30%,SCREENGLOW2,transparent 70%);pointer-events:none;}
.machine-screen::after{content:'';position:absolute;inset:0;background:repeating-linear-gradient(0deg,transparent,transparent 3px,rgba(0,0,0,0.1) 3px,rgba(0,0,0,0.1) 4px);pointer-events:none;border-radius:12px;}
.scrn-emoji{font-size:5.2em;line-height:1;position:relative;z-index:1;filter:drop-shadow(0 0 12px SCREENDROP);transition:filter 0.3s;}
.scrn-emoji.flash,.scrn-img.flash{animation:screenFlash 0.6s ease;}
@keyframes screenFlash{0%{filter:drop-shadow(0 0 12px SCREENDROP) brightness(1);}35%{filter:drop-shadow(0 0 40px SCREENFLASH) brightness(1.6);}100%{filter:drop-shadow(0 0 12px SCREENDROP) brightness(1);}}
.scrn-img{width:140px;height:140px;object-fit:contain;position:relative;z-index:1;filter:drop-shadow(0 0 12px SCREENDROP);}
.scrn-name{font-size:1.75em;font-weight:bold;color:ACCENT;position:relative;z-index:1;text-shadow:0 0 14px ACCENTGLOW;letter-spacing:1px;font-family:'Courier New',monospace;}
.scrn-badge-pill{font-size:0.78em;padding:4px 16px;border-radius:50px;position:relative;z-index:1;font-family:'Courier New',monospace;font-weight:bold;}
.scrn-badge-pill.carnivore{background:rgba(239,83,80,0.25);border:1px solid #ef5350;color:#ef9a9a;}
.scrn-badge-pill.herbivore{background:rgba(102,187,106,0.25);border:1px solid #66bb6a;color:#a5d6a7;}
.scrn-badge-pill.omnivore{background:rgba(255,167,38,0.25);border:1px solid #ffa726;color:#ffcc80;}
.scrn-badge-pill.spring{background:rgba(102,187,106,0.25);border:1px solid #66bb6a;color:#a5d6a7;}
.scrn-badge-pill.summer{background:rgba(255,167,38,0.25);border:1px solid #ffa726;color:#ffcc80;}
.scrn-badge-pill.autumn{background:rgba(239,108,0,0.25);border:1px solid #ef6c00;color:#ffab40;}
.scrn-badge-pill.winter{background:rgba(100,181,246,0.25);border:1px solid #64b5f6;color:#bbdefb;}
.scrn-badge-pill.any{background:rgba(206,147,216,0.25);border:1px solid #ce93d8;color:#e1bee7;}
.scrn-badge-txt{font-size:0.68em;color:ACCENTDIM;text-align:center;position:relative;z-index:1;font-family:'Courier New',monospace;padding:2px 8px;}
.scrn-fact{font-size:0.7em;color:ACCENTDIM;text-align:center;line-height:1.45;max-width:250px;position:relative;z-index:1;font-family:'Courier New',monospace;min-height:3em;}
.grille{width:100%;background:linear-gradient(180deg,#080814,#040408);border-radius:12px;padding:12px 14px;border:1px solid rgba(255,255,255,0.05);}
.grille-row{display:flex;gap:5px;justify-content:center;margin-bottom:5px;}
.grille-row:last-child{margin-bottom:0;}
.grille-dot{width:7px;height:7px;border-radius:50%;background:rgba(255,255,255,0.1);box-shadow:inset 0 1px 2px rgba(0,0,0,0.5);transition:background 0.1s,box-shadow 0.1s;}
.grille-dot.lit{background:ACCENT;box-shadow:0 0 6px ACCENT,0 0 12px ACCENTGLOW;animation:dotPop 0.2s ease both;}
@keyframes dotPop{from{transform:scale(0.5);}to{transform:scale(1);}}
.waves{display:flex;align-items:center;justify-content:center;gap:4px;height:28px;opacity:0;transition:opacity 0.3s;}
.waves.active{opacity:1;}
.wv{width:4px;background:ACCENT;border-radius:4px;animation:wvPulse 0.7s ease-in-out infinite;}
.wv:nth-child(1){height:10px;animation-delay:0s;}.wv:nth-child(2){height:20px;animation-delay:0.1s;}.wv:nth-child(3){height:26px;animation-delay:0.2s;}.wv:nth-child(4){height:20px;animation-delay:0.3s;}.wv:nth-child(5){height:10px;animation-delay:0.4s;}
@keyframes wvPulse{0%,100%{transform:scaleY(0.4);opacity:0.5;}50%{transform:scaleY(1);opacity:1;}}
.press-btn{width:100%;background:BTNBG;border:none;border-radius:18px;padding:18px 14px;cursor:pointer;font-family:inherit;color:BTNTEXT;font-size:1.25em;font-weight:bold;text-align:center;line-height:1.3;box-shadow:0 8px 0 BTNSHADOW,0 12px 24px ACCENTGLOW;transition:all 0.12s;letter-spacing:0.5px;}
.press-btn:hover{background:HBTNBG;transform:translateY(-2px);}
.press-btn:active,.press-btn.pressed{transform:translateY(6px);box-shadow:0 2px 0 BTNSHADOW,0 4px 10px ACCENTGLOW;}
.btn-icon{font-size:1.2em;display:block;margin-bottom:3px;}
.btn-sub{font-size:0.6em;opacity:0.65;font-weight:normal;display:block;margin-top:2px;}
.done-overlay{display:none;position:absolute;inset:0;z-index:50;background:rgba(0,0,0,0.45);align-items:center;justify-content:center;}
.done-overlay.show{display:flex;}
.done-card{background:#fff;border-radius:24px;padding:38px 36px;text-align:center;max-width:320px;width:90%;box-shadow:0 20px 60px rgba(0,0,0,0.4);animation:popIn 0.5s cubic-bezier(0.175,0.885,0.32,1.275);}
.done-card h2{font-size:1.8em;color:ACCENT;margin:10px 0 8px;}
.done-card p{color:#555;font-size:0.95em;margin-bottom:20px;}
.restart-btn{background:BTNBG;color:BTNTEXT;border:none;border-radius:50px;padding:13px 36px;font-size:1em;font-weight:bold;cursor:pointer;font-family:inherit;box-shadow:0 5px 16px rgba(0,0,0,0.2);transition:0.22s;}
.restart-btn:hover{transform:translateY(-2px);}
@keyframes popIn{0%{transform:scale(0.5) rotate(-5deg);opacity:0;}100%{transform:scale(1) rotate(0);opacity:1;}}
.cf{position:fixed;pointer-events:none;z-index:9999;animation:cfFall 2.5s linear forwards;}
@keyframes cfFall{0%{transform:translateY(-10px) rotateZ(0);opacity:1;}100%{transform:translateY(105vh) rotateZ(720deg);opacity:0;}}
@media(max-height:900px) and (min-width:701px){
  .left-pane{gap:6px;padding:10px 14px 12px;overflow-y:auto;}.deck-area{min-height:0;}
  .card-emoji-big{font-size:4.2em;}.card-name-big{font-size:1.6em;}
  .right-pane{align-items:flex-start;overflow-y:auto;padding:16px 20px;}
  .machine{padding:10px 14px 14px;gap:8px;}.machine-plate{padding:5px 16px;font-size:0.55em;}
  .machine-screen{padding:10px 10px 10px;gap:5px;}.scrn-emoji{font-size:3em;}
  .scrn-img{width:80px;height:80px;}.scrn-name{font-size:1.4em;}.scrn-fact{font-size:0.65em;min-height:2.5em;}
  .grille{padding:8px 10px;}.waves{height:22px;}.press-btn{padding:8px 12px;font-size:1em;}
}
@media(max-width:700px){
  body{overflow-y:auto;}.layout{flex-direction:column;height:auto;min-height:100dvh;}
  .left-pane{width:100%;padding:14px 14px 18px;}.right-pane{padding:18px 14px 30px;}
  .machine{max-width:100%;}.top-card,.ghost{width:260px;}
  .card-emoji-big{font-size:6.5em;}.scrn-emoji{font-size:4.2em;}
}
"""

def themed_css(leftbg, ghostbg, machinebg, platebg,
               screenglow, screenglow2, screendrop, screenflash,
               hbtnbg, btnshadow, btntext, btnbg,
               accentglow, accentdark, accentlight, accentdim, accenttext, accent):
    # Replace longest variants first to avoid partial substitution
    return (BASE_CSS
        .replace("ACCENTGLOW",  accentglow)
        .replace("ACCENTDARK",  accentdark)
        .replace("ACCENTLIGHT", accentlight)
        .replace("ACCENTDIM",   accentdim)
        .replace("ACCENTTEXT",  accenttext)
        .replace("ACCENT",      accent)
        .replace("SCREENGLOW2", screenglow2)
        .replace("SCREENGLOW",  screenglow)
        .replace("SCREENDROP",  screendrop)
        .replace("SCREENFLASH", screenflash)
        .replace("HBTNBG",      hbtnbg)
        .replace("BTNSHADOW",   btnshadow)
        .replace("BTNTEXT",     btntext)
        .replace("BTNBG",       btnbg)
        .replace("LEFTBG",      leftbg)
        .replace("GHOSTBG",     ghostbg)
        .replace("MACHINEBG",   machinebg)
        .replace("PLATEBG",     platebg))


# ──────────────────────────────────────────────────────────────
#  SHARED JS LOGIC (written as a plain string — no .format())
# ──────────────────────────────────────────────────────────────
SHARED_LOGIC = r"""
function imgFail(img){var d=document.createElement("div");d.className="card-emoji-big pop";d.textContent=img.dataset.e;img.replaceWith(d);}
function imgFailScreen(img){var d=document.createElement("div");d.className="scrn-emoji";d.id="screenEmojiEl";d.textContent=img.dataset.e;img.replaceWith(d);}
function buildGrille(lit){
  var g=document.getElementById("grille");g.innerHTML="";
  for(var r=0;r<4;r++){var row=document.createElement("div");row.className="grille-row";for(var c=0;c<14;c++){var dot=document.createElement("div");dot.className="grille-dot"+(lit&&Math.random()>0.35?" lit":"");row.appendChild(dot);}g.appendChild(row);}
}
function navigate(dir){
  var next=idx+dir;
  if(next<0)return;
  if(next>=cards.length){checkDone();return;}
  idx=next;renderAll();
}
function pressMachine(){
  var btn=document.getElementById("pressBtn");btn.classList.add("pressed");setTimeout(function(){btn.classList.remove("pressed");},180);
  var sel=document.getElementById("screenEmojiEl");if(sel){sel.classList.remove("flash");void sel.offsetWidth;sel.classList.add("flash");}
  buildGrille(true);setTimeout(function(){buildGrille(false);},1100);
  document.getElementById("waves").classList.add("active");speak();
}
function speak(){
  if(!("speechSynthesis" in window))return;
  var card=cards[idx];window.speechSynthesis.cancel();
  var utt=new SpeechSynthesisUtterance(card.n+"!   "+card.f);utt.rate=0.9;utt.pitch=1.1;
  utt.onend=function(){document.getElementById("waves").classList.remove("active");};
  window.speechSynthesis.speak(utt);
}
function launchConfetti(){
  var cols=["#C1","#ffe030","#ff6b6b","#43cea2","#667eea","#f093fb","#84fab0","#fff"];
  for(var i=0;i<100;i++){(function(i){setTimeout(function(){var p=document.createElement("div");p.className="cf";var sz=8+Math.random()*12;p.style.cssText="width:"+sz+"px;height:"+sz+"px;left:"+(Math.random()*100)+"vw;top:-20px;background:"+cols[Math.floor(Math.random()*cols.length)]+";animation-duration:"+(1.6+Math.random()*2.2)+"s;border-radius:"+(Math.random()>0.5?"50%":"3px")+";";document.body.appendChild(p);setTimeout(function(){p.remove();},5000);},i*20);})(i);}
}
"""

# Replace confetti colour placeholder
def shared_js(accent_hex):
    return SHARED_LOGIC.replace('"#C1"', '"' + accent_hex + '"')

# ──────────────────────────────────────────────────────────────
#  PAGE BUILDER
# ──────────────────────────────────────────────────────────────
def build_page(title, css, heading, cat_bar_html, card_extra_html,
               screen_badge_html, total, first_prog,
               plate_text, btn_sub, done_title, restart_label, js_code):
    return (
"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>""" + title + """</title>
<style>""" + css + """</style>
</head>
<body>
<div class="layout">
  <div class="left-pane">
    <div class="left-top">
      <a href="../index.html" class="back-link">&#x1F3E0; Home</a>
      <span class="left-heading">""" + heading + """</span>
    </div>
    """ + cat_bar_html + """
    <div class="deck-area">
      <div class="ghost"></div><div class="ghost"></div><div class="ghost"></div>
      <div class="top-card" id="topCard" onclick="pressMachine()">
        <span class="card-num-badge" id="cardNum">1 / """ + str(total) + """</span>
        <div id="cardFace"></div>
        <div class="card-name-big" id="cardName"></div>
        """ + card_extra_html + """
      </div>
    </div>
    <div class="deck-nav">
      <button class="nav-btn" onclick="navigate(-1)">&#9664; Prev</button>
      <button class="nav-btn" onclick="navigate(1)">Next &#9654;</button>
    </div>
    <div class="prog-strip">
      <div class="prog-bg"><div class="prog-fg" id="progFg" style="width:""" + str(first_prog) + """%"></div></div>
      <div class="prog-txt" id="progTxt">Card 1 of """ + str(total) + """</div>
    </div>
  </div>
  <div class="right-pane">
    <div class="machine">
      <div class="machine-plate">""" + plate_text + """</div>
      <div class="machine-screen">
        <div id="screenFace"></div>
        <div class="scrn-name" id="screenName"></div>
        """ + screen_badge_html + """
        <div class="scrn-fact" id="screenFact"></div>
      </div>
      <div class="grille" id="grille"></div>
      <div class="waves" id="waves">
        <div class="wv"></div><div class="wv"></div><div class="wv"></div>
        <div class="wv"></div><div class="wv"></div>
      </div>
      <div class="press-btn" id="pressBtn" onclick="pressMachine()">
        <span class="btn-icon">&#128266;</span>
        TAP TO HEAR!
        <span class="btn-sub">""" + btn_sub + """</span>
      </div>
    </div>
    <div class="done-overlay" id="doneOverlay">
      <div class="done-card">
        <div style="font-size:3em">&#127881;</div>
        <h2>""" + done_title + """</h2>
        <p id="doneMsg"></p>
        <button class="restart-btn" onclick="restart()">""" + restart_label + """</button>
      </div>
    </div>
  </div>
</div>
<script>
""" + js_code + """
renderAll();
</script>
<script>if("serviceWorker" in navigator){navigator.serviceWorker.register("../service-worker.js");let r=false;navigator.serviceWorker.addEventListener("controllerchange",()=>{if(!r){r=true;location.reload();}});}</script>
</body>
</html>""")


# ═══════════════════════════════════════════════════════════
#  S O L A R   S Y S T E M
# ═══════════════════════════════════════════════════════════
solar_css = themed_css(
    leftbg     = "linear-gradient(160deg,#0f0c29 0%,#1a1650 50%,#302b63 100%)",
    ghostbg    = "linear-gradient(150deg,#1a2a6a 0%,#0d1445 100%)",
    machinebg  = "linear-gradient(170deg,#0f0c29 0%,#1a1650 100%)",
    platebg    = "linear-gradient(135deg,#22226a,#0f0c29)",
    screenglow = "rgba(247,201,72,0.08)",
    screenglow2= "rgba(247,201,72,0.07)",
    screendrop = "rgba(247,201,72,0.4)",
    screenflash= "rgba(247,201,72,1)",
    hbtnbg     = "linear-gradient(145deg,#ffd060,#f0b000)",
    btnshadow  = "#9a6800",
    btntext    = "#1a1a2e",
    btnbg      = "linear-gradient(145deg,#f7c948,#e8a000)",
    accentglow = "rgba(247,201,72,0.5)",
    accentdark = "#e8a000",
    accentlight= "#fff176",
    accentdim  = "rgba(247,201,72,0.55)",
    accenttext = "#1a1a2e",
    accent     = "#f7c948",
)

SOLAR_JS = r"""
var cards=[
  {e:"\u2600\uFE0F",img:"https://api.iconify.design/noto/sun.svg?width=120&height=120",n:"Sun",badge:"\u2B50 Star \u00B7 Centre of Solar System",f:"The Sun is a giant star! It gives light and warmth to all planets. About one million Earths could fit inside the Sun!"},
  {e:"\u26AB",img:"https://api.iconify.design/noto/new-moon.svg?width=120&height=120",n:"Mercury",badge:"\uD83E\uDEA8 1st Planet from the Sun",f:"Mercury is the smallest planet and the fastest mover \u2014 it zooms around the Sun in just 88 days!"},
  {e:"\uD83D\uDFE1",img:"https://api.iconify.design/noto/yellow-circle.svg?width=120&height=120",n:"Venus",badge:"\uD83D\uDD25 2nd Planet \u00B7 Hottest Planet",f:"Venus is the hottest planet \u2014 even hotter than Mercury! It is covered in thick poisonous clouds."},
  {e:"\uD83C\uDF0D",img:"https://api.iconify.design/noto/globe-showing-americas.svg?width=120&height=120",n:"Earth",badge:"\uD83C\uDF0A 3rd Planet \u00B7 Our Home",f:"Earth is our home \u2014 the only planet known to have liquid water, air to breathe, and living things!"},
  {e:"\uD83D\uDD34",img:"https://api.iconify.design/noto/red-circle.svg?width=120&height=120",n:"Mars",badge:"\uD83C\uDFDC\uFE0F 4th Planet \u00B7 The Red Planet",f:"Mars is called the Red Planet! It has the tallest volcano in the Solar System \u2014 Olympus Mons!"},
  {e:"\uD83D\uDFE4",img:"https://api.iconify.design/noto/brown-circle.svg?width=120&height=120",n:"Jupiter",badge:"\uD83D\uDC51 5th Planet \u00B7 Largest Planet",f:"Jupiter is the biggest planet \u2014 over 1,300 Earths can fit inside! It has a storm bigger than Earth called the Great Red Spot!"},
  {e:"\uD83E\uDE90",img:"https://api.iconify.design/noto/ringed-planet.svg?width=120&height=120",n:"Saturn",badge:"\uD83D\uDC8D 6th Planet \u00B7 Ring Planet",f:"Saturn has beautiful rings made of ice and rock! It is so light it could float on water \u2014 if there were an ocean big enough!"},
  {e:"\uD83D\uDD35",img:"https://api.iconify.design/noto/blue-circle.svg?width=120&height=120",n:"Uranus",badge:"\u2744\uFE0F 7th Planet \u00B7 Ice Giant",f:"Uranus is a blue ice giant that spins on its side like a rolling ball! It has 13 rings and 27 moons."},
  {e:"\uD83C\uDF00",img:"https://api.iconify.design/noto/blue-circle.svg?width=120&height=120",n:"Neptune",badge:"\uD83C\uDF2C\uFE0F 8th Planet \u00B7 Farthest Planet",f:"Neptune is the farthest planet from the Sun. It has the strongest winds in the Solar System \u2014 up to 2,100 km per hour!"},
  {e:"\uD83C\uDF15",img:"https://api.iconify.design/noto/full-moon.svg?width=120&height=120",n:"Moon",badge:"\uD83C\uDF0D Earth Natural Satellite",f:"The Moon is Earth natural satellite. In 1969, astronauts first walked on it \u2014 a giant leap for humankind!"},
  {e:"\uD83C\uDF17",img:"https://api.iconify.design/noto/last-quarter-moon.svg?width=120&height=120",n:"Pluto",badge:"\uD83E\uDDE3 Dwarf Planet \u00B7 Kuiper Belt",f:"Pluto was once the 9th planet, but in 2006 it was reclassified as a dwarf planet. It is smaller than our Moon!"}
];
var idx=0;
function renderAll(){
  var card=cards[idx],total=cards.length;
  var cf=document.getElementById("cardFace");
  cf.innerHTML='<img class="card-img" src="'+card.img+'" alt="'+card.n+'" data-e="'+card.e+'" onerror="imgFail(this)">';
  var inner=cf.firstChild;if(inner){inner.classList.remove("pop");void inner.offsetWidth;inner.classList.add("pop");}
  document.getElementById("cardName").textContent=card.n;
  document.getElementById("cardNum").textContent=(idx+1)+" / "+total;
  document.getElementById("cardCatBadge").textContent=card.badge;
  document.getElementById("screenFace").innerHTML='<img class="scrn-img" id="screenEmojiEl" src="'+card.img+'" alt="'+card.n+'" data-e="'+card.e+'" onerror="imgFailScreen(this)">';
  document.getElementById("screenName").textContent=card.n;
  document.getElementById("screenBadge").textContent=card.badge;
  document.getElementById("screenFact").textContent=card.f;
  document.getElementById("progFg").style.width=((idx+1)/total*100)+"%";
  document.getElementById("progTxt").textContent="Card "+(idx+1)+" of "+total;
  buildGrille(false);
}
function checkDone(){
  document.getElementById("doneMsg").textContent="Amazing! You explored all "+cards.length+" objects in the Solar System!";
  document.getElementById("doneOverlay").classList.add("show");launchConfetti();
}
function restart(){idx=0;document.getElementById("doneOverlay").classList.remove("show");renderAll();}
""" + shared_js("#f7c948")

solar_html = build_page(
    title         = "Solar System Cards",
    css           = solar_css,
    heading       = "&#x1FA90; Solar System",
    cat_bar_html  = "",
    card_extra_html = '<span class="card-cat-badge" id="cardCatBadge"></span>',
    screen_badge_html = '<div class="scrn-badge-txt" id="screenBadge"></div>',
    total         = 11,
    first_prog    = 9,
    plate_text    = "&#11088; Solar System Cards &#11088;",
    btn_sub       = "Press &#8212; I will tell you about this space object!",
    done_title    = "Amazing Job!",
    restart_label = "&#128260; Explore Again",
    js_code       = SOLAR_JS,
)


# ═══════════════════════════════════════════════════════════
#  D I N O S A U R S
# ═══════════════════════════════════════════════════════════
dino_css = themed_css(
    leftbg     = "linear-gradient(160deg,#0a1a05 0%,#122a0a 50%,#1a3a10 100%)",
    ghostbg    = "linear-gradient(150deg,#0d2205 0%,#0a1a05 100%)",
    machinebg  = "linear-gradient(170deg,#0f1a08 0%,#162210 100%)",
    platebg    = "linear-gradient(135deg,#1a3a08,#0f1a05)",
    screenglow = "rgba(124,205,66,0.08)",
    screenglow2= "rgba(124,205,66,0.07)",
    screendrop = "rgba(124,205,66,0.4)",
    screenflash= "rgba(124,205,66,1)",
    hbtnbg     = "linear-gradient(145deg,#90d958,#5aaa20)",
    btnshadow  = "#2d5a08",
    btntext    = "#fff",
    btnbg      = "linear-gradient(145deg,#7ccd42,#4a9010)",
    accentglow = "rgba(124,205,66,0.5)",
    accentdark = "#4a9010",
    accentlight= "#a8e063",
    accentdim  = "rgba(168,224,99,0.55)",
    accenttext = "#fff",
    accent     = "#7ccd42",
)

DINO_JS = r"""
var ALL_CARDS=[
  {e:"\uD83E\uDD96",img:"https://api.iconify.design/noto/t-rex.svg?width=120&height=120",n:"T-Rex",diet:"carnivore",f:"T-Rex was one of the most feared hunters ever! It had tiny arms but the most powerful bite of any land animal \u2014 able to crush bone!"},
  {e:"\uD83E\uDD95",img:"https://api.iconify.design/noto/triceratops.svg?width=120&height=120",n:"Triceratops",diet:"herbivore",f:"Triceratops had three sharp horns and a huge bony frill on its head. It used them to defend against T-Rex and fight rival Triceratops!"},
  {e:"\uD83E\uDD95",img:"https://api.iconify.design/noto/sauropod.svg?width=120&height=120",n:"Brachiosaurus",diet:"herbivore",f:"Brachiosaurus was one of the tallest dinosaurs \u2014 as tall as a 5-storey building! It stretched its long neck to eat treetop leaves."},
  {e:"\uD83E\uDD95",img:"https://api.iconify.design/noto/sauropod.svg?width=120&height=120",n:"Stegosaurus",diet:"herbivore",f:"Stegosaurus had large bony plates along its back and sharp spikes on its tail. Its brain was only the size of a walnut!"},
  {e:"\uD83E\uDD96",img:"https://api.iconify.design/noto/t-rex.svg?width=120&height=120",n:"Velociraptor",diet:"carnivore",f:"Velociraptors were fast and smart hunters. They hunted in packs and had a deadly curved claw on each foot. They were actually feathered!"},
  {e:"\uD83E\uDD85",img:"https://api.iconify.design/noto/eagle.svg?width=120&height=120",n:"Pterodactyl",diet:"carnivore",f:"Pterodactyl was a flying reptile, not a dinosaur! It soared on wide leathery wings and swooped to catch fish from lakes and seas."},
  {e:"\uD83E\uDD95",img:"https://api.iconify.design/noto/sauropod.svg?width=120&height=120",n:"Diplodocus",diet:"herbivore",f:"Diplodocus was one of the longest dinosaurs at up to 27 metres! It used its whip-like tail to make sonic boom sounds to scare predators!"},
  {e:"\uD83D\uDC22",img:"https://api.iconify.design/noto/turtle.svg?width=120&height=120",n:"Ankylosaurus",diet:"herbivore",f:"Ankylosaurus was like a living tank! Its whole body was covered in thick bony armour, and its tail had a huge club that could break bones!"},
  {e:"\uD83E\uDD96",img:"https://api.iconify.design/noto/t-rex.svg?width=120&height=120",n:"Spinosaurus",diet:"carnivore",f:"Spinosaurus was even bigger than T-Rex \u2014 the largest meat-eating dinosaur! It had a huge sail on its back and loved to catch fish."},
  {e:"\uD83E\uDD8E",img:"https://api.iconify.design/noto/lizard.svg?width=120&height=120",n:"Iguanodon",diet:"herbivore",f:"Iguanodon was one of the first dinosaurs ever discovered! It had a spike-like thumb claw it used to pull down branches to eat."},
  {e:"\uD83C\uDFBA",img:"https://api.iconify.design/noto/sauropod.svg?width=120&height=120",n:"Parasaurolophus",diet:"herbivore",f:"Parasaurolophus had a long hollow crest on its head it used like a musical instrument to make loud booming calls to its herd!"},
  {e:"\uD83E\uDD96",img:"https://api.iconify.design/noto/t-rex.svg?width=120&height=120",n:"Allosaurus",diet:"carnivore",f:"Allosaurus was the top predator of the Jurassic period. It could open its upper jaw wide like a hatchet to slice into large prey!"},
  {e:"\uD83E\uDEA8",img:"https://api.iconify.design/noto/lizard.svg?width=120&height=120",n:"Pachycephalosaurus",diet:"omnivore",f:"Pachycephalosaurus had a super-thick dome skull up to 25 cm thick! Males would head-butt each other to compete for the herd!"},
  {e:"\uD83D\uDC26",img:"https://api.iconify.design/noto/lizard.svg?width=120&height=120",n:"Compsognathus",diet:"carnivore",f:"Compsognathus was one of the tiniest dinosaurs \u2014 about the size of a chicken! But it was a speedy little hunter that chased lizards and insects."},
  {e:"\uD83E\uDDA3",img:"https://api.iconify.design/noto/mammoth.svg?width=120&height=120",n:"Mammoth",diet:"herbivore",f:"The Woolly Mammoth lived during the Ice Age! It had long curved tusks and a thick furry coat to stay warm. Early humans painted pictures of them!"}
];
var cards=ALL_CARDS.slice();
var idx=0;
var activeFilter="all";
var FILTERS=[["all","All \uD83E\uDD95"],["carnivore","\uD83E\uDD69 Carnivore"],["herbivore","\uD83C\uDF3F Herbivore"],["omnivore","\uD83C\uDF7D\uFE0F Omnivore"]];
function buildCatBar(){
  var bar=document.getElementById("catBar");bar.innerHTML="";
  FILTERS.forEach(function(f){
    var btn=document.createElement("button");btn.className="cat-btn"+(activeFilter===f[0]?" active":"");
    btn.textContent=f[1];btn.dataset.key=f[0];btn.onclick=function(){setFilter(f[0]);};
    bar.appendChild(btn);
  });
}
function setFilter(key){
  activeFilter=key;
  cards=key==="all"?ALL_CARDS.slice():ALL_CARDS.filter(function(c){return c.diet===key;});
  idx=0;
  document.querySelectorAll(".cat-btn").forEach(function(b){b.classList.toggle("active",b.dataset.key===key);});
  document.getElementById("doneOverlay").classList.remove("show");
  renderAll();
}
function renderAll(){
  var card=cards[idx],total=cards.length;
  var cf=document.getElementById("cardFace");
  cf.innerHTML='<img class="card-img" src="'+card.img+'" alt="'+card.n+'" data-e="'+card.e+'" onerror="imgFail(this)">';
  var inner=cf.firstChild;if(inner){inner.classList.remove("pop");void inner.offsetWidth;inner.classList.add("pop");}
  document.getElementById("cardName").textContent=card.n;
  document.getElementById("cardNum").textContent=(idx+1)+" / "+total;
  var dp=document.getElementById("cardPill");dp.textContent=card.diet.charAt(0).toUpperCase()+card.diet.slice(1);dp.className="card-pill "+card.diet;
  document.getElementById("screenFace").innerHTML='<img class="scrn-img" id="screenEmojiEl" src="'+card.img+'" alt="'+card.n+'" data-e="'+card.e+'" onerror="imgFailScreen(this)">';
  document.getElementById("screenName").textContent=card.n;
  var sb=document.getElementById("screenBadge");
  sb.textContent=(card.diet==="carnivore"?"\uD83E\uDD69 ":card.diet==="herbivore"?"\uD83C\uDF3F ":"\uD83C\uDF7D\uFE0F ")+card.diet.charAt(0).toUpperCase()+card.diet.slice(1);
  sb.className="scrn-badge-pill "+card.diet;
  document.getElementById("screenFact").textContent=card.f;
  document.getElementById("progFg").style.width=((idx+1)/total*100)+"%";
  document.getElementById("progTxt").textContent="Card "+(idx+1)+" of "+total;
  buildGrille(false);
}
function checkDone(){
  document.getElementById("doneMsg").textContent="Roarsome! You met all "+cards.length+" dinosaurs!";
  document.getElementById("doneOverlay").classList.add("show");launchConfetti();
}
function restart(){idx=0;activeFilter="all";cards=ALL_CARDS.slice();document.getElementById("doneOverlay").classList.remove("show");buildCatBar();renderAll();}
buildCatBar();
""" + shared_js("#7ccd42")

dino_html = build_page(
    title         = "Dinosaurs Cards",
    css           = dino_css,
    heading       = "&#x1F995; Dinosaurs",
    cat_bar_html  = '<div class="cat-bar" id="catBar"></div>',
    card_extra_html = '<div class="card-pill" id="cardPill"></div>',
    screen_badge_html = '<div class="scrn-badge-pill" id="screenBadge"></div>',
    total         = 15,
    first_prog    = 7,
    plate_text    = "&#x1F995; Dino Cards &#x1F995;",
    btn_sub       = "Press &#8212; I will tell you about this dinosaur!",
    done_title    = "Roarsome!",
    restart_label = "&#128260; Meet Again",
    js_code       = DINO_JS,
)


# ═══════════════════════════════════════════════════════════
#  W E A T H E R
# ═══════════════════════════════════════════════════════════
weather_css = themed_css(
    leftbg     = "linear-gradient(160deg,#0a1428 0%,#14284e 50%,#1e3c72 100%)",
    ghostbg    = "linear-gradient(150deg,#0a1c3a 0%,#050e1e 100%)",
    machinebg  = "linear-gradient(170deg,#050e1e 0%,#0a1c3a 100%)",
    platebg    = "linear-gradient(135deg,#0d2050,#050e1e)",
    screenglow = "rgba(100,181,246,0.08)",
    screenglow2= "rgba(100,181,246,0.07)",
    screendrop = "rgba(100,181,246,0.4)",
    screenflash= "rgba(100,181,246,1)",
    hbtnbg     = "linear-gradient(145deg,#80c8ff,#1e7ee0)",
    btnshadow  = "#0d47a1",
    btntext    = "#fff",
    btnbg      = "linear-gradient(145deg,#64b5f6,#1565c0)",
    accentglow = "rgba(100,181,246,0.5)",
    accentdark = "#1565c0",
    accentlight= "#90caf9",
    accentdim  = "rgba(100,181,246,0.55)",
    accenttext = "#fff",
    accent     = "#64b5f6",
)

WEATHER_JS = r"""
var ALL_CARDS=[
  {e:"\u2600\uFE0F",img:"https://api.iconify.design/noto/sun.svg?width=120&height=120",n:"Sunny",season:"summer",f:"On a sunny day the sky is clear and blue. The Sun shines brightly keeping us warm. Great day for playing outside!"},
  {e:"\u2601\uFE0F",img:"https://api.iconify.design/noto/cloud.svg?width=120&height=120",n:"Cloudy",season:"any",f:"Clouds are made of millions of tiny water droplets floating in the sky. They come in many shapes \u2014 fluffy, flat, wispy and more!"},
  {e:"\uD83C\uDF27\uFE0F",img:"https://api.iconify.design/noto/cloud-with-rain.svg?width=120&height=120",n:"Rainy",season:"any",f:"Rain falls when water droplets in clouds become too heavy. Rain fills our rivers and helps plants and flowers grow!"},
  {e:"\u26C8\uFE0F",img:"https://api.iconify.design/noto/cloud-with-lightning-and-rain.svg?width=120&height=120",n:"Thunderstorm",season:"summer",f:"During a thunderstorm lightning flashes and thunder booms! Lightning is a giant spark of electricity. Always stay indoors when there is lightning!"},
  {e:"\u2744\uFE0F",img:"https://api.iconify.design/noto/cloud-with-snow.svg?width=120&height=120",n:"Snowy",season:"winter",f:"Snowflakes form when water freezes high in the clouds. Every single snowflake has a unique six-sided shape \u2014 no two are ever exactly alike!"},
  {e:"\uD83D\uDCA8",img:"https://api.iconify.design/noto/wind-face.svg?width=120&height=120",n:"Windy",season:"any",f:"Wind is moving air! Warm air rises and cool air rushes in to take its place. It can be a gentle breeze or a powerful storm!"},
  {e:"\uD83C\uDF08",img:"https://api.iconify.design/noto/rainbow.svg?width=120&height=120",n:"Rainbow",season:"spring",f:"A rainbow appears when sunlight shines through raindrops. It always has the same 7 colours: Red, Orange, Yellow, Green, Blue, Indigo, Violet!"},
  {e:"\uD83C\uDF2B\uFE0F",img:"https://api.iconify.design/noto/fog.svg?width=120&height=120",n:"Foggy",season:"autumn",f:"Fog is like a cloud that sits right on the ground! It makes it hard to see far away. Fog usually disappears after the Sun warms the air in the morning."},
  {e:"\uD83C\uDF28\uFE0F",img:"https://api.iconify.design/noto/cloud-with-snow.svg?width=120&height=120",n:"Hailstorm",season:"spring",f:"Hail is balls of ice that fall from thunderclouds! They form when raindrops get carried high up in the cold part of a storm cloud and freeze."},
  {e:"\uD83C\uDF21\uFE0F",img:"https://api.iconify.design/noto/thermometer.svg?width=120&height=120",n:"Hot",season:"summer",f:"Very hot weather happens in summer \u2014 the hottest season. People cool off by drinking water, swimming and eating ice cream!"},
  {e:"\uD83E\uDD76",img:"https://api.iconify.design/noto/cold-face.svg?width=120&height=120",n:"Cold",season:"winter",f:"Cold weather comes in winter. We wear coats, scarves and gloves to stay warm. Water turns to ice and puddles can freeze solid overnight!"},
  {e:"\uD83C\uDF38",img:"https://api.iconify.design/noto/cherry-blossom.svg?width=120&height=120",n:"Spring",season:"spring",f:"Spring is warm and fresh! Flowers bloom, trees grow new leaves and baby animals are born. After cold winter, spring feels wonderful!"},
  {e:"\uD83C\uDF1E",img:"https://api.iconify.design/noto/sun-with-face.svg?width=120&height=120",n:"Summer",season:"summer",f:"Summer is the hottest season with the longest days. The Sun stays up late! Perfect for beaches, ice cream and outdoor adventures!"},
  {e:"\uD83C\uDF42",img:"https://api.iconify.design/noto/fallen-leaf.svg?width=120&height=120",n:"Autumn",season:"autumn",f:"In autumn leaves turn beautiful shades of red, orange and yellow before falling. Animals like squirrels collect food for winter!"},
  {e:"\u26C4",img:"https://api.iconify.design/noto/snowflake.svg?width=120&height=120",n:"Winter",season:"winter",f:"Winter is the coldest season with the shortest days. It can snow, making the world look white and magical. Time for hot chocolate and cosy blankets!"},
  {e:"\uD83C\uDF00",img:"https://api.iconify.design/noto/cyclone.svg?width=120&height=120",n:"Hurricane",season:"summer",f:"A hurricane is a massive spinning storm with very strong winds over warm ocean water. It can bring heavy rain and flooding. Always stay safe!"},
  {e:"\uD83C\uDFDC\uFE0F",img:"https://api.iconify.design/noto/sun.svg?width=120&height=120",n:"Drought",season:"summer",f:"A drought happens when a place gets very little or no rain for a long time. The ground dries up, rivers shrink and water becomes precious!"},
  {e:"\uD83C\uDF2A\uFE0F",img:"https://api.iconify.design/noto/tornado.svg?width=120&height=120",n:"Tornado",season:"spring",f:"A tornado is a fast-spinning funnel of wind that touches the ground. It can pick up cars and trees! Tornado Alley in the USA sees hundreds every year!"},
  {e:"\u26C5",img:"https://api.iconify.design/noto/sun-behind-cloud.svg?width=120&height=120",n:"Partly Cloudy",season:"any",f:"Partly cloudy means some clouds in the sky but also sunshine! One of the most common types of weather \u2014 not too hot, not too gloomy!"},
  {e:"\uD83C\uDF28\uFE0F",img:"https://api.iconify.design/noto/cloud-with-snow.svg?width=120&height=120",n:"Blizzard",season:"winter",f:"A blizzard is a very heavy snowstorm with strong winds that blow snow everywhere. It can be hard to see even a few steps ahead \u2014 called a whiteout!"}
];
var cards=ALL_CARDS.slice();
var idx=0;
var activeFilter="all";
var SEASON_EMOJI={spring:"\uD83C\uDF38",summer:"\u2600\uFE0F",autumn:"\uD83C\uDF42",winter:"\u2744\uFE0F",any:"\uD83C\uDFB4"};
var FILTERS=[["all","All \uD83C\uDF24\uFE0F"],["spring","\uD83C\uDF38 Spring"],["summer","\u2600\uFE0F Summer"],["autumn","\uD83C\uDF42 Autumn"],["winter","\u2744\uFE0F Winter"],["any","\uD83C\uDFB4 Any Season"]];
function buildCatBar(){
  var bar=document.getElementById("catBar");bar.innerHTML="";
  FILTERS.forEach(function(f){
    var btn=document.createElement("button");btn.className="cat-btn"+(activeFilter===f[0]?" active":"");
    btn.textContent=f[1];btn.dataset.key=f[0];btn.onclick=function(){setFilter(f[0]);};
    bar.appendChild(btn);
  });
}
function setFilter(key){
  activeFilter=key;
  cards=key==="all"?ALL_CARDS.slice():ALL_CARDS.filter(function(c){return c.season===key;});
  idx=0;
  document.querySelectorAll(".cat-btn").forEach(function(b){b.classList.toggle("active",b.dataset.key===key);});
  document.getElementById("doneOverlay").classList.remove("show");
  renderAll();
}
function renderAll(){
  var card=cards[idx],total=cards.length;
  var cf=document.getElementById("cardFace");
  cf.innerHTML='<img class="card-img" src="'+card.img+'" alt="'+card.n+'" data-e="'+card.e+'" onerror="imgFail(this)">';
  var inner=cf.firstChild;if(inner){inner.classList.remove("pop");void inner.offsetWidth;inner.classList.add("pop");}
  document.getElementById("cardName").textContent=card.n;
  document.getElementById("cardNum").textContent=(idx+1)+" / "+total;
  var dp=document.getElementById("cardPill");dp.textContent=(SEASON_EMOJI[card.season]||"")+card.season.charAt(0).toUpperCase()+card.season.slice(1);dp.className="card-pill "+card.season;
  document.getElementById("screenFace").innerHTML='<img class="scrn-img" id="screenEmojiEl" src="'+card.img+'" alt="'+card.n+'" data-e="'+card.e+'" onerror="imgFailScreen(this)">';
  document.getElementById("screenName").textContent=card.n;
  var sb=document.getElementById("screenBadge");
  sb.textContent=(SEASON_EMOJI[card.season]||"")+card.season.charAt(0).toUpperCase()+card.season.slice(1);
  sb.className="scrn-badge-pill "+card.season;
  document.getElementById("screenFact").textContent=card.f;
  document.getElementById("progFg").style.width=((idx+1)/total*100)+"%";
  document.getElementById("progTxt").textContent="Card "+(idx+1)+" of "+total;
  buildGrille(false);
}
function checkDone(){
  document.getElementById("doneMsg").textContent="Brilliant! You learnt all "+cards.length+" types of weather!";
  document.getElementById("doneOverlay").classList.add("show");launchConfetti();
}
function restart(){idx=0;activeFilter="all";cards=ALL_CARDS.slice();document.getElementById("doneOverlay").classList.remove("show");buildCatBar();renderAll();}
buildCatBar();
""" + shared_js("#64b5f6")

weather_html = build_page(
    title         = "Weather and Seasons Cards",
    css           = weather_css,
    heading       = "&#x1F326;&#xFE0F; Weather",
    cat_bar_html  = '<div class="cat-bar" id="catBar"></div>',
    card_extra_html = '<div class="card-pill" id="cardPill"></div>',
    screen_badge_html = '<div class="scrn-badge-pill" id="screenBadge"></div>',
    total         = 20,
    first_prog    = 5,
    plate_text    = "&#x1F326;&#xFE0F; Weather Cards &#x1F326;&#xFE0F;",
    btn_sub       = "Press &#8212; I will tell you about this weather!",
    done_title    = "Brilliant!",
    restart_label = "&#128260; Play Again",
    js_code       = WEATHER_JS,
)


# ──────────────────────────────────────────────────────────────
#  WRITE FILES
# ──────────────────────────────────────────────────────────────
files = [
    (GAMES / "solar-system-game.html", solar_html,   "Solar System"),
    (GAMES / "dinosaurs-game.html",    dino_html,    "Dinosaurs"),
    (GAMES / "weather-game.html",      weather_html, "Weather"),
]

for path, content, label in files:
    path.write_text(content, encoding="utf-8")
    print(f"  OK  {label:20s}  {path.name}  ({len(content):,} chars)")

print("\nDone!")
