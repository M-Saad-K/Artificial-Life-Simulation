import cv2
import numpy as np 

x = 1080
y = 1920
num_particles = 600

window = np.zeros((x, y, 3))

while True:
    cv2.imshow("window", window)
    cv2.waitKey(1)
