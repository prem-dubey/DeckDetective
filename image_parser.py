from importlib.resources import files
import pytesseract
from PIL import Image  # fix import, use 'from PIL import Image'
import os

# Print your path here to get the data feeded to gemini api
# if path is a folder
PATH = "./NoogatAssignment"

def extract_text_from_images_folder(image_folder):
    """Extract text from a single image file using OCR."""

    all_data = []

    files = os.listdir(image_folder)
    files.sort()  # Sort alphabetically (case-sensitive)

    for i, image_file in enumerate(files, start=1):
        full_path = os.path.join(image_folder, image_file)
        print(f"Processing image: {full_path}")
        img = Image.open(full_path)

        text = pytesseract.image_to_string(img)
        slide_data = {
            "slide_number": i,
            "text": [text] if text.strip() else [],
            "image_text": [],
            "charts": []
        }
        all_data.append(slide_data)

    return all_data

def extract_text_from_single_image(image_path):
    all_data = []
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    slide_data = {
        "slide_number": 1,
        "text": [text] if text.strip() else [],
        "image_text": [],
        "charts": []
    }
    all_data.append(slide_data)
    return all_data


if __name__ == "__main__":
    from pprint import pprint
    data = extract_text_from_images_folder("./NoogatAssignment")
    pprint(data)



