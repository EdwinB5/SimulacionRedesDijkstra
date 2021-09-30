def leer_entrada(vertices):
    '''
    Esta función lee la entrada del usuario y controla las excepciones
    '''
    while True:
        print(f'Nodos en el programa:\n{vertices}')
        inicio = str(input('Introduzca el nodo inicial: ')).upper().strip()
        fin = str(input('Introduzca el nodo final: ')).upper().strip()
        if inicio in vertices and fin in vertices:
            break
        else:
            print('-'*40)
            print('Por favor, digite nodos validos...')
            print('-'*40)

    return inicio, fin

def leer_mensaje():
    '''
    Esta función lee el mensaje que sera enviada a través de la
    red de nodos
    '''
    print('-'*45)
    print('Bienvenido al programa de simulación de Dijkstra')
    print('-'*45)

    texto = str(input('Digite el mensaje que desea enviar al nodo: '))
    while True:
        try:
            tamaño = int(input('Digite el tamaño de los paquetes: '))
            if tamaño > len(texto):
                tamaño = len(texto)
            break
        except:
            print('-'*40)
            print('Por favor, digite un tamaño válido...')
            print('-'*40)
    return texto, tamaño