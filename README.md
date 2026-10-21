# megaZINE

A collective of weird little apps, sounds, games, paintings and stories. Between money and doom.

Each issue is one sheet of paper folded into an 8-page mini-zine. Every code on the paper points at this site, and the site points at the work, so links can change without reprinting.

## What's here

| Path | What it is |
| --- | --- |
| `index.html` | The site. Built from `tools/page.html`; don't edit it directly. |
| `works.json` | Every work and every issue. This is the only file you edit to add things. |
| `print/issue-01.pdf` | The sheet to photocopy (one master, unnumbered). |
| `print/issue-01-numbered.pdf` | 50 numbered copies, each with its own back-cover code. |
| `tools/make_sheet.py` | Regenerates the PDFs from `works.json`. |
| `tools/build.py` | Regenerates `index.html` from `tools/page.html`. |
| `media/` | Images for works (paintings, screenshots). |
| `CLAUDE.md` | Instructions Claude follows when working in this repo. |
| `MATT.md` | How Matt (or anyone) adds work by talking to Claude. |

## Put it online (once)

1. Create a public repo named `megazine` under `samuelling`.
2. Push this folder to it.
3. Repo **Settings → Pages → Deploy from branch → main / root**.
4. The site appears at `https://samuelling.github.io/megazine/`, which is the address already printed in the codes. If you pick a different name, change `base_url` in `works.json` and rerun `make_sheet.py` before printing.

## Add a work

Add an entry to `works` in `works.json`:

```json
{
  "id": "short-id",
  "title": "Name",
  "kind": "game | sound | music | tool | toy | art | painting | story",
  "made": "hands | claude | both",
  "makers": ["Matt"],
  "platform": "Web",
  "image": "media/short-id.jpg",
  "blurb": "Two or three plain sentences. The paper uses the first one.",
  "links": [
    { "label": "Play", "url": "https://..." },
    { "label": "TestFlight", "url": null, "status": "Beta link soon" }
  ]
}
```

Keep blurbs oblique about influences: don't name other people's games, films, brands or characters, and don't use their artwork (see `CLAUDE.md`).

A link with `"url": null` shows as a dashed "coming" button. Fill the URL in later and every printed code for it starts working, no reprint needed.

`makers` and `made` print the gold seal: "MADE BY MATT · BY HAND". `image` is optional (paintings). Add `"status": "workshop"` with no links to list something as still being built.

To feature it in an issue, add its `id` to that issue's `works` list (the paper fits 12). Workshop items show up under **In the workshop**.

## Outside submissions

Anyone else submits through The Septic Tankz BBS (`samuelling.github.io/BBS`): make an account, wait for the SysOp to validate it, then post in the **megaZINE Submissions** base using the template in its first post. The SysOp is pinged for each submission. Accepted pieces go into `works.json` with the submitter's name on the seal.

## Links the site understands

- `/?go=townies` jumps straight to that work's first live link (this is what the paper codes use). If the work has no live link yet, it shows its card instead.
- `/?copy=37` shows "You're holding copy 37 of 50" plus a starting point picked from the issue by copy number.
- `/?w=townies` scrolls to and highlights a card.

## Visitor stats

Counts go to [GoatCounter](https://www.goatcounter.com) (free for non-commercial sites, no cookies, no banner needed), only from the live site.

**Set up once:** sign up at goatcounter.com/signup and choose the site code `megazine` (it's set as `zine.goatcounter` in `works.json`; if you pick another code, change it there). Then in GoatCounter's settings, add Matt as a user, and optionally make the dashboard public.

**Dashboard:** `https://megazine.goatcounter.com`

| Path | Means |
| --- | --- |
| `/` | A visit to the site. |
| `/scan/<id>` | Someone scanned that work's code on the paper. |
| `/scan/copy-<n>` | Someone scanned the back cover of copy *n*. |
| `/click/<id>` | Someone clicked out to that work from the site. |

## Make the paper

```
pip install qrcode reportlab
python3 tools/make_sheet.py              # 50 numbered copies by default
python3 tools/make_sheet.py --copies 100
```

Print single-sided on letter paper, landscape, at 100% (no "fit to page"). Black only; it's designed for a photocopier.

**Fold:** the top row prints upside down, which is correct.
1. Fold in half the long way (top to bottom), then unfold.
2. Fold in half the short way, then into quarters, so you have 8 panels. Unfold.
3. Cut along the dashed line in the middle (only between the two centre panels).
4. Refold the long way, push the ends together so the cut opens into a diamond, and flatten into a booklet with the cover on the front.

## To fill in

- `ambit` → App Store URL once Ambit: Quartet clears review.
- `townies` → TestFlight public link for (Water) Townies.
- Matt's work: paintings, his iOS app, anything (see `MATT.md`).
