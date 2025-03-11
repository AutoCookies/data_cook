import pandas as pd
import logging

def basic_join(df1: pd.DataFrame, df2: pd.DataFrame, on_column, how='inner'):
    """
    Join two dataframes based on a common column.

    Args:
        df1 (pd.DataFrame): The first dataframe.
        df2 (pd.DataFrame): The second dataframe.
        on_column (str): The column to join on.
        how (str): Type of join to perform. Options: 'inner', 'outer', 'left', 'right'.

    Returns:
        pd.DataFrame: The joined dataframe.
    """
    try:
        if (df1 is None or df2 is None):
            raise ValueError("Both dataframes must be provided.")
        logging("Date joined")
        return df1.join(df2.set_index(on_column), on=on_column, how=how)
    except Exception as e:
        logging.error(f"An error occurred while joining data: {str(e)}")