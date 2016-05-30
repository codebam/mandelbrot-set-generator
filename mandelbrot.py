#!/usr/bin/env python3

# Sean Behan
# Mandelbrot set generator

# This program uses python's built in complex number library
import time
import pygame
import sys
time1 = time.time()
pygame.init()

window_x = 800
window_y = 600
black = (0, 0, 0)
white = (255, 255, 255)
bailout = 2.0
max_i = 255
red = 10
green = 0
blue = 0

screen = pygame.display.set_mode((window_x, window_y))
screen.fill(white)

for j in range(int(window_y/2)+1):
    for i in range(window_x):
        c = complex(4*(i-window_x/2)/window_x, 3*(j-window_y/2)/window_y)
        # the complex() function is equivalent to AddZ()
        z = 0j
        n = 0
        while (abs(z) < bailout) and (n < max_i):
            z = z*z+c
            n += 1
        if n >= max_i:
            pygame.draw.lines(screen, black, False, [(i, j), (i, j)], 1)
            # top side draw black pixel
            pygame.draw.lines(screen, black, False, [(i,window_y-j), (i, window_y-j)], 1)
            # bottom side draw black pixel
        else:
            colour = ((red + 10 * n)%255, (green + 0 * n) % 255, (blue + 0 * n)%255)
            pygame.draw.lines(screen, colour, False, [(i, j), (i, j)], 1)
            # top side draw coloured pixel
            pygame.draw.lines(screen, colour, False, [(i,window_y-j), (i, window_y-j)], 1)
            # bottom side draw coloured pixel
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Exit if the user quits while the program is running
time2 = time.time()
total_time = time2 - time1
print("DONE!")
print("Total time:",total_time)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
# Check if the user quits after the program is finished running
