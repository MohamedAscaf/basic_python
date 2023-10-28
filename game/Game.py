# import turtle
# import random
#
# w = 500
# h = 500
# food_size = 10
# delay = 150
#
# offsets = {
#     "up": (0, 20),
#     "down": (0, -20),
#     "left": (-20, 0),
#     "right": (20, 0)
# }
#
# def reset():
#     global snake, snake_dir, food_position, pen
#     snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
#     snake_dir = "up"
#     food_position = get_random_food_position()
#     food.goto(food_position)
#     move_snake()
#
# def move_snake():
#     global snake_dir
#
#     new_head = snake[-1].copy()
#     new_head[0] = snake[-1][0] + offsets[snake_dir][0]
#     new_head[1] = snake[-1][1] + offsets[snake_dir][1]
#
#
#     if new_head in snake[:-1]:
#         reset()
#     else:
#         snake.append(new_head)
#
#
#         if not food_collision():
#             snake.pop(0)
#
#
#         if snake[-1][0] > w / 2:
#             snake[-1][0] -= w
#         elif snake[-1][0] < - w / 2:
#             snake[-1][0] += w
#         elif snake[-1][1] > h / 2:
#             snake[-1][1] -= h
#         elif snake[-1][1] < -h / 2:
#             snake[-1][1] += h
#
#
#         pen.clearstamps()
#
#
#         for segment in snake:
#             pen.goto(segment[0], segment[1])
#             pen.stamp()
#
#
#         screen.update()
#
#         turtle.ontimer(move_snake, delay)
#
# def food_collision():
#     global food_position
#     if get_distance(snake[-1], food_position) < 20:
#         food_position = get_random_food_position()
#         food.goto(food_position)
#         return True
#     return False
#
# def get_random_food_position():
#     x = random.randint(- w / 2 + food_size, w / 2 - food_size)
#     y = random.randint(- h / 2 + food_size, h / 2 - food_size)
#     return (x, y)
#
# def get_distance(pos1, pos2):
#     x1, y1 = pos1
#     x2, y2 = pos2
#     distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
#     return distance
# def go_up():
#     global snake_dir
#     if snake_dir != "down":
#         snake_dir = "up"
#
# def go_right():
#     global snake_dir
#     if snake_dir != "left":
#         snake_dir = "right"
#
# def go_down():
#     global snake_dir
#     if snake_dir!= "up":
#         snake_dir = "down"
#
# def go_left():
#     global snake_dir
#     if snake_dir != "right":
#         snake_dir = "left"
#
#
# screen = turtle.Screen()
# screen.setup(w, h)
# screen.title("Sanria Snake Game")
#
# screen.setup(500, 500)
# screen.tracer(0)
#
#
# pen = turtle.Turtle("square")
# pen.penup()
#
#
# food = turtle.Turtle()
# food.shape("turtle")
# food.color("red")
# food.shapesize(food_size / 10)
# food.penup()
#
#
# screen.listen()
# screen.onkey(go_up, "Up")
# screen.onkey(go_right, "Right")
# screen.onkey(go_down, "Down")
# screen.onkey(go_left, "Left")
#
#
# reset()
# turtle.done()
#Coded with Sanria💙 by Mr. Mohamed Ascaf




