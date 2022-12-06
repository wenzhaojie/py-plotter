# 有关画图的lib
from matplotlib import pyplot as plt
import os
import numpy as np
from matplotlib.ticker import FuncFormatter
from scipy import stats
from typing import List


class Pyplot_config:
    def __init__(self, figsize=(20, 6), fontsize=30):
        self.color_list = ["b", "g", "r", "c", "#EE82EE", "y", "grey", "brown", "purple"]
        self.hatch_list = [None, '...', 'x', '***', '|', '-', '/', '+', 'O', 'o', 'XXX', '.', '*']
        self.linestyle_list = [None, '--', '-.', ':', '-', '-', '-', '-']
        self.dash_list = [(2, 5), (4, 10), (3, 3, 2, 2), (5, 2, 20, 2), (5, 2), (1, 1, 5, 4), (5, 8), (2, 4, 5)]
        self.marker_list = ['o', '.', '*', '+', 'v']
        self.edge_color_list = ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black']
        self.label_size = int(fontsize * 0.8)
        self.tick_size = int(fontsize * 0.8)
        self.title_size = fontsize
        self.legend_size = int(fontsize * 0.8)
        self.legend_title_fontsize = int(fontsize * 0.8)
        self.bar_width = 0.1
        self.dpi = 300
        self.figsize = figsize
        self.title = None


