import unittest
import pandas as pd
import os
from data_py.csv.split.data_split_cross_validation import generate_cross_validation_folds

class TestGenerateCrossValidationFolds(unittest.TestCase):

    def test_none_dataframe(self):
        with self.assertRaises(ValueError):
            generate_cross_validation_folds(None)

    def test_invalid_dataframe(self):
        with self.assertRaises(ValueError):
            generate_cross_validation_folds("invalid")

    def test_invalid_num_folds(self):
        with self.assertRaises(ValueError):
            generate_cross_validation_folds(pd.DataFrame(), num_folds=1)

    def test_non_integer_num_folds(self):
        with self.assertRaises(ValueError):
            generate_cross_validation_folds(pd.DataFrame(), num_folds=3.5)

    def test_invalid_output_directory(self):
        with self.assertRaises(ValueError):
            generate_cross_validation_folds(pd.DataFrame(), save_to_disk=True, output_directory=123)

    def test_correct_number_of_folds(self):
        dataframe = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
        folds = generate_cross_validation_folds(dataframe, num_folds=3)
        self.assertEqual(len(folds), 3)

    def test_save_to_disk(self):
        dataframe = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
        output_directory = 'test_output'
        generate_cross_validation_folds(dataframe, save_to_disk=True, output_directory=output_directory)
        self.assertTrue(os.path.exists(output_directory))
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'train_fold_1.csv')))
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'test_fold_1.csv')))
        os.rmdir(output_directory)

    def test_dont_save_to_disk(self):
        dataframe = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
        output_directory = 'test_output'
        generate_cross_validation_folds(dataframe, save_to_disk=False, output_directory=output_directory)
        self.assertFalse(os.path.exists(output_directory))

if __name__ == '__main__':
    unittest.main()