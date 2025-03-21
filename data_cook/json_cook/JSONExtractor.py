import json
import logging
import os
from collections import defaultdict
from .utils import combine_json, drop_keys, join_json

logging.basicConfig(level=logging.ERROR)

class JSONExtractor:
    def __init__(self, json_path=None):
        """
        Khởi tạo JSONExtractor:
        - self.path: đường dẫn file JSON
        - self.data: dữ liệu JSON đã load
        - self.keys_by_level: Lưu trữ key theo cấp độ lồng nhau
        - self.all_keys: Tập hợp tất cả các key duy nhất
        - self.key_value: Lưu trữ giá trị của một key cụ thể
        """
        self.path = json_path
        self.data = None
        self.keys_by_level = defaultdict(set)
        self.all_keys = set()
        self.key_value = defaultdict(list)
        self.combined_json = None
        if json_path:
            self.read_json()
            self.extract_keys_level()

    def combine_json (self, json2):
        self.combined_json = combine_json(self.data, json2)

    def read_json(self):
        """Đọc file JSON và lưu vào self.data."""
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                self.data = json.load(file)
        except Exception as e:
            logging.error(f"Lỗi đọc file JSON: {e}")

    def extract_keys_level(self, data=None, level=0):
        """Trích xuất tất cả các key từ JSON theo cấp độ lồng nhau."""
        if data is None:
            data = self.data
        if isinstance(data, dict):
            for key, value in data.items():
                self.keys_by_level[level].add(key)
                self.all_keys.add(key)
                self.extract_keys_level(value, level + 1)
        elif isinstance(data, list):
            for item in data:
                self.extract_keys_level(item, level)

    def find_and_extract_keys(self, target_key):
        """Tìm kiếm và trích xuất tất cả các object chứa target_key."""
        def _recursive_search(data):
            if isinstance(data, dict):
                for key, value in data.items():
                    if key == target_key:
                        print(f"\nExtracting keys from '{target_key}': {value}")
                        if isinstance(value, (dict, list)):
                            self.extract_keys_level(value)
                    else:
                        _recursive_search(value)
            elif isinstance(data, list):
                for item in data:
                    _recursive_search(item)

        if self.data is None:
            print("Lỗi: Dữ liệu chưa được load.")
            return

        self.keys_by_level.clear()
        _recursive_search(self.data)

    def combine_json(self, json_file):
        """Hợp nhất JSON hiện tại với một file JSON khác."""
        if not isinstance(json_file, dict):
            print("Lỗi: JSON cần hợp nhất không hợp lệ.")
            return
        self.data = combine_json(self.data, json_file)

    def get_all_keys(self):
        """Trả về danh sách tất cả các key có trong JSON."""
        return list(self.all_keys)

    def get_json(self):
        """Trả về dữ liệu JSON hiện tại."""
        return self.data

    def print_keys_by_level(self):
        """In các key theo cấp độ lồng nhau."""
        if not self.keys_by_level:
            print("Không có key nào được trích xuất.")
            return
        print("\nCác key theo cấp độ:")
        for level, keys in sorted(self.keys_by_level.items()):
            print(f"Cấp {level}: {keys}")

    def print_json(self):
        """In dữ liệu JSON theo format đẹp."""
        if self.data is None:
            print("Lỗi: Không có dữ liệu JSON.")
            return
        print(json.dumps(self.data, indent=4, ensure_ascii=False))

    def set_data(self, data):
        """Thiết lập dữ liệu JSON mới."""
        if isinstance(data, dict):
            self.data = data
            self.keys_by_level.clear()
            self.all_keys.clear()
        else:
            print("Lỗi: Dữ liệu JSON không hợp lệ.")

    def save_json(self, out_dir):
        """Lưu dữ liệu JSON vào một file."""
        if self.data is None:
            print("Lỗi: Không có dữ liệu JSON để lưu.")
            return

        try:
            os.makedirs(os.path.dirname(out_dir), exist_ok=True)
            with open(out_dir, "w", encoding="utf-8") as file:
                json.dump(self.data, file, indent=4, ensure_ascii=False)
            print(f"Dữ liệu JSON đã được lưu vào {out_dir}")
        except Exception as e:
            print(f"Lỗi khi lưu file JSON: {e}")

    def drop_key(self, key):
        return drop_keys(self.data, key)
    
    def join_json (self, json2, method = 'outer'):
        return join_json(self.data, json2, method)
