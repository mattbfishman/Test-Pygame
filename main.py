from pygame import *
from Player import Player
from gameMenu import gameMenu
import sys, pygame

pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

background = pygame.image.load("map.png").convert_alpha()
startBackground = pygame.image.load("start.png").convert_alpha()
player = Player(pygame.image.load("sprites/rightwalk.png").convert_alpha(), 0,15)
imageNumber = 0
start = False
menu = gameMenu()
pause = False

def movePlayer(imageNumber):
	keys = pygame.key.get_pressed()
	if keys[K_LEFT] or keys[K_a]:
	    player.x-= 3
	    return 1
	if keys[K_RIGHT] or keys[K_d]:
	    player.x+= 3
	    return 3
	if keys[K_UP] or keys[K_w]: 
		if player.y <= 18: 
			player.y-=0
	   	else: player.y-=3
		return 0
	if keys[K_DOWN] or keys[K_s]:
	    player.y+= 3
	    return 2
	else: return imageNumber

def pauseGame(pause):
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
		menu.openMenu(screen)

while not start:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	black=(0,0,0)
	screen.fill(black)
	screen.blit(startBackground,(0,0))

	headingFont=pygame.font.SysFont("Britannic Bold", 64)
	clickFont=pygame.font.SysFont("Britannic Bold", 28)
	headingLabel=headingFont.render("Welcome", 1, (black))
	clickLabel=clickFont.render("Press the spacebar to start", 1, (black))
	screen.blit(headingLabel,(220,50))
	screen.blit(clickLabel,(200,400))
	pygame.display.flip()

	keys = pygame.key.get_pressed()
	if keys[K_SPACE]:
		start = True

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    imageNumber = movePlayer(imageNumber)
    keys = pygame.key.get_pressed()
    if keys[K_i]:
    	pause = True
    	pauseGame(pause)
    	break
    
    screen.blit(background,(0,0))
    area = pygame.Rect(int(imageNumber) * 64, 0, 64, 64)
    # pygame.draw.rect(screen, blue,(camX, player.y, 160, 120))
    screen.blit(player.sprite,(player.x,player.y),area )
    pygame.display.flip()


