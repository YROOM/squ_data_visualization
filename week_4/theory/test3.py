#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Seaborn数据可视化 - 第二课时：常用图形与统计可视化
包含所有PPT内容：直方图、密度图、散点图、箱线图、小提琴图、散点图矩阵、热力图、回归图、关系图等
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
import matplotlib.font_manager as fm
warnings.filterwarnings('ignore')

# ============================================================================
# 0. 中文设置（根据你的系统选择一行）
# ============================================================================

font_path = 'C:/Windows/Fonts/simhei.ttf'  # 黑体文件路径（确保这个文件存在）
# 加载字体并获取字体属性
font_prop = fm.FontProperties(fname=font_path)
font_name = font_prop.get_name()  # 获取字体名称
# ============================================================================
# 1. 环境设置与数据加载
# ============================================================================

print("=" * 80)
print("Seaborn数据可视化 - 第二课时")
print("=" * 80)

# 设置Seaborn主题
sns.set_theme(style='whitegrid', context='notebook', palette='deep',font=font_name)

# 加载数据集
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')
penguins = sns.load_dataset('penguins')

print(f"\n数据集信息:")
print(f"  Tips数据集: {tips.shape}")
print(f"  Iris数据集: {iris.shape}")
print(f"  Penguins数据集: {penguins.shape}")
print("=" * 80)


# ============================================================================
# 2. 直方图和密度曲线图 (PPT 7.3.1)
# ============================================================================

def plot_distribution():
    """
    直方图和密度曲线图
    对应PPT内容：distplot、kdeplot、rugplot
    """

    print("\n" + "=" * 80)
    print("2. 直方图和密度曲线图")
    print("=" * 80)

    # 2.1 基础直方图 + 密度曲线
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))

    # 直方图
    sns.histplot(tips['total_bill'], bins=20, ax=axes[0, 0])
    axes[0, 0].set_title('直方图', fontsize=14)

    # 直方图 + 密度曲线
    sns.histplot(tips['total_bill'], bins=20, kde=True, ax=axes[0, 1])
    axes[0, 1].set_title('直方图 + 密度曲线', fontsize=14)

    # 密度曲线（kdeplot）
    sns.kdeplot(tips['total_bill'], fill=True, ax=axes[0, 2])
    axes[0, 2].set_title('密度曲线 (kdeplot)', fontsize=14)

    # 毛毯图（rugplot）
    sns.kdeplot(tips['total_bill'], fill=True, alpha=0.6, ax=axes[1, 0])
    sns.rugplot(tips['total_bill'], color='red', height=0.05, ax=axes[1, 0])
    axes[1, 0].set_title('密度曲线 + 毛毯图', fontsize=14)

    # 分组密度图
    sns.kdeplot(data=tips, x='total_bill', hue='sex', fill=True, alpha=0.5, ax=axes[1, 1])
    axes[1, 1].set_title('分组密度图 (按性别)', fontsize=14)

    # Iris数据集分布
    sns.kdeplot(data=iris, x='petal_length', hue='species', fill=True, alpha=0.5, ax=axes[1, 2])
    axes[1, 2].set_title('Iris花瓣长度分布', fontsize=14)

    plt.tight_layout()
    plt.show()

    # 2.2 示例：iris数据集中Petal.Width的分布（对应PPT例7-15）
    print("\n【示例】iris数据集中Petal.Width的分布")
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    sns.histplot(iris['petal_width'], bins=20)
    plt.title('直方图')

    plt.subplot(1, 3, 2)
    sns.kdeplot(iris['petal_width'], fill=True)
    plt.title('密度曲线')

    plt.subplot(1, 3, 3)
    sns.histplot(iris['petal_width'], bins=20, kde=True)
    sns.rugplot(iris['petal_width'], color='red')
    plt.title('直方图+密度+毛毯图')

    plt.tight_layout()
    plt.show()


# ============================================================================
# 3. 散点图 (PPT 7.3.2)
# ============================================================================

