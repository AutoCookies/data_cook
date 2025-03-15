import unittest
import pandas as pd
from data_py import merge_with_suffix

class TestMergeWithSuffix(unittest.TestCase):
    def test_inner_merge(self):
        df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
        df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value': [4, 5, 6]})
        result = merge_with_suffix(df1, df2, 'key')
        expected = pd.DataFrame({'key': ['A', 'B'], 'value_left': [1, 2], 'value_right': [4, 5]})
        pd.testing.assert_frame_equal(result, expected)
    
    def test_outer_merge(self):
        df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
        df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value': [4, 5, 6]})
        result = merge_with_suffix(df1, df2, 'key', how='outer')
        expected = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
                                 'value_left': [1, 2, 3, None],
                                 'value_right': [4, 5, None, 6]})
        pd.testing.assert_frame_equal(result, expected)
    
    def test_left_merge(self):
        df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
        df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value': [4, 5, 6]})
        result = merge_with_suffix(df1, df2, 'key', how='left')
        expected = pd.DataFrame({'key': ['A', 'B', 'C'], 'value_left': [1, 2, 3], 'value_right': [4, 5, None]})
        pd.testing.assert_frame_equal(result, expected)
    
    def test_right_merge(self):
        df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
        df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value': [4, 5, 6]})
        result = merge_with_suffix(df1, df2, 'key', how='right')
        expected = pd.DataFrame({'key': ['A', 'B', 'D'], 'value_left': [1, 2, None], 'value_right': [4, 5, 6]})
        pd.testing.assert_frame_equal(result, expected)
    
    def test_merge_with_multiple_columns(self):
        df1 = pd.DataFrame({'key1': ['A', 'B'], 'key2': ['X', 'Y'], 'value': [1, 2]})
        df2 = pd.DataFrame({'key1': ['A', 'B'], 'key2': ['X', 'Y'], 'value': [3, 4]})
        result = merge_with_suffix(df1, df2, ['key1', 'key2'])
        expected = pd.DataFrame({'key1': ['A', 'B'], 'key2': ['X', 'Y'], 'value_left': [1, 2], 'value_right': [3, 4]})
        pd.testing.assert_frame_equal(result, expected)
    
    def test_merge_with_different_suffixes(self):
        df1 = pd.DataFrame({'key': ['A', 'B'], 'value': [1, 2]})
        df2 = pd.DataFrame({'key': ['A', 'B'], 'value': [3, 4]})
        result = merge_with_suffix(df1, df2, 'key', suffixes=('_df1', '_df2'))
        expected = pd.DataFrame({'key': ['A', 'B'], 'value_df1': [1, 2], 'value_df2': [3, 4]})
        pd.testing.assert_frame_equal(result, expected)
    
    def test_merge_with_non_existent_column(self):
        df1 = pd.DataFrame({'key': ['A', 'B'], 'value': [1, 2]})
        df2 = pd.DataFrame({'id': ['A', 'B'], 'value': [3, 4]})
        with self.assertRaises(KeyError):
            merge_with_suffix(df1, df2, 'key')
    
    def test_merge_with_empty_dataframes(self):
        df1 = pd.DataFrame({'key': [], 'value': []})
        df2 = pd.DataFrame({'key': [], 'value': []})
        result = merge_with_suffix(df1, df2, 'key')
        expected = pd.DataFrame(columns=['key', 'value_left', 'value_right'])
        pd.testing.assert_frame_equal(result, expected)

if __name__ == '__main__':
    unittest.main()