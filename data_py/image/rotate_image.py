import cv2
import numpy as np
import os
import logging

def rotate_image(image, angle, center=None, scale=1.0):
    """Rotate an image by a given angle around a specified center and scale."""
    (h, w) = image.shape[:2]

    if center is None:
        center = (w / 2, h / 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    
    logging(f"Rotated image by {angle} degrees.")

    return rotated

def rotate_images_in_folder(folder_path, angle, center=None, scale=1.0):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        image = cv2.imread(file_path)
        rotated_image = rotate_image(image, angle, center, scale)
        cv2.imwrite(file_path, rotated_image)

    logging(f"Rotated {len(os.listdir(folder_path))} images in {folder_path} by {angle} degrees.")