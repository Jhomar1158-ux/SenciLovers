import time
import serial

#nombre del dispositivo serial : dmesg | grep -v disconnect | grep -Eo "tty(ACM|USB)." | tail -1
ser = serial.Serial("/dev/ttyUSB1", baudrate=9600)
ser.flushInput()
retiro_Senci = [1,0,0,1]
monto_Senci = [0,0,0,0]
read = "1,2,3,4"
aux=1

try:
    while True:
        if(aux==1):
            retiroBytes = (','.join(str(x) for x in retiro_Senci)).encode('latin-1')
            ser.write(retiroBytes)
            print(retiroBytes)
            time.sleep(0.5)
            aux=0
        if(aux==0):
            read = ser.readline().decode('latin-1').strip()
            if (read == "LISTO"): aux=1

except KeyboardInterrupt:
    print("\nInterrupcion por teclado")
except ValueError as ve:
    print(ve)
    print("Otra interrupcion")
finally:
    ser.close()