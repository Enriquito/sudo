# from tensorflow.keras.models import load_model
import imutils

import cv2
import numpy as np
from keras.saving.save import load_model
from matplotlib import pyplot as plt

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
classes = np.arange(0, 10)
model = load_model('model-OCR.h5')
input_size = 48

# Read image
img = cv2.imread('sudoku1.jpg')
plt.imshow(img, interpolation='nearest')
plt.show()
