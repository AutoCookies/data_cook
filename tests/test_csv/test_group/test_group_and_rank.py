import unittest
import pandas as pd
from data_py.csv.group.group_and_rank import group_and_rank

class TestGroupAndRank(unittest.TestCase):

    def test_valid_input(self):
        df = pd.DataFrame({
            'group': ['A', 'A', 'B', 'B'],
            'value': [10, 20, 30, 40]
        })
        result = group_and_rank(df, 'group', 'value')
        self.assertIsInstance(result, pd.DataFrame)
        self.assertIn('rank', result.columns)

    def test_none_input(self):
        with self.assertRaises(ValueError):
            group_and_rank(None, 'group', 'value')

    def test_non_dataframe_input(self):
        with self.assertRaises(ValueError):
            group_and_rank('not a dataframe', 'group', 'value')

    def test_invalid_group_by_column_type(self):
        df = pd.DataFrame({
            'group': ['A', 'A', 'B', 'B'],
            'value': [10, 20, 30, 40]
        })
        with self.assertRaises(ValueError):
            group_and_rank(df, 123, 'value')

    def test_invalid_rank_by_column_type(self):
        df = pd.DataFrame({
            'group': ['A', 'A', 'B', 'B'],
            'value': [10, 20, 30, 40]
        })
        with self.assertRaises(ValueError):
            group_and_rank(df, 'group', 123)

    def test_non_existent_rank_by_column(self):
        df = pd.DataFrame({
            'group': ['A', 'A', 'B', 'B'],
            'value': [10, 20, 30, 40]
        })
        with self.assertRaises(ValueError):
            group_and_rank(df, 'group', 'non_existent_column')

    def test_non_existent_group_by_column(self):
        df = pd.DataFrame({
            'group': ['A', 'A', 'B', 'B'],
            'value': [10, 20, 30, 40]
        })
        with self.assertRaises(ValueError):
            group_and_rank(df, 'non_existent_column', 'value')

    def test_rank_ascending_false(self):
        df = pd.DataFrame({
            'group': ['A', 'A', 'B', 'B'],
            'value': [10, 20, 30, 40]
        })
        result = group_and_rank(df, 'group', 'value', rank_ascending=False)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertIn('rank', result.columns)

    def test_multiple_group_by_columns(self):
        df = pd.DataFrame({
            'group1': ['A', 'A', 'B', 'B'],
            'group2': ['X', 'X', 'Y', 'Y'],
            'value': [10, 20, 30, 40]
        })
        result = group_and_rank(df, ['group1', 'group2'], 'value')
        self.assertIsInstance(result, pd.DataFrame)
        self.assertIn('rank', result.columns)

if __name__ == '__main__':
    unittest.main()