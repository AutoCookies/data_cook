import unittest
import pandas as pd
import logging
from data_py.csv.group.group_and_split import group_and_split

class TestGroupAndSplit(unittest.TestCase):
    def test_valid_dataframe(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        group_column = 'B'
        train_size = 0.7
        train_df, test_df = group_and_split(df, group_column, train_size)
        self.assertIsInstance(train_df, pd.DataFrame)
        self.assertIsInstance(test_df, pd.DataFrame)

    def test_multiple_groups(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'B': [1, 1, 2, 2, 3, 3, 4, 4, 5]})
        group_column = 'B'
        train_size = 0.7
        train_df, test_df = group_and_split(df, group_column, train_size)
        self.assertIsInstance(train_df, pd.DataFrame)
        self.assertIsInstance(test_df, pd.DataFrame)

    def test_train_size_0_5(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        group_column = 'B'
        train_size = 0.5
        train_df, test_df = group_and_split(df, group_column, train_size)
        self.assertIsInstance(train_df, pd.DataFrame)
        self.assertIsInstance(test_df, pd.DataFrame)

    def test_random_state(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        group_column = 'B'
        train_size = 0.7
        random_state = 42
        train_df, test_df = group_and_split(df, group_column, train_size, random_state)
        self.assertIsInstance(train_df, pd.DataFrame)
        self.assertIsInstance(test_df, pd.DataFrame)

    def test_invalid_dataframe(self):
        df = None
        group_column = 'B'
        train_size = 0.7
        with self.assertRaises(ValueError):
            group_and_split(df, group_column, train_size)

    def test_invalid_group_column(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        group_column = None
        train_size = 0.7
        with self.assertRaises(ValueError):
            group_and_split(df, group_column, train_size)

    def test_invalid_train_size_less_than_0(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        group_column = 'B'
        train_size = -0.1
        with self.assertRaises(ValueError):
            group_and_split(df, group_column, train_size)

    def test_invalid_train_size_greater_than_1(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        group_column = 'B'
        train_size = 1.1
        with self.assertRaises(ValueError):
            group_and_split(df, group_column, train_size)

    def test_invalid_random_state(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        group_column = 'B'
        train_size = 0.7
        random_state = 'hello'
        with self.assertRaises(ValueError):
            group_and_split(df, group_column, train_size, random_state)

if __name__ == '__main__':
    unittest.main()