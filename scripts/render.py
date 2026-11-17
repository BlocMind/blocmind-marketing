#!/usr/bin/env python3
"""Render a day's post images from a spec.

Usage:
  python3 scripts/render.py posts/2026-11-17/post.json

post.json:
{
  "app": "fairloop",                    # spencio | reap | markeo | axilo | fairloop
  "facebook": {"eyebrow": "...", "headline": "...", "sub": "...", "cta": ""},
  "tiktok": [                           # 3-4 slides
    {"eyebrow": "...", "headline": "...", "sub": "..."},
    ...
  ]
}

Writes facebook.png (1080x1350) and tiktok-1.jpg ... (TikTok only accepts JPEG/WebP) (1080x1920) next to post.json.
Needs: pip install playwright && python3 -m playwright install chromium
"""
import asyncio, html, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = (ROOT / "templates" / "card.html").read_text()

THEMES = {
    "fairloop": dict(appName="Fairloop", bg="#121613", fg="#F6F7F5", accent="#AFEA6A", sub="#B8C2BA", chipBg="rgba(255,255,255,.1)", chipFg="#D9F2E2", ctaFg="#11190A", mind="#AFEA6A", cta="On Google Play · iPhone soon"),
    "spencio": dict(appName="Spencio", bg="#F6F7F5", fg="#121613", accent="#1F9D55", sub="#3A403B", chipBg="#D9F2E2", chipFg="#14532D", ctaFg="#FFFFFF", mind="#1F9D55", cta="Free on App Store & Google Play"),
    "reap": dict(appName="Reap", bg="#EDF8F4", fg="#0F2A22", accent="#0CA678", sub="#335247", chipBg="#CDEEE3", chipFg="#0B6E52", ctaFg="#FFFFFF", mind="#0CA678", cta="Free on Google Play"),
    "markeo": dict(appName="Markeo", bg="#1E1840", fg="#FFFFFF", accent="#B3A6FF", sub="#C9C2F5", chipBg="rgba(255,255,255,.1)", chipFg="#C9C2F5", ctaFg="#1E1840", mind="#B3A6FF", cta="Free on App Store & Google Play"),
    "axilo": dict(appName="Axilo", bg="linear-gradient(160deg,#6C5CE7,#8B7FE8)", fg="#FFFFFF", accent="#FFBE0B", sub="rgba(255,255,255,.9)", chipBg="rgba(255,255,255,.16)", chipFg="#FFFFFF", ctaFg="#1E2140", mind="#FFBE0B", cta="Free on App Store & Google Play"),
}


def fill(app, f, slide, n=""):
    t = dict(THEMES[app])
    h = slide["headline"].strip()
    body, stop = (h[:-1], h[-1]) if h[-1:] in ".?!" else (h, ".")
    tall = f == "tt"
    vals = dict(
        t, app=app,
        w=1080, h=1920 if tall else 1350,
        pad="300px 180px 420px 84px" if tall else "84px 84px 80px",  # TikTok safe area: top 300 (status + search bar), bottom 420 (caption, dots), right 180 (action buttons)
        big=(92 if len(h) > 48 else 112) if tall else (88 if len(h) > 48 else 104),
        subSize=46 if tall else 40,
        headline=html.escape(body), stop=html.escape(stop),
        eyebrowChip=f'<span class="eyebrow">{html.escape(slide["eyebrow"])}</span>' if slide.get("eyebrow") else "",
        subP=f'<p>{html.escape(slide["sub"])}</p>' if slide.get("sub") else "",
        nChip=f'<span class="n">{html.escape(n)}</span>' if n else "",
    )
    if slide.get("cta"):
        vals["cta"] = slide["cta"]
    vals["cta"] = html.escape(vals["cta"])
    out = TEMPLATE
    for k, v in vals.items():
        out = out.replace("{{" + k + "}}", str(v))
    return out, vals["w"], vals["h"]


async def main(spec_path):
    from playwright.async_api import async_playwright
    spec_path = pathlib.Path(spec_path).resolve()
    spec = json.loads(spec_path.read_text())
    app = spec["app"]
    out_dir = spec_path.parent
    jobs = []
    if spec.get("facebook"):
        jobs.append(("facebook.png", *fill(app, "fb", spec["facebook"])))
    slides = spec.get("tiktok") or []
    for i, s in enumerate(slides, 1):
        jobs.append((f"tiktok-{i}.jpg", *fill(app, "tt", s, f"{i}/{len(slides)}")))
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, page_html, w, h in jobs:
            tmp = ROOT / "templates" / f"_render_{name}.html"  # beside the template so relative font/icon paths resolve
            tmp.write_text(page_html)
            pg = await b.new_page(viewport={"width": w, "height": h})
            await pg.goto(tmp.as_uri())
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(200)
            await pg.screenshot(path=str(out_dir / name), **({"type": "jpeg", "quality": 92} if name.endswith(".jpg") else {}))
            await pg.close()
            tmp.unlink()
            print(out_dir / name)
        await b.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    asyncio.run(main(sys.argv[1]))
