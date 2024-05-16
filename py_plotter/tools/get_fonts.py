import matplotlib.font_manager

# 获取系统中可用的所有字体
all_fonts = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')

# 输出所有字体名字
for font in all_fonts:
    print(font)



import matplotlib.pyplot as plt

# 获取当前所有设置的 plt.rcParams['font.sans-serif'] 的值
sans_serif_fonts = plt.rcParams['font.sans-serif']

# 打印所有设置的字体列表
print(sans_serif_fonts)


# 获取当前所有设置的 plt.rcParams['font.serif'] 的值
sans_serif_fonts = plt.rcParams['font.serif']

# 打印所有设置的字体列表
print(sans_serif_fonts)
