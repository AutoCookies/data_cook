import unittest
import pandas as pd
from data_cook import index_join

class TestIndexJoinFunction(unittest.TestCase):

    def test_inner_join_matching_indices(self):
        df1 = pd.DataFrame({'A': [1, 2, 3]}, index=['a', 'b', 'c'])
        df2 = pd.DataFrame({'B': [4, 5, 6]}, index=['a', 'b', 'c'])
        result = index_join(df1, df2, how='inner')
        expected = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'c'])
        self.assertTrue(result.equals(expected))

    def test_inner_join_non_matching_indices(self):
        df1 = pd.DataFrame({'A': [1, 2, 3]}, index=['a', 'b', 'c'])
        df2 = pd.DataFrame({'B': [4, 5, 6]}, index=['d', 'e', 'f'])
        result = index_join(df1, df2, how='inner')
        expected = pd.DataFrame({'A': [], 'B': []}, index=[])
        self.assertTrue(result.equals(expected))

    def test_outer_join_matching_and_non_matching_indices(self):
        df1 = pd.DataFrame({'A': [1, 2, 3]}, index=['a', 'b', 'c'])
        df2 = pd.DataFrame({'B': [4, 5, 6]}, index=['a', 'b', 'd'])
        result = index_join(df1, df2, how='outer')
        expected = pd.DataFrame({'A': [1, 2, 3, None], 'B': [4, 5, None, 6]}, index=['a', 'b', 'c', 'd'])
        self.assertTrue(result.equals(expected))

    def test_left_join_matching_and_non_matching_indices(self):
        df1 = pd.DataFrame({'A': [1, 2, 3]}, index=['a', 'b', 'c'])
        df2 = pd.DataFrame({'B': [4, 5, 6]}, index=['a', 'b', 'd'])
        result = index_join(df1, df2, how='left')
        expected = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, None]}, index=['a', 'b', 'c'])
        self.assertTrue(result.equals(expected))

    def test_right_join_matching_and_non_matching_indices(self):
        df1 = pd.DataFrame({'A': [1, 2, 3]}, index=['a', 'b', 'c'])
        df2 = pd.DataFrame({'B': [4, 5, 6]}, index=['a', 'b', 'd'])
        result = index_join(df1, df2, how='right')
        expected = pd.DataFrame({'A': [1, 2, None], 'B': [4, 5, 6]}, index=['a', 'b', 'd'])
        self.assertTrue(result.equals(expected))

    def test_invalid_join_type(self):
        df1 = pd.DataFrame({'A': [1, 2, 3]}, index=['a', 'b', 'c'])
        df2 = pd.DataFrame({'B': [4, 5, 6]}, index=['a', 'b', 'c'])
        with self.assertRaises(ValueError):
            index_join(df1, df2, how='invalid')

    def test_none_input(self):
        df1 = pd.DataFrame({'A': [1, 2, 3]}, index=['a', 'b', 'c'])
        with self.assertRaises(ValueError):
            index_join(df1, None)

    def test_non_dataframe_input(self):
        df1 = pd.DataFrame({'A': [1, 2, 3]}, index=['a', 'b', 'c'])
        with self.assertRaises(ValueError):
            index_join(df1, 'not a dataframe')

if __name__ == '__main__':
    unittest.main()