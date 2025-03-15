import unittest
import pandas as pd
from data_cook import join_dataframes

class TestJoinDataframes(unittest.TestCase):
    def test_inner_join(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
        df2 = pd.DataFrame({'id': [1, 2, 3], 'age': [25, 30, 35]})
        result = join_dataframes(df1, df2, 'id')
        expected = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]})
        pd.testing.assert_frame_equal(result, expected)

    def test_outer_join(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
        df2 = pd.DataFrame({'id': [1, 2, 4], 'age': [25, 30, 40]})
        result = join_dataframes(df1, df2, 'id', 'outer')
        expected = pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['Alice', 'Bob', 'Charlie', None], 'age': [25, 30, None, 40]})
        pd.testing.assert_frame_equal(result, expected)

    def test_left_join(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
        df2 = pd.DataFrame({'id': [1, 2, 4], 'age': [25, 30, 40]})
        result = join_dataframes(df1, df2, 'id', 'left')
        expected = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, None]})
        pd.testing.assert_frame_equal(result, expected)

    def test_right_join(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
        df2 = pd.DataFrame({'id': [1, 2, 4], 'age': [25, 30, 40]})
        result = join_dataframes(df1, df2, 'id', 'right')
        expected = pd.DataFrame({'id': [1, 2, 4], 'name': ['Alice', 'Bob', None], 'age': [25, 30, 40]})
        pd.testing.assert_frame_equal(result, expected)

    def test_non_existent_column(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
        df2 = pd.DataFrame({'id': [1, 2, 3], 'age': [25, 30, 35]})
        with self.assertRaises(ValueError):
            join_dataframes(df1, df2, 'non_existent_column')

    def test_non_string_join_column(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
        df2 = pd.DataFrame({'id': [1, 2, 3], 'age': [25, 30, 35]})
        with self.assertRaises(ValueError):
            join_dataframes(df1, df2, 123)

    def test_invalid_join_type(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
        df2 = pd.DataFrame({'id': [1, 2, 3], 'age': [25, 30, 35]})
        with self.assertRaises(ValueError):
            join_dataframes(df1, df2, 'id', 'invalid_join_type')

    def test_none_dataframes(self):
        df1 = None
        df2 = pd.DataFrame({'id': [1, 2, 3], 'age': [25, 30, 35]})
        with self.assertRaises(ValueError):
            join_dataframes(df1, df2, 'id')

if __name__ == '__main__':
    unittest.main()