import numpy as np
import matplotlib.pyplot as plt
fig, axes = plt.subplots()
labels = ['Taxi', 'Metro', 'Walk', 'Bus', 'Bicycle', 'Driving']
sizes = [10, 30, 5, 25, 5, 25]
explode = (0, 0.1, 0, 0, 0, 0)
axes.pie(sizes, explode=explode, labels=labels, autopct='%1.5f%%', shadow=True, startangle=90)
axes.axis('equal')
axes.set_title('pie chart')
plt.show()