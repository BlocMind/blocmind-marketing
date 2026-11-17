import asyncio, pathlib, random
from playwright.async_api import async_playwright

R = pathlib.Path('/home/claude/blocmind-marketing')
OUT = R / 'posts/2026-11-17-markeo'; OUT.mkdir(parents=True, exist_ok=True)
F = R / 'brand/fonts'; ICON = (R / 'brand/icons/markeo-icon.png').as_uri()
V = '#5B47E0'; DEEP = '#1E1840'; LILAC = '#B3A6FF'; LIME = '#C6F36B'; PINK = '#FF8FB1'; SUN = '#FFD54A'

random.seed(7)
def confetti(n=110, w=1080, h=1920, top=0):
    cols = [LIME, PINK, SUN, LILAC, '#7FE0FF', '#FFFFFF']
    out = []
    for _ in range(n):
        x, y = random.randint(-20, w), random.randint(top, h)
        if 140 < x < w - 160 and 220 < y < h - 260: continue
        c = random.choice(cols); r = random.randint(-60, 60); s = random.randint(14, 34)
        shape = random.choice(['r', 'c', 'b'])
        if shape == 'r': out.append(f'<i style="left:{x}px;top:{y}px;width:{s}px;height:{s*2.2:.0f}px;background:{c};transform:rotate({r}deg);border-radius:4px"></i>')
        elif shape == 'c': out.append(f'<i style="left:{x}px;top:{y}px;width:{s}px;height:{s}px;background:{c};border-radius:50%"></i>')
        else: out.append(f'<i style="left:{x}px;top:{y}px;width:{s*1.1:.0f}px;height:{s*1.5:.0f}px;background:{c};transform:rotate({r}deg);clip-path:polygon(0 0,100% 0,100% 100%,50% 75%,0 100%)"></i>')
    return '<div class="conf">' + ''.join(out) + '</div>'

CSS = f"""
@font-face{{font-family:J;src:url({(F/'plus-jakarta-sans-latin-500-normal.woff').as_uri()});font-weight:500}}
@font-face{{font-family:J;src:url({(F/'plus-jakarta-sans-latin-700-normal.woff').as_uri()});font-weight:700}}
@font-face{{font-family:J;src:url({(F/'plus-jakarta-sans-latin-800-normal.woff').as_uri()});font-weight:800}}
*{{box-sizing:border-box;margin:0}}body{{font-family:J;-webkit-font-smoothing:antialiased}}
.s{{position:relative;overflow:hidden;width:1080px;height:1920px;color:#fff;background:radial-gradient(120% 80% at 50% 30%,#3A2C8F 0%,{DEEP} 70%)}}
.conf{{position:absolute;inset:0;z-index:1}}.conf i{{position:absolute;display:block}}
.ray{{position:absolute;left:50%;top:44%;width:2800px;height:2800px;margin:-1400px 0 0 -1400px;background:repeating-conic-gradient(rgba(179,166,255,.10) 0 9deg,transparent 9deg 18deg)}}
.top{{position:absolute;left:72px;right:72px;top:96px;display:flex;align-items:center;gap:20px;z-index:6}}
.top img{{width:88px;height:88px;border-radius:24px;box-shadow:0 0 0 4px rgba(255,255,255,.15)}}
.top b{{font-size:46px;font-weight:800;letter-spacing:-1.5px}}
.n{{margin-left:auto;padding:10px 20px;border-radius:999px;background:rgba(255,255,255,.14);font-weight:800;font-size:28px}}
.c{{position:absolute;left:72px;right:72px;z-index:5}}
.tag{{display:inline-block;padding:14px 24px;border-radius:16px;background:{LIME};color:{DEEP};font-size:30px;font-weight:800;letter-spacing:2px;text-transform:uppercase}}
h1{{font-weight:800;letter-spacing:-.045em;line-height:.95}}
.big{{font-size:380px;font-weight:800;letter-spacing:-.06em;line-height:.85;background:linear-gradient(180deg,#fff 30%,{LILAC});-webkit-background-clip:text;color:transparent;filter:drop-shadow(0 18px 0 {V})}}
p{{font-size:46px;font-weight:500;line-height:1.35;color:#D9D3FF}}
.store{{display:flex;align-items:center;gap:22px;padding:26px 34px;border-radius:30px;background:#fff;color:{DEEP};box-shadow:12px 12px 0 {V}}}
.store .ic{{width:76px;height:76px;border-radius:20px;display:grid;place-items:center;font-size:44px;background:{DEEP};color:#fff}}
.store small{{display:block;font-size:26px;font-weight:700;color:#6B6496}}
.store b{{font-size:48px;font-weight:800;letter-spacing:-1.5px}}
.feat{{display:flex;align-items:center;gap:24px;padding:26px 30px;border-radius:30px;background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.14);font-size:40px;font-weight:700}}
.feat span{{width:72px;height:72px;flex:none;border-radius:20px;display:grid;place-items:center;font-size:38px;background:{V}}}
.foot{{position:absolute;left:72px;right:72px;bottom:120px;display:flex;justify-content:space-between;align-items:center;font-size:32px;font-weight:800;z-index:3;color:#D9D3FF}}
.mark{{display:inline-grid;grid-template-columns:repeat(2,20px);gap:5px;vertical-align:middle;margin-right:12px}}
.mark i{{display:block;width:20px;height:20px;border-radius:5px;background:#fff}}.mark i.m{{border-radius:50%;background:{LILAC}}}
"""
def top(n): return f'<div class="top"><img src="{ICON}"><b>Markeo</b><span class="n">{n}</span></div>'
FOOT = '<div class="foot"><span>Save it now. Read it later.</span><span><span class="mark"><i></i><i class="m"></i><i></i><i></i></span>blocmind</span></div>'
APPLE = '<span class="ic" style="font-size:40px">📱</span>'; PLAY = '<span class="ic" style="background:#0F9D58">▶</span>'
STORES = f'''<div style="display:flex;flex-direction:column;gap:26px">
<div class="store">{APPLE}<div><small>NEW · Download on the</small><b>App Store</b></div></div>
<div class="store">{PLAY}<div><small>Get it on</small><b>Google Play</b></div></div></div>'''

