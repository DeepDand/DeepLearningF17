import glob
from PIL import Image
import numpy as np

for filename in glob.iglob('*.png'):
  print(filename)

  img = Image.open(filename).convert('L')
  img.save(filename)

