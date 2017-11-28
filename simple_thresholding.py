import numpy as np
import argparse
import cv2
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(image, (5, 5), 0)
plt.imshow(blurred, cmap='gray')

(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
plt.figure()
plt.imshow(thresh, cmap='gray')

(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
plt.figure()
plt.imshow(threshInv, cmap='gray')
anded = cv2.bitwise_and(image, image, mask=threshInv)
plt.figure()
plt.imshow(anded, cmap='gray')

plt.show()
