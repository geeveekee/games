import pygame
import random
import time
import sus
import sus2

pygame.init()

run = True
window = pygame.display.set_mode((800, 560))
pygame.display.set_caption("Snakes and Ladders")


#background
bg = pygame.image.load('snl.jpg')
bgg = pygame.image.load('bgg.jpg')
goh = pygame.image.load('goh.jpg')
gop = pygame.image.load('gop.jpg')
button = pygame.Rect((600, 80), (125, 125))

#players
p1 = pygame.image.load('p1.png')
p2 = pygame.image.load('p2.png')

font1 = pygame.font.SysFont('comicsansms', 30)
font2 = pygame.font.SysFont('comicsansms', 30)


dice = pygame.image.load('dice.png')

def drawScreen():
	window.blit(bgg, (0, 0))
	window.blit(bg, (0, 0))
	window.blit(dice, (600, 80))

def drawWinnerScreen(chance):
	if chance == 'po':
		#winner homer
		window.blit(goh, (0, 0))
	else:
		window.blit(gop, (0, 0))
	 
def player1(p1x = 13, p1y = 495):
	window.blit(p1, (p1x, p1y))

def player2(p2x = 2, p2y = 485):
	window.blit(p2, (p2x, p2y))

def pickNumber():
	dr = random.randint(1, 6)
	if dr == 1:
		dice = pygame.image.load('d1.png')
	elif dr == 2:
		dice = pygame.image.load('d2.png')
	elif dr == 3:
		dice = pygame.image.load('d3.png')
	elif dr == 4:
		dice = pygame.image.load('d4.png')
	elif dr == 5:
		dice = pygame.image.load('d5.png')
	elif dr == 6:
		dice = pygame.image.load('d6.png')

	return(dice, dr)

def po():
	msg1 = font1.render("Po...", True, (0, 0, 0))
	window.blit(msg1, [580, 300])
	window.blit(p1, (700, 300))

def homer():
	msg2 = font2.render("Homer...", True, (0, 0, 0))
	window.blit(msg2, [580, 300])
	window.blit(p2, (700, 280))

def turn():
	msg3 = font2.render("It is Your Turn", True, (255, 255, 255))
	window.blit(msg3, [580, 350])


p1x = 13
p1y = 495
p2x = 2
p2y = 485
x1 =0
y1 =0 
x2 =0
y2 =0
chance = 'po'
while run:

	window.fill((0, 255, 195))
	drawScreen()

	if chance == 'po':
		po()
		turn()
	else:
		homer()
		turn()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = pygame.mouse.get_pos()
			if button.collidepoint(mouse_pos):
				pickNumber()
				dice,dr = pickNumber()
				window.blit(dice, (600, 80))
				print(dr)

			#for po
			if chance == 'po' and pickNumber():
				#chance = 'homer'
				x1, y1, chance = sus.impostar(p1x, p1y, dr)
				p1x = x1
				p1y = y1
				print("back here")	

			#for homer
			elif chance == 'homer' and pickNumber():
				x2, y2, chance = sus2.impostar(p2x, p2y, dr)
				p2x = x2
				p2y = y2
	

	
	player1(p1x, p1y)
	player2(p2x, p2y)
	if (p1x == 13 and p1y == 0) or (p2x == 2 and p2y == -10):
		print("Game over")
		drawWinnerScreen(chance)
	pygame.display.update()
	time.sleep(0.25)


pygame.quit()
quit()
