#coding:utf-8

from PIL import Image
import os

images_to_resize_folder = "./original_images"

for file in os.listdir(images_to_resize_folder):
	im = Image.open(images_to_resize_folder+"/"+file)
	im = im.resize((512,512))
	im.save("./images/"+file)