import unittest
import pandas as pd
import os
import shutil
from data_py import data_split_time_series

class TestDataSplitTimeSeries(unittest.TestCase):

    def setUp(self):
        """Tạo dataset giả lập với cột thời gian."""
        self.df = pd.DataFrame({
            'date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
            'value': range(100)
        })

    def test_valid_split_proportions(self):
        """Kiểm tra tỷ lệ phân chia hợp lệ."""
        train, test = data_split_time_series(self.df, 'date', train_size=0.7, test_size=0.3)
        self.assertEqual(len(train) + len(test), len(self.df))
        self.assertAlmostEqual(len(train) / len(self.df), 0.7, places=1)
        self.assertAlmostEqual(len(test) / len(self.df), 0.3, places=1)

    def test_invalid_split_proportions(self):
        """Kiểm tra lỗi khi tổng tỷ lệ lớn hơn 1."""
        with self.assertRaises(ValueError):
            data_split_time_series(self.df, 'date', train_size=0.7, test_size=0.3, validation_size=0.2)

    def test_time_order_preserved(self):
        """Kiểm tra dữ liệu có thứ tự thời gian đúng không."""
        train, test = data_split_time_series(self.df, 'date', train_size=0.7, test_size=0.3)
        self.assertTrue(train['date'].max() < test['date'].min())  # Train phải có ngày nhỏ hơn test

    def test_save_to_csv(self):
        """Kiểm tra file có được tạo khi bật is_save=True."""
        output_dir = 'test_splits'
        os.makedirs(output_dir, exist_ok=True)

        train, test = data_split_time_series(self.df, 'date', train_size=0.7, test_size=0.3, is_save=True, output_dir=output_dir)

        self.assertTrue(os.path.exists(os.path.join(output_dir, 'train.csv')))
        self.assertTrue(os.path.exists(os.path.join(output_dir, 'test.csv')))

        shutil.rmtree(output_dir)  # Xóa thư mục sau khi test

    def test_reproducibility(self):
        """Kiểm tra có giữ nguyên thứ tự sau nhiều lần chạy không."""
        train1, test1 = data_split_time_series(self.df, 'date', train_size=0.7, test_size=0.3)
        train2, test2 = data_split_time_series(self.df, 'date', train_size=0.7, test_size=0.3)

        pd.testing.assert_frame_equal(train1, train2)
        pd.testing.assert_frame_equal(test1, test2)

if __name__ == '__main__':
    unittest.main()
