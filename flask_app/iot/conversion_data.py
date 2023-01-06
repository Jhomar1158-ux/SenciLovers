#Convierte el RETIRO(FLOAT) a una RETIRO(LISTA)    
## RETIRO(LISTA) -> 0.50, 1, 2, 5 soles
def conversion_data(retiroActual):
    retiroActual=float(retiroActual)
    # pesos -> [0.5, 1, 2, 5]
    #2.5 ->[1,0,1,0]
    #2.5 ->[5,0,0,0]
    #2.5 ->[0,0,0,0]
    #2.5 ->[0,0,0,0]
    pass

def greedyMoney(residualpay):
    money = [0.5,1,2,5]
    # residualpay = 96
    selectedMoney = []
    index = len(money) - 1
    while (residualpay > 0):
        pay = residualpay - money[index]
        if (pay >= 0):
            residualpay = pay
            selectedMoney.append(money[index])
        else:
            index = index - 1
    return selectedMoney