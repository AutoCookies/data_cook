import cv2
import os

def read_image(file_path):
    """Đọc một ảnh từ file."""
    image = cv2.imread(file_path)
    if image is None:
        print(f"Không thể đọc ảnh từ {file_path}")
    else:
        print(f"Đã đọc ảnh: {file_path} - Kích thước: {image.shape}")
    return image

def read_images_from_folder(folder_path):
    """Read all images in a folder."""
    images = {}
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} did not existe!")
        return images

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp')):
            image = cv2.imread(file_path)
            if image is not None:
                images[filename] = image
                print(f"Image read: {filename} - Size: {image.shape}")
            else:
                print(f"Error reading image: {filename}")
    
    return images
