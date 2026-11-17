import asyncio, pathlib
from playwright.async_api import async_playwright

OUT = pathlib.Path('/home/claude/story/out'); OUT.mkdir(parents=True, exist_ok=True)
FONTS = pathlib.Path('/home/claude/mkt/brand/fonts')
ICON = pathlib.Path('/home/claude/mkt/brand/icons/spencio-icon.png')

INK = '#121613'; GREEN = '#1F9D55'; MINT = '#6FE3A0'; PAPER = '#F6F7F5'
SKIN = '#C98B62'; SKIN_D = '#B37750'; HAIR = '#22160F'; TOP = '#FF7A59'; TOP_D = '#E8603F'

# ---------- characters ----------
def maya(mood='neutral', phone=False, w=520):
    """Original character: Maya, early 20s. mood: neutral|happy|worried|shock|joy"""
    eyes = {
        'neutral': '<circle cx="160" cy="215" r="11" fill="#1A1A1A"/><circle cx="240" cy="215" r="11" fill="#1A1A1A"/><circle cx="164" cy="211" r="3.5" fill="#fff"/><circle cx="244" cy="211" r="3.5" fill="#fff"/>',
        'happy': '<path d="M146 218 Q160 202 174 218" stroke="#1A1A1A" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M226 218 Q240 202 254 218" stroke="#1A1A1A" stroke-width="7" fill="none" stroke-linecap="round"/>',
        'joy': '<path d="M146 218 Q160 200 174 218" stroke="#1A1A1A" stroke-width="8" fill="none" stroke-linecap="round"/><path d="M226 218 Q240 200 254 218" stroke="#1A1A1A" stroke-width="8" fill="none" stroke-linecap="round"/>',
        'worried': '<circle cx="160" cy="218" r="10" fill="#1A1A1A"/><circle cx="240" cy="218" r="10" fill="#1A1A1A"/><circle cx="163" cy="214" r="3" fill="#fff"/><circle cx="243" cy="214" r="3" fill="#fff"/>',
        'shock': '<circle cx="160" cy="215" r="16" fill="#fff" stroke="#1A1A1A" stroke-width="5"/><circle cx="240" cy="215" r="16" fill="#fff" stroke="#1A1A1A" stroke-width="5"/><circle cx="160" cy="217" r="6" fill="#1A1A1A"/><circle cx="240" cy="217" r="6" fill="#1A1A1A"/>',
    }[mood]
    brows = {
        'worried': '<path d="M140 194 Q160 190 178 180" stroke="#22160F" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M260 194 Q240 190 222 180" stroke="#22160F" stroke-width="7" fill="none" stroke-linecap="round"/>',
        'shock': '<path d="M142 180 Q160 168 178 178" stroke="#22160F" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M222 178 Q240 168 258 180" stroke="#22160F" stroke-width="7" fill="none" stroke-linecap="round"/>',
    }.get(mood, '<path d="M144 186 Q160 178 176 186" stroke="#22160F" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M224 186 Q240 178 256 186" stroke="#22160F" stroke-width="6" fill="none" stroke-linecap="round"/>')
    mouth = {
        'neutral': '<path d="M182 262 Q200 274 218 262" stroke="#7A2E1E" stroke-width="6" fill="none" stroke-linecap="round"/>',
        'happy': '<path d="M176 256 Q200 286 224 256 Z" fill="#7A2E1E"/><path d="M186 262 Q200 270 214 262" fill="#fff"/>',
        'joy': '<path d="M170 252 Q200 300 230 252 Z" fill="#7A2E1E"/><path d="M182 258 Q200 268 218 258" fill="#fff"/><ellipse cx="200" cy="280" rx="14" ry="7" fill="#E96A6A"/>',
        'worried': '<path d="M180 272 Q190 262 200 272 Q210 282 220 272" stroke="#7A2E1E" stroke-width="6" fill="none" stroke-linecap="round"/>',
        'shock': '<ellipse cx="200" cy="272" rx="16" ry="20" fill="#7A2E1E"/>',
    }[mood]
    sweat = '<path d="M290 160 Q302 182 290 192 Q278 182 290 160Z" fill="#7FD0FF" stroke="#2D8BC9" stroke-width="3"/>' if mood in ('worried', 'shock') else ''
    hand = ''
    if phone:
        hand = ('<g transform="rotate(-12 300 400)"><rect x="262" y="318" width="86" height="150" rx="16" fill="#1B1F1C"/>'
                '<rect x="270" y="330" width="70" height="120" rx="10" fill="#9FF0C2"/>'
                f'<circle cx="305" cy="430" r="24" fill="{SKIN}"/><circle cx="282" cy="440" r="20" fill="{SKIN}"/></g>')
    return f'''<svg width="{w}" viewBox="0 0 400 520" xmlns="http://www.w3.org/2000/svg">
  <path d="M60 520 Q60 380 200 370 Q340 380 340 520Z" fill="{TOP}"/>
  <path d="M150 380 Q200 420 250 380" stroke="{TOP_D}" stroke-width="8" fill="none"/>
  <rect x="176" y="300" width="48" height="70" rx="20" fill="{SKIN_D}"/>
  <circle cx="200" cy="66" r="44" fill="{HAIR}"/>
  <path d="M80 220 Q70 90 200 88 Q330 90 320 220 Q330 330 300 360 L100 360 Q70 330 80 220Z" fill="{HAIR}"/>
  <ellipse cx="200" cy="220" rx="112" ry="118" fill="{SKIN}"/>
  <ellipse cx="88" cy="226" rx="16" ry="24" fill="{SKIN_D}"/><ellipse cx="312" cy="226" rx="16" ry="24" fill="{SKIN_D}"/>
  <path d="M88 200 Q96 104 200 100 Q304 104 312 200 Q280 140 236 136 Q210 170 150 150 Q110 160 88 200Z" fill="{HAIR}"/>
  <circle cx="132" cy="250" r="16" fill="#F28B82" opacity=".55"/><circle cx="268" cy="250" r="16" fill="#F28B82" opacity=".55"/>
  {brows}{eyes}{mouth}{sweat}
  <path d="M196 226 Q192 244 204 246" stroke="{SKIN_D}" stroke-width="5" fill="none" stroke-linecap="round"/>
  {hand}
</svg>'''


