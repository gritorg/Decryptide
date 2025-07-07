import matplotlib.pyplot as plt
import tkinter as tk
from math import cos, sin, pi
from utils import BIOME1, BIOME2, BIOME3, BIOME4, BIOME5, BIOME6
from utils import Biome, BiomeColor

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
    
def  place_hex_net(cv : tk.Canvas, x0, y0, r, grid):
    """ne marche que pour des largeur paire"""

    for i in range(len(grid)):
        x = x0
        y = y0 + i*2*r*sin(pi/3)
        yp = y + r*sin(pi/3)
        for j in range(len(grid[0])//2):
            place_hexa(cv, x, y, r, BiomeColor[grid[i, 2*j]])
            xp = x + r*(1+cos(pi/3))
            place_hexa(cv, xp, yp, r, BiomeColor[grid[i, 2*j+1]])
            x += 2*r*(1 + cos(pi/3))
    
fenetre = tk.Tk()
canva = tk.Canvas(fenetre, width=1000, height=1000)
place_hex_net(canva, 100, 100, 20, BIOME1)
canva.pack()
fenetre.mainloop()