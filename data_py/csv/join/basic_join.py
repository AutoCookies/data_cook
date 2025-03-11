import pandas as pd
import logging

def join_dataframes(df1: pd.DataFrame, df2: pd.DataFrame, join_column: str, join_type: str = 'inner') -> pd.DataFrame:
    """
    Join two dataframes based on a common column.

    Args:
        df1 (pd.DataFrame): The first dataframe.
        df2 (pd.DataFrame): The second dataframe.
        join_column (str): The column to join on.
        join_type (str): Type of join to perform. Options: 'inner', 'outer', 'left', 'right'.

    Returns:
        pd.DataFrame: The joined dataframe.
    """
    if df1 is None or df2 is None:
        raise ValueError("Both dataframes must be provided.")

    if not isinstance(join_column, str):
        raise ValueError("The join_column argument must be a string.")

    if join_type not in ['inner', 'outer', 'left', 'right']:
        raise ValueError("Invalid join type. Valid options are 'inner', 'outer', 'left', 'right'.")

    if join_column not in df1.columns or join_column not in df2.columns:
        raise ValueError(f"The column '{join_column}' does not exist in one of the dataframes.")

    return pd.merge(df1, df2, on=join_column, how=join_type, copy=False, validate="one_to_one")
