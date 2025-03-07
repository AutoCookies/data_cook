def join_with_suffix(df1, df2, on_column, how='inner', suffixes=('_left', '_right')):
    """
    Join two dataframes and add suffixes to overlapping columns.

    Args:
        df1 (pd.DataFrame): The first dataframe.
        df2 (pd.DataFrame): The second dataframe.
        on_column (str): The column to join on.
        how (str): Type of join to perform. Options: 'inner', 'outer', 'left', 'right'.
        suffixes (tuple): Suffixes to add to overlapping columns.

    Returns:
        pd.DataFrame: The joined dataframe.
    """
    return df1.join(df2.set_index(on_column), on=on_column, how=how, lsuffix=suffixes[0], rsuffix=suffixes[1])