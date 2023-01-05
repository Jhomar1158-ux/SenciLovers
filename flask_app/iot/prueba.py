import COM_ESP32
import time


COM_ESP32.sendDataToESP32("1,1,1,1")
time.sleep(1)

# print(COM_ESP32.getDatafromESP())