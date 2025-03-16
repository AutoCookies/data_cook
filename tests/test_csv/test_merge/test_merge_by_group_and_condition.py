import unittest
import pandas as pd
from data_cook import merge_by_group_and_condition

class TestMergeByGroupAndCondition(unittest.TestCase):
    def setUp(self):
        self.df1 = pd.DataFrame({
            'group': [1, 2, 3, 4],
            'value1': ['A', 'B', 'C', 'D']
        })
        
        self.df2 = pd.DataFrame({
            'group': [3, 4, 5, 6],
            'value2': ['X', 'Y', 'Z', 'W'],
            'condition_col': [10, 20, 10, 30]
        })
    
    def test_inner_merge_condition_match(self):
        result = merge_by_group_and_condition(self.df1, self.df2, 'group', 'condition_col', 10, how='inner')
        expected = pd.DataFrame({
            'group': [3],
            'value1': ['C'],
            'value2': ['X'],
            'condition_col': [10]
        })
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)
    
    def test_left_merge_no_match(self):
        result = merge_by_group_and_condition(self.df1, self.df2, 'group', 'condition_col', 99, how='left')
        self.assertTrue(result.empty)
    
    def test_right_merge(self):
        result = merge_by_group_and_condition(self.df1, self.df2, 'group', 'condition_col', 20, how='right')
        expected = pd.DataFrame({
            'group': [4],
            'value1': ['D'],
            'value2': ['Y'],
            'condition_col': [20]
        })
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)
    
    def test_outer_merge(self):
        result = merge_by_group_and_condition(self.df1, self.df2, 'group', 'condition_col', 10, how='outer')
        expected = pd.DataFrame({
            'group': [3],
            'value1': ['C'],
            'value2': ['X'],
            'condition_col': [10]
        })
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

if __name__ == '__main__':
    unittest.main()
