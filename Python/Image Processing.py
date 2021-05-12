# Image Processing
# The main objective of this task is to apply filters for a given input image and find the variations in it.

import cv2
import numpy as np

# Reading the image from the folder or by specifying the path
img = cv2.imread('giraffes.jpg', 0)

scale_percent = 50  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized = cv2.resize(img, dim, cv2.INTER_LINEAR)
cv2.imshow("Original Image", resized)

# Identifying the pixel intensity by applying a threshold value. The pixels intensity can be viewed as dark or bright by
# threshold value. Greater the threshold value, brighter the image and lesser the threshold value, darker the image.
# 1. Simple Threshold

width1 = int(img.shape[1]*0.5)
height1 = int(img.shape[0]*0.5)
dim1 = (width1, height1)
Thresh_resized = cv2.resize(img, dim1, cv2.INTER_AREA)
ret, threshold = cv2.threshold(Thresh_resized, 127, 255, cv2.THRESH_BINARY)
Thresh_img = cv2.imshow("BinaryThresh_image", threshold)

# 2. Adaptive Threshold

adap_thresh = cv2.adaptiveThreshold(Thresh_resized, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
adp_img = cv2.imshow("AdaptiveThresh_image", adap_thresh)

# Filters are used in detecting the edges and removing the noise from the images.
# 2D Filter

image = cv2.imread("giraffes.jpg")
image_resized = cv2.resize(image, dim1, cv2.INTER_AREA)
kernel = np.ones(shape=(4, 4), dtype=np.float32)/10
filter_img = cv2.filter2D(image_resized, -1, kernel)
Filter_img = cv2.imshow("2D Filtered image", filter_img)

# Averaging

blur = cv2.blur(image_resized, (5, 5))
blur_img = cv2.imshow("Blur image", blur)

# Gaussian Blur
g_blur = cv2.GaussianBlur(image_resized, (5, 5), 0)
g_blur_img = cv2.imshow("Gaussian Blur image", g_blur)

# Median Blur
median_blur = cv2.medianBlur(image_resized, 5)
median_blur_img = cv2.imshow("Median Blur image", median_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
