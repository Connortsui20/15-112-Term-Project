import numpy as np

class NDCTriangle:
    def __init__(self, triangle, normal, color):
        
        self.normal = normal #? Do I need this?
        self.color = color
        
        self.triangle = np.array([np.true_divide(x, x[3])[:3] for x in triangle]) #perspective divide