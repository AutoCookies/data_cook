import pandas as pd

def merge_by_group(df1, df2, group_column, how='inner', suffixes=('_left', '_right')):
    """
    Merge two dataframes by grouping them on a common column and then merging the groups.

    Args:
        df1 (pd.DataFrame): The first dataframe.
        df2 (pd.DataFrame): The second dataframe.
        group_column (str or list): The column(s) to group by.
        how (str): Type of merge to perform. Options: 'inner', 'outer', 'left', 'right'.
        suffixes (tuple): Suffixes to add to overlapping columns.

    Returns:
        pd.DataFrame: The merged dataframe.
    """
    # Nhóm dữ liệu trong cả hai DataFrame
    grouped1 = df1.groupby(group_column)
    grouped2 = df2.groupby(group_column)
    
    # Danh sách để lưu các nhóm đã ghép
    merged_groups = []
    
    # Lặp qua các nhóm trong df1
    for name, group1 in grouped1:
        # Kiểm tra xem nhóm có tồn tại trong df2 không
        if name in grouped2.groups:
            group2 = grouped2.get_group(name)
            # Ghép hai nhóm lại với nhau
            merged = pd.merge(group1, group2, on=group_column, how=how, suffixes=suffixes)
            merged_groups.append(merged)
    
    # Kết hợp tất cả các nhóm đã ghép thành một DataFrame
    return pd.concat(merged_groups)