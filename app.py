import cv2
import numpy as np
import math
import copy
import serial
import time
import pyttsx3

# =========================
# SERIAL ARDUINO
# =========================

arduino = serial.Serial('COM5', 9600)
time.sleep(2)

# =========================
# AUDIO
# =========================

def hablar(texto):

    print(f"[AUDIO]: {texto}")

    voz = pyttsx3.init()

    voz.setProperty('rate', 170)

    voz.say(texto)

    voz.runAndWait()

    voz.stop()

# =========================
# CONFIG
# =========================

ROWS = 6
COLS = 7

PLAYER = 2   # rojo (humano)
AI = 3       # amarillo (IA)
EMPTY = 1

# =========================
# COORDENADAS
# =========================

coordenadas = [

    (142, 103),
    (261, 103),
    (381, 103),
    (501, 103),
    (620, 103),
    (740, 103),
    (860, 103),

    (142, 205),
    (261, 205),
    (381, 205),
    (501, 205),
    (620, 205),
    (740, 205),
    (860, 205),

    (142, 308),
    (261, 308),
    (381, 308),
    (501, 308),
    (620, 308),
    (740, 308),
    (860, 308),

    (142, 411),
    (261, 411),
    (381, 411),
    (501, 411),
    (620, 411),
    (740, 411),
    (860, 411),

    (142, 514),
    (261, 514),
    (381, 514),
    (501, 514),
    (620, 514),
    (740, 514),
    (860, 514),

    (142, 617),
    (261, 617),
    (381, 617),
    (501, 617),
    (620, 617),
    (740, 617),
    (860, 617)

]

# =========================
# GRAVEDAD
# =========================

def apply_gravity(board):

    new_board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

    for col in range(COLS):

        stack = []

        for row in range(ROWS - 1, -1, -1):

            if board[row][col] != EMPTY:
                stack.append(board[row][col])

        for row in range(ROWS - 1, -1, -1):

            if stack:
                new_board[row][col] = stack.pop(0)

    return new_board

# =========================
# VALIDACIÓN
# =========================

def is_valid_location(board, col):

    return board[0][col] == EMPTY


def get_next_open_row(board, col):

    for r in range(ROWS - 1, -1, -1):

        if board[r][col] == EMPTY:
            return r

    return None


def drop_piece(board, row, col, piece):

    board[row][col] = piece

# =========================
# GANADOR
# =========================

def winning_move(board, piece):

    # Horizontal
    for r in range(ROWS):

        for c in range(COLS - 3):

            if all(board[r][c + i] == piece for i in range(4)):
                return True

    # Vertical
    for c in range(COLS):

        for r in range(ROWS - 3):

            if all(board[r + i][c] == piece for i in range(4)):
                return True

    # Diagonal positiva
    for r in range(ROWS - 3):

        for c in range(COLS - 3):

            if all(board[r + i][c + i] == piece for i in range(4)):
                return True

    # Diagonal negativa
    for r in range(3, ROWS):

        for c in range(COLS - 3):

            if all(board[r - i][c + i] == piece for i in range(4)):
                return True

    return False

# =========================
# IA
# =========================

def evaluate_window(window, piece):

    score = 0

    opp_piece = PLAYER if piece == AI else AI

    if window.count(piece) == 4:
        score += 1000

    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 50

    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 10

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 80

    if window.count(opp_piece) == 4:
        score -= 1000

    return score


