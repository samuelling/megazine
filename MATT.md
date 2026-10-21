# Matt: how to get your stuff into megaZINE

## Once

1. Accept the GitHub invite to `samuelling/megazine` (it went to CrumpLab; check your email or github.com/notifications).
2. Make sure your Claude can reach your GitHub (in the Claude app, GitHub under Settings → Connectors, or use Claude Code on your Mac).
3. Ask Sam to add you to the stats dashboard at megazine.goatcounter.com (or he'll make it public).

## Every time

Paste this to Claude, then tell it what you want to do:

> I'm Matt Crump, co-editor of megaZINE with Sam Ling. The repo is github.com/samuelling/megazine. Please add it to this session, read CLAUDE.md in it, and follow it.

Then just talk normally, e.g.:

- "Add my painting *Name*. Here's the photo. Made by hand."
- "Add my iOS app *Name*, TestFlight link is …, made with Claude."
- "Add *Name* to the workshop list; it's not out yet."
- "Put my two newest pieces in Issue 02."

Claude will ask if you don't say: how it was made (by hand, by Claude, or both) and where it lives (a link, or a photo for paintings).

Descriptions stay oblique about influences: no names of other people's games, films, brands or characters, and no borrowed artwork. Claude will reword if you mention them.

## How the site works

- **The issue** is the current lineup. Its cards appear in a new random order on every visit, so nobody's piece is always first.
- **In the workshop** lists things still being built: named and described, no links.
- **Seals:** every piece gets a gold megaZINE seal: "MADE BY MATT" plus how it was made. It's the one rule.
- **Paintings** show their photo on the card.
- **Links can wait.** A link marked "soon" shows as a dashed button; fill it in later and every printed code for that piece starts working, no reprint.

## Other people's work

Outsiders submit through The Septic Tankz BBS: they dial in, make an account, Sam validates them as SysOp, and they post in the **megaZINE Submissions** message base (its first post has the template). To accept one, tell Claude "add <title> from <handle>'s BBS submission" and paste or summarize the post; it goes in with their name on the seal.

## The paper

- One letter-size sheet folds into an 8-page mini-zine. It fits **12** pieces from the current issue; any beyond 12 appear only on the site.
- Every code on the paper goes through the site first, so links can change after printing.
- If you change the current issue, Claude regenerates `print/issue-NN.pdf` (one master) and `print/issue-NN-numbered.pdf` (numbered copies, each with its own back-cover code).

## Stats

The dashboard at **megazine.goatcounter.com** shows visits (`/`), paper scans per piece (`/scan/<id>`), back-cover scans per copy (`/scan/copy-<n>`), and clicks out to each piece (`/click/<id>`).
