#coding:utf-8

from matplotlib.widgets import Cursor, PolygonSelector, TextBox, Slider
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backend_bases import MouseButton
from matplotlib.patches import Polygon
from pynput.keyboard import Key, Controller
import time
import json
import tkinter.filedialog as fd
from tkinter import *
from PIL import Image
import cv2

root = Tk()
root.title("Choose the image you want to label")
filename = fd.askopenfilename(initialdir='./images',title="Choose the image you want to label")
root.destroy()
image = filename.split("/")[-1]
keyboard = Controller()
key = Key.esc


im = Image.open(filename)
im = im.resize((512,512))
im.save("./images/"+image)

features = {}
polygons = []

fig, ax = plt.subplots(figsize=(8, 6))
colors = ['red','blue','yellow', 'green', 'black', 'white', 'blueviolet','deeppink','brown']
axfreq = plt.axes([0.2, 0.05, 0.65, 0.03])
classNum = 1

root = Tk()
root.title("Choose the polygon layer you want to modify")
feature_filename = fd.askopenfilename(initialdir='.',title="Choose the polygon layer you want to modify")
root.destroy()
if feature_filename!="":
	with open(feature_filename) as f:
		features = json.load(f)
		polygons = features["polygons"]

n = len(polygons)

def switch(i):
	global classNum
	classNum = int(i)

slider = Slider(axfreq, "class n°", 1, len(colors), valstep = 1)
slider.on_changed(switch)

def addPoly(p):
	global classNum
	global polygons
	polygon = []
	for point in p:
		polygon.append((int(point[0]),int(point[1])))
	color = colors[classNum-1]
	ax.add_patch(Polygon(p, alpha=0.5, fill=True, color=color))
	polygon.append(classNum)
	polygons.append(polygon)
	keyboard.tap(key)
	plt.show()

polySelector = PolygonSelector(ax, addPoly, useblit=True)


img = mpimg.imread("./images/"+image)
size = img.shape
ax.imshow(img)

for poly in polygons:
	save = classNum
	classNum = poly[-1]
	color = colors[classNum-1]
	ax.add_patch(Polygon(poly[:-1], alpha=0.5, fill=True, color=color))
	classNum = save

plt.show()

features["input_size"] = size
features["polygons"] = polygons

if n < len(polygons):
	root = Tk()
	root.title("Choose the folder to save updated polygon layer")
	folder = fd.askdirectory(initialdir='.',title="Choose the folder to save updated polygon layer")
	root.destroy()
	with open(folder+"/polygons_"+image.split(".")[-2]+".json","w") as f:
		json.dump(features,f)
	print("polygon layer saved")

	root = Tk()
	folder_mask = fd.askdirectory(initialdir='.',title="Choose the folder to export the mask")
	root.destroy()
	size = features["input_size"]
	polygons = features["polygons"]
	tmp_mask = np.zeros((size[0],size[1]))
	nb_class = np.max([poly[-1] for poly in polygons]) + 1
	mask = np.zeros((size[0],size[1],nb_class))

	for poly in polygons:
		cv2.fillPoly(tmp_mask, np.array([poly[:-1]]),poly[-1])

	for i in range(size[0]):
		for j in range(size[1]):
			mask[i,j,int(tmp_mask[i,j])] = 1 

	np.save(folder_mask+'/mask_'+image.split(".")[-2], mask)
	print("mask saved for ",nb_class," classes")