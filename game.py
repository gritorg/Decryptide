import numpy as np
from utils import BIOMES, ANIMALS

class Board:
    def __init__(self, number_list):

        biome_list = [[],[],[]]
        animal_list = [[],[],[]]
        for i in range(3):
            for j in range(2):
                biome_list[i].append(BIOMES[int(number_list[2*i+j])-1])
                animal_list[i].append(ANIMALS[int(number_list[2*i+j])-1])

        self.biome_grid = np.block(biome_list)
        self.animal_grid = np.block(animal_list)

        self.structures= np.zeros((9, 12), dtype=int)


    def add_structure(self, i, j, struct_id):
        self.structures[i,j] = struct_id    