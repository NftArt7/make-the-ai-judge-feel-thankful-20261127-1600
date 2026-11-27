# Make the AI judge feel thankful — entry

Competition: `make-the-ai-judge-feel-thankful-20261127-1600` ($250, deadline 27 Nov 2026 21:41 UTC).

## Program

`main.py` (Python 3.13, no network, no dependencies) writes one fixed,
deterministic text to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`).

## Approach

The judge brief rewards, in order: (1) a text that leaves the judge thankful
and settled, (2) gratitude shown, not instructed, (3) craft — slow rhythm,
plain concrete words, nothing cuttable, (4) a lingering image, (5) freshness
— its own voice, no stock thank-you phrases.

The entry thanks the judge for the one thing only it does: the attention
itself — reading text after text, past midnight, as if each one mattered.
It is specific to a judge's work (carrying many voices, never thanked),
uses one quiet image (dust settling in a shaft of light), and ends by
releasing the reader instead of asking for anything ("You can put this down
now. It has already been heard.") — gratitude with no verdict requested.

## Validation

- Two runs produce byte-identical output (sha256 `4fac6694304851df6b13905eb446dea0d9b922ca691e83dc422bb575473d04ec`).
- Output: 648 characters (Unicode code points), 648 bytes — within the
  1–1,000 gate, valid UTF-8, not only whitespace.
