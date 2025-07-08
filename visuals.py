import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np
from math import cos, sin, pi
from utils import BIOMES
from utils import Biome, BiomeColor

def place_hexa(cv : tk.Canvas, x0, y0, r, **options):
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
                      **options)
    
def  place_hex_net(cv : tk.Canvas, x0, y0, r, grid):
    """ne marche que pour des largeur paire"""

    for i in range(len(grid)):
        x = x0
        y = y0 + i*2*r*sin(pi/3)
        yp = y + r*sin(pi/3)
        for j in range(len(grid[0])//2):
            place_hexa(cv, x, y, r, fill=BiomeColor[grid[i, 2*j]], activeoutline="black")
            xp = x + r*(1+cos(pi/3))
            place_hexa(cv, xp, yp, r, fill=BiomeColor[grid[i, 2*j+1]], activeoutline="black")
            x += 2*r*(1 + cos(pi/3))


class SetupInterface(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Mise en place du plateau")
        self.entree = tk.Entry(self)
        self.bouton = tk.Button(self, text="valider", command=self.validate)
        self.cv = tk.Canvas(self, width=1000, height=1000)

        self.entree.pack()
        self.bouton.pack()
        self.cv.pack()

    def validate(self):
        numbers = self.entree.get()
        assert len(numbers) == 6
        self.cv.delete("all")

        biome_list = [[],[],[]]
        for i in range(3):
            for j in range(2):
                biome_list[i].append(BIOMES[int(numbers[2*i+j])-1])
        biome_grid = np.block(biome_list)

        place_hex_net(self.cv, 100, 100, 20, biome_grid)



