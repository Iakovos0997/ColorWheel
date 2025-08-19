from graphics import *
import math, colorsys, button, ColorWheel

win = GraphWin("Color Wheel", 600, 600, autoflush=False)

wheel = ColorWheel.ColorWheel(win, step=3)
wheel.run()