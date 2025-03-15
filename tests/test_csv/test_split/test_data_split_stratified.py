import unittest
import pandas as pd
import os
import shutil
from collections import Counter
from data_py import data_split_stratified

class TestDataSplitStratified(unittest.TestCase):

    def setUp(self):
        """Tạo dataset giả lập với nhãn không cân bằng."""
        self.df = pd.DataFrame({
            'feature': range(100),
            'target': [0] * 50 + [1] * 30 + [2] * 20  # Lớp 0 nhiều hơn lớp 1, 2
        })

    def test_valid_split_proportions(self):
        """Kiểm tra tỷ lệ phân chia hợp lệ."""
        train, test = data_split_stratified(self.df, 'target', train_size=0.7, test_size=0.3, random_state=42)
        self.assertEqual(len(train) + len(test), len(self.df))
        self.assertAlmostEqual(len(train) / len(self.df), 0.7, places=1)
        self.assertAlmostEqual(len(test) / len(self.df), 0.3, places=1)

    def test_invalid_split_proportions(self):
        """Kiểm tra lỗi khi tổng tỷ lệ khác 1."""
        with self.assertRaises(ValueError):
            data_split_stratified(self.df, 'target', train_size=0.6, test_size=0.3, validation_size=0.2)

    def test_stratified_sampling_preserved(self):
        """Kiểm tra phân bố nhãn giữa tập train/test giống ban đầu."""
        train, test = data_split_stratified(self.df, 'target', train_size=0.7, test_size=0.3, random_state=42)
        
        orig_counts = Counter(self.df['target'])
        train_counts = Counter(train['target'])
        test_counts = Counter(test['target'])

        for label in orig_counts.keys():
            orig_ratio = orig_counts[label] / len(self.df)
            train_ratio = train_counts[label] / len(train)
            test_ratio = test_counts[label] / len(test)

            self.assertAlmostEqual(orig_ratio, train_ratio, places=1)
            self.assertAlmostEqual(orig_ratio, test_ratio, places=1)

    def test_save_to_csv(self):
        """Kiểm tra file được tạo khi bật is_save=True."""
        output_dir = 'test_splits'
        os.makedirs(output_dir, exist_ok=True)

        train, test = data_split_stratified(self.df, 'target', train_size=0.7, test_size=0.3, is_save=True, output_dir=output_dir)

        self.assertTrue(os.path.exists(os.path.join(output_dir, 'train.csv')))
        self.assertTrue(os.path.exists(os.path.join(output_dir, 'test.csv')))

        shutil.rmtree(output_dir)  # Xóa thư mục sau khi test

    def test_reproducibility_with_seed(self):
        """Kiểm tra nếu random_state giống nhau thì kết quả giống nhau."""
        train1, test1 = data_split_stratified(self.df, 'target', train_size=0.7, test_size=0.3, random_state=42)
        train2, test2 = data_split_stratified(self.df, 'target', train_size=0.7, test_size=0.3, random_state=42)

        pd.testing.assert_frame_equal(train1, train2)
        pd.testing.assert_frame_equal(test1, test2)

if __name__ == '__main__':
    unittest.main()
