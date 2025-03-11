import cv2
import os

def grayscale_image(image_path, output_path):
    """
    Chuyển đổi một hình ảnh sang grayscale và lưu kết quả.

    Args:
        image_path (str): Đường dẫn đến hình ảnh đầu vào.
        output_path (str): Đường dẫn để lưu hình ảnh đã chuyển đổi.
    """
    try:
        # Đọc hình ảnh
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Không thể đọc hình ảnh từ đường dẫn đã cung cấp.")

        # Chuyển đổi sang grayscale
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Lưu hình ảnh đã chuyển đổi
        cv2.imwrite(output_path, grayscale_image)
        print(f"Hình ảnh grayscale được lưu tại: {output_path}")

    except Exception as e:
        print(f"Lỗi khi chuyển đổi hình ảnh sang grayscale: {e}")


def grayscale_images_in_folder(input_folder, output_folder):
    """
    Chuyển đổi tất cả hình ảnh trong một thư mục sang grayscale và lưu kết quả vào thư mục đầu ra.

    Args:
        input_folder (str): Đường dẫn đến thư mục chứa hình ảnh đầu vào.
        output_folder (str): Đường dẫn đến thư mục để lưu hình ảnh đã chuyển đổi.
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

                # Chuyển đổi hình ảnh sang grayscale
                grayscale_image(image_path, output_path)

        print(f"Đã chuyển đổi tất cả hình ảnh trong thư mục: {input_folder}")

    except Exception as e:
        print(f"Lỗi khi chuyển đổi hình ảnh trong thư mục: {e}")