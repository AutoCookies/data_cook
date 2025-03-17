import json

def find_merge_key(lst):
    """
    Xác định khóa chính để hợp nhất danh sách các dictionary.
    Nếu có 'id', 'name', 'title', hoặc 'key', chọn nó làm khóa chính.
    """
    possible_keys = {"id", "name", "title", "key"}
    if lst and isinstance(lst[0], dict):
        for key in possible_keys:
            if key in lst[0]:
                return key
    return None  # Không có khóa đặc biệt, chỉ nối danh sách

def merge_lists(list1, list2):
    """
    Hợp nhất hai danh sách. Nếu phần tử là dictionary, hợp nhất theo khóa chính.
    """
    merge_key = find_merge_key(list1) or find_merge_key(list2)
    
    if merge_key:
        merged_dict = {item[merge_key]: item for item in list1}
        for item in list2:
            key = item[merge_key]
            if key in merged_dict:
                merged_dict[key] = combine_json(merged_dict[key], item)  # Hợp nhất nếu trùng key
            else:
                merged_dict[key] = item
        return list(merged_dict.values())

    return list1 + list2  # Nếu không có key chung, chỉ đơn giản nối danh sách

def combine_json(json1, json2):
    """
    Hợp nhất hai JSON với quy tắc:
    - Nếu là dict → hợp nhất từng key
    - Nếu là list → hợp nhất danh sách theo khóa chính
    - Nếu khác nhau → đưa vào danh sách
    """
    if isinstance(json1, dict) and isinstance(json2, dict):
        combined_data = {}
        for key in set(json1.keys()).union(json2.keys()):
            if key in json1 and key in json2:
                combined_data[key] = combine_json(json1[key], json2[key])  # Gọi đệ quy nếu có cùng key
            else:
                combined_data[key] = json1.get(key, json2.get(key))
        return combined_data

    elif isinstance(json1, list) and isinstance(json2, list):
        return merge_lists(json1, json2)  # Gọi hàm hợp nhất danh sách

    elif json1 == json2:
        return json1  # Nếu giống nhau, giữ nguyên

    return [json1, json2]  # Nếu khác nhau, đóng gói thành list để giữ cả hai giá trị
