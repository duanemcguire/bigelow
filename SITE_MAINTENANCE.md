# Maintaining this site

## Straight HTML pages
### pages (e.g. index, news, company, etc)

These are in the pages directory with the extension of .vue  These files are straight HTML.  The \<SCRIPT> section is used to set page title and description for Search Engine Optimization (SEO) only.

## Organ pages
### content/organs (meta data)
Basic data about the organ is created in markdown files in the content/organs directory. The top section contains meta data for the organ which will be used on the specs, stoplist, and opus  list pages.

As example, Opus 37 has the following meta data:
```
---
opus: 37
year: 2020
owner: [Musical Instrument Museum, Restoration of 1859 Robjohn]
location: Phoenix, AZ
manuals: 2
voices: 10
ranks: 11
---
```
That's pretty clear. The only wrinkle is the "owner" data. Some of the  "owner" data is displayed as multiple lines. So the owner is shown here as a comma separated list. The comma between "Museum" and "Restoration" shows where the line break will be.  The square braces are required whether or not owner data is single or multiple.

Following the ending "---", additional markdown text or HTML may be included.   Those general remarks for the organ appear in the left sidebar of the specs and stoplist pages.

### pages/opus (Specs display pages)
These pages appear in pages/opus with a naming convention that matches the meta data described above.  e.g. 11-specs.vue is the display page for the organ created in content/organs/11-specs.md The only HTML to be editted here is the photos for display.

### static (images and PDFs)
Each organ is expected to have at least a thumb.jpg Image naming convention must be followed.

Each organ is expected to have a PDF stoplist document.  Naming convention must be followed.
