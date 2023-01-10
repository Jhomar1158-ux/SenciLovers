#Convierte el RETIRO(FLOAT) a una RETIRO(LISTA)    
## RETIRO(LISTA) -> 0.50, 1, 2, 5 soles
# ejemplo: [1,1,1,1] = 8.5 soles
def conversion_data(retiroActual):
    retiroActual=float(retiroActual)
    # pesos -> [0.5, 1, 2, 5]
    #2.5 ->[1,0,1,0]
    #2.5 ->[5,0,0,0]
    #2.5 ->[0,0,0,0]
    #2.5 ->[0,0,0,0]
    pass

''' 
Esta funcion convierte el monto ingresado (var: residualpay) en una lista
de monedas de Senci. Se debe ingresar como segundo argumento la cantidad
de monedas disponibles en formato lista(var: available). La funcion 
utilizara todas las monedas disponibles para alcanzar el monto.
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

# VALIDACION
def validation(residualpay,available):
    # available format is [#,#,#,#] (# int)
    money = [0.5,1,2,5]
    index = len(money) - 1
    while (residualpay > 0):
        pay = residualpay - money[index]
        if pay >= 0:
            if available[index]>0:
                residualpay = pay
            else:
                index = index - 1
                if index < 0: break
                else: return False
        else:
            index = index - 1
    return True
# print(convertir_monto(10,[0,0,0,2]))
# print(convertir_monto(10,[0,0,5,0]))
# print(convertir_monto(10,[0,0,0,0]))
