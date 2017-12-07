import numpy as np
import json, copy, sys, os
from jsonmerge import merge


if __name__ == "__main__":

  this_dir = os.path.dirname(__file__)
  this_dir = os.path.join(this_dir, 'anns') 

  # Second, selct annotations needed for V-COCO
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

  keypts_imlist = [j_i['image_id'] for j_i in json_trainval_key['annotations']]
  insts_imlist = [j_i['image_id'] for j_i in json_trainval_ins['annotations']]
  # Loop over 'annotations' structures in keypts to find image id's and keypoint lists

  print 'length of keypts list:'
  print len(keypts_imlist)
  print 'length of insts list:'
  print len(insts_imlist)








  keep_is = []
  keep_ims = []

  for ind in range(len(keypts_imlist)):
    #imidi = json_trainval_key['annotations'][ind]['image_id']
    imidi = keypts_imlist[ind]
    keyps = json_trainval_key['annotations'][ind]['keypoints']

    # Now find corresponding image id in instances, and add data to json dicts. 
    for j in range(len(insts_imlist)):
      #imidj = json_trainval_ins['annotations'][ind]['image_id']
      imidj = insts_imlist[j]
      if(imidi == imidj):
        json_trainval_ins['annotations'][j]['keypoints'] = keyps
        keep_is.append(j)
        keep_ims.append(json_trainval_ins['annotations'][j]['image_id'])

  j_annotations_ins = [json_trainval_ins['annotations'][ind] for ind in keep_is] 
  json_trainval_ins['annotations'] = j_annotations_ins






  # Now clean out the (image) ones which don't have keypoints:
  coco_imlist2 = [j_i['id'] for j_i in json_trainval_ins['images']]
  coco_imlist2 = np.array(coco_imlist2)[:,np.newaxis]
  in_keypt_list = []
  for i in range(len(coco_imlist2)):
    if np.any(coco_imlist2[i] == keep_ims):
      in_keypt_list.append(i)
  j_images_ins = [json_trainval_ins['images'][ind] for ind in in_keypt_list] 
  json_trainval_ins['images'] = j_images_ins


  vcoco = os.path.join(this_dir, 'testout_test5.json')
  print("Writing COCO annotations needed for V-COCO to %s."%(format(vcoco)))
  with open(vcoco, 'wt') as f:
    json.dump(json_trainval_ins, f)




























