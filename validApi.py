import os
import json
from inference_sdk import InferenceHTTPClient

# Inicializar cliente de inferência
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="0TgGCksSMHBEKktA9CYJ"
)

# Configurar diretórios
input_dir = "fotos"
output_dir = "resultados"
os.makedirs(output_dir, exist_ok=True)

# Processar imagens
for filename in os.listdir(input_dir):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        input_path = os.path.join(input_dir, filename)
        result = CLIENT.infer(input_path, model_id="test-7wlfs/1")  # Fazer inferência
        output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.json")
        with open(output_path, "w") as f:
            json.dump(result, f, indent=4)  # Salvar resultado como JSON

print("Resultados salvos em 'resultados'.")
