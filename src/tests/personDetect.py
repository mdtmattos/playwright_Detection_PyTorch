import torch
import torchvision.transforms as T
from torchvision import models
from PIL import Image
from torchvision.models.detection import FasterRCNN_ResNet50_FPN_Weights
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load pre-trained model
model = models.detection.fasterrcnn_resnet50_fpn(weights=FasterRCNN_ResNet50_FPN_Weights.COCO_V1)
model.eval()

# Load the image
image = Image.open("screenshots/webpageImage.png")
transform = T.Compose([T.ToTensor()])
image_tensor = transform(image).unsqueeze(0)  # Add batch dimension

# Perform detection
with torch.no_grad():
    prediction = model(image_tensor)

# Filter person detections (class 1 in COCO dataset)
person_class_id = 1
person_boxes = [box for box, label in zip(prediction[0]['boxes'], prediction[0]['labels']) if label == person_class_id]

# Ensure the folder to save cropped person images exists
os.makedirs("screenshots/persons", exist_ok=True)

# Save cropped person images and count how many were found
person_count = 0
for i, box in enumerate(person_boxes):
    xmin, ymin, xmax, ymax = box.int().tolist()
    cropped_image = image.crop((xmin, ymin, xmax, ymax))
    cropped_image.save(f"screenshots/persons/person_{i}.png")
    person_count += 1
    print(f"Detected person image saved at: screenshots/persons/person_{i}.png")

# Inform how many person images were found
print(f"Total detected person images: {person_count}")
