import matplotlib.pyplot as plt
import numpy as np

from week_two.theory.part8.demo_8_10 import opacity

fig, axes = plt.subplots()
data_m = (40, 60, 120, 180, 20, 200)  # 男士
data_f = (30, 100, 150, 30, 20, 50)  # 女士
index = np.arange(6)
width = 0.4
opacity = 0.4
axes.bar(index, data_m, width, color='c', label='men', alpha=opacity)
axes.bar(index, data_f, width, color='b', label='women',align='edge',alpha = opacity)
axes.set_xticks(index + width / 2)
axes.set_xticklabels(('Taxi', 'Metro', 'Walk', 'Bus', 'Bicycle', 'Driving'))
axes.legend()
axes.set_title('bar chart')
plt.show()
