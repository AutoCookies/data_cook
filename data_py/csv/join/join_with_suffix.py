def join_with_suffix(
    left_df: pd.DataFrame, right_df: pd.DataFrame, join_column: str,
    how: str = 'inner', suffixes: tuple = ('_left', '_right')
) -> pd.DataFrame:
    """
    Join two dataframes and add suffixes to overlapping columns.

    Parameters
    ----------
    left_df : pd.DataFrame
        The left dataframe.
    right_df : pd.DataFrame
        The right dataframe.
    join_column : str
        The column to join on.
    how : str, optional
        The type of join to perform. Options are 'inner', 'outer', 'left',
        'right'. Defaults to 'inner'.
    suffixes : tuple, optional
        The suffixes to add to overlapping columns. Defaults to ('_left',
        '_right').

    Returns
    -------
    pd.DataFrame
        The joined dataframe.
    """
    if not isinstance(left_df, pd.DataFrame) or not isinstance(right_df, pd.DataFrame):
        raise ValueError("Both dataframes must be pd.DataFrames")
    if not isinstance(join_column, str):
        raise ValueError("The join_column argument must be a string")
    if how not in ['inner', 'outer', 'left', 'right']:
        raise ValueError("how must be one of 'inner', 'outer', 'left', 'right'")
    if not isinstance(suffixes, tuple) or len(suffixes) != 2:
        raise ValueError("suffixes must be a tuple of length 2")

    left_indexed = left_df.set_index(join_column)
    right_indexed = right_df.set_index(join_column)
    merged_indexed = left_indexed.join(right_indexed, how=how, lsuffix=suffixes[0], rsuffix=suffixes[1])
    return merged_indexed.reset_index(drop=True)
