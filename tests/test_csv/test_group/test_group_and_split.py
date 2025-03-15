import unittest
import pandas as pd
from data_cook.csv.group.group_and_split import group_and_split

class TestGroupAndSplit(unittest.TestCase):

    def test_valid_input(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        group_column = 'B'
        train_size = 0.7
        train_df, test_df = group_and_split(df, group_column, train_size)
        self.assertIsInstance(train_df, pd.DataFrame)
        self.assertIsInstance(test_df, pd.DataFrame)

    def test_invalid_input_df_none(self):
        df = None
        group_column = 'B'
        train_size = 0.7
        with self.assertRaises(ValueError):
            group_and_split(df, group_column, train_size)

    def test_invalid_input_group_column_none(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        group_column = None
        train_size = 0.7
        with self.assertRaises(ValueError):
            group_and_split(df, group_column, train_size)

    def test_invalid_input_train_size_less_than_zero(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        group_column = 'B'
        train_size = -0.1
        with self.assertRaises(ValueError):
            group_and_split(df, group_column, train_size)

    def test_invalid_input_train_size_greater_than_one(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        group_column = 'B'
        train_size = 1.1
        with self.assertRaises(ValueError):
            group_and_split(df, group_column, train_size)

    def test_random_state(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        group_column = 'B'
        train_size = 0.7
        random_state = 42
        train_df1, test_df1 = group_and_split(df, group_column, train_size, random_state)
        train_df2, test_df2 = group_and_split(df, group_column, train_size, random_state)
        self.assertTrue(train_df1.equals(train_df2))
        self.assertTrue(test_df1.equals(test_df2))

    def test_multiple_group_columns(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3], 'C': [1, 2, 1, 2, 3]})
        group_column = ['B', 'C']
        train_size = 0.7
        train_df, test_df = group_and_split(df, group_column, train_size)
        self.assertIsInstance(train_df, pd.DataFrame)
        self.assertIsInstance(test_df, pd.DataFrame)

    def test_edge_case_train_size_zero(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        group_column = 'B'
        train_size = 0
        train_df, test_df = group_and_split(df, group_column, train_size)
        self.assertIsInstance(train_df, pd.DataFrame)
        self.assertIsInstance(test_df, pd.DataFrame)
        self.assertTrue(train_df.empty)
        self.assertTrue(test_df.equals(df))

    def test_edge_case_train_size_one(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        group_column = 'B'
        train_size = 1
        train_df, test_df = group_and_split(df, group_column, train_size)
        self.assertIsInstance(train_df, pd.DataFrame)
        self.assertIsInstance(test_df, pd.DataFrame)
        self.assertTrue(train_df.equals(df))
        self.assertTrue(test_df.empty)

if __name__ == '__main__':
    unittest.main()