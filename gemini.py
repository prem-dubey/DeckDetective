from google import genai
import os
import json 
from pptx_parser import process_pptx
from dotenv import load_dotenv
from image_parser import extract_text_from_images_folder
from image_parser import extract_text_from_single_image


# Path to your PPTX file
PATH = "./NoogatAssignment"


def determine_path_type(path):
    if os.path.isdir(path):
        return 'folder';
    if os.path.isfile(path):
        ext = os.path.splitext(path)[1].lower()
        if ext in [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff"]:
            return "image"
        elif ext == '.pptx':
            return 'pptx'
        else:
            return 'unknown'
    return 'unknown file type'

# loading .env file
load_dotenv()

path_type = determine_path_type(PATH)
if path_type == 'folder':
    data = extract_text_from_images_folder(PATH)
elif path_type == 'image':
    data = extract_text_from_single_image(PATH)
elif path_type == 'pptx':
    data = process_pptx(PATH)


# Making the code for PPTX analysis
client = genai.Client()

# writing the prompt for sending it 
prompt = """
You are an AI agent that detects factual and logical inconsistencies across multiple PowerPoint slides.

I will give you data in the following format:
[
  {
    "slide_number": 1,
    "text": ["Text extracted from slide shapes..."],
    "image_text": ["Text extracted from images via OCR..."],
    "charts": [
      {
        "chart_type": "COLUMN_CLUSTERED",
        "series": [
          {
            "name": "Revenue 2023",
            "categories": ["Q1", "Q2", "Q3", "Q4"],
            "values": [100, 200, 300, 400]
          }
        ]
      }
    ]
  },
  ...
]

Your job:
1. Read all slides and compare information across them.
2. Detect and list any factual or logical inconsistencies, such as:
   - Conflicting statements about the same topic or same numbers.
   - Conflicting numerical data (same metric, different values).
   - Percentages that don’t add up to 100%.
   - Contradictory textual claims.
   - Timeline mismatches or date conflicts.
   - Logical contradictions between statements.
3. If an inconsistency involves numbers from charts, mention that it came from a chart.

Output format (JSON array):
Return ONLY a JSON array of issues in the format:
    [
      {"type": "Numerical mismatch", "slides": [2, 5], "details": "Revenue in 2023 is inconsistent"},
      {"type": "Contradiction", "slides": [3, 4], "details": "Market described as both saturated and niche"},
      {"type": "Timeline mismatch", "slides": [4], "details": "Project timelines are inconsistent with the overall strategy"}

    ]

Do not add explanations outside of this JSON. Only return the JSON output.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=json.dumps({"data": data, "prompt": prompt})
)
if len(response.text) > 0:
    print(response.text)
else:
    print("No errors found")