import pandas as pd
import logging

def group_and_filter(df: pd.DataFrame, group_column, filter_func):
    """
    Group the dataframe by a column and filter groups based on a condition.

    Args:
        df (pd.DataFrame): The input dataframe.
        group_column (str or list): The column(s) to group by.
        filter_func (function): A function to filter groups. It should return a boolean.

    Returns:
        pd.DataFrame: A dataframe containing only the filtered groups.
    """
    if (df is None) or (group_column is None) or (filter_func is None):
        raise ValueError("df, group_column, and filter_func cannot be None")
    
    try:
        grouped = df.groupby(group_column)
        filtered_groups = [group for name, group in grouped if filter_func(group)]
        
        logging(f"Filtered {len(df) - len(filtered_groups)} groups out of {len(df)} groups.")
        return pd.concat(filtered_groups)
    except Exception as e:
        logging.error(f"An error occurred while filtering groups: {str(e)}")