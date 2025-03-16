import unittest
import pandas as pd
import os
from data_cook import data_split_by_distribution

class TestDataSplitByDistribution(unittest.TestCase):
    def test_default_split(self):
        # Create a sample dataframe
        df = pd.DataFrame({
            'target': [0, 0, 0, 1, 1, 1],
            'feature': [1, 2, 3, 4, 5, 6]
        })

        # Split the dataframe
        train, test = data_split_by_distribution(df, 'target')

        # Check the lengths of the splits
        self.assertEqual(len(train), 4)
        self.assertEqual(len(test), 2)

    def test_custom_split(self):
        # Create a sample dataframe
        df = pd.DataFrame({
            'target': [0, 0, 0, 1, 1, 1],
            'feature': [1, 2, 3, 4, 5, 6]
        })

        # Split the dataframe with custom train and test sizes
        train, test = data_split_by_distribution(df, 'target', train_size=0.5, test_size=0.5)

        # Check the lengths of the splits
        self.assertEqual(len(train), 3)
        self.assertEqual(len(test), 3)

    def test_split_with_validation(self):
        # Create a sample dataframe
        df = pd.DataFrame({
            'target': [0, 0, 0, 1, 1, 1],
            'feature': [1, 2, 3, 4, 5, 6]
        })

        # Split the dataframe with validation set
        train, test, validation = data_split_by_distribution(df, 'target', validation_size=0.2)

        # Check the lengths of the splits
        self.assertEqual(len(train), 4)
        self.assertEqual(len(test), 1)
        self.assertEqual(len(validation), 1)

    def test_split_with_random_state(self):
        # Create a sample dataframe
        df = pd.DataFrame({
            'target': [0, 0, 0, 1, 1, 1],
            'feature': [1, 2, 3, 4, 5, 6]
        })

        # Split the dataframe with random state
        train1, test1 = data_split_by_distribution(df, 'target', random_state=42)
        train2, test2 = data_split_by_distribution(df, 'target', random_state=42)

        # Check that the splits are the same
        self.assertTrue(train1.equals(train2))
        self.assertTrue(test1.equals(test2))

    def test_split_with_saving_to_csv(self):
        # Create a sample dataframe
        df = pd.DataFrame({
            'target': [0, 0, 0, 1, 1, 1],
            'feature': [1, 2, 3, 4, 5, 6]
        })

        # Split the dataframe and save to CSV
        output_dir = 'test_output'
        data_split_by_distribution(df, 'target', is_save=True, output_dir=output_dir)

        # Check that the files exist
        self.assertTrue(os.path.exists(os.path.join(output_dir, 'train.csv')))
        self.assertTrue(os.path.exists(os.path.join(output_dir, 'test.csv')))

    def test_invalid_input(self):
        # Create a sample dataframe
        df = pd.DataFrame({
            'target': [0, 0, 0, 1, 1, 1],
            'feature': [1, 2, 3, 4, 5, 6]
        })

        # Test invalid target column
        with self.assertRaises(KeyError):
            data_split_by_distribution(df, 'invalid_column')

        # Test invalid train/test sizes
        with self.assertRaises(ValueError):
            data_split_by_distribution(df, 'target', train_size=1.1)

if __name__ == '__main__':
    unittest.main()