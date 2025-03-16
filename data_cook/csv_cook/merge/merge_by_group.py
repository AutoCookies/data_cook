def merge_by_group(df1, df2, group_column, how='inner', suffixes=('_left', '_right')):
    """
    Merge two dataframes by grouping them on a common column and then merging the groups.

    Args:
        df1 (pd.DataFrame): The first dataframe.
        df2 (pd.DataFrame): The second dataframe.
        group_column (str or list): The column(s) to group by.
        how (str): Type of merge to perform. Options: 'inner', 'outer', 'left', 'right'.
        suffixes (tuple): Suffixes to add to overlapping columns.

    Returns:
        pd.DataFrame: The merged dataframe.
    """
    df1_indexed = df1.set_index(group_column)
    df2_indexed = df2.set_index(group_column)
    merged_indexed = df1_indexed.join(df2_indexed, how=how, lsuffix=suffixes[0], rsuffix=suffixes[1])
    return merged_indexed.reset_index(drop=True)
