import numpy as np
import json, copy, sys, os



if __name__ == "__main__":

  this_dir = os.path.dirname(__file__)
  this_dir = os.path.join(this_dir, 'data') 

  # The V-COCO annotations files:
  v_train = json.load(open('{:s}/vcoco_{:s}.json'.format(this_dir, 'trainval'), 'r'))
  v_test = json.load(open('{:s}/vcoco_{:s}.json'.format(this_dir, 'test'), 'r'))

  # Now, search for annotations in both v-coco jsons, corresponding to sit and stand. How many examples total? 
  # Test set:
  print(v_test[1]["action_name"])
  print(v_test[2]["action_name"])

  stand_list_test = np.array(v_test[1]["ann_id"][:])
  stand_label_test = np.array(v_test[1]["label"][:])
  stand_test = stand_list_test[stand_label_test==1]

  sit_list_test = np.array(v_test[2]["ann_id"][:])
  sit_label_test = np.array(v_test[2]["label"][:])
  sit_test = sit_list_test[sit_label_test==1]

  sit_img_list_test = np.array(v_test[2]["image_id"][:])
  sit_img_test = sit_img_list_test[sit_label_test==1]
  stand_img_list_test = np.array(v_test[1]["image_id"][:])
  stand_img_test = stand_img_list_test[stand_label_test==1]

  # Train set:
  print(v_train[1]["action_name"])
  print(v_train[2]["action_name"])

  stand_list_train = np.array(v_train[1]["ann_id"][:])
  stand_label_train = np.array(v_train[1]["label"][:])
  stand_train = stand_list_train[stand_label_train==1]

  sit_list_train = np.array(v_train[2]["ann_id"][:])
  sit_label_train = np.array(v_train[2]["label"][:])
  sit_train = sit_list_train[sit_label_train==1]

  sit_img_list_train = np.array(v_train[2]["image_id"][:])
  sit_img_train = sit_img_list_train[sit_label_train==1]
  stand_img_list_train = np.array(v_train[1]["image_id"][:])
  stand_img_train = stand_img_list_train[stand_label_train==1]

  # All together now:
  img_all = np.concatenate((sit_img_train, sit_img_test, stand_img_train, stand_img_test), axis=0)
  
  sit_all = np.concatenate((sit_train, sit_test), axis=0)
  stand_all = np.concatenate((stand_train, stand_test),axis=0)

  # The MS-COCO (merged insts and keypoints, reduced) annotations files:
  a_train = json.load(open('{:s}/anns_{:s}.json'.format(this_dir, 'train'), 'r'))
  a_test = json.load(open('{:s}/anns_{:s}.json'.format(this_dir, 'test'), 'r'))








  # select images that we need
  # annotations training set: 
  a_train_imlist = [j_i['id'] for j_i in a_train['images']]	# image id list
  a_train_imlist = np.array(a_train_imlist)[:,np.newaxis]
  in_vcoco = []
  for i in range(len(a_train_imlist)):
    if np.any(a_train_imlist[i] == img_all):
      in_vcoco.append(i)
  a_train_sit_images = [a_train['images'][ind] for ind in in_vcoco] 

  print(np.shape(in_vcoco))


  # annotations test set: 
  a_test_imlist = [j_i['id'] for j_i in a_test['images']]	# image id list
  a_test_imlist = np.array(a_test_imlist)[:,np.newaxis]
  in_vcoco = []
  for i in range(len(a_test_imlist)):
    if np.any(a_test_imlist[i] == img_all):
      in_vcoco.append(i)
  a_test_sit_images = [a_test['images'][ind] for ind in in_vcoco] 

  print(np.shape(in_vcoco))


  # select annotations that we need
  # sit: 
  # annotations training set: 
  a_anns_imlist = []
  a_anns_imlist = [j_i['id'] for j_i in a_train['annotations']] 	# image id list

  a_anns_imlist = np.array(a_anns_imlist)[:,np.newaxis]

  print(np.shape(a_anns_imlist))

  in_vcoco = []
  for i in range(len(a_anns_imlist)):
    if np.any(a_anns_imlist[i] == sit_all):
      in_vcoco.append(i)
      a_train['annotations'][i]['sitstand'] = 0

  print(np.shape(in_vcoco))

  # stand: 
  # annotations training set: 
  a_anns_imlist = []
  a_anns_imlist = [j_i['id'] for j_i in a_train['annotations']] 	# image id list
  a_anns_imlist = np.array(a_anns_imlist)[:,np.newaxis]
  for i in range(len(a_anns_imlist)):
    if np.any(a_anns_imlist[i] == stand_all):
      in_vcoco.append(i)
      a_train['annotations'][i]['sitstand'] = 1
  j_annotations_train = [a_train['annotations'][ind] for ind in in_vcoco] 

  print(np.shape(in_vcoco))






  # annotations test set: 
  # sit: 
  a_anns_imlist = []
  a_anns_imlist = [j_i['id'] for j_i in a_test['annotations']] 	# image id list
  a_anns_imlist = np.array(a_anns_imlist)[:,np.newaxis]

  print(np.shape(a_anns_imlist))

  in_vcoco = []
  for i in range(len(a_anns_imlist)):
    if np.any(a_anns_imlist[i] == sit_all):
      in_vcoco.append(i)
      a_test['annotations'][i]['sitstand'] = 0

  print(np.shape(in_vcoco))

  # annotations test set: 
  # stand: 
  a_anns_imlist = []
  a_anns_imlist = [j_i['id'] for j_i in a_test['annotations']] 	# image id list
  a_anns_imlist = np.array(a_anns_imlist)[:,np.newaxis]

  for i in range(len(a_anns_imlist)):
    if np.any(a_anns_imlist[i] == stand_all):
      in_vcoco.append(i)
      a_test['annotations'][i]['sitstand'] = 1
  j_annotations_test = [a_test['annotations'][ind] for ind in in_vcoco] 

  print(np.shape(in_vcoco))

  # Now reduce annotations and images sets and write out 


  a_train['annotations'] = j_annotations_train
  a_train['images'] = a_train_sit_images

  a_test['annotations'] = j_annotations_test
  a_test['images'] = a_test_sit_images



















  # Save everything

  vcoco = os.path.join(this_dir, 'test_out_1.json')
  print("Writing COCO annotations needed for V-COCO (train) to %s."%(format(vcoco)))
  with open(vcoco, 'wt') as f:
    json.dump(a_test, f)

  vcoco = os.path.join(this_dir, 'train_out_1.json')
  print("Writing COCO annotations needed for V-COCO (test) to %s."%(format(vcoco)))
  with open(vcoco, 'wt') as f:
    json.dump(a_train, f)
