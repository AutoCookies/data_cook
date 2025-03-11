import unittest
import pandas as pd
from data_py.csv.join import join_on_condition

class TestJoinOnCondition(unittest.TestCase):
    def test_valid_input(self):
        # Create sample dataframes
        left = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        right = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
        condition = pd.Series([True, False, True])

        # Call the function
        result = join_on_condition(left, right, condition)

        # Check the result
        expected_result = pd.DataFrame({'A': [1, 3], 'B': [4, 6], 'C': [7, 9], 'D': [10, 12]})
        pd.testing.assert_frame_equal(result, expected_result)

    def test_none_input_dataframes(self):
        with self.assertRaises(ValueError):
            join_on_condition(None, pd.DataFrame(), pd.Series())

        with self.assertRaises(ValueError):
            join_on_condition(pd.DataFrame(), None, pd.Series())

    def test_none_condition(self):
        with self.assertRaises(ValueError):
            join_on_condition(pd.DataFrame(), pd.DataFrame(), None)

    def test_non_pandas_series_condition(self):
        with self.assertRaises(TypeError):
            join_on_condition(pd.DataFrame(), pd.DataFrame(), [True, False, True])

    def test_empty_condition(self):
        with self.assertRaises(ValueError):
            join_on_condition(pd.DataFrame(), pd.DataFrame(), pd.Series())

    def test_mismatched_index_lengths(self):
        left = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        right = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
        condition = pd.Series([True, False])  # shorter than left dataframe

        with self.assertRaises(KeyError):
            join_on_condition(left, right, condition)

    def test_mismatched_index_lengths_between_left_and_right(self):
        left = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        right = pd.DataFrame({'C': [7, 8], 'D': [10, 11]})  # shorter than left dataframe
        condition = pd.Series([True, False, True])

        with self.assertRaises(KeyError):
            join_on_condition(left, right, condition)

if __name__ == '__main__':
    unittest.main()