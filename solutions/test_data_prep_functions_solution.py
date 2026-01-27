from data_prep_functions import calc_avg_over_col, fill_df_null_cols_with_avg
import pandas as pd

def test_calc_avg_over_col():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]
    }
    df = pd.DataFrame(data)
    
    avg_A = calc_avg_over_col(df, 'A')
    avg_B = calc_avg_over_col(df, 'B')
    
    assert avg_A == 3.0, f"Expected average of column A to be 3.0 but got {avg_A}"
    assert avg_B == 30.0, f"Expected average of column B to be 30.0 but got {avg_B}"

def test_fill_df_null_cols_with_avg():
    data = {
        'A': [1, 2, None, 4, 5],
        'B': [10, None, 30, None, 50],
        'C': [100, 200, 300, 400, 500]
    }
    df = pd.DataFrame(data)
    
    filled_df = fill_df_null_cols_with_avg(df, ['A', 'B'])
    
    expected_A_avg = (1 + 2 + 4 + 5) / 4
    expected_B_avg = (10 + 30 + 50) / 3
    
    assert filled_df['A'].isnull().sum() == 0, "Column A still has null values after filling."
    assert filled_df['B'].isnull().sum() == 0, "Column B still has null values after filling."
    assert filled_df.loc[2, 'A'] == expected_A_avg, f"Expected filled value in column A to be {expected_A_avg} but got {filled_df.loc[2, 'A']}"
    assert filled_df.loc[1, 'B'] == expected_B_avg, f"Expected filled value in column B to be {expected_B_avg} but got {filled_df.loc[1, 'B']}"
    assert filled_df.loc[3, 'B'] == expected_B_avg, f"Expected filled value in column B to be {expected_B_avg} but got {filled_df.loc[3, 'B']}"