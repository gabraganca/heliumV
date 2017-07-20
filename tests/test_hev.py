"""
Test functions
"""
import numpy as np
import pandas as pd
from heliumv import HeV

def test_HeV():

    df_type = type(pd.DataFrame())

    grid10 = HeV(10)
    assert isinstance(grid10.grid_df, df_type)

    grid50 = HeV(50)
    assert isinstance(grid50.grid_df, df_type)


    try:
        grid_null = HeV()
    except TypeError:
        pass

    try:
        grid_wrong = HeV(40)
    except RuntimeError:
        pass

def test_vsini_4026_10k():
    """
    Check if vsini values of the HeI@4026 on the 10k grid
    """
    hei_line = 4026
    grid10 = HeV(10)

    vsini_vals = range(0, 401, 50)

    # For teff = 15000 K
    teff = 15000
    fwhm_vals = [1.65, 2.02, 3.02, 4.09, 5.03, 5.98, 6.95, 7.97, 9.02999]
    for fwhm, vsini in zip(fwhm_vals, vsini_vals):
        assert np.allclose(grid10.get_vsini(teff, hei_line, fwhm), vsini)

    # For teff = 20000 K
    teff = 20000
    fwhm_vals = [1.96, 2.59, 3.45, 4.25, 5.08, 6., 6.92, 7.89, 8.86999]
    for fwhm, vsini in zip(fwhm_vals, vsini_vals):
        assert np.allclose(grid10.get_vsini(teff, hei_line, fwhm), vsini)

    # For teff = 25000 K
    teff = 25000
    fwhm_vals = [1.84000000001, 2.36, 3.19, 4.03, 4.88, 5.79, 6.74, 7.73, 8.72]
    for fwhm, vsini in zip(fwhm_vals, vsini_vals):
        assert np.allclose(grid10.get_vsini(teff, hei_line, fwhm), vsini)

    # For teff = 30000 K
    teff = 30000
    fwhm_vals = [1.64000000001, 2.1, 2.92, 3.82, 4.7, 5.65, 6.63, 7.63, 8.63]
    for fwhm, vsini in zip(fwhm_vals, vsini_vals):
        assert np.allclose(grid10.get_vsini(teff, hei_line, fwhm), vsini)
