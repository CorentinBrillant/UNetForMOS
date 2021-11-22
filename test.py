#coding:utf-8

import numpy as np
import os
import cv2
from PIL import Image, ImageColor
from unet import UNetCompiled
import tensorflow as tf
import matplotlib.pyplot as plt

checkpoint_path = "./models/checkpoint_2.ckpt"
unet = UNetCompiled(input_size=(512,512,3), n_filters=32, n_classes=3)
unet.compile(optimizer=tf.keras.optimizers.Adam(),loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),metrics=['accuracy'])
unet.load_weights(checkpoint_path)
image_test = "./images/map3.png"

def VisualizeResults(filename):
	im = np.array(Image.open(filename).convert('RGB'))
	size = im.shape
	im = im[np.newaxis,...]
	colors = ['black','red','blue']#,'yellow', 'green', 'black', 'white', 'blueviolet','deeppink','brown']
	result = unet.predict(im)
	mask = np.zeros(size)
	for i in range(size[0]):
		for j in range(size[1]):
			
			color = ImageColor.getrgb(colors[int(np.argmax(result[0,i,j]))])
			for k in range(3):
				mask[i,j,k] = color[k]
			
			#mask[i,j] = int(np.argmax(result[0,i,j]))*100
	"""
	kernel = np.ones((2,2),np.uint8)
	mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	"""
	res_im = Image.fromarray(mask.astype(np.uint8))
	plt.imshow(res_im)
	plt.show()

VisualizeResults(image_test)