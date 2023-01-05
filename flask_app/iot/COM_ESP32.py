import time
import serial

# Verificar la direccion del puerto de comunicacion
serialport = "/dev/ttyUSB1"

# nombre del dispositivo serial : dmesg | grep -v disconnect | grep -Eo "tty(ACM|USB)." | tail -1

# Solicita retiro de dinero a la ESP32
def sendDataToESP32(retiro_Senci):
    # Verificar el tipo de dato de retiro_Senci (lista 4 elementos tipo entero)
    with serial.Serial(serialport, 9600, timeout=1) as ser:
        time.sleep(0.1) # wait for serial to open
        # retiro_Senci = [1,0,0,1] 
        # Agregar validacion de variable retiro_Senci (tipo: lista de enteros)
        try:
            retiroBytes = (','.join(str(x) for x in retiro_Senci)).encode('latin-1')
            ser.write(retiroBytes)
            # print(retiroBytes)
            time.sleep(0.5)
            
        except KeyboardInterrupt:
            return None
                # print("\nInterrupcion por teclado")
            
        except ValueError as ve:
            # print(ve)
            # print("Otra interrupcion")
            return None
            
        finally:
            ser.close()

# Obtiene el valor del Monto de Senci directamente de la ESP32
def getDatafromESP():
    with serial.Serial(serialport, 9600, timeout=1) as ser:
        time.sleep(0.1) # wait for serial to open
        if ser.isOpen():
            try:
                ser.write("PASAME EL DATO")
                # print(retiroBytes)
                time.sleep(0.3)
                monto_Senci = ser.readline().decode('latin-1').strip()
                return monto_Senci

            except KeyboardInterrupt:
                return None
                    # print("\nInterrupcion por teclado")
                
            except ValueError as ve:
                # print(ve)
                # print("Otra interrupcion")
                return None
                
            finally:
                ser.close()

# Validacion de la cantidad de monedas (por si acaso)
def validation(retiro_Senci, fondo_Senci = getDatafromESP()):
    val = 0
    for index in range(4):
        if retiro_Senci[index] >= fondo_Senci[index]: val=+1
    
    if val == 4:  return True
    else: return False