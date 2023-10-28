# import turtle
# a=turtle.Turtle()
# a.forward(100)
# a.backward(50)
# a.right(90)
# a.dot()
# a.forward(100)
# a.home()
# # a.clear()
# a.goto(60,60)
# a.shape("circle")
# a.left(750)
# a.right(80)
# a.forward(70)
# turtle.done()

# import turtle
# b=turtle.Turtle()
# b.speed(1)
# b.color("black")
# b.forward(100)
# b.right(90)
# b.color("red")
# b.left(90)
# b.color("yellow")
# b.forward(100)
# b.color("pink")
# b.shape("circle")
# b.color("brown")
# b.home()
# turtle.done()


# import turtle
# t=turtle.Turtle()
# t.penup()
# t.setpos(-30,50)
# t.pendown()
# t.pensize(20)
# t.pencolor("pink")
# t.forward(150)
# t.backward(150)
# t.right(10)
# t.forward(150)
# t.left(100)
# t.forward(150)
# t.backward(150)
# t.right(100)
# t.forward(150)
# t.left(100)
# t.forward(150)
# t.left(80)
# t.forward(150)
# t.left(100)
# t.home()
# turtle.done()


#
# import turtle
# star = turtle.Turtle()
# for x in range(10):
#     star.forward(200)
#     star.right(144)
# turtle.done()


# import turtle
# d=turtle.Turtle()
# d.speed(1)
# d.color("red")
# d.forward(100)
# d.right(90)
# d.color("orange")
# d.backward(100)
# d.left(90)
# d.color("yellow")
# d.forward(100)
# d.color("green")
# d.shape("circle")
# d.color("blue")
# d.home()
# turtle.done()


# import turtle
# colors = [ "red" , "orange" , "yellow" , "green" , "blue" , "indigo" , "violet" ]
# sketch = turtle.Pen()
# turtle.bgcolor("black")
# for x in range(200):
#
#    sketch.pencolor(colors[x % 7])
#    sketch.width(x/100 + 1)
#    sketch.forward(x)
#    sketch.left(59)


# import turtle
# s=turtle.Pen()
# s.width(50)
# s.color("indigo")
# s.right(90)
# s.forward(500)
# s.backward(600)
# for r in range(9):
#    for a in ("red","orange","yellow","green","blue" , "indigo" , "violet"):
#       s.color(a)
#       s.forward(10+r*10)
#       s.right(20)
# s.right(40)
# s.color("red")
# s.forward(100)
# s.color("black")
# s.shape("circle")
# turtle.done()



# import turtle
# s=turtle.Turtle()
# s.pensize(50)
# n=5
# s.speed(50)
# for x in range(20):
#    for a in ("Red" , "orange" , "yellow" , "green" , "blue", "indigo" , "violet"):
#       s.seth(n)
#       s.pencolor(a)
#       s.circle(100)
#       n+=10
# turtle.done()


# import turtle
# window = turtle.Screen()
# window.setup(520,520)   # Set Window size.
# window.tracer(0)        # Turn-off animation.
#
# TTL = turtle.Turtle()
# TTL.speed(1)
# TTL.shape("turtle")     # Select turtle's shape.
# TTL.penup()
# TTL.goto(-300, 0)       # Set turtle's starting position.
# turtle.write("Hello, livewire!")
# while True:
#     window.update()     # In each while loop, refresh the window with the new drawing.
#     TTL.forward(0.01)
# window.exitonclick()



import turtle
screen=turtle.Screen()
a=turtle.Turtle()
screen.setup(620,620)
screen.bgcolor('black')
clr=['bronze' , 'green' , 'blue' , 'yellow' , 'purple']
a.pensize(6)
a.shape('turtle')
a.penup()
a.pencolor('orange')
m=0
for x in range(12):
    m=m+1
    a.penup()
    a.setheading(-30*x+60)
    a.forward(150)
    a.pendown()
    a.forward(25)
    a.penup()
    a.forward(20)
    a.write(str(m),align="center",font=("Arial",12,"normal"))
    if m==12:
     m=0
    a.home()
a.home()
a.setpos(0,-250)
a.pendown()
a.pensize(10)
a.pencolor('white')
a.circle(250)
a.penup()
a.setpos(150,-270)
a.pendown()
a.pencolor('olive')
a.write('bye bye python',font=("Arial",12,"normal"))
a.ht()
turtle.done()
