import numpy as np
import argparse
import cv2
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

plt.subplot(221)
plt.imshow(image)

plt.subplot(222)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray)

plt.subplot(223)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
plt.imshow(hsv)

plt.subplot(224)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
plt.imshow(lab)

plt.show()
