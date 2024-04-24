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
                # 格式化为1.0x10^n形式
                s = f"{x:.{self.ndigits}e}"
                base, exponent = s.split('e')
                exponent = int(exponent)  # 转换为整数
                if exponent == 0:
                    return f"{base}"
                else:
                    return fr"${base} \times 10^{{{exponent}}}$"
            else:
                # 保留ndigits位小数
                return f"{x:.{self.ndigits}f}"



if __name__ == '__main__':
    my_formatter = CustomFormatter(ndigits=2)

