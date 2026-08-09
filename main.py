import cv2
import numpy as np
import math
import random

x = 1080
y = 1920
num_particles = 600

window = np.zeros((x, y, 3))
cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Random particle ex-y position generated 
# # Making an array, with each element a particle's position
particle_pos_x = [random.randint(5, x-5) for _ in range(num_particles)] # This is within boundaries of the screen#
particle_pos_y = [random.randint(5, y-5) for _ in range(num_particles)]


while True:
    # Loop through every particle and draw it as a circle on the screen
    for idx in range(num_particles):
        cv2.circle(window, (int(particle_pos_y[idx]), int(particle_pos_x[idx])), 3, (255, 0, 0), -1)

    img = cv2.resize(window, (1920, 1080), interpolation=cv2.INTER_AREA)  
    
    cv2.imshow("window", window)
    cv2.waitKey(1)
