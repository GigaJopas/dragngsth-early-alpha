import pygame
from random import * 

pygame.init()

scrn_hght = 1000
scrn_wdth = 1000

screen = pygame.display.set_mode((scrn_wdth, scrn_hght))

snoww = (230, 230, 230)
blackish = (30, 30, 30)
greenish = (90, 90, 90)
green = (70, 180, 70)
red = (180, 70, 70)

inside = pygame.Rect(30, 30, 940, 940)

clone_btn = pygame.Rect(35, 6, 20, 20)
runaway_btn = pygame.Rect(60, 6, 20, 20)
follow_btn = pygame.Rect(85, 6, 20, 20)
random_btn = pygame.Rect(110, 6, 20, 20)
rotate_btn = pygame.Rect(240, 6, 20, 20)
slidin_btn = pygame.Rect(314, 6, 20, 20)

switchole = pygame.Rect(265, 6, 44, 20)
switcher1 = pygame.Rect(265, 6, 22, 20)
switcher2 = pygame.Rect(287, 6, 22, 20)

clean1 = 19
clean2 = 23
clean_btn = pygame.Surface((clean1, clean2), pygame.SRCALPHA)
clean_btn.fill((0, 0, 0, 0))

sliderhole = pygame.Rect(135, 10, 100, 12)
sliderer = pygame.Rect(135, 8, 25, 16) 
slider_min = 135
slider_max = 210

SCORE = 0

score_display = pygame.Rect(972, 971, 25, 25)
font1 = pygame.font.SysFont(None, 40)
score_text = font1.render(str(SCORE), True, (255, 255, 255))

cloning = False
runaway = False
followin = True
slidin = False

randomin = False

rotating = False

guyval = True

holdval = False

class Background(pygame.sprite.Sprite):
	def __init__(self, image, x, y):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(image).convert_alpha()

		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)

things = pygame.sprite.Group()
tzone = Background("tzone1.png", 100, 750)
things.add(tzone)

guy_num = 1
cleanin = False

randval = 4

rotate = pygame.USEREVENT + 0
pygame.time.set_timer(rotate, 9)
def rotatef():
	pass
angle = 0

movement = pygame.USEREVENT + 1
slide_speed = 35

pygame.time.set_timer(movement, slide_speed)

mouse_move = pygame.mouse.get_rel()
mouse_x_move = mouse_move[0]
mouse_y_move = mouse_move[1]

