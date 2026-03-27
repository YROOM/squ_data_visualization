import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.font_manager as fm

# 忽略警告，避免干扰讲解
warnings.filterwarnings('ignore')

# ============================================================================
# 0. 版本检查与说明（保留你的逻辑）
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
# 1. 中文显示核心配置（移到最前，优先于所有Seaborn设置）
# ============================================================================
# 1.1 指定Windows系统黑体文件路径（必存在）
font_path = 'C:/Windows/Fonts/simhei.ttf'  # 黑体文件路径
font_prop = fm.FontProperties(fname=font_path)  # 加载字体文件
font_name = font_prop.get_name()  # 获取字体名称

# 1.2 全局Matplotlib配置（一次性更新，避免重复）
plt.rcParams.update({
    'font.family': font_name,  # 全局字体
    'axes.unicode_minus': False,  # 解决负号显示为方块
    'font.sans-serif': [font_name],  # 兜底字体列表
    'figure.figsize': (10, 6),  # 全局图表大小（可选）
})

# 1.3 Seaborn全局设置（仅调用一次，避免覆盖）
sns.set_theme(
    style='darkgrid',
    context='notebook',
    palette='deep',
    font=font_name,  # 关键：告诉Seaborn使用中文字体
    font_scale=1.1  # 字体缩放，提升可读性
)

# ============================================================================
# 2. 生成示例数据
# ============================================================================
x = np.linspace(0, 10, 100)
y = np.sin(x)
y_cos = np.cos(x)


# ============================================================================
# 3. set_theme() vs set() - 全局设置对比（修改中文显示逻辑）
# ============================================================================
def compare_global_settings():
    """
    对比新旧版本的全局设置方法（含中文显示）
    """
    print("\n" + "=" * 80)
    print("【新旧版本对比】全局设置函数")
    print("=" * 80)

    print("\n旧版方式 (sns.set() + 多个单独设置):")
    print("-" * 60)
    print("""
    # 旧版代码示例（Seaborn < 0.11）
    sns.set()                      # 基础设置
    sns.set_style('darkgrid')      # 设置主题
    sns.set_context('notebook')    # 设置上下文
    sns.set_palette('deep')        # 设置调色板
    # 旧版中文适配（需手动加，易被覆盖）
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    """)

    print("\n新版方式 (sns.set_theme() 统一设置 + 中文适配):")
    print("-" * 60)
    print(f"""
    # 新版推荐写法（Seaborn ≥ 0.11）
    # 1. 先加载中文字体文件（解决名称识别问题）
    font_path = 'C:/Windows/Fonts/simhei.ttf'
    font_prop = fm.FontProperties(fname=font_path)
    font_name = font_prop.get_name()

    # 2. 全局配置
    plt.rcParams['font.family'] = font_name
    plt.rcParams['axes.unicode_minus'] = False

    # 3. set_theme 中显式指定中文字体（核心区别）
    sns.set_theme(
        style='darkgrid',    # 主题风格
        context='notebook',  # 缩放上下文
        palette='deep',      # 调色板
        font=font_name,      # 新版新增：直接指定中文字体
        font_scale=1         # 字体缩放
    )
    """)

    # 演示新版设置（不再重复调用set_theme，避免覆盖）
    print("\n【新版设置示例（中文生效）】")
    # 创建图表（所有中文文本显式绑定字体）
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, linewidth=2, label='sin(x) - 正弦曲线')
    plt.plot(x, y_cos, linewidth=2, label='cos(x) - 余弦曲线', linestyle='--')

    # 核心：所有中文文本显式指定字体
    plt.title('新版 sns.set_theme() 统一设置示例（含中文）', fontproperties=font_prop, fontsize=14)
    plt.xlabel('X轴 - 数值范围（0-10）', fontproperties=font_prop, fontsize=12)
    plt.ylabel('Y轴 - 三角函数值（含负号：-1.0）', fontproperties=font_prop, fontsize=12)
    plt.legend(prop=font_prop)  # 图例也绑定字体
    plt.grid(True, alpha=0.3)
    plt.tight_layout()  # 防止中文截断
    plt.show()


# 执行对比函数
if __name__ == "__main__":
    compare_global_settings()