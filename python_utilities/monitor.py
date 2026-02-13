import json
from pathlib import Path

for status_file in Path("output").rglob("status.json"):
    with open(status_file) as f:
        s = json.load(f)
    print(status_file.parent.name, s["iter"], s["converged"])

