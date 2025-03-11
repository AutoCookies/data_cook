import logging
import pandas as pd

def group_and_rank(df: pd.DataFrame, group_column, rank_column, ascending=True):
    """
    Group the dataframe by a column and rank rows within each group.

    Args:
        df (pd.DataFrame): The input dataframe.
        group_column (str or list): The column(s) to group by.
        rank_column (str): The column to rank by.
        ascending (bool): Whether to rank in ascending order.

    Returns:
        pd.DataFrame: A dataframe with an additional 'rank' column.
    """
    try:
        df['rank'] = df.groupby(group_column)[rank_column].rank(ascending=ascending, method='min')
        logging.info("Data grouped")
        return df
    except Exception as e:
        logging.error(f"An error occurred while grouping and ranking data: {str(e)}")