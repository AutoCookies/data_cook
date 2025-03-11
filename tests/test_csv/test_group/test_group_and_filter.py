import unittest
import pandas as pd
import logging
import data_py.csv.group.group_and_filter as group_and_filter

class TestGroupAndFilter(unittest.TestCase):
    def test_valid_input(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
        group_column = 'A'
        filter_func = lambda x: x['B'].mean() > 20
        result = group_and_filter(df, group_column, filter_func)
        self.assertIsInstance(result, pd.DataFrame)

    def test_invalid_input_none_values(self):
        df = None
        group_column = 'A'
        filter_func = lambda x: x['B'].mean() > 20
        with self.assertRaises(ValueError):
            group_and_filter(df, group_column, filter_func)

        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
        group_column = None
        filter_func = lambda x: x['B'].mean() > 20
        with self.assertRaises(ValueError):
            group_and_filter(df, group_column, filter_func)

        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
        group_column = 'A'
        filter_func = None
        with self.assertRaises(ValueError):
            group_and_filter(df, group_column, filter_func)

    def test_filter_func_returns_true_for_all_groups(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
        group_column = 'A'
        filter_func = lambda x: True
        result = group_and_filter(df, group_column, filter_func)
        self.assertEqual(len(result), len(df))

    def test_filter_func_returns_false_for_all_groups(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
        group_column = 'A'
        filter_func = lambda x: False
        result = group_and_filter(df, group_column, filter_func)
        self.assertEqual(len(result), 0)

    def test_filter_func_returns_true_for_some_groups_and_false_for_others(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
        group_column = 'A'
        filter_func = lambda x: x['B'].mean() > 20
        result = group_and_filter(df, group_column, filter_func)
        self.assertLess(len(result), len(df))

    def test_exception_raised_during_filtering(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
        group_column = 'A'
        filter_func = lambda x: x['C'].mean()  # raises KeyError
        with self.assertRaises(Exception):
            group_and_filter(df, group_column, filter_func)

if __name__ == '__main__':
    unittest.main()