from pyecharts import Pie
attr =["昨天", "今天", "明天"]
v1 =[63,87,181]
pie =Pie("民谣歌手活在昨天、今天、还是明天？？")
pie.add("", attr, v1, is_label_show=True)
pie.render()