class Plotter(Pyplot_config):
    def __init__(self, figsize=(20, 6), fontsize=30):
        super().__init__(figsize=figsize, fontsize=fontsize)
        pass

    # 用于画折线图, 有几条线就画几个
    def plot_lines(self, x_list=None, y_list=None, legend_label_list=None, x_label="x", y_label="y", title=None, x_grid=False, y_grid=True, y_min=None, y_max=None,
                   save_root="./", filename="demo.png", is_show=False,
                   legend_loc="best", legend_title="legend"):
        # 如果 save_root 没有创建，则创建一个
        os.makedirs(save_root, exist_ok=True)
        # 如果没有指定x的值，就用正整数列进行生成
        if x_list == None:
            x_list = [[i for i in range(len(y_list[0]))] for i in range(len(y_list))]
        fig = plt.figure(figsize=self.figsize, dpi=self.dpi)

        if legend_label_list != None:
            for index, y in enumerate(y_list):
                plt.plot(x_list[index], y, color=self.color_list[index], linestyle=self.linestyle_list[index],
                         label=legend_label_list[index])
        else:
            for index, y in enumerate(y_list):
                plt.plot(x_list[index], y, color=self.color_list[index], linestyle=self.linestyle_list[index])

        plt.xlabel(x_label, fontsize=self.label_size)
        plt.ylabel(y_label, fontsize=self.label_size)
        # 判断是否绘制title
        if title != None:
            plt.title(title, fontdict={'size': self.title_size})
        # 判断是否绘制legend
        if legend_label_list != None:
            plt.legend(fontsize=self.legend_size, loc=legend_loc, title=legend_title,
                       title_fontsize=self.legend_size)  # 将样例显示出来

        # 调整 tick 的字体大小
        plt.xticks(fontsize=self.tick_size)
        plt.yticks(fontsize=self.tick_size)

        # 网格线
        if x_grid and y_grid:
            cmd = "both"
            plt.grid(axis=cmd)
        else:
            if x_grid:
                cmd = "x"
                plt.grid(axis=cmd)
            if y_grid:
                cmd = "y"
                plt.grid(axis=cmd)

        # 设置ylim
        if y_min != None and y_max != None:
            plt.ylim(y_min, y_max)

        plt.tight_layout()
        savepath = os.path.join(save_root, filename)
        print(f"图片保存到:{savepath}")
        plt.savefig(savepath)
        # 展示图片
        if is_show:
            plt.show()

    # 绘制条形图
    def plot_bars(self, x_label="x", y_label="y", legend_title="legend", legend_ncol=1, bbox_to_anchor=None,
                  legend_loc="best", x_data=None, bar_data_list=None, legend_label_list=None, y_min=None, y_max=None,
                  x_grid=False, y_grid=True, save_root="./", filename="demo.png", is_hatch=False,
                  is_show=False):
        fig = plt.figure(figsize=self.figsize, dpi=self.dpi)
        ax = plt.subplot(111)
        # 设置轴的标签字体和大小
        ax.set_xlabel(x_label, fontdict={'size': self.label_size})
        ax.set_ylabel(y_label, fontdict={'size': self.label_size})

        # 分别画柱子
        r_base = np.arange(len(x_data))
        # 是否用阴影hatch区别
        if is_hatch:
            hatch_list = self.hatch_list
        else:
            hatch_list = [None for i in range(10)]

        for index, (bar_label, bar_data) in enumerate(zip(legend_label_list, bar_data_list)):
            r = [x + self.bar_width * (index) for x in r_base]
            ax.bar(r, bar_data, color=self.color_list[index], width=self.bar_width,
                   edgecolor=self.edge_color_list[index], label=legend_label_list[index], hatch=hatch_list[index])  # 创建柱子

        # 添加x轴名称
        plt.xticks([r + (len(bar_data_list) - 1) / 2 * self.bar_width for r in range(len(x_data))], x_data,
                   size=self.label_size)
        plt.yticks(size=self.label_size)

        # 创建图例
        legend = plt.legend(fontsize=self.legend_size, title=legend_title, loc=legend_loc, ncol=legend_ncol,
                            bbox_to_anchor=bbox_to_anchor)
        legend.get_title().set_fontsize(fontsize=self.legend_size)
        legend._legend_box.align = "left"

        # 网格线
        if x_grid and y_grid:
            cmd = "both"
            plt.grid(axis=cmd)
        else:
            if x_grid:
                cmd = "x"
                plt.grid(axis=cmd)
            if y_grid:
                cmd = "y"
                plt.grid(axis=cmd)

        # 设置ylim
        if y_min != None and y_max != None:
            plt.ylim(y_min, y_max)
        plt.tight_layout()

        savepath = os.path.join(save_root, filename)
        print(f"图片保存到:{savepath}")
        plt.savefig(savepath)
        # 展示图片
        if is_show:
            plt.show()
        pass

    @staticmethod
    def formatnum(x, pos):
        if x == 0:
            return f'{int(x)}'
        return "%.1f" % x

    @staticmethod
    def cal_cdf(input_data):
        val, cnt = np.unique(input_data, return_counts=True)
        pmf = cnt / len(input_data)
        fs_rv_dist = stats.rv_discrete(values=(val, pmf))
        return {"x": val, "y": fs_rv_dist.cdf(val)}

    # 绘制 cdf 图
    def plot_cdfs(self, x_label="x", y_label="cdf", legend_title="legend", legend_ncol=1, bbox_to_anchor=None,
                  legend_loc="best", cdf_data_list=None, legend_label_list=None, is_marker=False, linewidth=2, alpha=1,
                  save_root="./", filename="demo.png", is_show=False):
        # 画布
        fig = plt.figure(figsize=self.figsize, dpi=self.dpi)
        ax = fig.add_subplot(111)
        # 设置轴的标签字体和大小
        ax.set_xlabel(x_label, fontdict={'size': self.label_size})
        ax.set_ylabel(y_label, fontdict={'size': self.label_size})
        # 调整 tick 的字体大小
        plt.xticks(fontsize=self.tick_size)
        plt.yticks(fontsize=self.tick_size)
        # 让角标变0
        formatter = FuncFormatter(self.formatnum)
        ax.xaxis.set_major_formatter(formatter)
        ax.yaxis.set_major_formatter(formatter)
        # 计算cdf的值
        for index, (cdf_data, cdf_label) in enumerate(zip(cdf_data_list, legend_label_list)):
            res = self.cal_cdf(cdf_data)
            x = res["x"]
            y = res["y"]
            # 画图
            if is_marker:
                marker = self.marker_list[index]
            else:
                marker = None
            ax.plot(
                x, y,
                color=self.color_list[index],
                linestyle=self.linestyle_list[index],
                dashes=self.dash_list[index],
                marker=marker,
                linewidth=linewidth,
                alpha=alpha,
                label=cdf_label,
            )
        # 创建图例
        legend = plt.legend(fontsize=self.legend_size, title=legend_title, loc=legend_loc, ncol=legend_ncol,
                            bbox_to_anchor=bbox_to_anchor)
        legend.get_title().set_fontsize(fontsize=self.legend_size)
        legend._legend_box.align = "left"

        plt.tight_layout()
        savepath = os.path.join(save_root, filename)
        print(f"图片保存到:{savepath}")
        plt.savefig(savepath)
        # 展示图片
        if is_show:
            plt.show()
        pass

    # 绘制 box 图
    def plot_boxes(self, x: List[str]=None, box_data_list=None, legend_label_list=None, x_label="Replicas", y_label="Cost",
                  legend_title="legend", legend_loc="best", legend_ncol=1, bbox_to_anchor=None, save_root="./",
                  filename="demo.png", is_show=False):

        fig = plt.figure(figsize=self.figsize, dpi=300)
        ax = fig.add_subplot(111)
        ax.yaxis.grid(linestyle='dashed')
        ax.set_ylabel(y_label, fontsize=self.label_size)
        ax.set_xlabel(x_label, fontsize=self.label_size)

        width = 0.2
        interval = width * 1.25
        space = interval * 3
        interval_xtick = interval * (len(legend_label_list) - 1) + space
        position = np.arange(1, 1 + interval_xtick * len(x), interval_xtick)

        colors = ['red', 'darkblue', 'darkgreen', 'purple','gold']
        facecolors = ['pink', 'lightblue', 'lightgreen', 'violet','yellow']
        boxes = []

        for i in range(len(legend_label_list)):
            box_data = box_data_list[i]
            bp = ax.boxplot(box_data, showmeans=False, showfliers=False,
                            positions=[pos + interval * i for pos in position], widths=width, patch_artist=True)
            boxes.append(bp['boxes'][0])
            color = colors[i]
            facecolor = facecolors[i]
            for b in bp['boxes']:
                b.set(color=color)
                b.set(facecolor=facecolor)
                b.set(linewidth=2)
            for m in bp['medians']:
                m.set(color=color, linewidth=2)
            for c in bp['caps']:
                c.set(color=color, linewidth=2)
            for w in bp['whiskers']:
                w.set(color=color, linewidth=1.5, linestyle=':')

        offset = interval * (len(legend_label_list) - 1) / 2
        ax.set_xticks([pos + offset for pos in position])


        ax.set_xticklabels(x, fontsize=self.label_size, rotation=0)
        ax.tick_params(axis='both', which='major', labelsize=self.label_size)


        plt.xticks(size=self.label_size)
        plt.yticks(size=self.label_size)

        legend = plt.legend(boxes, legend_label_list, fontsize=self.legend_size, title=legend_title, loc=legend_loc, ncol=legend_ncol,
                            bbox_to_anchor=bbox_to_anchor)
        legend.get_title().set_fontsize(fontsize=self.legend_size)
        legend._legend_box.align = "left"

        plt.tight_layout()
        savepath = os.path.join(save_root, filename)
        print(f"图片保存到:{savepath}")
        plt.savefig(savepath)
        # 展示图片
        if is_show:
            plt.show()

    def plot_error_grids(self, ms: list, ns: list, ys: list, predict_ys: list, x_label='Memory Size (MB)', y_label='Jobs', legend_label="Relative Error", save_root="./",
        filename="plot_grid_demo", is_show=False):
        # 绘制误差率的网格图
        fig = plt.figure(dpi=300, figsize=(8, 6))
        ax = plt.subplot(111)

        errors = [abs(y - predict_y) / y for y, predict_y in zip(ys, predict_ys)]
        mapping = {}  # 从(memory size, image num)到误差率的映射
        for m, n, error in zip(ms, ns, errors):
            mapping[(m, n)] = error

        u_ms, u_ns = np.sort(np.unique(ms)), np.sort(np.unique(ns))
        xticks, yticks = range(len(u_ms)), range(len(u_ns))
        Xs, Ys = np.meshgrid(xticks, yticks)
        zs = [[mapping.setdefault((u_ms[Xs[i][j]], u_ns[Ys[i][j]]), 0) for j in range(len(xticks))] for i in
              range(len(yticks))]
        graph = ax.pcolor(Xs, Ys, zs, shading='auto')
        cb = fig.colorbar(graph)
        cb.ax.tick_params(labelsize=self.label_size)
        cb.set_label(legend_label, fontdict={'size': self.label_size})

        # 设置x轴和y轴的标签字体和大小
        ax.set_xlabel(x_label, fontdict={'size': self.label_size})
        ax.set_ylabel(y_label, fontdict={'size': self.label_size})
        # 设置x轴和y轴的刻度字体和大小
        plt.xticks(xticks, u_ms.astype(int), size=self.label_size)
        plt.yticks(yticks, u_ns.astype(int), size=self.label_size)

        plt.tight_layout()
        savepath = os.path.join(save_root, filename)
        print(f"图片保存到:{savepath}")
        plt.savefig(savepath)
        # 展示图片
        if is_show:
            plt.show()


    def plot_grids(self, x_list: list, y_list: list, z_list: list, x_label="Memory Size (MB)", y_label="Jobs", legend_label="Relative Error", save_root="./",
        filename="plot_grid_demo", is_show=False):
        # 绘制误差率的网格图
        fig = plt.figure(dpi=self.dpi, figsize=self.figsize)
        ax = plt.subplot(111)

        mapping = {} # 从(memory size, image num)到误差率的映射
        for m, n, error in zip(x_list, y_list, z_list):
            mapping[(m, n)] = error

        u_ms, u_ns = np.sort(np.unique(x_list)), np.sort(np.unique(y_list))
        xticks, yticks = range(len(u_ms)), range(len(u_ns))
        Xs, Ys = np.meshgrid(xticks, yticks)
        zs = [[mapping.setdefault((u_ms[Xs[i][j]], u_ns[Ys[i][j]]), 0) for j in range(len(xticks))] for i in
              range(len(yticks))]
        graph = ax.pcolor(Xs, Ys, zs, shading='auto')
        cb = fig.colorbar(graph)
        cb.ax.tick_params(labelsize=self.label_size)
        cb.set_label(legend_label, fontdict={'size': self.label_size})

        # 设置x轴和y轴的标签字体和大小
        ax.set_xlabel(x_label, fontdict={'size': self.label_size})
        ax.set_ylabel(y_label, fontdict={'size': self.label_size})
        # 设置x轴和y轴的刻度字体和大小
        plt.xticks(xticks, u_ms.astype(int), size=self.label_size)
        plt.yticks(yticks, u_ns.astype(int), size=self.label_size)

        plt.tight_layout()
        savepath = os.path.join(save_root, filename)
        print(f"图片保存到:{savepath}")
        plt.savefig(savepath)
        # 展示图片
        if is_show:
            plt.show()


    def plot_acc_bars(self, x_data=None, bar_data_list=None, bar_width=0.35, x_label="x", y_label="y", legend_loc="best", legend_title="legend", legend_ncol=1, bbox_to_anchor=None,
                    legend_label_list=None, y_min=None, y_max=None,
                  x_grid=False, y_grid=True, save_root="./", filename="plot_acc_bars_demo", is_hatch=False,
                  is_show=False):

        fig = plt.figure(dpi=self.dpi, figsize=self.figsize)
        ax = plt.subplot(111)
        # 设置轴的标签字体和大小
        ax.set_xlabel(x_label, fontdict={'size': self.label_size})
        ax.set_ylabel(y_label, fontdict={'size': self.label_size})

        ind = np.arange(len(bar_data_list))  # the x locations for the groups
        bottom = [0 for i in range(len(bar_data_list[0]))]
        for index, bar_data in enumerate(bar_data_list):

            ax.bar(ind, bar_data_list[index], bar_width, label=legend_label_list[index], color=self.color_list[index], edgecolor=self.edge_color_list[index], bottom=bottom)

            # 更新 bottom
            for i in range(len(bottom)):
                bottom[i] += bar_data[i]

        # 添加x轴名称
        plt.xticks(ticks=ind, size=self.label_size, labels=legend_label_list)
        plt.yticks(size=self.label_size)

        # 创建图例
        legend = plt.legend(fontsize=self.legend_size, title=legend_title, loc=legend_loc,
                            ncol=legend_ncol,
                            bbox_to_anchor=bbox_to_anchor)
        legend.get_title().set_fontsize(fontsize=self.legend_size)
        legend._legend_box.align = "left"

        # 网格线
        if x_grid and y_grid:
            cmd = "both"
            plt.grid(axis=cmd)
        else:
            if x_grid:
                cmd = "x"
                plt.grid(axis=cmd)
            if y_grid:
                cmd = "y"
                plt.grid(axis=cmd)

        # 设置ylim
        if y_min != None and y_max != None:
            plt.ylim(y_min, y_max)

        plt.tight_layout()
        savepath = os.path.join(save_root, filename)
        print(f"图片保存到:{savepath}")
        plt.savefig(savepath)
        # 展示图片
        if is_show:
            plt.show()




