#coding:utf-8

from sklearn.model_selection import train_test_split
import numpy as np
import os
from PIL import Image
from unet import UNetCompiled
import tensorflow as tf
import json
import datetime

folder_path = "."
model_save_folder = "./models/checkpoint.ckpt"

X = []
Y = []

for file in os.listdir(folder_path+"/images"):
	X.append(np.array(Image.open(folder_path+"/images/"+file).convert('RGB')))

for file in os.listdir(folder_path+"/labels"):
	Y.append(np.load(folder_path+"/labels/"+file))

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

unet = UNetCompiled(input_size=(512,512,3), n_filters=32, n_classes=2)

unet.summary()

unet.compile(optimizer=tf.keras.optimizers.Adam(),loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),metrics=['accuracy'])

cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=model_save_folder,save_weights_only=True,verbose=1, save_freq='epoch')

log_dir = "./models/logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

results = unet.fit(np.array(X_train), np.array(Y_train), batch_size=1, epochs=40, validation_data=(np.array(X_test), np.array(Y_test)),callbacks=[cp_callback, tensorboard_callback])

with open('./models/train_history.json', 'w') as file_pi:
	json.dump(results.history, file_pi)