import cv2
import os

def crop_image(image_path, output_path, x, y, width, height):
    """
    Cắt một hình ảnh và lưu kết quả.

    Args:
        image_path (str): Đường dẫn đến hình ảnh đầu vào.
        output_path (str): Đường dẫn để lưu hình ảnh đã cắt.
        x (int): Tọa độ x của điểm bắt đầu.
        y (int): Tọa độ y của điểm bắt đầu.
        width (int): Chiều rộng của vùng cắt.
        height (int): Chiều cao của vùng cắt.
    """
    try:
        # Đọc hình ảnh
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Không thể đọc hình ảnh từ đường dẫn đã cung cấp.")

        # Cắt hình ảnh
        cropped_image = image[y:y + height, x:x + width]

        # Lưu hình ảnh đã cắt
        cv2.imwrite(output_path, cropped_image)
        print(f"Hình ảnh đã cắt được lưu tại: {output_path}")

    except Exception as e:
        print(f"Lỗi khi cắt hình ảnh: {e}")

def crop_images_in_folder(input_folder, output_folder, x, y, width, height):
    """
    Cắt tất cả hình ảnh trong một thư mục và lưu kết quả vào thư mục đầu ra.

    Args:
        input_folder (str): Đường dẫn đến thư mục chứa hình ảnh đầu vào.
        output_folder (str): Đường dẫn đến thư mục để lưu hình ảnh đã cắt.
        x (int): Tọa độ x của điểm bắt đầu.
        y (int): Tọa độ y của điểm bắt đầu.
        width (int): Chiều rộng của vùng cắt.
        height (int): Chiều cao của vùng cắt.
    """
    try:
        # Tạo thư mục đầu ra nếu nó không tồn tại
        os.makedirs(output_folder, exist_ok=True)

        # Duyệt qua tất cả các tệp trong thư mục đầu vào
        for filename in os.listdir(input_folder):
            # Kiểm tra xem tệp có phải là hình ảnh không
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                # Đường dẫn đầy đủ đến hình ảnh đầu vào
                image_path = os.path.join(input_folder, filename)

                # Đường dẫn đầy đủ đến hình ảnh đầu ra
                output_path = os.path.join(output_folder, filename)

                # Cắt hình ảnh
                crop_image(image_path, output_path, x, y, width, height)

        print(f"Đã cắt tất cả hình ảnh trong thư mục: {input_folder}")

    except Exception as e:
        print(f"Lỗi khi cắt hình ảnh trong thư mục: {e}")