import pytesseract
from PIL import Image
import json
import os

print("--- OCR Script Started ---")

# ----- FORCE PYTHON TO USE TESSERACT DIRECTLY -----
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Image path
image_path = r"C:\Users\Admin\OneDrive\Desktop\Documents\OCR_Project\images\sample.jfif"

# Check if file exists
if not os.path.exists(image_path):
    print("ERROR: Image not found at:", image_path)
    exit()

print(f"Loading image: {image_path}")

# Read image using PIL
try:
    img = Image.open(image_path)
    print("Image loaded successfully.")

    # Extract text
    print("Extracting text (this may take a few seconds)...")
    text = pytesseract.image_to_string(img)
    print("OCR Extraction complete.")

    print("\nExtracted Text:")
    print("-" * 20)
    print(text if text.strip() else "[No text detected]")
    print("-" * 20)

    # Convert to JSON
    data = {
        "filename": image_path,
        "extracted_text": text
    }

    # Save JSON file
    print("Saving results to output.json...")
    with open("output.json", "w") as file:
        json.dump(data, file, indent=4)

    print("\nOCR Completed Successfully! Check output.json")

except Exception as e:
    print(f"ERROR during OCR process: {e}")
