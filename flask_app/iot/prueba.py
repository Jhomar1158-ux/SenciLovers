import time
import conversion_data
import COM_ESP32

val = COM_ESP32.getDatafromESP()
print(val)
print(type(val))
for element in val:
    print (type(element))

monto = 8.5
print(conversion_data.validation(monto,val))
lista = conversion_data.convertir_monto(monto,val)
COM_ESP32.sendDataToESP32(lista)