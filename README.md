# Luca Cossu — Personal Academic Website

Static site for GitHub Pages. All content lives in `data/*.json` —
you never need to touch `index.html` for routine updates.

---

## Project structure

```
/
├── index.html          # Layout, styles, rendering logic (rarely edited)
├── README.md
└── data/
    ├── profile.json        # Name, title, stats, badges, contact links
    ├── research.json       # Research area cards
    ├── publications.json   # Full publication list
    ├── projects.json       # Research projects & grants
    ├── education.json      # Degree & career timeline
    ├── awards.json         # Awards and honors
    └── teaching.json       # Courses and co-advised theses
```

---

## Deploy on GitHub Pages

1. Create a repo called `<your-github-username>.github.io`
2. Push the entire folder (with `data/`) to the `main` branch
3. Go to **Settings → Pages → Source → Deploy from branch: `main` / `/ (root)`**
4. Your site goes live at `https://<your-github-username>.github.io`

> **Note:** GitHub Pages serves files via HTTP, so `fetch()` works correctly.
> If you open `index.html` directly as a local file (`file://`), the browser
> blocks `fetch()` and shows a warning. Use a local server instead:
> ```
> python3 -m http.server
> # then open http://localhost:8000
> ```

---

## How to update content

### Add a new publication — `data/publications.json`

Copy an existing object and fill in the fields:

```json
{
  "year": 2026,
  "type": "journal",          // "journal" | "conference" | "book"
  "first_author": true,       // true = bold title + appears in "First author" filter
  "title": "Your paper title here",
  "authors": "L. Cossu, G. Cappon, A. Facchinetti",
  "authors_note": "* equally contributed",   // optional
  "venue": "Journal of Diabetes Science and Technology",
  "doi": "10.xxxx/xxxxxx"    // omit field if no DOI yet
}
```

Publications are rendered in the order they appear in the file.
Sort descending by year (newest first) for consistency.

---

### Add a research project — `data/projects.json`

```json
{
  "title": "Project Name — Funder",
  "period": "2025–2027",
  "tag_color": "teal",        // "teal" | "gold"
  "description": "What you did in this project.",
  "pills": ["Funder", "Budget", "Topic", "Tool"]
}
```

---

### Add a research area card — `data/research.json`

```json
{
  "icon": "🧬",
  "color": "#ddf0f1",         // background of the icon box
  "title": "New Research Topic",
  "description": "Brief description shown on the card."
}
```

---

### Update your stats — `data/profile.json`

Edit the `stats` array:

```json
"stats": [
  { "value": "15",  "label": "Journal papers" },
  { "value": "9",   "label": "Conference papers" },
  { "value": "6",   "label": "H-index" },
  { "value": "120", "label": "Citations (GS)" }
]
```

---

### Update contact / profile links — `data/profile.json`

```json
"links": {
  "scholar":  "https://scholar.google.com/citations?user=YOUR_ID",
  "orcid":    "https://orcid.org/YOUR-ORCID",
  "linkedin": "https://www.linkedin.com/in/your-handle"
}
```

---

### Add a thesis to co-advisorship — `data/teaching.json`

Append to the `theses` array:

```json
{
  "period": "2025–2026",
  "name": "Student Name",
  "title": "Thesis title here"
}
```

---

### Add an award — `data/awards.json`

```json
{
  "year": 2026,
  "title": "Award Name",
  "description": "Brief description of what the award is for."
}
```

---

## Theming

All colors are CSS variables at the top of `index.html`:

```css
--accent: #c1440e;   /* terracotta — change this to retheme everything */
--teal:   #1b6b72;
--gold:   #b08030;
--ink:    #0f1117;
--paper:  #f7f6f2;
```

Changing `--accent` alone is enough to completely retheme the site.
