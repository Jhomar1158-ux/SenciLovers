import time
import conversion_data
# import COM_ESP32
'''
val = COM_ESP32.getDatafromESP()
print(val)
print(type(val))
for element in val:
    print (type(element))

monto = 8.5
print(conversion_data.validation(monto,val))
lista = conversion_data.convertir_monto(monto,val)
COM_ESP32.sendDataToESP32(lista)
'''
monto = 16
valor_lista = [0,4,2,3]
# print(len(valor_lista))
# print(conversion_data.validation(monto,valor_lista))
retiro = conversion_data.greedy_convertir_monto(monto)
print(retiro)
print(conversion_data.validation(retiro,valor_lista))