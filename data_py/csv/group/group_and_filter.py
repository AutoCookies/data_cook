import pandas as pd

def group_and_filter(df, group_column, filter_func):
    """
    Group the dataframe by a column and filter groups based on a condition.

    Args:
        df (pd.DataFrame): The input dataframe.
        group_column (str or list): The column(s) to group by.
        filter_func (function): A function to filter groups. It should return a boolean.

    Returns:
        pd.DataFrame: A dataframe containing only the filtered groups.
    """
    grouped = df.groupby(group_column)
    filtered_groups = [group for name, group in grouped if filter_func(group)]
    return pd.concat(filtered_groups)