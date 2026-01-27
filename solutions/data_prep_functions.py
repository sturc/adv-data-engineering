import pandas as pd

def calc_avg_over_col(df:pd.DataFrame, col_name:str)->float:
    col_avg = df[col_name].mean()
    return col_avg

def fill_df_null_cols_with_avg(df:pd.DataFrame,col_names:list)->pd.DataFrame:
   avg_values = {}
   for curr_col in col_names :
      avg_values[curr_col] = round(calc_avg_over_col(df, curr_col))
      print (avg_values[curr_col])
   df_with_filled_nulls = df.fillna(avg_values)
   return df_with_filled_nulls
