def group_and_merge(df, group_column, merge_column):
    """
    Group the dataframe by a column and merge groups based on another column.

    Args:
        df (pd.DataFrame): The input dataframe.
        group_column (str or list): The column(s) to group by.
        merge_column (str): The column to merge groups on.

    Returns:
        pd.DataFrame: A dataframe with merged groups.
    """
    grouped = df.groupby(group_column)
    merged_groups = []

    for _, group in grouped:
        merged_group = group.merge(df, on=merge_column, how='left')
        merged_groups.append(merged_group)

    return pd.concat(merged_groups)