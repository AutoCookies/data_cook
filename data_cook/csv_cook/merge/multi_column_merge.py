import pandas as pd

def multi_column_merge(df1, df2, on_columns, how='inner'):
    """
    Merge two dataframes based on multiple common columns.

    Args:
        df1 (pd.DataFrame): The first dataframe.
        df2 (pd.DataFrame): The second dataframe.
        on_columns (list): The list of columns to merge on.
        how (str): Type of merge to perform. Options: 'inner', 'outer', 'left', 'right'.

    Returns:
        pd.DataFrame: The merged dataframe.
    """
    return pd.merge(df1, df2, on=on_columns, how=how)