#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Seaborn数据可视化 - 第一课时：Seaborn基础与视觉美学
包含主要方法的详细参数解释 + 新旧版本对比
"""


import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.font_manager as fm
from matplotlib import font_manager
warnings.filterwarnings('ignore')

# ============================================================================
# 0. 版本检查与说明
# ============================================================================

print("=" * 80)
print("Seaborn版本信息与新旧版本对比说明")
print("=" * 80)
print(f"当前Seaborn版本: {sns.__version__}")
print(f"当前Matplotlib版本: {plt.matplotlib.__version__}")

# 判断版本
is_new_version = float(sns.__version__.split('.')[0]) >= 0.12
print(f"\n版本类型: {'新版 (≥0.12)' if is_new_version else '旧版 (<0.12)'}")
print("=" * 80)

print("\n【新旧版本主要区别】")
print("-" * 60)
print("1. 全局设置函数:")
print("   旧版: sns.set(), sns.set_style(), sns.set_context(), sns.set_palette()")
print("   新版: sns.set_theme() 统一管理所有设置")
print()
print("2. 直方图函数:")
print("   旧版: sns.distplot() (已废弃)")
print("   新版: sns.histplot() 和 sns.kdeplot()")
print()
print("3. 分类图函数:")
print("   旧版: sns.factorplot() (已废弃)")
print("   新版: sns.catplot()")
print()
print("4. 热力图:")
print("   新版增加更多参数: annot_kws, cbar_kws, square等")
print("=" * 80)

# ============================================================================
# 1. 环境设置
# ============================================================================
# ========== 核心：指定字体文件路径 ==========
# Windows 系统黑体（SimHei）的默认路径（复制直接用）
# 1. 指定系统字体文件路径（Windows 必生效）
font_path = 'C:/Windows/Fonts/simhei.ttf'  # 黑体文件路径（确保这个文件存在）
# 加载字体并获取字体属性
font_prop = fm.FontProperties(fname=font_path)
font_name = font_prop.get_name()  # 获取字体名称

# 2. 全局配置（先于 Seaborn 设置，避免被覆盖）
plt.rcParams.update({
    'font.family': font_name,          # 全局字体
    'axes.unicode_minus': False,       # 解决负号显示
    'font.sans-serif': [font_name],    # 兜底字体列表
})

# ====================== 第二步：Seaborn 设置（兼容中文） ======================
# 关键：Seaborn set_theme 中显式指定中文字体
# sns.set_theme(
#     style='darkgrid',
#     context='notebook',
#     palette='deep',
#     font=font_name,  # 核心！告诉 Seaborn 使用我们的中文字体
#     font_scale=1
# )

# # 设置中文字体（解决中文显示问题）
# plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
# plt.rcParams['axes.unicode_minus'] = False
#

# # 创建示例数据
x = np.linspace(0, 10, 100)
y = np.sin(x)
y_cos = np.cos(x)


# ============================================================================
# 2. set_theme() vs set() - 全局设置对比
# ============================================================================

def compare_global_settings():
    """
    对比新旧版本的全局设置方法
    """

    print("\n" + "=" * 80)
    print("【新旧版本对比】全局设置函数")
    print("=" * 80)

    print("\n旧版方式 (sns.set() + 多个单独设置):")
    print("-" * 60)
    print("""
    # 旧版代码示例
    sns.set()                      # 基础设置
    sns.set_style('darkgrid')      # 设置主题
    sns.set_context('notebook')    # 设置上下文
    sns.set_palette('deep')        # 设置调色板
    """)

    print("\n新版方式 (sns.set_theme() 统一设置):")
    print("-" * 60)
    print("""
    # 新版推荐写法
    sns.set_theme(
        style='darkgrid',    # 主题风格
        context='notebook',  # 缩放上下文
        palette='deep',      # 调色板
        font='sans-serif',   # 字体
        font_scale=1,        # 字体缩放
        color_codes=True,    # 颜色代码
        rc=None              # 额外rc参数
    )
    """)

    # 演示新版设置
    print("\n【新版设置示例】")
    # sns.set_theme(style='darkgrid', context='notebook', palette='deep')
    sns.set_theme(
        style='darkgrid',
        context='notebook',
        palette='deep',
        font=font_name,  # 核心！告诉 Seaborn 使用我们的中文字体
        font_scale=1
    )

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, linewidth=2, label='sin(x)')
    plt.title('新版 sns.set_theme() 统一设置示例')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


def explain_set_theme():
    """
    sns.set_theme() 参数详解（新版推荐）

    参数详解：
    ----------
    context : str or dict, default='notebook'
        设置绘图元素的缩放比例。可选值：
        - 'paper': 适合论文插图（最小）
        - 'notebook': 适合Jupyter Notebook（默认）
        - 'talk': 适合演讲幻灯片（较大）
        - 'poster': 适合海报展示（最大）

    style : str or dict, default='darkgrid'
        设置绘图的主题风格。可选值：
        - 'darkgrid': 深色网格背景（默认）
        - 'whitegrid': 白色网格背景
        - 'dark': 深色无网格
        - 'white': 白色无网格
        - 'ticks': 白底+刻度线

    palette : str or dict, default='deep'
        设置调色板。常用值：
        - 'deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind'
        - 'husl', 'hls', 'viridis', 'plasma', 'magma', 'inferno', 'cividis'
        - 也可以传入自定义颜色列表

    font : str, default='sans-serif'
        设置字体家族

    font_scale : float, default=1
        字体缩放比例

    color_codes : bool, default=True
        是否自动将颜色代码转换为实际颜色

    rc : dict, optional
        传递给matplotlib的rc参数，用于精细控制
    """

    print("\n" + "=" * 80)
    print("sns.set_theme() 参数详解（新版推荐）")
    print("=" * 80)

    print("【参数说明】")
    print("-" * 60)
    print("context: 设置绘图元素缩放比例")
    print("  - paper: 论文级别（最小）")
    print("  - notebook: Jupyter级别（默认）")
    print("  - talk: 演讲级别（较大）")
    print("  - poster: 海报级别（最大）")
    print()
    print("style: 设置主题风格")
    print("  - darkgrid: 深色网格（默认）")
    print("  - whitegrid: 白色网格")
    print("  - dark: 深色无网格")
    print("  - white: 白色无网格")
    print("  - ticks: 白底+刻度线")
    print()
    print("palette: 设置调色板")
    print("  - 分类调色板: deep, muted, pastel, bright, dark, colorblind")
    print("  - 连续调色板: viridis, plasma, magma, inferno, cividis")
    print("  - 循环调色板: husl, hls")
    print()
    print("font_scale: 字体缩放比例（1为基准）")
    print("color_codes: 是否自动转换颜色代码")
    print("=" * 80)

    # 示例：不同context对比
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    contexts = ['paper', 'notebook', 'talk', 'poster']

    for ax, context in zip(axes.flatten(), contexts):
        sns.set_theme(style='whitegrid', context=context, palette='deep')
        ax.plot(x, y, linewidth=2, label='sin(x)')
        ax.set_title(f'context="{context}"', fontsize=12, pad=10)
        ax.set_xlabel('X轴标签')
        ax.set_ylabel('Y轴标签')
        ax.legend()

    plt.tight_layout()
    plt.show()

    # 恢复默认
   # sns.set_theme(style='darkgrid', context='notebook')


# ============================================================================
# 3. set_style() vs axes_style() - 主题设置对比
# ============================================================================

def compare_style_functions():
    """
    对比新旧版本的主题设置方法
    """

    print("\n" + "=" * 80)
    print("【新旧版本对比】主题设置函数")
    print("=" * 80)

    print("\n旧版方式:")
    print("-" * 60)
    print("""
    sns.set_style('darkgrid')     # 全局设置主题
    sns.axes_style()               # 获取当前主题参数
    """)

    print("\n新版方式:")
    print("-" * 60)
    print("""
    # 方式1: 通过 set_theme 设置
    sns.set_theme(style='darkgrid')

    # 方式2: 单独使用 set_style（仍然支持）
    sns.set_style('whitegrid')

    # 方式3: 临时使用（推荐）
    with sns.axes_style('dark'):
        plt.plot(x, y)
    """)


def explain_set_style():
    """
    sns.set_style() / sns.axes_style() 参数详解

    参数详解：
    ----------
    style : str or dict
        主题名称或自定义样式字典
        - 'darkgrid', 'whitegrid', 'dark', 'white', 'ticks'

    rc : dict, optional
        额外的rc参数字典，用于覆盖默认设置
        - 例如: {'axes.edgecolor': 'red', 'grid.color': 'gray'}
    """

    print("\n" + "=" * 80)
    print("sns.set_style() / sns.axes_style() 参数详解")
    print("=" * 80)

    print("【参数说明】")
    print("-" * 60)
    print("style: 主题风格")
    print("  - darkgrid: 深色网格背景（数据密集时推荐）")
    print("  - whitegrid: 白色网格背景（适合学术展示）")
    print("  - dark: 深色无网格（适合暗色背景）")
    print("  - white: 白色无网格（最简洁）")
    print("  - ticks: 白底+刻度线（出版级别）")
    print()
    print("rc: 额外配置，例如:")
    print("  {'axes.edgecolor': 'blue', 'grid.linestyle': '--'}")
    print("=" * 80)

    # 示例：5种主题对比
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()

    themes = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']

    for i, theme in enumerate(themes):
        with sns.axes_style(theme):
            axes[i].plot(x, y, linewidth=2)
            axes[i].set_title(f'主题：{theme}', fontsize=14, pad=10)
            axes[i].set_xlabel('X轴')
            axes[i].set_ylabel('Y轴')

    # 第6个展示自定义rc
    custom_style = {'axes.edgecolor': 'red', 'grid.linestyle': '--', 'grid.color': 'gray'}
    with sns.axes_style('white', rc=custom_style):
        axes[5].plot(x, y, linewidth=2)
        axes[5].set_title('自定义rc参数', fontsize=14, pad=10)
        axes[5].set_xlabel('X轴')
        axes[5].set_ylabel('Y轴')

    plt.tight_layout()
    plt.show()


# ============================================================================
# 4. despine() - 移除轴线（新旧版本基本一致）
# ============================================================================

def explain_despine():
    """
    sns.despine() 参数详解

    参数详解：
    ----------
    fig : matplotlib figure, optional
        指定要操作的图形对象，默认为当前图形

    ax : matplotlib axes, optional
        指定要操作的坐标轴对象，默认为当前坐标轴

    top : bool, default=True
        是否移除顶部轴线

    right : bool, default=True
        是否移除右侧轴线

    left : bool, default=True
        是否移除左侧轴线

    bottom : bool, default=True
        是否移除底部轴线

    offset : int or tuple, optional
        轴线偏移量，可以是单个数字或(top, right, bottom, left)元组

    trim : bool, default=False
        是否将轴线裁剪到数据范围内
    """

    print("\n" + "=" * 80)
    print("sns.despine() 参数详解")
    print("=" * 80)
    print("【参数说明】")
    print("-" * 60)
    print("top / right / left / bottom: 控制各边框是否移除")
    print("  - True: 移除该边框")
    print("  - False: 保留该边框")
    print()
    print("offset: 轴线偏移量")
    print("  - 数字: 所有边框偏移相同距离")
    print("  - 元组: (top, right, bottom, left) 分别设置")
    print()
    print("trim: 是否裁剪轴线到数据范围")
    print("  - True: 轴线只延伸到数据范围")
    print("  - False: 轴线延伸到整个坐标轴范围")
    print()
    print("【新旧版本对比】")
    print("-" * 60)
    print("despine() 函数在新旧版本中基本一致，无重大变化")
    print("=" * 80)

    # 示例1：基础despine
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    sns.set_style('white')

    # 原始图形
    axes[0].plot(x, y)
    axes[0].set_title('原始图形')

    # 移除上、右边框
    axes[1].plot(x, y)
    sns.despine(ax=axes[1])
    axes[1].set_title('移除上、右边框')

    # 完全控制轴线
    axes[2].plot(x, y)
    sns.despine(ax=axes[2], top=True, right=False, left=True, bottom=True)
    axes[2].set_title('全部舍弃')

    plt.tight_layout()
    plt.show()

    # 示例2：偏移与裁剪
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    # 偏移轴线
    axes[0].plot(x, y)
    sns.despine(ax=axes[0], offset=100)
    axes[0].set_title('轴线偏移10点')

    # 裁剪轴线
    axes[1].plot(x, y)
    sns.despine(ax=axes[1], trim=True)
    axes[1].set_title('裁剪超出范围的轴线')

    plt.tight_layout()
    plt.show()


# ============================================================================
# 5. set_context() - 上下文缩放（新旧版本基本一致）
# ============================================================================

def explain_set_context():
    """
    sns.set_context() 参数详解

    参数详解：
    ----------
    context : str or dict
        上下文名称或自定义字典。可选值：
        - 'paper': 论文级别（最小字体和线条）
        - 'notebook': Jupyter级别（默认）
        - 'talk': 演讲级别（较大字体和线条）
        - 'poster': 海报级别（最大字体和线条）

    font_scale : float, default=1
        字体缩放比例，1为基准

    rc : dict, optional
        额外的rc参数，用于精细控制
        - 'lines.linewidth': 线条宽度
        - 'axes.labelsize': 轴标签字体大小
        - 'xtick.labelsize': x轴刻度标签大小
        - 'ytick.labelsize': y轴刻度标签大小
        - 'legend.fontsize': 图例字体大小
    """

    print("\n" + "=" * 80)
    print("sns.set_context() 参数详解")
    print("=" * 80)
    print("【参数说明】")
    print("-" * 60)
    print("context: 上下文缩放级别")
    print("  - paper: 论文级别（最小）")
    print("  - notebook: Jupyter级别（默认）")
    print("  - talk: 演讲级别（较大）")
    print("  - poster: 海报级别（最大）")
    print()
    print("font_scale: 字体缩放比例")
    print("  - 1: 基准大小")
    print("  - 1.5: 放大1.5倍")
    print("  - 0.8: 缩小0.8倍")
    print()
    print("rc: 额外配置示例")
    print("  - rc={'lines.linewidth': 2, 'axes.labelsize': 12}")
    print()
    print("【新旧版本对比】")
    print("-" * 60)
    print("set_context() 在新旧版本中基本一致")
    print("新版推荐通过 set_theme(context='talk') 方式设置")
    print("=" * 80)

    # 示例：上下文对比
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    contexts = ['paper', 'notebook', 'talk', 'poster']

    for ax, context in zip(axes.flatten(), contexts):
        sns.set_context(context)
        ax.plot(x, y, linewidth=2, label='sin(x)')
        ax.set_title(f'上下文：{context}', fontsize=14, pad=10)
        ax.set_xlabel('X轴标签')
        ax.set_ylabel('Y轴标签')
        ax.legend(loc='upper right')

    plt.tight_layout()
    plt.show()

    # 恢复默认
    # sns.set_context('notebook')


# ============================================================================
# 6. 调色板设置 - palette对比
# ============================================================================

def compare_palette():
    """
    对比新旧版本的调色板设置
    """

    print("\n" + "=" * 80)
    print("【新旧版本对比】调色板设置")
    print("=" * 80)

    print("\n旧版方式:")
    print("-" * 60)
    print("""
    sns.set_palette('deep')        # 设置调色板
    sns.color_palette()             # 获取调色板
    sns.hls_palette(8)              # HLS调色板
    sns.husl_palette(8)             # HUSL调色板
    """)

    print("\n新版方式:")
    print("-" * 60)
    print("""
    # 方式1: 通过 set_theme 设置
    sns.set_theme(palette='viridis')

    # 方式2: 单独使用 set_palette（仍然支持）
    sns.set_palette('muted')

    # 新版新增调色板
    # - 'rocket', 'mako', 'flare', 'crest' 等新调色板
    """)


def show_palettes():
    """
    展示各种调色板
    """

    print("\n" + "=" * 80)
    print("【调色板示例】")
    print("=" * 80)

    # 分类调色板
    categorical_palettes = ['deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind']

    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    axes = axes.flatten()

    for i, palette in enumerate(categorical_palettes):
        colors = sns.color_palette(palette, 8)
        for j, color in enumerate(colors):
            axes[i].bar(j, 1, color=color)
        axes[i].set_title(f'{palette}', fontsize=12)
        axes[i].set_xticks([])
        axes[i].set_yticks([])

    plt.suptitle('分类调色板示例', fontsize=16)
    plt.tight_layout()
    plt.show()

    # 连续调色板
    sequential_palettes = ['viridis', 'plasma', 'magma', 'inferno', 'cividis', 'rocket']

    fig, axes = plt.subplots(2, 3, figsize=(15, 6))
    axes = axes.flatten()

    for i, palette in enumerate(sequential_palettes):
        colors = sns.color_palette(palette, 100)
        for j, color in enumerate(colors):
            axes[i].bar(j, 1, color=color)
        axes[i].set_title(f'{palette}', fontsize=12)
        axes[i].set_xticks([])
        axes[i].set_yticks([])

    plt.suptitle('连续调色板示例', fontsize=16)
    plt.tight_layout()
    plt.show()


# ============================================================================
# 7. 课堂练习
# ============================================================================

def classroom_exercise():
    """
    课堂练习：综合应用所学知识

    任务：
    1. 创建一个包含3个子图的图形
    2. 分别使用 whitegrid、dark、ticks 三种主题
    3. 每个子图绘制正弦曲线和余弦曲线
    4. 使用 despine 移除顶部和右侧轴线
    5. 添加图例和标题
    6. 分别使用旧版和新版方式实现
    """

    print("\n" + "=" * 80)
    print("课堂练习：新旧版本对比实现")
    print("=" * 80)

    print("\n【任务1：旧版方式实现】")
    print("-" * 60)

    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    themes = ['whitegrid', 'dark', 'ticks']

    for ax, theme in zip(axes, themes):
        sns.set_style(theme)
        ax.plot(x, y, label='sin(x)', linewidth=2)
        ax.plot(x, y_cos, label='cos(x)', linewidth=2)
        ax.set_title(f'主题：{theme}（旧版）', fontsize=12)
        ax.set_xlabel('X轴')
        ax.set_ylabel('Y轴')
        ax.legend()
        sns.despine(ax=ax, top=True, right=True)

    plt.tight_layout()
    plt.show()

    print("\n【任务2：新版方式实现】")
    print("-" * 60)

    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    for ax, theme in zip(axes, themes):
        with sns.axes_style(theme):
            ax.plot(x, y, label='sin(x)', linewidth=2)
            ax.plot(x, y_cos, label='cos(x)', linewidth=2)
            ax.set_title(f'主题：{theme}（新版）', fontsize=12)
            ax.set_xlabel('X轴')
            ax.set_ylabel('Y轴')
            ax.legend()
            sns.despine(ax=ax, top=True, right=True)

    plt.tight_layout()
    plt.show()

    print("\n练习完成！")
    print("总结：")
    print("  - 旧版使用 sns.set_style() 全局设置")
    print("  - 新版推荐使用 with sns.axes_style() 临时设置")


# ============================================================================
# 主程序
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("Seaborn数据可视化 - 第一课时")
    print("主题：Seaborn基础与视觉美学（含新旧版本对比）")
    print("=" * 80)

    # 运行各个讲解函数
    # compare_global_settings()
    # explain_set_theme()
    # compare_style_functions()
    # explain_set_style()
    # explain_despine()
    # explain_set_context()
    # compare_palette()
    show_palettes()
    # classroom_exercise()

