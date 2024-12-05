import cv2
from ultralytics import YOLO

model = YOLO("yolo8l.pt")

classNames = [
    "Person",
    "Head",
    "Face",
    "Glasses",
    "Face-mask-medical",
    "Face-guard",
    "Ear",
    "Earmuffs",
    "Hands",
    "Gloves",
    "Foot",
    "Shoes",
    "Safety-vest",
    "Tools",
    "Helmet",
    "Medical-suit",
    "Safety-suit"
]

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 60)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not cap.isOpened():
    print("Erro ao conectar à câmera. Verifique as configurações.")
    exit()

print("Transmissão ao vivo iniciada com detecção de EPI. Pressione 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Não foi possível obter o frame da câmera.")
        break

    results = model(frame)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = round(float(box.conf[0]), 2)
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            color = (0, 255, 0) if 'NO-' not in currentClass else (0, 0, 255)

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{currentClass} {conf}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    cv2.imshow("Transmissão ao Vivo com Detecção de EPI", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
