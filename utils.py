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


BIOME1 = array([[0,0,0,0,4,4],
                [2,2,0,1,4,4],
                [2,2,1,1,1,4]])
BIOME2 = array([[2,4,4,4,4,4],
                [2,2,4,1,1,1],
                [2,3,3,3,3,1]])
BIOME3 = array([[2,2,4,4,4,0],
                [2,2,4,3,0,0],
                [3,3,3,3,0,0]])
BIOME4 = array([[1,1,3,3,3,3],
                [1,1,3,0,0,0],
                [1,1,1,4,4,4]])
BIOME5 = array([[0,0,0,0,1,1],
                [3,3,0,1,1,2],
                [3,3,3,2,2,2]])
BIOME6 = array([[1,1,2,2,2,4],
                [3,3,2,2,4,4],
                [3,0,0,0,0,4]])

