###-----------------------------YOU CAN DELETE IT IF YOU WANT -----------------------------------------------
#import colorgram
#rgb_color_list = []

### This function is using colorgram.py library and
### It get the color from the image and extract it, so like this
### You have the RGB color in a list previously created called rgb_color_list
#def take_color(quant_pic):
#    color = colorgram.extract('image.jpg', quant_pic)
#    for color in color:
#        r = color.rgb.r
#        g = color.rgb.g
#        b = color.rgb.b
#        rgb_tuple = (r, g, b)
#        rgb_color_list.append(rgb_tuple)

#take_color(30)
#print(rgb_color_list)
###---------------------------------------------------------------------------------------
import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

color_list = [(190, 18, 44), (245, 232, 62), (220, 64, 106),
              (197, 175, 15), (201, 75, 29), (10, 143, 88), (210, 236, 242),
              (14, 126, 177), (106, 182, 211), (251, 220, 228), (10, 167, 215),
              (242, 232, 1), (24, 40, 78), (211, 150, 90), (34, 43, 112), (77, 176, 94),
              (215, 65, 48), (186, 42, 60), (221, 129, 156), (125, 185, 112), (239, 162, 182),
              (5, 60, 40), (146, 208, 221), (6, 90, 53), (4, 86, 111), (165, 28, 27), (238, 170, 162),
              (162, 212, 176)]

terry = Turtle()

num = 0

terry.penup()
terry.speed("fastest")


def paint_line():
    for color in range(0, 10):
        rgb_color = random.choice(color_list)
        terry.pencolor(rgb_color)
        terry.dot(20)
        terry.forward(50)


def change_row(quant_position):
    terry.goto(0, quant_position)


for _ in range(0, 10):
    num += 50
    paint_line()
    change_row(num)
terry.hideturtle()


screen = Screen()
screen.exitonclick()

