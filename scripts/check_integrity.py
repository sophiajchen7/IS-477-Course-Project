import hashlib
from pathlib import Path
import json

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    files = ["data/raw/violations.csv", "data/raw/permits.csv"]

    checksums = {f: sha256(f) for f in files}

    Path("metadata").mkdir(exist_ok=True)
    with open("metadata/checksums.json", "w") as out:
        json.dump(checksums, out, indent=2)

    print("Checksums written to metadata/checksums.json")

if __name__ == "__main__":
    main()