if __name__ == "__main__":
    my_plotter = Plotter(figsize=(8, 6))

    y1 = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]
    y2 = [-1, 0, 1, 0, -1, -1, 0, 1, 0, -1]
    y3 = [1, 2, 3, 4, 2, 4, 6, 1, 5, 1]
    y4 = [1, 2, 3, 4, 2, 4, 6, 1, 5, 1]
    y5 = [0, 2, 3, 4, 2, 1, 6, 8, 5, 1]

    my_plotter.plot_lines(
        x_list=[[i for i in range(len(y1))] for i in range(5)],
        y_list=[y1,y2,y3,y4,y5],
        legend_label_list=["y1","y2","y3","y4","y5"],
        x_label="X",
        y_label="Y",
        x_grid=True,
        y_grid=True,
        y_min=0,
        y_max=10,
        legend_loc="best",
        legend_title="Legend",
        title="This is a demo!",
        save_root="./results",
        filename="plot_lines_demo"
    )

    my_plotter.plot_boxes(
        x=["2.0", "1.0", "3", "5"],
        box_data_list=[[y1, y2, y3, y4], [y2, y3, y4, y5], [y3, y4, y5, y1], [y4, y5, y1, y2]],
        legend_label_list=["1234", "2345", "3451", "4512"],
        x_label="x",
        y_label="y",
        save_root="./results",
        filename="plot_boxes_demo"
    )

    my_plotter.plot_bars(
        x_data=["0","1.0","2","3.5"],
        bar_data_list=[
            [1,2,3,4],
            [2,3,4,5],
            [3,4,5,6],
            [7,8,9,10]
        ],
        legend_label_list=["1","2","3","4"],
        x_label="X",
        y_label="Y",
        save_root="./results",
        filename="plot_bars_demo"
    )

    my_plotter.plot_error_grids(
        ms=[1,1,1,2,2,3,3,3,3],
        ns=[4,5,6,4,5,6,4,5,6],
        ys=[1,1,1,1,1,1,1,1,1],
        predict_ys=[1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9],
        x_label="X",
        y_label="Y",
        legend_label="Error",
        save_root="./results",
        filename="plot_error_grids_demo"
    )

    my_plotter.plot_grids(
        x_list=[1, 1, 1, 2, 2, 3, 3, 3, 3],
        y_list=[4, 5, 6, 4, 5, 6, 4, 5, 6],
        z_list=[1.1,2.2,1.3,1.4,4.5,1.6,1.7,1.8,4.9],
        x_label="X",
        y_label="Y",
        legend_label="Error",
        save_root="./results",
        filename="plot_grids_demo"
    )

    my_plotter.plot_acc_bars(
        x_data=["0", "1.0", "2", "3.5"],
        bar_data_list=[
            [1, 2, 3, 4],
            [2, 3, 4, 5],
            [3, 4, 5, 6],
            [7, 8, 9, 10]
        ],
        legend_label_list=["1", "2", "3", "4"],
        x_label="X",
        y_label="Y",
        save_root="./results",
        filename="plot_acc_bars_demo",
        y_min=0,
        y_max=40,
    )