def plot_scatter():
    """
    散点图
    对应PPT内容：stripplot、swarmplot、jitter参数
    """

    print("\n" + "=" * 80)
    print("3. 散点图")
    print("=" * 80)

    # 3.1 基础散点图
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex', size='size', sizes=(50, 200))
    plt.title('散点图：小费 vs 总账单（颜色=性别，大小=人数）', fontsize=14)
    plt.xlabel('总账单金额($)')
    plt.ylabel('小费金额($)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

    # 3.2 stripplot（各变量在每个类别的值）- 对应PPT例7-19
    print("\n【示例】stripplot: 显示Petal.Width在Species上的分布")
    plt.figure(figsize=(10, 5))
    sns.stripplot(x='species', y='petal_width', data=iris)
    plt.title('stripplot: 花瓣宽度在不同物种上的分布')
    plt.show()

    # 3.3 添加抖动（jitter=True）- 对应PPT例7-20
    plt.figure(figsize=(10, 5))
    sns.stripplot(x='species', y='petal_width', data=iris, jitter=True, alpha=0.6)
    plt.title('stripplot + 抖动 (jitter=True)')
    plt.show()

    # 3.4 swarmplot（自动避免重叠）- 对应PPT例7-21
    plt.figure(figsize=(10, 5))
    sns.swarmplot(x='species', y='petal_width', data=iris, hue='species')
    plt.title('swarmplot: 自动避免重叠')
    plt.show()

    # 3.5 对比stripplot和swarmplot
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, alpha=0.6, ax=axes[0])
    axes[0].set_title('stripplot (带抖动)')

    sns.swarmplot(x='day', y='total_bill', data=tips, ax=axes[1])
    axes[1].set_title('swarmplot (自动排列)')

    plt.tight_layout()
    plt.show()


# ============================================================================
# 4. 箱线图 (PPT 7.3.3)
# ============================================================================

def plot_boxplot():
    """
    箱线图
    对应PPT内容：boxplot
    """

    print("\n" + "=" * 80)
    print("4. 箱线图")
    print("=" * 80)

    # 4.1 基础箱线图 - 对应PPT例7-22
    plt.figure(figsize=(10, 5))
    sns.boxplot(x='species', y='petal_width', data=iris)
    plt.title('箱线图：不同物种的花瓣宽度分布')
    plt.show()

    # 4.2 分组箱线图
    plt.figure(figsize=(10, 5))
    sns.boxplot(x='day', y='total_bill', hue='sex', data=tips)
    plt.title('箱线图：不同星期的小费分布（按性别分组）')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

    # 4.3 带缺口的箱线图（用于比较中位数）
    plt.figure(figsize=(10, 5))
    sns.boxplot(x='day', y='total_bill', data=tips, notch=True)
    plt.title('箱线图（带缺口）：缺口表示中位数的置信区间')
    plt.show()


# ============================================================================
# 5. 散点图矩阵 (PPT 7.3.4)
# ============================================================================

def plot_pairplot():
    """
    散点图矩阵
    对应PPT内容：pairplot
    """

    print("\n" + "=" * 80)
    print("5. 散点图矩阵 (pairplot)")
    print("=" * 80)

    # 5.1 基础散点图矩阵 - 对应PPT例7-23
    print("\n【示例】iris数据集散点图矩阵")
    sns.pairplot(iris, hue='species')
    plt.suptitle('散点图矩阵：iris数据集特征两两关系', y=1.02, fontsize=14)
    plt.show()

    # 5.2 指定部分特征
    print("\n【示例】仅选择部分特征")
    sns.pairplot(iris, vars=['sepal_length', 'sepal_width', 'petal_length'], hue='species')
    plt.suptitle('散点图矩阵：部分特征', y=1.02, fontsize=14)
    plt.show()

    # 5.3 定制化散点图矩阵
    g = sns.pairplot(iris,
                     vars=['sepal_length', 'petal_length'],
                     hue='species',
                     diag_kind='kde',
                     markers=['o', 's', 'D'],
                     height=3)
    plt.suptitle('定制化散点图矩阵', y=1.02, fontsize=14)
    plt.show()


