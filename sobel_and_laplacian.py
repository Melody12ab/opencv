import numpy as np
import argparse
import cv2
from matplotlib import pyplot as plt
import mahotas

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(image, cmap="gray")
lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
plt.figure()
plt.imshow(lap, cmap="gray")

sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

plt.figure()
plt.subplot(131)
plt.imshow(sobelX, cmap="gray")
plt.subplot(132)
plt.imshow(sobelY, cmap="gray")
plt.subplot(133)
plt.imshow(sobelCombined, cmap="gray")

plt.show()
