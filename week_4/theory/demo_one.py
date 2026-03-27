import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Windows 用户（取消下面一行的注释）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

x = np.linspace(0, 10, 100)
y = np.sin(x)
y_cos = np.cos(x)

def sinplot(flip=2):
    x = np.linspace(0, 20, 50)
    for i in range(1, 5):
        plt.plot(x, np.cos(x + i * 0.8) * (9 - 2*i) * flip)
sinplot()

plt.show()

# 老版本
sns.set(font_scale=1.5)
sns.set_style('darkgrid')      # 设置主题
sns.set_context('notebook')    # 设置上下文
sns.set_palette('deep')        # 设置调色板
sinplot()
plt.show()

# 新版本
sns.set_theme(style='dark',font_scale=1.5)
sinplot()
plt.show()

# 新版推荐写法
#     sns.set_theme(
#         style='darkgrid',    # 主题风格
#         context='notebook',  # 缩放上下文
#         palette='deep',      # 调色板
#         font='sans-serif',   # 字体
#         font_scale=1,        # 字体缩放
#         color_codes=True,    # 颜色代码
#         rc=None              # 额外rc参数
#     )


    # 示例：不同context对比
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
contexts = ['paper', 'notebook', 'talk', 'poster']

for ax, context in zip(axes.flatten(), contexts):
    sns.set_theme(style='whitegrid', context=context, palette='deep')
    ax.plot(x, y, linewidth=2, label='sin(x)')
    ax.set_title(f'context="{context}"', fontsize=12, pad=10)
    ax.set_xlabel('X label')
    ax.set_ylabel('Y label')
    ax.legend()
plt.tight_layout()
plt.show()