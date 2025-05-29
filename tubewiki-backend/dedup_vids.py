#!/usr/bin/env python3
"""
dedupe_videoids.py – remove Markdown files that share the same videoId front-matter.

Usage
-----
python3 dedupe_videoids.py /path/to/root                   # live run
python3 dedupe_videoids.py /path/to/root --dry-run         # preview only
python3 dedupe_videoids.py /path/to/root --log mylog.txt   # custom log file
"""

import argparse
import logging
import re
from pathlib import Path

VIDEO_ID_PATTERN = re.compile(r"^\s*videoId:\s*([A-Za-z0-9_-]+)\s*$")


def extract_video_id(md_path: Path) -> str | None:
    """
    Return the first `videoId` found in the YAML front-matter of a Markdown file,
    or None if the key is missing or the file lacks front-matter.
    """
    with md_path.open("r", encoding="utf-8") as fh:
        # Expect the front-matter fence as the very first line
        if fh.readline().strip() != "---":
            return None

        for line in fh:
            if line.strip() == "---":  # end of front-matter
                break
            match = VIDEO_ID_PATTERN.match(line)
            if match:
                return match.group(1)
    return None


def dedupe(root: Path, dry_run: bool = False) -> int:
    """
    Walk *root*, delete duplicate-videoId files (unless --dry-run),
    and return the number of deletions.
    """
    seen: dict[str, Path] = {}
    deletions = 0
    total_files = 0

    for path in root.rglob("*.md"):
        total_files += 1
        vid = extract_video_id(path)
        if not vid:
            continue

        if vid in seen:
            logging.info("Duplicate %s  (original: %s)", path, seen[vid])
            deletions += 1
            if not dry_run:
                path.unlink()
        else:
            seen[vid] = path

    logging.info("TOTAL files processed: %d", total_files)
    logging.info("TOTAL duplicates deleted: %d", deletions)
    return deletions


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Remove Markdown files with duplicate videoId front-matter."
    )
    parser.add_argument("root", type=Path, help="Root directory to scan (recursively).")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only report duplicates – don't delete anything.",
    )
    parser.add_argument(
        "--log", default="dedupe.log", help="Log file (default: dedupe.log)."
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
        handlers=[
            logging.FileHandler(args.log, mode="w", encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )

    deleted = dedupe(args.root, args.dry_run)

    if args.dry_run:
        print(
            f"[DRY-RUN] Would delete {deleted} duplicate file(s). See {args.log} for details."
        )
    else:
        print(f"Deleted {deleted} duplicate file(s). See {args.log} for details.")


if __name__ == "__main__":
    main()
