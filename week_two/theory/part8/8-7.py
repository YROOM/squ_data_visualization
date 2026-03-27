import matplotlib.pyplot as plt
import numpy as np

data = np.random.standard_normal(1000)  # 生成1000个服从正太分布的随机数
fig, axes = plt.subplots()
n, bins, patches = axes.hist(data, bins=10, density=True)
y = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * bins ** 2)
axes.plot(bins, y, '--')
axes.set_title('demo 23  inter 1')
plt.show()
# fig, axes = plt.subplots()
# labels = ['Taxi', 'Metro', 'Walk', 'Bus', 'Bicycle', 'Driving']
# sizes = [10, 30, 5, 25, 5, 25]
# explode = (0, 0.1, 0, 0, 0, 0)
# axes.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
# axes.axis('equal')
# axes.set_title('pie chart')
# plt.show()