import asyncio, pathlib, random
from playwright.async_api import async_playwright

R = pathlib.Path('/home/claude/blocmind-marketing')
OUT = R / 'posts/2026-11-17-tiktok-100-likes'; OUT.mkdir(parents=True, exist_ok=True)
F = R / 'brand/fonts'; IC = lambda a: (R / f'brand/icons/{a}-icon.png').as_uri()
INK = '#121613'; PAPER = '#F6F7F5'; GREEN = '#1F9D55'; MINT = '#6FE3A0'; PINK = '#FF4F7B'

random.seed(100)
def hearts(n, w, h, keep_clear):
    x0, y0, x1, y1 = keep_clear; out = []
    while len(out) < n:
        x, y = random.randint(-30, w), random.randint(0, h)
        if x0 < x < x1 and y0 < y < y1: continue
        if y < 220 or y > h - 240: continue
        s = random.randint(30, 90); r = random.randint(-30, 30)
        c = random.choice([PINK, MINT, '#FFFFFF', '#FF9FB5'])
        o = random.choice([.35, .55, .8, 1])
        out.append(f'<svg style="position:absolute;left:{x}px;top:{y}px;transform:rotate({r}deg);opacity:{o}" width="{s}" viewBox="0 0 24 22"><path d="M12 21s-9-5.6-9-12.2C3 5.5 5.5 3 8.6 3c1.6 0 2.7.8 3.4 1.9C12.7 3.8 13.8 3 15.4 3 18.5 3 21 5.5 21 8.8 21 15.4 12 21 12 21z" fill="{c}"/></svg>')
    return ''.join(out)

HEART = f'<svg width="{{w}}" viewBox="0 0 24 22"><path d="M12 21s-9-5.6-9-12.2C3 5.5 5.5 3 8.6 3c1.6 0 2.7.8 3.4 1.9C12.7 3.8 13.8 3 15.4 3 18.5 3 21 5.5 21 8.8 21 15.4 12 21 12 21z" fill="{PINK}"/></svg>'

CSS = f"""
@font-face{{font-family:J;src:url({(F/'plus-jakarta-sans-latin-500-normal.woff').as_uri()});font-weight:500}}
@font-face{{font-family:J;src:url({(F/'plus-jakarta-sans-latin-700-normal.woff').as_uri()});font-weight:700}}
@font-face{{font-family:J;src:url({(F/'plus-jakarta-sans-latin-800-normal.woff').as_uri()});font-weight:800}}
*{{box-sizing:border-box;margin:0}}body{{font-family:J;-webkit-font-smoothing:antialiased}}
.s{{position:relative;overflow:hidden;width:1080px;color:#fff;background:radial-gradient(110% 70% at 50% 40%,#1E2A22 0%,{INK} 70%)}}
.paper{{background:{PAPER};color:{INK}}}
.c{{position:absolute;left:72px;right:72px;z-index:5}}
.brand{{position:absolute;left:72px;right:72px;top:96px;display:flex;align-items:center;gap:16px;font-size:46px;font-weight:800;letter-spacing:-1.8px;z-index:6}}
.mark{{display:grid;grid-template-columns:repeat(2,24px);gap:6px}}.mark i{{display:block;width:24px;height:24px;border-radius:7px;background:currentColor}}.mark i.m{{border-radius:50%;background:{MINT}}}
.paper .mark i.m{{background:{GREEN}}}
.n{{margin-left:auto;padding:10px 20px;border-radius:999px;background:rgba(255,255,255,.12);font-weight:800;font-size:28px;letter-spacing:0}}
.paper .n{{background:rgba(0,0,0,.07)}}
.num{{font-size:440px;font-weight:800;letter-spacing:-.07em;line-height:.8;color:#fff;text-shadow:0 20px 0 {GREEN}}}
h1{{font-weight:800;letter-spacing:-.045em;line-height:.95}}
p{{font-size:46px;font-weight:500;line-height:1.35;color:#B8C2BA}}
.paper p{{color:#3A403B}}
.tag{{display:inline-flex;align-items:center;gap:12px;padding:14px 24px;border-radius:16px;background:{PINK};color:#fff;font-size:30px;font-weight:800;letter-spacing:2px;text-transform:uppercase}}
.app{{display:flex;align-items:center;gap:22px;padding:20px 24px;border-radius:28px;background:#fff;box-shadow:inset 0 0 0 2px #E3E7E2}}
.app img{{width:84px;height:84px;border-radius:22px}}.app b{{font-size:38px;font-weight:800;letter-spacing:-1px}}.app span{{display:block;font-size:26px;font-weight:500;color:#5D665F}}
.foot{{position:absolute;left:72px;right:72px;bottom:120px;display:flex;justify-content:space-between;font-size:32px;font-weight:800;z-index:6;color:#B8C2BA}}
.paper .foot{{color:#3A403B}}
"""
def brand(n=''): return f'<div class="brand"><span class="mark"><i></i><i class="m"></i><i></i><i></i></span>blocmind{f"<span class=n>{n}</span>" if n else ""}</div>'

