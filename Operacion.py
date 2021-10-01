from random import randrange

def calcular_peso(tamaño, latencia_segundos):
    '''
    Calcula el peso en las aristas, utilizando el tamaño de la ventana
    y la latencia por cada medio
    '''
    return round(tamaño/latencia_segundos, 3)

def peso_nodo(tamaño):
    '''
    Esta función permite calcular el peso en cada arista a partir de 
    la formula, para calcular la banda ancha utilizando la función 
    creada, calcular_peso.
    '''
    pesos = []
    for i in range(9):
        latencia = randrange(1,59)
        valor_peso = calcular_peso(tamaño, latencia)
        pesos.append(valor_peso)

    return pesos