import unittest
import pandas as pd
from data_py.csv.group.group_and_aggregate import group_and_aggregate

import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestGroupAndAggregate(unittest.TestCase):
    def test_valid_input(self):
        # Create a sample DataFrame
        data = {'Category': ['A', 'B', 'A', 'B'], 
                'Value': [10, 20, 30, 40]}
        df = pd.DataFrame(data)

        # Define group_cols and aggregation_dict
        group_cols = 'Category'
        aggregation_dict = {'Value': ['sum', 'mean']}

        # Call the function
        result = group_and_aggregate(df, group_cols, aggregation_dict)

        # Check the result
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(result.shape, (2, 2))

    def test_invalid_input_none_values(self):
        # Test with None values for dataframe, group_cols, and aggregation_dict
        with self.assertRaises(ValueError):
            group_and_aggregate(None, None, None)

    def test_invalid_input_non_dataframe(self):
        # Test with non-DataFrame input
        with self.assertRaises(TypeError):
            group_and_aggregate('not a dataframe', 'Category', {'Value': ['sum', 'mean']})

    def test_invalid_input_non_dict_aggregation_dict(self):
        # Test with non-dict aggregation_dict
        with self.assertRaises(TypeError):
            group_and_aggregate(pd.DataFrame(), 'Category', 'not a dict')

    def test_invalid_input_non_string_list_group_cols(self):
        # Test with non-string/list group_cols
        with self.assertRaises(TypeError):
            group_and_aggregate(pd.DataFrame(), 123, {'Value': ['sum', 'mean']})

    def test_invalid_aggregation_functions(self):
        # Test with aggregation_dict containing invalid aggregation functions
        with self.assertRaises(KeyError):
            group_and_aggregate(pd.DataFrame(), 'Category', {'Value': [' invalid_func']})

    def test_non_existent_columns(self):
        # Test with group_cols containing non-existent columns
        with self.assertRaises(KeyError):
            group_and_aggregate(pd.DataFrame(), 'non_existent_column', {'Value': ['sum', 'mean']})

if __name__ == '__main__':
    unittest.main()