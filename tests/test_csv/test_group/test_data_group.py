import unittest
import pandas as pd
import os
import logging
from data_py.csv.group import data_group


class TestDataGroup(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50]
        })

    def test_valid_input(self):
        result = data_group(self.df, 'A')
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 5)

    def test_invalid_input_none_df(self):
        with self.assertRaises(ValueError):
            data_group(None, 'A')

    def test_invalid_input_none_group_column(self):
        with self.assertRaises(ValueError):
            data_group(self.df, None)

    def test_is_save_true_output_dir_specified(self):
        output_dir = 'test_output'
        result = data_group(self.df, 'A', is_save=True, output_dir=output_dir)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 5)
        self.assertTrue(os.path.exists(output_dir))
        self.assertTrue(os.path.exists(os.path.join(output_dir, 'A_1.csv')))

    def test_is_save_true_default_output_dir(self):
        result = data_group(self.df, 'A', is_save=True)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 5)
        self.assertTrue(os.path.exists('A_1.csv'))

    def test_is_save_false(self):
        result = data_group(self.df, 'A', is_save=False)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 5)

    def test_non_existent_output_dir(self):
        output_dir = 'non_existent_dir'
        result = data_group(self.df, 'A', is_save=True, output_dir=output_dir)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 5)
        self.assertTrue(os.path.exists(output_dir))

    def test_group_column_not_in_df(self):
        with self.assertRaises(KeyError):
            data_group(self.df, 'C')

if __name__ == '__main__':
    unittest.main()