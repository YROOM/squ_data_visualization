import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# 数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, y)

# ==================== 主刻度 major ====================
ax.xaxis.set_major_locator(MultipleLocator(2))  # 主刻度间隔 2
ax.yaxis.set_major_locator(MultipleLocator(0.5))  # 主刻度间隔 0.5
ax.tick_params(which='major', length=10, color='blue', labelsize=12)

# ==================== 次刻度 minor ====================
ax.xaxis.set_minor_locator(MultipleLocator(0.5))  # 次刻度间隔 0.5
ax.yaxis.set_minor_locator(MultipleLocator(0.25))  # 次刻度间隔 0.25

# 关键：手动把次刻度也显示数值
for tick in ax.xaxis.get_minorticklocs():
    ax.text(tick, -1.1, f'{tick}', ha='center', fontsize=8, color='red')

for tick in ax.yaxis.get_minorticklocs():
    ax.text(-0.3, tick, f'{tick:.2f}', va='center', fontsize=8, color='red')

# 次刻度样式（更短）
ax.tick_params(which='minor', length=4, color='red')

# 网格
ax.grid(which='both', alpha=0.3)
plt.ylim(-1.2, 1.2)
plt.tight_layout()
plt.show()