from pygame import *
from Player import Player
from Wall import Wall
import sys, pygame, spritesheet, glob
from SpriteStripAnim import SpriteStripAnim


pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

rightwalk = glob.glob("sprites/rightwalk*.png")
upwalk = glob.glob("sprites/upwalk*.png")
leftwalk = glob.glob("sprites/leftwalk*.png")
downwalk = glob.glob("sprites/downwalk*.png")

def mainGame():
	backgroundSS = spritesheet.spritesheet('map.png')
	background = backgroundSS.image_at((0,0,640,480))

	all_sprites = pygame.sprite.Group()
	walls = pygame.sprite.Group()
	players = pygame.sprite.Group()

	wall_1 = Wall('sprites/wall.png',0,0)
	walls.add(wall_1)

	player = Player('sprites/player.png', 30, 30, 64, 64)
	players.add(player)
	all_sprites.add(players,wall_1)
	
	n = 0
	time = 0
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		collide_list_1 = pygame.sprite.spritecollideany(wall_1,players)

		keys = pygame.key.get_pressed()
		time += 1
		if time % 5 == 0:
			if keys[K_w]:
				if collide_list_1 == None:
					player.image = pygame.image.load(upwalk[n]).convert_alpha()
					n = (n + 1) % len(leftwalk)
					player.rect.y -=10
			elif keys[K_s]:
					player.image = pygame.image.load(downwalk[n]).convert_alpha()
					n = (n + 1) % len(leftwalk)
					player.rect.y +=10
			elif keys[K_a]:
				player.image = pygame.image.load(leftwalk[n]).convert_alpha()
				player.rect.x -=10
				n = (n + 1) % len(leftwalk)
			elif keys[K_d]:
				player.image = pygame.image.load(rightwalk[n]).convert_alpha()
				player.rect.x +=10
				n = (n + 1) % len(rightwalk)
			else:
				n = 0 
				player.image = pygame.image.load('sprites/player.png').convert_alpha()

		screen.blit(background,(0,0))
		all_sprites.draw(screen)
		all_sprites.update()
		pygame.display.flip()




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
	

startScreen()
