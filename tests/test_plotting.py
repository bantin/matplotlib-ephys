"""Testing plotting functions"""
import numpy
import glob
import matplotlib.pyplot as plt
from matplotlib_ephys import plot_trace, plot_traces


def test_plotting_single_ephys():

    for i, file in enumerate(glob.glob("./test_data_*.npy")):

        data = numpy.load(file)

        for style in ["explore", "paper"]:

            # Plot without current
            fig, axis = plot_trace(
                data[0],
                data[2],
                style=style
            )
            plt.savefig(f"test_plot_trace_{style}_{i}_nocurrent.png")
            plt.close(fig)

            # Plot with current
            fig, axis = plot_trace(
                data[0],
                data[2],
                data[1],
                style=style
            )
            plt.savefig(f"test_plot_trace_{style}_{i}.png")
            plt.close(fig)

            # Plot with current and long title
            fig, axis = plot_trace(
                data[0],
                data[2],
                data[1],
                style=style,
                title="This is an extremely long title that should really "
                      "not exist but we will see what happens"
            )
            plt.savefig(f"test_plot_trace_{style}_{i}_title.png")
            plt.close(fig)


def test_plotting_multiple_ephys():

    data = []
    for i, file in enumerate(glob.glob("./test_data_*.npy")):
        data.append(numpy.load(file))
    data = numpy.array(data)

    for style in ["explore", "paper"]:

        # Plot without current
        fig, axis = plot_traces(
            data[:, 0],
            data[:, 2],
            style=style
        )
        plt.savefig(f"test_plot_multiple_traces_{style}_nocurrent.png")
        plt.close(fig)

        # Plot with current
        fig, axis = plot_traces(
            data[:, 0],
            data[:, 2],
            data[:, 1],
            style=style
        )
        plt.savefig(f"test_plot_multiple_traces_{style}.png")
        plt.close(fig)

        # Plot with current and long title
        fig, axis = plot_traces(
            data[:, 0],
            data[:, 2],
            data[:, 1],
            style=style,
            title="This is an extremely long title that should really "
                "not exist but we will see what happens"
        )
        plt.savefig(f"test_plot_multiple_traces_{style}_title.png")
        plt.close(fig)

        # Plot with current and long title
        fig, axis = plot_traces(
            data[:, 0],
            data[:, 2],
            data[:, 1],
            style=style,
            title=["This is an extremely long title that should really "
                  "not exist but we will see what happens"] * len(data)
        )
        plt.savefig(f"test_plot_multiple_traces_{style}_titles.png")
        plt.close(fig)

test_plotting_single_ephys()
test_plotting_multiple_ephys()
