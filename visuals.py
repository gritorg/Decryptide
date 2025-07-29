import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np
from math import cos, sin, pi, exp
from cmath import exp
from utils import BIOMES, Biome, BiomeColor, AnimalsColor, StructureList
from game import Board

def place_reg_poly(cv, n, x0, y0, r, phi=0,**options):
    """place a regular polygon centered on x0, y0"""

    l=[]
    for k in range(n):
        affix = x0 + y0*1j + r*exp(((2*k/n)*pi+phi)*1j)
        x, y = float(affix.real), float(affix.imag)
        l.append((x, y))

    id = cv.create_polygon(l, **options)
    return id


def place_hexa(cv : tk.Canvas, x0, y0, r, **options):
    "draw a regular hexagone on the canva cv"
    "with left vertex a coordinates x0, y0"
    id = place_reg_poly(cv, 6, x0, y0, r, **options)
    return id

def place_triangle(cv : tk.Canvas, x0, y0, r, **options):
    "draw an equilateral triangle with left vertex at coordinate x0, y0"
    id = place_reg_poly(cv, 3, x0, y0, r, phi=pi/6, **options)
    return id 
    
def place_octogone(cv : tk.Canvas, x0, y0, r, **options):
    "draw a reglar octogone of radius r centered on x0, y0"
    id = place_reg_poly(cv, 8, x0, y0, r, phi=pi/8, **options)
    return id 

def draw_structure(cv, struct_id, x, y, r, **options):

    color = StructureList[struct_id][1]
    if StructureList[struct_id][0] == 3:
        id = place_triangle(cv, x, y, r, fill=color, **options)
    elif StructureList[struct_id][0] == 8:
        id = place_octogone(cv, x, y, r, fill=color, **options)
    else:
        raise ValueError("les structures ne peuvent être que des cabanes ou des pierres")
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
        self.hex_id_table = []
        self.id_to_coord = {}
        for i in range(len(biome_grid)):
            self.hex_id_table.append([])
            x = 70
            y = 100 + i*2*r*sin(pi/3)
            yp = y + r*sin(pi/3)
            for j in range(len(biome_grid[0])//2):
                place_hexa(self, x, y, r, fill=BiomeColor[biome_grid[i, 2*j]], outline="black", width=1,  **options)
                hex_id = place_hexa(self, x, y, 35, fill='', outline=AnimalsColor[animal_grid[i, 2*j]], width=3, activefill="white", **options)
                self.hex_id_table[i].append(hex_id)
                self.id_to_coord[hex_id] = (i, 2*j)
                xp = x + r*(1+cos(pi/3))
                place_hexa(self, xp, yp, r, fill=BiomeColor[biome_grid[i, 2*j+1]], outline="black", width=1, activefill="white", **options)
                hex_id = place_hexa(self, xp, yp, 35, fill='', outline=AnimalsColor[animal_grid[i, 2*j+1]], width=3, activefill="white", **options)
                self.hex_id_table[i].append(hex_id)
                self.id_to_coord[hex_id] = (i, 2*j +1)
                x += 2*r*(1 + cos(pi/3))

    def set_click_function(self, func):
        """func is a  function that takes the id as an argument"""
        for i in range(9):
            for j in range(12):
                hex_id = self.hex_id_table[i][j]
                self.tag_bind(hex_id, '<Button-1>', lambda e, i=hex_id : func(i))

class SelectionCanvas(tk.Canvas):

    def __init__(self, master):
        super().__init__(master, width = 600, height=100, bg="white")
        self.selected_structure = None
        self.id_table = {}

    def draw_choice(self):
        for struct_id in range(6):
            id = draw_structure(self, struct_id, 50+100*struct_id, 50, 30, outline="black", activefill="#888888")
            self.id_table[id] = struct_id
            self.tag_bind(id, "<Button-1>", lambda e, i=id : self.struct_on_click(i))
    
    def struct_on_click(self, id):
        if self.selected_structure is not None:
            self.itemconfig(self.selected_structure, outline="black", width=1)
        self.selected_structure = id
        self.itemconfig(id, outline="red", width=3)

    @property
    def chosen(self):
        return self.id_table[self.selected_structure]


class SetupInterface(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Mise en place du plateau")

        self.top_frame = tk.Frame(self)
        
        self.board_choice_frame = tk.Frame(self.top_frame)
        self.entree = tk.Entry(self.board_choice_frame)
        self.bouton = tk.Button(self.board_choice_frame, text="Valider", command=self.validate)
        self.end_button = tk.Button(self.top_frame, text="Done", command=self.quit)

        self.structure_cv = SelectionCanvas(self.top_frame)

        self.cv = CryptideBoardCanvas(self)

        self.entree.pack()
        self.bouton.pack()
        self.board_choice_frame.pack(side="left", expand=True)
        self.structure_cv.pack(side="left", expand=True)
        self.end_button.pack(side="left")
        self.top_frame.pack()
        self.cv.pack()

    def validate(self):
        numbers = list(map(int,list(self.entree.get())))
        assert len(numbers) == 6
        
        self.board = Board(numbers)

        self.cv.place_hex_net(self.board.biome_grid, self.board.animal_grid)
        self.structure_placement_routine()

    def structure_placement_routine(self):

        self.structure_cv.draw_choice()

        def click_func(id):
            self.place_structure(self.structure_cv.chosen, id)
            i,j = self.cv.id_to_coord[id]
            self.board.add_structure(i,j,self.structure_cv.chosen)

        self.cv.set_click_function(click_func)

    def place_structure(self, struct_id, hex_id, **options):
        """structure_id is the index of the structure in StructureList"""
        l = self.cv.coords(hex_id)
        x, y = l[0]-35, l[1]
        draw_structure(self.cv, struct_id, x, y, 25, **options)

    def mainloop(self, n = 0):
        super().mainloop(n)
        return self.board
     
        
class GameInterface(tk.Tk):
    def __init__(self):
        pass
