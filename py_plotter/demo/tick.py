import matplotlib.pyplot as plt
import numpy as np

# 生成示例数据
x = np.linspace(-10, 10, 100)
y = np.sin(x)

# 创建绘图对象和子图对象
fig, ax = plt.subplots()

# 设置x轴和y轴的刻度位置
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# 设置x轴和y轴的原点刻度位置
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# 绘制图像
ax.plot(x, y)

# 显示图像
plt.show()