import json
import pandas as pd
import matplotlib.pyplot as plt

# 设置中文显示（解决matplotlib中文乱码）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

# 步骤1：读取JSON文件
def read_json_file(file_path):
    """读取JSON文件并返回解析后的数据"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)  # 解析JSON为Python列表（包含字典）
        print("JSON数据读取成功！")
        return data
    except FileNotFoundError:
        print("文件不存在，请检查路径！")
        return None
    except json.JSONDecodeError:
        print("JSON格式错误，请检查文件内容！")
        return None

# 调用函数读取数据
json_data = read_json_file('student_score.json')

if json_data:
    # 转换为DataFrame（方便数据处理）
    df = pd.DataFrame(json_data)
    print("\n解析后的数据预览：")
    print(df.head())  # 打印前5行数据

# 步骤2：数据清洗与提取
if json_data:
    # 提取字段
    names = df['name'].tolist()  # 学生姓名列表
    math_scores = df['math'].tolist()  # 数学成绩
    english_scores = df['english'].tolist()  # 英语成绩
    python_scores = df['python'].tolist()  # Python成绩

    # 计算各科平均分
    avg_math = round(df['math'].mean(), 1)
    avg_english = round(df['english'].mean(), 1)
    avg_python = round(df['python'].mean(), 1)

    print(f"\n各科平均分：数学{avg_math}，英语{avg_english}，Python{avg_python}")

    # 步骤3-1：学生各科成绩对比柱状图
    if json_data:
        # 设置图表大小
        plt.figure(figsize=(10, 6))
        # 柱状图位置调整（避免重叠）
        x = range(len(names))
        width = 0.25

        # 绘制三科成绩柱状图
        plt.bar([i - width for i in x], math_scores, width=width, label='数学', color='skyblue')
        plt.bar(x, english_scores, width=width, label='英语', color='lightgreen')
        plt.bar([i + width for i in x], python_scores, width=width, label='Python', color='salmon')

        # 添加图表标签
        plt.xlabel('学生姓名')
        plt.ylabel('成绩')
        plt.title('学生各科成绩对比')
        plt.xticks(x, names)  # x轴显示学生姓名
        plt.legend()  # 显示图例
        plt.grid(axis='y', linestyle='--', alpha=0.7)  # 添加网格线
        plt.savefig('student_scores_bar.png')  # 保存图表
        plt.show()

# 步骤3-2：各科平均分对比条形图
if json_data:
    plt.figure(figsize=(8, 5))
    subjects = ['数学', '英语', 'Python']
    avg_scores = [avg_math, avg_english, avg_python]

    # 绘制平均分条形图
    plt.bar(subjects, avg_scores, color=['skyblue', 'lightgreen', 'salmon'])

    # 在条形图上标注数值
    for i, score in enumerate(avg_scores):
        plt.text(i, score + 0.5, str(score), ha='center', fontsize=12)

    plt.xlabel('科目')
    plt.ylabel('平均分')
    plt.title('各科平均分对比')
    plt.ylim(0, 100)  # y轴范围0-100
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig('avg_scores_bar.png')
    plt.show()