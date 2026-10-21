#!/usr/bin/env python3
"""Reassemble approved RGBA frame assets; never redraw character art."""
from pathlib import Path
import argparse,hashlib,json
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
STATES=[('idle',6),('running-right',8),('running-left',8),('waving',4),('jumping',5),('failed',8),('waiting',6),('running',6),('review',6)]
def build():
 atlas=Image.new('RGBA',(1536,2288))
 for row,(state,count) in enumerate(STATES):
  for frame in range(count):
   im=Image.open(ROOT/f'assets/frames/{state}/{frame:02}.png').convert('RGBA')
   assert im.size==(192,208)
   atlas.paste(im,(frame*192,row*208))
 for i in range(16):
  im=Image.open(ROOT/f'assets/gaze/{i:02}.png').convert('RGBA');assert im.size==(192,208)
  atlas.paste(im,((i%8)*192,(9+i//8)*208))
 return atlas
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=ROOT/'build/dario-v2.png');a=p.parse_args();a.output.parent.mkdir(parents=True,exist_ok=True);im=build();im.save(a.output)
 original=Image.open(ROOT/'assets/atlas/dario-v2.png').convert('RGBA');same=im.tobytes()==original.tobytes();print(json.dumps({'pixel_identical_to_release':same,'sha256':hashlib.sha256(a.output.read_bytes()).hexdigest()}));assert same
