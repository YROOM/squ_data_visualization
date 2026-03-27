import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# -------------------------- 第一步：准备示例数据（模拟成绩数据） --------------------------
# 生成50个学生的语文、数学、英语成绩（0-100分）
np.random.seed(100)  # 固定随机种子，结果可复现
chinese = np.random.randint(50, 100, size=50)  # 语文成绩
math = np.random.randint(40, 95, size=50)     # 数学成绩
english = np.random.randint(45, 98, size=50)  # 英语成绩
total = (chinese + math + english) / 3        # 平均分（用于颜色映射）

# -------------------------- 第二步：创建3D画布 --------------------------
# 方法1：新版Matplotlib推荐方式（兼容3.4+）
fig = plt.figure(figsize=(15, 5))  # 总画布大小：宽15，高5

# -------------------------- 子图1：3D散点图（成绩分布） --------------------------
ax1 = fig.add_subplot(131, projection='3d')  # 1行3列第1个子图，3D投影
# 绘制散点图：x=语文，y=数学，z=英语，c=平均分（颜色映射），s=点大小，alpha=透明度
scatter = ax1.scatter(chinese, math, english, c=total, cmap='viridis', s=60, alpha=0.8)
# 设置坐标轴标签
ax1.set_xlabel('语文成绩', fontsize=10)
ax1.set_ylabel('数学成绩', fontsize=10)
ax1.set_zlabel('英语成绩', fontsize=10)
ax1.set_title('3D散点图：学生三科成绩分布', fontsize=12)
# 添加颜色条（对应平均分）
fig.colorbar(scatter, ax=ax1, shrink=0.6, label='平均分')

# -------------------------- 子图2：3D曲面图（成绩趋势） --------------------------
ax2 = fig.add_subplot(132, projection='3d')  # 1行3列第2个子图
# 生成网格数据（模拟成绩趋势）
x = np.linspace(50, 100, 20)  # 语文成绩范围
y = np.linspace(40, 95, 20)   # 数学成绩范围
X, Y = np.meshgrid(x, y)      # 生成网格
Z = 0.8*X + 0.7*Y - 20        # 英语成绩拟合公式（模拟趋势）
# 绘制曲面图，cmap=颜色映射，edgecolor=边缘色
surf = ax2.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='gray', alpha=0.7)
ax2.set_xlabel('语文成绩', fontsize=10)
ax2.set_ylabel('数学成绩', fontsize=10)
ax2.set_zlabel('拟合英语成绩', fontsize=10)
ax2.set_title('3D曲面图：成绩拟合趋势', fontsize=12)
fig.colorbar(surf, ax=ax2, shrink=0.6, label='拟合分数')

# -------------------------- 子图3：3D折线图（单科成绩变化） --------------------------
ax3 = fig.add_subplot(133, projection='3d')  # 1行3列第3个子图
# 选取前20个学生的成绩绘制折线
x_line = chinese[:20]
y_line = math[:20]
z_line = english[:20]
# 绘制3D折线：marker=点标记，linewidth=线宽，color=颜色
ax3.plot(x_line, y_line, z_line, marker='o', linewidth=2, color='darkorange', markersize=5)
ax3.set_xlabel('语文成绩', fontsize=10)
ax3.set_ylabel('数学成绩', fontsize=10)
ax3.set_zlabel('英语成绩', fontsize=10)
ax3.set_title('3D折线图：前20名学生成绩变化', fontsize=12)

# -------------------------- 全局设置与显示 --------------------------
plt.tight_layout()  # 自动调整子图间距，避免重叠
plt.show()  # 显示图形