from plot import Plotter
import numpy as np

def test_violin():
    # 创建一个Plotter实例
    plotter = Plotter(
        figsize=(8, 6),
        font_thirdparty="SimSun",
        font="Arial Unicode MS"
    )

    # 准备数据
    data = [np.random.normal(0, 1, 100), np.random.normal(1, 2, 100), np.random.normal(2, 1, 100)]
    x_labels = ['类别 1', 'Category 2', 'Category 3']
    y_label = 'Value值'
    legend_label_list = ['组 1', 'Group 2', 'Group 3']

    # 绘制violin图，添加图例
    plotter.plot_violin(data, x_labels, y_label, legend_label_list, title='Violin Plot with Legend Demo', is_show=True, save_root="./results")


def test_violin_twin():
    # 创建一个Plotter实例
    plotter = Plotter(
        figsize=(8, 6),
        font_thirdparty="SimSun",
        font="Arial Unicode MS"
    )

    # 准备数据
    data = [(np.random.normal(0, 1, 100), np.random.normal(1, 2, 100)), (np.random.normal(2, 1, 100),
            np.random.normal(3, 1, 100))]
    x_labels = ['类别 1', 'Category 2']
    y_label = 'Value值'
    legend_label_list = ['组 1', 'Group 2']

    # 绘制半边violin图，添加图例
    plotter.plot_violin_twin(data, x_labels, y_label, legend_label_list, title='Half 小提琴Violin Plot with Legend Demo',
                        is_show=True, save_root="./results")


def test_stack_bars():
    # 创建一个Plotter实例
    plotter = Plotter(
        figsize=(8, 6),
        font_thirdparty="SimSun",
        font="Arial Unicode MS"
    )

    # 准备数据
    x_data = ['A艾', 'B不', 'C', 'D', 'E']
    bar_data_list = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
    legend_label_list = ['分类 1', '分类 2', '分类 3']

    plotter.plot_stack_bars(x_label="x-轴", y_label="y-轴", legend_title="Categories分类", legend_ncol=1, bbox_to_anchor=None,
                      y_tick_ndigits=2,
                      legend_loc="best", x_data=x_data, bar_data_list=bar_data_list,
                      legend_label_list=legend_label_list, y_min=None, y_max=None,
                      x_grid=False, y_grid=True, save_root="./results", filename="plot_stack_bars", is_show=True)


def test_chinese_stack_bars():
    # 创建一个Plotter实例
    plotter = Plotter(
        figsize=(8, 6),
        font="Arial Unicode MS",
        font_thirdparty="SimSun"
    )

    # 准备数据
    x_data = ['A', 'B', 'C', 'D', 'E']
    bar_data_list = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
    legend_label_list = ['分类 1', '分类 2', '分类 3']

    plotter.plot_stack_bars(x_label="x-axis", y_label="y-axis", legend_title="Categories", legend_ncol=1, bbox_to_anchor=None,
                      y_tick_ndigits=2,
                      legend_loc="best", x_data=x_data, bar_data_list=bar_data_list,
                      legend_label_list=legend_label_list, y_min=None, y_max=None,
                      x_grid=False, y_grid=True, save_root="./results", filename="plot_chinese_stack_bars", is_show=True)


def test_plot_lines_cdf_boxes():
    my_plotter = Plotter(figsize=(8, 6), font_thirdparty="SimHei", font="Arial Unicode MS")

    y1 = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]
    y2 = [-1, 0, 1, 0, -1, -1, 0, 1, 0, -1]
    y3 = [1, 2, 3, 4, 2, 4, 6, 1, 5, 1]
    y4 = [1, 6, 3, 8, 6, 4, 3, 1, 3, 0]
    y5 = [0, 2, 3, 4, 2, 1, 6, 8, 5, 1]
    y11 = [10000, 20000, 30000, 20000, 10000, 20000, 30000, 20000, 10000, 20000]
    y22 = [-10000, 0, 10000, 0, -10000, -10000, 0, 10000, 0, -10000]
    #
    my_plotter.plot_lines(
        x_list=[[i for i in range(len(y1))] for i in range(5)],
        line_data_list=[y1, y2],
        legend_label_list=["y1", "y2"],
        data_label_list=[["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
                         ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]],
        x_label="X轴",
        y_label="Y轴",
        x_grid=True,
        y_grid=True,
        y_min=-10,
        y_max=10,
        is_marker=True,
        legend_loc="best",
        legend_title="Legend",
        title="This is a demo!",
        save_root="./results",
        filename="plot_lines_demo"
    )
    my_plotter.plot_lines(
        x_list=[[i for i in range(len(y1))] for i in range(5)],
        line_data_list=[y11, y22],
        legend_label_list=["y11", "y22"],
        data_label_list=[["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
                         ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]],
        x_label="X",
        y_label="Y",
        y_tick_interval=20000,
        x_grid=True,
        y_grid=True,
        y_min=None,
        y_max=None,
        is_x_tick_sci=False,
        is_y_tick_sci=True,
        x_tick_ndigits=0,
        y_tick_ndigits=0,
        is_marker=True,
        legend_loc="best",
        legend_title="Legend",
        title="This is a demo!",
        save_root="./results",
        filename="plot_lines_sci_demo"
    )

    my_plotter.plot_cdfs(
        cdf_data_list=[y1, y2, y3, y4, y5],
        legend_label_list=["y1以", "y2为", "y3", "y4", "y5"],
        legend_loc="best",
        x_label="X轴",
        y_label="Y轴",
        legend_title="Legend图例",
        save_root="./results",
        filename="plot_cdfs_demo"
    )

    my_plotter.plot_boxes(
        x=["2.0", "1.0", "三", ],
        box_data_list=[[y1, y2, y3], [y2, y3, y5], [y4, y5, y1], [y4, y1, y2]],
        legend_label_list=["一万二", "2345", "3451", "4512"],
        x_label="x轴",
        y_label="y轴",
        is_data_label=True,
        legend_title="Legend图例",
        save_root="./results",
        filename="plot_boxes_demo"
    )


