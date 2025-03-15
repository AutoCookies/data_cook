import pandas as pd

def merge_with_suffix(df1, df2, on_column, suffixes=('_left', '_right'), how='inner'):
    """
    Merge two dataframes and add suffixes to overlapping columns.

    Args:
        df1 (pd.DataFrame): The first dataframe.
        df2 (pd.DataFrame): The second dataframe.
        on_column (str or list): The column(s) to merge on.
        suffixes (tuple): Suffixes to add to overlapping columns.
        how (str): Type of merge to perform. Options: 'inner', 'outer', 'left', 'right'.

    Returns:
        pd.DataFrame: The merged dataframe.
    """
    return pd.merge(df1, df2, on=on_column, suffixes=suffixes, how=how)
