from data_prep_functions import calc_avg_over_col, fill_df_null_cols_with_avg
import pandas as pd

def test_calc_avg_over_col():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]
    }
    df = pd.DataFrame(data)
    # TODO: Implement test for calc_avg_over_col
    

def test_fill_df_null_cols_with_avg():
    data = {
        'A': [1, 2, None, 4, 5],
        'B': [10, None, 30, None, 50],
        'C': [100, 200, 300, 400, 500]
    }
    df = pd.DataFrame(data)
    # TODO: Implement test for fill_df_null_cols_with_avg
    