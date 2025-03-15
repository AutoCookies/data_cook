import unittest
import pandas as pd
from data_cook import group_and_filter

class TestGroupAndFilter(unittest.TestCase):
    def test_valid_input(self):
        dataframe = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        group_by_column = 'A'
        filter_function = lambda x: x['B'].mean() > 5
        result = group_and_filter(dataframe, group_by_column, filter_function)
        self.assertEqual(len(result), 1)

    def test_none_dataframe(self):
        with self.assertRaises(ValueError):
            group_and_filter(None, 'A', lambda x: x['B'].mean() > 5)

    def test_none_group_by_column(self):
        dataframe = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        with self.assertRaises(ValueError):
            group_and_filter(dataframe, None, lambda x: x['B'].mean() > 5)

    def test_none_filter_function(self):
        dataframe = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        with self.assertRaises(ValueError):
            group_and_filter(dataframe, 'A', None)

    def test_empty_dataframe(self):
        dataframe = pd.DataFrame()
        group_by_column = 'A'
        filter_function = lambda x: x['B'].mean() > 5
        result = group_and_filter(dataframe, group_by_column, filter_function)
        self.assertEqual(len(result), 0)

    def test_filter_function_returns_false(self):
        dataframe = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        group_by_column = 'A'
        filter_function = lambda x: x['B'].mean() < 0
        result = group_and_filter(dataframe, group_by_column, filter_function)
        self.assertEqual(len(result), 0)

    def test_filter_function_returns_true(self):
        dataframe = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        group_by_column = 'A'
        filter_function = lambda x: x['B'].mean() > 0
        result = group_and_filter(dataframe, group_by_column, filter_function)
        self.assertEqual(len(result), 3)

    def test_exception_in_filter_function(self):
        dataframe = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        group_by_column = 'A'
        filter_function = lambda x: x['C'].mean() > 5
        with self.assertRaises(Exception):
            group_and_filter(dataframe, group_by_column, filter_function)

if __name__ == '__main__':
    unittest.main()