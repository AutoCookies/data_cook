import unittest
import pandas as pd
from data_cook import group_and_merge


class TestGroupAndMerge(unittest.TestCase):

    def test_valid_input(self):
        df = pd.DataFrame({
            'id': [1, 2, 3, 4, 5],
            'group': ['A', 'B', 'A', 'B', 'A'],
            'value': [10, 20, 30, 40, 50]
        })
        result = group_and_merge(df, 'group', 'id')
        self.assertIsInstance(result, pd.DataFrame)

    def test_invalid_input_dataframe(self):
        with self.assertRaises(ValueError):
            group_and_merge(None, 'group', 'id')

    def test_invalid_group_column(self):
        df = pd.DataFrame({
            'id': [1, 2, 3, 4, 5],
            'group': ['A', 'B', 'A', 'B', 'A'],
            'value': [10, 20, 30, 40, 50]
        })
        with self.assertRaises(ValueError):
            group_and_merge(df, None, 'id')

    def test_invalid_merge_column(self):
        df = pd.DataFrame({
            'id': [1, 2, 3, 4, 5],
            'group': ['A', 'B', 'A', 'B', 'A'],
            'value': [10, 20, 30, 40, 50]
        })
        with self.assertRaises(ValueError):
            group_and_merge(df, 'group', None)

    def test_multiple_group_columns(self):
        df = pd.DataFrame({
            'id': [1, 2, 3, 4, 5],
            'group1': ['A', 'B', 'A', 'B', 'A'],
            'group2': ['X', 'Y', 'X', 'Y', 'X'],
            'value': [10, 20, 30, 40, 50]
        })
        result = group_and_merge(df, ['group1', 'group2'], 'id')
        self.assertIsInstance(result, pd.DataFrame)

    def test_non_existent_merge_column(self):
        df = pd.DataFrame({
            'id': [1, 2, 3, 4, 5],
            'group': ['A', 'B', 'A', 'B', 'A'],
            'value': [10, 20, 30, 40, 50]
        })
        with self.assertRaises(KeyError):
            group_and_merge(df, 'group', 'non_existent_column')

    def test_non_existent_group_column(self):
        df = pd.DataFrame({
            'id': [1, 2, 3, 4, 5],
            'group': ['A', 'B', 'A', 'B', 'A'],
            'value': [10, 20, 30, 40, 50]
        })
        with self.assertRaises(KeyError):
            group_and_merge(df, 'non_existent_column', 'id')

if __name__ == '__main__':
    unittest.main()