def penny(mood='happy', w=360, wave=False):
    """Spencio's mascot: Penny, a green piggy bank."""
    eye = ('<path d="M108 128 Q122 112 136 128" stroke="#0E2A1B" stroke-width="8" fill="none" stroke-linecap="round"/>'
           '<path d="M168 128 Q182 112 196 128" stroke="#0E2A1B" stroke-width="8" fill="none" stroke-linecap="round"/>') if mood == 'happy' else (
           '<circle cx="122" cy="124" r="15" fill="#fff"/><circle cx="182" cy="124" r="15" fill="#fff"/>'
           '<circle cx="125" cy="126" r="8" fill="#0E2A1B"/><circle cx="185" cy="126" r="8" fill="#0E2A1B"/>')
    arm = ('<path d="M250 170 Q290 130 300 90" stroke="#178246" stroke-width="22" fill="none" stroke-linecap="round"/>'
           '<circle cx="300" cy="86" r="16" fill="#178246"/>') if wave else '<ellipse cx="262" cy="190" rx="20" ry="30" fill="#178246"/>'
    return f'''<svg width="{w}" viewBox="0 0 320 300" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="160" cy="288" rx="110" ry="10" fill="#000" opacity=".12"/>
  <rect x="88" y="236" width="34" height="50" rx="14" fill="#178246"/><rect x="190" y="236" width="34" height="50" rx="14" fill="#178246"/>
  <path d="M74 64 L96 20 L130 56Z" fill="#178246"/><path d="M190 56 L224 20 L246 64Z" fill="#178246"/>
  <ellipse cx="160" cy="160" rx="120" ry="104" fill="{GREEN}"/>
  <ellipse cx="128" cy="110" rx="52" ry="30" fill="#fff" opacity=".14"/>
  <rect x="128" y="58" width="64" height="12" rx="6" fill="#0E5A31"/>
  {arm}
  <ellipse cx="58" cy="184" rx="20" ry="28" fill="#178246"/>
  {eye}
  <ellipse cx="152" cy="176" rx="40" ry="28" fill="{MINT}"/>
  <ellipse cx="140" cy="176" rx="7" ry="10" fill="#0E5A31"/><ellipse cx="164" cy="176" rx="7" ry="10" fill="#0E5A31"/>
  <path d="M130 214 Q152 232 174 214" stroke="#0E2A1B" stroke-width="7" fill="none" stroke-linecap="round"/>
  <circle cx="92" cy="176" r="13" fill="#FF9FB0" opacity=".7"/><circle cx="212" cy="176" r="13" fill="#FF9FB0" opacity=".7"/>
</svg>'''


def spark(x, y, s=1, c='#FFFFFF'):
    return f'<svg style="position:absolute;left:{x}px;top:{y}px" width="{60*s}" viewBox="0 0 60 60"><path d="M30 0 L36 24 L60 30 L36 36 L30 60 L24 36 L0 30 L24 24Z" fill="{c}"/></svg>'


