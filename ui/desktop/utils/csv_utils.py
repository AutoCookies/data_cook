import pandas as pd
import tkinter as tk
from tkinter import ttk

def load_csv(file_path, notebook):
    """ Mở file CSV và hiển thị nội dung trong một tab """
    df = pd.read_csv(file_path)

    # Tạo một frame mới cho file CSV
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=file_path.split("/")[-1])  # Thêm tab với tên file

    # 🔹 Canvas để cuộn nội dung
    canvas = tk.Canvas(frame, bg="white")
    scroll_x = ttk.Scrollbar(frame, orient="horizontal", command=canvas.xview)
    scroll_y = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    canvas.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

    scroll_x.pack(side="bottom", fill="x")
    scroll_y.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # 🔹 Frame chứa dữ liệu (đặt trong Canvas)
    inner_frame = tk.Frame(canvas, bg="white")
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    # 🔹 Gán sự kiện cuộn chuột mượt hơn
    canvas.bind("<Configure>", lambda e, canvas=canvas: canvas.config(scrollregion=canvas.bbox("all")))

    # Hiển thị tiêu đề cột
    for col_idx, col_name in enumerate(df.columns):
        label = tk.Label(inner_frame, text=col_name, font=("Arial", 10, "bold"), bg="#D5DBDB", relief="ridge", padx=5, pady=3)
        label.grid(row=0, column=col_idx, sticky="nsew")

    # Hiển thị dữ liệu
    for row_idx, row in df.iterrows():
        for col_idx, value in enumerate(row):
            cell = tk.Label(inner_frame, text=value, font=("Arial", 10), bg="white", relief="ridge", padx=5, pady=3)
            cell.grid(row=row_idx + 1, column=col_idx, sticky="nsew")

    # Cập nhật kích thước scroll region
    inner_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # 🔹 Thêm nút phóng to/thu nhỏ
    zoom_frame = ttk.Frame(frame)
    zoom_frame.pack(side="top", fill="x")

    zoom_in_button = ttk.Button(zoom_frame, text="Zoom In", command=lambda: zoom_csv(inner_frame, 1.2))
    zoom_in_button.pack(side="left", padx=5, pady=5)

    zoom_out_button = ttk.Button(zoom_frame, text="Zoom Out", command=lambda: zoom_csv(inner_frame, 0.8))
    zoom_out_button.pack(side="left", padx=5, pady=5)

    return df

def zoom_csv(inner_frame, scale_factor):
    """ Phóng to/thu nhỏ bảng CSV """
    for widget in inner_frame.winfo_children():
        current_font = widget.cget("font")
        font_size = int(current_font.split(" ")[1])  # Lấy kích thước font hiện tại
        new_font_size = max(8, int(font_size * scale_factor))  # Giới hạn kích thước tối thiểu
        widget.config(font=("Arial", new_font_size))