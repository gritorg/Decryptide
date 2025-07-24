import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np
from math import cos, sin, pi, exp
from cmath import exp
from utils import BIOMES, Biome, BiomeColor, AnimalsColor
from game import Board

def place_reg_poly(cv, n, x0, y0, r, **options):
    """place a regular polygon centered on x0, y0"""

    l=[]
    for k in range(n):
        affix = x0 + y0*1j + r*exp((2*k/n)*pi*1j)
        x, y = float(affix.real), float(affix.imag)
        l.append((x, y))

    id = cv.create_polygon(l, **options)
    return id


def place_hexa(cv : tk.Canvas, x0, y0, r, **options):
    "draw a regular hexagone on the canva cv"
    "with left vertex a coordinates x0, y0"
    place_reg_poly(cv, 6, x0, y0, r, **options)
    return id

def place_triangle(cv : tk.Canvas, x0, y0, r, **options):
    "draw an equilateral triangle with left vertex at coordinate x0, y0"
    id = place_reg_poly(cv, 3, x0, y0, r, **options)
    return id 
    
def place_octogone(cv : tk.Canvas, x0, y0, r, **options):
    "draw a reglar octogone of radius r centered on x0, y0"
    id = place_reg_poly(cv, 8, x0, y0, r, **options)
    return id 


class CryptideBoardCanvas(tk.Canvas):
    def __init__(self, master, biome_grid = None, animal_grid = None):
        super().__init__(master, width=800, height=800, bg="white")
        if biome_grid is not None and animal_grid is not None:
             self.biome_grid = biome_grid
             self.animal_grid = animal_grid
             self.place_hex_net(self, self.biome_grid, self.animal_grid)


    def place_hex_net(self, biome_grid, animal_grid, **options):
        """ne marche que pour des largeur paire"""
        r=40
        self.delete("all")
        assert biome_grid.shape == animal_grid.shape
        self.hex_id_table = [[]]*len(biome_grid)
        for i in range(len(biome_grid)):
            x = 70
            y = 100 + i*2*r*sin(pi/3)
            yp = y + r*sin(pi/3)
            for j in range(len(biome_grid[0])//2):
                hex_id = place_hexa(self, x, y, r, fill=BiomeColor[biome_grid[i, 2*j]], outline="black", width=1,  **options)
                place_hexa(self, x, y, 35, fill='', outline=AnimalsColor[animal_grid[i, 2*j]], width=3, activefill="white", **options)
                self.hex_id_table[i].append(hex_id)
                xp = x + r*(1+cos(pi/3))
                hex_id = place_hexa(self, xp, yp, r, fill=BiomeColor[biome_grid[i, 2*j+1]], outline="black", width=1, activefill="white", **options)
                place_hexa(self, xp, yp, 35, fill='', outline=AnimalsColor[animal_grid[i, 2*j+1]], width=3, activefill="white", **options)
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

        self.cv.place_hex_net(self.board.biome_grid, self.board.animal_grid)

    def place_structure(self):
        pass
     
        
class GameInterface(tk.Tk):
    def __init__(self):
        pass
