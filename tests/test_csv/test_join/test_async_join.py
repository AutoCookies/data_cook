import unittest
import pandas as pd
import logging
from data_cook import async_join

class TestAsyncJoin(unittest.TestCase):

    def test_valid_input(self):
        # Create sample dataframes
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df2 = pd.DataFrame({'A': [1.1, 2.1, 3.1], 'C': [7, 8, 9]})

        # Test with valid input
        result = async_join(df1, df2, 'A', 0.1)
        self.assertIsNotNone(result)

    def test_invalid_input_not_dataframes(self):
        # Test with invalid input (not pandas DataFrames)
        df1 = 'not a dataframe'
        df2 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

        with self.assertRaises(ValueError):
            async_join(df1, df2, 'A', 0.1)

    def test_missing_on_column(self):
        # Test with missing on_column in one of the dataframes
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df2 = pd.DataFrame({'C': [7, 8, 9]})

        with self.assertRaises(ValueError):
            async_join(df1, df2, 'A', 0.1)

    def test_tolerance_zero(self):
        # Test with tolerance value of 0
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df2 = pd.DataFrame({'A': [1.1, 2.1, 3.1], 'C': [7, 8, 9]})

        result = async_join(df1, df2, 'A', 0)
        self.assertIsNotNone(result)

    def test_tolerance_greater_than_zero(self):
        # Test with tolerance value greater than 0
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df2 = pd.DataFrame({'A': [1.1, 2.1, 3.1], 'C': [7, 8, 9]})

        result = async_join(df1, df2, 'A', 0.1)
        self.assertIsNotNone(result)

    def test_error_handling(self):
        # Test with error handling (exception raised)
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df2 = pd.DataFrame({'A': [1.1, 2.1, 3.1], 'C': [7, 8, 9]})

        # Simulate an error
        with self.assertRaises(Exception):
            async_join(df1, df2, 'A', ' invalid tolerance')

if __name__ == '__main__':
    unittest.main()