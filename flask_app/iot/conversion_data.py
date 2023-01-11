#Convierte el RETIRO(FLOAT) a una RETIRO(LISTA)    
## RETIRO(LISTA) -> 0.50, 1, 2, 5 soles
# ejemplo: [1,1,1,1] = 8.5 soles

''' 
Esta funcion convierte el monto ingresado (var: residualpay) en una lista
de monedas de Senci. Se debe ingresar como segundo argumento la cantidad
de monedas disponibles en formato lista(var: available). La funcion 
utilizara todas las monedas disponibles para alcanzar el monto.
''' 
'''
def convertir_monto(residualpay,available):
    # available format is [#,#,#,#] (# int)
    money = [0.5,1,2,5]
    senciList = [0,0,0,0]
    index = len(money) - 1
    while (residualpay > 0):
        pay = residualpay - money[index]
        if pay >= 0:
            if available[index]>0:
                residualpay = pay
                senciList[index] += 1
            else:
                index = index - 1
        else:
            senciList[index]=0
            index = index - 1
    return senciList
'''
# Validacion entre dos listas
def validation(retiro,disponible):
    aux = 0
    for index in range(4):
        if retiro[index] <= disponible[index]: aux = aux + 1
    
    if aux == 4: return True
    else: return False 
            

# Entrega una lista con el minimo numero de monedas
def greedy_monto(residualpay):
    money = [0.5,1,2,5]
    selectedMoney = []
    index = len(money) - 1
    senciList = [0,0,0,0]
    while (residualpay > 0):
        pay = residualpay - money[index]
        if (pay >= 0):
            residualpay = pay
            senciList[index] = senciList[index]+1
        else:
            index = index - 1
    return senciList