import unittest
import pandas as pd
from data_cook import join_on_multiple_columns

class TestJoinOnMultipleColumns(unittest.TestCase):
    def test_inner_join(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        df2 = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 11, 12], 'D': [13, 14, 15]})
        expected = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [13, 14, 15]})
        result = join_on_multiple_columns(df1, df2, ['A', 'B'])
        pd.testing.assert_frame_equal(result, expected)

    def test_outer_join(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        df2 = pd.DataFrame({'A': [1, 2, 4], 'B': [10, 11, 12], 'D': [13, 14, 15]})
        expected = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [4, 5, 6, 12], 'C': [7, 8, 9, None], 'D': [13, 14, None, 15]})
        result = join_on_multiple_columns(df1, df2, ['A', 'B'], 'outer')
        pd.testing.assert_frame_equal(result, expected)

    def test_left_join(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        df2 = pd.DataFrame({'A': [1, 2, 4], 'B': [10, 11, 12], 'D': [13, 14, 15]})
        expected = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [13, 14, None]})
        result = join_on_multiple_columns(df1, df2, ['A', 'B'], 'left')
        pd.testing.assert_frame_equal(result, expected)

    def test_right_join(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        df2 = pd.DataFrame({'A': [1, 2, 4], 'B': [10, 11, 12], 'D': [13, 14, 15]})
        expected = pd.DataFrame({'A': [1, 2, 4], 'B': [4, 5, 12], 'C': [7, 8, None], 'D': [13, 14, 15]})
        result = join_on_multiple_columns(df1, df2, ['A', 'B'], 'right')
        pd.testing.assert_frame_equal(result, expected)

    def test_non_matching_columns(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        df2 = pd.DataFrame({'D': [10, 11, 12], 'E': [13, 14, 15]})
        with self.assertRaises(ValueError):
            join_on_multiple_columns(df1, df2, ['A', 'B'])

    def test_invalid_join_type(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        df2 = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 11, 12], 'D': [13, 14, 15]})
        with self.assertRaises(ValueError):
            join_on_multiple_columns(df1, df2, ['A', 'B'], 'invalid_join')

if __name__ == '__main__':
    unittest.main()
