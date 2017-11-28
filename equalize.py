import numpy as np
import argparse
import cv2
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
plt.subplot(121)
plt.imshow(image)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
eq = cv2.equalizeHist(image)
plt.subplot(122)
plt.imshow(np.hstack([image, eq]))

plt.show()
