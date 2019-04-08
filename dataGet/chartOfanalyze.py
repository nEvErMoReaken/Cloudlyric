import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
# 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
plt.figure(figsize=(8, 6), dpi=80)

# 再创建一个规格为 1 x 1 的子图
plt.subplot(1, 1, 1)

# 柱子总数
N = 11
# 包含每个柱子对应值的序列
values = (75, 17, 9, 9, 2,7,6,12,7,9,25)

# 包含每个柱子下标的序列
index = np.arange(N)

# 柱子的宽度
width = 0.35

# 绘制柱状图, 每根柱子的颜色为紫罗兰色
p2 = plt.bar(index, values, width, label="城市", color="#87CEFA")

# 设置横轴标签
plt.xlabel('')
# 设置纵轴标签
plt.ylabel('次数')

# 添加标题
plt.title('民谣歌手最钟爱的城市')

# 添加纵横轴的刻度
plt.xticks(index, ('北京', '上海', '深圳', '成都', '苏州', '重庆','武汉','南京','青岛','郑州','兰州'))
plt.yticks(np.arange(0, 81, 10))

# 添加图例
plt.legend(loc="upper right")

plt.show()