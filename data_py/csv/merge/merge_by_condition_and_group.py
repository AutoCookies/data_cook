import pandas as pd

def merge_by_condition_and_group(df1, df2, group_column, condition_column, condition_value, how='inner'):
    """
    Merge two dataframes based on a condition and group.

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
    # Lọc dữ liệu dựa trên điều kiện
    df1_filtered = df1[df1[condition_column] == condition_value]
    
    # Nhóm dữ liệu
    grouped = df1_filtered.groupby(group_column)
    
    # Ghép từng nhóm với df2
    merged_list = []
    for name, group in grouped:
        merged = pd.merge(group, df2, on=group_column, how=how)
        merged_list.append(merged)
    
    return pd.concat(merged_list)