# fitsize

Compress an image to fit under the file size you need — by searching for the
right JPEG quality level instead of guessing it.

**Live:** https://web-production-60a6a.up.railway.app

## Why

Upload forms keep rejecting my photos for being too large. The tools I found
either cost money or only get you somewhere near the target size. Most of them
compress once at a guessed quality level and hand you whatever comes out.

fitsize searches for the highest quality that still fits under your target.

## How it works

JPEG has a quality setting from 1 to 95, but there is no way to ask for a
specific file size directly. So the app runs a binary search over the quality
levels: compress at quality 62, measure the result, go up or down, repeat.
After about seven passes it has found the highest quality that stays under
the target.

I limit the search to 30–95 because below 30 the compression artifacts get
too ugly to be useful.

If quality alone is not enough, the image is scaled down to 70% of its edge
length and the search runs again — repeatedly, until it fits or the image
would drop below 600px width. In that case you get an error message instead
of a file.

## Features

- [x] Upload a JPEG or PNG, enter a target size in KB, the result downloads automatically
- [x] Finds the highest JPEG quality under the target, or explains why it can't
- [x] Files are processed in memory only — nothing is written to disk or stored
- [x] Deployed and reachable under one URL
- [ ] Clear error message for oversized uploads
- [ ] Custom domain

## Not in scope

- HEIC, WebP, AVIF, RAW
- Batch processing
- Accounts, history, stored files

## Trade-offs

- **Server-side processing.** Files are uploaded, processed in RAM, and
  returned with the response. Nothing touches a disk or database. A
  browser-only version would avoid the upload entirely, but this project
  is a Python exercise.
- **Quality over speed.** The binary search runs several compression passes,
  so a result takes a moment longer than a single-pass tool.
- **Transparency is lost.** PNGs with an alpha channel are converted to RGB,
  since JPEG has no transparency.

## Run locally
pip(3) install -r requirements.txt


Create a `.env` file with:

secret_key=any-random-string


Then:

python app.py


The app runs at http://localhost:5555 

## Tech

Python, Flask, Pillow

## Status

Deployed and working. Open: upload size limit, custom domain.