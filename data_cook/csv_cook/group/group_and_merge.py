import pandas as pd
import logging

def group_and_merge(df: pd.DataFrame, group_column: str or list, merge_column: str) -> pd.DataFrame:
    """
    Group the dataframe by a column and merge groups based on another column.

    Args:
        df (pd.DataFrame): The input dataframe.
        group_column (str or list): The column(s) to group by.
        merge_column (str): The column to merge groups on.

    Returns:
        pd.DataFrame: A dataframe with merged groups.
    """
    if df is None or group_column is None or merge_column is None:
        raise ValueError("df, group_column, and merge_column cannot be None")

    try:
        grouped = df.groupby(group_column, as_index=False).agg(list)
        merged_groups = grouped.merge(df[[merge_column]], on=merge_column, how='left')
        return merged_groups
    except Exception as e:
        logging.error(f"An error occurred while merging groups: {str(e)}")
        raise
