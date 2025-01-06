import os
import torch
from PIL import Image

# Configuração do caminho para o diretório de imagens
image_dir = 'fotos'  # Substitua pelo caminho onde estão suas imagens
output_dir = 'resultados'  # Diretório onde os resultados serão salvos
model_path = '460.pt'  # Substitua pelo caminho do seu modelo YOLOv5
repo_dir = 'yolov5'  # Substitua pelo caminho onde o repositório foi clonado

model = torch.hub.load(repo_dir, 'custom', path=model_path, source='local')
# Verifica se o diretório de resultados existe; se não, cria
os.makedirs(output_dir, exist_ok=True)

# Iterar sobre as imagens no diretório
for image_name in os.listdir(image_dir):
    # Verifica se o arquivo é uma imagem
    if image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(image_dir, image_name)
        
        # Realiza a predição
        results = model(image_path)
        
        # Salva a imagem com as detecções no diretório de saída
        results.save(save_dir=output_dir)
        
        print(f"Processado: {image_name}")

print(f"Resultados salvos no diretório: {output_dir}")
