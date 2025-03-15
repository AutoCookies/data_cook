import pandas as pd
import unittest
from data_cook import join_with_suffix

class TestJoinWithSuffix(unittest.TestCase):
    def test_inner_join_default_suffixes(self):
        left_df = pd.DataFrame({'key': ['A', 'B', 'C'], 'value_left': [1, 2, 3]})
        right_df = pd.DataFrame({'key': ['A', 'B', 'D'], 'value_right': [4, 5, 6]})
        result = join_with_suffix(left_df, right_df, 'key')
        expected = pd.DataFrame({'key': ['A', 'B'], 'value_left': [1, 2], 'value_right': [4, 5]})
        pd.testing.assert_frame_equal(result, expected)

    def test_outer_join_default_suffixes(self):
        left_df = pd.DataFrame({'key': ['A', 'B', 'C'], 'value_left': [1, 2, 3]})
        right_df = pd.DataFrame({'key': ['A', 'B', 'D'], 'value_right': [4, 5, 6]})
        result = join_with_suffix(left_df, right_df, 'key', how='outer')
        expected = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value_left': [1, 2, 3, None], 'value_right': [4, 5, None, 6]})
        pd.testing.assert_frame_equal(result, expected)

    def test_left_join_default_suffixes(self):
        left_df = pd.DataFrame({'key': ['A', 'B', 'C'], 'value_left': [1, 2, 3]})
        right_df = pd.DataFrame({'key': ['A', 'B', 'D'], 'value_right': [4, 5, 6]})
        result = join_with_suffix(left_df, right_df, 'key', how='left')
        expected = pd.DataFrame({'key': ['A', 'B', 'C'], 'value_left': [1, 2, 3], 'value_right': [4, 5, None]})
        pd.testing.assert_frame_equal(result, expected)

    def test_right_join_default_suffixes(self):
        left_df = pd.DataFrame({'key': ['A', 'B', 'C'], 'value_left': [1, 2, 3]})
        right_df = pd.DataFrame({'key': ['A', 'B', 'D'], 'value_right': [4, 5, 6]})
        result = join_with_suffix(left_df, right_df, 'key', how='right')
        expected = pd.DataFrame({'key': ['A', 'B', 'D'], 'value_left': [1, 2, None], 'value_right': [4, 5, 6]})
        pd.testing.assert_frame_equal(result, expected)

    def test_inner_join_custom_suffixes(self):
        left_df = pd.DataFrame({'key': ['A', 'B', 'C'], 'value_left': [1, 2, 3]})
        right_df = pd.DataFrame({'key': ['A', 'B', 'D'], 'value_right': [4, 5, 6]})
        result = join_with_suffix(left_df, right_df, 'key', suffixes=('_foo', '_bar'))
        expected = pd.DataFrame({'key': ['A', 'B'], 'value_foo': [1, 2], 'value_bar': [4, 5]})
        pd.testing.assert_frame_equal(result, expected)

    def test_invalid_input_types(self):
        with self.assertRaises(ValueError):
            join_with_suffix('not a dataframe', pd.DataFrame({'key': ['A', 'B']}), 'key')

    def test_invalid_join_type(self):
        with self.assertRaises(ValueError):
            join_with_suffix(pd.DataFrame({'key': ['A', 'B']}), pd.DataFrame({'key': ['A', 'B']}), 'key', how=' invalid')

    def test_invalid_suffixes(self):
        with self.assertRaises(ValueError):
            join_with_suffix(pd.DataFrame({'key': ['A', 'B']}), pd.DataFrame({'key': ['A', 'B']}), 'key', suffixes=(' invalid',))

if __name__ == '__main__':
    unittest.main()