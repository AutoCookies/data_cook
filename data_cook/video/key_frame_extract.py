import cv2
import os
import numpy as np
from skimage.metrics import structural_similarity as ssim

def extract_key_frames(video_path, output_path, diff_threshold=0.05):
    """
    Tách frame từ video, chỉ lưu frame có sự thay đổi lớn so với frame trước đó.

    Args:
        video_path (str): Đường dẫn video đầu vào.
        output_path (str): Thư mục lưu frame.
        diff_threshold (float): Ngưỡng khác biệt SSIM để lưu frame (0.0 - 1.0).
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    cap = cv2.VideoCapture(video_path)
    success, prev_frame = cap.read()
    if not success:
        print("Không thể đọc video!")
        return

    prev_frame_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    frame_id = 0

    while True:
        success, frame = cap.read()
        if not success:
            break

        # Chuyển frame hiện tại sang ảnh xám để so sánh
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Tính mức độ giống nhau giữa 2 frame liên tiếp
        similarity = ssim(prev_frame_gray, frame_gray)

        if similarity < (1 - diff_threshold):  # Nếu khác biệt lớn hơn ngưỡng
            frame_filename = os.path.join(output_path, f"keyframe_{frame_id:05d}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f"Đã lưu: {frame_filename}")

            prev_frame_gray = frame_gray  # Cập nhật frame trước đó
            frame_id += 1

    cap.release()
    print(f"Hoàn thành tách keyframes từ {video_path}!")