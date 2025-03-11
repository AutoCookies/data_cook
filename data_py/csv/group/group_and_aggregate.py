import logging
import pandas as pd

def group_and_aggregate(dataframe: pd.DataFrame, group_cols, aggregation_dict):
    """
    Group the dataframe by specified columns and perform aggregation.

    Args:
        dataframe (pd.DataFrame): The input dataframe.
        group_cols (str or list): Column(s) to group by.
        aggregation_dict (dict): Aggregation operations for each column.
            Example: {'value': ['sum', 'mean'], 'count': 'max'}

    Returns:
        pd.DataFrame: Dataframe with grouped and aggregated results.
    """
    if not dataframe or not group_cols or not aggregation_dict:
        raise ValueError("dataframe, group_cols, and aggregation_dict cannot be None")

    try:
        return dataframe.groupby(group_cols, sort=False).agg(aggregation_dict)
    except Exception as error:
        raise RuntimeError(f"Error during aggregation: {str(error)}")
