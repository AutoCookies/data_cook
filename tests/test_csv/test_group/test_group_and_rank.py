import unittest
import pandas as pd
from data_cook.csv.group.group_and_rank import group_and_rank

class TestGroupAndRank(unittest.TestCase):

    def test_valid_input(self):
        dataframe = pd.DataFrame({
            'group': ['A', 'A', 'B', 'B'],
            'value': [1, 2, 3, 4]
        })
        result = group_and_rank(dataframe, 'group', 'value')
        self.assertEqual(result.shape, (4, 3))
        self.assertIn('rank', result.columns)

    def test_none_input(self):
        with self.assertRaises(ValueError):
            group_and_rank(None, 'group', 'value')

    def test_invalid_input_types(self):
        dataframe = pd.DataFrame({
            'group': ['A', 'A', 'B', 'B'],
            'value': [1, 2, 3, 4]
        })
        with self.assertRaises(ValueError):
            group_and_rank(dataframe, 123, 'value')
        with self.assertRaises(ValueError):
            group_and_rank(dataframe, 'group', 123)

    def test_non_existent_columns(self):
        dataframe = pd.DataFrame({
            'group': ['A', 'A', 'B', 'B'],
            'value': [1, 2, 3, 4]
        })
        with self.assertRaises(ValueError):
            group_and_rank(dataframe, 'non_existent_column', 'value')
        with self.assertRaises(ValueError):
            group_and_rank(dataframe, 'group', 'non_existent_column')

    def test_ascending_ranking(self):
        dataframe = pd.DataFrame({
            'group': ['A', 'A', 'B', 'B'],
            'value': [1, 2, 3, 4]
        })
        result = group_and_rank(dataframe, 'group', 'value')
        self.assertEqual(result.loc[0, 'rank'], 1.0)
        self.assertEqual(result.loc[1, 'rank'], 2.0)

    def test_descending_ranking(self):
        dataframe = pd.DataFrame({
            'group': ['A', 'A', 'B', 'B'],
            'value': [1, 2, 3, 4]
        })
        result = group_and_rank(dataframe, 'group', 'value', rank_ascending=False)
        self.assertEqual(result.loc[0, 'rank'], 2.0)
        self.assertEqual(result.loc[1, 'rank'], 1.0)

    def test_single_group_column(self):
        dataframe = pd.DataFrame({
            'group': ['A', 'A', 'B', 'B'],
            'value': [1, 2, 3, 4]
        })
        result = group_and_rank(dataframe, 'group', 'value')
        self.assertEqual(result.shape, (4, 3))

    def test_multiple_group_columns(self):
        dataframe = pd.DataFrame({
            'group1': ['A', 'A', 'B', 'B'],
            'group2': ['X', 'X', 'Y', 'Y'],
            'value': [1, 2, 3, 4]
        })
        result = group_and_rank(dataframe, ['group1', 'group2'], 'value')
        self.assertEqual(result.shape, (4, 4))

if __name__ == '__main__':
    unittest.main()