import json
import logging
from collections import defaultdict

class JSONExtractor:
    def __init__ (self, json_path):
        self.path = json_path
        self.data = None
        self.key_by_level = defaultdict(set)

    def read_json(self):
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                self.data = json.load(file)
        except Exception as e:
            logging(e)

    def extract_keys(self, level=0):
        """
        Trích xuất tất cả các key từ JSON và nhóm theo cấp độ lồng nhau (depth).

        Args:
            data (dict | list): Dữ liệu JSON đầu vào.
            level (int): Cấp độ hiện tại của JSON.
        """
        if self.data is None:
            print("The data must be loaded before extracting keys.")
            return
        try:
            if isinstance(self.data, dict):
                for key, value in self.data.items():
                    self.keys_by_level[level].add(key)  # Lưu key theo cấp độ
                    self.extract_keys(value, level + 1)  # Đệ quy vào level tiếp theo

            elif isinstance(self.data, list):
                for item in self.data:
                    self.extract_keys(item, level)  # List không tăng cấp độ vì không tạo thêm cấp JSON
        

    def get_json (self):
        return self.data    
    
    def set_data (self, data):
        self.data = data
    