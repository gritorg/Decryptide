import tkinter as tk
import numpy as np

from visuals import SetupInterface
from utils import BIOMES, ANIMALS

fenetre = SetupInterface()
board = fenetre.mainloop()
print(board.structures) 