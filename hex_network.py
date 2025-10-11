import numpy as np

def neighbor(self, i, j):
        l = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        if i%2 == 0:
            l.append((i+1, j+1))
            l.append((i+1, j-1))
        else:
            l.append((i-1, j+1))
            l.append((i-1, j-1))

        for (k,(i,j)) in enumerate(l):
            
            if i<0 or i>8:
                l.pop(k)
            if j<0 or j>11:
                l.pop(k)
        return l

class HexaNetwork:

    def __init__(self, row = 9, cols=12):
        self.content = np.zeros(row, cols)

    def __getitem__(self, key):
        return self.content[key]
    
    def __setitem__(self, key):
        return self.content[key]


    
