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

## Explanation of Features and Functionality
- **PPTX Parsing**:
Extracts multi-modal content (text, charts, images) from slides. Uses python-pptx for structural data and pytesseract OCR to read embedded images, ensuring comprehensive data extraction.

- **Screenshot Parsing**:
Applies OCR to images to find text regions , capturing numeric and textual information even without access to the original .pptx file.

- **Gemini API Integration**:
Constructs detailed JSON representations of slide content and submits them to Gemini AI with a carefully designed prompt that asks for identification of factual, logical, and timeline inconsistencies.

- **Structured Output**:
Presents AI findings clearly in the terminal with slide references and categorized inconsistency descriptions, facilitating quick review and actionable insights.

- **Modularity**:
Separates concerns cleanly into parsers and the AI interface, allowing future improvements such as additional input formats, enhanced detection algorithms, or UI enhancements without rewriting core logic.


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

### Limitations
- OCR Dependence:
The accuracy of text extraction from images depends heavily on image quality and formatting. Low resolution or noisy images may reduce effectiveness.

- API Token Limits:
Large presentations may exceed Gemini API token limits, and the current implementation does not batch or chunk inputs to mitigate this.

- No GUI:
The tool operates purely via the terminal interface, which meets the project requirements but may limit user-friendliness.

- Model Dependency:
The quality and completeness of inconsistency detection rely on the Gemini AI model’s capabilities and prompt design; unusual or domain-specific slides may pose challenges.

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




