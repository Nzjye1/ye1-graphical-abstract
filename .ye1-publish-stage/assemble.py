import json,shutil
from pathlib import Path
base=Path('.'); manifest=json.loads((base/'.ye1-publish-stage/manifest.json').read_text())
for entry in manifest:
 p=base/entry['path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b''.join((base/i).read_bytes() for i in entry['parts']))
shutil.rmtree(base/'.ye1-publish-stage')
(base/'.github/workflows/ye1-publication.yml').unlink()
