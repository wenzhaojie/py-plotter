# 有关画图的lib
from matplotlib import pyplot as plt
import os
import numpy as np

from scipy import stats
from typing import List
from py_plotter.tick_formatter import CustomFormatter
from matplotlib.ticker import MaxNLocator
import matplotlib.patches as mpatches

class Pyplot_config:
    def __init__(self, figsize=(20, 6), fontsize=30):
        self.color_list = ["b", "g", "r", "c", "#EE82EE", "y", "grey", "brown", "purple"]
        self.hatch_list = [None, '...', 'x', '***', '|', '-', '/', '+', 'O', 'o', 'XXX', '.', '*']
        self.linestyle_list = [None, '--', '-.', ':', '-', '-', '-', '-']
        self.dash_list = [(2, 5), (4, 10), (3, 3, 2, 2), (5, 2, 20, 2), (5, 2), (1, 1, 5, 4), (5, 8), (2, 4, 5)]
        self.marker_list = ['*','.','v','+','o']
        self.edge_color_list = ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black']
        self.label_size = int(fontsize * 1)
        self.data_size = int(fontsize * 0.5)
        self.tick_size = int(fontsize * 1)
        self.title_size = fontsize
        self.legend_size = int(fontsize * 0.8)
        self.legend_title_fontsize = int(fontsize * 0.8)
        self.bar_width = 0.1
        self.dpi = 300
        self.figsize = figsize
        self.title = None


