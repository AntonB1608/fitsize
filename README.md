# fitsize

Compress an image to the exact file size you need — in your browser,
without uploading anything.

## Why

Upload forms keep rejecting my photos for being too large. The tools I found
either cost money or only get you "roughly" to the target size.

## Done means

- Drop in a JPEG or PNG, type a target size in KB or MB, get a file back
- The result lands within 5% of the target, or tells me why it can't
- Everything runs client-side; no file ever leaves the device
- Works on mobile Safari and Chrome
- Deployed and reachable under one URL

## Not in scope

- HEIC, WebP, AVIF
- Batch processing
- Accounts, history, storage

## Tradeoffs

- Browser-Encoder instead of MozJPEG
- no HEIC

but:

- no Uploads
- shorter waiting time
