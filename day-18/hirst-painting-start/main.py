import colorgram
import random
import turtle as t
# turtle: https://docs.python.org/3.8/library/turtle.html#module-turtle

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

tim.hideturtle()  # make the turtle invisible
tim.penup()  # no drawing when moving

tim.setheading(225)
tim.forward(353)
tim.setheading(0)

dot_interval = 50
number_of_dots = 100
dot_radius = 20
dot_per_row = 10


def go_to_start_position(_):
    if _ % dot_per_row == 0:
        tim.setheading(90)
        tim.forward(dot_interval)
        tim.setheading(180)
        tim.forward(dot_per_row * dot_interval)
        tim.setheading(0)


for dot_count in range(1, number_of_dots + 1):
    tim.dot(dot_radius, random.choice(rgb_colors))
    tim.forward(dot_interval)
    go_to_start_position(dot_count)

screen = t.Screen()
screen.exitonclick()
