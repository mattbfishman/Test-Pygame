from pygame import *
import sys, pygame
from SpriteStripAnim import SpriteStripAnim

class Player():
	def __init__(self, x ,y):
		# self.sprite = sprite
		self.x = x
		self.y = y

	def playerMove(self, player, n, right, left, up, down, defaultPlayer):
		keys = pygame.key.get_pressed()
		if keys[K_d]:
		    if n >= len(right):
		        n = 0
		    image = right[n].next()
		    player.x +=2
		    return image
		if keys[K_a]:
			if n >= len(left):
				n = 0
			image = left[n].next()
			player.x -=2
			return image
		if keys[K_w]:
			if(player.y > 15):
				if n >= len(up):
					n = 0
				image = up[n].next()
				player.y -=2
				return image
			else:
				if n >= len(up):
					n = 0
				image = up[n].next()
				player.y -=0
				return image
		if keys[K_s]:
			if n >= len(down):
				n = 0
			image = down[n].next()
			player.y +=2
			return image
		else:
			n = 0 
			return defaultPlayer

	def rightSprite(self):
		rightWalkSprite = [
		    SpriteStripAnim('sprites/rightwalk.png', ((0,0,64,64)), 9, 0, True, 10),
		    SpriteStripAnim('sprites/rightwalk.png', ((64,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/rightwalk.png', ((128,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/rightwalk.png', ((192,64,48,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/rightwalk.png', ((256,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/rightwalk.png', ((320,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/rightwalk.png', ((384,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/rightwalk.png', ((448,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/rightwalk.png', ((512,0,64,64)), 0, 0, True, 10)
		] 
		return rightWalkSprite

	def leftSprite(self):
		leftWalkSprite = [
		    SpriteStripAnim('sprites/leftwalk.png', ((0,0,64,64)), 9, 0, True, 10),
		    SpriteStripAnim('sprites/leftwalk.png', ((64,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/leftwalk.png', ((128,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/leftwalk.png', ((192,64,48,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/leftwalk.png', ((256,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/leftwalk.png', ((320,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/leftwalk.png', ((384,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/leftwalk.png', ((448,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/leftwalk.png', ((512,0,64,64)), 0, 0, True, 10)
		] 
		return leftWalkSprite

	def upSprite(self):
		upWalkSprite = [
		    SpriteStripAnim('sprites/upwalk.png', ((0,0,64,64)), 9, 0, True, 10),
		    SpriteStripAnim('sprites/upwalk.png', ((64,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/upwalk.png', ((128,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/upwalk.png', ((192,64,48,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/upwalk.png', ((256,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/upwalk.png', ((320,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/upwalk.png', ((384,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/upwalk.png', ((448,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/upwalk.png', ((512,0,64,64)), 0, 0, True, 10)
		] 
		return upWalkSprite

	def downSprite(self):
		downWalkSprite = [
		    SpriteStripAnim('sprites/downwalk.png', ((0,0,64,64)), 9, 0, True, 10),
		    SpriteStripAnim('sprites/downwalk.png', ((64,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/downwalk.png', ((128,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/downwalk.png', ((192,64,48,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/downwalk.png', ((256,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/downwalk.png', ((320,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/downwalk.png', ((384,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/downwalk.png', ((448,0,64,64)), 0, 0, True, 10),
		    SpriteStripAnim('sprites/downwalk.png', ((512,0,64,64)), 0, 0, True, 10)
		] 
		return downWalkSprite

