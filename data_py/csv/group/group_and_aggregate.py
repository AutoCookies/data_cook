import logging
import pandas as pd

def group_and_aggregate(df: pd.DataFrame, group_column, agg_dict):
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
    if (df is None) or (group_column is None) or (agg_dict is None):
        raise ValueError("df, group_column, and agg_dict cannot be None")
    
    try:
        logging.info("Grouping and aggregating data...")
        return df.groupby(group_column).agg(agg_dict)
    except Exception as e:
        logging.error(f"An error occurred while grouping and aggregating data: {str(e)}")