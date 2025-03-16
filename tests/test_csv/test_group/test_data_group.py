import unittest
import pandas as pd
import os
import shutil
from data_cook import data_group

class TestDataGroup(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50],
            'C': ['a', 'b', 'c', 'd', 'e']
        })

    def test_valid_input(self):
        result = data_group(self.df, 'C', is_save=False)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 5)

    def test_valid_input_save(self):
        output_dir = 'test_output'
        result = data_group(self.df, 'C', is_save=True, output_dir=output_dir)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 5)
        self.assertTrue(os.path.exists(output_dir))
        for key in result:
            filename = f"C_{key}.csv"
            filepath = os.path.join(output_dir, filename)
            self.assertTrue(os.path.exists(filepath))
        shutil.rmtree(output_dir)

    def test_invalid_input_none(self):
        with self.assertRaises(ValueError):
            data_group(None, None)

    def test_invalid_input_column_not_found(self):
        with self.assertRaises(KeyError):
            data_group(self.df, 'D')

    def test_exception_permission_error(self):
        output_dir = '/root/test_output'
        with self.assertRaises(PermissionError):
            data_group(self.df, 'C', is_save=True, output_dir=output_dir)

if __name__ == '__main__':
    unittest.main()