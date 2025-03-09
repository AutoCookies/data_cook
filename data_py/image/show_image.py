import cv2

def show_image(image, title="Image"):
    """Hiển thị ảnh với OpenCV."""
    if image is not None:
        cv2.imshow(title, image)
        cv2.waitKey(0)  # Đợi nhấn phím bất kỳ để đóng cửa sổ
        cv2.destroyAllWindows()
    else:
        print("Ảnh không hợp lệ!")
