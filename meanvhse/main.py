import os
from io import StringIO
import numpy as np
import pandas as pd
from scipy.interpolate import RectBivariateSpline, interp1d

TEFF_VALUES = range(15000, 30001, 5000)


class MeanVshe():
    """Obtain vsini from Teff and FWHM of a He I line.
    """

    def __init__(self, grid_res):

        # Test grid resolution
        if str(grid_res) not in ['10', '50']:
            raise RuntimeError('The grid resolution should be 10 or 50.')
        else:
            self.grid_res = grid_res

        # Load the grid
        self._load_grid()


    def _load_grid(self):
        """
        Read the grid in the file into a Pandas DataFrame

        Parameters
        ----------

        resolution: int,str:
            The resolution of the grid. It can be 10 or 50.
        """
        this_dir, _ = os.path.split(__file__)

        with open(this_dir +'/grids/grid{}K.dat'.format(self.grid_res)) as grid:
            grids = grid.read().split('\n\n')

        read_grid = lambda grid: pd.read_csv(StringIO(grid),
                                             delim_whitespace=True,
                                             names=['vsini', 4026, 4388, 4471],
                                             skiprows=1)


        grid_dic = {teff:read_grid(g) for teff, g in zip(TEFF_VALUES, grids)}
        self.grid_df = pd.concat(grid_dic, axis=0)


    def get_vsini(self, teff, he_line, fwhm):
        """
        Obtain the vsini from the FWHM of a HeI line
        and for a specific temperature.



        Parameters
        ----------

        teff: int, float;
            Effective temperature between 15000 and 30000 K

        he_line: int;
            The He I line. it can be the lines at 4026, 4388 and 4471 angstroms.

        fwhm: float;
            The Full Width and Half Maximum of the He I line.
        """

        # Test if values given are OK
        if (teff < 15000) or (teff > 30000):
            raise RuntimeError('teff should be between 15000 and 30000 K.')

        if he_line not in [4026, 4388, 4471]:
            raise RuntimeError('he_line should be 4026, 4388 or 4471.')

        # Obtain the FWHM measured for the desired HeI line
        fwhm_meshgrid = self.grid_df[he_line].values.reshape(4, 9)

        # Calculate a spline of the FWHM to be interpolated
        vsini_values = range(0, 401, 50)
        spl = RectBivariateSpline(TEFF_VALUES, vsini_values, fwhm_meshgrid)

        # Invert the interpolation above for a specific temperature.
        # It creates a interpolation of the FWHM with vsini and returns
        # the vsini for the FWHM given by the user

        vsini_vals = range(0, 401, 1)
        fwhm_vals = spl.ev(teff, vsini_vals)

        interp = interp1d(fwhm_vals, vsini_vals)

        try:
            return interp([fwhm])[0]
        except ValueError:
            # Value of FWHM is outside the grid
            return np.nan
