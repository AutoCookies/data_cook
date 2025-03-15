import cv2
import os
import logging

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def extract_frames(video_path, output_path, frame_rate=1):
    """
    Tách frame từ video và lưu vào thư mục output.

    Args:
        video_path (str): Đường dẫn video đầu vào.
        output_path (str): Thư mục lưu frame.
        frame_rate (int): Số frame trích xuất mỗi giây (mặc định = 1).
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        logging.error(f"Không thể mở video: {video_path}")
        return

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_interval = max(1, fps // frame_rate)  # Chia FPS để lấy frame đúng tỷ lệ

    logging.info(f"Đang tách frame từ {video_path} | FPS: {fps}, Tổng frame: {total_frames}, Lưu mỗi {frame_interval} frame")

    count = 0
    frame_id = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if count % frame_interval == 0:
            frame_filename = os.path.join(output_path, f"frame_{frame_id:05d}.jpg")
            cv2.imwrite(frame_filename, frame)
            logging.info(f"Đã lưu: {frame_filename}")
            frame_id += 1

        count += 1

    cap.release()
    logging.info(f"Hoàn thành tách frame từ {video_path}!")

def extract_frames_from_folder(input_folder, output_folder, frame_rate=1):
    """
    Tách frame từ tất cả video trong thư mục và lưu vào thư mục riêng cho từng video.

    Args:
        input_folder (str): Thư mục chứa video đầu vào.
        output_folder (str): Thư mục gốc để lưu frame.
        frame_rate (int): Số frame trích xuất mỗi giây.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    videos = [f for f in os.listdir(input_folder) if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]

    if not videos:
        logging.warning("Không tìm thấy video nào trong thư mục đầu vào!")
        return

    for filename in videos:
        video_path = os.path.join(input_folder, filename)
        video_name = os.path.splitext(filename)[0]  # Tên video không có đuôi mở rộng
        video_output_path = os.path.join(output_folder, video_name)  # Tạo thư mục riêng cho video

        logging.info(f"Bắt đầu xử lý video: {filename}")
        extract_frames(video_path, video_output_path, frame_rate)