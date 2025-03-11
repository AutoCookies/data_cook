import cv2
import os

def flip_image(image_path, output_path, flip_code):
    """
    Lật một hình ảnh và lưu kết quả.

    Args:
        image_path (str): Đường dẫn đến hình ảnh đầu vào.
        output_path (str): Đường dẫn để lưu hình ảnh đã lật.
        flip_code (int): Mã lật hình ảnh:
            - 0: Lật theo chiều dọc (vertical flip).
            - 1: Lật theo chiều ngang (horizontal flip).
            - -1: Lật cả chiều dọc và ngang.
    """
    try:
        # Đọc hình ảnh
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Không thể đọc hình ảnh từ đường dẫn đã cung cấp.")

        # Lật hình ảnh
        flipped_image = cv2.flip(image, flip_code)

        # Lưu hình ảnh đã lật
        cv2.imwrite(output_path, flipped_image)
        print(f"Hình ảnh đã lật được lưu tại: {output_path}")

    except Exception as e:
        print(f"Lỗi khi lật hình ảnh: {e}")
        

def flip_images_in_folder(input_folder, output_folder, flip_code):
    """
    Lật tất cả hình ảnh trong một thư mục và lưu kết quả vào thư mục đầu ra.

    Args:
        input_folder (str): Đường dẫn đến thư mục chứa hình ảnh đầu vào.
        output_folder (str): Đường dẫn đến thư mục để lưu hình ảnh đã lật.
        flip_code (int): Mã lật hình ảnh:
            - 0: Lật theo chiều dọc (vertical flip).
            - 1: Lật theo chiều ngang (horizontal flip).
            - -1: Lật cả chiều dọc và ngang.
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

                # Lật hình ảnh
                flip_image(image_path, output_path, flip_code)

        print(f"Đã lật tất cả hình ảnh trong thư mục: {input_folder}")

    except Exception as e:
        print(f"Lỗi khi lật hình ảnh trong thư mục: {e}")