import matplotlib.pyplot as plt
import numpy as np

data = np.random.standard_normal(1000)  # 生成1000个服从正太分布的随机数
fig, axes = plt.subplots()
n, bins, patches = axes.hist(data, bins=50, density=True)
y = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * bins ** 2)
axes.plot(bins, y, '--')
plt.show()
