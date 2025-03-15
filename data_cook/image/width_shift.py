import os
import cv2
import numpy as np

def shift_image(image_path, shift, output_path):
    """D ch ảnh theo chi u ngang m t kho ng shift pixels.

    Parameters
    ----------
    image_path : str
        Đường dẫn tới ảnh cần d ch.
    shift : int
        Kho ng d ch theo chi u ngang.
    output_path : str
        Đường dẫn để lưu ảnh đã d ch.
    """
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Error: File not found: {image_path}")

        img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        if img is None:
            raise ValueError(f"Error: Could not read image: {image_path}")

        height, width = img.shape[:2]

        # Ma trận d ch ảnh
        M = np.array([[1, 0, shift], [0, 1, 0]], dtype=np.float32)

        # D ch ảnh
        shifted_img = cv2.warpAffine(img, M, (width, height), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)

        # Lưu ảnh đã d ch
        cv2.imwrite(output_path, shifted_img, [cv2.IMWRITE_PNG_COMPRESSION, 3])
        print(f"  i lưu ảnh đã d ch: {output_path}")

    except Exception as e:
        print(f"Error: {e}")


"""Function to shift all images in a folder horizontally by a specified amount and save them to the output folder.

Parameters
----------
input_folder : str
    Path to the folder containing images to be shifted.
shift : int
    The number of pixels to shift the images horizontally.
output_folder : str
    Path to the folder where the shifted images will be saved.

Returns
-------
None
"""

def shift_images_in_folder(input_folder, shift, output_folder):
    """Shift all images in the input folder horizontally by a specified amount and save them to the output folder.

    Parameters
    ----------
    input_folder : str
        Path to the folder containing images to be shifted.
    shift : int
        The number of pixels to shift the images horizontally.
    output_folder : str
        Path to the folder where the shifted images will be saved.
    """
    # Create the output directory if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over each file in the input directory using os.scandir
    for entry in os.scandir(input_folder):
        if not entry.is_file() or not entry.name.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue
        
        input_path = entry.path
        output_path = os.path.join(output_folder, f"shifted_{entry.name}")
        # Shift the image and save the result
        shift_image(input_path, shift, output_path)
