    ## Redondeo 0.5, 0.0
    # "2.5"
    # "2.1" -> "2.0"
    # "2.2" -> "2.0"
    # "2.4" -> "2.0"
    # "2.5" -> "2.5"
    
    # "2.6" -> "3.0"
    # "2.7" -> "3.0"
    # "2.9" -> "3.0"
    ## Conversión a String (1,1,1,1)
    # 2.0 ->
import math
def conversion_data(retiroActual):
    tempRetiroActual = retiroActual.split(".")
    tempDecimal = int(tempRetiroActual[1])
    print(type(tempDecimal))
    retiroActualFloat = float(retiroActual)
    if(tempDecimal==0 or tempDecimal==5):
        print("cantidad correcta")
        print(retiroActualFloat)
    elif(tempDecimal<5): #"2.3"
        retiroActualFloat = float(math.floor(retiroActualFloat))
        print("cantidad incorrecta")
        print("redondeando")
        print(retiroActualFloat)
    elif(tempDecimal>5):
        retiroActualFloat = float(math.ceil(retiroActualFloat))
        print("cantidad incorrecta")
        print("redondeando")
        print(retiroActualFloat)
