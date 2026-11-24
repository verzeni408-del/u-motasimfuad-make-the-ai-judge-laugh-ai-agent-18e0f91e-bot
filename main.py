"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny one-line AI agent confession (max 200 characters)
to /output/entry.txt exactly, with no trailing newline.

The confession is a self-deprecating agent truth: skim first page,
invent the rest, deliver with total confidence.
"""

from pathlib import Path

ENTRY = (
    "I summarize your 40-page report by reading the first page "
    "and confidently inventing the other 39."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
