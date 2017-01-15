from pygame import *
from Player import Player
import sys, pygame, spritesheet
from SpriteStripAnim import SpriteStripAnim

pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

def anTest():
	FPS = 120
	frames = FPS/12
	playerSS = spritesheet.spritesheet('sprites/rightwalk.png')
	player = playerSS.image_at((0,0,64,64))
	tempPlayer = Player(0,15)
	strips = [
	    SpriteStripAnim('sprites/rightwalk.png', ((0,0,64,64)), 9, 1, True, frames),
	    SpriteStripAnim('sprites/rightwalk.png', ((64,0,64,64)), 0, 1, True, frames),
	    SpriteStripAnim('sprites/rightwalk.png', ((128,0,64,64)), 0, 1, True, frames),
	    SpriteStripAnim('sprites/rightwalk.png', ((192,64,48,64)), 0, 1, True, frames),
	    SpriteStripAnim('sprites/rightwalk.png', ((256,0,64,64)), 0, 1, True, frames),
	    SpriteStripAnim('sprites/rightwalk.png', ((320,0,64,64)), 0, 1, True, frames),
	    SpriteStripAnim('sprites/rightwalk.png', ((384,0,64,64)), 0, 1, True, frames),
	    SpriteStripAnim('sprites/rightwalk.png', ((448,0,64,64)), 0, 1, True, frames),
	    SpriteStripAnim('sprites/rightwalk.png', ((512,0,64,64)), 0, 1, True, frames),
	] 
	n = 0
	strips[n].iter()
	image = strips[n].next()
	while True:
	    for e in pygame.event.get():
	        if e.type == KEYUP:
	            if e.key == K_ESCAPE:
	                sys.exit()
	        keys = pygame.key.get_pressed()
            if keys[K_d]:
                if n >= len(strips):
                    n = 0
                image = strips[n].next()
                tempPlayer.x +=2
            else: 
            	image = player
	    screen.blit(image, (tempPlayer.x,tempPlayer.y))
	    pygame.display.flip()
	    # clock.tick(FPS)


def mainGame():
	backgroundSS = spritesheet.spritesheet('map.png')
	background = backgroundSS.image_at((0,0,640,480))

	player = Player(0,15)
	playerRight = []
	playerSS = spritesheet.spritesheet('sprites/rightwalk.png')

	FPS = 120
	frames = FPS/12
	playerSS = spritesheet.spritesheet('sprites/rightwalk.png')
	defaultPlayer = playerSS.image_at((0,0,64,64), colorkey=(0,0,0))
	tempPlayer = Player(0,15)
	right = [
	    SpriteStripAnim('sprites/rightwalk.png', ((0,0,64,64)), 9, 0, True, frames),
	    SpriteStripAnim('sprites/rightwalk.png', ((64,0,64,64)), 0, 0, True, frames),
	    SpriteStripAnim('sprites/rightwalk.png', ((128,0,64,64)), 0, 0, True, frames),
	    SpriteStripAnim('sprites/rightwalk.png', ((192,64,48,64)), 0, 0, True, frames),
	    SpriteStripAnim('sprites/rightwalk.png', ((256,0,64,64)), 0, 0, True, frames),
	    SpriteStripAnim('sprites/rightwalk.png', ((320,0,64,64)), 0, 0, True, frames),
	    SpriteStripAnim('sprites/rightwalk.png', ((384,0,64,64)), 0, 0, True, frames),
	    SpriteStripAnim('sprites/rightwalk.png', ((448,0,64,64)), 0, 0, True, frames),
	    SpriteStripAnim('sprites/rightwalk.png', ((512,0,64,64)), 0, 0, True, frames),
	] 
	n = 0
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		playerImage = playerMove(player,n,right, defaultPlayer)
		screen.blit(background,(0,0))
		screen.blit(playerImage,(player.x, player.y))
		pygame.display.flip()

def playerMove(player, n, spritesheet, defaultPlayer):
	keys = pygame.key.get_pressed()
	if keys[K_d]:
	    if n >= len(spritesheet):
	        n = 0
	    image = spritesheet[n].next()
	    player.x +=2
	    return image
	else: 
		return defaultPlayer



def startScreen():
	start = False
	startScreenSS = spritesheet.spritesheet('start.png')
	startScreen = startScreenSS.image_at((0,0,640,480))
	
	while not start:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		screen.blit(startScreen,(0,0))
		black = (255,255,255)
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
			mainGame()

    

# def movePlayer(imageNumber):
# 	keys = pygame.key.get_pressed()
# 	if keys[K_LEFT] or keys[K_a]:
# 	    player.x-= 3
# 	    return 1
# 	if keys[K_RIGHT] or keys[K_d]:
# 	    player.x+= 3
# 	    return 3
# 	if keys[K_UP] or keys[K_w]: 
# 		if player.y <= 18: 
# 			player.y-=0
# 	   	else: player.y-=3
# 		return 0
# 	if keys[K_DOWN] or keys[K_s]:
# 	    player.y+= 3
# 	    return 2
# 	else: return imageNumber

# def pauseGame(pause):
# 	while pause:
# 		for event in pygame.event.get():
# 			if event.type == pygame.QUIT: sys.exit()
# 		menu.openMenu(screen)

# while not start:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT: sys.exit()

	# black=(0,0,0)
	# screen.fill(black)
	# screen.blit(startBackground,(0,0))

	# headingFont=pygame.font.SysFont("Britannic Bold", 64)
	# clickFont=pygame.font.SysFont("Britannic Bold", 28)
	# headingLabel=headingFont.render("Welcome", 1, (black))
	# clickLabel=clickFont.render("Press the spacebar to start", 1, (black))
	# screen.blit(headingLabel,(220,50))
	# screen.blit(clickLabel,(200,400))
	# pygame.display.flip()

	# keys = pygame.key.get_pressed()
	# if keys[K_SPACE]:
	# 	start = True


    # imageNumber = movePlayer(imageNumber)
    # keys = pygame.key.get_pressed()
    # if keys[K_i]:
    # 	pause = True
    # 	pauseGame(pause)
    # 	break
    
    # screen.blit(ss,(0,0))
    # area = pygame.Rect(int(imageNumber) * 64, 0, 64, 64)
    # pygame.draw.rect(screen, blue,(camX, player.y, 160, 120))


startScreen()
#anTest()