class Guys(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)

		if guyval == True:
			self.states = [
				pygame.image.load("guy1.png").convert_alpha(),
				pygame.image.load("guy1f.png").convert_alpha()
			]
			self.steps = [
				pygame.image.load("guy1m1.png").convert_alpha(),
				pygame.image.load("guy1m2.png").convert_alpha()
			]
		else:
			self.states = [
				pygame.image.load("guy2.png").convert_alpha(),
				pygame.image.load("guy2f.png").convert_alpha()
			]
			self.steps = [
				pygame.image.load("guy2m1.png").convert_alpha(),
				pygame.image.load("guy2m2.png").convert_alpha()
			]

		self.state_index = 0
		self.image = pygame.transform.rotate(self.states[self.state_index], angle)

		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)

		self.hold = False
		self.step_index = 0
		self.step_value = 0

	def update(self):

		if guyval == True:
			self.states = [
				pygame.image.load("guy1.png").convert_alpha(),
				pygame.image.load("guy1f.png").convert_alpha()
			]
			self.steps = [
				pygame.image.load("guy1m1.png").convert_alpha(),
				pygame.image.load("guy1m2.png").convert_alpha()
			]
		else:
			self.states = [
				pygame.image.load("guy2.png").convert_alpha(),
				pygame.image.load("guy2f.png").convert_alpha()
			]
			self.steps = [
				pygame.image.load("guy2m1.png").convert_alpha(),
				pygame.image.load("guy2m2.png").convert_alpha()
			]

		global SCORE

		global cleanin
		global tzone
		global guy_num

		self.moving = False

		if mouse_helders[0]:
			try:
				if self.rect.collidepoint(event.pos):
					self.hold = True
				else:
					self.hold = False
			except AttributeError:
				pass

		else:
			self.hold = False

		if self.hold == False:
			if runaway == True:
				if mouse_x in range(self.rect.x + 12, self.rect.x + 125) and mouse_y in range(self.rect.y + 11, self.rect.y + 120):
					self.rect.y += randval
					self.moving = True
				if self.rect.x + 68 < mouse_x + 57:
					self.rect.x -= randval
					self.moving = True
				if self.rect.x + 68 > mouse_x - 57:
					self.rect.x += randval
					self.moving = True
				if self.rect.y + 68 < mouse_y + 57:
					self.rect.y -= randval
					self.moving = True
				if self.rect.y + 68 > mouse_y - 57:
					self.rect.y += randval
					self.moving = True
			elif followin == True:
				if self.rect.x + 145 < mouse_x:
					self.rect.x += randval
					self.moving = True
				if self.rect.x - 43 > mouse_x:
					self.rect.x -= randval
					self.moving = True
				if self.rect.y - 51 < mouse_y:
					self.rect.y += randval
					self.moving = True
				if self.rect.y + 102 > mouse_y:
					self.rect.y -= randval
					self.moving = True
			if randomin == True:
				def right():
					self.rect.x += randval
				def left():
					self.rect.x -= randval
				def down():
					self.rect.y += randval
				def up():
					self.rect.y -= randval
				self.moving = True
				moves = [right, left, down, up]
				move = choice(moves)
				move()

			if slidin == True:
				self.rect.x = eval(f"{self.rect.x} + {mouse_x_move}")
				self.rect.y = eval(f"{self.rect.y} + {mouse_y_move}")
				if mouse_x_move != 0 or mouse_y_move != 0:
					self.moving = True
				else:
					self.moving = False

			if self.moving:
				self.step_value += 1
				if self.step_value >= 10:
					self.step_index = (self.step_index + 1) %len(self.steps)
					self.step_value = 0
					self.image = pygame.transform.rotate(self.steps[self.step_index], angle)
				self.image = pygame.transform.rotate(self.steps[self.step_index], angle)
			else:
				self.image = pygame.transform.rotate(self.states[0], angle)
		else:
			self.image = pygame.transform.rotate(self.states[1], angle)
			try:
				if self.rect.topleft != event.pos:
					if self.rect.left > inside.left - 1 and self.rect.right < inside.right + 1:
						self.rect.x = event.pos[0] - 40
					if self.rect.top > inside.top - 1 and self.rect.bottom < inside.bottom + 1:
						self.rect.y = event.pos[1] - 40
			except AttributeError:
				pass
		if self.rect.top < inside.top:
			self.rect.y = inside.y + 1
		if self.rect.bottom > inside.bottom:
			self.rect.y = inside.y + inside.height - self.rect.height - 1
		if self.rect.left < inside.left:
			self.rect.x = inside.x + 1
		if self.rect.right > inside.right:
			self.rect.x = inside.y + inside.width - self.rect.width - 1

		if self.rect.colliderect(tzone.rect):

			SCORE += 1
			print(SCORE)

			x1 = randint(31, 870)
			y1 = randint(31, 870)

			tzone.kill()
			tzone = Background("tzone1.png", x1, y1)
			things.add(tzone)

			if cloning == True:
				if guy_num < 100:
					guy_num += 1
					guysers = {
					"varname" : f"guy{guy_num}",
					"image1" : "guy1.png",
					"image2" : "guy1f.png",
					"walk1" : "guy1m1.png",
					"walk2" : "guy1m2.png",
					"x" : 400,
					"y" : 400
					}
					print(guy_num)
					print(guysers['varname'])

					guysers["varname"] = Guys(400, 400)
					guy_group.add(guysers["varname"])

guy_group = pygame.sprite.Group()
areas = pygame.sprite.Group()

guy1 = Guys(475, 400)

guy_group.add(guy1)

area1 = Background("bg1.png", 30, 30)

areas.add(area1)

