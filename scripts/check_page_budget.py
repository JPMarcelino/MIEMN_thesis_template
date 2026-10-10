#!/usr/bin/env python3
"""Report per-section page counts against the DCM dissertation budgets.

Usage:
    python3 scripts/check_page_budget.py thesis.pdf [--industrial] [--strict]

The DCM rules (2014, amended Nov 2020) cap the written content at 33 pages
and give per-section budgets. This script reads the PDF's table-of-contents
file (thesis.toc) to find where each chapter starts, works out how many
pages each one spans, and prints a table.

Exit status is 0 unless --strict is given and something is over budget.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

# Section title (as it appears in the ToC) -> page budget.
BUDGETS = {
    "Introduction": 5,
    "Materials and Methods": 2,
    "Results and Discussion": 20,
    "Conclusions and Future Perspectives": 2,
    "Bibliography": 2,
}
# Extended budget for theses done in an industrial environment.
INDUSTRIAL_BUDGETS = {"Materials and Methods": 6}

TOC_CHAPTER = re.compile(
    r"\\contentsline\s*\{chapter\}\{(?P<title>.*)\}\{(?P<page>\d+)\}"
    r"(?:\{[^}]*\})?\s*%?\s*$"
)


def clean_title(raw: str) -> str:
    """Strip LaTeX macros/braces from a ToC title."""
    title = re.sub(r"\\numberline\s*\{[^}]*\}", "", raw)
    title = re.sub(r"\\[a-zA-Z]+\s*", "", title)
    title = title.replace("{", "").replace("}", "")
    return title.strip()


def read_toc(toc_path: Path) -> list[tuple[str, int]]:
    entries: list[tuple[str, int]] = []
    for line in toc_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        match = TOC_CHAPTER.search(line)
        if match:
            entries.append((clean_title(match.group("title")), int(match.group("page"))))
    return entries


def pdf_page_count(pdf_path: Path) -> int | None:
    """Count pages, preferring pdfinfo and falling back to a raw scan."""
    try:
        out = subprocess.run(
            ["pdfinfo", str(pdf_path)],
            capture_output=True, text=True, check=False,
        ).stdout
        match = re.search(r"^Pages:\s+(\d+)", out, re.MULTILINE)
        if match:
            return int(match.group(1))
    except (OSError, ValueError):
        pass

    data = pdf_path.read_bytes()
    count = len(re.findall(rb"/Type\s*/Page(?![s])", data))
    return count or None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", nargs="?", default="thesis.pdf", help="built PDF")
    parser.add_argument("--toc", default="thesis.toc", help="LaTeX .toc file")
    parser.add_argument("--industrial", action="store_true",
                        help="use the extended Materials and Methods budget (6 pages)")
    parser.add_argument("--strict", action="store_true",
                        help="exit non-zero when a section is over budget")
    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    toc_path = Path(args.toc)

    if not pdf_path.exists() or not toc_path.exists():
        print(f"error: need both {pdf_path} and {toc_path} (build the thesis first)")
        return 1

    entries = read_toc(toc_path)
    if not entries:
        print("error: no chapters found in the .toc file")
        return 1

    total_pages = pdf_page_count(pdf_path)
    # Content starts at the first numbered chapter (page 1).
    first_page = min(page for _, page in entries)
    last_page = total_pages if total_pages else max(page for _, page in entries)

    # Everything after the bibliography is annex material and is excluded
    # from the 33-page count.
    content_end = last_page
    for index, (title, _start) in enumerate(entries):
        if title == "Bibliography":
            content_end = (
                entries[index + 1][1] - 1
                if index + 1 < len(entries)
                else last_page
            )
            break

    budgets = dict(BUDGETS)
    if args.industrial:
        budgets.update(INDUSTRIAL_BUDGETS)

    print(f"PDF: {pdf_path}  ({total_pages or '?'} pages total)")
    print(f"{'Section':42} {'Pages':>6} {'Budget':>7}  Status")
    print("-" * 68)

    over = False
    for index, (title, start) in enumerate(entries):
        next_start = entries[index + 1][1] if index + 1 < len(entries) else last_page + 1
        pages = max(next_start - start, 0)
        budget = budgets.get(title)
        if budget is None:
            print(f"{title[:42]:42} {pages:>6} {'-':>7}  -")
            continue
        status = "OK" if pages <= budget else "OVER"
        over = over or pages > budget
        print(f"{title[:42]:42} {pages:>6} {budget:>7}  {status}")

    content_pages = max(content_end - first_page + 1, 0)
    print("-" * 68)
    print(f"Written content: {content_pages} pages "
          f"(limit 33; annexes/indexes excluded)")

    if over and args.strict:
        print("\nOne or more sections are over budget.")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
