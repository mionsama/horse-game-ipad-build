"""Check the local workflow's bounded publication and source pins, without running it."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
text = (ROOT/'.github/workflows/build-ipad-runtime.yml').read_text(encoding='utf-8')
source = '8b52c1810a0b77614238001ed86199978865afd1'
actions = json.loads((ROOT/'action-pins.json').read_text(encoding='utf-8'))
assert '\non:\n  workflow_dispatch:\n' in text
assert '\n  push:' not in text and '\n  pull_request:' not in text
assert 'contents: read' in text and 'contents: write' not in text
assert 'secrets.' not in text
checkouts = re.findall(r'^\s+- uses: actions/checkout@[0-9a-f]{40}[^\n]*\n(.*?)(?=\n\s+- |\n\S|\Z)', text, re.M|re.S)
assert len(checkouts) == 7, len(checkouts)
for block in checkouts:
    assert 'repository: willfaust/Madeira' in block
    assert 'ref: '+source in block
    assert 'persist-credentials: false' in block
for name, revision in re.findall(r'uses: (actions/[\w/-]+)@([^\s]+)', text):
    repository = '/'.join(name.split('/')[:2])
    assert revision == actions[repository]
assert 'component: [dock, windows, moltenvk, zink, mesa-d3d12, vulkan-pe, kosmickrisp]' in text
assert 'build/wine-i386/build.sh' in text
assert 'runs-on: xcode-27' in text
print('PASS: manual-only trigger, read-only token, seven pinned source checkouts, pinned actions, i386 and OpenGL build stages.')
print('This checks targeted workflow properties, not YAML syntax, build success, or runtime safety.')
