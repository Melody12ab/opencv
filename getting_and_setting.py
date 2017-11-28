from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {} ".format(image.shape[2]))

# (b, g, r) = image[0, 0]
# print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
# image[0, 0] = (0, 0, 255)
# (b, g, r) = image[0, 0]
# print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
#
# cv2.imshow("Image", image)
# cv2.waitKey(0)

# start from h (400,400)->(500,500)
corner = image[400:500, 400:500]
cv2.imshow("Image", corner)
cv2.waitKey(0)
image[400:500, 400:500] = (0, 255, 0)
cv2.imshow("Updated", image)
cv2.waitKey(0)
