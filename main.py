from graphics import *
import math, colorsys

win = GraphWin("Color Wheel", 900, 600)

# Areas and Sizes
cx, cy, R = 300, 300, 250
Circle(Point(cx, cy), R).draw(win)

panel = Rectangle(Point(600, 40), Point(880, 560))
panel.setOutline("gray")
panel.draw(win)
Text(Point(740, 60), "Selection Panel").draw(win)

win.getMouse()
win.Close()