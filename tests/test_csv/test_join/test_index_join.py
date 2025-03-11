import pandas as pd
import unittest
from data_py.csv.join import index_join

class TestIndexJoin(unittest.TestCase):
    def test_inner_join_matching_indices(self):
        df1 = pd.DataFrame({'A': [1, 2, 3]}, index=[1, 2, 3])
        df2 = pd.DataFrame({'B': [4, 5, 6]}, index=[1, 2, 3])
        result = index_join(df1, df2, how='inner')
        expected = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=[1, 2, 3])
        pd.testing.assert_frame_equal(result, expected)

    def test_inner_join_non_matching_indices(self):
        df1 = pd.DataFrame({'A': [1, 2, 3]}, index=[1, 2, 3])
        df2 = pd.DataFrame({'B': [4, 5, 6]}, index=[2, 3, 4])
        result = index_join(df1, df2, how='inner')
        expected = pd.DataFrame({'A': [2, 3], 'B': [5, 6]}, index=[2, 3])
        pd.testing.assert_frame_equal(result, expected)

    def test_outer_join(self):
        df1 = pd.DataFrame({'A': [1, 2, 3]}, index=[1, 2, 3])
        df2 = pd.DataFrame({'B': [4, 5, 6]}, index=[2, 3, 4])
        result = index_join(df1, df2, how='outer')
        expected = pd.DataFrame({'A': [1, 2, 3, None], 'B': [None, 5, 6, 7]}, index=[1, 2, 3, 4])
        pd.testing.assert_frame_equal(result, expected)

    def test_left_join(self):
        df1 = pd.DataFrame({'A': [1, 2, 3]}, index=[1, 2, 3])
        df2 = pd.DataFrame({'B': [4, 5, 6]}, index=[2, 3, 4])
        result = index_join(df1, df2, how='left')
        expected = pd.DataFrame({'A': [1, 2, 3], 'B': [None, 5, 6]}, index=[1, 2, 3])
        pd.testing.assert_frame_equal(result, expected)

    def test_right_join(self):
        df1 = pd.DataFrame({'A': [1, 2, 3]}, index=[1, 2, 3])
        df2 = pd.DataFrame({'B': [4, 5, 6]}, index=[2, 3, 4])
        result = index_join(df1, df2, how='right')
        expected = pd.DataFrame({'A': [None, 2, 3], 'B': [5, 6, 7]}, index=[2, 3, 4])
        pd.testing.assert_frame_equal(result, expected)

    def test_invalid_join_type(self):
        df1 = pd.DataFrame({'A': [1, 2, 3]}, index=[1, 2, 3])
        df2 = pd.DataFrame({'B': [4, 5, 6]}, index=[1, 2, 3])
        with self.assertRaises(ValueError):
            index_join(df1, df2, how='invalid')

    def test_none_input(self):
        df1 = pd.DataFrame({'A': [1, 2, 3]}, index=[1, 2, 3])
        with self.assertRaises(ValueError):
            index_join(None, df1)

    def test_non_dataframe_input(self):
        df1 = pd.DataFrame({'A': [1, 2, 3]}, index=[1, 2, 3])
        with self.assertRaises(ValueError):
            index_join(df1, 'not a dataframe')

if __name__ == '__main__':
    unittest.main()