import sys
import pandas as pd

sys.path.insert(0, 'D:\\Github Projects\\data_py')

from data_py.csv.group.data_group import data_group

df = pd.read_csv('./data/train.csv')

group = data_group(df, "Price", is_save = True)
print(group)
