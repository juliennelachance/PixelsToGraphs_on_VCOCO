import numpy as np
import json, copy, sys, os
from jsonmerge import merge


if __name__ == "__main__":

  this_dir = os.path.dirname(__file__)
  this_dir = os.path.join(this_dir, 'anns') 

  # Second, select annotations needed for V-COCO
  json_trainval_ins = json.load(open('{:s}/instances_vcoco_all_{:s}.json'.format(this_dir, '2014'), 'r'))
  json_trainval_key = json.load(open('{:s}/person_keypoints_vcoco_all_{:s}.json'.format(this_dir, '2014'), 'r'))

  vcoco_imlist = np.loadtxt(os.path.join(this_dir, 'vcoco_all.ids'))[:,np.newaxis]




  # select images that we need
  coco_imlist = [j_i['id'] for j_i in json_trainval_ins['images']]
  coco_imlist = np.array(coco_imlist)[:,np.newaxis]
  in_vcoco = []
  for i in range(len(coco_imlist)):
    if np.any(coco_imlist[i] == vcoco_imlist):
      in_vcoco.append(i)
  j_images_ins = [json_trainval_ins['images'][ind] for ind in in_vcoco] 

  # select annotations that we need
  coco_imlist = [j_i['image_id'] for j_i in json_trainval_ins['annotations']] 
  coco_imlist = np.array(coco_imlist)[:,np.newaxis]
  in_vcoco = []
  for i in range(len(coco_imlist)):
    if np.any(coco_imlist[i] == vcoco_imlist):
      in_vcoco.append(i)
  j_annotations_ins = [json_trainval_ins['annotations'][ind] for ind in in_vcoco] 

  json_trainval_ins['annotations'] = j_annotations_ins
  json_trainval_ins['images'] = j_images_ins






  # select images that we need
  coco_imlist = [j_i['id'] for j_i in json_trainval_key['images']]
  coco_imlist = np.array(coco_imlist)[:,np.newaxis]
  in_vcoco = []
  for i in range(len(coco_imlist)):
    if np.any(coco_imlist[i] == vcoco_imlist):
      in_vcoco.append(i)
  j_images_key = [json_trainval_key['images'][ind] for ind in in_vcoco] 

  # select annotations that we need
  coco_imlist = [j_i['image_id'] for j_i in json_trainval_key['annotations']] 
  coco_imlist = np.array(coco_imlist)[:,np.newaxis]
  in_vcoco = []
  for i in range(len(coco_imlist)):
    if np.any(coco_imlist[i] == vcoco_imlist):
      in_vcoco.append(i)
  j_annotations_key = [json_trainval_key['annotations'][ind] for ind in in_vcoco] 

  json_trainval_key['annotations'] = j_annotations_key
  json_trainval_key['images'] = j_images_key







  # Now that we've reduced the annotations lists, let's merge keypoints in... 

  keypts_imlist = [j_i['id'] for j_i in json_trainval_key['annotations']]
  insts_imlist = [j_i['id'] for j_i in json_trainval_ins['annotations']]
  # Loop over 'annotations' structures in keypts to find image id's and keypoint lists


  for ind in range(len(keypts_imlist)):
    imidi = keypts_imlist[ind]
    keyps = json_trainval_key['annotations'][ind]['keypoints']
    num_keyps = json_trainval_key['annotations'][ind]['num_keypoints']

    # Now find corresponding image id in instances, and add data to json dicts. 
    for j in range(len(insts_imlist)):
      imidj = insts_imlist[j]
      if(imidi == imidj):
        json_trainval_ins['annotations'][j]['keypoints'] = keyps
        json_trainval_ins['annotations'][j]['num_keypoints'] = num_keyps

  # Add in the keypoint category data for people (category_id = 1):
  json_trainval_ins['categories'][0]['keypoints'] = json_trainval_key['categories'][0]['keypoints']
  json_trainval_ins['categories'][0]['skeleton'] = json_trainval_key['categories'][0]['skeleton']


  vcoco = os.path.join(this_dir, 'testout_test12.json')
  print("Writing COCO annotations needed for V-COCO to %s."%(format(vcoco)))
  with open(vcoco, 'wt') as f:
    json.dump(json_trainval_ins, f)




























