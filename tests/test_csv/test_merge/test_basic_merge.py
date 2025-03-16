import unittest
import pandas as pd
from data_cook import basic_merge

class TestBasicMerge(unittest.TestCase):

    def test_inner_merge_single_column(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df2 = pd.DataFrame({'A': [1, 2, 3], 'C': [7, 8, 9]})
        expected = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        self.assertTrue(basic_merge(df1, df2, 'A').equals(expected))

    def test_inner_merge_multiple_columns(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df2 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        expected = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        self.assertTrue(basic_merge(df1, df2, ['A', 'B']).equals(expected))

    def test_outer_merge(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df2 = pd.DataFrame({'A': [2, 3, 4], 'C': [7, 8, 9]})
        expected = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [4, 5, 6, None], 'C': [None, 7, 8, 9]})
        self.assertTrue(basic_merge(df1, df2, 'A', 'outer').equals(expected))

    def test_left_merge(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df2 = pd.DataFrame({'A': [2, 3, 4], 'C': [7, 8, 9]})
        expected = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [None, 7, 8]})
        self.assertTrue(basic_merge(df1, df2, 'A', 'left').equals(expected))

    def test_right_merge(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df2 = pd.DataFrame({'A': [2, 3, 4], 'C': [7, 8, 9]})
        expected = pd.DataFrame({'A': [2, 3, 4], 'B': [5, 6, None], 'C': [7, 8, 9]})
        self.assertTrue(basic_merge(df1, df2, 'A', 'right').equals(expected))

    def test_invalid_merge_type(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df2 = pd.DataFrame({'A': [2, 3, 4], 'C': [7, 8, 9]})
        with self.assertRaises(ValueError):
            basic_merge(df1, df2, 'A', 'invalid')

    def test_non_existent_column(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
        with self.assertRaises(KeyError):
            basic_merge(df1, df2, 'E')

    def test_empty_dataframes(self):
        df1 = pd.DataFrame({'A': [], 'B': []})
        df2 = pd.DataFrame({'A': [], 'C': []})
        expected = pd.DataFrame({'A': [], 'B': [], 'C': []})
        self.assertTrue(basic_merge(df1, df2, 'A').equals(expected))

if __name__ == '__main__':
    unittest.main()