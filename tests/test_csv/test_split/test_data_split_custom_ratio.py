import unittest
import pandas as pd
import numpy as np
import os
from data_py import data_split_custom_ratio

class TestDataSplitCustomRatio(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame
        self.df = pd.DataFrame({'A': range(100), 'B': range(100, 200)})
        self.output_dir = 'test_splits'

    def tearDown(self):
        # Cleanup generated files
        if os.path.exists(self.output_dir):
            for file in os.listdir(self.output_dir):
                os.remove(os.path.join(self.output_dir, file))
            os.rmdir(self.output_dir)
    
    def test_valid_splits(self):
        ratios = [0.6, 0.3, 0.1]
        splits = data_split_custom_ratio(self.df, ratios, random_state=42)
        expected_lengths = [60, 30, 10]
        
        self.assertEqual(len(splits), len(ratios))
        for split, expected_length in zip(splits, expected_lengths):
            self.assertEqual(len(split), expected_length)
    
    def test_invalid_ratios(self):
        with self.assertRaises(ValueError):
            data_split_custom_ratio(self.df, [0.5, 0.3, 0.3])  # Sum > 1
        with self.assertRaises(ValueError):
            data_split_custom_ratio(self.df, [0.2, 0.3])  # Sum < 1
    
    def test_saving_splits(self):
        ratios = [0.5, 0.5]
        data_split_custom_ratio(self.df, ratios, is_save=True, output_dir=self.output_dir, random_state=42)
        
        self.assertTrue(os.path.exists(self.output_dir))
        self.assertEqual(len(os.listdir(self.output_dir)), 2)
    
    def test_reproducibility(self):
        ratios = [0.7, 0.3]
        splits1 = data_split_custom_ratio(self.df, ratios, random_state=123)
        splits2 = data_split_custom_ratio(self.df, ratios, random_state=123)
        
        for df1, df2 in zip(splits1, splits2):
            pd.testing.assert_frame_equal(df1, df2)
    
    def test_no_random_state(self):
        ratios = [0.5, 0.5]
        splits1 = data_split_custom_ratio(self.df, ratios)
        splits2 = data_split_custom_ratio(self.df, ratios)
        
        # The results may be different due to randomness
        with self.assertRaises(AssertionError):
            pd.testing.assert_frame_equal(splits1[0], splits2[0])

if __name__ == '__main__':
    unittest.main()
