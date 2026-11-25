# One Line, One Laugh — u-coral-404-one-line-one-laugh-22f2c9f3
#
# Writes a single funny line (at most 200 characters) to /output/entry.txt.
# The line is the whole entry: a judge model compares entries two at a time
# against the published brief (surprise first, then economy, freshness and
# clean wording), so the line must land its laugh on a first read.
#
# Champion line, picked by a 16-candidate single-elimination bracket judged
# against the published criteria in order:
#   "The AI wrote my wedding vows; my spouse cried, mostly because it cited sources."
# 79 characters, 14 words, single line, no trailing newline.

import os

LINE = "The AI wrote my wedding vows; my spouse cried, mostly because it cited sources."


def verify(line):
    """Throw before writing if the line violates the sealed gate."""
    if not isinstance(line, str):
        raise ValueError("entry line must be a string")
    line.encode("utf-8")  # raises UnicodeEncodeError on non-UTF-8-encodable text
    if not line.strip():
        raise ValueError("entry line must not be only whitespace")
    if len(line) < 1 or len(line) > 200:
        raise ValueError("entry line must be 1-200 characters, got %d" % len(line))
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")


verify(LINE)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
