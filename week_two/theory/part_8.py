# matplotlib_all_examples.py
# 所有绘图例子整合版

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ====================== 1. 多子图 ======================
def example_1_subplots():
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)
    axes[0, 0].plot(t, s)
    axes[0, 0].set_title('simple plot')

    np.random.seed(20180201)
    s = np.random.randn(2, 50)
    axes[0, 1].hist(s[0])
    axes[0, 1].set_title('histogram')

    axes[1, 0].scatter(s[0], s[1])
    axes[1, 0].set_title('scatter plot')

    labels = ['Taxi', 'Metro', 'Walk', 'Bus', 'Bicycle', 'Drive']
    sizes = [10, 30, 5, 25, 5, 25]
    explode = (0, 0.1, 0, 0, 0, 0)
    axes[1, 1].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                   shadow=True, startangle=90)
    axes[1, 1].axis('equal')
    axes[1, 1].set_title('pie chart')

    plt.tight_layout()
    plt.show()

# ====================== 2. 线条样式 ======================
def example_2_line_style():
    fig, axes = plt.subplots()
    t = np.arange(0.0, 2.0, 0.01)
    s1 = np.sin(2 * np.pi * t)
    s2 = np.sin(2 * np.pi * (t + 0.5))
    axes.plot(t, s1, color='k', linestyle='-', label='line1')
    axes.plot(t, s2, color='c', linestyle='--', label='line2')
    axes.legend()
    plt.show()

# ====================== 3. 坐标轴与边框 ======================
def example_3_axis_spine():
    fig, axes = plt.subplots()
    t = np.arange(0.0, 2.0, 0.01)
    s1 = np.sin(2 * np.pi * t)
    s2 = np.sin(2 * np.pi * (t + 0.5))
    axes.plot(t, s1, color='k', linestyle='-', label='line1')
    axes.plot(t, s2, color='c', linestyle='--', label='line2')

    axes.set_xticks(np.arange(0.0, 2.5, 0.5))
    axes.set_yticks([-1, 0, 1])
    axes.minorticks_on()

    axes.spines['right'].set_color('none')
    axes.spines['top'].set_color('none')
    axes.spines['bottom'].set_position(('data', 0))
    plt.show()

# ====================== 4. 注释与文字 ======================
def example_4_annotate():
    fig, axes = plt.subplots()
    axes.plot(np.arange(0, 24, 2), [14, 9, 7, 5, 12, 19, 23, 26, 27, 24, 21, 19], '-o')
    axes.set_xticks(np.arange(0, 24, 2))
    axes.annotate('hottest at 16:00', xy=(16, 27), xytext=(16, 22),
                  arrowprops=dict(facecolor='black', shrink=0.2),
                  ha='center', va='center')
    axes.text(12, 10, 'Date: March 26th, 2018',
              bbox={'facecolor': 'cyan', 'alpha': 0.3, 'pad': 6})
    plt.show()

# ====================== 5. 直方图 ======================
def example_5_hist():
    data = np.random.standard_normal(1000)
    fig, axes = plt.subplots()
    axes.hist(data, bins=50)
    axes.set_title('histogram')
    plt.show()

# ====================== 6. 直方图+拟合曲线 ======================
def example_6_hist_fit():
    data = np.random.standard_normal(1000)
    fig, axes = plt.subplots()
    n, bins, patches = axes.hist(data, bins=50, density=True)
    y = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * bins ** 2)
    axes.plot(bins, y, '--')
    plt.show()

# ====================== 7. 基础散点图 ======================
def example_7_scatter_basic():
    N = 60
    np.random.seed(100)
    x = np.random.rand(N)
    y = np.random.rand(N)
    fig, axes = plt.subplots()
    axes.scatter(x, y)
    plt.show()

# ====================== 8. 高级散点图 ======================
def example_8_scatter_advanced():
    N = 60
    np.random.seed(100)
    x = np.random.rand(N)
    y = np.random.rand(N)
    s = np.pi * (10 * np.random.rand(N)) ** 2
    c = -s
    fig, axes = plt.subplots()
    axes.scatter(x, y, s, c, alpha=0.7)
    plt.show()

# ====================== 9. 分组柱状图 ======================
def example_9_bar_group():
    fig, axes = plt.subplots()
    data_m = (40, 60, 120, 180, 20, 200)
    data_f = (30, 100, 150, 30, 20, 50)
    index = np.arange(6)
    width = 0.4
    axes.bar(index, data_m, width, color='c', label='men')
    axes.bar(index + width, data_f, width, color='b', label='women')
    axes.set_xticks(index + width / 2)
    axes.set_xticklabels(('Taxi', 'Metro', 'Walk', 'Bus', 'Bicycle', 'Driving'))
    axes.legend()
    plt.show()

