import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# # Apply the default theme
# sns.set_theme()
#
# # Load an example dataset
# tips = sns.load_dataset("tips")
#
# # Create a visualization
# sns.relplot(
#     data=tips,
#     x="total_bill", y="tip", col="time",
#     hue="smoker", style="smoker", size="size",
# )
sns.set(style='whitegrid',font_scale=1.5)
def sinplot(flip=2):
    x = np.linspace(0, 20, 50)
    for i in range(1, 5):
        plt.plot(x, np.cos(x + i * 0.8) * (9 - 2*i) * flip)
sinplot()


plt.show()
