"""
SYST 230: Mod 4- OO Programming
Lab 4: 2D Random Walk with Enhancements
Author: Joshua R. Obee
Purpose: This program is a game where two turtles
start from the center and move only in random directions.
The first turtle to reach the border of their square wins.
"""

import turtle
from random import choice

# World and step parameters
WORLDSIZE = 250
STEPSIZE = 5
CENTERS = (-200, 0), (200, 0)
turtle.speed(30)

class World:
    """Data and methods for setting and drawing boundaries
    for random walk"""

    def __init__(self, size, center=(0, 0), pen=None):
        self.size = size
        self.center = center
        self.pen = turtle.Turtle() if pen is None else pen

    def draw_world(self):
        x, y = self.center
        cords = (x + self.size // 2, y + self.size // 2), (x - self.size // 2, y + self.size // 2), \
                (x - self.size // 2, y - self.size // 2), (x + self.size // 2, y - self.size // 2)

        self.pen.penup()
        self.pen.goto(cords[0])
        self.pen.pendown()
        for p in cords + (cords[0],):
            self.pen.goto(p)
        self.pen.penup()
        self.pen.goto(self.center)
        self.pen.pendown()

    def get_limits(self) -> tuple:
        half_size = self.size // 2
        x, y = self.center
        xll = x - half_size
        yll = y - half_size
        xul = x + half_size
        yul = y + half_size
        return xll, yll, xul, yul


class Walker:
    """Data and methods for implementing and tracing a Random walk"""

    def __init__(self, step_size, world, pen=None, pen_color=None):
        self.step_size = step_size
        self.world = world
        self.pen = world.pen if pen is None else pen
        self.numsteps = 0
        if pen_color:
            self.pen.color(pen_color)
        self.pen.speed(2)

    def step(self):
        paths = (0, self.step_size), (0, -self.step_size), (self.step_size, 0), (-self.step_size, 0)
        c = choice(paths)
        new_pos = (self.pen.xcor() + c[0], self.pen.ycor() + c[1])
        self.pen.goto(new_pos)

    def next_step(self) -> bool:
        limits = self.world.get_limits()
        if limits[0] < self.pen.xcor() < limits[2] and limits[1] < self.pen.ycor() < limits[3]:
            self.step()
            turtle.stamp()
            return True
        return False

def main():
    turtle.bgcolor("#252525")
    turtle.title('2D RANDOM WALK WITH ENHANCEMENTS')

    pens = [turtle.Turtle("turtle") for _ in CENTERS]
    colors = 'green', 'gold'
    worlds = [World(WORLDSIZE, c, p) for c, p in zip(CENTERS, pens)]
    walkers = [Walker(STEPSIZE, w, pen_color=c) for w, c in zip(worlds, colors)]

    for w in worlds:
        w.draw_world()

    turtle.textinput("ENTER TO CONTINUE", "SERIOUSLY PRESS <ENTER>")

    while walkers:
        for w in walkers:
            if not w.next_step():
                walkers.remove(w)


if __name__ == '__main__':
    main()
    turtle.exitonclick()
