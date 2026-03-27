import matplotlib.pyplot as plt
import numpy as np
N = 60
np.random.seed(100) #设置随机数种子
x = np.random.rand(N)
y = np.random.rand(N)
s = np.pi*(15*np.random.rand(N))**2
c =-s
opacity = 0.1
fig, axes = plt.subplots()
axes.scatter(x, y,s,c,alpha = opacity)
plt.show()