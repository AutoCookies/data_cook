import pandas as pd 

def merge_with_operation(df1, df2, on_column, operation, how='inner'):
    """
    Merge two dataframes and apply an operation on corresponding columns.

    Args:
        df1 (pd.DataFrame): The first dataframe.
        df2 (pd.DataFrame): The second dataframe.
        on_column (str or list): The column(s) to merge on.
        operation (function): The operation to apply on corresponding columns.
        how (str): Type of merge to perform. Options: 'inner', 'outer', 'left', 'right'.

    Returns:
        pd.DataFrame: The merged dataframe.
    """
    merged = pd.merge(df1, df2, on=on_column, suffixes=('_left', '_right'), how=how)
    for col in df1.columns.intersection(df2.columns):
        if col != on_column:
            merged[col] = merged[[f'{col}_left', f'{col}_right']].apply(operation, axis=1)
            merged.drop(columns=[f'{col}_left', f'{col}_right'], inplace=True)
    return merged