def score_position(board, piece):

    score = 0

    # Centro
    center_array = [board[r][COLS // 2] for r in range(ROWS)]
    center_count = center_array.count(piece)

    score += center_count * 6

    # Horizontal
    for r in range(ROWS):

        row_array = [board[r][c] for c in range(COLS)]

        for c in range(COLS - 3):

            window = row_array[c:c + 4]
            score += evaluate_window(window, piece)

    # Vertical
    for c in range(COLS):

        col_array = [board[r][c] for r in range(ROWS)]

        for r in range(ROWS - 3):

            window = col_array[r:r + 4]
            score += evaluate_window(window, piece)

    # Diagonal positiva
    for r in range(ROWS - 3):

        for c in range(COLS - 3):

            window = [board[r + i][c + i] for i in range(4)]
            score += evaluate_window(window, piece)

    # Diagonal negativa
    for r in range(3, ROWS):

        for c in range(COLS - 3):

            window = [board[r - i][c + i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score

# =========================
# MINIMAX
# =========================

def minimax(board, depth, alpha, beta, maximizing):

    valid_cols = [c for c in range(COLS) if is_valid_location(board, c)]

    terminal = (

        winning_move(board, PLAYER) or
        winning_move(board, AI) or
        len(valid_cols) == 0

    )

    if depth == 0 or terminal:

        if terminal:

            if winning_move(board, AI):
                return None, 1000000

            elif winning_move(board, PLAYER):
                return None, -1000000

            else:
                return None, 0

        return None, score_position(board, AI)

    # MAX
    if maximizing:

        value = -math.inf
        best_col = valid_cols[0]

        for col in valid_cols:

            row = get_next_open_row(board, col)

            temp_board = copy.deepcopy(board)

            drop_piece(temp_board, row, col, AI)

            new_score = minimax(
                temp_board,
                depth - 1,
                alpha,
                beta,
                False
            )[1]

            if new_score > value:

                value = new_score
                best_col = col

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return best_col, value

    # MIN
    else:

        value = math.inf
        best_col = valid_cols[0]

        for col in valid_cols:

            row = get_next_open_row(board, col)

            temp_board = copy.deepcopy(board)

            drop_piece(temp_board, row, col, PLAYER)

            new_score = minimax(
                temp_board,
                depth - 1,
                alpha,
                beta,
                True
            )[1]

            if new_score < value:

                value = new_score
                best_col = col

            beta = min(beta, value)

            if alpha >= beta:
                break

        return best_col, value

# =========================
# CÁMARA
# =========================

cap = cv2.VideoCapture(0)

print("\n====================================")
print("CONECTA 4 IA + ARDUINO")
print("====================================")
print("BOTÓN -> analizar tablero")
print("ESC    -> salir")
print("====================================\n")

hablar("El juego ha comenzado")
time.sleep(1)

hablar("Turno del jugador")
time.sleep(1)

while True:

    ret, frame = cap.read()

    if not ret:
        continue

    frame = cv2.resize(frame, (1000, 700))

    # =========================
    # SUAVIZAR IMAGEN
    # =========================

    frame = cv2.GaussianBlur(frame, (5, 5), 0)

    # =========================
    # MOSTRAR PUNTOS
    # =========================

    for i, (x, y) in enumerate(coordenadas):

        if 'board_flat' in locals():
            val = board_flat[i]
        else:
            val = EMPTY

        # Gris
        if val == EMPTY:
            color = (200, 200, 200)

        # Rojo
        elif val == PLAYER:
            color = (0, 0, 255)

        # Amarillo
        else:
            color = (0, 255, 255)

        cv2.circle(frame, (x, y), 15, color, -1)

    cv2.imshow("Conecta 4 IA", frame)

    key = cv2.waitKey(1) & 0xFF

    # ESC
    if key == 27:
        break

    # =========================
    # BOTÓN ARDUINO
    # =========================

    if arduino.in_waiting:

        boton = arduino.readline().decode().strip()

        if boton == "BTN":

            

            board_flat = []

            # =========================
            # DETECCIÓN HSV
            # =========================

            for (x, y) in coordenadas:

                zona = frame[y-25:y+25, x-25:x+25]

                hsv = cv2.cvtColor(zona, cv2.COLOR_BGR2HSV)

                # =========================
                # ROJO
                # =========================

                rojo1 = cv2.inRange(
                    hsv,
                    np.array([0, 120, 70]),
                    np.array([10, 255, 255])
                )

                rojo2 = cv2.inRange(
                    hsv,
                    np.array([170, 120, 70]),
                    np.array([180, 255, 255])
                )

                mascara_rojo = rojo1 + rojo2

                # =========================
                # AMARILLO
                # =========================

                mascara_amarillo = cv2.inRange(
                    hsv,
                    np.array([15, 100, 100]),
                    np.array([40, 255, 255])
                )

                # =========================
                # CONTAR PIXELES
                # =========================

                pixeles_rojos = cv2.countNonZero(mascara_rojo)

                pixeles_amarillos = cv2.countNonZero(mascara_amarillo)

                # =========================
                # DECISIÓN
                # =========================

                if pixeles_rojos > 300:

                    board_flat.append(PLAYER)

                elif pixeles_amarillos > 300:

                    board_flat.append(AI)

                else:

                    board_flat.append(EMPTY)

            # =========================
            # MATRIZ
            # =========================

            board = []

            for i in range(0, 42, 7):

                board.append(board_flat[i:i+7])

            # Aplicar gravedad
            board = apply_gravity(board)

            # =========================
            # MOSTRAR TABLERO
            # =========================

            print("\n==============================")
            print("TABLERO DETECTADO")
            print("==============================")

            for fila in board:
                print(fila)

            # =========================
            # VERIFICAR GANADOR
            # =========================

            if winning_move(board, PLAYER):

                print("\nEL JUGADOR HA GANADO")

                hablar("El jugador ha ganado")
                time.sleep(3)

                break

            elif winning_move(board, AI):

                print("\nLA IA HA GANADO")

                hablar("La inteligencia artificial ha ganado")
                time.sleep(3)

                break

            # =========================
            # IA
            # =========================

            hablar("Turno de la inteligencia artificial")
            time.sleep(1)

            best_col, score = minimax(
                board,
                5,
                -math.inf,
                math.inf,
                True
            )

            print("\n==============================")
            print("MEJOR JUGADA DE LA IA")
            print("==============================")

            if best_col is not None:

                columna_fisica = best_col + 1

                print(f"Columna física: {columna_fisica}")
                print(f"Columna código: {best_col}")
                print(f"Puntaje: {score}")

                # =========================
                # ENVIAR A ARDUINO
                # =========================

                arduino.write(str(columna_fisica).encode())

                print("\nENVIADO A ARDUINO")

                

            else:

                print("EMPATE - TABLERO LLENO")

                hablar("Empate")
                time.sleep(2)

            print("==============================")

            hablar("Turno del jugador")
            time.sleep(1)

cap.release()
cv2.destroyAllWindows()
arduino.close()