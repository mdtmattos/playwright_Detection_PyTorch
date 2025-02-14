# Description

This project uses Playwright and Python to perform some tests using AI with PyTorch.

## 📝 File Descriptions
- **.gitignore**: Defines files and directories to be ignored by Git.
- **README.md**: Project documentation.
- **requirements.txt**: List of project dependencies.
- **src/**: Main source code of the project.
- **tests/**: Directory containing the tests.
- **accessebility.py**: Code for accessibility tests.
- **faceDetect.py**: Code for face detection.
- **personDetect.py**: Code for person detection.
- **screenshots/**: Directory to store screenshots.
- **takeWebpageScreenshots.py**: Script to capture screenshots of web pages.

## 💻 Activate the Virtual Environment
```bash
python -m venv venv
.\venv\Scripts\activate
```

## 📦 Install dependencies
```bash
pip install -r requirements.txt
```

# 📝 Available Scripts
## Capture Screenshot of a Web Page
The script takeWebpageScreenshots.py captures a screenshot of a specified web page.
```bash
python src/tests/takeWebpageScreenshots.py
```

## Check Accessibility
The script accessebility.py checks the accessibility of a web page and performs contrast, text readability, and color analysis.
```bash
python src/tests/accessebility.py
```

## Detect People in an Image
The script personDetect.py detects people in an image using a pre-trained PyTorch model.
```bash
python src/tests/personDetect.py
```

## Detect Faces in an Image
The script faceDetect.py detects faces in an image using the facenet_pytorch library.
```bash
python src/tests/faceDetect.py
```

## ⚙️ Dependencies
The project dependencies are listed in the requirements.txt file:

playwright
torch
numpy
pillow
pytesseract
torchvision
facenet_pytorch
