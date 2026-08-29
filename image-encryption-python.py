from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog
import os


def swap_pixel_channels(image_path, output_path):
    """
    Swaps the Red and Blue channel values of every pixel.
    """

    img = Image.open(image_path).convert("RGB")
    pixels = np.array(img)

    # Swap R and B channels
    swapped = pixels[:, :, [2, 1, 0]]

    result = Image.fromarray(swapped.astype("uint8"))
    result.save(output_path)

    print(f"✅ Channel-swapped image saved to: {output_path}")


def apply_math_operation(image_path, output_path, key, operation="add"):
    """
    Applies a mathematical operation to every pixel channel.
    Supported operations: add, subtract, multiply.
    """

    img = Image.open(image_path).convert("RGB")

    # Use int16 to avoid overflow during calculations
    pixels = np.array(img, dtype=np.int16)

    if operation == "add":
        result = (pixels + key) % 256

    elif operation == "subtract":
        result = (pixels - key) % 256

    elif operation == "multiply":
        result = (pixels * key) % 256

    else:
        raise ValueError(
            "Unsupported operation. Choose add, subtract, or multiply."
        )

    result_img = Image.fromarray(result.astype("uint8"))
    result_img.save(output_path)

    print(f"✅ {operation.capitalize()} operation applied.")
    print(f"   Key: {key}")
    print(f"   Saved to: {output_path}")


def select_image():
    """
    Opens a file browser and allows the user to select an image.
    """

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("Image Files", "*.jpg *.jpeg *.png *.bmp *.webp"),
            ("JPG Files", "*.jpg *.jpeg"),
            ("PNG Files", "*.png"),
            ("All Files", "*.*")
        ]
    )

    root.destroy()

    return file_path


if __name__ == "__main__":

    print("======================================")
    print("       IMAGE ENCRYPTION TOOL")
    print("======================================")

    # Open file selection window
    print("\n📂 Please select an image...")

    INPUT_IMG = select_image()

    # Check if user selected an image
    if not INPUT_IMG:
        print("❌ No image selected.")
        exit()

    print("\n✅ Image selected:")
    print(INPUT_IMG)

    # Get folder of original image
    image_folder = os.path.dirname(INPUT_IMG)

    # Output paths
    OUTPUT_SWAPPED = os.path.join(
        image_folder,
        "output_swapped.png"
    )

    OUTPUT_MATH = os.path.join(
        image_folder,
        "output_math.png"
    )

    # ----------------------------------------
    # RGB CHANNEL SWAP
    # ----------------------------------------

    print("\n--- RGB Channel Swap ---")

    swap_pixel_channels(
        INPUT_IMG,
        OUTPUT_SWAPPED
    )

    # ----------------------------------------
    # MATHEMATICAL OPERATION
    # ----------------------------------------

    print("\n--- Pixel Mathematical Operation ---")

    try:
        key = int(input("Enter key value: "))

    except ValueError:
        print("❌ Key must be an integer.")
        exit()

    print("\nChoose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")

    choice = input("\nEnter your choice (1/2/3): ").strip()

    if choice == "1":
        operation = "add"

    elif choice == "2":
        operation = "subtract"

    elif choice == "3":
        operation = "multiply"

    else:
        print("❌ Invalid choice.")
        exit()

    apply_math_operation(
        INPUT_IMG,
        OUTPUT_MATH,
        key,
        operation
    )

    print("\n======================================")
    print("          PROCESS COMPLETED")
    print("======================================")

    print("\n📁 Output files:")
    print(OUTPUT_SWAPPED)
    print(OUTPUT_MATH)

    input("\nPress Enter to exit...")
