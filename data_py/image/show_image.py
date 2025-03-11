import cv2
import os

def show_image(image, title="Image"):
    """Hiển thị ảnh với OpenCV."""
    if image is not None:
        cv2.imshow(title, image)
        cv2.waitKey(0)  # Đợi nhấn phím bất kỳ để đóng cửa sổ
        cv2.destroyAllWindows()
    else:
        print("Ảnh không hợp lệ!")

def show_num_of_images (folder_path):
    try:
        for image in os.listdir(folder_path):
            show_image(cv2.imread(os.path.join(folder_path, image)))
    except:
        print("Không tìm thấy ảnh trong folder")
            