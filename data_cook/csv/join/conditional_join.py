import pandas as pd
import logging

def join_on_condition(left: pd.DataFrame, right: pd.DataFrame, condition: pd.Series) -> pd.DataFrame:
    """
    Join two dataframes based on a condition.

    Args:
        left (pd.DataFrame): The left dataframe.
        right (pd.DataFrame): The right dataframe.
        condition (pd.Series): A boolean series representing the condition.

    Returns:
        pd.DataFrame: The joined dataframe.
    """
    if left is None or right is None:
        raise ValueError("Both dataframes must be provided.")
    
    if condition is None:
        raise ValueError("Condition must be provided.")

    if not isinstance(condition, pd.Series):
        raise TypeError("Condition must be a pandas Series.")

    if condition.empty:
        raise ValueError("Condition cannot be empty.")

    # Filter the left dataframe
    filtered_left = left.loc[condition]

    # Join with the right dataframe using the index
    joined = filtered_left.join(right, how='inner')

    return joined
