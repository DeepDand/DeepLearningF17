# by Pablo Rivas
# vanilla script to view the weights using matplotlib

import numpy as np
import matplotlib.pyplot as plt

x = np.load('filters.npy')
p = np.zeros((320,320))

for i in range(10):
  for j in range(10):
    p[i*32:(i*32)+32,j*32:(j*32)+32] = np.reshape(x[:,(i*10)+j],(32,32))

plt.imshow(p,cmap='spectral')
plt.colorbar()
plt.show()

