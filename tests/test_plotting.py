"""Testing plotting functions"""
import numpy
import matplotlib.pyplot as plt

from matplotlib_ephys import plot_trace


def test_plotting():

    # Test that the function plot_trace works
    time_series = numpy.arange(0, 1000, 1)
    voltage_series = (numpy.random.random(size=1000) + 140.) - 70.
    current_series = numpy.random.random(size=1000) * 0.3

    for style in ["explore", "paper"]:
        fig, axis = plot_trace(
            time_series,
            voltage_series,
            current_series,
            style=style
        )
        plt.savefig(f"test_plot_trace_{style}.png")
        plt.show()
        plt.close(fig)


test_plotting()