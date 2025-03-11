import unittest
import pandas as pd
import logging
from data_py.csv.group.group_and_transform import group_and_transform_data

class TestGroupAndTransformData(unittest.TestCase):

    def test_valid_input(self):
        # Create a sample dataframe
        data = pd.DataFrame({
            'group': ['A', 'A', 'B', 'B'],
            'value': [1, 2, 3, 4]
        })

        # Define a transformation function
        def transform_function(x):
            return x * 2

        # Call the function with valid input
        result = group_and_transform_data(data, 'group', 'value', transform_function)

        # Check the result
        self.assertEqual(result.shape, (4, 3))
        self.assertIn('value_transformed', result.columns)

    def test_invalid_input_data_none(self):
        # Call the function with invalid input (data is None)
        with self.assertRaises(ValueError):
            group_and_transform_data(None, 'group', 'value', lambda x: x)

    def test_invalid_input_group_by_column_none(self):
        # Create a sample dataframe
        data = pd.DataFrame({
            'group': ['A', 'A', 'B', 'B'],
            'value': [1, 2, 3, 4]
        })

        # Call the function with invalid input (group_by_column is None)
        with self.assertRaises(ValueError):
            group_and_transform_data(data, None, 'value', lambda x: x)

    def test_invalid_input_transform_column_none(self):
        # Create a sample dataframe
        data = pd.DataFrame({
            'group': ['A', 'A', 'B', 'B'],
            'value': [1, 2, 3, 4]
        })

        # Call the function with invalid input (transform_column is None)
        with self.assertRaises(ValueError):
            group_and_transform_data(data, 'group', None, lambda x: x)

    def test_invalid_input_transform_function_none(self):
        # Create a sample dataframe
        data = pd.DataFrame({
            'group': ['A', 'A', 'B', 'B'],
            'value': [1, 2, 3, 4]
        })

        # Call the function with invalid input (transform_function is None)
        with self.assertRaises(ValueError):
            group_and_transform_data(data, 'group', 'value', None)

    def test_non_existent_column(self):
        # Create a sample dataframe
        data = pd.DataFrame({
            'group': ['A', 'A', 'B', 'B'],
            'value': [1, 2, 3, 4]
        })

        # Define a transformation function
        def transform_function(x):
            return x * 2

        # Call the function with non-existent column
        with self.assertRaises(ValueError):
            group_and_transform_data(data, 'group', 'non_existent_column', transform_function)

    def test_exception_during_transformation(self):
        # Create a sample dataframe
        data = pd.DataFrame({
            'group': ['A', 'A', 'B', 'B'],
            'value': [1, 2, 3, 4]
        })

        # Define a transformation function that raises an exception
        def transform_function(x):
            raise Exception('Test exception')

        # Call the function with exception during transformation
        with self.assertRaises(Exception):
            group_and_transform_data(data, 'group', 'value', transform_function)

if __name__ == '__main__':
    unittest.main()