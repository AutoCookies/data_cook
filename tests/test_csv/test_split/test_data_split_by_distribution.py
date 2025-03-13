import unittest
import pandas as pd
import numpy as np
from data_py.csv.split.data_split_by_distribution import data_split_by_distribution

class TestDataSplitByDistribution(unittest.TestCase):
    def test_default_sizes(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        train, test, _ = data_split_by_distribution(df, 'B')
        self.assertEqual(len(train), 3)
        self.assertEqual(len(test), 2)

    def test_custom_sizes(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        train, test, _ = data_split_by_distribution(df, 'B', train_size=0.6, test_size=0.4)
        self.assertEqual(len(train), 3)
        self.assertEqual(len(test), 2)

    def test_validation_set(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        train, test, validation = data_split_by_distribution(df, 'B', validation_size=0.2)
        self.assertEqual(len(train), 3)
        self.assertEqual(len(test), 1)
        self.assertEqual(len(validation), 1)

    def test_no_validation_set(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        train, test, _ = data_split_by_distribution(df, 'B', validation_size=None)
        self.assertEqual(len(train), 3)
        self.assertEqual(len(test), 2)

    def test_random_state(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        train1, test1, _ = data_split_by_distribution(df, 'B', random_state=42)
        train2, test2, _ = data_split_by_distribution(df, 'B', random_state=42)
        self.assertTrue(train1.equals(train2))
        self.assertTrue(test1.equals(test2))

    def test_save_to_csv(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        data_split_by_distribution(df, 'B', is_save=True, output_dir='test_output')
        self.assertTrue(os.path.exists('test_output/train.csv'))
        self.assertTrue(os.path.exists('test_output/test.csv'))

    def test_invalid_input(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 1, 2, 2, 3]})
        with self.assertRaises(KeyError):
            data_split_by_distribution(df, 'C', 'B')

if __name__ == '__main__':
    unittest.main()