import cv2
import os

def blur_image(image_path, output_path, kernel_size=(5, 5)):
    """
    Làm mờ một hình ảnh và lưu kết quả.

    Args:
        image_path (str): Đường dẫn đến hình ảnh đầu vào.
        output_path (str): Đường dẫn để lưu hình ảnh đã làm mờ.
        kernel_size (tuple): Kích thước của kernel Gaussian Blur. Mặc định là (5, 5).
    """
    try:
        # Đọc hình ảnh
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Không thể đọc hình ảnh từ đường dẫn đã cung cấp.")

        # Áp dụng Gaussian Blur
        blurred_image = cv2.GaussianBlur(image, kernel_size, 0)

        # Lưu hình ảnh đã làm mờ
        cv2.imwrite(output_path, blurred_image)
        print(f"Hình ảnh đã làm mờ được lưu tại: {output_path}")

    except Exception as e:
        print(f"Lỗi khi làm mờ hình ảnh: {e}")

def blur_images_in_folder(input_folder, output_folder, kernel_size=(5, 5)):
    """
    Làm mờ tất cả hình ảnh trong một thư mục và lưu kết quả vào thư mục đầu ra.

    Args:
        input_folder (str): Đường dẫn đến thư mục chứa hình ảnh đầu vào.
        output_folder (str): Đường dẫn đến thư mục để lưu hình ảnh đã làm mờ.
        kernel_size (tuple): Kích thước của kernel Gaussian Blur. Mặc định là (5, 5).
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

                # Làm mờ hình ảnh
                blur_image(image_path, output_path, kernel_size)

        print(f"Đã làm mờ tất cả hình ảnh trong thư mục: {input_folder}")

    except Exception as e:
        print(f"Lỗi khi làm mờ hình ảnh trong thư mục: {e}")