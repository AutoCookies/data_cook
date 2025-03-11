import pandas as pd
import unittest
from data_py.csv.join import join_with_suffix

class TestJoinWithSuffix(unittest.TestCase):

    def test_inner_join_default_suffixes(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
        df2 = pd.DataFrame({'id': [1, 2, 4], 'age': [25, 30, 35]})
        result = join_with_suffix(df1, df2, 'id')
        expected = pd.DataFrame({'id': [1, 2], 'name': ['Alice', 'Bob'], 'age_left': [25, 30]})
        pd.testing.assert_frame_equal(result, expected)

    def test_inner_join_custom_suffixes(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
        df2 = pd.DataFrame({'id': [1, 2, 4], 'age': [25, 30, 35]})
        result = join_with_suffix(df1, df2, 'id', suffixes=('_x', '_y'))
        expected = pd.DataFrame({'id': [1, 2], 'name': ['Alice', 'Bob'], 'age_x': [25, 30]})
        pd.testing.assert_frame_equal(result, expected)

    def test_outer_join(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
        df2 = pd.DataFrame({'id': [1, 2, 4], 'age': [25, 30, 35]})
        result = join_with_suffix(df1, df2, 'id', how='outer')
        expected = pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['Alice', 'Bob', 'Charlie', None], 'age_left': [25, 30, None, 35]})
        pd.testing.assert_frame_equal(result, expected)

    def test_left_join(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
        df2 = pd.DataFrame({'id': [1, 2, 4], 'age': [25, 30, 35]})
        result = join_with_suffix(df1, df2, 'id', how='left')
        expected = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie'], 'age_left': [25, 30, None]})
        pd.testing.assert_frame_equal(result, expected)

    def test_right_join(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
        df2 = pd.DataFrame({'id': [1, 2, 4], 'age': [25, 30, 35]})
        result = join_with_suffix(df1, df2, 'id', how='right')
        expected = pd.DataFrame({'id': [1, 2, 4], 'name': ['Alice', 'Bob', None], 'age_right': [25, 30, 35]})
        pd.testing.assert_frame_equal(result, expected)

    def test_join_non_existent_column(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
        df2 = pd.DataFrame({'id': [1, 2, 4], 'age': [25, 30, 35]})
        with self.assertRaises(KeyError):
            join_with_suffix(df1, df2, 'non_existent_column')

    def test_join_mismatched_data_types(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
        df2 = pd.DataFrame({'id': ['a', 'b', 'c'], 'age': [25, 30, 35]})
        with self.assertRaises(TypeError):
            join_with_suffix(df1, df2, 'id')

if __name__ == '__main__':
    unittest.main()