TT = [
f'''<div class="s"><div class="ray"></div>{confetti(90)}{top('1/4')}
<div class="c" style="top:420px;text-align:center"><span class="tag">Milestone 🎉</span>
<div class="big" style="margin-top:50px">1K+</div>
<h1 style="font-size:120px;margin-top:40px">downloads<span style="color:{LIME}">.</span></h1>
<p style="margin-top:40px">Thank you for saving with Markeo.</p></div>{FOOT}</div>''',
f'''<div class="s">{confetti(30)}{top('2/4')}
<div class="c" style="top:280px"><h1 style="font-size:118px">Why 1,000+ people keep their links here<span style="color:{LIME}">.</span></h1>
<div style="display:flex;flex-direction:column;gap:22px;margin-top:70px">
<div class="feat"><span>↗</span>Save from any app in one tap</div>
<div class="feat"><span>⏰</span>Read-later reminders that actually remind</div>
<div class="feat"><span>🗂</span>Folders and smart collections</div>
<div class="feat"><span>🔒</span>No account. Links stay on your phone</div>
</div></div>{FOOT}</div>''',
f'''<div class="s"><div class="ray"></div>{confetti(60)}{top('3/4')}
<div class="c" style="top:320px"><span class="tag">New</span>
<h1 style="font-size:150px;margin-top:40px">Now on iPhone too<span style="color:{LIME}">.</span></h1>
<p style="margin-top:40px;max-width:880px">Markeo is live on the App Store. Same calm app, now on both platforms.</p></div>
<div class="c" style="top:1180px">{STORES}</div>{FOOT}</div>''',
f'''<div class="s"><div class="ray"></div>{confetti(70)}{top('4/4')}
<div class="c" style="top:360px;text-align:center"><img src="{ICON}" style="width:240px;height:240px;border-radius:60px;box-shadow:0 0 0 10px rgba(255,255,255,.12),20px 20px 0 {V}">
<h1 style="font-size:128px;margin-top:70px">Get Markeo<span style="color:{LIME}">.</span></h1>
<p style="margin-top:30px">Search “Markeo” on the App Store or Google Play.</p></div>
<div class="c" style="top:1200px">{STORES}</div>{FOOT}</div>''',
]

FB = f'''<div class="s" style="height:1350px"><div class="ray" style="top:40%"></div>{confetti(70,1080,1350)}
<div class="top" style="top:70px"><img src="{ICON}"><b>Markeo</b><span class="n" style="background:{LIME};color:{DEEP}">Milestone 🎉</span></div>
<div class="c" style="top:200px"><div class="big" style="font-size:300px">1K+</div><h1 style="font-size:100px;margin-top:10px">downloads<span style="color:{LIME}">.</span></h1></div>
<div class="c" style="top:640px"><h1 style="font-size:76px">And now on iPhone too<span style="color:{LIME}">.</span></h1>
<p style="font-size:36px;margin-top:18px;max-width:920px">Save links from any app, get reminded to read them, keep them organised. No account needed.</p></div>
<div class="c" style="top:950px;display:grid;grid-template-columns:1fr 1fr;gap:26px">
<div class="store">{APPLE}<div><small>NEW · Download on the</small><b>App Store</b></div></div>
<div class="store">{PLAY}<div><small>Get it on</small><b>Google Play</b></div></div></div>
<div class="foot" style="bottom:64px"><span>Thank you for saving with Markeo.</span><span><span class="mark"><i></i><i class="m"></i><i></i><i></i></span>blocmind</span></div></div>'''

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, body, h in [('facebook.png', FB, 1350)] + [(f'tiktok-{i}.jpg', t, 1920) for i, t in enumerate(TT, 1)]:
            f = OUT / f'_{name}.html'
            f.write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>')
            pg = await b.new_page(viewport={'width': 1080, 'height': h})
            await pg.goto(f.as_uri()); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(250)
            await pg.screenshot(path=str(OUT / name), **({'type': 'jpeg', 'quality': 92} if name.endswith('.jpg') else {}))
            f.unlink()
        await b.close()
asyncio.run(main())
