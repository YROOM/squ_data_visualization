from pyecharts import options as opts
from pyecharts.globals import ThemeType
import numpy as np

from pyecharts.charts import Bar

# x轴数据
items = ["相机", "短视频", "视频", "浏览器", "商城", "购票", "小说", "聊天", "小工具", "理财记账"]
# y轴数据
sum_app = [[5045137.0], [4608092.0], [35723063.0], [23775808.0], [15367847.0], [10424808.0], [76975429.0], [7393185.0], [64636392.0], [50491990.0]]
# 生成实例化对象
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis([ "总数"])
for item in items:
    bar.add_yaxis(item,sum_app[items.index(item)])
bar.set_global_opts(title_opts=opts.TitleOpts(title="APP类型", subtitle="APP类型"))
bar.render("APP类型.html")
#bar.render_notebook()