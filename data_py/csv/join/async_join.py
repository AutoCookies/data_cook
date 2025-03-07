import pandas

def async_join(df1, df2, on_column, tolerance):
    """
    Join two dataframes based on the closest values in a column.

    Args:
        df1 (pd.DataFrame): The first dataframe.
        df2 (pd.DataFrame): The second dataframe.
        on_column (str): The column to join on.
        tolerance (float): The maximum allowed difference between values.

    Returns:
        pd.DataFrame: The joined dataframe.
    """
    df1 = df1.sort_values(by=on_column).reset_index(drop=True)
    df2 = df2.sort_values(by=on_column).reset_index(drop=True)
    return pd.merge_asof(df1, df2, on=on_column, tolerance=tolerance)