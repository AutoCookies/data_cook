import unittest
import pandas as pd
from data_py.csv.group.group_and_aggregate import group_and_aggregate

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

    def test_invalid_input_types(self):
        # Tạo DataFrame có dữ liệu thay vì DataFrame rỗng
        df = pd.DataFrame({'Category': ['A', 'B'], 'Value': [10, 20]})

        # Test với non-DataFrame input
        with self.assertRaises(TypeError):
            group_and_aggregate('not a dataframe', 'Category', {'Value': ['sum', 'mean']})
        
        # Test với non-string/list group_cols
        with self.assertRaises(TypeError):
            group_and_aggregate(df, 123, {'Value': ['sum', 'mean']})
        
        # Test với non-dict aggregation_dict
        with self.assertRaises(TypeError):
            group_and_aggregate(df, 'Category', 'not a dict')


    def test_empty_dataframe(self):
        # Test with empty DataFrame
        with self.assertRaises(ValueError):
            group_and_aggregate(pd.DataFrame(), 'Category', {'Value': ['sum', 'mean']})

    def test_missing_columns(self):
        # Test with missing columns in group_cols
        with self.assertRaises(KeyError):
            group_and_aggregate(pd.DataFrame({'A': [1, 2]}), 'B', {'A': ['sum']})
        
        # Test with missing columns in aggregation_dict
        with self.assertRaises(KeyError):
            group_and_aggregate(pd.DataFrame({'A': [1, 2]}), 'A', {'B': ['sum']})

    def test_aggregation_error(self):
        # Test with aggregation error
        with self.assertRaises(RuntimeError):
            group_and_aggregate(pd.DataFrame({'A': [1, 2]}), 'A', {'A': [' invalid_func']})

if __name__ == '__main__':
    unittest.main()