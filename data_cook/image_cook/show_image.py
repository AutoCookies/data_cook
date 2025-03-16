import cv2
import os

def display_image(image, window_title="Image"):
    """Display an image using OpenCV.

    Args:
        image: The image to display.
        window_title (str): The title of the window displaying the image.
    """
    if image is not None:
        cv2.imshow(window_title, image)
        cv2.waitKey(0)  # Wait for a key press to close the window
        cv2.destroyAllWindows()
    else:
        print("Invalid image!")

def show_number_of_images(folder_path):
    """Hiển thị s  ảnh trong một thư mục.
    
    Hiển thị s  ảnh trong thư mục `folder_path`.
    Nếu thư mục tr ng, sẽ in ra thông báo lỗi.
    """
    try:
        for image in os.listdir(folder_path):
            image_path = os.path.join(folder_path, image)
            show_image(cv2.imread(image_path), image)
    except FileNotFoundError:
        print(f"Không tìm thấy ảnh trong thư mục: {folder_path}")
            