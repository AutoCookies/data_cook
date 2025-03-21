import json

def drop_keys(data, keys):
    """
    Drop multiple keys from a nested JSON structure and return the modified copy.

    Parameters
    ----------
    data : dict or list
        The JSON structure to drop the keys from.
    keys : list or set
        The keys to drop.

    Returns
    -------
    dict or list
        A new JSON structure with specified keys removed.

    Notes
    -----
    - The function does not modify the input data.
    - Works recursively for nested dictionaries and lists.
    """
    if isinstance(data, dict):
        # Xóa các key và tạo một dictionary mới
        return {k: drop_keys(v, keys) for k, v in data.items() if k not in keys}

    elif isinstance(data, list):
        # Xử lý từng phần tử trong danh sách
        return [drop_keys(item, keys) if isinstance(item, (dict, list)) else item for item in data]

    return data  # Nếu không phải dict hoặc list, giữ nguyên