import pandas as pd

def conditional_merge(df1, df2, condition):
    """
    Merge two dataframes based on a condition.

    Args:
        df1 (pd.DataFrame): The first dataframe.
        df2 (pd.DataFrame): The second dataframe.
        condition (pd.Series): A boolean series representing the condition.

    Returns:
        pd.DataFrame: The merged dataframe.
    """
    return pd.merge(df1[condition], df2, left_index=True, right_index=True)