import pandas as pd
import unittest
from data_py import merge_with_operation

class TestMergeWithOperation(unittest.TestCase):
    def test_inner_merge_with_simple_operation(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df2 = pd.DataFrame({'A': [1, 2, 3], 'B': [7, 8, 9]})
        operation = lambda x: x[0] + x[1]
        result = merge_with_operation(df1, df2, 'A', operation)
        expected = pd.DataFrame({'A': [1, 2, 3], 'B': [11, 13, 15]})
        pd.testing.assert_frame_equal(result, expected)

    def test_outer_merge_with_simple_operation(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df2 = pd.DataFrame({'A': [1, 2, 4], 'B': [7, 8, 9]})
        operation = lambda x: sum(filter(pd.notna, x))
        result = merge_with_operation(df1, df2, 'A', operation, how='outer')
        expected = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [11, 13, 6, 9]})
        pd.testing.assert_frame_equal(result, expected)

    def test_left_merge_with_simple_operation(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df2 = pd.DataFrame({'A': [1, 2, 4], 'B': [7, 8, 9]})
        operation = lambda x: sum(filter(pd.notna, x))
        result = merge_with_operation(df1, df2, 'A', operation, how='left')
        expected = pd.DataFrame({'A': [1, 2, 3], 'B': [11, 13, 6]})
        pd.testing.assert_frame_equal(result, expected)

    def test_right_merge_with_simple_operation(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df2 = pd.DataFrame({'A': [1, 2, 4], 'B': [7, 8, 9]})
        operation = lambda x: sum(filter(pd.notna, x))
        result = merge_with_operation(df1, df2, 'A', operation, how='right')
        expected = pd.DataFrame({'A': [1, 2, 4], 'B': [11, 13, 9]})
        pd.testing.assert_frame_equal(result, expected)

    def test_merge_with_multiple_columns(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        df2 = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 11, 12], 'C': [13, 14, 15]})
        operation = lambda x: x[0] + x[1]
        result = merge_with_operation(df1, df2, ['A', 'B'], operation)
        expected = pd.DataFrame({'A': [1, 2, 3], 'B': [14, 16, 18], 'C': [7, 8, 9]})
        pd.testing.assert_frame_equal(result, expected)

    def test_merge_with_empty_dataframes(self):
        df1 = pd.DataFrame({'A': []})
        df2 = pd.DataFrame({'A': []})
        operation = lambda x: sum(filter(pd.notna, x))
        result = merge_with_operation(df1, df2, 'A', operation)
        expected = pd.DataFrame({'A': []})
        pd.testing.assert_frame_equal(result, expected)

    def test_merge_with_non_existent_column(self):
        df1 = pd.DataFrame({'A': [1, 2, 3]})
        df2 = pd.DataFrame({'B': [4, 5, 6]})
        operation = lambda x: sum(filter(pd.notna, x))
        with self.assertRaises(KeyError):
            merge_with_operation(df1, df2, 'A', operation)

if __name__ == '__main__':
    unittest.main()