import unittest
import pandas as pd
import os
import shutil
from data_py import data_split

class TestDataSplit(unittest.TestCase):

    def setUp(self):
        """Tạo dataset giả lập."""
        self.df = pd.DataFrame({'value': range(100)})  # 100 dòng

    def test_valid_split_proportions(self):
        """Kiểm tra tỷ lệ train/test đúng không."""
        train, test = data_split(self.df, train_size=0.7, test_size=0.3)
        self.assertEqual(len(train) + len(test), len(self.df))  # Tổng không đổi
        self.assertAlmostEqual(len(train) / len(self.df), 0.7, places=1)
        self.assertAlmostEqual(len(test) / len(self.df), 0.3, places=1)

    def test_valid_split_with_validation(self):
        """Kiểm tra tỷ lệ train/test/validation đúng không."""
        train, test, val = data_split(self.df, train_size=0.6, test_size=0.3, validation_size=0.1)
        self.assertEqual(len(train) + len(test) + len(val), len(self.df))  # Tổng không đổi
        self.assertAlmostEqual(len(train) / len(self.df), 0.6, places=1)
        self.assertAlmostEqual(len(test) / len(self.df), 0.3, places=1)
        self.assertAlmostEqual(len(val) / len(self.df), 0.1, places=1)

    def test_invalid_split_proportions(self):
        """Kiểm tra lỗi khi tổng tỷ lệ lớn hơn 1."""
        with self.assertRaises(ValueError):
            data_split(self.df, train_size=0.7, test_size=0.3, validation_size=0.2)

    def test_save_to_csv(self):
        """Kiểm tra file có được tạo khi bật is_save=True."""
        output_dir = 'test_splits'
        os.makedirs(output_dir, exist_ok=True)
        train, test = data_split(self.df, train_size=0.7, test_size=0.3, is_save=True)

        self.assertTrue(os.path.exists('train.csv'))
        self.assertTrue(os.path.exists('test.csv'))

        os.remove('train.csv')
        os.remove('test.csv')

    def test_reproducibility(self):
        """Kiểm tra có giữ nguyên thứ tự sau nhiều lần chạy không."""
        train1, test1 = data_split(self.df, train_size=0.7, test_size=0.3)
        train2, test2 = data_split(self.df, train_size=0.7, test_size=0.3)

        pd.testing.assert_frame_equal(train1, train2)
        pd.testing.assert_frame_equal(test1, test2)

if __name__ == '__main__':
    unittest.main()
