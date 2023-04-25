from plot import Plotter


if __name__ == "__main__":
    my_plotter = Plotter(figsize=(8, 6))

    y1 = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]
    y2 = [-1, 0, 1, 0, -1, -1, 0, 1, 0, -1]
    y3 = [1, 2, 3, 4, 2, 4, 6, 1, 5, 1]
    y4 = [1, 6, 3, 8, 6, 4, 3, 1, 3, 0]
    y5 = [0, 2, 3, 4, 2, 1, 6, 8, 5, 1]

    my_plotter.plot_lines(
        x_list=[[i for i in range(len(y1))] for i in range(5)],
        line_data_list=[y1, y2],
        legend_label_list=["y1", "y2"],
        data_label_list=[["1","2","3","4","5","6","7","8","9","10"],["a","b","c","d","e","f","g","h","i","j"]],
        x_label="X",
        y_label="Y",
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

    my_plotter.plot_cdfs(
        cdf_data_list=[y1, y2, y3, y4, y5],
        legend_label_list=["y1", "y2", "y3", "y4", "y5"],
        legend_loc="best",
        legend_title="Legend",
        save_root="./results",
        filename="plot_cdfs_demo"
    )

    my_plotter.plot_boxes(
        x=["2.0", "1.0", "3",],
        box_data_list=[[y1, y2, y3], [y2, y3, y5], [y4, y5, y1], [y4, y1, y2]],
        legend_label_list=["1234", "2345", "3451", "4512"],
        x_label="x",
        y_label="y",
        is_data_label=True,
        save_root="./results",
        filename="plot_boxes_demo"
    )

    my_plotter.plot_bars(
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
        filename="plot_bars_demo"
    )

    my_plotter.plot_error_grids(
        ms=[1, 1, 1, 2, 2, 3, 3, 3, 3],
        ns=[4, 5, 6, 4, 5, 6, 4, 5, 6],
        ys=[1, 1, 1, 1, 1, 1, 1, 1, 1],
        predict_ys=[1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
        x_label="X",
        y_label="Y",
        legend_label="Error",
        save_root="./results",
        filename="plot_error_grids_demo"
    )

    my_plotter.plot_grids(
        x_list=[1, 1, 1, 2, 2, 3, 3, 3, 3],
        y_list=[4, 5, 6, 4, 5, 6, 4, 5, 6],
        z_list=[1.1, 2.2, 1.3, 1.4, 4.5, 1.6, 1.7, 1.8, 4.9],
        x_label="X",
        y_label="Y",
        legend_label="Error",
        save_root="./results",
        filename="plot_grids_demo"
    )

    my_plotter.plot_acc_bars(
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
