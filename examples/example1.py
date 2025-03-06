import sys
import pandas as pd

sys.path.insert(0, 'D:\\Github Projects\\data_py')

from data_splitter import data_split

df = pd.read_csv('./data/train.csv')

train, test = data_split(df, train_size = 0.7, test_size = 0.3, is_save = True)
print(train.shape, test.shape)
