import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置字体为宋体
font = FontProperties(fname=r'/Users/wzj/GitHubProjects/py-plotter/py_plotter/fonts/SimSun.ttf', size=12)

# 示例数据
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 创建画布和子图
fig, ax = plt.subplots()

# 绘制折线图
ax.plot(x, y)

# 设置标题和标签字体为宋体
ax.set_title('示例折线图', fontproperties=font)
ax.set_xlabel('X轴', fontproperties=font)
ax.set_ylabel('Y轴', fontproperties=font)

# 显示图形
plt.show()
