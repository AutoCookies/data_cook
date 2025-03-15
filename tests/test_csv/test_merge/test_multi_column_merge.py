import unittest
import pandas as pd
from data_py import multi_column_merge

class TestMultiColumnMerge(unittest.TestCase):
    
    def test_inner_merge(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': ['x', 'y', 'z'], 'C': [10, 20, 30]})
        df2 = pd.DataFrame({'A': [1, 2, 4], 'B': ['x', 'y', 'w'], 'D': [100, 200, 400]})
        result = multi_column_merge(df1, df2, ['A', 'B'])
        expected = pd.DataFrame({'A': [1, 2], 'B': ['x', 'y'], 'C': [10, 20], 'D': [100, 200]})
        pd.testing.assert_frame_equal(result, expected)

    def test_outer_merge(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': ['x', 'y', 'z'], 'C': [10, 20, 30]})
        df2 = pd.DataFrame({'A': [1, 2, 4], 'B': ['x', 'y', 'w'], 'D': [100, 200, 400]})
        result = multi_column_merge(df1, df2, ['A', 'B'], how='outer')
        expected = pd.DataFrame({
            'A': [1, 2, 3, 4],
            'B': ['x', 'y', 'z', 'w'],
            'C': [10, 20, 30, None],
            'D': [100, 200, None, 400]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_left_merge(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': ['x', 'y', 'z'], 'C': [10, 20, 30]})
        df2 = pd.DataFrame({'A': [1, 2, 4], 'B': ['x', 'y', 'w'], 'D': [100, 200, 400]})
        result = multi_column_merge(df1, df2, ['A', 'B'], how='left')
        expected = pd.DataFrame({
            'A': [1, 2, 3],
            'B': ['x', 'y', 'z'],
            'C': [10, 20, 30],
            'D': [100, 200, None]
        })
        pd.testing.assert_frame_equal(result, expected)
    
    def test_right_merge(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': ['x', 'y', 'z'], 'C': [10, 20, 30]})
        df2 = pd.DataFrame({'A': [1, 2, 4], 'B': ['x', 'y', 'w'], 'D': [100, 200, 400]})
        result = multi_column_merge(df1, df2, ['A', 'B'], how='right')
        expected = pd.DataFrame({
            'A': [1, 2, 4],
            'B': ['x', 'y', 'w'],
            'C': [10, 20, None],
            'D': [100, 200, 400]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_merge_with_no_common_columns(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'C': [10, 20, 30]})
        df2 = pd.DataFrame({'B': ['x', 'y', 'z'], 'D': [100, 200, 300]})
        with self.assertRaises(KeyError):
            multi_column_merge(df1, df2, ['A', 'B'])
    
if __name__ == '__main__':
    unittest.main()
