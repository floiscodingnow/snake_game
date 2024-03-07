from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakespiel - für Pascal und Santiago")

sarting_positions = [(0,0),(-20,0),(-40,0)] 

for positions in range(0,3):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(sarting_positions[positions])


screen.exitonclick()