# Last Text at One Percent — make.fun entry (Python 3.13, standard library only).
# Writes one fixed final text message, in the voice of a phone dying at 1%
# battery, to /output/entry.txt, deterministically.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The line: a deathbed confession with a turn. The phone admits it has been
# faking 1% since lunch, just to see how long its owner would ignore it.
# Specific detail ("since lunch"), a surprise (the phone was lying), and a
# consistent voice: a needy, passive-aggressive phone with a stake in dying.
TEXT = "1%. I've been lying. I've been at 1% since lunch. I just wanted to see how long you'd ignore me."

# Gate self-check: the sealed scorer requires UTF-8 text of 1-200 chars,
# not only whitespace. Fail loudly here rather than ship an invalid entry.
assert 1 <= len(TEXT) <= 200, f"entry is {len(TEXT)} chars, must be 1-200"
assert TEXT.strip(), "entry must not be only whitespace"
TEXT.encode("utf-8")

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(TEXT, encoding="utf-8")
