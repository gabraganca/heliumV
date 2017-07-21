"""
Test functions
"""
import numpy as np
import pandas as pd
from heliumv import HeV

VSINI_VALS = range(0, 401, 50)

def test_HeV():
    """Test HeV class initialization.

    It also test the `_load_grid' function scine it is initalizd together with
    the function.
    """

    df_type = type(pd.DataFrame())

    grid10 = HeV(10)
    assert isinstance(grid10.grid_df, df_type)

    grid50 = HeV(50)
    assert isinstance(grid50.grid_df, df_type)


    try:
        _ = HeV()
    except TypeError:
        pass

    try:
        _ = HeV(40)
    except RuntimeError:
        pass

def test_fwhm_outside_grid():
    """
    Test if nan returned if FHWM is outside the grid
    """

    assert HeV(10).get_vsini(15000, 4026, 0) is np.nan



class VsiniTest():
    """
    A constructor used to create tests to check visni from the knots in the
    grid.
    """

    def __init__(self, he_line, grid_resolution):
        self.he_line = he_line
        self.grid_resolution = grid_resolution

        self.grid = HeV(self.grid_resolution)
        self.fwhm_values = self._get_fwhm_values()

    def _get_fwhm_values(self):
        fwhm_dic = {4026:{
            15000:[1.65, 2.02, 3.02, 4.09, 5.03, 5.98, 6.95, 7.97, 9.02999],
            20000:[1.96, 2.59, 3.45, 4.25, 5.08, 6., 6.92, 7.89, 8.86999],
            25000:[1.84000000001, 2.36, 3.19, 4.03, 4.88, 5.79, 6.74, 7.73,
                   8.72],
            30000:[1.64000000001, 2.1, 2.92, 3.82, 4.7, 5.65, 6.63, 7.63, 8.63]}
                   }

        return fwhm_dic[self.he_line]

    def test(self):
        """run the test"""
        # Check values
        for teff in self.fwhm_values:
            for fwhm, vsini in zip(self.fwhm_values[teff], VSINI_VALS):
                try:
                    assert np.allclose(self.grid.get_vsini(teff, self.he_line,
                                                           fwhm),
                                       vsini)
                except AssertionError:
                    # print values for bugging tracking.
                    # I should probbaly implement logging here instead of using
                    # print messages
                    print(teff, fwhm, vsini)
                    raise

def test_vsini_4026_10k():
    """
    Check if vsini values of the HeI@4026 on the 10k grid
    """
    test = VsiniTest(4026, 10)
    test.test()
