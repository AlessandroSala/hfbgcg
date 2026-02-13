import json
import subprocess
from pathlib import Path
from copy import deepcopy

TEMPLATE = "template.json"
INPUT_DIR = Path("input/exec")
OUTPUT_BASE = Path("output")

INPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_BASE.mkdir(exist_ok=True)

targets = [round(x * 0.1, 2) for x in range(-5, 6)]

with open(TEMPLATE) as f:
    template = json.load(f)

for t in targets:
    data = deepcopy(template)

    # --- naming ---
    run_name = f"t{t:+.2f}".replace(".", "p")
    output_dir = OUTPUT_BASE / run_name
    output_dir.mkdir(exist_ok=True)

    # --- modify JSON ---
    data["constraints"][0]["target"] = t
    data["outputDirectory"] = str(output_dir)
    data["outputName"] = run_name

    # --- write input ---
    input_path = INPUT_DIR / f"{run_name}.json"
    with open(input_path, "w") as f:
        json.dump(data, f, indent=2)

    # --- submit ---
    subprocess.run([
        "sbatch",
        "--job-name", run_name,
        "run.slurm",
        str(input_path)
    ])

print("All jobs submitted.")