# ============================================================================
# 6. 小提琴图 (PPT 7.3.5)
# ============================================================================

def plot_violinplot():
    """
    小提琴图（箱线图+核密度图）
    对应PPT内容：violinplot
    """

    print("\n" + "=" * 80)
    print("6. 小提琴图 (violinplot)")
    print("=" * 80)

    # 6.1 基础小提琴图 - 对应PPT例7-24
    plt.figure(figsize=(10, 5))
    sns.violinplot(x='species', y='petal_length', data=iris)
    plt.title('小提琴图：不同物种的花瓣长度分布')
    plt.show()

    # 6.2 分割小提琴图（对比两组数据）
    plt.figure(figsize=(10, 5))
    sns.violinplot(x='day', y='total_bill', hue='sex', data=tips, split=True)
    plt.title('分割小提琴图：对比男女性别')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

    # 6.3 带内部箱线图的小提琴图
    plt.figure(figsize=(10, 5))
    sns.violinplot(x='day', y='total_bill', data=tips, inner='box')
    plt.title('小提琴图（内部显示箱线图）')
    plt.show()


# ============================================================================
# 7. 柱状图 (PPT 7.3.6)
# ============================================================================

def plot_barplot():
    """
    柱状图
    对应PPT内容：barplot、countplot
    """

    print("\n" + "=" * 80)
    print("7. 柱状图")
    print("=" * 80)

    # 7.1 barplot（默认显示均值）
    plt.figure(figsize=(10, 5))
    sns.barplot(x='day', y='total_bill', data=tips)
    plt.title('barplot：不同星期的平均总账单')
    plt.show()

    # 7.2 分组barplot
    plt.figure(figsize=(10, 5))
    sns.barplot(x='day', y='total_bill', hue='sex', data=tips)
    plt.title('barplot：不同星期的平均总账单（按性别分组）')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

    # 7.3 countplot（计数图）
    plt.figure(figsize=(10, 5))
    sns.countplot(x='day', data=tips)
    plt.title('countplot：不同星期的订单数量')
    plt.show()

    # 7.4 分组countplot
    plt.figure(figsize=(10, 5))
    sns.countplot(x='day', hue='sex', data=tips)
    plt.title('countplot：不同星期的订单数量（按性别分组）')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()


# ============================================================================
# 8. 多变量图 (PPT 7.3.7)
# ============================================================================

def plot_jointplot():
    """
    多变量图（联合分布图）
    对应PPT内容：jointplot
    """

    print("\n" + "=" * 80)
    print("8. 多变量图 (jointplot)")
    print("=" * 80)

    # 8.1 散点图 + 直方图
    g = sns.jointplot(data=tips, x='total_bill', y='tip', kind='scatter')
    g.fig.suptitle('联合分布图：散点图 + 直方图', y=1.02)
    plt.show()

    # 8.2 密度图 + 等高线（kind='kde'）
    g = sns.jointplot(data=tips, x='total_bill', y='tip', kind='kde', fill=True)
    g.fig.suptitle('联合分布图：密度等高线图', y=1.02)
    plt.show()

    # 8.3 六边形图（适合大数据量）
    g = sns.jointplot(data=tips, x='total_bill', y='tip', kind='hex')
    g.fig.suptitle('联合分布图：六边形图', y=1.02)
    plt.show()

    # 8.4 回归图
    g = sns.jointplot(data=tips, x='total_bill', y='tip', kind='reg')
    g.fig.suptitle('联合分布图：带回归线', y=1.02)
    plt.show()


# ============================================================================
# 9. 回归图 (PPT 7.3.8)
# ============================================================================

