"""Write a blinded copy of the site for double-blind review.

Usage: python3 scripts/blind.py OUTPUT_DIR

Reads index.html, removes anything that names the author as the guide's
author, and writes index.html plus .nojekyll to OUTPUT_DIR. The page has no
local assets, so nothing else is copied (no CNAME, no README). Exits non-zero
if a blocklisted string survives the scrub.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# The author's own paper is cited in the third person, which double-blind
# review allows. It is masked before the blocklist check.
EXEMPT = ['Luo, Lan E., and Olivier Toubia (2026)']

# Case-insensitive. Bare "Lan Luo" is not listed: the page cites
# Zhang and Luo (2023), whose second author is a different Lan Luo.
BLOCKLIST = [
    "laneluo",
    "ericluo04",
    "ll773",
    "Lan E. Luo",
    "Lan Eric Luo",
    "Eric Luo",
    "Lane Luo",
    "Luo, Lan E.",
]

# Links to the author's own site or GitHub account become plain text.
OWN_LINK = re.compile(
    r'<a\b[^>]*href="[^"]*(?:laneluo\.com|github\.com/ericluo04)[^"]*"[^>]*>(.*?)</a>',
    re.IGNORECASE | re.DOTALL,
)
# Any remaining bare URL to those hosts is dropped.
OWN_URL = re.compile(r'https?://(?:www\.)?(?:laneluo\.com|github\.com/ericluo04)\S*', re.IGNORECASE)


def scrub(html: str) -> str:
    html = OWN_LINK.sub(r"\1", html)
    html = OWN_URL.sub("", html)
    return html


def leaks(html: str) -> list[str]:
    masked = html
    for keep in EXEMPT:
        masked = masked.replace(keep, "")
    low = masked.lower()
    return [s for s in BLOCKLIST if s.lower() in low]


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    html = scrub((ROOT / "index.html").read_text(encoding="utf-8"))
    found = leaks(html)
    if found:
        print("blind.py: blocklisted strings remain: " + ", ".join(found), file=sys.stderr)
        return 1
    (out / "index.html").write_text(html, encoding="utf-8")
    (out / ".nojekyll").write_text("", encoding="utf-8")
    print(f"blind.py: wrote {out / 'index.html'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