def test_plot_bars():
    my_plotter = Plotter(figsize=(8, 6), font_thirdparty="SimHei", font="Arial Unicode MS")
    my_plotter.plot_bars(
        x_data=["0零", "1.0", "2", "3.5"],
        bar_data_list=[
            [1, 2, 3, 4],
            [2, 3, 4, 5],
            [3, 4, 5, 6],
            [7, 8, 9, 10]
        ],
        legend_label_list=["1一", "2二", "3三", "4四"],
        x_label="X轴",
        y_label="Y轴",
        legend_title="Legend图例",
        save_root="./results",
        filename="plot_bars_demo"
    )

def test_plot_error_grids():
    my_plotter = Plotter(figsize=(8, 6), font_thirdparty="SimHei", font="Arial Unicode MS")
    my_plotter.plot_error_grids(
        ms=[1, 1, 1, 2, 2, 3, 3, 3, 3],
        ns=[4, 5, 6, 4, 5, 6, 4, 5, 6],
        ys=[1, 1, 1, 1, 1, 1, 1, 1, 1],
        predict_ys=[1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
        x_label="X轴",
        y_label="Y周",
        legend_label="Error误差",
        save_root="./results",
        filename="plot_error_grids_demo"
    )

def test_plot_grids():
    my_plotter = Plotter(figsize=(8, 6), font_thirdparty="SimHei", font="Arial Unicode MS")
    my_plotter.plot_grids(
        x_list=[1, 1, 1, 2, 2, 3, 3, 3, 3],
        y_list=[4, 5, 6, 4, 5, 6, 4, 5, 6],
        z_list=[1.1, 2.2, 1.3, 1.4, 4.5, 1.6, 1.7, 1.8, 4.9],
        x_label="X轴",
        y_label="Y轴",
        legend_label="Error误差",
        save_root="./results",
        filename="plot_grids_demo"
    )

def test_plot_acc_bars():
    my_plotter = Plotter(figsize=(8, 6), font_thirdparty="SimHei", font="Arial Unicode MS")
    my_plotter.plot_acc_bars(
        bar_data_list=[
            [1, 2, 3, 4],
            [2, 3, 4, 5],
            [3, 4, 5, 6],
            [7, 8, 9, 10]
        ],
        legend_label_list=["1一", "2二", "3", "4"],
        x_label="X轴",
        y_label="Y轴",
        save_root="./results",
        filename="plot_acc_bars_demo",
        legend_title="Legend图例",
        y_min=0,
        y_max=40,
    )


def test_plot_bars_and_lines():
    x_data = ['A', 'B', 'C', 'D', 'E']
    bar_data_list = [[10, 20, 15, 25, 30], [15, 25, 20, 30, 35]]
    legend_label_list = ['Group 1', 'Group 2']
    line_data_list = [[5, 10, 8, 12, 15], [8, 12, 10, 14, 18]]
    # 使用默认参数以及一些简单的测试数据调用函数
    my_plotter = Plotter(figsize=(8, 6), font_thirdparty="SimHei", font="Arial Unicode MS")
    my_plotter.plot_bars_and_lines(
        x_data=x_data,
        bar_y_label="Bar Y轴",
        line_y_label="Line Y轴",
        bar_data_list=bar_data_list,
        legend_label_list=legend_label_list,
        line_data_list=line_data_list,
        save_root="./results",
        filename="plot_bars_and_lines",
        legend_title="Legend图例",
        bar_y_min=3,
        bar_y_max=40,
        line_y_min=0,
        line_y_max=20,
        bar_y_tick_ndigits=0,
        line_y_tick_ndigits=1,
        is_marker=True,
    )

def test_plot_bars_and_lines_with_legend():
    x_data = ['A', 'B', 'C', 'D', 'E']
    bar_data_list = [[10, 20, 15, 25, 30], [15, 25, 20, 30, 35]]
    legend_label_list = ['Group 1', 'Group 2']
    line_data_list = [[5, 10, 8, 12, 15], [8, 12, 10, 14, 18]]
    # 使用默认参数以及一些简单的测试数据调用函数
    my_plotter = Plotter(figsize=(8, 6), font_thirdparty="SimHei", font="Arial Unicode MS")
    my_plotter.plot_bars_and_lines_with_legend(
        x_data=x_data,
        bar_y_label="Bar Y轴",
        line_y_label="Line Y轴",
        bar_data_list=bar_data_list,
        legend_label_list=legend_label_list,
        bar_legend=True,
        line_legend=True,
        line_data_list=line_data_list,
        save_root="./results",
        filename="plot_bars_and_lines_with_legend",
        legend_title="Legend图例",
        bar_y_min=3,
        bar_y_max=40,
        line_y_min=0,
        line_y_max=20,
        bar_y_tick_ndigits=0,
        line_y_tick_ndigits=1,
        is_marker=True,
    )



if __name__ == "__main__":
    # test_violin()
    # test_violin_twin()
    # test_stack_bars()
    # test_plot_lines_cdf_boxes()
    # test_plot_bars()
    # test_plot_error_grids()
    # test_plot_grids()
    # test_plot_acc_bars()
    # test_chinese_stack_bars()
    # test_plot_bars_and_lines()
    test_plot_bars_and_lines_with_legend()

