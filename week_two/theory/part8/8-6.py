import matplotlib.pyplot as plt #画图
import numpy as np # 用来计算，模拟一些数

fig,axes = plt.subplots()
axes.plot(np.arange(0,24,2),[14,9,7,5,12,19,23,26,27,24,21,19],'-o')
axes.set_xticks(np.arange(0,24,2))
axes.annotate('hottest at 16:00',# 文本
              xy=(16,27), #箭头指向的方向
              xytext=(16,22),#文本未知
              arrowprops=dict(facecolor='black',shrink=0.2),#箭头属性
              ha='center', #水平居中
              va='center' # 垂直居中
              )
axes.text(12, #文本的x坐标
          10, #文本的y坐标
          'Date: March 26th, 2018',
         bbox={'facecolor':'cyan','alpha':0.3,'pad':6})

plt.show()
