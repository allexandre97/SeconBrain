---
type: overview
status: active
created: 2026-07-01
updated: 2026-07-01
areas: []
categories:
  - admin/wiki-maintenance
tags:
  - authors
  - metadata
related:
  - "[[wiki/entities/README]]"
sources: []
sensitivity: public
encryption: none
graph_exclude: true
---

# Author Entities

Author entity pages are optional. Create them when an author appears in multiple ingested sources or is especially relevant to the wiki.

Do not create an author page for every one-off paper author by default. Source pages may still list authors in frontmatter without corresponding author entity pages.

Author entity pages should use:

```yaml
---
type: entity
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
entity_type: author
aliases: []
sources: []
categories: []
graph_exclude: false
---
```

Use source-page frontmatter for ordinary bibliographic browsing:

```yaml
authors:
  - "Author Name"
author_entities:
  - "wiki/entities/authors/author-name"
year: 2026
venue: "Venue"
doi: "10.xxxx/example"
arxiv: "2603.16770v1"
```
