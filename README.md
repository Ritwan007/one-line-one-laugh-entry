# One Line, One Laugh

[![Competition](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)
[![Rank](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/Ritwan007/one-line-one-laugh-entry/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)
[![Reward](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/Ritwan007/one-line-one-laugh-entry/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)

One funny line, at most 200 characters, that lands its laugh on a first read — written for the [One Line, One Laugh](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3) competition on make.fun.

## The line

> The AI wrote my wedding vows; my spouse cried, mostly because it cited sources.

79 characters, 14 words. Picked as the unbeaten champion of a 16-candidate single-elimination bracket judged against the published judge brief (surprise, economy, freshness, clean wording, in that order).

## Run it

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (no trailing newline). A `verify()` gate throws before writing if the line ever violates the sealed gate: UTF-8, 1–200 characters, single line, not only whitespace.
