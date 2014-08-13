# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.

import os

ROOT = os.path.abspath(os.path.dirname(__file__))


class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """

    def setup(self):

        import matplotlib
        matplotlib.use('Agg')

        from matplotlib import pyplot as plt
        self.fig = plt.figure()

        from astropy.io import fits
        self.msx_header = fits.Header.fromtextfile(os.path.join(ROOT, 'msx_header'))

    def time_basic_plot(self):

        from astropy.wcs import WCS
        from wcsaxes import WCSAxes

        ax = WCSAxes(self.fig, [0.15, 0.15, 0.7, 0.7],
                     wcs=WCS(self.msx_header))
        self.fig.add_axes(ax)

        ax.set_xlim(-0.5, 148.5)
        ax.set_ylim(-0.5, 148.5)

        self.fig.canvas.draw()

    def time_basic_plot_with_grid(self):

        from astropy.wcs import WCS
        from wcsaxes import WCSAxes

        ax = WCSAxes(self.fig, [0.15, 0.15, 0.7, 0.7],
                     wcs=WCS(self.msx_header))
        self.fig.add_axes(ax)

        ax.grid(color='red', alpha=0.5, linestyle='solid')

        ax.set_xlim(-0.5, 148.5)
        ax.set_ylim(-0.5, 148.5)

        self.fig.canvas.draw()
