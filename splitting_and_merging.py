import numpy as np
import argparse
import cv2
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(B, G, R) = cv2.split(image)
plt.subplot(231)
plt.imshow(R)
plt.subplot(232)
plt.imshow(G)
plt.subplot(233)
plt.imshow(B)
plt.subplot(212)
merged = cv2.merge([B, G, R])
plt.imshow(merged)
plt.show()
