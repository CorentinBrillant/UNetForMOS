#coding:utf-8

import json
import numpy as np
import cv2
import os

nb_class = 3

features_path = "./features_layers_2"

for file in os.listdir(features_path):
	with open(features_path+"/"+file) as f:
		features = json.load(f)

	size = features["input_size"]
	polygons = features["polygons"]
	tmp_mask = np.zeros((size[0],size[1]))
	mask = np.zeros((size[0],size[1],nb_class))

	for poly in polygons:
		cv2.fillPoly(tmp_mask, np.array([poly[:-1]]),poly[-1])

	for i in range(size[0]):
		for j in range(size[1]):
			mask[i,j,int(tmp_mask[i,j])] = 1 

	np.save('./labels_2/mask_'+"_".join(file.split(".")[-2].split("_")[1:]), mask)