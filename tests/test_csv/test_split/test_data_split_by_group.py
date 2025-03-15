import unittest
import pandas as pd
import numpy as np
import os

class TestDataSplitByGroup(unittest.TestCase):
    def test_default_split_proportions(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        train, test = data_split_by_group(df, 'B')
        self.assertEqual(len(train), 3)
        self.assertEqual(len(test), 2)

    def test_custom_split_proportions(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        train, test = data_split_by_group(df, 'B', train_size=0.6, test_size=0.4)
        self.assertEqual(len(train), 3)
        self.assertEqual(len(test), 2)

    def test_validation_set(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        train, test, validation = data_split_by_group(df, 'B', validation_size=0.2)
        self.assertEqual(len(train), 3)
        self.assertEqual(len(test), 1)
        self.assertEqual(len(validation), 1)

    def test_no_validation_set(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        train, test = data_split_by_group(df, 'B')
        self.assertEqual(len(train), 3)
        self.assertEqual(len(test), 2)

    def test_random_state(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        train1, test1 = data_split_by_group(df, 'B', random_state=42)
        train2, test2 = data_split_by_group(df, 'B', random_state=42)
        self.assertTrue(train1.equals(train2))
        self.assertTrue(test1.equals(test2))

    def test_save_to_csv(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        data_split_by_group(df, 'B', is_save=True, output_dir='test_output')
        self.assertTrue(os.path.exists('test_output/train.csv'))
        self.assertTrue(os.path.exists('test_output/test.csv'))
        os.rmdir('test_output')

    def test_invalid_input_none_dataframe(self):
        with self.assertRaises(ValueError):
            data_split_by_group(None, 'B')

    def test_invalid_input_invalid_group_column(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
        with self.assertRaises(KeyError):
            data_split_by_group(df, 'B')

    def test_invalid_input_invalid_split_proportions(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        with self.assertRaises(ValueError):
            data_split_by_group(df, 'B', train_size=1.1, test_size=0.4)

if __name__ == '__main__':
    unittest.main()