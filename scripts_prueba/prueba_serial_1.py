import time
import serial
#nombre del dispositivo serial : dmesg | grep -v disconnect | grep -Eo "tty(ACM|USB)." | tail -1
ser = serial.Serial("/dev/ttyUSB0", baudrate=9600)
ser.flushInput()
# Variables de Senci
# Orden de las monedas: 0.5 -- 1 -- 2 -- 5
retiro_Senci = [1,1,1,1]
monto_Senci = [0,0,0,0]
try:
    while True:
        comando = "PASAME EL DATO"
        comandoBytes = comando.encode()
        ser.write(comandoBytes)
        time.sleep(0.1)
        # Lee los datos y los convierte a una lista de enteros
        read = ser.readline().decode()
        monto_Senci = [int(k) for k in read.split(',')]
        # Verificacion
        print(read)
        print(monto_Senci)
        time.sleep(0.1)
        #------------------------------------#
        # Envio de lista de monedas a retirar
        retiroBytes = (','.join(str(x) for x in retiro_Senci)).encode()
        ser.write(retiroBytes)
        # Verificacion
        print(retiroBytes)

except KeyboardInterrupt:
    print("\nInterrupcion por teclado")
except ValueError as ve:
    print(ve)
    print("Otra interrupcion")
finally:
    ser.close()