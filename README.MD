# Conecta4_OpenCV

Sistema robótico autónomo capaz de jugar Conecta 4 contra un usuario humano mediante técnicas de visión artificial, inteligencia artificial y control electromecánico.

El proyecto integra OpenCV para la detección del estado del tablero, el algoritmo Minimax para la toma de decisiones estratégicas y una plataforma robótica basada en Arduino y servomotores para ejecutar físicamente los movimientos de la inteligencia artificial.

---

## Descripción General

El sistema analiza el tablero de juego utilizando una cámara web y procesamiento de imágenes en tiempo real. Una vez detectada la jugada del usuario, el estado del tablero es reconstruido digitalmente y evaluado mediante un algoritmo Minimax con poda Alpha-Beta para determinar la mejor respuesta posible.

Posteriormente, la decisión calculada es enviada a un Arduino, el cual controla los actuadores encargados de realizar el movimiento físico correspondiente.

El sistema también incorpora retroalimentación por voz para mejorar la interacción con el usuario durante la partida.

---

## Características

- Detección automática de fichas mediante visión artificial.
- Reconocimiento de fichas rojas y amarillas utilizando OpenCV.
- Reconstrucción automática del tablero digital.
- Aplicación de gravedad para corregir posibles errores de detección.
- Inteligencia Artificial basada en Minimax.
- Optimización mediante poda Alpha-Beta.
- Comunicación serial entre Python y Arduino.
- Control físico mediante servomotores.
- Interfaz visual en tiempo real.
- Sistema de audio para notificaciones y eventos del juego.
- Activación mediante pulsador físico.

---

## Arquitectura del Sistema

```text
Jugador
   │
   ▼
Tablero Físico
   │
   ▼
Cámara Web
   │
   ▼
OpenCV
   │
   ▼
Detección de Fichas
   │
   ▼
Construcción del Tablero
   │
   ▼
Minimax + Alpha Beta
   │
   ▼
Puerto Serial
   │
   ▼
Arduino
   │
   ▼
Servomotores
   │
   ▼
Movimiento de la IA
```

---

## Tecnologías Utilizadas

### Software

- Python 3.x
- OpenCV
- NumPy
- PySerial
- Pyttsx3

### Hardware

- Arduino Uno
- Cámara Web USB
- Servomotores
- Pulsador momentáneo
- Estructura mecánica del robot
- Tablero físico de Conecta 4

---

## Algoritmo de Inteligencia Artificial

La toma de decisiones se realiza mediante el algoritmo Minimax, el cual explora posibles estados futuros del juego para seleccionar la jugada óptima.

Se implementó poda Alpha-Beta para reducir significativamente el número de nodos evaluados y mejorar el tiempo de respuesta del sistema.

### Criterios de evaluación

- Victoria inmediata.
- Bloqueo de jugadas ganadoras del adversario.
- Formación de líneas de 2 y 3 fichas.
- Control de la columna central.
- Evaluación horizontal, vertical y diagonal.

---

## Visión Artificial

La detección de fichas se realiza mediante:

1. Captura de imagen desde cámara web.
2. Suavizado mediante filtro Gaussiano.
3. Conversión al espacio de color HSV.
4. Segmentación de colores rojo y amarillo.
5. Conteo de píxeles por región.
6. Clasificación de cada posición del tablero.

---

## Instalación

### Clonar repositorio

```bash
git clone https://github.com/ManuelMZ06/Conecta4_OpenCV.git
cd Conecta4_OpenCV
```

### Instalar dependencias

```bash
pip install opencv-python
pip install numpy
pip install pyserial
pip install pyttsx3
```

O bien:

```bash
pip install -r requirements.txt
```

---

## Ejecución

Conectar:

- Arduino
- Cámara Web
- Sistema mecánico

Ejecutar:

```bash
python app.py
```

---

## Funcionamiento

1. El usuario realiza una jugada.
2. Presiona el pulsador físico.
3. El sistema captura una imagen del tablero.
4. Se detectan las fichas presentes.
5. Se genera una representación digital del estado actual.
6. La IA calcula la mejor jugada.
7. Se envía la columna seleccionada al Arduino.
8. El robot ejecuta físicamente el movimiento.
9. El sistema anuncia el cambio de turno mediante audio.

---

## Resultados

Durante las pruebas realizadas se obtuvo:

- Detección estable de fichas rojas y amarillas.
- Comunicación serial confiable entre Python y Arduino.
- Correcta identificación de victorias horizontales, verticales y diagonales.
- Selección adecuada de movimientos mediante Minimax.
- Integración exitosa entre visión artificial, inteligencia artificial y robótica.

---

## Estructura del Proyecto

```text
Conecta4_OpenCV/
│
├── app.py
├── README.md
├── requirements.txt
├── arduino/
│   └── conecta4_robot.ino
├── docs/
│   ├── informe_tecnico.pdf
│   └── diagramas/
└── assets/
    └── imagenes/
```

---

## Trabajo Académico

Proyecto desarrollado como parte del curso de Inteligencia Artificial.

El objetivo principal fue demostrar la integración práctica de:

- Visión Artificial
- Inteligencia Artificial
- Robótica
- Sistemas Embebidos

en una solución autónoma capaz de interactuar con usuarios en un entorno físico real.

---

## Licencia

Este proyecto se distribuye con fines académicos y educativos.