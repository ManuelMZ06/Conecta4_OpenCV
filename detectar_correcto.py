import cv2

cap = cv2.VideoCapture(0)

def obtener_coordenadas(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"X={x}, Y={y}")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.resize(frame, (1000, 700))

    cv2.imshow("Seleccionar Puntos", frame)
    cv2.setMouseCallback("Seleccionar Puntos", obtener_coordenadas)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC para salir
        break

cap.release()
cv2.destroyAllWindows()