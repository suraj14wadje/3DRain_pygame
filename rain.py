import pygame
import random
import time
import sys

blue = (138,43,226)
baground = (230,230,250)


pygame.init()
window=pygame.display.set_mode((1200,700))
pygame.display.set_caption("3D Rain")

speed = 1
accelaration = 0.6
clock = pygame.time.Clock()
run = True


length=20
breadth=5

speed=1
accelaration=0.1
x=800
y=0
drop = []
population = 200


def createDrop():
	x=random.randrange(0,1200)
	y=random.randrange(100,700)
	y*=-1
	weight=random.randrange(1,3)
	return [x,y,weight,accelaration,speed]


for i in range(population):
	drop.append(createDrop())


while run:

	
	
	clock.tick(70)

	for i in range(len(drop)):
		pygame.draw.rect(window,blue,(drop[i][0],drop[i][1],breadth*drop[i][2],length*drop[i][2]))
		
		drop[i][1]+=(drop[i][4])
		drop[i][4]+=(drop[i][3]*drop[i][2])

		if(drop[i][1]>700):
			drop[i]=createDrop()
	pygame.display.flip()
	

	window.fill(baground)
	
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False


pygame.quit()