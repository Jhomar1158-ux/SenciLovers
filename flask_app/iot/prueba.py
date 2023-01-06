# import COM_ESP32
import time
import conversion_data

# val = float (input("Valor :"))
# print(conversion_data.greedyMoney(val))
money = [0.5,1,2,5]
residualpay = 13
selectedMoney = []
senciMoney = [0,0,0,0]
index = len(money) - 1
while (residualpay > 0):
    pay = residualpay - money[index]
    if (pay >= 0):
        residualpay = pay
        selectedMoney.append(money[index])
    else:
        index = index - 1

for element in selectedMoney:
    if (element == 0.5):
        selectedMoney.remove(element)
    
print(selectedMoney)


# COM_ESP32.sendDataToESP32("1,1,1,1")
# time.sleep(1)

# print(COM_ESP32.getDatafromESP())