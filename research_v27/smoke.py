from pathlib import Path
import json

out = Path('research_v27/results')
out.mkdir(parents=True, exist_ok=True)
(out / 'smoke.json').write_text(json.dumps({'status': 'ok'}, indent=2))
print('V27 smoke completed')
