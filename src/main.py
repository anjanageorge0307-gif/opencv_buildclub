import cv2
import os
from utils import cartoonize_image   # 👈 use the function from utils.py


def main():
    print("[INFO] Running Cartoonizer Project...")

    # Figure out paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)
    assets_dir = os.path.join(root_dir, "assets")
    results_dir = os.path.join(root_dir, "results")

    # Input + output paths
    input_path = os.path.join(assets_dir, "sample.png")   # your umbrella image
    output_path = os.path.join(results_dir, "cartoon_output.png")

    # Check if image exists
    if not os.path.exists(input_path):
        print("[ERROR] sample.png not found in assets folder:", input_path)
        return

    # Read image
    img = cv2.imread(input_path)
    if img is None:
        print("[ERROR] Failed to load image with cv2.imread")
        return

    # ---- Apply cartoon effect ----
    cartoon = cartoonize_image(img)

    # Make sure results/ exists
    os.makedirs(results_dir, exist_ok=True)

    # Save cartoon
    cv2.imwrite(output_path, cartoon)
    print("[INFO] Cartoon image saved at:", output_path)

    # Show both images
    cv2.imshow("Original", img)
    cv2.imshow("Cartoon", cartoon)

    print("[INFO] Press any key in an image window to close.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
