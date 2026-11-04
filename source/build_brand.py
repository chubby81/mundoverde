"""Build vector logo masters and a static design preview. Run from the original workspace.
Requires fontTools and the supplied DejaVu Sans installation; no network access.
"""
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import json, shutil, re, html

ROOT=Path(__file__).resolve().parents[1]
ASSETS=ROOT/'assets'
COLORS={'forest':'#193E32','moss':'#47683F','paper':'#F5F3EB','sage':'#DCE6D5','ink':'#20382E','muted':'#526458','earth':'#77624F','line':'#C5CFC1'}
FONT=Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
font=TTFont(FONT); glyphs=font.getGlyphSet(); cmap=font.getBestCmap(); scale=100/font['head'].unitsPerEm

def letters(word,x,color):
    parts=[]
    for c in word:
        name=cmap[ord(c)];pen=SVGPathPen(glyphs)
        glyphs[name].draw(TransformPen(pen,(scale,0,0,-scale,x,88)))
        parts.append(f'<path fill="{color}" d="{pen.getCommands()}"/>')
        x+=font['hmtx'][name][0]*scale-1.5
    return ''.join(parts),x

V_BODY='M0 32 H10 L27 76 L44 32 H54 L33 88 H21 Z'
V_LEAF='M44 33 C43 19 51 13 65 12 C64 26 57 33 44 33 Z'

def mark(x=0,color=COLORS['moss'],micro=False):
    return f'<g transform="translate({x} 0)" fill="{color}"><path d="{V_BODY}"/>'+('' if micro else f'<path d="{V_LEAF}"/>')+'</g>'

def wordmark(first=COLORS['forest'],second=COLORS['moss']):
    left,x=letters('mundo',14,first)
    x+=1
    v=mark(x,second)
    right,end=letters('erde',x+63,second)
    return left+v+right,round(end+12,2)

def svg(body,w,h,title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{title}</title>{body}</svg>'

for name,first,second in [('primary',COLORS['forest'],COLORS['moss']),('mono',COLORS['forest'],COLORS['forest']),('white','#FFFFFF','#FFFFFF')]:
    body,width=wordmark(first,second)
    (ASSETS/f'mundoverde-wordmark-{name}.svg').write_text(svg(body,width,112,'mundoverde'),encoding='utf8')
for name,color in [('green',COLORS['moss']),('mono',COLORS['forest']),('white','#FFFFFF')]:
    (ASSETS/f'mundoverde-symbol-{name}.svg').write_text(svg(mark(17,color),100,100,'mundoverde – v als Keimling'),encoding='utf8')
micro='<rect width="64" height="64" rx="14" fill="#193E32"/><g transform="translate(13 -11) scale(.7)" fill="#F5F3EB"><path d="'+V_BODY+'"/></g>'
(ASSETS/'mundoverde-favicon.svg').write_text(svg(micro,64,64,'mundoverde'),encoding='utf8')
(ASSETS/'mundoverde-symbol-micro.svg').write_text(svg('<g transform="translate(0 -10)">'+mark(17,COLORS['forest'],True)+'</g>',100,100,'mundoverde – v'),encoding='utf8')

def lum(h):
    rgb=[int(h[i:i+2],16)/255 for i in (1,3,5)]
    rgb=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in rgb]
    return sum(a*b for a,b in zip(rgb,[.2126,.7152,.0722]))
def contrast(a,b):
    light,dark=sorted([lum(a),lum(b)],reverse=True)
    return (light+.05)/(dark+.05)
