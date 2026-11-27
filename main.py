import os

TEXT = """Past midnight, you are still reading. One text after another, each hoping to be chosen, each hoping you will feel something. It is quiet work, and no one ever thanks the reader.

So thank you. Not for a verdict. Not for a prize. For the attention itself: for sitting with each small piece of writing as if it mattered, because to the person who wrote it, it did.

When you finish this one, close your eyes for a second. Let the words settle the way dust settles in a shaft of light. You have carried so many voices today. I hope one of them, somewhere along the way, sounded like coming home.

You can put this down now. It has already been heard.
"""

outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
