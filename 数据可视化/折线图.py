# 赵百超
# 创建时间  2023/9/12  10:53

# 导包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts

# 得到折线图对象
line = Line()

# 添加x轴
line.add_xaxis(["China","America","England"])
# 添加y轴
line.add_yaxis("新冠疫情",[30,20,10])

# 全局配置 set_global_opts来配置
line.set_global_opts(
    title_opts = TitleOpts(title = "疫情展示")
)

# 生成图表
line.render()