def plot_regplot():
    """
    回归图
    对应PPT内容：regplot、lmplot
    """

    print("\n" + "=" * 80)
    print("9. 回归图")
    print("=" * 80)

    # 9.1 基础回归图 (regplot)
    plt.figure(figsize=(10, 6))
    sns.regplot(data=tips, x='total_bill', y='tip',
                scatter_kws={'alpha': 0.5},
                line_kws={'color': 'red', 'linewidth': 2})
    plt.title('regplot：小费与总账单的线性关系', fontsize=14)
    plt.xlabel('总账单金额($)')
    plt.ylabel('小费金额($)')
    plt.show()

    # 9.2 多项式回归 (order=2)
    plt.figure(figsize=(10, 6))
    sns.regplot(data=tips, x='total_bill', y='tip', order=2,
                scatter_kws={'alpha': 0.5},
                line_kws={'color': 'red', 'linewidth': 2})
    plt.title('regplot：二阶多项式回归', fontsize=14)
    plt.show()

    # 9.3 分组回归图 (lmplot)
    g = sns.lmplot(data=tips, x='total_bill', y='tip', hue='sex', col='time',
                   height=4, aspect=1.2)
    g.fig.suptitle('lmplot：分组回归分析', y=1.02)
    plt.show()


# ============================================================================
# 10. 关系类图 (PPT 7.3.9)
# ============================================================================

def plot_relplot():
    """
    关系类图
    对应PPT内容：relplot（scatter和line）
    """

    print("\n" + "=" * 80)
    print("10. 关系类图 (relplot)")
    print("=" * 80)

    # 10.1 散点图类型 - 对应PPT例7-30
    g = sns.relplot(data=tips, x='total_bill', y='tip',
                    hue='sex', size='size', sizes=(50, 200),
                    kind='scatter', height=5, aspect=1.2)
    g.fig.suptitle('relplot：散点图（小费总额 vs 小费）', y=1.02)
    plt.show()

    # 10.2 折线图类型
    # 创建时序数据
    np.random.seed(42)
    dates = pd.date_range('2023-01-01', periods=50, freq='D')
    time_data = pd.DataFrame({
        'date': dates,
        'value': np.cumsum(np.random.randn(50)),
        'category': np.random.choice(['A', 'B'], 50)
    })

    g = sns.relplot(data=time_data, x='date', y='value',
                    hue='category', kind='line', height=5, aspect=1.5)
    g.fig.suptitle('relplot：折线图（时间序列）', y=1.02)
    plt.xticks(rotation=45)
    plt.show()


# ============================================================================
# 11. 热力图 (PPT 7.3.10)
# ============================================================================

def plot_heatmap():
    """
    热力图
    对应PPT内容：heatmap
    """

    print("\n" + "=" * 80)
    print("11. 热力图 (heatmap)")
    print("=" * 80)

    # 11.1 基础热力图
    # 计算相关系数矩阵
    numeric_cols = tips.select_dtypes(include=[np.number]).columns
    corr = tips[numeric_cols].corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0)
    plt.title('热力图：Tips数据集相关系数矩阵', fontsize=14)
    plt.show()

    # 11.2 定制化热力图
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr,
                annot=True,  # 显示数值
                fmt='.2f',  # 数值格式
                cmap='RdBu_r',  # 颜色映射
                center=0,  # 中心值
                square=True,  # 正方形单元格
                linewidths=0.5,  # 单元格分隔线宽度
                cbar_kws={'shrink': 0.8},  # 颜色条缩放
                annot_kws={'size': 10})  # 注释字体大小
    plt.title('定制化热力图', fontsize=14)
    plt.show()

    # 11.3 Iris数据集热力图
    iris_numeric = iris.select_dtypes(include=[np.number])
    iris_corr = iris_numeric.corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(iris_corr, annot=True, fmt='.2f', cmap='viridis',
                square=True, linewidths=0.5)
    plt.title('热力图：Iris数据集相关系数矩阵', fontsize=14)
    plt.show()


# ============================================================================
# 12. 综合案例：多图层组合图
# ============================================================================

