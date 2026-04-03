from pyecharts import options as opts
from pyecharts.charts import EffectScatter
from pyecharts.globals import SymbolType
c = (
        EffectScatter()
       .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
     .add_yaxis('商家A', [114, 55, 27, 101, 125, 27, 105])
#        .add_yaxis('商家B',[57, 134, 137, 129, 145, 60, 49])
        .set_global_opts(title_opts=opts.TitleOpts(title="EffectScatter-基本示例"))
    )
c.render("EffectScatter-基本示例.html")