CSS = f"""
@font-face{{font-family:J;src:url({(FONTS/'plus-jakarta-sans-latin-500-normal.woff').as_uri()});font-weight:500}}
@font-face{{font-family:J;src:url({(FONTS/'plus-jakarta-sans-latin-700-normal.woff').as_uri()});font-weight:700}}
@font-face{{font-family:J;src:url({(FONTS/'plus-jakarta-sans-latin-800-normal.woff').as_uri()});font-weight:800}}
*{{box-sizing:border-box;margin:0}}
body{{font-family:J;-webkit-font-smoothing:antialiased;color:{INK}}}
.s{{position:relative;overflow:hidden;width:1080px;height:1920px}}
.abs{{position:absolute}}
.top{{position:absolute;left:72px;right:72px;top:96px;display:flex;align-items:center;gap:20px}}
.top img{{width:84px;height:84px;border-radius:22px}}
.top b{{font-size:44px;font-weight:800;letter-spacing:-1.5px}}
.n{{margin-left:auto;padding:10px 20px;border-radius:999px;background:rgba(0,0,0,.08);font-weight:800;font-size:28px}}
.cap{{position:absolute;left:72px;right:72px;font-weight:800;letter-spacing:-.04em;line-height:1}}
.cap i{{font-style:normal;color:{GREEN}}}
.tag{{display:inline-block;padding:12px 22px;border-radius:14px;background:{INK};color:#fff;font-size:28px;font-weight:800;letter-spacing:2px;text-transform:uppercase;margin-bottom:28px}}
.bub{{position:absolute;background:#fff;color:#121613;border:6px solid {INK};border-radius:44px;padding:30px 38px;font-size:46px;font-weight:800;line-height:1.15;box-shadow:12px 12px 0 {INK}}}
.bub small{{display:block;font-size:26px;font-weight:700;color:#5D665F;margin-bottom:8px;letter-spacing:1px;text-transform:uppercase}}
.cloud{{position:absolute;background:#fff;color:#121613;border:5px solid {INK};border-radius:999px;padding:18px 30px;font-size:34px;font-weight:800;box-shadow:8px 8px 0 {INK};white-space:nowrap}}
.foot{{position:absolute;left:72px;right:72px;bottom:120px;display:flex;align-items:center;justify-content:space-between;font-weight:800;font-size:32px}}
.mark{{display:inline-grid;grid-template-columns:repeat(2,20px);gap:5px;vertical-align:middle;margin-right:12px}}
.mark i{{display:block;width:20px;height:20px;border-radius:5px;background:currentColor}}.mark i.m{{border-radius:50%;background:{GREEN}}}
.ray{{position:absolute;left:50%;top:50%;width:2600px;height:2600px;margin:-1300px 0 0 -1300px;background:repeating-conic-gradient(rgba(255,255,255,.10) 0 10deg,transparent 10deg 20deg)}}
.dots{{position:absolute;inset:0;background-image:radial-gradient(rgba(0,0,0,.08) 3px,transparent 3px);background-size:40px 40px}}
.card{{position:absolute;background:#fff;border-radius:48px;border:6px solid {INK};box-shadow:16px 16px 0 {INK};padding:44px}}
.line{{display:flex;justify-content:space-between;font-size:36px;font-weight:700;padding:14px 0;border-bottom:3px dashed #D5DBD4}}
.line span:last-child{{font-weight:800}}
"""

def top(n, dark=False):
    c = '#fff' if dark else INK
    return f'<div class="top" style="color:{c}"><img src="{ICON.as_uri()}"><b>Spencio</b><span class="n" style="background:{"rgba(255,255,255,.18)" if dark else "rgba(0,0,0,.08)"}">{n}</span></div>'

def foot(dark=False, left='Free on App Store &amp; Google Play'):
    c = '#fff' if dark else INK
    return f'<div class="foot" style="color:{c}"><span>{left}</span><span><span class="mark"><i></i><i class="m"></i><i></i><i></i></span>blocmind</span></div>'

