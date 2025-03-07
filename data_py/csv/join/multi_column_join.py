def multi_column_join(df1, df2, on_columns, how='inner'):
    """
    Join two dataframes based on multiple common columns.

    Args:
        df1 (pd.DataFrame): The first dataframe.
        df2 (pd.DataFrame): The second dataframe.
        on_columns (list): The list of columns to join on.
        how (str): Type of join to perform. Options: 'inner', 'outer', 'left', 'right'.

    Returns:
        pd.DataFrame: The joined dataframe.
    """
    return df1.join(df2.set_index(on_columns), on=on_columns, how=how)