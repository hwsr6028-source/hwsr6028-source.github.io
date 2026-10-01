from pathlib import Path
import csv, re, unicodedata

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "bulk_columns.csv"
POSTS = ROOT / "_posts"

def safe_slug(s):
    s = unicodedata.normalize("NFKC", s.strip().lower())
    s = re.sub(r"[^a-z0-9가-힣\-]+", "-", s)
    return re.sub(r"-+", "-", s).strip("-")

POSTS.mkdir(exist_ok=True)

with CSV.open(encoding="utf-8-sig", newline="") as f:
    for row in csv.DictReader(f):
        date = row["date"].strip()
        slug = safe_slug(row["slug"] or row["title"])
        target = POSTS / f"{date}-{slug}.md"
        fm = f"""---
layout: post
title: {row["title"]!r}
seo_title: {row["seo_title"]!r}
description: {row["description"]!r}
category: {row["category"]!r}
date: {date} 09:00:00 +0900
---

{row["content"].strip()}
"""
        target.write_text(fm, encoding="utf-8")
        print("created", target.name)
