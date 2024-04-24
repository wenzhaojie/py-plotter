import matplotlib.ticker as ticker


# 设置坐标轴刻度格式
class CustomFormatter(ticker.Formatter):
    def __init__(self, ndigits=1, use_sci=False):
        self.ndigits = ndigits
        self.use_sci = use_sci

    def __call__(self, x, pos=None):
        if x == 0:
            return str(int(x))
        else:
            if self.use_sci:
                # 使用科学计数法
                return f"{x:.{self.ndigits}e}"
            else:
                # 保留ndigits位小数
                return f"{x:.{self.ndigits}f}"



if __name__ == '__main__':
    my_formatter = CustomFormatter(ndigits=2)

