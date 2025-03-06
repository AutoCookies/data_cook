def group_and_transform(df, group_column, transform_column, transform_func):
    """
    Group the dataframe by a column and apply a transformation to each group.

    Args:
        df (pd.DataFrame): The input dataframe.
        group_column (str or list): The column(s) to group by.
        transform_column (str): The column to apply the transformation to.
        transform_func (function): The transformation function.

    Returns:
        pd.DataFrame: A dataframe with the transformed column.
    """
    df[f'transformed_{transform_column}'] = df.groupby(group_column)[transform_column].transform(transform_func)
    return df