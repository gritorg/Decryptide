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

    id = cv.create_polygon(x0, y0,
                      x1, y1,
                      x2, y2, 
                      x3, y3, 
                      x4, y4, 
                      x5, y5,
                      **options)
    return id
    



class CryptideBoardCanvas(tk.Canvas):
    def __init__(self, master, biome_grid = None, animal_grid = None):
         super().__init__(master, width=1000, height=800)
         if biome_grid is not None and animal_grid is not None:
             self.biome_grid = biome_grid
             self.animal_grid = animal_grid
             self.place_hex_net(self, 30, self.biome_grid, self.animal_grid)

    def place_hex_net(self, r, biome_grid, animal_grid, **options):
        """ne marche que pour des largeur paire"""
        self.delete("all")
        assert biome_grid.shape == animal_grid.shape
        self.hex_id_table = [[]]*len(biome_grid)
        for i in range(len(biome_grid)):
            x = 100
            y = 100 + i*2*r*sin(pi/3)
            yp = y + r*sin(pi/3)
            for j in range(len(biome_grid[0])//2):
                hex_id = place_hexa(self, x, y, r, fill=BiomeColor[biome_grid[i, 2*j]], outline=AnimalsColor[animal_grid[i, 2*j]], width=10, **options)
                self.hex_id_table[i].append(hex_id)
                xp = x + r*(1+cos(pi/3))
                hex_id = place_hexa(self, xp, yp, r, fill=BiomeColor[biome_grid[i, 2*j+1]], outline=AnimalsColor[animal_grid[i, 2*j+1]], width=10, **options)
                self.hex_id_table[i].append(hex_id)
                x += 2*r*(1 + cos(pi/3))

class SetupInterface(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Mise en place du plateau")
        self.entree = tk.Entry(self)
        self.cv = CryptideBoardCanvas(self)
        self.bouton = tk.Button(self, text="valider", command=self.validate)

        self.entree.pack()
        self.bouton.pack()
        self.cv.pack()

    def validate(self):
        numbers = list(map(int,list(self.entree.get())))
        assert len(numbers) == 6
        
        self.board = Board(numbers)

        self.cv.place_hex_net(30, self.board.biome_grid, self.board.animal_grid)
        
    

class GameInterface(tk.Tk):
    def __init__(self):
        pass