APPS = [('spencio','Spencio','Know what’s safe to spend.'),('reap','Reap','Eat what you buy.'),('markeo','Markeo','Save it now. Read it later.'),('axilo','Axilo','Every sensor, made readable.'),('fairloop','Fairloop','Money between friends, made light.')]
ROWS = ''.join(f'<div class="app"><img src="{IC(k)}"><div><b>{n}</b><span>{t}</span></div></div>' for k, n, t in APPS)

TT = [
f'''<div class="s" style="height:1920px">{hearts(46,1080,1920,(60,300,1020,1500))}{brand('1/2')}
<div class="c" style="top:420px;text-align:center"><span class="tag">{HEART.format(w=34).replace(PINK,'#fff')} Thank you</span>
<div style="display:flex;align-items:center;justify-content:center;gap:10px;margin-top:70px"><span class="num">100</span>{HEART.format(w=220)}</div>
<h1 style="font-size:130px;margin-top:50px">likes<span style="color:{MINT}">.</span></h1>
<p style="margin-top:40px">A small studio, five small apps, and 100 of you tapping that heart. It means a lot.</p></div>
<div class="foot"><span>Swipe →</span><span>@blocmind</span></div></div>''',
f'''<div class="s paper" style="height:1920px">{brand('2/2')}
<div class="c" style="top:260px"><h1 style="font-size:116px">Here’s what you’re cheering on<span style="color:{GREEN}">.</span></h1>
<div style="display:flex;flex-direction:column;gap:16px;margin-top:56px">{ROWS}</div>
<p style="margin-top:50px">Follow along. We share every step, one bloc at a time.</p></div>
<div class="foot"><span>Small tools for everyday life.</span><span>blocmind.com</span></div></div>''',
]

FB = f'''<div class="s" style="height:1350px">{hearts(36,1080,1350,(40,200,1040,1150))}
<div class="brand" style="top:72px"><span class="mark"><i></i><i class="m"></i><i></i><i></i></span>blocmind<span class="n" style="background:{PINK};color:#fff">on TikTok</span></div>
<div class="c" style="top:250px;text-align:center"><div style="display:flex;align-items:center;justify-content:center;gap:10px"><span class="num" style="font-size:380px">100</span>{HEART.format(w=190)}</div>
<h1 style="font-size:110px;margin-top:40px">likes on TikTok<span style="color:{MINT}">.</span></h1>
<p style="margin-top:34px;font-size:42px">Thank you for every heart. Come say hi at @blocmind for stories, updates and what we’re building next.</p></div>
<div class="foot" style="bottom:70px"><span>Small tools for everyday life.</span><span>blocmind.com</span></div></div>'''

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, body, h in [('facebook.png', FB, 1350), ('tiktok-1.jpg', TT[0], 1920), ('tiktok-2.jpg', TT[1], 1920)]:
            f = OUT / f'_{name}.html'
            f.write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>')
            pg = await b.new_page(viewport={'width': 1080, 'height': h})
            await pg.goto(f.as_uri()); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(250)
            await pg.screenshot(path=str(OUT / name), **({'type': 'jpeg', 'quality': 92} if name.endswith('.jpg') else {}))
            f.unlink()
        await b.close()
asyncio.run(main())
