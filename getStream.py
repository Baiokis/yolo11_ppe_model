import cv2

username = "admin" #login
password = "autvix123456" #senha
ip_camera = "192.168.1.108" #IP da CAM
port = "554" #porta específica para stream

rtsp_url = f"rtsp://{username}:{password}@{ip_camera}:{port}/cam/realmonitor?channel=1&subtype=0" #Url para a stream
cap = cv2.VideoCapture(rtsp_url) #Capturar a stream

if not cap.isOpened(): #Erro em abrir a camêra
    print("Erro ao conectar à câmera. Verifique as configurações.")
    exit()

print("Transmissão ao vivo iniciada. Pressione 'q' para sair.")

while True:
    ret, frame = cap.read() #Lendo os frames da stream
    if not ret:
        print("Não foi possível obter o frame da câmera.")
        break

    frame = cv2.resize(frame, (1920, 1080)) #Setando o tamanho da janela
    cv2.imshow("Transmissão ao Vivo", frame) #Abrir a Janela com a Stream
    if cv2.waitKey(1) & 0xFF == ord('q'): #Atalho para fechar janela
        break

cap.release() #libera os recursos da camera
cv2.destroyAllWindows() #fecha as janelas
