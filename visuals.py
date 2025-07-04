import matplotlib.pyplot as plt
import tkinter as tk
from math import cos, sin, pi
from utils import BIOME1, BIOME2, BIOME3, BIOME4, BIOME5, BIOME6

def place_hexa(cv : tk.Canvas, x0, y0, r, color):
    "draw a regular hexagone on the canva cv at coordiante x0, y0"
    x1, y1 = x0 + r*cos(pi/3), y0 + r*sin(pi/3)
    x2, y2 = x1 + r, y1
    x3, y3 = x2 + r*cos(pi/3), y0
    x4, y4 = x2, y0 - r*sin(pi/3)
    x5, y5 = x1, y4

    cv.create_polygon(x0, y0,
                      x1, y1,
                      x2, y2, 
                      x3, y3, 
                      x4, y4, 
                      x5, y5,
                      fill = color)
    
