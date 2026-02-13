import json
import math
from pathlib import Path
from copy import deepcopy
import numpy as np

TEMPLATE = "python_utilities/template.json"
INPUT_DIR = Path("input/exec")
OUTPUT_BASE = Path("output")

INPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_BASE.mkdir(exist_ok=True)

targets = np.array([round(x * 0.1, 2) for x in range(-2, 3)])
A = 44
R = 1.2*A**(1/3)
pi = math.pi
prefactor = (4*pi)/(3*A*R**2)
print(targets)
print(targets/prefactor)

with open(TEMPLATE) as f:
    template = json.load(f)

for t in targets:
    data = deepcopy(template)

    run_name = f"t{t:+.2f}".replace(".", "p")
    out_dir = OUTPUT_BASE / run_name
    out_dir.mkdir(exist_ok=True)

    data["constraints"][0]["target"] = t/prefactor
    data["initialBeta2"] = t
    data["outputDirectory"] = str(out_dir)
    data["outputName"] = run_name

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

