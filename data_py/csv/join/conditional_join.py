import pandas as pd
import logging

def conditional_join(df1: pd.DataFrame, df2: pd.DataFrame, condition):
    """
    Join two dataframes based on a condition.

    Args:
        df1 (pd.DataFrame): The first dataframe.
        df2 (pd.DataFrame): The second dataframe.
        condition (pd.Series): A boolean series representing the condition.

    Returns:
        pd.DataFrame: The joined dataframe.
    """
    try:
        if (df1 is None or df2 is None):
            raise ValueError("Both dataframes must be provided.")
        logging("Date joined")
        return df1[condition].join(df2, how='inner')
    except Exception as e:
        logging.error(f"An error occurred while joining data: {str(e)}")