import os
import torch

image_dir = 'fotos'
output_dir = 'resultados'
model_path = 'last.pt'
repo_dir = 'yolov5'

model = torch.hub.load(repo_dir, 'custom', path=model_path, source='local')
os.makedirs(output_dir, exist_ok=True)

for image_name in os.listdir(image_dir):
    if image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(image_dir, image_name)

        results = model(image_path)

        results.save(save_dir=output_dir)

        print(f"Processado: {image_name}")

print(f"Resultados salvos no diretório: {output_dir}")
