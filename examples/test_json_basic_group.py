import json
import os
from collections import defaultdict

# Đọc dữ liệu từ file JSON
json_file_path = os.path.join(os.path.dirname(__file__), "test.json")

with open(json_file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

keys_by_level = defaultdict(set)  # Dictionary lưu keys theo cấp độ (depth)

def extract_keys(data, level=0):
    """
    Trích xuất tất cả các key từ JSON và nhóm theo cấp độ lồng nhau (depth).

    Args:
        data (dict | list): Dữ liệu JSON đầu vào.
        level (int): Cấp độ hiện tại của JSON.
    """
    if isinstance(data, dict):
        for key, value in data.items():
            keys_by_level[level].add(key)  # Lưu key theo cấp độ
            extract_keys(value, level + 1)  # Đệ quy vào level tiếp theo

    elif isinstance(data, list):
        for item in data:
            extract_keys(item, level)  # List không tăng cấp độ vì không tạo thêm cấp JSON

# 🔹 Hàm tìm tất cả key có tên target_key trong JSON
def find_and_extract_keys(data, target_key):
    """
    Tìm tất cả key có tên target_key trong JSON và trích xuất keys bên trong object chứa nó.

    Args:
        data (dict | list): Dữ liệu JSON đầu vào.
        target_key (str): Tên key cần tìm.
    """
    if isinstance(data, dict):
        for key, value in data.items():
            if key == target_key:
                print(f"\n🔹 Trích xuất keys từ '{target_key}': {value}")  # Kiểm tra dữ liệu được tìm thấy
                # 🛠 Chỉ trích xuất keys nếu value là dict hoặc list
                if isinstance(value, (dict, list)):
                    extract_keys(value)
            else:
                find_and_extract_keys(value, target_key)  # Duyệt tiếp vào bên trong

    elif isinstance(data, list):
        for item in data:
            find_and_extract_keys(item, target_key)  # Duyệt tiếp vào từng phần tử danh sách

# Gọi hàm tìm và trích xuất key từ "department_name"
find_and_extract_keys(data, "employees")

# In keys theo cấp độ (chỉ in nếu có key)
if keys_by_level:
    print("\n🔹 Keys theo cấp độ:")
    for level, keys in keys_by_level.items():
        print(f"Level {level}: {keys}")
else:
    print("\n❌ Không tìm thấy keys nào bên trong 'employees'!")
