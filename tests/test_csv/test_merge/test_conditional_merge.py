import unittest
import pandas as pd
from data_cook import conditional_merge

class TestConditionalMerge(unittest.TestCase):
    def test_valid_condition(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
        condition = pd.Series([True, False, True], index=[0, 1, 2])
        expected = pd.DataFrame({'A': [1, 3], 'B': [4, 6], 'C': [7, 9], 'D': [10, 12]})
        result = conditional_merge(df1, df2, condition)
        pd.testing.assert_frame_equal(result, expected)

    def test_invalid_condition(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
        condition = pd.Series([1, 2, 3], index=[0, 1, 2])
        with self.assertRaises(ValueError):
            conditional_merge(df1, df2, condition)

    def test_missing_values_in_condition(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
        condition = pd.Series([True, None, True], index=[0, 1, 2])
        with self.assertRaises(ValueError):
            conditional_merge(df1, df2, condition)

    def test_condition_doesnt_match_index_of_df1(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
        condition = pd.Series([True, False, True], index=[3, 4, 5])
        with self.assertRaises(ValueError):
            conditional_merge(df1, df2, condition)

    def test_empty_dataframes(self):
        df1 = pd.DataFrame()
        df2 = pd.DataFrame()
        condition = pd.Series()
        expected = pd.DataFrame()
        result = conditional_merge(df1, df2, condition)
        pd.testing.assert_frame_equal(result, expected)

    def test_non_pandas_dataframe_inputs(self):
        df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        df2 = 'not a dataframe'
        condition = pd.Series([True, False, True], index=[0, 1, 2])
        with self.assertRaises(TypeError):
            conditional_merge(df1, df2, condition)

if __name__ == '__main__':
    unittest.main()