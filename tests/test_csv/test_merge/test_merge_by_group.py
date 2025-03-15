from data_py import merge_by_group
import pandas as pd
import unittest

class TestMergeByGroup(unittest.TestCase):

    def test_inner_merge_single_group_column(self):
        df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
        df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value2': [4, 5, 6]})
        result = merge_by_group(df1, df2, 'key')
        expected = pd.DataFrame({'key': ['A', 'B'], 'value1': [1, 2], 'value2': [4, 5]})
        pd.testing.assert_frame_equal(result, expected)

    def test_inner_merge_multiple_group_columns(self):
        df1 = pd.DataFrame({'key1': ['A', 'B', 'C'], 'key2': ['X', 'Y', 'Z'], 'value1': [1, 2, 3]})
        df2 = pd.DataFrame({'key1': ['A', 'B', 'D'], 'key2': ['X', 'Y', 'W'], 'value2': [4, 5, 6]})
        result = merge_by_group(df1, df2, ['key1', 'key2'])
        expected = pd.DataFrame({'key1': ['A', 'B'], 'key2': ['X', 'Y'], 'value1': [1, 2], 'value2': [4, 5]})
        pd.testing.assert_frame_equal(result, expected)

    def test_outer_merge_single_group_column(self):
        df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
        df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value2': [4, 5, 6]})
        result = merge_by_group(df1, df2, 'key', how='outer')
        expected = pd.DataFrame({
            'key': ['A', 'B', 'C', 'D'],
            'value1': [1, 2, 3, None],
            'value2': [4, 5, None, 6]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_left_merge_single_group_column(self):
        df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
        df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value2': [4, 5, 6]})
        result = merge_by_group(df1, df2, 'key', how='left')
        expected = pd.DataFrame({
            'key': ['A', 'B', 'C'],
            'value1': [1, 2, 3],
            'value2': [4, 5, None]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_right_merge_single_group_column(self):
        df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
        df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value2': [4, 5, 6]})
        result = merge_by_group(df1, df2, 'key', how='right')
        expected = pd.DataFrame({
            'key': ['A', 'B', 'D'],
            'value1': [1, 2, None],
            'value2': [4, 5, 6]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_merge_with_suffixes(self):
        df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
        df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value': [4, 5, 6]})
        result = merge_by_group(df1, df2, 'key', suffixes=('_left', '_right'))
        expected = pd.DataFrame({'key': ['A', 'B'], 'value_left': [1, 2], 'value_right': [4, 5]})
        pd.testing.assert_frame_equal(result, expected)

    def test_merge_with_non_existent_group_column(self):
        df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
        df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value2': [4, 5, 6]})
        # Kiểm tra xem hàm có ném lỗi KeyError khi cột group không tồn tại hay không
        with self.assertRaises(KeyError):
            merge_by_group(df1, df2, 'nonexistent')

if __name__ == '__main__':
    unittest.main()