import numpy as np
import argparse
import cv2
from matplotlib import pyplot as plt
import mahotas
import pytesseract

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
plt.imshow(blurred, cmap="gray")

T = mahotas.otsu(blurred)
print("Otsu`s threshold:{}".format(T))

thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < T] = 0
thresh = cv2.bitwise_not(thresh)
plt.figure()
plt.imshow(thresh, cmap="gray")

T = mahotas.rc(blurred)
print("Riddler-Calvard:{}".format(T))

thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < T] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imwrite("binew.png",thresh)

plt.figure()
plt.imshow(thresh, cmap="gray")

plt.show()
