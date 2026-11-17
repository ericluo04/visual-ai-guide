# Visual AI Field Guide

A one-page practitioner guide to current visual AI tools for marketing research. It covers image embeddings (global and patch level), labeling images with vision-language models, predicting outcomes from images, inference with predicted variables, image generation, and video generation and analysis. A further section covers specialized tools: detection and segmentation, OCR, faces, saliency, and aesthetics.

Each section lists the best open and closed options, gives a short illustrative Python snippet, links the leaderboard that tracks the field, and cites a marketing paper that uses the method.

## Files

- `index.html` is the whole site. It has no build step. Styles and scripts are inline. It loads Google Fonts and Prism (code highlighting) from cdnjs.
- The decision guide data is the `window.GUIDE` object in the "Choose a method" section of `index.html`.

## Update the picks

1. Open the "Track it" links in the section you want to update.
2. Edit the picks table in that section of `index.html`.
3. Edit the matching leaf in `window.GUIDE` if the name changed.
4. Change the "Released" month in the picks table if the model version changed.
5. Change the "Checked" date in the side rail and in the "How to read this guide" Track it card.

Model rankings were checked on 17 November 2026.

## Preview locally

```
python3 -m http.server 8000
```

Then open http://localhost:8000.
