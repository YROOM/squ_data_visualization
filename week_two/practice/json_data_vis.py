import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 解决中文乱码（仅保留核心配置）
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 读取并解析JSON文件（合并异常处理+核心逻辑）
try:
    with open('student_score.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    print("数据读取成功，预览：\n", df.head())
except Exception as e:
    print(f"读取失败：{e}")
    exit()  # 读取失败直接退出

# 2. 提取数据+计算平均分（简化变量名，剔除冗余列表转换）
names = df['name']
avg_math, avg_english, avg_python = round(df['math'].mean(),1), round(df['english'].mean(),1), round(df['python'].mean(),1)
print(f"\n各科平均分：数学{avg_math}，英语{avg_english}，Python{avg_python}")

# 3. 绘制柱状图（简化布局，剔除冗余注释，保留核心绘图逻辑）
plt.figure(figsize=(10,6))
x = range(len(names))
width = 0.25

# 绘制三科柱状图
plt.bar([i-width for i in x], df['math'], width, label='数学', color='skyblue')
plt.bar(x, df['english'], width, label='英语', color='lightgreen')
plt.bar([i+width for i in x], df['python'], width, label='Python', color='salmon')

# 基础样式配置
plt.xlabel('学生姓名'), plt.ylabel('成绩'), plt.title('学生各科成绩对比')
plt.xticks(x, names), plt.legend(), plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('student_scores_bar.png'), plt.show()