# """Pacman, classic arcade game.
#
# Exercises
#
# 1. Change the board.
# 2. Change the number of ghosts.
# 3. Change where pacman starts.
# 4. Make the ghosts faster/slower.
# 5. Make the ghosts smarter.
# """
#
# from random import choice
# from turtle import *
#
# from freegames import floor, vector
#
# state = {'score': 0}
# path = Turtle(visible=False)
# writer = Turtle(visible=False)
# aim = vector(5, 0)
# pacman = vector(-40, -80)
# ghosts = [
#     [vector(-180, 160), vector(5, 0)],
#     [vector(-180, -160), vector(0, 5)],
#     [vector(100, 160), vector(0, -5)],
#     [vector(100, -160), vector(-5, 0)],
# ]
# # fmt: off
# tiles = [
#     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#     0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
#     0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
#     0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
#     0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
#     0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
#     0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
#     0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
#     0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
#     0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
#     0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
#     0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
#     0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
#     0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
#     0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
#     0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
#     0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
#     0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
#     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
# ]
# # fmt: on
#
#
# def square(x, y):
#     """Draw square using path at (x, y)."""
#     path.up()
#     path.goto(x, y)
#     path.down()
#     path.begin_fill()
#
#     for count in range(4):
#         path.forward(20)
#         path.left(90)
#
#     path.end_fill()
#
#
# def offset(point):
#     """Return offset of point in tiles."""
#     x = (floor(point.x, 20) + 200) / 20
#     y = (180 - floor(point.y, 20)) / 20
#     index = int(x + y * 20)
#     return index
#
#
# def valid(point):
#     """Return True if point is valid in tiles."""
#     index = offset(point)
#
#     if tiles[index] == 0:
#         return False
#
#     index = offset(point + 19)
#
#     if tiles[index] == 0:
#         return False
#
#     return point.x % 20 == 0 or point.y % 20 == 0
#
#
# def world():
#     """Draw world using path."""
#     bgcolor('black')
#     path.color('blue')
#
#     for index in range(len(tiles)):
#         tile = tiles[index]
#
#         if tile > 0:
#             x = (index % 20) * 20 - 200
#             y = 180 - (index // 20) * 20
#             square(x, y)
#
#             if tile == 1:
#                 path.up()
#                 path.goto(x + 10, y + 10)
#                 path.dot(5, 'white')
#
#
# def move():
#     """Move pacman and all ghosts."""
#     writer.undo()
#     writer.write(state['score'])
#
#     clear()
#
#     if valid(pacman + aim):
#         pacman.move(aim)
#
#     index = offset(pacman)
#
#     if tiles[index] == 1:
#         tiles[index] = 2
#         state['score'] += 1
#         x = (index % 20) * 20 - 200
#         y = 180 - (index // 20) * 20
#         square(x, y)
#
#     up()
#     goto(pacman.x + 10, pacman.y + 10)
#     dot(20, 'yellow')
#
#     for point, course in ghosts:
#         if valid(point + course):
#             point.move(course)
#         else:
#             options = [
#                 vector(5, 0),
#                 vector(-5, 0),
#                 vector(0, 5),
#                 vector(0, -5),
#             ]
#             plan = choice(options)
#             course.x = plan.x
#             course.y = plan.y
#
#         up()
#         goto(point.x + 10, point.y + 10)
#         dot(20, 'red')
#
#     update()
#
#     for point, course in ghosts:
#         if abs(pacman - point) < 20:
#             return
#
#     ontimer(move, 100)
#
#
# def change(x, y):
#     """Change pacman aim if valid."""
#     if valid(pacman + vector(x, y)):
#         aim.x = x
#         aim.y = y
#
#
# setup(420, 420, 370, 0)
# hideturtle()
# tracer(False)
# writer.goto(160, 160)
# writer.color('white')
# writer.write(state['score'])
# listen()
# onkey(lambda: change(5, 0), 'Right')
# onkey(lambda: change(-5, 0), 'Left')
# onkey(lambda: change(0, 5), 'Up')
# onkey(lambda: change(0, -5), 'Down')
# world()
# move()
# done()

#Coded with Sanria💙 by Mr. Mohamed Ascaf




'''
Sanria Hangman Game
-------------------------------------------------------------
'''


# import random
# import time
# import os
#
#
# def play_again():
#   question = 'Do You want to play again? y = yes, n = no \n'
#   play_game = input(question)
#   while play_game.lower() not in ['y', 'n']:
#       play_game = input(question)
#
#   if play_game.lower() == 'y':
#       return True
#   else:
#       return False
#
#
# def hangman(word):
#   display = '_' * len(word)
#   count = 0
#   limit = 5
#   letters = list(word)
#   guessed = []
#   while count < limit:
#       guess = input(f'Hangman Word: {display} Enter your guess: \n').strip()
#       while len(guess) == 0 or len(guess) > 1:
#           print('Invalid input. Enter a single letter\n')
#           guess = input(
#               f'Hangman Word: {display} Enter your guess: \n').strip()
#
#       if guess in guessed:
#           print('Oops! You already tried that guess, try again!\n')
#           continue
#
#       if guess in letters:
#           letters.remove(guess)
#           index = word.find(guess)
#           display = display[:index] + guess + display[index + 1:]
#
#       else:
#           guessed.append(guess)
#           count += 1
#           if count == 1:
#               time.sleep(1)
#               print('   _____ \n'
#                     '  |      \n'
#                     '  |      \n'
#                     '  |      \n'
#                     '  |      \n'
#                     '  |      \n'
#                     '  |      \n'
#                     '__|__\n')
#               print(f'Wrong guess: {limit - count} guesses remaining\n')
#
#           elif count == 2:
#               time.sleep(1)
#               print('   _____ \n'
#                     '  |     | \n'
#                     '  |     | \n'
#                     '  |      \n'
#                     '  |      \n'
#                     '  |      \n'
#                     '  |      \n'
#                     '__|__\n')
#               print(f'Wrong guess: {limit - count} guesses remaining\n')
#
#           elif count == 3:
#               time.sleep(1)
#               print('   _____ \n'
#                     '  |     | \n'
#                     '  |     | \n'
#                     '  |     | \n'
#                     '  |      \n'
#                     '  |      \n'
#                     '  |      \n'
#                     '__|__\n')
#               print(f'Wrong guess: {limit - count} guesses remaining\n')
#
#           elif count == 4:
#               time.sleep(1)
#               print('   _____ \n'
#                     '  |     | \n'
#                     '  |     | \n'
#                     '  |     | \n'
#                     '  |     O \n'
#                     '  |      \n'
#                     '  |      \n'
#                     '__|__\n')
#               print(f'Wrong guess: {limit - count} guesses remaining\n')
#
#           elif count == 5:
#               time.sleep(1)
#               print('   _____ \n'
#                     '  |     | \n'
#                     '  |     | \n'
#                     '  |     | \n'
#                     '  |     O \n'
#                     '  |    /|\ \n'
#                     '  |    / \ \n'
#                     '__|__\n')
#               print('Wrong guess. You\'ve been hanged!!!\n')
#               print(f'The word was: {word}')
#
#       if display == word:
#           print(f'Congrats! You have guessed the word \'{word}\' correctly!')
#           break
#
#
# def play_hangman():
#    print('\nWelcome to Sanria Hangman\n')
#    name = input('Enter your name: ')
#    print(f'Hello {name}! Best of Luck!')
#    time.sleep(1)
#    print('The game is about to start!\nLet\'s play Hangman!')
#    time.sleep(1)
#    os.system('cls' if os.name == 'nt' else 'clear')
#
#    words_to_guess = [
#        'january', 'border', 'image', 'film', 'promise', 'kids',
#        'lungs', 'doll', 'rhyme', 'damage', 'plants', 'hello', 'world'
#    ]
#    play = True
#    while play:
#        word = random.choice(words_to_guess)
#        hangman(word)
#        play = play_again()
#
#    print('Thanks For Playing! We expect you back again!')
#    exit()
#
#
# if __name__ == '__main__':
#   play_hangman()

