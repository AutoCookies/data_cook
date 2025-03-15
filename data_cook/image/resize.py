import cv2
import os

def resize_image(image_path, output_path, width, height):
    """
    Thay đổi kích thước hình ảnh và lưu kết quả.

    Args:
        image_path (str): Đường dẫn đến hình ảnh đầu vào.
        output_path (str): Đường dẫn để lưu hình ảnh đã thay đổi kích thước.
        width (int): Chiều rộng mới.
        height (int): Chiều cao mới.
    """
    try:
        # Đọc hình ảnh
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Không thể đọc hình ảnh từ đường dẫn đã cung cấp.")

        # Thay đổi kích thước
        resized_image = cv2.resize(image, (width, height))

        # Lưu hình ảnh đã thay đổi kích thước
        cv2.imwrite(output_path, resized_image)
        print(f"Hình ảnh đã thay đổi kích thước được lưu tại: {output_path}")

    except Exception as e:
        print(f"Lỗi khi thay đổi kích thước hình ảnh: {e}")

def resize_images_in_folder(input_folder, output_folder, width, height):
    """
    Thay đổi kích thước tất cả hình ảnh trong một thư mục và lưu kết quả vào thư mục đầu ra.

    Args:
        input_folder (str): Đường dẫn đến thư mục chứa hình ảnh đầu vào.
        output_folder (str): Đường dẫn đến thư mục để lưu hình ảnh đã thay đổi kích thước.
        width (int): Chiều rộng mới.
        height (int): Chiều cao mới.
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

                # Đọc hình ảnh
                image = cv2.imread(image_path)
                if image is None:
                    print(f"Không thể đọc hình ảnh: {filename}")
                    continue

                # Thay đổi kích thước hình ảnh
                resized_image = cv2.resize(image, (width, height))

                # Lưu hình ảnh đã thay đổi kích thước
                cv2.imwrite(output_path, resized_image)
                print(f"Đã thay đổi kích thước và lưu: {output_path}")

        print(f"Đã thay đổi kích thước tất cả hình ảnh trong thư mục: {input_folder}")

    except Exception as e:
        print(f"Lỗi khi thay đổi kích thước hình ảnh trong thư mục: {e}")