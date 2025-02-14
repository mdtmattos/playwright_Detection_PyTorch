from playwright.sync_api import sync_playwright
import json
import torch
import numpy as np
from PIL import Image, ImageOps
import pytesseract
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Function to check accessibility
def check_accessibility(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        # Inject axe-core for accessibility analysis
        axe_script = page.evaluate("""
            async () => {
                const response = await fetch('https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.4.2/axe.min.js');
                const scriptText = await response.text();
                eval(scriptText);
                return axe.run();
            }
        """)

        # Process the results
        accessibility_issues = json.loads(json.dumps(axe_script))
        
        # Capture screenshot of the page
        screenshot = page.screenshot(full_page=True)
        browser.close()

        return accessibility_issues, screenshot

# Function to analyze contrast
def analyze_contrast(image_bytes):
    # Open image with PIL
    image = Image.open(io.BytesIO(image_bytes))

    # Convert the image to grayscale
    grayscale_image = ImageOps.grayscale(image)
    image_array = np.array(grayscale_image)

    # Use PyTorch to process the image
    tensor_image = torch.tensor(image_array).float() / 255.0  # Normalize the image

    # Calculate contrast (simple: difference between maximum and minimum intensity)
    contrast = tensor_image.max() - tensor_image.min()
    print("📊 Analyzing Contrast...")
    print(f"Average image contrast: {contrast:.2f}")

    # Suggestion: if the contrast is low
    if contrast < 0.5:
        print("⚠️ The image contrast is low! Consider increasing the contrast to improve readability.")
    else:
        print("✅ The contrast is adequate.")

# Function to analyze text legibility
def analyze_text_legibility(image_bytes):
    # Using PyTesseract to detect text in the image
    image = Image.open(io.BytesIO(image_bytes))
    text = pytesseract.image_to_string(image)

    print("📊 Analyzing Text Legibility...")

    # Check if the text is sufficiently large
    if len(text) > 0:
        print(f"Detected text: {text[:100]}...")  # Displaying only the first 100 characters
        print("✅ Legible text detected.")
    else:
        print("⚠️ No legible text detected in the image!")

# Function to analyze colors (color blindness)
def analyze_colors(image_bytes):
    print("📊 Analyzing Accessible Colors...")

    # Load the image with PIL
    image = Image.open(io.BytesIO(image_bytes))
    image = image.convert("RGB")
    image_array = np.array(image)

    # Example of color check (simple): detect predominant colors
    reds = np.sum(image_array[:, :, 0] > 200)
    greens = np.sum(image_array[:, :, 1] > 200)
    blues = np.sum(image_array[:, :, 2] > 200)

    if reds > 50000:
        print("⚠️ Possible issue with excessive use of red! Check for color blindness.")
    if greens > 50000:
        print("⚠️ Possible issue with excessive use of green! Check for color blindness.")
    if blues > 50000:
        print("⚠️ Possible issue with excessive use of blue! Check for color blindness.")

# URL to test
url = "https://www.google.com/"
issues, screenshot = check_accessibility(url)

# Display accessibility issues
for issue in issues['violations']:
    print(f"🔴 Issue: {issue['description']}")
    print(f"ℹ️ Impact: {issue['impact']}")
    print(f"📌 Affected elements: {[el['html'] for el in issue['nodes']]}")
    print("-" * 50)

# Contrast analysis with PyTorch
analyze_contrast(screenshot)

# Text legibility analysis
analyze_text_legibility(screenshot)

# Color analysis (for color blindness)
analyze_colors(screenshot)