#Coded with Sanria💙 by Mr. Mohamed Ascaf




#EGG GAME
# from itertools import cycle
# from random import randrange
# from tkinter import Canvas, Tk, messagebox, font
#
# canvas_width = 800
# canvas_height = 400
#
# root = Tk()
# root.title("Egg Catcher by Sanria")
# c = Canvas(root, width=canvas_width, height=canvas_height, background="deep sky blue")
# c.create_rectangle(-5, canvas_height-100, canvas_width+5, canvas_height+5, fill="sea green", width=0)
# c.create_oval(-80, -80, 120, 120, fill='orange', width=0)
# c.pack()
#
# color_cycle = cycle(["light blue", "light green", "light pink", "light yellow", "light cyan"])
# egg_width = 45
# egg_height = 55
# egg_score = 10
# egg_speed = 100
# egg_interval = 4000
# difficulty = 0.95
# catcher_color = "blue"
# catcher_width = 100
# catcher_height = 100
# catcher_startx = canvas_width / 2 - catcher_width / 2
# catcher_starty = canvas_height - catcher_height - 20
# catcher_startx2 = catcher_startx + catcher_width
# catcher_starty2 = catcher_starty + catcher_height
#
# catcher = c.create_arc(catcher_startx, catcher_starty, catcher_startx2, catcher_starty2, start=200, extent=140, style="arc", outline=catcher_color, width=3)
# game_font = font.nametofont("TkFixedFont")
# game_font.config(size=18)
#
#
# score = 0
# score_text = c.create_text(10, 10, anchor="nw", font=game_font, fill="darkblue", text="Score: "+ str(score))
#
# lives_remaining = 3
# lives_text = c.create_text(canvas_width-10, 10, anchor="ne", font=game_font, fill="darkblue", text="Lives: "+ str(lives_remaining))
#
# eggs = []
#
# def create_egg():
#     x = randrange(10, 740)
#     y = 40
#     new_egg = c.create_oval(x, y, x+egg_width, y+egg_height, fill=next(color_cycle), width=0)
#     eggs.append(new_egg)
#     root.after(egg_interval, create_egg)
#
# def move_eggs():
#     for egg in eggs:
#         (eggx, eggy, eggx2, eggy2) = c.coords(egg)
#         c.move(egg, 0, 10)
#         if eggy2 > canvas_height:
#             egg_dropped(egg)
#     root.after(egg_speed, move_eggs)
#
# def egg_dropped(egg):
#     eggs.remove(egg)
#     c.delete(egg)
#     lose_a_life()
#     if lives_remaining == 0:
#         messagebox.showinfo("Game Over!", "Final Score: "+ str(score))
#         root.destroy()
#
# def lose_a_life():
#     global lives_remaining
#     lives_remaining -= 1
#     c.itemconfigure(lives_text, text="Lives: "+ str(lives_remaining))
#
# def check_catch():
#     (catcherx, catchery, catcherx2, catchery2) = c.coords(catcher)
#     for egg in eggs:
#         (eggx, eggy, eggx2, eggy2) = c.coords(egg)
#         if catcherx < eggx and eggx2 < catcherx2 and catchery2 - eggy2 < 40:
#             eggs.remove(egg)
#             c.delete(egg)
#             increase_score(egg_score)
#     root.after(100, check_catch)
#
# def increase_score(points):
#     global score, egg_speed, egg_interval
#     score += points
#     egg_speed = int(egg_speed * difficulty)
#     egg_interval = int(egg_interval * difficulty)
#     c.itemconfigure(score_text, text="Score: "+ str(score))
#
# def move_left(event):
#     (x1, y1, x2, y2) = c.coords(catcher)
#     if x1 > 0:
#         c.move(catcher, -20, 0)
#
# def move_right(event):
#     (x1, y1, x2, y2) = c.coords(catcher)
#     if x2 < canvas_width:
#         c.move(catcher, 20, 0)
#
# c.bind("<Left>", move_left)
# c.bind("<Right>", move_right)
# c.focus_set()
# root.after(1000, create_egg)
# root.after(1000, move_eggs)
# root.after(1000, check_catch)
# root.mainloop()

