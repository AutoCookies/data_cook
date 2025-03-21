import json

def join_json(json1, json2, method="outer"):
    """
    Merge two JSON structures recursively based on the given method.

    Parameters
    ----------
    json1 : dict, list, or any type
        The first JSON data.
    json2 : dict, list, or any type
        The second JSON data.
    method : str, optional
        Merge method: "left", "right", "inner", "outer" (default is "outer").

    Returns
    -------
    Merged JSON structure (dict, list, or combined values).
    """
    if isinstance(json1, dict) and isinstance(json2, dict):
        if method == "inner":
            common_keys = json1.keys() & json2.keys()
        elif method == "left":
            common_keys = json1.keys()
        elif method == "right":
            common_keys = json2.keys()
        else:  # outer (default)
            common_keys = json1.keys() | json2.keys()
        
        merged = {}
        for key in common_keys:
            if key in json1 and key in json2:
                merged[key] = join_json(json1[key], json2[key], method)
            elif key in json1:
                merged[key] = json1[key]
            else:
                merged[key] = json2[key]
        return merged

    elif isinstance(json1, list) and isinstance(json2, list):
        return json1 + json2  # Nối danh sách (không ảnh hưởng bởi method)

    elif json1 == json2:
        return json1  # Nếu giống nhau, giữ nguyên

    return json1 if method == "left" else json2 if method == "right" else [json1, json2]

