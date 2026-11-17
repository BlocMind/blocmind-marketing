# Playbook

Followed by the daily task "blocmind daily social post" (19:06 Asia/Colombo). One post per day on the **blocmind Facebook Page** (published right away via **Windsor.ai**, `facebook_organic`, account `1316150458256111`) and **blocmind TikTok** (scheduled for **19:30** via **Metricool**, brand `8139300`). Edit this file to change what the posts do; the next run follows it.

## Rotation (Fairloop weighted)
| Weekday | App |
|---|---|
| Mon | Fairloop |
| Tue | Spencio |
| Wed | Fairloop |
| Thu | Reap |
| Fri | Markeo |
| Sat | Fairloop |
| Sun | Axilo |

Use the weekday in Asia/Colombo. If the same app + angle is in the last 14 lines of `log.md`, pick a different angle.

## Apps
See `brand/brand.md` for what each app does, its link, store status and colours.

## Trend step
1. Search the web for today's trending topics, hashtags and memes (Google Trends daily, TikTok Creative Center, X trends; Sri Lanka and global).
2. Pick ONE that connects naturally to the day's app (a big match or concert → splitting tickets with Fairloop; payday or holiday shopping → Spencio; a viral recipe → Reap; a "saving this for later" meme → Markeo; a loud event or science moment → Axilo).
3. If nothing fits safely, use an everyday moment (end of month, weekend plans, groceries, trip season). Never force it.

## Brand safety (hard rules)
Never tie a post to tragedies, disasters, deaths, accidents, wars, terrorism, crime, politics, elections, religion, health scares, layoffs, anyone's personal life, or anything mocking a person or group. No real people's photos or names, no celebrity likenesses, no other brands' logos or characters, no films, games or sports leagues, no song lyrics. No invented stats, reviews, user counts or prices. No "free" claims beyond what the apps really offer. Calm, plain voice: short sentences, no hype, no ALL CAPS, at most one emoji.

## Post format
- `posts/<date>/post.json` → `python3 scripts/render.py posts/<date>/post.json`.
- **Facebook:** `facebook` slide (eyebrow ≤ 48 chars naming the trend, headline ≤ 90 ending in . or ?, sub ≤ 170). Caption: 2–4 short lines, call to action, app link, 3–5 hashtags.
- **TikTok:** 3–4 `tiktok` slides: hook naming the trend → 1–2 slides showing the app solving it → "Get <App>." slide. Caption ≤ 150 chars + 4–6 hashtags.
- Always `#blocmind` plus the app tag (`#fairloop #spencio #reap #markeo #axilo`).
- Save both captions in `posts/<date>/captions.md`.

## TikTok safe area (1080×1920)
TikTok draws its own UI over photo posts. Keep ALL text, logos, buttons and key art inside the safe area, or it gets covered:
- **Top 300px:** status bar and the "Find related content" search bar. Background only.
- **Bottom 420px:** caption, username, carousel dots and comment box. Background only.
- **Right 180px:** like / comment / save / share buttons (from mid-slide down). Background only.
- Safe box: x 84–900, y 300–1500. `scripts/render.py` already pads to this; hand-made slides must follow it too. Facebook cards (1080×1350) have no overlay.
- Check before publishing: look at every TikTok slide and confirm nothing important sits outside the safe box.

## Failure handling
- Facebook photo post fails → retry once → post text + app link instead.
- TikTok not connected or fails twice → skip TikTok today.
- Any failure or skip → push notification to the owner saying what to fix.

## Log
Append to `log.md`: `YYYY-MM-DD · app · trend/angle · FB ok|fallback|fail · TikTok ok|skipped|fail`
