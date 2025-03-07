def index_join(df1, df2, how='inner'):
    """
    Join two dataframes based on their index.

    Args:
        df1 (pd.DataFrame): The first dataframe.
        df2 (pd.DataFrame): The second dataframe.
        how (str): Type of join to perform. Options: 'inner', 'outer', 'left', 'right'.

    Returns:
        pd.DataFrame: The joined dataframe.
    """
    return df1.join(df2, how=how)