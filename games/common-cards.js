/* Shared JS for card-machine games: localStorage helpers, achievements, stats, settings, modals */

var _audioCtx=null;
function _getAudioCtx(){if(!_audioCtx)_audioCtx=new(window.AudioContext||window.webkitAudioContext)();return _audioCtx;}

function lsGet(k,def){try{var v=localStorage.getItem(GAME_KEY+"_"+k);return v?JSON.parse(v):def;}catch(e){return def;}}
function lsSet(k,v){try{localStorage.setItem(GAME_KEY+"_"+k,JSON.stringify(v));}catch(e){}}

function checkAchievementsBase(totalCards,statsObj,achObj,achDefs,learnedSize){
  var changed=false;
  if(!achObj.first_step&&learnedSize>=1){achObj.first_step=true;changed=true;showAchToast(achDefs[0]);}
  if(!achObj.halfway&&learnedSize>=Math.ceil(totalCards/2)){achObj.halfway=true;changed=true;showAchToast(achDefs[1]);}
  if(!achObj.all_learned&&learnedSize>=totalCards){achObj.all_learned=true;changed=true;showAchToast(achDefs[2]);}
  if(!achObj.quiz_master&&statsObj.quizzes>=5){achObj.quiz_master=true;changed=true;showAchToast(achDefs[4]);}
  if(changed)lsSet("achievements",achObj);
}

function showAchToast(ach){
  var t=document.createElement("div");t.className="ach-toast";t.innerHTML=ach.icon+" <b>"+ach.name+"</b> unlocked!";
  document.body.appendChild(t);setTimeout(function(){t.style.opacity="0";t.style.transition="opacity 0.4s";setTimeout(function(){t.remove();},500);},2800);
}

function playCorrectSound(){
  try{var a=_getAudioCtx(),o=a.createOscillator(),g=a.createGain();o.connect(g);g.connect(a.destination);o.frequency.value=880;g.gain.value=0.1;o.start();o.stop(a.currentTime+0.15);}catch(e){}
}

function launchConfettiCanvas(cols){
  var cvs=document.createElement("canvas");cvs.style.cssText="position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:99999;";
  cvs.width=window.innerWidth;cvs.height=window.innerHeight;document.body.appendChild(cvs);
  var ctx=cvs.getContext("2d"),ps=[];
  for(var i=0;i<80;i++)ps.push({x:Math.random()*cvs.width,y:Math.random()*-cvs.height*0.5,s:4+Math.random()*8,c:cols[Math.floor(Math.random()*cols.length)],vy:1.5+Math.random()*3,vx:(Math.random()-0.5)*2,r:Math.random()>0.5});
  var af,t=0;(function draw(){ctx.clearRect(0,0,cvs.width,cvs.height);var alive=false;ps.forEach(function(p){p.y+=p.vy;p.x+=p.vx;p.vy+=0.03;if(p.y<cvs.height+20){alive=true;ctx.fillStyle=p.c;if(p.r){ctx.beginPath();ctx.arc(p.x,p.y,p.s/2,0,6.28);ctx.fill();}else{ctx.fillRect(p.x,p.y,p.s,p.s);}}});t++;if(alive&&t<300){af=requestAnimationFrame(draw);}else{cancelAnimationFrame(af);cvs.remove();}})();
}

function initModalDismiss(closeFns){
  document.addEventListener("keydown",function(e){if(e.key==="Escape"){closeFns.forEach(function(fn){fn();});}});
  document.querySelectorAll(".modal-overlay").forEach(function(ov){ov.addEventListener("click",function(e){if(e.target===ov){closeFns.forEach(function(fn){fn();});}});});
}

function initBuildInfo(){
  var K='_buildInfo',T='_buildInfoT',el=document.getElementById('build-info');
  if(!el)return;
  var c=localStorage.getItem(K),ct=+localStorage.getItem(T)||0;
  if(c&&Date.now()-ct<300000){el.textContent=c;return;}
  fetch('https://api.github.com/repos/aakash-jain-1/kids-learning-games/commits/main').then(function(r){return r.json();}).then(function(d){var t='Build: '+d.sha.slice(0,7)+' \xB7 '+d.commit.committer.date.slice(0,10);el.textContent=t;try{localStorage.setItem(K,t);localStorage.setItem(T,''+Date.now());}catch(e){}}).catch(function(){if(c)el.textContent=c;});
}

/* Settings helpers */
function applySettingsBase(settings){
  document.body.classList.toggle("dark-mode",settings.dark);
  document.body.classList.remove("font-small","font-medium","font-large");
  document.body.classList.add("font-"+settings.fontSize);
  var togDark=document.getElementById("togDark");if(togDark)togDark.checked=settings.dark;
  var togSound=document.getElementById("togSound");if(togSound)togSound.checked=settings.sound;
  var togSpeak=document.getElementById("togSpeak");if(togSpeak)togSpeak.checked=settings.autoSpeak;
  document.querySelectorAll(".font-btn").forEach(function(b){b.classList.toggle("active",b.getAttribute("data-size")===settings.fontSize);});
}
