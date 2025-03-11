import pandas as pd
import unittest
from data_py.csv.join import join_on_multiple_columns

class TestJoinOnMultipleColumns(unittest.TestCase):
    def test_inner_join_matching_columns(self):
        df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
        df2 = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'D': [7, 8]})
        result = join_on_multiple_columns(df1, df2, ['A', 'B'])
        expected = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6], 'D': [7, 8]})
        pd.testing.assert_frame_equal(result, expected)

    def test_inner_join_non_matching_columns(self):
        df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
        df2 = pd.DataFrame({'A': [1, 3], 'B': [3, 5], 'D': [7, 8]})
        result = join_on_multiple_columns(df1, df2, ['A', 'B'])
        expected = pd.DataFrame({'A': [1], 'B': [3], 'C': [5], 'D': [7]})
        pd.testing.assert_frame_equal(result, expected)

    def test_outer_join_matching_columns(self):
        df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
        df2 = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'D': [7, 8]})
        result = join_on_multiple_columns(df1, df2, ['A', 'B'], join_type='outer')
        expected = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6], 'D': [7, 8]})
        pd.testing.assert_frame_equal(result, expected)

    def test_outer_join_non_matching_columns(self):
        df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
        df2 = pd.DataFrame({'A': [1, 3], 'B': [3, 5], 'D': [7, 8]})
        result = join_on_multiple_columns(df1, df2, ['A', 'B'], join_type='outer')
        expected = pd.DataFrame({'A': [1, 2, 3], 'B': [3, 4, 5], 'C': [5, 6, None], 'D': [7, None, 8]})
        pd.testing.assert_frame_equal(result, expected)

    def test_left_join_matching_columns(self):
        df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
        df2 = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'D': [7, 8]})
        result = join_on_multiple_columns(df1, df2, ['A', 'B'], join_type='left')
        expected = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6], 'D': [7, 8]})
        pd.testing.assert_frame_equal(result, expected)

    def test_left_join_non_matching_columns(self):
        df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
        df2 = pd.DataFrame({'A': [1, 3], 'B': [3, 5], 'D': [7, 8]})
        result = join_on_multiple_columns(df1, df2, ['A', 'B'], join_type='left')
        expected = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6], 'D': [7, None]})
        pd.testing.assert_frame_equal(result, expected)

    def test_invalid_column(self):
        df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        df2 = pd.DataFrame({'X': [1, 2], 'Y': [3, 4]})
        with self.assertRaises(KeyError):
            join_on_multiple_columns(df1, df2, ['A', 'B'])

    def test_invalid_join_type(self):
        df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        df2 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        with self.assertRaises(ValueError):
            join_on_multiple_columns(df1, df2, ['A', 'B'], join_type='invalid_type')

if __name__ == '__main__':
    unittest.main()
