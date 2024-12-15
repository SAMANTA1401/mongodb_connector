import os
from pathlib import Path

package_name = 'mongodb_connect'

list_of_files = [
    ".github/workflows/ci.yaml",
    'src/__init__.py',
    f'src/{package_name}/__init__.py',
    f'src/{package_name}/connect.py',
    f'src/{package_name}/mongo_crud.py',
    'tests/__init__.py',
    'tests/integration/__init__.py',
    'tests/integration/int.py',
    'tests/unit/__init__.py',
    'tests/unit/unit.py',
    'tox.ini',
    'init_setup.sh',
    'requirements.txt',
    'requirements_dev.txt',
    'pytproject.toml',
    'LICENSE',
    'README.md',
    'setup.py',
    'setup.cfg',
    'experiments/experiments.ipynb'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        print(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            print(f"Creating empty file: {filepath}")

    else:
        print(f"{filename} already exists")
