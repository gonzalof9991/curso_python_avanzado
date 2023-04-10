from PIL import Image
import numpy as np


class Canvas:
    def __init__(self, height,width,color) -> None:
        self.height = height
        self.width = width
        self.color = color
        
        # Create a 3D numpy of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # changes [0,0,0] with user given values for color
        self.data[:] = self.color
    
    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)
