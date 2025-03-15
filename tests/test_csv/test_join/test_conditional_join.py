import pandas as pd
import unittest
from data_cook import join_on_condition

class TestJoinOnCondition(unittest.TestCase):
    def test_valid_inputs(self):
        left = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        right = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
        condition = pd.Series([True, False, True], index=[0, 1, 2])
        result = join_on_condition(left, right, condition)
        expected = pd.DataFrame({'A': [1, 3], 'B': [4, 6], 'C': [7, 9], 'D': [10, 12]})
        pd.testing.assert_frame_equal(result, expected)

    def test_missing_left_dataframe(self):
        right = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
        condition = pd.Series([True, False, True], index=[0, 1, 2])
        with self.assertRaises(ValueError):
            join_on_condition(None, right, condition)

    def test_missing_right_dataframe(self):
        left = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        condition = pd.Series([True, False, True], index=[0, 1, 2])
        with self.assertRaises(ValueError):
            join_on_condition(left, None, condition)

    def test_missing_condition(self):
        left = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        right = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
        with self.assertRaises(ValueError):
            join_on_condition(left, right, None)

    def test_non_pandas_series_condition(self):
        left = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        right = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
        condition = [True, False, True]
        with self.assertRaises(TypeError):
            join_on_condition(left, right, condition)

    def test_empty_condition(self):
        left = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        right = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
        condition = pd.Series()
        with self.assertRaises(ValueError):
            join_on_condition(left, right, condition)

    def test_condition_doesnt_match_left_dataframe_index(self):
        left = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        right = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
        condition = pd.Series([True, False, True], index=[3, 4, 5])
        result = join_on_condition(left, right, condition)
        expected = pd.DataFrame({'A': [], 'B': [], 'C': [], 'D': []})
        pd.testing.assert_frame_equal(result, expected)

if __name__ == '__main__':
    unittest.main()