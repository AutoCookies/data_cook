import logging
from collections import defaultdict

def json_basic_group(data: dict, list_key: str, group_columns: list) -> dict:
    """
    Group JSON data by specified columns.

    Args:
        data (dict): JSON object containing a list.
        list_key (str): The key of the list inside the JSON.
        group_columns (list): A list of column names to group by.

    Returns:
        dict: A dictionary where keys are grouped values (as strings) and values are lists of grouped items.
    """
    if not isinstance(data, dict) or not isinstance(group_columns, list):
        raise ValueError("data must be a dict and group_columns must be a list")
    
    grouped = defaultdict(list)

    try:
        # Lấy danh sách từ khóa list_key trong JSON
        if list_key not in data:
            raise KeyError(f"Key '{list_key}' not found in data")
        
        data_list = data[list_key]

        for row in data_list:
            if not isinstance(row, dict):
                raise ValueError("Each element in data must be a dictionary")
            
            # Chuyển tuple key thành string để JSON có thể xử lý
            key = "_".join(str(row[col]) for col in group_columns if col in row)
            grouped[key].append(row)

        return dict(grouped)
    
    except Exception as e:
        logging.error(f"An error occurred while grouping data: {str(e)}")
        raise
