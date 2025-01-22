import torch
from torchvision import transforms as T
from PIL import Image
import os
from facenet_pytorch import MTCNN

def main():
    # Carregar a imagem
    image_path = "screenshots/webpageImage.png"
    if not os.path.exists(image_path):
        print(f"Erro: Arquivo de imagem não encontrado em {image_path}")
        return

    image = Image.open(image_path)
    transform = T.Compose([T.ToTensor()])
    image_tensor = transform(image).unsqueeze(0)  # Adiciona batch dimension

    # Inicializar o detector de rostos
    mtcnn = MTCNN(keep_all=True)

    # Detectar rostos
    boxes, _ = mtcnn.detect(image)
    if boxes is None:
        print("Nenhum rosto detectado.")
        return

    # Garantir que a pasta para salvar as imagens recortadas exista
    os.makedirs("screenshots/faces", exist_ok=True)

    # Salvar imagens recortadas dos rostos detectados e contar quantos foram encontrados
    face_count = 0
    for i, box in enumerate(boxes):
        xmin, ymin, xmax, ymax = [int(b) for b in box]
        cropped_face = image.crop((xmin, ymin, xmax, ymax))
        cropped_face.save(f"screenshots/faces/face_{i}.png")
        face_count += 1
        print(f"Imagem de rosto detectada salva em: screenshots/faces/face_{i}.png")

    # Informar quantas imagens de rostos foram encontradas
    print(f"Total de imagens de rostos detectadas: {face_count}")

if __name__ == "__main__":
    main()