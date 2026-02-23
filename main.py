import tkinter as tk
import numpy as np

from visuals import SetupInterface
from utils import BIOMES, ANIMALS

fenetre = SetupInterface("123456")
board = fenetre.mainloop()
print(board.structures) 