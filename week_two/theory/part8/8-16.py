import matplotlib.pyplot as plt

import numpy as np

fig, axes = plt.subplots()

np.random.seed(100)

x = np.arange(0, 10, 1)
y1 = np.random.rand(10)
print(y1)
y2 = np.random.rand(10)
print(y2)

axes.plot(x, y1, '-o', color='c')
axes.plot(x, y2, '--o', color='b')

plt.show()
