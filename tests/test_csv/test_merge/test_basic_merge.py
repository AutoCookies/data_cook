import unittest
import pandas as pd
from data_py.csv.merge import basic_merge

class TestBasicMerge(unittest.TestCase):
    def setUp(self):
        """Tạo các DataFrame test trước mỗi test case."""
        self.df1 = pd.DataFrame({
            'ID': [1, 2, 3, 4],
            'Value1': ['A', 'B', 'C', 'D']
        })

        self.df2 = pd.DataFrame({
            'ID': [3, 4, 5, 6],
            'Value2': ['X', 'Y', 'Z', 'W']
        })

    def test_inner_merge(self):
        """Test merge kiểu 'inner' (chỉ giữ lại giá trị trùng)."""
        result = basic_merge(self.df1, self.df2, on_column='ID', how='inner')
        expected = pd.DataFrame({
            'ID': [3, 4],
            'Value1': ['C', 'D'],
            'Value2': ['X', 'Y']
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_outer_merge(self):
        """Test merge kiểu 'outer' (giữ tất cả giá trị, fill NaN nếu không có)."""
        result = basic_merge(self.df1, self.df2, on_column='ID', how='outer')
        expected = pd.DataFrame({
            'ID': [1, 2, 3, 4, 5, 6],
            'Value1': ['A', 'B', 'C', 'D', None, None],
            'Value2': [None, None, 'X', 'Y', 'Z', 'W']
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_left_merge(self):
        """Test merge kiểu 'left' (giữ lại tất cả giá trị từ df1)."""
        result = basic_merge(self.df1, self.df2, on_column='ID', how='left')
        expected = pd.DataFrame({
            'ID': [1, 2, 3, 4],
            'Value1': ['A', 'B', 'C', 'D'],
            'Value2': [None, None, 'X', 'Y']
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_right_merge(self):
        """Test merge kiểu 'right' (giữ lại tất cả giá trị từ df2)."""
        result = basic_merge(self.df1, self.df2, on_column='ID', how='right')
        expected = pd.DataFrame({
            'ID': [3, 4, 5, 6],
            'Value1': ['C', 'D', None, None],
            'Value2': ['X', 'Y', 'Z', 'W']
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_merge_with_no_common_values(self):
        """Test merge khi không có giá trị chung giữa hai DataFrame."""
        df3 = pd.DataFrame({'ID': [10, 11, 12], 'Value3': ['P', 'Q', 'R']})
        result = basic_merge(self.df1, df3, on_column='ID', how='inner')
        expected = pd.DataFrame(columns=['ID', 'Value1', 'Value3'])  # Không có match nào
        pd.testing.assert_frame_equal(result, expected)

    def test_merge_with_multiple_columns(self):
        """Test merge với nhiều cột."""
        df4 = pd.DataFrame({
            'ID': [1, 2, 3, 4],
            'Category': ['X', 'Y', 'Z', 'W'],
            'Value2': ['AA', 'BB', 'CC', 'DD']
        })
        df5 = pd.DataFrame({
            'ID': [1, 2, 3, 4],
            'Category': ['X', 'Y', 'Z', 'W'],
            'Score': [10, 20, 30, 40]
        })
        result = basic_merge(df4, df5, on_column=['ID', 'Category'], how='inner')
        expected = pd.DataFrame({
            'ID': [1, 2, 3, 4],
            'Category': ['X', 'Y', 'Z', 'W'],
            'Value2': ['AA', 'BB', 'CC', 'DD'],
            'Score': [10, 20, 30, 40]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_merge_with_missing_column(self):
        """Test merge khi thiếu cột cần ghép."""
        df_wrong = pd.DataFrame({
            'UserID': [1, 2, 3, 4],  # Sai tên cột (UserID thay vì ID)
            'Value2': ['AA', 'BB', 'CC', 'DD']
        })
        with self.assertRaises(KeyError):
            basic_merge(self.df1, df_wrong, on_column='ID', how='inner')

if __name__ == '__main__':
    unittest.main()
