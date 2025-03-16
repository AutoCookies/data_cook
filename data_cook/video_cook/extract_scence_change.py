import cv2
import os
import numpy as np

def extract_scene_changes(video_path, output_path, threshold=30.0):
    """
    Trích xuất frame khi có sự thay đổi lớn trong nội dung video.

    Args:
        video_path (str): Đường dẫn video đầu vào.
        output_path (str): Thư mục lưu frame.
        threshold (float): Ngưỡng SSIM để phát hiện sự thay đổi.
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    cap = cv2.VideoCapture(video_path)
    success, prev_frame = cap.read()
    frame_id = 0

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # Chuyển đổi ảnh về grayscale để so sánh
        gray_prev = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
        gray_curr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Tính sự khác biệt giữa 2 frame
        diff = cv2.absdiff(gray_prev, gray_curr)
        score = np.mean(diff)

        if score > threshold:  # Nếu sự khác biệt lớn hơn ngưỡng, lưu frame
            frame_filename = os.path.join(output_path, f"scene_{frame_id:05d}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f"Đã lưu: {frame_filename}")
            frame_id += 1
        
        prev_frame = frame  # Cập nhật frame trước đó

    cap.release()
    print(f"Hoàn thành tách frame theo cảnh từ {video_path}!")