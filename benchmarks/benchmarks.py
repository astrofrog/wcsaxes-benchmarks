# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.

import os

from astropy.io import fits
from astropy.wcs import WCS
from wcsaxes import WCSAxes

# Use the OO interface to really benchmark WCSAxes and not pyplot

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

ROOT = os.path.abspath(os.path.dirname(__file__))


class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """

    def setup(self):

        self.msx_header = fits.Header.fromtextfile(os.path.join(ROOT, 'msx_header'))

    def time_basic_plot(self):

        fig = Figure()
        canvas = FigureCanvas(fig)

        ax = WCSAxes(fig, [0.15, 0.15, 0.7, 0.7],
                     wcs=WCS(self.msx_header))
        fig.add_axes(ax)

        ax.set_xlim(-0.5, 148.5)
        ax.set_ylim(-0.5, 148.5)

        canvas.draw()

    def time_basic_plot_with_grid(self):

        fig = Figure()
        canvas = FigureCanvas(fig)

        ax = WCSAxes(fig, [0.15, 0.15, 0.7, 0.7],
                     wcs=WCS(self.msx_header))
        fig.add_axes(ax)

        ax.grid(color='red', alpha=0.5, linestyle='solid')

        ax.set_xlim(-0.5, 148.5)
        ax.set_ylim(-0.5, 148.5)

        canvas.draw()
