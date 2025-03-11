import unittest
import pandas as pd
import logging
from your_module import async_join  # Replace with the actual module name

class TestAsyncJoin(unittest.TestCase):
    def test_valid_input(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'value': [10, 20, 30]})
        df2 = pd.DataFrame({'id': [1.1, 2.1, 3.1], 'value2': [100, 200, 300]})
        result = async_join(df1, df2, 'id', 0.1)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)

    def test_invalid_input(self):
        df1 = 'not a dataframe'
        df2 = pd.DataFrame({'id': [1, 2, 3], 'value': [10, 20, 30]})
        with self.assertRaises(ValueError):
            async_join(df1, df2, 'id', 0.1)

    def test_missing_on_column(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'value': [10, 20, 30]})
        df2 = pd.DataFrame({'value2': [100, 200, 300]})
        with self.assertRaises(ValueError):
            async_join(df1, df2, 'id', 0.1)

    def test_tolerance_zero(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'value': [10, 20, 30]})
        df2 = pd.DataFrame({'id': [1.1, 2.1, 3.1], 'value2': [100, 200, 300]})
        result = async_join(df1, df2, 'id', 0)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)

    def test_empty_dataframes(self):
        df1 = pd.DataFrame()
        df2 = pd.DataFrame()
        result = async_join(df1, df2, 'id', 0.1)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)

    def test_different_data_types(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'value': [10, 20, 30]})
        df2 = pd.DataFrame({'id': ['1.1', '2.1', '3.1'], 'value2': [100, 200, 300]})
        result = async_join(df1, df2, 'id', 0.1)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)

    def test_nan_values(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'value': [10, 20, 30]})
        df2 = pd.DataFrame({'id': [1.1, 2.1, np.nan], 'value2': [100, 200, 300]})
        result = async_join(df1, df2, 'id', 0.1)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    unittest.main()