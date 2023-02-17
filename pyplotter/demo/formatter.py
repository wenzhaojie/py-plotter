import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# 生成示例数据
x = np.linspace(-10, 10, 100)
y = np.sin(x)

# 创建绘图对象和子图对象
fig, ax = plt.subplots()


# 设置x轴刻度格式
class CustomFormatter(ticker.Formatter):
    def __call__(self, x, pos=None):
        if x == 0:
            return str(int(x))
        else:
            return '{:.1f}'.format(x)


ax.xaxis.set_major_formatter(CustomFormatter())

# 设置x轴和y轴的原点刻度位置
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# 绘制图像
ax.plot(x, y)

# 显示图像
plt.show()