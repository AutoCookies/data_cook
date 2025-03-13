import unittest
import os
import cv2
from data_py.video.key_frame_extract import extract_key_frames

class TestExtractKeyFrames(unittest.TestCase):
    def setUp(self):
        self.video_path = 'test_video.mp4'
        self.output_path = 'test_output'
        self.diff_threshold = 0.05

    def test_output_directory_creation(self):
        if os.path.exists(self.output_path):
            os.rmdir(self.output_path)
        extract_key_frames(self.video_path, self.output_path, self.diff_threshold)
        self.assertTrue(os.path.exists(self.output_path))

    def test_video_file_readability(self):
        cap = cv2.VideoCapture(self.video_path)
        success, _ = cap.read()
        cap.release()
        self.assertTrue(success)

    def test_keyframe_extraction(self):
        extract_key_frames(self.video_path, self.output_path, self.diff_threshold)
        keyframes = os.listdir(self.output_path)
        self.assertGreater(len(keyframes), 0)

    def test_diff_threshold(self):
        extract_key_frames(self.video_path, self.output_path, 0.1)
        keyframes = os.listdir(self.output_path)
        self.assertGreater(len(keyframes), 0)

    def test_unreadable_video_file(self):
        with self.assertRaises(Exception):
            extract_key_frames('non_existent_video.mp4', self.output_path, self.diff_threshold)

    def test_output_path_not_directory(self):
        with self.assertRaises(Exception):
            extract_key_frames(self.video_path, 'non_existent_file.txt', self.diff_threshold)

if __name__ == '__main__':
    unittest.main()