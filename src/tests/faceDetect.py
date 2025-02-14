import torch
from torchvision import transforms as T
from PIL import Image
import os
from facenet_pytorch import MTCNN

def main():
    # Load the image
    image_path = "screenshots/webpageImage.png"
    if not os.path.exists(image_path):
        print(f"Error: Image file not found at {image_path}")
        return

    image = Image.open(image_path)
    transform = T.Compose([T.ToTensor()])
    image_tensor = transform(image).unsqueeze(0)  # Add batch dimension

    # Initialize the face detector
    mtcnn = MTCNN(keep_all=True)

    # Detect faces
    boxes, _ = mtcnn.detect(image)
    if boxes is None:
        print("No faces detected.")
        return

    # Ensure the folder to save cropped face images exists
    os.makedirs("screenshots/faces", exist_ok=True)

    # Save cropped face images and count how many were found
    face_count = 0
    for i, box in enumerate(boxes):
        xmin, ymin, xmax, ymax = [int(b) for b in box]
        cropped_face = image.crop((xmin, ymin, xmax, ymax))
        cropped_face.save(f"screenshots/faces/face_{i}.png")
        face_count += 1
        print(f"Detected face image saved at: screenshots/faces/face_{i}.png")

    # Inform how many face images were found
    print(f"Total detected face images: {face_count}")

if __name__ == "__main__":
    main()