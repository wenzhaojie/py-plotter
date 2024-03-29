import matplotlib.ticker as ticker


# 设置坐标轴刻度格式
class CustomFormatter(ticker.Formatter):

    def __init__(self, ndigits=1):
        self.ndigits = ndigits

    def __call__(self, x, pos=None):
        if x == 0:
            return str(int(x))
        else:
            # 保留ndigits位小数
            res = "{:.{}f}".format(x, self.ndigits)
            return res



if __name__ == '__main__':
    my_formatter = CustomFormatter(ndigits=2)

