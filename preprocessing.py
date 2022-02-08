# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11zHxpPaLFV50qtNP5SnDwzGucn0LZWZj
"""

import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import fashion_mnist

if __name__ == "__main__":
    (trainIn, trainOut), (testIn, testOut) = fashion_mnist.load_data()

    # visualisation of the classes:
    img_classes_fig = plt.figure("The image classes")
    grid_specification = img_classes_fig.add_gridspec(2, 5)

    num_classes = int(np.max(trainOut) + 1)
    class_dictionary = {
        "0": "T-shirt/Top",
        "1": "Trouser",
        "2": "Pullover",
        "3": "Dress",
        "4": "Coat",
        "5": "Sandal",
        "6": "Shirt",
        "7": "Sneaker",
        "8": "Bag",
        "9": "Ankle Boot",
    }
    
    class_labels = [
        "T-shirt/Top",
        "Trouser",
        "Pullover",
        "Dress",
        "Coat",
        "Sandal",
        "Shirt",
        "Sneaker",
        "Bag",
        "Ankle Boot",
    ]
    ctr = 0

    Image_list = []
    Image_class_label = []
    for i in range(num_classes):
        for j in range(trainIn.shape[0]):
            if trainOut[j] == i and i < 5:
                globals()["ax" + str(i + 1)] = img_classes_fig.add_subplot(
                    grid_specification[0, i]
                )
                plt.imshow(trainIn[j], cmap="gray")
                Image_list.append(trainIn[j])
                plt.xlabel(class_dictionary[str(i)], fontsize=15)
                Image_class_label.append(class_dictionary[str(i)])
                break
            elif trainOut[j] == i and i >= 5:
                globals()["ax" + str(5 + i + 1)] = img_classes_fig.add_subplot(
                    grid_specification[1, i - 5]
                )
                plt.imshow(trainIn[j], cmap="gray")
                plt.xlabel(class_dictionary[str(i)], fontsize=15)
                Image_list.append(trainIn[j])
                Image_class_label.append(class_dictionary[str(i)])
                break

    plt.show()

