"""Create warmer serif wordmarks from an installed DejaVu Serif font.
Requires Python and fontTools. SVG exports do not require a font at runtime.
"""
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import xml.etree.ElementTree as ET
import json

ROOT=Path(__file__).resolve().parent
(ROOT/'assets').mkdir(exist_ok=True)
FONT=Path('/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf')
font=TTFont(FONT);glyphs=font.getGlyphSet();cmap=font.getBestCmap();scale=100/font['head'].unitsPerEm
def text_paths(word,x,fill):
    paths=[]
    for char in word:
        name=cmap[ord(char)]
        pen=SVGPathPen(glyphs)
        glyphs[name].draw(TransformPen(pen,(scale,0,0,-scale,x,88)))
        paths.append(f'<path fill="{fill}" d="{pen.getCommands()}"/>')
        x+=font['hmtx'][name][0]*scale-2.0
    return ''.join(paths),x
def logo(a,b):
    left,x=text_paths('mundo',14,a)
    v=f'<g transform="translate({x+1} 0)" fill="{b}"><path d="M0 32 H10 L27 76 L44 32 H54 L33 88 H21 Z"/><path d="M44 33 C43 19 51 13 65 12 C64 26 57 33 44 33 Z"/></g>'
    right,end=text_paths('erde',x+65,b)
    return left+v+right,round(end+14,2)
def svg(body,w,h,title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{title}</title>{body}</svg>'
for name,a,b in [('primary','#193E32','#47683F'),('mono','#193E32','#193E32'),('white','#FFFFFF','#FFFFFF')]:
    body,width=logo(a,b)
    (ROOT/f'assets/mundoverde-wordmark-{name}.svg').write_text(svg(body,width,112,'mundoverde'),encoding='utf-8')

# Text-independent source illustration of the revised logo.
body,width=logo('#193E32','#47683F')
board=['<rect width="1600" height="1160" fill="#F5F3EB"/>']
def label(x,y,value,size=22,color='#193E32'):
    board.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans,sans-serif" font-size="{size}" fill="{color}">{value}</text>')
label(80,65,'MUNDOVERDE / SCHRIFTENTWURF 02',18)
label(80,130,'Mehr Wärme. Mehr redaktioneller Charakter.',34)
label(80,195,'BISHER',16,'#526458')
old=ROOT/'reference/mundoverde-wordmark-v1.svg'
if old.exists():
    tree=ET.parse(old).getroot();oldw=float(tree.attrib['viewBox'].split()[2]);oldbody=''.join(ET.tostring(e,encoding='unicode') for e in tree if e.tag.split('}')[-1]!='title')
    board.append(f'<g transform="translate(65 210) scale({1420/oldw})">{oldbody}</g>')
board.append('<path d="M80 480 H1520" stroke="#C5CFC1"/>')
label(80,530,'NEUER VORSCHLAG',16,'#526458')
board.append(f'<g transform="translate(65 555) scale({1420/width})">{body}</g>')
label(80,855,'Ruhige Serifen · offenere Buchstabenwirkung · Keimling und Farben bleiben',22,'#526458')
board.append('<rect x="80" y="905" width="1440" height="150" rx="5" fill="#193E32"/>')
white,_=logo('#FFFFFF','#FFFFFF')
board.append(f'<g transform="translate(110 915) scale({820/width})">{white}</g>')
label(80,1120,'Vektorfassung · einfarbig nutzbar · Website noch unverändert',16,'#526458')
(ROOT/'vergleich.svg').write_text(svg(''.join(board),1600,1160,'mundoverde – bisherige und neue Logoschrift'),encoding='utf-8')
(ROOT/'specification.json').write_text(json.dumps({'wordmark':'mundoverde','font_basis':'DejaVu Serif Book','outline_export':True,'symbol':'unchanged from V1','colors':['#193E32','#47683F'],'viewBox':[width,112]},indent=2))
print('Logo variants and comparison generated:',width)
