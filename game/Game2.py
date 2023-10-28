# import pygame
# import time
# import random
#
# pygame.init()
#
# white = (255, 255, 255)
# pink = (255, 255, 102)
# black = (0, 0, 0)
# red = (213, 50, 80)
# green = (0, 255, 0)
# blue = (50, 153, 213)
#
# dis_width = 600
# dis_height = 400
#
# dis = pygame.display.set_mode((dis_width, dis_height))
# pygame.display.set_caption('Snake Game by Sanria')
#
# clock = pygame.time.Clock()
#
# snake_block = 10
# snake_speed = 10
#
# font_style = pygame.font.SysFont("bahnschrift", 25)
# score_font = pygame.font.SysFont("comicsansms", 35)
#
# def our_snake(snake_block, snake_list):
#     for x in snake_list:
#         pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
#
#
# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_width / 6, dis_height / 3])
#
#
# def gameLoop():
#     game_over = False
#     game_close = False
#
#     x1 = dis_width / 2
#     y1 = dis_height / 2
#
#     x1_change = 0
#     y1_change = 0
#
#     snake_List = []
#     Length_of_snake = 1
#
#     foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#     foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
#
#     while not game_over:
#
#         while game_close == True:
#             dis.fill(blue)
#             message("You Lost! Press C-Play Again or Q-Quit", red)
#
#             pygame.display.update()
#
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         gameLoop()
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -snake_block
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = snake_block
#                     x1_change = 0
#
#         if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
#             game_close = True
#         x1 += x1_change
#         y1 += y1_change
#         dis.fill(blue)
#         pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
#         snake_Head = []
#         snake_Head.append(x1)
#         snake_Head.append(y1)
#         snake_List.append(snake_Head)
#         if len(snake_List) > Length_of_snake:
#             del snake_List[0]
#
#         for x in snake_List[:-1]:
#             if x == snake_Head:
#                 game_close = True
#
#         our_snake(snake_block, snake_List)
#
#
#         pygame.display.update()
#
#         if x1 == foodx and y1 == foody:
#             foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#             foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
#             Length_of_snake += 1
#
#         clock.tick(snake_speed)
#
#     pygame.quit()
#     quit()
#
#
# gameLoop()

#Coded with Sanria💙 by Mr. Mohamed Ascaf



# '''
# Mad Libs Generator
# -------------------------------------------------------------
# '''
#
# # Questions for the user to answer
#
# noun = input('Choose a noun: ')
#
# p_noun = input('Choose a plural noun: ')
#
# noun2 = input('Choose a noun: ')
#
# place = input('Name a place: ')
#
# adjective = input('Choose an adjective (Describing word): ')
#
# noun3 = input('Choose a noun: ')
#
# # Print a story from the user input
#
# print('------------------------------------------')
#
# print('Be kind to your', noun, '- footed', p_noun)
#
# print('For a duck may be somebody\'s', noun2, ',')
#
# print('Be kind to your', p_noun, 'in', place)
#
# print('Where the weather is always', adjective, '. \n')
#
# print('You may think that is this the', noun3, ',')
#
# print('Well it is.')
#
# print('------------------------------------------')

#Coded with Sanria💙 by Mr. Mohamed Ascaf



# import turtle
# import time
# import random
#
# # Set up the screen
# wn = turtle.Screen()
# wn.title("Snake Sanria Game")
# wn.bgcolor("black")
# wn.setup(width=600, height=600)
# wn.tracer(0)
#
# # Snake head
# head = turtle.Turtle()
# head.speed(0)
# head.shape("circle")
# head.color("brown")
# head.penup()
# head.goto(0, 0)
# head.direction = "stop"
#
# # Food
# food = turtle.Turtle()
# food.speed(0)
# food.shape("circle")
# food.color("white")
# food.penup()
# food.goto(0, 100)
#
# segments = []
#
# # Functions
# def move():
#     if head.direction == "up":
#         y = head.ycor()
#         head.sety(y + 20)
#
#     if head.direction == "down":
#         y = head.ycor()
#         head.sety(y - 20)
#
#     if head.direction == "left":
#         x = head.xcor()
#         head.setx(x - 20)
#
#     if head.direction == "right":
#         x = head.xcor()
#         head.setx(x + 20)
#
# def go_up():
#     if head.direction != "down":
#         head.direction = "up"
#
# def go_down():
#     if head.direction != "up":
#         head.direction = "down"
#
# def go_left():
#     if head.direction != "right":
#         head.direction = "left"
#
# def go_right():
#     if head.direction != "left":
#         head.direction = "right"
#
# # Keyboard bindings
# wn.listen()
# wn.onkeypress(go_up, "Up")
# wn.onkeypress(go_down, "Down")
# wn.onkeypress(go_left, "Left")
# wn.onkeypress(go_right, "Right")
#
# # Main game loop
# while True:
#     wn.update()
#
#     # Check for collision with food
#     if head.distance(food) < 20:
#         x = random.randint(-290, 290)
#         y = random.randint(-290, 290)
#         food.goto(x, y)
#
#         # Add a segment to the snake
#         new_segment = turtle.Turtle()
#         new_segment.speed(5)
#         new_segment.shape("circle")
#         new_segment.color("pink")
#         new_segment.penup()
#         segments.append(new_segment)
#
#     # Move the end segments first in reverse order
#     for index in range(len(segments) - 1, 0, -1):
#         x = segments[index - 1].xcor()
#         y = segments[index - 1].ycor()
#         segments[index].goto(x, y)
#
#     # Move segment 0 to where the head is
#     if len(segments) > 0:
#         x = head.xcor()
#         y = head.ycor()
#         segments[0].goto(x, y)
#
#     move()
#
#     # Check for collisions with the wall or the body
#     if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
#         time.sleep(1)
#         head.goto(0, 0)
#         head.direction = "stop"
#
#         # Hide the segments
#         for segment in segments:
#             segment.goto(1000, 1000)
#
#         segments.clear()
#
#     for segment in segments:
#         if segment.distance(head) < 20:
#             time.sleep(0.1)
#             head.goto(1, 1)
#             head.direction = "stop"
#
#             # Hide the segments
#             for segment in segments:
#                 segment.goto(1200, 1200)
#
#             segments.clear()
#
#     time.sleep(0.1)  # Increase the sleep time to slow down the snake
#
# wn.mainloop()

#Coded with Sanria💙 by Mr. Mohamed Ascaf



#import all the required libraries first
import sys
from tkinter import *
#import time library to obtain current time
import time

#create a function timing and variable current_time
def timing():
    #display current hour,minute,seconds
    current_time = time.strftime("%H : %M : %S")
    #configure the clock
    clock.config(text=current_time)
    #clock will change after every 200 microseconds
    clock.after(200,timing)

#Create a variable that will store our tkinter windowan
root=Tk()
#define size of the window
root.geometry("600x300")
#create a variable clock and store label
#First label will show time, second label will show hour:minute:second, third label will show the top digital clock
clock=Label(root,font=("times",60,"bold"),bg="blue")
clock.grid(row=2,column=2,pady=25,padx=100)
timing()

#create a variable for digital clock
digital=Label(root,text="AskPython's Digital Clock",font="times 24 bold")
digital.grid(row=0,column=2)

nota=Label(root,text="hours        minutes        seconds",font="times 15 bold")
nota.grid(row=3,column=2)

root.mainloop()
