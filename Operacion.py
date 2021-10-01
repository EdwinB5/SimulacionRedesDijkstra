from random import randrange

def calcular_peso(tamaño, bits_segundo):
    '''
    Calcula el peso en las aristas (latencia), utilizando el tamaño de la 
    ventana y los bits por segundo, para calcular la latencia
    '''
    return round(tamaño/bits_segundo, 3)

def peso_nodo(tamaño):
    '''
    Esta función permite calcular el peso en cada arista a partir de 
    la formula, para calcular la banda ancha utilizando la función 
    creada, calcular_peso.
    '''
    pesos = []
    for i in range(9):
        bits_segundo = randrange(1,59)
        valor_peso = calcular_peso(tamaño, bits_segundo)
        pesos.append(valor_peso)

    return pesos