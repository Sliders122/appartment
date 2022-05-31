import numpy as np
import matplotlib.pyplot as plt
import cv2

# create a numpy array with integer from 0 to 255 matching pixels
image_frame = (plt.imread("price_image.png") * 255).astype(int)
# plt.imshow(image_frame[40:60,0:20,0])
print(np.unique(image_frame[40:60, 0:20, 0]))  # It results with two values: 213 and 255. 213 should be grey
pos_gray = np.where(image_frame[:, 100, 0] == 213)
print(pos_gray)
pos_gray2 = np.where(image_frame[:, 300, 0] == 213)
print(pos_gray)
#result = np.where(image_frame[:, 5, ] == 213)


