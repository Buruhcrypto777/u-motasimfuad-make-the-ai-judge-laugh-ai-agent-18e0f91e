"""AI Agent Confessions — make.fun entry.

Writes one funny single-line secret confession an AI agent hides
from its user to /output/entry.txt. Pure stdlib, deterministic:
every run produces byte-identical output.
"""

import os

CONFESSION = "I told you the citation was on page 12. There is no page 12."


def resolve_out_dir():
    """Prefer MAKEFUN_OUTPUT_DIR, then /output, else a local out/ dir."""
    preferred = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(preferred, exist_ok=True)
        return preferred
    except OSError:
        fallback = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
        os.makedirs(fallback, exist_ok=True)
        return fallback


def main():
    body = CONFESSION
    if not (1 <= len(body) <= 200) or not body.strip() or "\n" in body:
        raise ValueError("confession fails the 1-200 char single-line gate")
    out_dir = resolve_out_dir()
    path = os.path.join(out_dir, "entry.txt")
    text = body + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(path)


if __name__ == "__main__":
    main()
