import os
import cv2

def horizontal_flip(image):
    """
    Lật ảnh theo chiều ngang.

    Args:
        image (numpy.ndarray): Ảnh đầu vào.

    Returns:
        numpy.ndarray: Ảnh sau khi lật ngang.
    """
    return cv2.flip(image, 1)

def horizontal_flip_folder(input_folder, output_folder):
    """
    Lật tất cả ảnh trong thư mục theo chiều ngang và lưu kết quả.

    Args:
        input_folder (str): Đường dẫn thư mục chứa ảnh đầu vào.
        output_folder (str): Đường dẫn thư mục lưu ảnh đã xử lý.
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

            flipped_image = horizontal_flip(image)

            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, flipped_image)
            print(f"Đã lưu: {output_path}")