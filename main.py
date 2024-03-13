import pygame,sys
from game import Game
from colors import Colors

# initialize pygame
pygame.init()

titleFont = pygame.font.Font(None,40)
score_surface = titleFont.render("Score", True, Colors.darkblue, Colors.white)
next_surface = titleFont.render("Next Block", True, Colors.darkblue, Colors.white)
game_over = titleFont.render("GAME OVER", True, Colors.darkblue, Colors.white)

score_rect = pygame.Rect(320, 100, 170, 60)
next_rect = pygame.Rect(320, 240, 170, 200)

mint_green = (134, 240, 162)
white = (255,255,255)

# display surface of width 300 and height 600 as a tuple was for the grid
screen = pygame.display.set_mode((500,620))
pygame.display.set_caption("TETRIS")

# clock object for the framerate of the game
clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE,250) #HAPPENS EVERY 200ms

# game loop
while True:

	# gets all the events required by pygame and puts them in a list
	for event in pygame.event.get():
		if event.type == pygame.QUIT:

			# game is ended if we quit the game
			pygame.quit()
			sys.exit()

			# users key input
		if event.type == pygame.KEYDOWN:

			if game.game_over == True:
				game.game_over = False
				game.reset()

				# LEFT ARROW KEY
			if event.key == pygame.K_LEFT and game.game_over==False:
				game.move_left()
			if event.key == pygame.K_RIGHT and game.game_over==False:
				game.move_right()
			if event.key == pygame.K_DOWN and game.game_over==False:
				game.move_down()
				game.update_score(0,1)
			if event.key == pygame.K_UP and game.game_over==False:
				game.rotate()

		if event.type == GAME_UPDATE and game.game_over==False:
			game.move_down()

	score_value_surface = titleFont.render(str(game.score),True,Colors.darkblue)		

	screen.fill(white)

	# text 
	screen.blit(score_surface,(365,60,100,100))
	screen.blit(next_surface,(335,200,100,100))

	if game.game_over==True:
		screen.blit(game_over,(325,500,100,100))

	# last two for rounded corners
	pygame.draw.rect(screen,Colors.blue, score_rect, 8 , 20)
	screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
	pygame.draw.rect(screen,Colors.blue, next_rect, 8 , 20)

	game.draw(screen)
	pygame.display.update()


	# the game will run at 60fps
	clock.tick(60) 