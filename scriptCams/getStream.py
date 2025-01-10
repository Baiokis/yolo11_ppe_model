import cv2

username = "admin"
password = "autvix123456"
ip_camera = "192.168.1.108"
port = "554"

rtsp_url = f"rtsp://{username}:{password}@{ip_camera}:{port}/cam/realmonitor?channel=1&subtype=0"
cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Erro ao conectar à câmera. Verifique as configurações.")
    exit()

print("Transmissão ao vivo iniciada. Pressione 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Não foi possível obter o frame da câmera.")
        break

    frame = cv2.resize(frame, (1920, 1080))
    cv2.imshow("Transmissão ao Vivo", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
