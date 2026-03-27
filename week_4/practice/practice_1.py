import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import warnings

plt.rcParams['font.sans-serif']=['simhei']
plt.rcParams['font.serif'] = ['simhei']

warnings.filterwarnings('ignore')
myfont=FontProperties(fname=r'C:\Windows\Fonts\SimHei.ttf',size=12)
sns.set(font=myfont.get_name())
df = pd.read_csv('.\data\StudentPerformance.csv')
# print(df.head(4))
# print(df)


df.rename(columns={'gender':'性别',
                   'NationalITy':'国籍',
                   'PlaceofBirth':'出生地',
                   'StageID':'学段',
                   'GradeID':'年级','SectionID':'班级','Topic':'科目',
                  'Semester':'学期','Relation':'监管人','raisedhands':'举手次数',
                  'VisITedResources':'浏览课件次数','AnnouncementsView':'浏览公告次数',
                  'Discussion':'讨论次数','ParentAnsweringSurvey':'父母问卷',
                  'ParentschoolSatisfaction':'家长满意度','StudentAbsenceDays':'缺勤次数',
                   'Class':'成绩'},inplace=True)


df.replace({'lowerlevel':'小学','MiddleSchool':'中学','HighSchool':'高中'},inplace=True)

# print(df.columns)

# print('学段取值：',df['学段'].unique())
# print('学期取值：',df['学期'].unique())

df['性别'].replace({'M':'男','F':'女'},inplace=True)
df['学期'].replace({'S':'春季','F':'秋季'},inplace=True)

# print(df.head(4))


# print(df.shape)
#
# print(df.isnull().sum())

# print(df.describe())

# print(df.dtypes)
# print(df.info())
print(df['成绩'].unique())
# 统计每个类别出现的次数 并且以柱状图显示
# sns.countplot(x = '成绩',
#               order = ['L', 'M', 'H'],
#               data = df,
#               linewidth=2,
#               edgecolor=sns.color_palette("dark",3)
#               )
#
#
# sns.countplot(x = '性别',
#               order = ['女', '男'],
#               data = df,
#               hue = '性别',
#               linewidth=2,
#               edgecolor=sns.color_palette("dark",2)
#               )




# 创建1行2列的子图
# fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# # 第一张图：成绩分布
# sns.countplot(x='成绩',
#               order=['L', 'M', 'H'],
#               data=df,
#               linewidth=2,
#               edgecolor=sns.color_palette("dark", 3),
#               ax=axes[0])  # 指定绘制在第一个子图上
# axes[0].set_title('成绩分布')
#
# # 第二张图：性别分布
# sns.countplot(x='性别',
#               order=['女', '男'],
#               data=df,
#               hue='性别',
#               linewidth=2,
#               edgecolor=sns.color_palette("dark", 2),
#               ax=axes[1])  # 指定绘制在第二个子图上
# axes[1].set_title('性别分布')
#
# plt.tight_layout()  # 自动调整子图间距
# plt.show()

# sns.set_style('whitegrid')
# sns.set(rc={'figure.figsize':(16,8)},font=myfont.get_name(),font_scale=1.5)
# sns.countplot(x = '科目', data = df)

df_temp = df[['科目', '性别']]
df_temp['count'] = 1
df_temp = df_temp.groupby(['科目', '性别']).agg('sum').reset_index()
print(df_temp.head(4))

plt.show()
