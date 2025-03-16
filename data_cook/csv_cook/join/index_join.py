def index_join(df1, df2, how='inner'):
    """
    Join two dataframes based on their index.

    This function performs an index-based join on two dataframes. The join is
    performed based on the index of the two dataframes. The type of join can be
    specified using the `how` parameter.

    Parameters
    ----------
    df1 : pd.DataFrame
        The first dataframe.
    df2 : pd.DataFrame
        The second dataframe.
    how : str, optional
        The type of join to perform. Options are 'inner', 'outer', 'left',
        'right'. Defaults to 'inner'.

    Returns
    -------
    pd.DataFrame
        The joined dataframe.
    """
    if df1 is None or df2 is None:
        raise ValueError("Both df1 and df2 must be provided.")

    if not isinstance(df1, pd.DataFrame) or not isinstance(df2, pd.DataFrame):
        raise ValueError("Both df1 and df2 must be pandas DataFrames.")

    if how not in ['inner', 'outer', 'left', 'right']:
        raise ValueError("Invalid join type. Valid options are 'inner', 'outer', 'left', 'right'.")

    # Use the map function to perform the join
    df1.index.map(df2.get)
