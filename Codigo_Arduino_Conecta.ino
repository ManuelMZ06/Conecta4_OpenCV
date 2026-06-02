#include <Servo.h>

// =========================
// SERVOS
// =========================

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;
Servo servo7;

// =========================
// BOTÓN
// =========================

const int botonPin = 9;

// =========================
// POSICIONES
// =========================

const int POS_CERRADO = 0;
const int POS_ABIERTO = 90;

// =========================
// ESTADO BOTÓN
// =========================

bool ultimoEstado = HIGH;

// =========================
// FUNCIÓN SERVO
// =========================

void moverServo(Servo &servo) {

  servo.write(POS_ABIERTO);

  delay(1500);

  servo.write(POS_CERRADO);

  delay(500);
}

// =========================
// SETUP
// =========================

void setup() {

  Serial.begin(9600);

  pinMode(botonPin, INPUT_PULLUP);

  servo1.attach(2);
  servo2.attach(3);
  servo3.attach(4);
  servo4.attach(5);
  servo5.attach(6);
  servo6.attach(7);
  servo7.attach(8);

  servo1.write(POS_CERRADO);
  servo2.write(POS_CERRADO);
  servo3.write(POS_CERRADO);
  servo4.write(POS_CERRADO);
  servo5.write(POS_CERRADO);
  servo6.write(POS_CERRADO);
  servo7.write(POS_CERRADO);

  Serial.println("Sistema listo");
}

// =========================
// LOOP
// =========================

void loop() {

  // =========================
  // BOTÓN
  // =========================

  bool estadoBoton = digitalRead(botonPin);

  if (ultimoEstado == HIGH && estadoBoton == LOW) {

    Serial.println("BTN");

    delay(300);
  }

  ultimoEstado = estadoBoton;

  // =========================
  // RECIBIR COLUMNAS
  // =========================

  if (Serial.available()) {

    char columna = Serial.read();

    if (columna == '1') moverServo(servo1);
    else if (columna == '2') moverServo(servo2);
    else if (columna == '3') moverServo(servo3);
    else if (columna == '4') moverServo(servo4);
    else if (columna == '5') moverServo(servo5);
    else if (columna == '6') moverServo(servo6);
    else if (columna == '7') moverServo(servo7);
  }
}