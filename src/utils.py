import cv2
import numpy as np

def cartoonize_image(img,
                     bilateral_repeats=5,
                     blur_ksize=5,
                     edge_block_size=9,
                     edge_C=5):

    # Convert to gray + smooth
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, blur_ksize)

    # Detect edges
    edges = cv2.adaptiveThreshold(
        gray_blur, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        edge_block_size, edge_C
    )

    # Smooth colors repeatedly for a cartoon look
    color = img
    for _ in range(bilateral_repeats):
        color = cv2.bilateralFilter(color, 9, 75, 75)

    edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Combine -> Cartoon effect
    cartoon = cv2.bitwise_and(color, edges_colored)
    return cartoon
