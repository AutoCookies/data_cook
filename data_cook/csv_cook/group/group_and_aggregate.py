import pandas as pd

def group_and_aggregate(dataframe: pd.DataFrame, group_cols, aggregation_dict):
    """
    Group the dataframe by specified columns and perform aggregation.

    Args:
        dataframe (pd.DataFrame): The input dataframe.
        group_cols (str or list): Column(s) to group by.
        aggregation_dict (dict): Aggregation operations for each column.

    Returns:
        pd.DataFrame: Dataframe with grouped and aggregated results.
    """
    # Kiểm tra kiểu dữ liệu của dataframe
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("dataframe must be a pandas DataFrame")
    
    # Kiểm tra dataframe không được rỗng
    if dataframe.empty:
        raise ValueError("dataframe cannot be empty")
    
    # Kiểm tra kiểu dữ liệu của group_cols (chuỗi hoặc danh sách)
    if not isinstance(group_cols, (str, list)):
        raise TypeError("group_cols must be a string or a list of strings")
    
    # Kiểm tra kiểu dữ liệu của aggregation_dict
    if not isinstance(aggregation_dict, dict):
        raise TypeError("aggregation_dict must be a dictionary")
    
    # Kiểm tra sự tồn tại của các cột trong dataframe
    missing_columns = set([group_cols] if isinstance(group_cols, str) else group_cols) - set(dataframe.columns)
    if missing_columns:
        raise KeyError(f"Columns {missing_columns} not found in dataframe")
    
    missing_agg_columns = set(aggregation_dict.keys()) - set(dataframe.columns)
    if missing_agg_columns:
        raise KeyError(f"Columns {missing_agg_columns} not found in dataframe")

    try:
        return dataframe.groupby(group_cols, sort=False).agg(aggregation_dict)
    except Exception as error:
        raise RuntimeError(f"Error during aggregation: {str(error)}")