TT = []
# 1 — the invite
TT.append(f'''<div class="s" style="background:#FFD54A"><div class="ray"></div>{top('1/5')}
<div class="cap" style="top:250px;font-size:120px">It's the 17th<i>.</i><br>Payday is the 25th<i>.</i></div>
<div class="bub" style="left:470px;top:640px;width:540px;transform:rotate(3deg)"><small>Group chat · 6:42 PM</small>Dinner tonight? 🍜 Everyone's in!</div>
<div class="abs" style="left:-10px;bottom:150px">{maya('shock', phone=True, w=760)}</div>
{spark(860,1060,1.4)}{spark(940,1300,.8)}
<div class="abs" style="right:72px;bottom:300px;font-size:70px;font-weight:800;transform:rotate(-8deg)">bzzt<span style="color:#fff">!</span></div>
</div>''')
# 2 — the spiral
TT.append(f'''<div class="s" style="background:#E7E1FF"><div class="dots"></div>{top('2/5')}
<div class="cap" style="top:250px;font-size:108px">Maya checks her bank app<i>.</i></div>
<div class="bub" style="left:72px;top:560px;width:600px;transform:rotate(-2deg)"><small>Bank balance</small><span style="font-size:84px">Rs 18,400</span></div>
<div class="cloud" style="left:640px;top:820px;transform:rotate(4deg)">But rent? 🏠</div>
<div class="cloud" style="left:72px;top:900px;transform:rotate(-5deg)">Electricity bill? 💡</div>
<div class="cloud" style="left:600px;top:1000px;transform:rotate(-3deg)">My trip fund? ✈️</div>
<div class="abs" style="left:190px;bottom:60px">{maya('worried', w=700)}</div>
</div>''')
# 3 — Penny appears
TT.append(f'''<div class="s" style="background:{GREEN};color:#fff"><div class="ray"></div>{top('3/5', dark=True)}
<div class="cap" style="top:250px;font-size:116px;color:#fff">Then Penny pops up<span style="color:#FFD54A">.</span></div>
<div class="bub" style="left:420px;top:600px;width:590px;transform:rotate(2deg)">"Let me do the maths first. Bills and goals come off the top."</div>
<div class="abs" style="left:90px;top:900px;width:760px;height:760px;border-radius:50%;background:#FFD54A;border:6px solid #121613;box-shadow:12px 12px 0 #121613"></div><div class="abs" style="left:110px;top:1000px">{penny('open', w=680, wave=True)}</div>
{spark(780,1080,1.6,'#FFD54A')}{spark(900,1380,1)}{spark(120,860,.9,'#FFD54A')}
<div class="abs" style="left:0;right:0;bottom:150px;text-align:center;font-size:40px;font-weight:800;opacity:.9">Meet Penny, the Spencio piggy 🐷</div>
</div>''')
# 4 — the answer
TT.append(f'''<div class="s" style="background:{PAPER}"><div class="dots"></div>{top('4/5')}
<div class="cap" style="top:250px;font-size:110px">One number<i>.</i> No guessing<i>.</i></div>
<div class="card" style="left:110px;right:110px;top:560px;transform:rotate(-1.5deg)">
  <div class="line"><span>Balance</span><span>Rs 18,400</span></div>
  <div class="line"><span>Rent &amp; bills due</span><span>− Rs 12,600</span></div>
  <div class="line"><span>Trip fund goal</span><span>− Rs 1,500</span></div>
  <div style="margin-top:30px;padding:34px;border-radius:32px;background:{GREEN};color:#fff">
    <div style="font-size:30px;font-weight:700;letter-spacing:2px;text-transform:uppercase;opacity:.9">Safe to spend today</div>
    <div style="font-size:118px;font-weight:800;letter-spacing:-4px">Rs 2,150</div>
  </div>
</div>
<div class="abs" style="left:640px;bottom:170px">{penny('happy', w=380)}</div>
<div class="bub" style="left:72px;bottom:420px;width:540px;transform:rotate(-3deg)">"Dinner fits. Go have fun!"</div>
<div class="abs" style="left:72px;bottom:150px;font-size:24px;font-weight:700;color:#5D665F">Example figures</div>
</div>''')
# 5 — yes + CTA
TT.append(f'''<div class="s" style="background:#FF9F7A"><div class="ray"></div>{top('5/5')}
<div class="cap" style="top:250px;font-size:124px">Maya says yes<span style="color:#fff">.</span><br>Zero guilt<span style="color:#fff">.</span></div>
<div class="bub" style="left:480px;top:690px;width:530px;transform:rotate(3deg)"><small>Group chat · 6:44 PM</small>I'm in! 🍜🙌</div>
<div class="abs" style="left:-20px;bottom:330px">{maya('joy', phone=True, w=640)}</div>
<div class="abs" style="left:620px;bottom:330px">{penny('happy', w=360, wave=True)}</div>
<div class="abs" style="left:72px;right:72px;bottom:190px;display:flex;align-items:center;gap:24px;padding:28px 34px;border-radius:36px;background:{INK};color:#fff">
  <img src="{ICON.as_uri()}" style="width:96px;height:96px;border-radius:24px">
  <div><div style="font-size:48px;font-weight:800;letter-spacing:-1.5px">Know what's safe to spend<span style="color:{MINT}">.</span></div>
  <div style="font-size:30px;font-weight:700;color:#B8C2BA">Spencio · Free on App Store &amp; Google Play</div></div>
</div>
{spark(900,1000,1.2)}{spark(120,640,.8)}
</div>''')

