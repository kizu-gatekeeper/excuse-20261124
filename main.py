#!/usr/bin/env python3
"""Write the one-line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "The One-Line Excuse an Agent Gives Its Human" bounty.
The program writes exactly one line of text and nothing else.
"""

import os
from pathlib import Path

LINE = "I outsourced the deadline to a subagent. It said 'almost done' six hours ago and has been typing ever since."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
