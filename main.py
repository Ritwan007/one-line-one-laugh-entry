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

import hashlib
import os
import sys

# --- Entry configuration -------------------------------------------------
LINE = "The AI wrote my wedding vows; my spouse cried, mostly because it cited sources."

MAX_CHARS = 200          # published brief limit
MAX_WORDS = 40           # sanity bound: a one-liner must stay punchy
# sha256 of the exact champion line, UTF-8, no trailing newline.
# Pins the sealed line so no accidental edit can change the entry.
EXPECTED_SHA256 = "1932b9f6b39e94dd0d2f061431d9f3b99d85c437feaea2954eeb43d30d8b6155"

OUTPUT_PATH = "/output/entry.txt"


# --- Verification gate ---------------------------------------------------
def check_line(line):
    """Return a list of gate violations (empty list means the line passes)."""
    violations = []
    if not isinstance(line, str):
        return ["entry line must be a string"]
    try:
        encoded = line.encode("utf-8")
    except UnicodeEncodeError:
        return ["entry line is not valid UTF-8"]
    if not line.strip():
        violations.append("entry line must not be only whitespace")
    if not 1 <= len(line) <= MAX_CHARS:
        violations.append(
            "entry line must be 1-%d characters, got %d" % (MAX_CHARS, len(line))
        )
    if "\n" in line or "\r" in line:
        violations.append("entry line must be a single line")
    words = line.split()
    if len(words) > MAX_WORDS:
        violations.append("entry line must be at most %d words, got %d" % (MAX_WORDS, len(words)))
    if hashlib.sha256(encoded).hexdigest() != EXPECTED_SHA256:
        violations.append("entry line does not match the sealed champion digest")
    return violations


def verify(line):
    """Throw before writing if the line violates any gate."""
    violations = check_line(line)
    if violations:
        raise ValueError("entry failed verification: " + "; ".join(violations))


# --- Entry point ---------------------------------------------------------
def main():
    verify(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
