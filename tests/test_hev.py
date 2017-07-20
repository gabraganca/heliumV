"""
Test functions
"""
from heliumv import HeV
import pandas as pd

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
