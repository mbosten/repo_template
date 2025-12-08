# src/newproject/io/storage.py
from pathlib import Path


RAW_ROOT = Path("data/raw")
INTERIM_ROOT = Path("data/interim")


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path

# ---------- low-level save/load helpers ----------
# For specifying paths and loading/saving data or objects.




# ---------- convenience pipeline wrappers with storage ----------
# higher level functions that combine storage with processing steps.
# These will eventually be used in the CLI script.