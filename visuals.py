import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np
from math import cos, sin, pi
from utils import BIOMES, Biome, BiomeColor, AnimalsColor
from game import Board

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
    
def place_hex_net(cv : tk.Canvas, x0, y0, r, biome_grid, animal_grid, **options):
    """ne marche que pour des largeur paire"""
    assert biome_grid.shape == animal_grid.shape
    for i in range(len(biome_grid)):
        x = x0
        y = y0 + i*2*r*sin(pi/3)
        yp = y + r*sin(pi/3)
        for j in range(len(biome_grid[0])//2):
            place_hexa(cv, x, y, r, fill=BiomeColor[biome_grid[i, 2*j]], outline=AnimalsColor[animal_grid[i, 2*j]], width=5, **options)
            xp = x + r*(1+cos(pi/3))
            place_hexa(cv, xp, yp, r, fill=BiomeColor[biome_grid[i, 2*j+1]], outline=AnimalsColor[animal_grid[i, 2*j+1]], width=5, **options)
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
        numbers = list(map(int,list(self.entree.get())))
        assert len(numbers) == 6
        
        self.board = Board(numbers)

        self.cv.delete("all")
        place_hex_net(self.cv, 100, 100, 40, self.board.biome_grid, self.board.animal_grid)
    

class GameInterface(tk.Tk):
    def __init__(self):
        pass
