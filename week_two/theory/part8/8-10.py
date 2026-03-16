import matplotlib.pyplot as plt
import numpy as np

N = 60
np.random.seed(100)
x = np.random.rand(N) #生成60个[0，1）之间的随机数
y = np.random.rand(N)
fig, axes = plt.subplots()
axes.scatter(x, y)
plt.show()