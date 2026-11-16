# blocmind-marketing

Everything behind blocmind's social posts: the playbook, brand assets, card templates, every post's images and captions, and the post log.

The repo is **public on purpose**. Every image pushed here gets a public link straight away, which is what Facebook (via Windsor.ai) and TikTok (via Metricool) need to publish it:

```
https://raw.githubusercontent.com/BlocMind/blocmind-marketing/main/posts/<date>/<file>.png
```

Only put things here that are meant to be public.

## Layout
```
playbook.md            rotation, trends, tone, banned topics: the daily task follows this
brand/brand.md         colours, apps, links, voice
brand/fonts/           Plus Jakarta Sans (500, 700, 800)
brand/icons/           app icons
templates/card.html    the card template for every app (Facebook 1080×1350, TikTok 1080×1920)
scripts/render.py      post.json → facebook.png + tiktok-N.png
posts/YYYY-MM-DD/      one folder per day: images, post.json, captions.md
log.md                 one line per day: app, angle, what posted
```

## Daily flow (automated, 19:06 Asia/Colombo)
1. Pick the day's app from `playbook.md` and a trend that fits it.
2. Write `posts/<date>/post.json` and `captions.md`.
3. `python3 scripts/render.py posts/<date>/post.json`
4. Commit and push to `main`.
5. Post to Facebook with the raw `facebook.png` link, and schedule the TikTok carousel for 19:30 with the raw `tiktok-N.png` links.
6. Add a line to `log.md` and push.

## Render locally
```bash
pip install playwright && python3 -m playwright install chromium
python3 scripts/render.py posts/2026-11-17/post.json
```
