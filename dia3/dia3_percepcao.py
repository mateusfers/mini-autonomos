import cv2
import numpy as np

# 1. Cria uma imagem sintética 400x400 (fundo cinza escuro)
imagem = np.zeros((400, 400, 3), dtype=np.uint8)
imagem[:] = (40, 40, 40)

# 2. Desenha um obstáculo vermelho
cv2.rectangle(imagem, (150, 100), (230, 180), (0, 0, 255), -1)

# 3. Converte de BGR para HSV
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# 4. Define a faixa do vermelho
vermelho_baixo = np.array([0, 120, 70])
vermelho_alto = np.array([10, 255, 255])

# 5. Cria a máscara
mascara = cv2.inRange(hsv, vermelho_baixo, vermelho_alto)

# 6. Encontra os contornos
contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 7. Desenha a bounding box
for contorno in contornos:
    x, y, w, h = cv2.boundingRect(contorno)
    cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 2)
    centro_x, centro_y = x + w // 2, y + h // 2
    print(f"Obstáculo detectado no centro: ({centro_x}, {centro_y})")

# 8. Salva a imagem
cv2.imwrite("detecao_obstaculo.png", imagem)
print("Imagem salva como 'detecao_obstaculo.png'")