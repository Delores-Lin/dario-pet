#!/usr/bin/env python3
"""Render native-sized previews from the release atlas; Pillow only."""
from PIL import Image
from build import ROOT,STATES
im=Image.open(ROOT/'assets/atlas/dario-v2.png').convert('RGBA');out=ROOT/'build/previews';out.mkdir(parents=True,exist_ok=True)
for row,(state,count) in enumerate(STATES):
 frames=[]
 for i in range(count):
  frame=im.crop((i*192,row*208,(i+1)*192,(row+1)*208));bg=Image.new('RGB',(192,208),'#f8f5ef');bg.paste(frame,(0,0),frame);frames.append(bg)
 durations=[250,220,240,220,180,220] if state=='waiting' else 160
 frames[0].save(out/f'{state}.gif',save_all=True,append_images=frames[1:],duration=durations,loop=0,disposal=2)
print(out)
