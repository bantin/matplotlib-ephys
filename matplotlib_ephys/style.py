"""Style classes definition"""
from dataclasses import dataclass


@dataclass
class ExploreStyle:
    """ Default class used to configure the aspect of the ephys plots. All other Style classes
    should inherit from this class.

    Args:
        shared_axis (bool): if True, the voltage and current traces are plotted on the same axis.
        show_spines (bool): if True, shows the spine (frame) around the plots.
        scale_bars (bool): if True, draws mV, nA and ms scale bars on the plots.
        linewidth (float): width of the voltage and current traces.
        voltage_color (str): color of the voltage traces.
        voltage_alpha (float): transparency of the voltage traces.
        current_color (str): color of the current traces.
        current_alpha (float): transparency of the current traces.
        title_fontsize (float): fontsize of the title.
        scale_bars_fontsize (float): fontsize of the scale bar labels.
    """

    shared_axis: bool = False
    show_spines: bool = True
    scale_bars: bool = False

    linewidth: int = 1.

    voltage_color: str = "black"
    voltage_alpha: float = 1.
    current_color: str = "gray"
    current_alpha: float = 1.

    title_fontsize: int = 14.
    scale_bars_fontsize: int = 10.
    label_fontsize: int = 12.


@dataclass
class PaperStyle(ExploreStyle):
    """ Paper class to display voltage traces without splines and with scale bars."""

    shared_axis: bool = True
    show_spines: bool = False
    scale_bars: bool = True

    linewidth: int = 1.

    voltage_color: str = "black"
    voltage_alpha: float = 0.9
    current_color: str = "red"
    current_alpha: float = 0.9

    title_fontsize: int = 14.
    scale_bars_fontsize: int = 10.
    label_fontsize: int = 12.
