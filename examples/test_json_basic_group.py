from data_cook import JSONExtractor
from collections import defaultdict

json_path1 = "test.json"
json_path2 = "test2.json"

extractor1 = JSONExtractor(json_path1)
data = extractor1.drop_key(['email', 'deadline'])
print(data)