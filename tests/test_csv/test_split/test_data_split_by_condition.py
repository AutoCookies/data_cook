import unittest
import pandas as pd
import os
from data_cook import data_split_by_condition

class TestDataSplitByCondition(unittest.TestCase):

    def test_valid_input(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
        condition = pd.Series([True, False, True, False, True])
        df_true, df_false = data_split_by_condition(df, condition)
        self.assertEqual(len(df_true), 3)
        self.assertEqual(len(df_false), 2)

    def test_none_input_dataframe(self):
        with self.assertRaises(ValueError):
            data_split_by_condition(None, pd.Series([True, False, True, False, True]))

    def test_none_input_condition(self):
        with self.assertRaises(ValueError):
            data_split_by_condition(pd.DataFrame({'A': [1, 2, 3, 4, 5]}), None)

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            data_split_by_condition(pd.DataFrame({'A': [1, 2, 3, 4, 5]}), pd.Series([True, False, True]))

    def test_save_to_csv(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
        condition = pd.Series([True, False, True, False, True])
        output_dir = 'test_output'
        data_split_by_condition(df, condition, is_save=True, output_dir=output_dir)
        self.assertTrue(os.path.exists(os.path.join(output_dir, 'true_subset.csv')))
        self.assertTrue(os.path.exists(os.path.join(output_dir, 'false_subset.csv')))
        shutil.rmtree(output_dir)

if __name__ == '__main__':
    unittest.main()