import logging
import pandas as pd

def group_and_rank(dataframe: pd.DataFrame, group_by_column, rank_by_column, rank_ascending=True):
    """
    Group the dataframe by a column and rank rows within each group.

    Args:
        dataframe (pd.DataFrame): The input dataframe.
        group_by_column (str or list): The column(s) to group by.
        rank_by_column (str): The column to rank by.
        rank_ascending (bool): Whether to rank in ascending order.

    Returns:
        pd.DataFrame: A dataframe with an additional 'rank' column.
    """
    if dataframe is None or group_by_column is None or rank_by_column is None:
        raise ValueError("dataframe, group_by_column, and rank_by_column cannot be None")

    if not isinstance(dataframe, pd.DataFrame):
        raise ValueError("dataframe must be a pandas DataFrame")

    if not isinstance(group_by_column, (str, list)) or not isinstance(rank_by_column, str):
        raise ValueError("group_by_column must be a string or a list of strings, rank_by_column must be a string")

    if rank_by_column not in dataframe.columns:
        raise ValueError(f"Column '{rank_by_column}' does not exist in the dataframe")

    if group_by_column not in dataframe.columns:
        raise ValueError(f"Column '{group_by_column}' does not exist in the dataframe")

    try:
        return dataframe.assign(
            rank=dataframe.groupby(group_by_column)[rank_by_column].rank(
                ascending=rank_ascending, method='min'
            )
        )
    except Exception as error:
        logging.error(f"Error during grouping and ranking: {str(error)}")
        raise
