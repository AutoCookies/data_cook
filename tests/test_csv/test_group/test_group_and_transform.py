import unittest
import pandas as pd
import logging
from data_cook import group_and_transform_data

class TestGroupAndTransformData(unittest.TestCase):
    def test_valid_input(self):
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        group_by_column = 'A'
        transform_column = 'B'
        transform_function = lambda x: x.mean()

        result = group_and_transform_data(data, group_by_column, transform_column, transform_function)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertIn('B_transformed', result.columns)

    def test_invalid_input_data_none(self):
        data = None
        group_by_column = 'A'
        transform_column = 'B'
        transform_function = lambda x: x.mean()

        with self.assertRaises(ValueError):
            group_and_transform_data(data, group_by_column, transform_column, transform_function)

    def test_invalid_input_group_by_column_none(self):
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        group_by_column = None
        transform_column = 'B'
        transform_function = lambda x: x.mean()

        with self.assertRaises(ValueError):
            group_and_transform_data(data, group_by_column, transform_column, transform_function)

    def test_invalid_input_transform_column_none(self):
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        group_by_column = 'A'
        transform_column = None
        transform_function = lambda x: x.mean()

        with self.assertRaises(ValueError):
            group_and_transform_data(data, group_by_column, transform_column, transform_function)

    def test_invalid_input_transform_function_none(self):
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        group_by_column = 'A'
        transform_column = 'B'
        transform_function = None

        with self.assertRaises(ValueError):
            group_and_transform_data(data, group_by_column, transform_column, transform_function)

    def test_invalid_input_transform_column_non_existent(self):
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        group_by_column = 'A'
        transform_column = 'C'
        transform_function = lambda x: x.mean()

        with self.assertRaises(ValueError):
            group_and_transform_data(data, group_by_column, transform_column, transform_function)

    def test_invalid_input_transform_function_non_callable(self):
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        group_by_column = 'A'
        transform_column = 'B'
        transform_function = 'mean'

        with self.assertRaises(ValueError):
            group_and_transform_data(data, group_by_column, transform_column, transform_function)

    def test_multiple_groups_and_transformations(self):
        data = pd.DataFrame({'A': [1, 1, 2, 2], 'B': [4, 5, 6, 7]})
        group_by_column = 'A'
        transform_column = 'B'
        transform_function = lambda x: x.mean()

        result = group_and_transform_data(data, group_by_column, transform_column, transform_function)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertIn('B_transformed', result.columns)
        self.assertEqual(result.shape[0], 4)

if __name__ == '__main__':
    unittest.main()