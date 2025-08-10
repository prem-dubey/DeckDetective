# AI-Powered PowerPoint Inconsistency Detector

This project provides a Python-based tool that detects factual, numerical, and logical inconsistencies across multi-slide PowerPoint presentations or screenshots of slides. Using AI (Gemini 2.5 Flash) and OCR, it analyzes slide text, images, and charts to flag conflicting data or contradictory claims.

---
## Problem Statement

The task is to build a Python tool that processes multi-slide PowerPoint presentations or slide images to detect factual and logical inconsistencies such as:  
- Conflicting numerical data (e.g., mismatched revenue or percentages)  
- Contradictory textual claims (e.g., market descriptions that conflict)  
- Timeline or date mismatches  

The tool must produce a clear, structured output referencing slide numbers and the type of inconsistencies found.  

---

## Solution Overview

- **PPTX Parsing**: Extracts text, images (OCR), and chart data from PowerPoint `.pptx` files.
- **Screenshot Parsing**: Processes slide screenshots (`.jpg`, `.jpeg`, `.png`), performing OCR to extract text from the image.
- **Gemini API Integration**: Sends extracted data to Gemini 2.5 Flash AI model for inconsistency detection.
- **Structured Output**: Prints a clear, easy-to-read report referencing slide numbers , type of inconsistency and inconsistency details.
- **Modular Design**: Separate modules for PPTX parsing, image parsing, and AI checking for easy extension.

---

## Workflow

- Input: PowerPoint file or folder of slide images.
- Parsing: Extract textual, numerical, and chart data with respective parsers.
- AI Analysis: Pass structured data to Gemini AI for deep inconsistency detection.
- Output: Receive and print a structured report highlighting slide-wise factual or logical issues.

---
## Code Explanation

- `pptx_parser.py`: Parses PowerPoint files, extracts text, charts, and images with OCR.  
- `image_parser.py`: Processes screenshots using OCR and computer vision to detect chart areas.  
- `gemini_checker.py`: Main orchestrator, calls parsers, sends data to Gemini API, and outputs inconsistency reports.  

---
## Sample Output
![sample output](https://res.cloudinary.com/dzwxshzzl/image/upload/v1754808976/Screenshot_2025-08-10_at_12.24.38_PM_fhetrl.png)


---

## Setup & Installation

**Clone the repository**  
   ```
     git clone https://github.com/prem-dubey/DeckDetective.git
     cd DeckDetective
   ```

**Setup venv**
```
python3 -m venv venv
```
- For mac : ```source venv/bin/activate```
- For Windows(PowerShell) : ```.\venv\Scripts\Activate.ps1```

**Install Dependencies**
```
pip install -r requirements.txt
```
**Install Tesseract OCR**
- macOS: ```brew install tesseract```
- Ubuntu: ```sudo apt install tesseract-ocr```
- Windows: Download and install from [here](https://github.com/UB-Mannheim/tesseract/wiki)


**Set Gemini API Key**
<br>
Set this into your .env file gemini will detect automatically <br>
**GEMINI_API_KEY**="your_api_key_here"


---

## How to use
- Simply upload the path to the pptx or folder in gemini.py (If you are facing issues then simply put in same folder in which you have cloned then change the name in the PATH variable)
- Run the file gemini.py using command ```python3 gemini.py ``` or ```python gemini.py```
- Sometimes it says operation not permitted so either permit vs code to acess the path or folder or move the folder to somewhere permitted ( Best option move it to the same folder DeckDetective)

---

## Limitations & Future Work

- OCR accuracy depends on input quality; some charts may be missed in images.  
- API token limits not yet fully managed for very large presentations.  
- Future improvements include batching and GUI development.

---
## 🤝 Credits
---

Designed and developed by: **Piyush Dubey (24NA10046)**  
As part of the **Software Development Internship Assignment By Noogat**
Inspired by the mission to build intelligent tools that enhance decision-making and consulting efficiency  


---

## 📬 Contact
Feel free to reach out to : <br>
premdubey10981@gmail.com <br>
[LinkedIn](https://www.linkedin.com/in/piyush-dubey-6b92a1312/) <br>
phone no - 9313553619




