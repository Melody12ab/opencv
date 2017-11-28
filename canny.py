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
image = cv2.GaussianBlur(image, (5, 5), 0)
plt.imshow(image, cmap="gray")

plt.figure()
canny = cv2.Canny(image, 30, 150)
plt.imshow(canny, cmap="gray")
plt.show()
