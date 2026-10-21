# megaZINE: notes for Claude

megaZINE is a collective run by two editors, **Sam Ling** (GitHub `samuelling`, owns this repo) and **Matt Crump**. It collects weird little things: apps, toys, tools, demos, music, paintings, stories. Some made with Claude, some by hand. Each issue is one sheet of paper folded into an 8-page mini-zine; every code on the paper points at this site (GitHub Pages, `https://samuelling.github.io/megazine/`), and the site points at the work.

Whoever you're talking to is one of the two editors. Ask which one if it matters (it does for `makers` and the seal).

## The one rule

Every work says who made it and how. `makers` and `made` in `works.json` drive the gold **megaZINE seal** on the site and the black-and-white seal on the paper:
- `made`: `"hands"` (no AI), `"claude"` (Claude did the making), `"both"`.
- `makers`: first names as they should appear on the seal, e.g. `["Matt"]`, `["Sam", "Matt"]`. Optional `seal` overrides the text in the middle (keep it under ~10 characters).

Never guess `made`. Ask.

## Files

| Path | Edit? | What |
| --- | --- | --- |
| `works.json` | **Yes**, this is where almost all changes go | Every work and every issue. |
| `tools/page.html` | For site design changes | The site's source (a fragment, no `<html>`/`<head>`). |
| `index.html` | **Never by hand** | Built from `tools/page.html` by `python3 tools/build.py`. |
| `tools/make_sheet.py` | For paper layout changes | Builds `print/issue-NN.pdf` and `print/issue-NN-numbered.pdf`. |
| `media/` | Add files | Images for works (paintings, screenshots). Keep each under ~1 MB, JPG or WebP. |
| `print/` | Generated | Commit regenerated PDFs with the change that caused them. |

## A work entry

```json
{
  "id": "kebab-case-id",
  "title": "Name",
  "kind": "game | sound | music | tool | toy | art | painting | story",
  "made": "hands | claude | both",
  "makers": ["Matt"],
  "platform": "Web",
  "image": "media/kebab-case-id.jpg",
  "blurb": "Two or three plain sentences. The paper prints only the first one, so make it stand alone.",
  "links": [
    { "label": "Play", "url": "https://..." },
    { "label": "TestFlight", "url": null, "status": "Beta link soon" }
  ]
}
```

- `image` is optional; it shows on the site's card (good for paintings). The paper is text-only.
- A link with `"url": null` renders as a dashed "coming" button. The first link with a URL is where `?go=<id>` sends people.
- `"status": "workshop"` (and `"links": []`) lists it under **In the workshop**: mentioned, not out yet.
- Credit kids' ideas with `"idea": "Name"` (first names only).

## Issues

`issues[-1]` is the current issue; its `works` list is the lineup in order. The paper fits **12**: pages 3–7 take the first ten in pairs, page 2 takes the 11th, the back cover the 12th. More than 12 and the extras appear only on the site. Never change the `id` of a work that's in a printed issue: the paper's codes use it.

## After any change

```
python3 tools/build.py                 # rebuild index.html
pip install qrcode reportlab           # once
python3 tools/make_sheet.py            # only if the current issue's lineup or text changed
```

`make_sheet.py` prints a warning if a page overflows; shorten the first sentence of that work's blurb rather than shrinking type. Then commit with a plain message saying what changed and push to `main`; Pages redeploys in about a minute.

## Voice

Plain, dry, short. No hype, no "revolutionary". Blurbs describe what the thing does, in present tense, as a person would tell a friend.
