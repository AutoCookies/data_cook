"""
    The idea is if user got a large JSON file, but got another smaller JSON file.
    But the smaller one has the same keys as the large json file.
    Or we could said the smaller one is the child of the bigger one
"""

def extract_keys_level(data, keys_by_level=None, level=0):
    """
    Recursively extract all keys from JSON and group them by nesting level.
    
    :param data: JSON data (dict or list)
    :param keys_by_level: Dictionary storing keys grouped by nesting level
    :param level: Current nesting level
    :return: Dictionary with keys grouped by level
    """
    if keys_by_level is None:
        from collections import defaultdict
        keys_by_level = defaultdict(set) 

    if isinstance(data, dict):
        for key, value in data.items():
            keys_by_level[level].add(key)
            extract_keys_level(value, keys_by_level, level + 1) 

    elif isinstance(data, list):
        for item in data:
            extract_keys_level(item, keys_by_level, level) 

    return keys_by_level

def can_combine_level(json1, json2):
    """
    Check if json2's keys are all present in json1.
    
    :param json1: The larger JSON object (dictionary or list).
    :param json2: The smaller JSON object.
    :return: True if json2 can be merged into json1, False otherwise.
    """
    keys1 = extract_keys_level(json1)
    keys2 = extract_keys_level(json2)

    # Lấy tất cả các key ở mọi cấp độ
    all_keys1 = set().union(*keys1.values())  
    all_keys2 = set().union(*keys2.values())

    return all_keys2.issubset(all_keys1)  # Kiểm tra json2 có phải tập con của json1 không

    