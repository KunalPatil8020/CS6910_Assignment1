# -*- coding: utf-8 -*-

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QU0CyAcaqzH4h1s_okUr4C_WY2p-YpDK
"""


#Imports
from keras.datasets import fashion_mnist
import numpy as np
import matplotlib.pyplot as plt

#Getting the data
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

#Normalizing the data.
train_images=train_images / 255.0
test_images = test_images / 255.0


class_dict = {0 : "T-shirt_top",
              1: "Trouser", 
              2: "Pullover", 
              3: "Dress", 
              4: "Coat", 
              5: "Sandal", 
              6: "Shirt", 
              7: "Sneaker", 
              8: "Bag", 
              9: "Ankle Boot"}

sample_image_class, sample_image_index = np.unique(train_labels, return_index=True)

#Using subplots to display the required grid.
fig = plt.figure(figsize=(10,5))
for i in range(0,len(sample_image_index)):
    plt.subplot(2,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[sample_image_index[i]], cmap=plt.cm.binary)
    plt.xlabel(class_dict[sample_image_class[i]], fontsize=8, fontweight='bold')
plt.show()
