import cv2

# =========================
# ESQUINAS
# =========================

x_inicio = 142
y_inicio = 86

x_fin = 901
y_fin = 645

# =========================
# ESPACIADO
# =========================

espacio_x = (x_fin - x_inicio) / 6
espacio_y = (y_fin - y_inicio) / 5

# =========================
# GENERAR COORDENADAS
# =========================

coordenadas = []

for fila in range(6):

    for columna in range(7):

        x = int(x_inicio + columna * espacio_x)
        y = int(y_inicio + fila * espacio_y)

        coordenadas.append((x, y))

# =========================
# MOSTRAR
# =========================

print("\nCOORDENADAS:\n")

for c in coordenadas:
    print(c)

# =========================
# CÁMARA
# =========================

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.resize(frame, (1000, 700))

    # =========================
    # DIBUJAR PUNTOS
    # =========================

    for (x, y) in coordenadas:

        cv2.circle(frame, (x, y), 8, (0, 0, 255), -1)

    cv2.imshow("Calibracion", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()