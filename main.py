import pygame
import numpy as np
from time import time


d = 900
r = d / 2
scr = pygame.display.set_mode((d, d))
pi = 0
total = 0
circle = 0
while True:
	s = time()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	pygame.display.update()
	for i in range(25):
		x, y = np.random.randint(0, d, 2)
		total += 1
		color = (255, 0, 0)
		if np.sqrt(np.square(np.abs(x - r)) + np.square(np.abs(y - r))) < 300:
			circle += 1
			color = (255, 255, 0)
		pygame.draw.circle(scr, color, (x, y), 2)
	pi = 4 * (circle / total)
	e = time() - s
	print(pi)