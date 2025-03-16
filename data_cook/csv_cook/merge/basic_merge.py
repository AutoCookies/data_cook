import pandas as pd

def basic_merge(df1, df2, on_column, how='inner'):
    """
    Merge two dataframes based on a common column.

    Args:
        df1 (pd.DataFrame): The first dataframe.
        df2 (pd.DataFrame): The second dataframe.
        on_column (str or list): The column(s) to merge on.
        how (str): Type of merge to perform. Options: 'inner', 'outer', 'left', 'right'.

    Returns:
        pd.DataFrame: The merged dataframe.
    """
    return pd.merge(df1, df2, on=on_column, how=how)