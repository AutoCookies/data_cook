import unittest
import pandas as pd
from data_cook import async_merge

class TestAsyncMerge(unittest.TestCase):

    def test_valid_input_matching_values(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 20, 30]})
        df2 = pd.DataFrame({'A': [1, 2, 3], 'C': [100, 200, 300]})
        result = async_merge(df1, df2, 'A', 0)
        expected = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 20, 30], 'C': [100, 200, 300]})
        pd.testing.assert_frame_equal(result, expected)

    def test_valid_input_non_matching_values(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 20, 30]})
        df2 = pd.DataFrame({'A': [2, 3, 4], 'C': [200, 300, 400]})
        result = async_merge(df1, df2, 'A', 0)
        expected = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 20, 30], 'C': [None, 200, 300]})
        pd.testing.assert_frame_equal(result, expected)

    def test_invalid_input_non_dataframe(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 20, 30]})
        df2 = 'not a dataframe'
        with self.assertRaises(TypeError):
            async_merge(df1, df2, 'A', 0)

    def test_missing_on_column(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 20, 30]})
        df2 = pd.DataFrame({'C': [100, 200, 300]})
        with self.assertRaises(KeyError):
            async_merge(df1, df2, 'A', 0)

    def test_tolerance_zero(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 20, 30]})
        df2 = pd.DataFrame({'A': [1.1, 2.1, 3.1], 'C': [100, 200, 300]})
        result = async_merge(df1, df2, 'A', 0)
        expected = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 20, 30], 'C': [None, None, None]})
        pd.testing.assert_frame_equal(result, expected)

    def test_tolerance_greater_than_zero(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 20, 30]})
        df2 = pd.DataFrame({'A': [1.1, 2.1, 3.1], 'C': [100, 200, 300]})
        result = async_merge(df1, df2, 'A', 0.1)
        expected = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 20, 30], 'C': [100, 200, 300]})
        pd.testing.assert_frame_equal(result, expected)

    def test_error_handling(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 20, 30]})
        df2 = pd.DataFrame({'A': [1, 2, 3], 'C': [100, 200, 300]})
        with self.assertRaises(TypeError):
            async_merge(df1, df2, 'A', 'not a float')

if __name__ == '__main__':
    unittest.main()