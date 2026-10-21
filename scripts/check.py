#!/usr/bin/env python3
"""Portable project integrity checks, NOT the platform's full acceptance gate."""
from pathlib import Path
import hashlib,json
from PIL import Image
from build import ROOT,STATES,build
im=Image.open(ROOT/'assets/atlas/dario-v2.png').convert('RGBA')
assert im.size==(1536,2288)
assert im.tobytes()==build().tobytes()
for row,(_,n) in enumerate(STATES):
 for i in range(8):
  box=im.crop((i*192,row*208,(i+1)*192,(row+1)*208)).getchannel('A').getbbox()
  assert bool(box)==(i<n),(row,i)
manifest=json.loads((ROOT/'manifest.json').read_text())
for item in manifest['files']:
 p=ROOT/item['path'];assert p.is_file(),p;assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'],p
print(f"PASS: frame assembly, occupied slots, and {len(manifest['files'])} file hashes")
