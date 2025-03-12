import unittest
import pandas as pd
from data_py.csv.merge import async_merge

class TestAsyncMerge(unittest.TestCase):
    def setUp(self):
        """Tạo các DataFrame test trước mỗi test case."""
        self.df1 = pd.DataFrame({
            'time': [1.0, 2.0, 3.0, 5.0],
            'value1': ['A', 'B', 'C', 'D']
        })

        self.df2 = pd.DataFrame({
            'time': [1.1, 2.2, 3.5, 4.9],
            'value2': [10, 20, 30, 40]
        })

    def test_merge_with_tolerance(self):
        """Test merge với tolerance cho phép."""
        result = async_merge(self.df1, self.df2, on_column='time', tolerance=0.5)
        expected = pd.DataFrame({
            'time': [1.0, 2.0, 3.0, 5.0],
            'value1': ['A', 'B', 'C', 'D'],
            'value2': [10.0, 20.0, 30.0, 40.0]  # Ghép gần nhất trong khoảng tolerance
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_merge_outside_tolerance(self):
        """Test merge khi các giá trị nằm ngoài tolerance (kết quả không có ghép)."""
        result = async_merge(self.df1, self.df2, on_column='time', tolerance=0.05)
        expected = pd.DataFrame({
            'time': [1.0, 2.0, 3.0, 5.0],
            'value1': ['A', 'B', 'C', 'D'],
            'value2': [None, None, None, None]  # Không ghép được do tolerance quá nhỏ
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_merge_with_duplicate_values(self):
        """Test merge khi có giá trị trùng trong df2."""
        df2_dup = pd.DataFrame({
            'time': [1.0, 1.1, 2.0, 2.1],
            'value2': [10, 15, 20, 25]
        })
        result = async_merge(self.df1, df2_dup, on_column='time', tolerance=0.2)
        expected = pd.DataFrame({
            'time': [1.0, 2.0, 3.0, 5.0],
            'value1': ['A', 'B', 'C', 'D'],
            'value2': [10.0, 20.0, None, None]  # Chọn giá trị gần nhất trong tolerance
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_merge_with_empty_dataframe(self):
        """Test merge khi một trong hai DataFrame rỗng."""
        empty_df = pd.DataFrame(columns=['time', 'value'])
        result = async_merge(self.df1, empty_df, on_column='time', tolerance=0.5)
        expected = self.df1.copy()  # Không có gì để merge
        expected['value2'] = None  # Cột mới nhưng toàn bộ là None
        pd.testing.assert_frame_equal(result, expected)

    def test_merge_with_missing_column(self):
        """Test merge khi thiếu cột `on_column`."""
        df_wrong = pd.DataFrame({
            'timestamp': [1.0, 2.0, 3.0],  # Sai tên cột
            'value2': [10, 20, 30]
        })
        with self.assertRaises(KeyError):
            async_merge(self.df1, df_wrong, on_column='time', tolerance=0.5)

if __name__ == '__main__':
    unittest.main()
