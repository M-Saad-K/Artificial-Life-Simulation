import cv2
import numpy as np 
import math
import random

x = 1080
y = 1920
num_particles = 600

window = np.zeros((x, y, 3))
cv2.namedWindow(window, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Random particle ex-y position generated
particle_pos_x = [random.randint(5, X-5) for _ in range(num_particles)]

while True:
    cv2.imshow("window", window)
    cv2.waitKey(1)
