import pandas as pd

def merge_by_group_and_condition(df1, df2, group_column, condition_column, condition_value, how='inner'):
    """
    Merge two dataframes based on group and apply a condition after merging.

    Args:
        df1 (pd.DataFrame): The first dataframe.
        df2 (pd.DataFrame): The second dataframe.
        group_column (str): The column to group by.
        condition_column (str): The column to apply the condition on.
        condition_value: The value to filter the condition column.
        how (str): Type of merge to perform. Options: 'inner', 'outer', 'left', 'right'.

    Returns:
        pd.DataFrame: The merged dataframe.
    """
    
    merged = pd.merge(df1, df2, on=group_column, how=how)
    
    return merged[merged[condition_column] == condition_value]