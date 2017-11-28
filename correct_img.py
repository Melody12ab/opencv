import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"], 0)
cv2.imshow("Orignal", image)
cv2.waitKey(0)

ret, thresh = cv2.threshold(image, 127, 255, 0)
(_, contours, hierarchy) = cv2.findContours(thresh.copy(), 1, 2)

