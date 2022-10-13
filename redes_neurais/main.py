import cv2
import time

# Cores para colocar em cada classe
colors = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

# Abrindo o arquivo coco.names e colocando cada linha na lista class_names
class_names = []
with open('coco.names', 'r') as f:
    class_names = [cname.strip() for cname in f.readlines()]

# Abrindo a webcam
cap = cv2.VideoCapture(0)

# Carregando os pesos da rede neural
net = cv2.dnn.readNet('yolov4-tiny.weights', 'yolov4-tiny.cfg')

# Setando os parâmetros da rede neural
model = cv2.dnn_DetectionModel(net)
model.setInputParms(size=(416, 416), scale=1/255)

# Lendo os frames do vídeo
while True:
    _, frame = cap.read() # Captura do frame
    start = time.time() # Começo da contagem dos milisegundos
    classes, scores, boxes = model.detect(frame, 0.1, 0.2) # Detecção
    end = time.time() # Fim da contagem dos milisegundos
    # percorrendo toda detecção
    for classid, score, box in zip(classes, scores, boxes):
        color = colors[int(classid) % len(colors)] # Gerando uma cor para a classe
        label = f'{class_names[classid[0]]} : {score}' # Pegando o nome da classe pelo ID e o seu score (texto que vai aparecer no quadrado)
        cv2.rectangle(frame, box, color, 2) # Desenhando a box da detecção
        cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5)
    # Calculando o tempo que levou para fazer a detecção
    fps_label = f'FPS: {round((1.0/(end - start)), 2)}'

    # Escrevendo o FPS na imagem
    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX(), 1)

    # Mostrando a imagem
    cv2.imshow('detections', frame)

    # Espera da resposta
    if cv2.waitKey(1) == 27:
        break

    # Liberação da câmera e destruindo todas as janelas
    cap.release()
    cv2.destroyallWindows()
