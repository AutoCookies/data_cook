def group_and_aggregate(df, group_column, agg_dict):
    """
    Group the dataframe by a column and calculate aggregate statistics.

    Args:
        df (pd.DataFrame): The input dataframe.
        group_column (str or list): The column(s) to group by.
        agg_dict (dict): A dictionary specifying the aggregation operations for each column.
                         Example: {'value': ['sum', 'mean'], 'count': 'max'}

    Returns:
        pd.DataFrame: A dataframe with the grouped and aggregated results.
    """
    return df.groupby(group_column).agg(agg_dict)