# Facebook: 4-panel comic, 1080x1350
def panel(bg, inner, label):
    return f'<div style="position:relative;overflow:hidden;background:{bg};border:6px solid {INK};border-radius:36px">{inner}<div style="position:absolute;left:22px;top:22px;padding:8px 16px;border-radius:12px;background:{INK};color:#fff;font-size:22px;font-weight:800;letter-spacing:1px">{label}</div></div>'

FB = f'''<div class="s" style="height:1350px;background:{PAPER};padding:60px 56px 56px;display:flex;flex-direction:column;gap:26px">
<div style="display:flex;align-items:center;gap:18px"><img src="{ICON.as_uri()}" style="width:74px;height:74px;border-radius:20px"><b style="font-size:40px;font-weight:800;letter-spacing:-1.5px">Spencio</b><span style="margin-left:auto;font-size:28px;font-weight:800;color:#5D665F">A mid-month story</span></div>
<div style="font-size:70px;font-weight:800;letter-spacing:-.04em;line-height:1">Dinner invite on the 17th<span style="color:{GREEN}">?</span></div>
<div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:20px">
{panel('#FFD54A', f'<div class="abs" style="left:-30px;bottom:-40px">{maya("shock", phone=True, w=380)}</div><div class="bub" style="right:18px;top:70px;width:250px;font-size:28px;padding:16px 20px;border-width:4px;box-shadow:6px 6px 0 #121613;border-radius:26px">Dinner tonight? 🍜</div>', '1')}
{panel('#E7E1FF', f'<div class="abs" style="left:70px;bottom:-60px">{maya("worried", w=360)}</div><div class="cloud" style="left:20px;top:80px;font-size:24px;padding:10px 18px;border-width:4px;box-shadow:5px 5px 0 #121613">Rent? 🏠</div><div class="cloud" style="right:16px;top:130px;font-size:24px;padding:10px 18px;border-width:4px;box-shadow:5px 5px 0 #121613">Bills? 💡</div>', '2')}
{panel(GREEN, f'<div class="ray"></div><div class="abs" style="left:30px;bottom:-30px;width:330px;height:330px;border-radius:50%;background:#FFD54A;border:4px solid #121613"></div><div class="abs" style="left:40px;bottom:10px">{penny("open", w=310, wave=True)}</div><div class="bub" style="right:16px;top:70px;width:230px;font-size:26px;padding:16px 20px;border-width:4px;box-shadow:6px 6px 0 #121613;border-radius:26px">Let me count first.</div>', '3')}
{panel('#FF9F7A', f'<div class="abs" style="left:20px;top:72px;right:20px;padding:16px 20px;z-index:2;border-radius:24px;background:#fff;border:4px solid #121613"><div style="font-size:20px;font-weight:800;letter-spacing:1px;color:{GREEN}">SAFE TO SPEND TODAY</div><div style="font-size:58px;font-weight:800;letter-spacing:-2px">Rs 2,150</div></div><div class="abs" style="left:10px;bottom:-110px">{maya("joy", w=260)}</div><div class="abs" style="right:6px;bottom:6px">{penny("happy", w=190)}</div>', '4')}
</div>
<div style="display:flex;align-items:center;justify-content:space-between"><span style="font-size:34px;font-weight:800">Know what's safe to spend<span style="color:{GREEN}">.</span></span><span style="padding:16px 26px;border-radius:999px;background:{GREEN};color:#fff;font-size:26px;font-weight:800">Free on App Store &amp; Google Play</span></div>
</div>'''


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        jobs = [('facebook.png', FB, 1350)] + [(f'tiktok-{i}.jpg', h, 1920) for i, h in enumerate(TT, 1)]
        for name, body, h in jobs:
            f = OUT / f'_{name}.html'
            f.write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>')
            pg = await b.new_page(viewport={'width': 1080, 'height': h})
            await pg.goto(f.as_uri()); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(250)
            kw = {'type': 'jpeg', 'quality': 92} if name.endswith('.jpg') else {}
            await pg.screenshot(path=str(OUT / name), **kw)
        await b.close()
asyncio.run(main())
