import os
import cv2
import numpy as np

def adjust_brightness(image, brightness_factor):
    """
    Điều chỉnh độ sáng của ảnh.

    Args:
        image (numpy.ndarray): Ảnh đầu vào.
        brightness_factor (float): Hệ số điều chỉnh độ sáng ( >1: sáng hơn, <1: tối hơn).

    Returns:
        numpy.ndarray: Ảnh sau khi điều chỉnh độ sáng.
    """
    # Chuyển ảnh sang kiểu float để tránh lỗi tràn giá trị
    bright_image = np.clip(image * brightness_factor, 0, 255).astype(np.uint8)
    return bright_image

def adjust_brightness_folder(input_folder, output_folder, brightness_factor):
    """
    Điều chỉnh độ sáng của tất cả ảnh trong thư mục.

    Args:
        input_folder (str): Đường dẫn thư mục chứa ảnh đầu vào.
        output_folder (str): Đường dẫn thư mục lưu ảnh đã xử lý.
        brightness_factor (float): Hệ số điều chỉnh độ sáng ( >1: sáng hơn, <1: tối hơn).
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_folder, filename)
            image = cv2.imread(img_path)
            if image is None:
                print(f"Lỗi: Không thể đọc ảnh {filename}")
                continue

            bright_image = adjust_brightness(image, brightness_factor)

            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, bright_image)
            print(f"Đã lưu: {output_path}")