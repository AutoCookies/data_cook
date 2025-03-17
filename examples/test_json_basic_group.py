from data_cook import JSONExtractor
from collections import defaultdict

json_path1 = "test.json"
json_path2 = "test2.json"

extractor1 = JSONExtractor(json_path1)
extractor2 = JSONExtractor(json_path2)

json2 = extractor2.get_json()
extractor1.combine_json(json2, extractor1.combined_json)

extractor1.save_json("./combined_json.json")