def composite_plot():
    """
    综合案例：一张图包含多种图形
    """

    print("\n" + "=" * 80)
    print("12. 综合案例：多图层组合图")
    print("=" * 80)

    # 创建画布
    fig = plt.figure(figsize=(16, 12))

    # 1. 主图：小提琴图
    ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
    sns.violinplot(data=tips, x='day', y='total_bill', hue='sex', split=True, ax=ax1)
    ax1.set_title('总账单金额分布（按星期和性别）', fontsize=14)
    ax1.set_xlabel('星期')
    ax1.set_ylabel('总账单金额($)')
    ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    # 2. 右上：箱线图
    ax2 = plt.subplot2grid((3, 3), (0, 2))
    sns.boxplot(data=tips, y='total_bill', ax=ax2)
    ax2.set_title('总账单金额整体分布', fontsize=14)
    ax2.set_ylabel('总账单金额($)')

    # 3. 左下：散点图 + 回归
    ax3 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
    sns.regplot(data=tips, x='total_bill', y='tip', scatter_kws={'alpha': 0.5}, ax=ax3)
    ax3.set_title('小费与总账单的关系（带回归线）', fontsize=14)
    ax3.set_xlabel('总账单金额($)')
    ax3.set_ylabel('小费金额($)')

    # 4. 右下：热力图
    ax4 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
    numeric_cols = tips.select_dtypes(include=[np.number]).columns
    corr = tips[numeric_cols].corr()
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0, ax=ax4, square=True)
    ax4.set_title('相关系数矩阵', fontsize=14)

    # 5. 底部：计数图
    ax5 = plt.subplot2grid((3, 3), (2, 0), colspan=2)
    sns.countplot(data=tips, x='time', hue='sex', ax=ax5)
    ax5.set_title('用餐时段与性别分布', fontsize=14)
    ax5.set_xlabel('用餐时段')
    ax5.set_ylabel('数量')
    ax5.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()
    plt.show()


# ============================================================================
# 13. 新旧版本对比总结
# ============================================================================

def version_comparison_summary():
    """
    新旧版本对比
    """

    print("\n" + "=" * 80)
    print("13. 新旧版本API对比总结")
    print("=" * 80)

    print("\n【主要变化】")
    print("-" * 60)
    print("| 图形类型 | 旧版本 (<0.12) | 新版本 (≥0.12) |")
    print("|----------|----------------|----------------|")
    print("| 直方图+密度 | distplot() | histplot() / kdeplot() |")
    print("| 分类图 | factorplot() | catplot() |")
    print("| 关系图 | relplot() | relplot() (增强) |")
    print("| 联合分布 | jointplot() | jointplot() (kind参数增强) |")
    print("| 多变量图 | pairplot() | pairplot() (性能优化) |")

    print("\n【迁移示例】")
    print("-" * 60)
    print("# 旧版代码")
    print("sns.distplot(tips['total_bill'], bins=20, kde=True, rug=True)")
    print()
    print("# 新版代码")
    print("sns.histplot(tips['total_bill'], bins=20, kde=True)")
    print("sns.rugplot(tips['total_bill'])")
    print()
    print("# 旧版代码")
    print("sns.factorplot(x='day', y='total_bill', data=tips, kind='box')")
    print()
    print("# 新版代码")
    print("sns.catplot(x='day', y='total_bill', data=tips, kind='box')")


# ============================================================================
# 主程序：运行所有图形
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("Seaborn数据可视化 - 第二课时")
    print("主题：常用图形与统计可视化")
    print("=" * 80)

    # 运行各个图形函数
    # plot_distribution()  # 2. 直方图和密度曲线图
    #plot_scatter()  # 3. 散点图
    # plot_boxplot()  # 4. 箱线图
    # plot_pairplot()  # 5. 散点图矩阵
    #plot_violinplot()  # 6. 小提琴图
    # plot_barplot()  # 7. 柱状图
    # plot_jointplot()  # 8. 多变量图
    # plot_regplot()  # 9. 回归图
   # plot_relplot()  # 10. 关系类图
    plot_heatmap()  # 11. 热力图
    # composite_plot()  # 12. 综合案例
    # version_comparison_summary()  # 13. 新旧版本对比

    print("\n" + "=" * 80)
    print("第二课时完成！")
    print("=" * 80)