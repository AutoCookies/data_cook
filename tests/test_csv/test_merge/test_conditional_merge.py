import unittest
import pandas as pd
from data_py.csv.merge import conditional_merge

class TestConditionalMerge(unittest.TestCase):
    def setUp(self):
        """Tạo các DataFrame test trước mỗi test case."""
        self.df1 = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': ['X', 'Y', 'Z', 'W', 'V']
        })

        self.df2 = pd.DataFrame({
            'C': [10, 20, 30, 40, 50],
            'D': ['P', 'Q', 'R', 'S', 'T']
        })

    def test_merge_with_valid_condition(self):
        """Test merge khi điều kiện hợp lệ (chọn một số hàng cụ thể)."""
        condition = self.df1['A'] > 2  # Chỉ chọn A > 2 (hàng index 2,3,4)
        result = conditional_merge(self.df1, self.df2, condition)

        expected = pd.DataFrame({
            'A': [3, 4, 5],
            'B': ['Z', 'W', 'V'],
            'C': [30, 40, 50],
            'D': ['R', 'S', 'T']
        }, index=[2, 3, 4])

        pd.testing.assert_frame_equal(result, expected)

    def test_merge_with_no_matching_condition(self):
        """Test merge khi điều kiện không khớp bản ghi nào."""
        condition = self.df1['A'] > 10  # Không có giá trị nào thỏa mãn
        result = conditional_merge(self.df1, self.df2, condition)

        expected = pd.DataFrame(columns=['A', 'B', 'C', 'D'])  # DataFrame rỗng
        pd.testing.assert_frame_equal(result, expected)

    def test_merge_with_complex_condition(self):
        """Test merge với điều kiện phức tạp (kết hợp nhiều điều kiện)."""
        condition = (self.df1['A'] > 1) & (self.df1['A'] < 5)  # Chọn 2 ≤ A ≤ 4
        result = conditional_merge(self.df1, self.df2, condition)

        expected = pd.DataFrame({
            'A': [2, 3, 4],
            'B': ['Y', 'Z', 'W'],
            'C': [20, 30, 40],
            'D': ['Q', 'R', 'S']
        }, index=[1, 2, 3])

        pd.testing.assert_frame_equal(result, expected)

    def test_merge_with_invalid_condition(self):
        """Test merge khi condition không phải Series hợp lệ."""
        with self.assertRaises(TypeError):
            conditional_merge(self.df1, self.df2, "A > 2")  # Điều kiện sai kiểu

    def test_merge_with_empty_dataframe(self):
        """Test merge khi df1 hoặc df2 rỗng."""
        empty_df = pd.DataFrame(columns=['A', 'B'])
        condition = empty_df.index > 0  # Điều kiện này không có tác dụng vì df rỗng

        result = conditional_merge(empty_df, self.df2, condition)
        expected = pd.DataFrame(columns=['A', 'B', 'C', 'D'])  # Kết quả cũng phải rỗng

        pd.testing.assert_frame_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
