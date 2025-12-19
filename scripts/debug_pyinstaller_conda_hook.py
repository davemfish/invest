import pathlib
import sys
import json

CONDA_ROOT = pathlib.Path(sys.prefix)
CONDA_META_DIR = CONDA_ROOT / "conda-meta"

print(f'checking contents of {CONDA_META_DIR}')
for path in CONDA_META_DIR.glob("*.json"):
    _json_path = pathlib.Path(path)
    data = json.loads(_json_path.read_text())
    try:
        _ = data['depends']
    except KeyError:
        print('!!!!!!!!!!!!!!!!!!!')
        print(f'KeyError {path}')
