import numpy as np
import matplotlib.pyplot as plt

# 生成数据
data = np.random.normal(size=1000)

# 计算CDF
counts, bin_edges = np.histogram(data, bins=100, density=True)
cdf = np.cumsum(counts)

# 绘制CDF图
plt.plot(bin_edges[1:], cdf)
plt.xlabel('Value')
plt.ylabel('CDF')
plt.show()