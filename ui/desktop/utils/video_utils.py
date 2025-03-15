import cv2
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

def load_video(file_path, notebook, video_captures):
    """ Mở file video và hiển thị trong một tab """
    # Tạo một frame mới cho video
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=file_path.split("/")[-1])  # Thêm tab với tên file

    # Tạo label để hiển thị video
    video_label = tk.Label(frame)
    video_label.pack(fill="both", expand=True)

    # Mở video
    video_capture = cv2.VideoCapture(file_path)
    video_captures[file_path] = video_capture

    # 🔹 Thêm nút phóng to/thu nhỏ
    zoom_frame = ttk.Frame(frame)
    zoom_frame.pack(side="top", fill="x")

    zoom_in_button = ttk.Button(zoom_frame, text="Zoom In", command=lambda: set_zoom_factor(1.2))
    zoom_in_button.pack(side="left", padx=5, pady=5)

    zoom_out_button = ttk.Button(zoom_frame, text="Zoom Out", command=lambda: set_zoom_factor(0.8))
    zoom_out_button.pack(side="left", padx=5, pady=5)

    zoom_factor = 1.0  # Tỷ lệ phóng to/thu nhỏ

    def set_zoom_factor(factor):
        """ Cập nhật tỷ lệ phóng to/thu nhỏ """
        nonlocal zoom_factor
        zoom_factor *= factor

    def update_frame():
        """ Cập nhật khung hình video với tỷ lệ phóng to/thu nhỏ """
        ret, frame = video_capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame)
            width, height = image.size
            new_size = (int(width * zoom_factor), int(height * zoom_factor))
            resized_image = image.resize(new_size, Image.Resampling.LANCZOS)  # Sửa ở đây
            photo = ImageTk.PhotoImage(resized_image)
            video_label.config(image=photo)
            video_label.image = photo  # Giữ tham chiếu
        video_label.after(30, update_frame)  # Cập nhật khung hình sau mỗi 30ms

    update_frame()