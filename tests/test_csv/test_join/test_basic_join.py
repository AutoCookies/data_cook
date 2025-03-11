import unittest
import pandas as pd
from data_py.csv.join.basic_join import join_dataframes

class TestJoinDataframes(unittest.TestCase):

    def test_valid_input(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'value': [10, 20, 30]})
        df2 = pd.DataFrame({'id': [1, 2, 3], 'value2': [100, 200, 300]})
        result = join_dataframes(df1, df2, 'id')
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)

    def test_invalid_input_dataframes(self):
        df1 = None
        df2 = pd.DataFrame({'id': [1, 2, 3], 'value2': [100, 200, 300]})
        with self.assertRaises(ValueError):
            join_dataframes(df1, df2, 'id')

    def test_invalid_join_column(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'value': [10, 20, 30]})
        df2 = pd.DataFrame({'id': [1, 2, 3], 'value2': [100, 200, 300]})
        with self.assertRaises(ValueError):
            join_dataframes(df1, df2, 123)

    def test_invalid_join_type(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'value': [10, 20, 30]})
        df2 = pd.DataFrame({'id': [1, 2, 3], 'value2': [100, 200, 300]})
        with self.assertRaises(ValueError):
            join_dataframes(df1, df2, 'id', 'invalid_join_type')

    def test_join_column_not_present(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'value': [10, 20, 30]})
        df2 = pd.DataFrame({'id2': [1, 2, 3], 'value2': [100, 200, 300]})
        with self.assertRaises(ValueError):
            join_dataframes(df1, df2, 'id')

    def test_inner_join(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'value': [10, 20, 30]})
        df2 = pd.DataFrame({'id': [1, 2, 3], 'value2': [100, 200, 300]})
        result = join_dataframes(df1, df2, 'id', 'inner')
        self.assertEqual(len(result), 3)

    def test_outer_join(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'value': [10, 20, 30]})
        df2 = pd.DataFrame({'id': [1, 2, 4], 'value2': [100, 200, 400]})
        result = join_dataframes(df1, df2, 'id', 'outer')
        self.assertEqual(len(result), 4)

    def test_left_join(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'value': [10, 20, 30]})
        df2 = pd.DataFrame({'id': [1, 2, 4], 'value2': [100, 200, 400]})
        result = join_dataframes(df1, df2, 'id', 'left')
        self.assertEqual(len(result), 3)

    def test_right_join(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'value': [10, 20, 30]})
        df2 = pd.DataFrame({'id': [1, 2, 4], 'value2': [100, 200, 400]})
        result = join_dataframes(df1, df2, 'id', 'right')
        self.assertEqual(len(result), 3)

if __name__ == '__main__':
    unittest.main()