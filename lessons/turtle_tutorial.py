from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
leo.color(99, 204, 250)
leo.penup()
leo.goto(-150, -50)
leo.pendown()
leo.begin_fill()
i: int = 0
while i < 3:
    leo.forward(300)
    leo.left(120)
    i = i + 1
# leo.begin_fill()
leo.fillcolor(200, 50, 150)
# code for shape to be filled 
leo.end_fill()
leo.speed(50)
leo.hideturtle()


bob: Turtle = Turtle()
bob.color(150,25,100)
bob.penup()
bob.goto(-150,-50)
bob.pendown()
bob.speed(100)

side_length: int = 300
i: int = 0
while i < 133:
    bob.forward(side_length)
    bob.left(121)
    side_length = side_length * 0.97
    i = i + 1

done()