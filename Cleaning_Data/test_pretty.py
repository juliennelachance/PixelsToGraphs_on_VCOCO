import numpy as np
import json, copy, sys, os


if __name__ == "__main__":

  this_dir = os.path.dirname(__file__)
  this_dir = os.path.join(this_dir, 'vcoco') 

  # The annotations file:
  parsed = json.load(open('{:s}/coco_{:s}.json'.format(this_dir, 'annotations'), 'r'))

  vcoco = os.path.join(this_dir, 'pretty_coco_annotations.json')
  print("Writing pretty file to %s."%(format(vcoco)))
  with open(vcoco, 'wt') as f:
    json.dump(parsed, f, indent=4, sort_keys=True)
