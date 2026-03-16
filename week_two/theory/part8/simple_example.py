
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
plt.show()                           # Show the figure.

# fig = plt.figure()             # an empty figure with no Axes
# fig, ax = plt.subplots()       # a figure with a single Axes
# fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
# # a figure with one Axes on the left, and two on the right:
# fig, axs = plt.subplot_mosaic([['left', 'right_top'],
#                                   ['left', 'right_bottom']])

# fig = plt.figure()
# axe = plt.subplot(2, 2, 1)
# axe = plt.subplot(2, 2, 3)
# fig.suptitle("121")
#
# plt.show()