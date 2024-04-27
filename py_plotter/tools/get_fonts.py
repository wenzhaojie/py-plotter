import matplotlib.font_manager

# 获取系统中可用的所有字体
all_fonts = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')

# 输出所有字体名字
for font in all_fonts:
    print(font)
