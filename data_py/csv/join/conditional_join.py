def conditional_join(df1, df2, condition):
    """
    Join two dataframes based on a condition.

    Args:
        df1 (pd.DataFrame): The first dataframe.
        df2 (pd.DataFrame): The second dataframe.
        condition (pd.Series): A boolean series representing the condition.

    Returns:
        pd.DataFrame: The joined dataframe.
    """
    return df1[condition].join(df2, how='inner')