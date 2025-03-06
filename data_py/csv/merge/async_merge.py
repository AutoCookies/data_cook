import pandas as pd

def async_merge(df1, df2, on_column, tolerance):
    """
    Merge two dataframes based on the closest values in a column.

    Args:
        df1 (pd.DataFrame): The first dataframe.
        df2 (pd.DataFrame): The second dataframe.
        on_column (str): The column to merge on.
        tolerance (float): The maximum allowed difference between values.

    Returns:
        pd.DataFrame: The merged dataframe.
    """
    df1 = df1.sort_values(by=on_column).reset_index(drop=True)
    df2 = df2.sort_values(by=on_column).reset_index(drop=True)
    merged = pd.merge_asof(df1, df2, on=on_column, tolerance=tolerance)
    return merged