# ====================== 10. 饼图 ======================
def example_10_pie():
    fig, axes = plt.subplots()
    labels = ['Taxi', 'Metro', 'Walk', 'Bus', 'Bicycle', 'Driving']
    sizes = [10, 30, 5, 25, 5, 25]
    explode = (0, 0.1, 0, 0, 0, 0)
    axes.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    axes.axis('equal')
    axes.set_title('pie chart')
    plt.show()

# ====================== 11. 重叠柱状图 ======================
def example_11_bar_overlap():
    fig, axes = plt.subplots()
    data_m = (40, 60, 120, 180, 20, 200)
    data_f = (30, 100, 150, 30, 20, 50)
    index = np.arange(6)
    width = 0.4
    axes.bar(index, data_m, width, color='c', align='center', alpha=0.4, label='men')
    axes.bar(index, data_f, width, color='b', align='edge', alpha=0.4, label='women')
    axes.set_xticks(index + width / 2)
    axes.set_xticklabels(('Taxi', 'Metro', 'Walk', 'Bus', 'Bicycle', 'Driving'))
    axes.legend()
    plt.show()

# ====================== 12. 水平柱状图 ======================
def example_12_barh():
    fig, axes = plt.subplots()
    data_m = (40, 60, 120, 180, 20, 200)
    data_f = (30, 100, 150, 30, 20, 50)
    index = np.arange(6)
    width = 0.4
    axes.barh(index, data_m, width, color='c', align='center', alpha=0.4, label='men')
    axes.barh(index + width, data_f, width, color='b', align='edge', alpha=0.4, label='women')
    axes.set_yticks(index + width / 2)
    axes.set_yticklabels(('Taxi', 'Metro', 'Walk', 'Bus', 'Bicycle', 'Driving'))
    axes.legend()
    plt.show()

# ====================== 13. 折线图 ======================
def example_13_plot_lines():
    fig, axes = plt.subplots()
    x = np.arange(0, 10, 1)
    y1 = np.random.rand(10)
    y2 = np.random.rand(10)
    axes.plot(x, y1, '-o', color='c')
    axes.plot(x, y2, '--o', color='b')
    plt.show()

# ====================== 14. 柱状图+表格 ======================
def example_14_bar_table():
    fig, axes = plt.subplots()
    data_m = (40, 60, 120, 180, 20, 200)
    data_f = (30, 100, 150, 30, 20, 50)
    index = np.arange(6)
    width = 0.4
    axes.bar(index, data_m, width, color='c', label='men')
    axes.bar(index, data_f, width, color='b', bottom=data_m, label='women')
    axes.set_xticks([])
    axes.legend()
    data = [data_m, data_f]
    rows = ['male', 'female']
    cols = ['Taxi', 'Metro', 'Walk', 'Bus', 'Bicycle', 'Driving']
    axes.table(cellText=data, rowLabels=rows, colLabels=cols, loc='bottom')
    plt.show()

# ====================== 15. 极坐标双纽线 ======================
def example_15_polar():
    fig, axes = plt.subplots(subplot_kw={'projection': 'polar'})
    theta = np.arange(0, 2 * np.pi, 0.01)
    r = 2 * np.cos(2 * theta)
    axes.plot(theta, r)
    axes.set_rticks([])
    plt.show()

# ====================== 16. 3D散点图 ======================
def example_16_3d_scatter():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    N = 60
    np.random.seed(100)
    x = np.random.rand(N)
    y = np.random.rand(N)
    z = np.random.rand(N)
    ax.scatter(x, y, z)
    plt.show()

# ====================== 主运行 ======================
if __name__ == '__main__':
    # 运行任意一个例子，把函数注释去掉即可
     example_1_subplots()
    # example_2_line_style()
    # example_3_axis_spine()
    # example_4_annotate()
    # example_5_hist()
    # example_6_hist_fit()
    # example_7_scatter_basic()
    # example_8_scatter_advanced()
    # example_9_bar_group()
    # example_10_pie()
    # example_11_bar_overlap()
    # example_12_barh()
    # example_13_plot_lines()
    # example_14_bar_table()
    # example_15_polar()
    # example_16_3d_scatter()