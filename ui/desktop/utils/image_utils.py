from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

def load_image(file_path, notebook):
    """ Mở file hình ảnh và hiển thị trong một tab """
    # Tạo một frame mới cho hình ảnh
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=file_path.split("/")[-1])  # Thêm tab với tên file

    # Đọc hình ảnh
    image = Image.open(file_path)
    image.thumbnail((800, 600))  # Giảm kích thước hình ảnh nếu quá lớn
    photo = ImageTk.PhotoImage(image)

    # Hiển thị hình ảnh
    label = tk.Label(frame, image=photo)
    label.image = photo  # Giữ tham chiếu để tránh bị thu hồi bộ nhớ
    label.pack(fill="both", expand=True)

    # 🔹 Thêm nút phóng to/thu nhỏ
    zoom_frame = ttk.Frame(frame)
    zoom_frame.pack(side="top", fill="x")

    zoom_in_button = ttk.Button(zoom_frame, text="Zoom In", command=lambda: zoom_image(label, image, 1.2))
    zoom_in_button.pack(side="left", padx=5, pady=5)

    zoom_out_button = ttk.Button(zoom_frame, text="Zoom Out", command=lambda: zoom_image(label, image, 0.8))
    zoom_out_button.pack(side="left", padx=5, pady=5)

def zoom_image(label, original_image, scale_factor):
    """ Phóng to/thu nhỏ hình ảnh """
    width, height = original_image.size
    new_size = (int(width * scale_factor), int(height * scale_factor))
    resized_image = original_image.resize(new_size, Image.Resampling.LANCZOS)  # Sửa ở đây
    photo = ImageTk.PhotoImage(resized_image)
    label.config(image=photo)
    label.image = photo  # Giữ tham chiếu