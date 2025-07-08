import numpy as np
from numpy import array
from enum import Enum

Biome = {
    0 : "LAC",
    1 : "DESERT",
    2 : "MARAIS",
    3 : "MONTAGNE",
    4 : "FORET"
}

BiomeColor = {0 : "blue",
              1 : "yellow",
              2 : "purple",
              3 : "grey",
              4 : "green"}

BIOMES = [0]*6
BIOMES[0] = array([[0,0,0,0,4,4],
                   [2,2,0,1,4,4],
                   [2,2,1,1,1,4]])
BIOMES[1] = array([[2,4,4,4,4,4],
                   [2,2,4,1,1,1],
                   [2,3,3,3,3,1]])
BIOMES[2] = array([[2,2,4,4,4,0],
                    [2,2,4,3,0,0],
                    [3,3,3,3,0,0]])
BIOMES[3] = array([[1,1,3,3,3,3],
                   [1,1,3,0,0,0],
                   [1,1,1,4,4,4]])
BIOMES[4] = array([[0,0,0,0,1,1],
                   [3,3,0,1,1,2],
                   [3,3,3,2,2,2]])
BIOMES[5] = array([[1,1,2,2,2,4],
                   [3,3,2,2,4,4],
                   [3,0,0,0,0,4]])

ANIMALS = [0]*6
ANIMALS[0] = array([[0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,1,1,1]])
ANIMALS[1] = array([[2,2,2,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0]])
ANIMALS[2] = array([[0,0,0,0,0,0],
                    [2,2,0,0,0,0],
                    [2,0,0,0,0,0]])
ANIMALS[3] = array([[0,0,0,0,0,0],
                    [0,0,0,0,0,2],
                    [0,0,0,0,0,2]])
ANIMALS[4] = array([[1,1,0,0,0,0],
                    [1,0,0,0,0,0],
                    [0,0,0,0,0,0]])
ANIMALS[5] = array([[1,0,0,0,0,0],
                    [1,0,0,0,0,0],
                    [0,0,0,0,0,0]])
AnimalsColor = {0 : "",
                1 : "red",
                2 : "black"}

