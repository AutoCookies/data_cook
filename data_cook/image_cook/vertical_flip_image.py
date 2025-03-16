import cv2
import os

def vertical_flip(image):
    """
    Lật ảnh theo chiều dọc.

    Args:
        image (numpy.ndarray): Ảnh đầu vào.

    Returns:
        numpy.ndarray: Ảnh đã lật.
    """
    return cv2.flip(image, 0)  # `flip_code = 0` lật dọc

def vertical_flip_folder(input_folder, output_folder):
    """
    Lật ảnh theo chiều dọc trong thư mục và lưu lại.

    Args:
        input_folder (str): Thư mục chứa ảnh đầu vào.
        output_folder (str): Thư mục lưu ảnh đã lật.
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

            flipped_image = vertical_flip(image)

            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, flipped_image)
            print(f"Đã lưu: {output_path}")