import torch
import torchvision.transforms as T
from torchvision import models
from PIL import Image
from torchvision.models.detection import FasterRCNN_ResNet50_FPN_Weights
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Carregar modelo pré-treinado
model = models.detection.fasterrcnn_resnet50_fpn(weights=FasterRCNN_ResNet50_FPN_Weights.COCO_V1)
model.eval()

# Carregar a imagem
image = Image.open("screenshots/webpageImage.png")
transform = T.Compose([T.ToTensor()])
image_tensor = transform(image).unsqueeze(0)  # Adiciona batch dimension

# Realizar detecção
with torch.no_grad():
    prediction = model(image_tensor)

# Filtrar detecções de pessoas (classe 1 no COCO dataset)
person_class_id = 1
person_boxes = [box for box, label in zip(prediction[0]['boxes'], prediction[0]['labels']) if label == person_class_id]

# Garantir que a pasta para salvar as imagens recortadas exista
os.makedirs("screenshots/persons", exist_ok=True)

# Salvar imagens recortadas das pessoas detectadas e contar quantas foram encontradas
person_count = 0
for i, box in enumerate(person_boxes):
    xmin, ymin, xmax, ymax = box.int().tolist()
    cropped_image = image.crop((xmin, ymin, xmax, ymax))
    cropped_image.save(f"screenshots/persons/person_{i}.png")
    person_count += 1
    print(f"Imagem de pessoa detectada salva em: screenshots/persons/person_{i}.png")

# Informar quantas imagens de pessoas foram encontradas
print(f"Total de imagens de pessoas detectadas: {person_count}")
