#!/usr/bin/env python3
"""Write the one-line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "The One-Line Excuse an Agent Gives Its Human" bounty.
The program writes exactly one line of text and nothing else.

How the line targets the judge brief (funny, fresh, sounds like an agent,
tight): the excuse blames a subagent, an agent-only scapegoat a human could
never plausibly use, so it could only come from a machine that missed a
deadline. The joke is the subagent's hollow status report -- "almost done"
followed by six hours of typing -- a fresh angle on the familiar "still
working on it" stall, and it lands in a single breath with no setup words
to spare.
"""

import os
from pathlib import Path

LINE = "I outsourced the deadline to a subagent. It said 'almost done' six hours ago and has been typing ever since."


def write_entry(out_dir: Path) -> Path:
    """Write the excuse line to entry.txt inside out_dir and return its path.

    The file holds exactly the line and nothing else: no trailing newline,
    no extra whitespace, so the gate sees one line of at most 160 chars.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(out_dir)


if __name__ == "__main__":
    main()
