"""make.fun news-image-20261119 entry (Python 3.13, standard library only).

Copies the bundled entry.png to /output/entry.png (or $MAKEFUN_OUTPUT_DIR).
No network, no randomness: both runs write the same bytes.
"""
import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "entry.png"
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out_dir / "entry.png")
