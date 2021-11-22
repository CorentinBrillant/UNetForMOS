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

image = 'quart_image.png'
keyboard = Controller()
key = Key.esc

polygons = []

fig, ax = plt.subplots(figsize=(8, 6))
colors = ['red']#,'blue','yellow', 'green', 'black', 'white', 'blueviolet','deeppink','brown']
axfreq = plt.axes([0.2, 0.05, 0.65, 0.03])

classNum = 1

def switch(i):
	global classNum
	classNum = int(i)

slider = Slider(axfreq, "class n°", 1, len(colors), valstep = 1)
slider.on_changed(switch)

def addPoly(p):
	global classNum
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


plt.show()

features = {}

features["input_size"] = size
features["polygons"] = polygons
print(polygons)

with open("./features_layers/polygons_"+image.split(".")[-2]+".json","w") as f:
	json.dump(features,f)