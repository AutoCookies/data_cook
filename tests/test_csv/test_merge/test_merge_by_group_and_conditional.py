import unittest
import pandas as pd
from data_py.csv.merge import merge_by_group_and_condition

class TestMergeByGroupAndCondition(unittest.TestCase):
    def setUp(self):
        """Tạo các DataFrame test trước mỗi test case."""
        self.df1 = pd.DataFrame({
            'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
            'Value': [10, 20, 30, 40, 50, 60],
            'Condition': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No']
        })

        self.df2 = pd.DataFrame({
            'Group': ['A', 'B', 'C'],
            'Extra': [100, 200, 300]
        })

    def test_merge_with_valid_condition(self):
        """Test merge khi điều kiện hợp lệ (`Condition == 'Yes'`)."""
        result = merge_by_group_and_condition(self.df1, self.df2, 'Group', 'Condition', 'Yes')

        expected = pd.DataFrame({
            'Group': ['A', 'B', 'C'],
            'Value': [10, 30, 50],
            'Condition': ['Yes', 'Yes', 'Yes'],
            'Extra': [100, 200, 300]
        }).reset_index(drop=True)

        pd.testing.assert_frame_equal(result, expected)

    def test_merge_with_no_matching_condition(self):
        """Test merge khi không có hàng nào thỏa mãn điều kiện (`Condition == 'Maybe'`)."""
        result = merge_by_group_and_condition(self.df1, self.df2, 'Group', 'Condition', 'Maybe')
        expected = pd.DataFrame(columns=['Group', 'Value', 'Condition', 'Extra'])  # Kết quả rỗng

        pd.testing.assert_frame_equal(result, expected)

    def test_merge_with_multiple_matching_groups(self):
        """Test merge với nhiều nhóm thỏa mãn điều kiện (`Condition == 'Yes'`)."""
        result = merge_by_group_and_condition(self.df1, self.df2, 'Group', 'Condition', 'Yes')

        expected = pd.DataFrame({
            'Group': ['A', 'B', 'C'],
            'Value': [10, 30, 50],
            'Condition': ['Yes', 'Yes', 'Yes'],
            'Extra': [100, 200, 300]
        }).reset_index(drop=True)

        pd.testing.assert_frame_equal(result, expected)

    def test_merge_with_left_join(self):
        """Test merge với kiểu 'left join'."""
        result = merge_by_group_and_condition(self.df1, self.df2, 'Group', 'Condition', 'Yes', how='left')

        expected = pd.DataFrame({
            'Group': ['A', 'B', 'C'],
            'Value': [10, 30, 50],
            'Condition': ['Yes', 'Yes', 'Yes'],
            'Extra': [100, 200, 300]
        }).reset_index(drop=True)

        pd.testing.assert_frame_equal(result, expected)

    def test_merge_with_outer_join(self):
        """Test merge với kiểu 'outer join'."""
        result = merge_by_group_and_condition(self.df1, self.df2, 'Group', 'Condition', 'Yes', how='outer')

        expected = pd.DataFrame({
            'Group': ['A', 'B', 'C'],
            'Value': [10, 30, 50],
            'Condition': ['Yes', 'Yes', 'Yes'],
            'Extra': [100, 200, 300]
        }).reset_index(drop=True)

        pd.testing.assert_frame_equal(result, expected)

    def test_merge_with_empty_dataframe(self):
        """Test merge khi df1 hoặc df2 rỗng."""
        empty_df = pd.DataFrame(columns=['Group', 'Value', 'Condition'])
        result = merge_by_group_and_condition(empty_df, self.df2, 'Group', 'Condition', 'Yes')

        expected = pd.DataFrame(columns=['Group', 'Value', 'Condition', 'Extra'])  # Kết quả rỗng
        pd.testing.assert_frame_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
