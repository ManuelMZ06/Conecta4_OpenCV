import serial
import time

# CAMBIA COM3 POR TU PUERTO
arduino = serial.Serial('COM3', 9600)

time.sleep(2)

while True:

    valor = input("Enviar columna: ")

    arduino.write(valor.encode())

    print("Enviado:", valor)