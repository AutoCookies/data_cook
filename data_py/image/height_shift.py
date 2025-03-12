import os
import cv2
import numpy as np

def height_shift_image(image, shift):
    """
    Dịch chuyển ảnh theo chiều dọc (height shift).
    
    Args:
        image (numpy.ndarray): Ảnh đầu vào.
        shift (int): Số pixel dịch chuyển (+ lên, - xuống).

    Returns:
        numpy.ndarray: Ảnh đã dịch chuyển.
    """
    h, w = image.shape[:2]
    
    # Tạo ma trận dịch chuyển affine
    M = np.float32([[1, 0, 0], [0, 1, shift]])

    # Áp dụng phép biến đổi affine
    shifted_image = cv2.warpAffine(image, M, (w, h), borderMode=cv2.BORDER_REFLECT)
    
    return shifted_image

def height_shift_folder(input_folder, output_folder, shift):
    """
    Dịch chuyển toàn bộ ảnh trong thư mục theo chiều dọc.

    Args:
        input_folder (str): Đường dẫn thư mục chứa ảnh đầu vào.
        output_folder (str): Đường dẫn thư mục lưu ảnh đã xử lý.
        shift (int): Số pixel dịch chuyển (+ lên, - xuống).
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

            shifted_image = height_shift_image(image, shift)

            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, shifted_image)
            print(f"Đã lưu: {output_path}")