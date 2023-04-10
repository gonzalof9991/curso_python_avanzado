import numpy as np
from PIL import Image

# Create 3d numpy array from image
data = np.zeros((5, 4, 3), dtype=np.uint8)
# [:] -> all rows, all columns, all channels
data[:] = [255, 0, 0]  # red patch in upper left
data[0:4, 0:3] = [0, 255, 0]  # green patch in upper left
print(data)

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')