class Plotter(Pyplot_config):
    def __init__(self, figsize=(20, 6), fontsize=30, font="Arial", dpi=None, label_size=None, tick_size=None, title_size=None, legend_size=None, data_size=None, bar_width=None, legend_title_fontsize=None):
        # 先调用父类的构造函数，初始默认值
        super().__init__(figsize=figsize, fontsize=fontsize)

        # 如果传入了新的参数，就使用新的参数
        if dpi != None:
            self.dpi = dpi
        if label_size != None:
            self.label_size = label_size
        if tick_size != None:
            self.tick_size = tick_size
        if title_size != None:
            self.title_size = title_size
        if legend_size != None:
            self.legend_size = legend_size
        if data_size != None:
            self.data_size = data_size
        if bar_width != None:
            self.bar_width = bar_width
        if legend_title_fontsize != None:
            self.legend_title_fontsize = legend_title_fontsize

        # 全局设置font
        if font != None:
            plt.rcParams['font.family'] = 'sans-serif'
            plt.rcParams['font.sans-serif'] = 'Arial'
            plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

    # 用于画折线图, 有几条线就画几个
    def plot_lines(self, x_list=None, line_data_list=None, data_label_list=None, legend_label_list=None, x_label="x",
                   y_label="y", title=None,
                   x_grid=False, y_grid=True, y_min=None, y_max=None, x_tick_ndigits=1, y_tick_ndigits=2, y_tick_interval=None,
                   is_marker=False, is_x_tick_sci=False, is_y_tick_sci=False,
                   line_width=2.0,  # 新增参数用于控制线条粗细
                   save_root="./", filename="demo.png", is_show=False, legend_ncol=1, bbox_to_anchor=None,
                   legend_loc="best", legend_title="legend"):
        os.makedirs(save_root, exist_ok=True)
        if x_list is None:
            x_list = [[i for i in range(len(line_data_list[0]))] for _ in range(len(line_data_list))]
        fig = plt.figure(figsize=self.figsize, dpi=self.dpi)

        if legend_label_list is not None:
            for index, y in enumerate(line_data_list):
                if is_marker:
                    plt.plot(x_list[index], y, color=self.color_list[index], linestyle=self.linestyle_list[index],
                             label=legend_label_list[index], marker=self.marker_list[index],
                             linewidth=line_width)
                else:
                    plt.plot(x_list[index], y, color=self.color_list[index], linestyle=self.linestyle_list[index],
                             label=legend_label_list[index], linewidth=line_width)
        else:
            for index, y in enumerate(line_data_list):
                if is_marker:
                    plt.plot(x_list[index], y, color=self.color_list[index], linestyle=self.linestyle_list[index],
                             marker=self.marker_list[index], linewidth=line_width)
                else:
                    plt.plot(x_list[index], y, color=self.color_list[index], linestyle=self.linestyle_list[index],
                             linewidth=line_width)

        plt.xlabel(x_label, fontsize=self.label_size)
        plt.ylabel(y_label, fontsize=self.label_size)
        if title is not None:
            plt.title(title, fontdict={'size': self.title_size})

        if legend_label_list is not None:
            legend = plt.legend(fontsize=self.legend_size, title=legend_title, loc=legend_loc, ncol=legend_ncol,
                                bbox_to_anchor=bbox_to_anchor)
            legend.get_title().set_fontsize(self.legend_size)
            legend._legend_box.align = "left"

        ax = plt.gca()
        x_formatter = CustomFormatter(ndigits=x_tick_ndigits, use_sci=is_x_tick_sci)
        y_formatter = CustomFormatter(ndigits=y_tick_ndigits, use_sci=is_y_tick_sci)
        ax.xaxis.set_major_formatter(x_formatter)
        ax.yaxis.set_major_formatter(y_formatter)

        plt.xticks(fontsize=self.tick_size)
        plt.yticks(fontsize=self.tick_size)

        if y_tick_interval is not None:
            # 如果y_min 和 y_max 为None，初始化一个
            if y_min is None:
                y_min = int(np.min(line_data_list))
            if y_max is None:
                y_max = int(np.max(line_data_list)) + 2
            ax.set_yticks(np.arange(y_min, y_max + y_tick_interval, y_tick_interval))

        if data_label_list is not None:
            for index, y in enumerate(line_data_list):
                for x, y, label in zip(x_list[index], line_data_list[index], data_label_list[index]):
                    plt.text(x, y, label, fontsize=self.data_size)

        if x_grid and y_grid:
            plt.grid(which='both')
        elif x_grid:
            plt.grid(axis='x')
        elif y_grid:
            plt.grid(axis='y')

        if y_min is not None and y_max is not None:
            plt.ylim(y_min, y_max)

        plt.tight_layout()
        savepath = os.path.join(save_root, filename)
        print(f"图片保存到: {savepath}")
        plt.savefig(savepath)
        if is_show:
            plt.show()
        plt.close()

    # 绘制条形图
    def plot_bars(self, x_label="x", y_label="y", legend_title="legend", legend_ncol=1, bbox_to_anchor=None, y_tick_ndigits=2,
                  legend_loc="best", x_data=None, bar_data_list=None, legend_label_list=None, y_min=None, y_max=None,
                  x_grid=False, y_grid=True, save_root="./", filename="demo.png", is_hatch=False,
                  is_show=False):

        plt.figure(figsize=self.figsize, dpi=self.dpi)
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
                   edgecolor=self.edge_color_list[index], label=legend_label_list[index],
                   hatch=hatch_list[index])  # 创建柱子

        # 添加x轴名称
        plt.xticks([r + (len(bar_data_list) - 1) / 2 * self.bar_width for r in range(len(x_data))], x_data,
                   size=self.label_size)
        plt.yticks(size=self.label_size)

        # 让角标变0
        ax = plt.gca()
        y_formatter = CustomFormatter(ndigits=y_tick_ndigits)
        ax.yaxis.set_major_formatter(y_formatter)

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
        # 释放内存
        plt.close()
        pass

    def plot_stack_bars(self, x_label="x", y_label="y", legend_title="legend", legend_ncol=1, bbox_to_anchor=None, y_tick_ndigits=2,
                  legend_loc="best", x_data=None, bar_data_list=None, legend_label_list=None, y_min=None, y_max=None,
                  x_grid=False, y_grid=True, save_root="./", filename="demo.png", is_hatch=False,
                  is_show=False):

        plt.figure(figsize=self.figsize, dpi=self.dpi)
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

        bottom = np.zeros(len(x_data))

        for index, (bar_label, bar_data) in enumerate(zip(legend_label_list, bar_data_list)):

            ax.bar(r_base, bar_data, bottom=bottom, color=self.color_list[index], width=self.bar_width,
                   edgecolor=self.edge_color_list[index], label=legend_label_list[index],
                   hatch=hatch_list[index])  # 创建柱子

            bottom += np.array(bar_data)

        # 添加x轴名称
        plt.xticks([r for r in range(len(x_data))], x_data,
                   size=self.label_size)
        plt.yticks(size=self.label_size)

        # 让角标变0
        ax = plt.gca()
        y_formatter = CustomFormatter(ndigits=y_tick_ndigits)
        ax.yaxis.set_major_formatter(y_formatter)

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
        # 释放内存
        plt.close()
        pass

    @staticmethod
    def cal_cdf(input_data):
        val, cnt = np.unique(input_data, return_counts=True)
        pmf = cnt / len(input_data)
        fs_rv_dist = stats.rv_discrete(values=(val, pmf))
        return {"x": val, "y": fs_rv_dist.cdf(val)}

    # 绘制 cdf 图
    def plot_cdfs(self, x_label="x", y_label="cdf", is_no_legend=False, legend_title="legend", legend_ncol=1, bbox_to_anchor=None,
                  x_tick_ndigits=1, y_tick_ndigits=1, num_x_ticks=5, num_y_ticks=5,
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
        x_formatter = CustomFormatter(ndigits=x_tick_ndigits)
        y_formatter = CustomFormatter(ndigits=y_tick_ndigits)


        ax.xaxis.set_major_formatter(x_formatter)
        ax.yaxis.set_major_formatter(y_formatter)

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

        # 设置x轴的刻度
        if num_x_ticks != None:
            ax.xaxis.set_major_locator(MaxNLocator(integer=False, prune="both", nbins=num_x_ticks))
        # 设置y轴的刻度
        if num_y_ticks != None:
            ax.yaxis.set_major_locator(MaxNLocator(integer=False, prune="both", nbins=num_y_ticks))

        # 创建图例
        if not is_no_legend:
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
        # 释放内存
        plt.close()
        pass

    # 绘制 box 图
    def plot_boxes(self, x: List[str] = None, box_data_list=None, legend_label_list=None, x_label="Replicas",
                   y_label="Cost", y_min=None, y_max=None,
                   legend_title="legend", legend_loc="best", legend_ncol=1, bbox_to_anchor=None, x_tick_ndigits=1,
                   y_tick_ndigits=2, is_data_label=False,
                   save_root="./", filename="demo.png", is_show=False):

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

        colors = ['red', 'darkblue', 'darkorange', 'darkgreen', 'gold', 'purple', ]
        facecolors = ['pink', 'lightblue', 'moccasin', 'lightgreen', 'yellow', 'violet', ]
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

        # 让角标变0
        ax = plt.gca()
        y_formatter = CustomFormatter(ndigits=y_tick_ndigits)
        ax.yaxis.set_major_formatter(y_formatter)

        plt.xticks(size=self.label_size)
        plt.yticks(size=self.label_size)

        legend = plt.legend(boxes, legend_label_list, fontsize=self.legend_size, title=legend_title, loc=legend_loc,
                            ncol=legend_ncol,
                            bbox_to_anchor=bbox_to_anchor)
        legend.get_title().set_fontsize(fontsize=self.legend_size)
        legend._legend_box.align = "left"

        # 在图上显示box的平均值
        if is_data_label:
            for i in range(len(legend_label_list)):
                box_data = box_data_list[i]
                for j in range(len(x)):
                    mean = np.mean(box_data[j])
                    ax.text(position[j] + interval * i, mean, '%.1f' % mean, ha='center', va='bottom', fontsize=self.data_size)

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
        # 释放内存
        plt.close()

    def plot_error_grids(self, ms: list, ns: list, ys: list, predict_ys: list, x_tick_ndigits=0, y_tick_ndigits=0,
                         x_label='Memory Size (MB)', y_label='Jobs', legend_label="Relative Error",
                         save_root="./", filename="plot_grid_demo", is_show=False):
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

        # 让角标变0
        x_formatter = CustomFormatter(ndigits=x_tick_ndigits)
        y_formatter = CustomFormatter(ndigits=y_tick_ndigits)
        ax.xaxis.set_major_formatter(x_formatter)
        ax.yaxis.set_major_formatter(y_formatter)

        plt.tight_layout()
        savepath = os.path.join(save_root, filename)
        print(f"图片保存到:{savepath}")
        plt.savefig(savepath)
        # 展示图片
        if is_show:
            plt.show()
        # 释放内存
        plt.close()

    def plot_grids(self, x_list: list, y_list: list, z_list: list, x_tick_ndigits=1, y_tick_ndigits=0,
                   x_label="Memory Size (MB)", y_label="Jobs",
                   legend_label="Relative Error", save_root="./",
                   filename="plot_grid_demo", is_show=False):
        # 绘制误差率的网格图
        fig = plt.figure(dpi=self.dpi, figsize=self.figsize)
        ax = plt.subplot(111)

        mapping = {}  # 从(memory size, image num)到误差率的映射
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

        # 让角标变0
        x_formatter = CustomFormatter(ndigits=x_tick_ndigits)
        y_formatter = CustomFormatter(ndigits=y_tick_ndigits)
        ax.xaxis.set_major_formatter(x_formatter)
        ax.yaxis.set_major_formatter(y_formatter)

        plt.tight_layout()
        savepath = os.path.join(save_root, filename)
        print(f"图片保存到:{savepath}")
        plt.savefig(savepath)
        # 展示图片
        if is_show:
            plt.show()
        # 释放内存
        plt.close()

    def plot_acc_bars(self, bar_data_list=None, bar_width=0.35, x_label="x", y_label="y",
                      legend_loc="best", legend_title="legend", legend_ncol=1, bbox_to_anchor=None,
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

            ax.bar(ind, bar_data_list[index], bar_width, label=legend_label_list[index], color=self.color_list[index],
                   edgecolor=self.edge_color_list[index], bottom=bottom)

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
        # 释放内存
        plt.close()

    # 在Plotter类中添加以下方法
    def plot_violin(self, data: List[np.ndarray], x_labels: List[str], y_label: str,
                    legend_label_list: List[str] = None,
                    title: str = None, save_root: str = "./", filename: str = "violin_demo.png",
                    is_show: bool = False):
        # 如果 save_root 没有创建，则创建一个
        os.makedirs(save_root, exist_ok=True)
        fig = plt.figure(figsize=self.figsize, dpi=self.dpi)

        # 创建violinplot
        parts = plt.violinplot(data, showmeans=True, showextrema=True, showmedians=True)

        # 设置violinplot的颜色和样式
        for i, (pc, color) in enumerate(zip(parts['bodies'], self.color_list)):
            pc.set_facecolor(color)
            pc.set_edgecolor(self.edge_color_list[i])
            pc.set_alpha(0.8)

        # 设置坐标轴和标题
        plt.xticks(np.arange(1, len(x_labels) + 1), x_labels, fontsize=self.tick_size)
        plt.xlabel("Categories", fontsize=self.label_size)
        plt.ylabel(y_label, fontsize=self.label_size)

        if title != None:
            plt.title(title, fontdict={'size': self.title_size})

        # 调整 tick 的字体大小
        plt.yticks(fontsize=self.tick_size)

        # 添加图例
        if legend_label_list is not None:
            legend_patches = [mpatches.Patch(color=color, label=label) for color, label in
                              zip(self.color_list, legend_label_list)]
            plt.legend(handles=legend_patches, fontsize=self.legend_size, loc='best')

        plt.tight_layout()
        savepath = os.path.join(save_root, filename)
        print(f"图片保存到:{savepath}")
        plt.savefig(savepath)

        # 展示图片
        if is_show:
            plt.show()
        # 释放内存
        plt.close()

    def plot_violin_twin(self, data: List[tuple], x_labels: List[str], y_label: str, legend_label_list: List[str] = None,
                    title: str = None, save_root: str = "./", filename: str = "violin_twin_demo.png", is_show: bool = False):
        # 如果 save_root 没有创建，则创建一个
        os.makedirs(save_root, exist_ok=True)
        fig = plt.figure(figsize=self.figsize, dpi=self.dpi)

        for i, group_tuple in enumerate(data):
            for j, group_data in enumerate(group_tuple):
                # 计算核密度估计值
                kde = stats.gaussian_kde(group_data)
                positions = np.linspace(min(group_data), max(group_data), 100)
                density = kde(positions)

                # 判断是左半边还是右半边
                side = -1 if j % 2 == 0 else 1

                # 绘制violin半边
                plt.fill_betweenx(positions, i + 1 + side * density / 2, i + 1 - side * density / 2,
                                  color=self.color_list[j], alpha=0.8)

        # 设置坐标轴和标题
        plt.xticks(np.arange(1, len(x_labels) + 1), x_labels, fontsize=self.tick_size)
        plt.xlabel("Categories", fontsize=self.label_size)
        plt.ylabel(y_label, fontsize=self.label_size)

        if title != None:
            plt.title(title, fontdict={'size': self.title_size})

        # 调整 tick 的字体大小
        plt.yticks(fontsize=self.tick_size)

        # 添加图例
        if legend_label_list is not None:
            legend_patches = [mpatches.Patch(color=color, label=label) for color, label in zip(self.color_list, legend_label_list)]
            plt.legend(handles=legend_patches, fontsize=self.legend_size, loc='best')

        plt.tight_layout()
        savepath = os.path.join(save_root, filename)
        print(f"图片保存到:{savepath}")
        plt.savefig(savepath)

        # 展示图片
        if is_show:
            plt.show()

        # 释放内存
        plt.close()
