import numpy as np
import json, copy, sys, os


if __name__ == "__main__":

  this_dir = os.path.dirname(__file__)
  this_dir = os.path.join(this_dir, 'data') 

  # The annotations file:
  json_in = json.load(open('{:s}/final_merge_{:s}.json'.format(this_dir, 'vcocoDec'), 'r'))

  # The data splits (lists of image indices):
  vcoco_train = np.loadtxt(os.path.join(this_dir, 'vcoco_train.ids'))[:,np.newaxis]
  vcoco_val = np.loadtxt(os.path.join(this_dir, 'vcoco_val.ids'))[:,np.newaxis]
  vcoco_test = np.loadtxt(os.path.join(this_dir, 'vcoco_test.ids'))[:,np.newaxis]


  json_train = json_in
  # select images that we need
  coco_imlist = [j_i['id'] for j_i in json_in['images']]	# image id list
  coco_imlist = np.array(coco_imlist)[:,np.newaxis]

  print len(coco_imlist)

  in_vcoco = []
  for i in range(len(coco_imlist)):
    if np.any(coco_imlist[i] == vcoco_train):
      in_vcoco.append(i)
  j_images = [json_in['images'][ind] for ind in in_vcoco] 

  print len(in_vcoco)

  # select annotations that we need
  coco_imlist = [j_i['image_id'] for j_i in json_in['annotations']] 	# image id list
  coco_imlist = np.array(coco_imlist)[:,np.newaxis]
  in_vcoco = []
  for i in range(len(coco_imlist)):
    if np.any(coco_imlist[i] == vcoco_train):
      in_vcoco.append(i)
  j_annotations = [json_in['annotations'][ind] for ind in in_vcoco] 

  json_train['annotations'] = j_annotations
  json_train['images'] = j_images












  json_in = json.load(open('{:s}/final_merge_{:s}.json'.format(this_dir, 'vcocoDec'), 'r'))

  json_val = json_in
  # select images that we need
  coco_imlist = [j_i['id'] for j_i in json_in['images']]	# image id list
  coco_imlist = np.array(coco_imlist)[:,np.newaxis]
  in_vcoco = []
  for i in range(len(coco_imlist)):
    if np.any(coco_imlist[i] == vcoco_val):
      in_vcoco.append(i)
  j_images = [json_in['images'][ind] for ind in in_vcoco] 
  print len(in_vcoco)

  # select annotations that we need
  coco_imlist = [j_i['image_id'] for j_i in json_in['annotations']] 	# image id list
  coco_imlist = np.array(coco_imlist)[:,np.newaxis]
  in_vcoco = []
  for i in range(len(coco_imlist)):
    if np.any(coco_imlist[i] == vcoco_val):
      in_vcoco.append(i)
  j_annotations = [json_in['annotations'][ind] for ind in in_vcoco] 

  json_val['annotations'] = j_annotations
  json_val['images'] = j_images




  json_in = json.load(open('{:s}/final_merge_{:s}.json'.format(this_dir, 'vcocoDec'), 'r'))
  json_test = json_in
  # select images that we need
  coco_imlist = [j_i['id'] for j_i in json_in['images']]	# image id list
  coco_imlist = np.array(coco_imlist)[:,np.newaxis]
  in_vcoco = []
  for i in range(len(coco_imlist)):
    if np.any(coco_imlist[i] == vcoco_test):
      in_vcoco.append(i)
  j_images = [json_in['images'][ind] for ind in in_vcoco] 
  print len(in_vcoco)

  # select annotations that we need
  coco_imlist = [j_i['image_id'] for j_i in json_in['annotations']] 	# image id list
  coco_imlist = np.array(coco_imlist)[:,np.newaxis]
  in_vcoco = []
  for i in range(len(coco_imlist)):
    if np.any(coco_imlist[i] == vcoco_test):
      in_vcoco.append(i)
  j_annotations = [json_in['annotations'][ind] for ind in in_vcoco] 

  json_test['annotations'] = j_annotations
  json_test['images'] = j_images









  vcoco = os.path.join(this_dir, 'vcoco_train1.json')
  print("Writing COCO annotations needed for V-COCO (train) to %s."%(format(vcoco)))
  with open(vcoco, 'wt') as f:
    json.dump(json_train, f)

  vcoco = os.path.join(this_dir, 'vcoco_val1.json')
  print("Writing COCO annotations needed for V-COCO (val) to %s."%(format(vcoco)))
  with open(vcoco, 'wt') as f:
    json.dump(json_val, f)

  vcoco = os.path.join(this_dir, 'vcoco_test1.json')
  print("Writing COCO annotations needed for V-COCO (test) to %s."%(format(vcoco)))
  with open(vcoco, 'wt') as f:
    json.dump(json_test, f)












