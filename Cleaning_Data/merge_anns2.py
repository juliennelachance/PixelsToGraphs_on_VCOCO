import numpy as np
import json, copy, sys, os
from jsonmerge import merge


if __name__ == "__main__":

  this_dir = os.path.dirname(__file__)
  this_dir = os.path.join(this_dir, 'anns') 

  # Load the combined json file. 
  final_merge = json.load(open('{:s}/testout_{:s}.json'.format(this_dir, 'test5'), 'r'))

  # Load the complete V-COCO list of annotations
  vcoco_imlist = np.loadtxt(os.path.join(this_dir, 'vcoco_all.ids'))[:,np.newaxis]

  # Pull out list of image id's from final_merge
  coco_imList = [j_i['id'] for j_i in final_merge['images']]
  coco_annList = [j_i['image_id'] for j_i in final_merge['annotations']] 

  # Check both annotations and images lists are identical
  print len(coco_imList)
  print len(coco_annList)