pygame.draw.circle(clean_btn, (215, 215, 215), (clean1 // 2, clean2 // 2), 9)

clock = pygame.time.Clock()
runnin = True

while runnin:
	screen.fill(blackish)

	mouse_x, mouse_y = pygame.mouse.get_pos() 

	mouse_helders = pygame.mouse.get_pressed()

	if SCORE < 100:
		score_text = font1.render(str(SCORE), True, (255, 255, 255))
	elif SCORE >= 100:
		score_text = font1.render(str(SCORE), True, (255, 255, 0))

	if rotating == True:
		def rotatef():
			global angle
			angle += 1.25
			if angle > 360:
				angle = 0
	else:
		def rotatef():
			global angle
			angle = 0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			runnin = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if clone_btn.collidepoint(event.pos):
					if cloning == True:
						cloning = False
					else:
						cloning = True
				if runaway_btn.collidepoint(event.pos):

					if runaway == True:
						runaway = False
					else:
						followin = False
						runaway = True

				if follow_btn.collidepoint(event.pos):
					if followin == True:
						followin = False
					else:
						runaway = False

						followin = True
				if random_btn.collidepoint(event.pos):
					if randomin == True:
						randomin = False
					else:
						randomin = True

				if clean_btn.get_rect().collidepoint(event.pos):
					guy_group.empty()
					guy_num = 1

					guy1 = Guys(449, 443)
					guy_group.add(guy1)

				if rotate_btn.collidepoint(event.pos):
					if rotating == True:
						rotating = False
					else:
						rotating = True

				if switcher1.collidepoint(event.pos):
					if guyval == True:
						guyval = False
				if switcher2.collidepoint(event.pos):
					if guyval == False:
						guyval = True

				if slidin_btn.collidepoint(event.pos):
					if slidin == True:
						slidin = False
					else:
						slidin = True

		if event.type == rotate:
			rotatef()

		if event.type == movement:
			mouse_move = pygame.mouse.get_rel()
			mouse_x_move = mouse_move[0]
			mouse_y_move = mouse_move[1]

	if mouse_helders[0]:
		try:
			if sliderer.collidepoint(event.pos):
				if sliderer.x in range(slider_min, slider_max):
					sliderer.x = mouse_x - 10
		except AttributeError:
			pass
	if sliderer.x >= slider_max:
		sliderer.x = slider_max - 1
	if sliderer.x <= slider_min:
		sliderer.x = slider_min + 1

	if sliderer.x <= 162:
		randval = 4
		slide_speed = 20
	if sliderer.x >= 188:
		randval = 13
		slide_speed = 25
	if sliderer.x in range(163, 187):
		randval = 7
		slide_speed = 31

	pygame.draw.rect(screen, greenish, inside)

	areas.draw(screen)

	things.draw(screen)

	if cloning == False:
		pygame.draw.rect(screen, red, clone_btn)
	else:
		pygame.draw.rect(screen, green, clone_btn)

	if runaway == False:
		pygame.draw.rect(screen, red, runaway_btn)
	else:
		pygame.draw.rect(screen, green, runaway_btn)

	if followin == False:
		pygame.draw.rect(screen, red, follow_btn)
	else:
		pygame.draw.rect(screen, green, follow_btn)

	if randomin == False:
		pygame.draw.rect(screen, red, random_btn)
	else:
		pygame.draw.rect(screen, green, random_btn)

	if rotating == False:
		pygame.draw.rect(screen, red, rotate_btn)
	else:
		pygame.draw.rect(screen, green, rotate_btn)

	if slidin == False:
		pygame.draw.rect(screen, red, slidin_btn)
	else:
		pygame.draw.rect(screen, green, slidin_btn)

	pygame.draw.rect(screen, greenish, switchole)
	if guyval == True:
		pygame.draw.rect(screen, (250, 250, 250), switcher1)
	else:
		pygame.draw.rect(screen, (250, 250, 250), switcher2)

	pygame.draw.rect(screen, greenish, sliderhole)
	pygame.draw.rect(screen, (250, 250, 250), sliderer)

	screen.blit(clean_btn, (8, 5))

	guy_group.update()
	guy_group.draw(screen)

	score_show = score_text.get_rect(center=score_display.center)
	screen.blit(score_text, score_show)

	pygame.display.flip()

	clock.tick(60)