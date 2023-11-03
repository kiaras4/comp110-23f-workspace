"""Happy Halloween with Jack-O-Lanterns and a Star!"""

__author__ = "730675328"

from turtle import Turtle, colormode, done, tracer, update

colormode(255)


def main() -> None:
    """The entrypoint of my Happy Halloween scene."""
    tracer(0, 0)  # Disable delay in tracing
    r_turtle: Turtle = Turtle()
    r_turtle.fillcolor("brown")
    r_turtle.setheading(0.0)
    draw_rect(r_turtle, -10, 140, 30)
    draw_rect(r_turtle, -207, 225, 25)
    draw_rect(r_turtle, 172, 225, 25)
    draw_pumpkins(r_turtle)
    r_turtle.fillcolor(250, 250, 50)
    draw_triangle(r_turtle, 25, 50, 40, 120)
    draw_triangle(r_turtle, -60, 50, 40, 120)
    r_turtle.setheading(0.0)
    draw_star(r_turtle, -50, 250, 100, 144)
    r_turtle.setheading(105.0)
    draw_star(r_turtle, -2, 216, 35, 144)
    draw_msg(r_turtle, -200, -200)
    r_turtle.fillcolor(250, 250, 50)
    draw_mouth(r_turtle, -30, 10, 15, 120)
    r_turtle.setheading(90.0)
    draw_rect(r_turtle, -225, 175, 15)
    draw_rect(r_turtle, -190, 175, 15)
    r_turtle.setheading(75.0)
    draw_rect(r_turtle, 150, 175, 15)
    r_turtle.setheading(285.0)
    draw_rect(r_turtle, 210, 180, 15)
    draw_mouth(r_turtle, -220, 150, 10, 120)
    draw_mouth(r_turtle, 160, 150, 10, 120)
    update()  # Now update the rendering
    done()


def draw_circle(c_turtle: Turtle, x: float, y: float, radius: float, color: str) -> None:
    """Draw a circle of the given radius where the bottom starts at x,y. - contributes to pumpkin."""
    c_turtle.color(0, 0, 0)
    c_turtle.penup()
    c_turtle.goto(x, y)
    c_turtle.pendown()
    c_turtle.begin_fill()
    c_turtle.fillcolor(color)
    c_turtle.circle(radius)
    c_turtle.end_fill()
    c_turtle.speed(300)
    c_turtle.hideturtle()


def draw_rect(r_turtle: Turtle, x: float, y: float, width: float) -> None:
    """This function is used to draw the stems for the pumpkins as well as some of the eyes."""
    r_turtle.penup()
    r_turtle.goto(x, y) 
    r_turtle.pendown()
    r_turtle.speed(300)
    r_turtle.begin_fill()
    i: int = 0
    while i < 4:
        if i % 2 != 0:
            r_turtle.forward(width)
            r_turtle.right(90)
            i = i + 1
        else:
            width2: float = width - 10
            r_turtle.forward(width2)
            r_turtle.right(90)
            i = i + 1
    r_turtle.end_fill()
    r_turtle.hideturtle()


def draw_triangle(t_turtle: Turtle, x: float, y: float, forward: float, left: float) -> None:
    """This function draw triangles of the given base length and angle."""
    t_turtle.penup()
    t_turtle.goto(x, y) 
    t_turtle.pendown()
    t_turtle.speed(300)
    t_turtle.begin_fill()
    i: int = 0
    while i < 3:
        t_turtle.forward(forward)
        t_turtle.left(left)
        i = i + 1
    t_turtle.end_fill()
    t_turtle.hideturtle()


def draw_pumpkins(circle1: Turtle) -> None:
    """This functions uses simpler functions to draw the pumpkins in the scene."""
    color: str = "orange"
    draw_circle(circle1, 40, -30, 75, color)
    draw_circle(circle1, -40, -30, 75, color)
    draw_circle(circle1, 0, -35, 75, color)
    x: int = -180
    y: int = 120
    num: int = 0
    while num < 2:
        draw_circle(circle1, x, y, 45, color)
        x -= 40
        draw_circle(circle1, x, y, 45, color)
        x += 20
        y -= 3
        draw_circle(circle1, x, y, 45, color)
        x += 400
        y += 3
        num += 1
    circle1.hideturtle()


def draw_star(sr_turtle: Turtle, x: float, y: float, length: float, angle: float) -> None:
    """This function draws stars using the given length and degree for the angles.
    
    The outline pen color is yellow instead of black.
    """
    sr_turtle.color(250, 250, 50)
    sr_turtle.penup()
    sr_turtle.goto(x, y) 
    sr_turtle.pendown()
    sr_turtle.speed(300)
    sr_turtle.begin_fill()
    i: int = 0
    while i < 5:
        sr_turtle.forward(length)
        sr_turtle.right(angle)
        i += 1
    sr_turtle.fillcolor(250, 250, 50)
    sr_turtle.end_fill()
    sr_turtle.hideturtle()


def draw_msg(r_turtle: Turtle, x: float, y: float) -> None:
    """Uses bonus function .write to include a message in the scene."""
    r_turtle.penup()
    r_turtle.color(0, 0, 0)
    r_turtle.goto(x, y)
    r_turtle.pendown()
    r_turtle.write("Happy Halloween", move=False, align="left", font=("Verdana", 35, "italic"))
    r_turtle.penup()
    r_turtle.color("orange")
    r_turtle.goto(x + 3, y + 1)
    r_turtle.pendown()
    r_turtle.write("Happy Halloween", move=False, align="left", font=("Verdana", 35, "italic"))


def draw_mouth(r_turtle: Turtle, x: float, y: float, base: float, left: float) -> None:
    """Calls draw_triangle to creates the mouths of the jack-o-lanterns."""
    r_turtle.penup()
    r_turtle.goto(x, y) 
    r_turtle.pendown()
    r_turtle.speed(300)
    r_turtle.begin_fill()
    xs: float = x
    i: int = 0
    while i < 3:
        r_turtle.setheading(0.0)
        draw_triangle(r_turtle, xs, y, base, left)
        r_turtle.setheading(180.0)
        draw_triangle(r_turtle, xs, y, base, left)
        xs += 2 * base
        i += 1
    r_turtle.end_fill()
    r_turtle.hideturtle()


if __name__ == "__main__":
    main()