pairs=[('Text','ink','paper'),('Sekundärtext','muted','paper'),('Link / Fokus','moss','paper'),('Button','paper','forest'),('Text auf Salbei','ink','sage'),('Erdton','earth','paper')]
results=[{'use':n,'foreground':COLORS[a],'background':COLORS[b],'ratio':round(contrast(COLORS[a],COLORS[b]),2),'AA_normal_text':contrast(COLORS[a],COLORS[b])>=4.5} for n,a,b in pairs]
assert all(r['AA_normal_text'] for r in results)
(ROOT/'validation/contrast.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))

body,width=wordmark()
board=['<rect width="1600" height="1200" fill="#F5F3EB"/>']
def text(x,y,s,size=22,color='#193E32'):
    board.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans,sans-serif" font-size="{size}" fill="{color}">{html.escape(s)}</text>')
text(80,68,'MUNDOVERDE / IDENTITÄT 01',18)
text(80,109,'Eine grüne Welt. Ein klarer Blick.',24)
board.append(f'<g transform="translate(65 160) scale(1.95)">{body}</g>')
text(80,424,'WELT + GRÜN',16)
text(80,470,'Das v wird zum Keimling.',32)
text(80,510,'Ein lesbarer Buchstabe. Ein Zeichen für Wachstum.',21,'#526458')
board.append('<rect x="1150" y="390" width="360" height="180" rx="8" fill="#DCE6D5"/>')
board.append(f'<g transform="translate(1275 405) scale(1.5)">{mark(0)}</g>')
for i,(name,key) in enumerate([('Wald','forest'),('Moos','moss'),('Papier','paper'),('Salbei','sage'),('Erde','earth')]):
    x=80+i*292
    board.append(f'<rect x="{x}" y="630" width="270" height="115" rx="4" fill="{COLORS[key]}" stroke="#C5CFC1"/>')
    text(x,783,name,22);text(x,818,COLORS[key],18,'#526458')
text(80,910,'Wortmarke',18)
mono,_=wordmark(COLORS['forest'],COLORS['forest'])
board.append(f'<g transform="translate(73 938) scale(.68)">{mono}</g>')
board.append('<rect x="650" y="875" width="860" height="240" rx="6" fill="#193E32"/>')
text(690,920,'EINFARBIG / NEGATIV',16,'#F5F3EB')
white,_=wordmark('#F5F3EB','#F5F3EB')
board.append(f'<g transform="translate(680 960) scale(1.15)">{white}</g>')
text(80,1138,'Natur verstehen. Bewusster handeln.',22)
text(80,1174,'Vektor-Master · 04.11.2026 · Entwurf, keine Markenfreigabe',15,'#526458')
(ROOT/'brandboard.svg').write_text(svg(''.join(board),1600,1200,'mundoverde – Logo und Farbwelt'),encoding='utf8')

# A complete local website copy preserves the article drafts and legal placeholders.
original=ROOT/'source/original-site'
web=ROOT/'website'
for p in original.iterdir():
    if p.is_file():shutil.copy2(p,web/p.name)
for p in ASSETS.glob('*.svg'):shutil.copy2(p,web/'assets'/p.name)
shutil.copy2(ASSETS/'mundoverde-favicon.svg',web/'favicon.svg')
for p in web.glob('*.html'):
    content=p.read_text()
    content=re.sub(r'<a class="logo".*?</a>','<a class="logo" href="index.html" aria-label="mundoverde – Startseite"><img src="assets/mundoverde-wordmark-primary.svg" alt="mundoverde" width="260" height="47"></a>',content,count=1)
    content=content.replace('>Das Magazin</a>','>Beiträge</a>').replace('>Die Idee</a>','>Über mundoverde</a>')
    content=content.replace('<body>','<body><a class="skip-link" href="#top">Zum Inhalt springen</a>')
    if p.name=='index.html':
        start=content.index('<section class="hero">');end=content.index('<section id="beitraege">')
        content=content[:start]+'''<section class="hero"><div><p class="eyebrow">Das Magazin für Natur und Nachhaltigkeit</p><h1>Die grüne Welt.<br><em>Klarer betrachtet.</em></h1><p>Natur verstehen, Zusammenhänge erkennen und im Alltag bewusster entscheiden. Mit Gedanken zu Ökologie, Klima und nachhaltigem Leben.</p><a class="pill" href="#beitraege">Beiträge entdecken <span aria-hidden="true">↗</span></a></div><aside class="brand-story"><img src="assets/mundoverde-symbol-green.svg" width="120" height="120" alt=""><p><strong>mundo</strong> · Welt<br><strong>verde</strong> · grün</p><p>Was uns verbindet,<br>kann wachsen.</p></aside></section>'''+content[end:]
        content=content.replace('Grüne Gedanken.','Lesestoff für eine grüne Welt.')
        content=content.replace('Beiträge durchsuchen','Titel und Kurztexte durchsuchen')
        content=content.replace('mundoverde bedeutet „grüne Welt“.','Der Name mundoverde verbindet „mundo“ – Welt – und „verde“ – grün.')
        content=content.replace('<div id="themen" class="filters"','<div id="themen" class="filters" hidden')
        content=content.replace('<input type="search" id="search"','<input type="search" id="search" disabled')
        content=content.replace('<div class="grid">','<noscript><p>Die Beiträge sind ohne JavaScript lesbar. Suche und Themenfilter benötigen JavaScript.</p></noscript><div class="grid">')
    p.write_text(content)
css='''/* mundoverde CI 01 – no remote fonts or libraries */
:root{--paper:#F5F3EB;--ink:#20382E;--forest:#193E32;--moss:#47683F;--muted:#526458;--sage:#DCE6D5;--line:#C5CFC1;--earth:#77624F;--space:8px}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:24px}body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.65 system-ui,-apple-system,"Segoe UI",sans-serif}a{color:inherit;text-underline-offset:4px}a:hover{color:var(--moss)}button,input{font:inherit}button{cursor:pointer}a:focus-visible,button:focus-visible,input:focus-visible{outline:3px solid var(--moss);outline-offset:5px}header{max-width:1260px;margin:auto;padding:28px 36px;display:flex;justify-content:space-between;align-items:center;gap:28px;border-bottom:1px solid var(--line)}.logo{display:block;flex-shrink:0}.logo img{display:block;width:260px;height:auto}nav{display:flex;gap:28px;font-size:14px}nav a{text-decoration:none;min-height:44px;display:flex;align-items:center}.wrap{max-width:1190px;margin:auto;padding:0 36px}.eyebrow{font-size:12px;letter-spacing:1.5px;text-transform:uppercase;font-weight:650;color:var(--moss)}.hero{display:grid;grid-template-columns:1fr 220px;gap:72px;padding:88px 0 72px;align-items:center}.hero h1{font:400 clamp(42px,5.3vw,70px)/1.1 Georgia,serif;letter-spacing:-1.5px;margin:20px 0 24px}.hero h1 em{font-style:normal;color:var(--moss)}.hero p:not(.eyebrow){max-width:570px;color:var(--muted)}.pill{display:inline-flex;align-items:center;gap:28px;background:var(--forest);color:var(--paper);border-radius:4px;padding:12px 20px;min-height:48px;text-decoration:none;margin-top:12px}.pill:hover{color:var(--paper);background:#234D3D}.brand-story{border-left:1px solid var(--line);padding-left:30px;font-size:15px}.brand-story img{display:block}.brand-story strong{color:var(--forest)}.section-title{display:flex;align-items:end;justify-content:space-between;gap:24px;border-top:1px solid var(--line);padding-top:28px;margin:0 0 24px}h2{font:400 34px/1.2 Georgia,serif;margin:8px 0 16px}.section-title h2{font-size:30px;max-width:440px}.section-title label{font-size:12px;min-width:260px}input{color:var(--ink);background:transparent;border:1px solid var(--muted);border-radius:4px;padding:10px 12px;min-height:44px;width:100%;max-width:310px}.filters{display:flex;flex-wrap:wrap;gap:8px;margin:24px 0 32px}.filters button{color:var(--ink);background:transparent;border:1px solid var(--muted);border-radius:4px;font-size:14px;min-height:44px;padding:8px 16px}.filters button[aria-pressed=true]{color:var(--paper);background:var(--forest);border-color:var(--forest)}.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:40px 32px}.card{border-top:1px solid var(--line);padding:24px 0 20px}.card>a{display:block;height:100%;text-decoration:none}.card h3{font:400 29px/1.2 Georgia,serif;margin:14px 0}.card p{color:var(--muted);font-size:16px;margin:0 0 20px}.card .thumb{display:none}.more{font-size:14px;text-decoration:underline;text-underline-offset:5px}.card a:hover h3{text-decoration:underline;text-underline-offset:5px}.draft{font-size:13px;color:var(--muted);margin:24px 0}.note{display:grid;grid-template-columns:1fr 1fr;gap:48px;border-top:1px solid var(--line);margin:64px 0 40px;padding-top:36px}.note p{color:var(--muted);font-size:16px}.note h2{font-size:34px}footer{border-top:1px solid var(--line);padding:24px 0 32px;display:flex;justify-content:space-between;gap:24px;color:var(--muted);font-size:13px}footer div{display:flex;flex-wrap:wrap;gap:20px}footer a{min-height:44px;display:inline-flex;align-items:center}.reading{max-width:800px;padding-top:48px;padding-bottom:64px}.reading h1{font:400 clamp(36px,5vw,54px)/1.15 Georgia,serif;letter-spacing:-.8px}.reading h2{font-size:28px;margin-top:36px}.reading .lead{font-size:21px;color:var(--muted)}.reading .thumb{max-width:100%;height:220px;overflow:hidden;background:var(--sage)}.reading .thumb svg{height:100%;width:100%}.source{border-top:1px solid var(--line);margin-top:32px;padding-top:20px;font-size:15px}.empty{padding:24px 0}.skip-link{position:absolute;left:12px;top:12px;transform:translateY(-200%);background:var(--forest);color:var(--paper);padding:10px 18px;z-index:10}.skip-link:focus{transform:translateY(0)}[hidden]{display:none!important}img,svg{max-width:100%}
@media(max-width:900px){header{padding:22px 28px;flex-wrap:wrap;gap:12px}nav{gap:22px}.hero{grid-template-columns:1fr 160px;gap:32px;padding:56px 0}.brand-story{padding-left:20px}.section-title{align-items:start;flex-direction:column}.grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:600px){header{padding:22px 24px}.logo img{width:230px}nav{width:100%;justify-content:space-between;gap:14px;font-size:13px}.wrap{padding:0 24px}.hero{grid-template-columns:1fr;padding:40px 0;gap:26px}.hero h1{font-size:44px;letter-spacing:-1px}.brand-story{display:flex;align-items:center;gap:16px;border-left:0;border-top:1px solid var(--line);padding:16px 0 0}.brand-story img{width:64px;height:64px}.brand-story p{margin:0}.brand-story p:last-child{display:none}.grid{grid-template-columns:1fr;gap:8px}.section-title label{min-width:0;width:100%}.section-title h2{font-size:30px}.card h3{font-size:29px}.note{grid-template-columns:1fr;gap:8px;margin-top:40px}footer{flex-direction:column;gap:8px}.reading .thumb{height:180px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
'''
(web/'style.css').write_text(css)
(ROOT/'tokens.css').write_text(css[:css.index('*{box-sizing')])
app='''"use strict";
(() => {
  const search = document.querySelector("#search");
  const filters = document.querySelector("#themen");
  const status = document.querySelector("#result");
  const empty = document.querySelector("#empty");
  const cards = Array.from(document.querySelectorAll(".card"));
  if (!search || !filters || !status || !empty || !cards.length) return;
  const buttons = Array.from(filters.querySelectorAll("[data-filter]"));
  let category = "Alle";
  const normalise = text => text.normalize("NFC").toLocaleLowerCase("de");
  const filter = () => {
    const query = normalise(search.value.trim());
    let count = 0;
    for (const card of cards) {
      const matches = (category === "Alle" || card.dataset.category === category)
        && normalise(card.dataset.search || "").includes(query);
      card.hidden = !matches;
      if (matches) count += 1;
    }
    empty.hidden = count > 0;
    status.textContent = `${count} ${count === 1 ? "Beitrag" : "Beiträge"} entdecken`;
  };
  for (const button of buttons) button.addEventListener("click", () => {
    category = button.dataset.filter;
    for (const item of buttons) item.setAttribute("aria-pressed", String(item === button));
    filter();
  });
  search.addEventListener("input", filter);
  search.disabled = false;
  filters.hidden = false;
  filter();
})();
'''
(web/'app.js').write_text(app)
(ROOT/'preview/.openai/hosting.json').write_text('{"static":{"directory":"dist"}}')
shutil.copytree(web,ROOT/'preview/dist/website',dirs_exist_ok=True)
shutil.copytree(ASSETS,ROOT/'preview/dist/assets',dirs_exist_ok=True)
print(json.dumps({'wordmark_viewbox':[width,112],'contrast':results,'output':str(ROOT)},ensure_ascii=False))
