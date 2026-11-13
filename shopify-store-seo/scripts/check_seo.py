#!/usr/bin/env python3
"""check_seo.py — check product SEO in a Shopify product CSV before publishing.

Part of the shopify-store-seo Claude skill.
See shopify-store-seo/SKILL.md, Step 8, for the full workflow.

What it does:
  Reads a product CSV in Shopify export format (see
  templates/seo-product-sample.csv) and reports every SEO problem it
  finds, one line per problem:
    - missing SEO title or SEO description
    - SEO title over 60 characters, or under 30 characters
    - SEO description over 160 characters, or under 120 characters
    - missing image alt text
    - duplicate SEO titles across products
    - product title over 70 characters
    - missing or very short product description (Body under 50 chars)
    - duplicate product Handles

  It reads these columns when present: Handle, Title, Body (HTML),
  Image Src, Image Alt Text, SEO Title, SEO Description. A missing
  SEO column is reported once as a missing column, not once per row.

  Prints PASS when there are no problems, FAIL with the problem list
  otherwise. Exits 0 on PASS, 1 on FAIL. Do not publish SEO that
  fails the check — fix every problem, then run the checker again.

Usage:
  python3 check_seo.py <products.csv>

  Example:
    python3 check_seo.py ../templates/seo-product-sample.csv

Requirements: Python 3, standard library only. No credentials, no network.
"""

import csv
import html
import re
import sys

# Hard limits from SKILL.md Step 5 (meta) and Step 2 (titles).
SEO_TITLE_MAX = 60
SEO_TITLE_MIN = 30
SEO_DESC_MAX = 160
SEO_DESC_MIN = 120
PRODUCT_TITLE_MAX = 70
BODY_MIN = 50
ALT_TEXT_MAX = 125

SEO_COLUMNS = [
    "Handle",
    "Title",
    "Body (HTML)",
    "Image Src",
    "Image Alt Text",
    "SEO Title",
    "SEO Description",
]


def strip_html(text):
    """Remove HTML tags and entities so length is measured on plain text."""
    no_tags = re.sub(r"<[^>]+>", " ", text or "")
    return html.unescape(no_tags).strip()


def check(path):
    """Check the CSV at path. Returns a list of problem strings."""
    problems = []

    try:
        with open(path, newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames is None:
                return ["File has no header row."]
            columns = [name.strip() for name in reader.fieldnames if name]
            rows = list(reader)
    except FileNotFoundError:
        return ["File not found: %s" % path]
    except (OSError, csv.Error) as exc:
        return ["Could not read %s: %s" % (path, exc)]

    missing = [col for col in SEO_COLUMNS if col not in columns]
    for col in missing:
        problems.append("Missing column: %s" % col)
    if "Handle" not in columns or "Title" not in columns:
        return problems  # Cannot check rows without Handle and Title.

    if not rows:
        return ["File has a header row but no product rows."]

    seen_handles = {}
    seen_seo_titles = {}
    for index, row in enumerate(rows, start=2):  # Row 1 is the header.
        label = "Row %d" % index
        handle = (row.get("Handle") or "").strip()
        title = (row.get("Title") or "").strip()
        body = strip_html(row.get("Body (HTML)") or "")
        image = (row.get("Image Src") or "").strip()
        alt = (row.get("Image Alt Text") or "").strip()
        seo_title = (row.get("SEO Title") or "").strip()
        seo_desc = (row.get("SEO Description") or "").strip()

        if not handle:
            problems.append("%s: Handle is empty." % label)
        elif handle in seen_handles:
            problems.append(
                "%s: duplicate Handle %r (first used on row %d)."
                % (label, handle, seen_handles[handle])
            )
        else:
            seen_handles[handle] = index

        if not title:
            problems.append("%s: Title is empty." % label)
        elif len(title) > PRODUCT_TITLE_MAX:
            problems.append(
                "%s: Title is %d characters (over %d): %r"
                % (label, len(title), PRODUCT_TITLE_MAX, title)
            )

        if not body:
            problems.append("%s: Body (HTML) is empty — no description." % label)
        elif len(body) < BODY_MIN:
            problems.append(
                "%s: description is only %d characters (under %d)."
                % (label, len(body), BODY_MIN)
            )

        if image and not alt:
            problems.append(
                "%s: Image Alt Text is missing for image %r."
                % (label, image)
            )
        if alt and len(alt) > ALT_TEXT_MAX:
            problems.append(
                "%s: Image Alt Text is %d characters (over %d)."
                % (label, len(alt), ALT_TEXT_MAX)
            )

        if not seo_title:
            problems.append("%s: SEO Title is missing." % label)
        else:
            if len(seo_title) > SEO_TITLE_MAX:
                problems.append(
                    "%s: SEO Title is %d characters (over %d): %r"
                    % (label, len(seo_title), SEO_TITLE_MAX, seo_title)
                )
            elif len(seo_title) < SEO_TITLE_MIN:
                problems.append(
                    "%s: SEO Title is only %d characters (under %d): %r"
                    % (label, len(seo_title), SEO_TITLE_MIN, seo_title)
                )
            key = seo_title.lower()
            if key in seen_seo_titles:
                problems.append(
                    "%s: duplicate SEO Title %r (first used on row %d)."
                    % (label, seo_title, seen_seo_titles[key])
                )
            else:
                seen_seo_titles[key] = index

        if not seo_desc:
            problems.append("%s: SEO Description is missing." % label)
        elif len(seo_desc) > SEO_DESC_MAX:
            problems.append(
                "%s: SEO Description is %d characters (over %d)."
                % (label, len(seo_desc), SEO_DESC_MAX)
            )
        elif len(seo_desc) < SEO_DESC_MIN:
            problems.append(
                "%s: SEO Description is only %d characters (under %d)."
                % (label, len(seo_desc), SEO_DESC_MIN)
            )

    return problems


def main(argv):
    if len(argv) != 2:
        print("Usage: %s <products.csv>" % argv[0], file=sys.stderr)
        return 2

    path = argv[1]
    problems = check(path)

    if problems:
        print("FAIL: %d problem(s) in %s" % (len(problems), path))
        for problem in problems:
            print("  - %s" % problem)
        print("Fix every problem above, then run the checker again.")
        print("Do not publish SEO that fails the check.")
        return 1

    print("PASS: %s — all product SEO checks passed." % path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