#Coded with Sanria💙 by Mr. Mohamed Ascaf





#
# import pygame
# black = (0, 0, 0)
# white = (255, 255, 255)
#
# red = (255, 0, 0)
# WIDTH = 20
# HEIGHT = 20
# MARGIN = 5
# grid = []
# for row in range(10):
#     grid.append([])
#     for column in range(10):
#         grid[row].append(0)
# grid[1][5] = 1
# pygame.init()
# window_size = [255, 255]
# scr = pygame.display.set_mode(window_size)
# pygame.display.set_caption("Sanria Grid")
# done = False
# clock = pygame.time.Clock()
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             pos = pygame.mouse.get_pos()
#             column = pos[0] // (WIDTH + MARGIN)
#             row = pos[1] // (HEIGHT + MARGIN)
#             grid[row][column] = 1
#             print("Click ", pos, "Grid coordinates: ", row, column)
#     scr.fill(black)
#     for row in range(10):
#         for column in range(10):
#             color = white
#             if grid[row][column] == 1:
#                 color = red
#             pygame.draw.rect(scr,
#                              color,
#                              [(MARGIN + WIDTH) * column + MARGIN,
#                               (MARGIN + HEIGHT) * row + MARGIN,
#                               WIDTH,
#                               HEIGHT])
#     clock.tick(50)
#     pygame.display.flip()
# pygame.quit()

#Coded with Sanria💙 by Mr. Mohamed Ascaf

import pygame, sys
import numpy as np
pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

RED = (255, 0, 0)
BG_COLOR = (20, 200, 160)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'SANRIA TIC TAC TOE' )
screen.fill( BG_COLOR )

board = np.zeros( (BOARD_ROWS, BOARD_COLS) )

def draw_lines():

	pygame.draw.line( screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH )

	pygame.draw.line( screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH )

	pygame.draw.line( screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH )

	pygame.draw.line( screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )

def draw_figures():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col] == 1:
				pygame.draw.circle( screen, CIRCLE_COLOR, (int( col * SQUARE_SIZE + SQUARE_SIZE//2 ), int( row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
			elif board[row][col] == 2:
				pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH )
				pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH )

def mark_square(row, col, player):
	board[row][col] = player

def available_square(row, col):
	return board[row][col] == 0

def is_board_full():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col] == 0:
				return False

	return True

def check_win(player):
	for col in range(BOARD_COLS):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			draw_vertical_winning_line(col, player)
			return True

	for row in range(BOARD_ROWS):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			draw_horizontal_winning_line(row, player)
			return True

	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		draw_asc_diagonal(player)
		return True

	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		draw_desc_diagonal(player)
		return True

	return False

def draw_vertical_winning_line(col, player):
	posX = col * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH )

def draw_horizontal_winning_line(row, player):
	posY = row * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH )

def draw_asc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH )

def draw_desc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH )

def restart():
	screen.fill( BG_COLOR )
	draw_lines()
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			board[row][col] = 0

draw_lines()

player = 1
game_over = False

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

			mouseX = event.pos[0]
			mouseY = event.pos[1]

			clicked_row = int(mouseY // SQUARE_SIZE)
			clicked_col = int(mouseX // SQUARE_SIZE)

			if available_square( clicked_row, clicked_col ):

				mark_square( clicked_row, clicked_col, player )
				if check_win( player ):
					game_over = True
				player = player % 2 + 1

				draw_figures()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				restart()
				player = 1
				game_over = False

	pygame.display.update()

#Coded with Sanria💙 by Mr. Mohamed Ascaf
