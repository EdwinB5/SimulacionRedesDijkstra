from Dijkstra import Dijkstra
from Paquete import Paquete

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

if __name__ == '__main__':
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    grafo = {
        'A': {'B': 5, 'E': 3, 'F': 18},
        'B': {'A': 5, 'C': 1, 'D': 3},
        'C': {'B': 1, 'G': 8},
        'D': {'B': 3, 'E': 14},
        'E': {'D': 14, 'G': 4, 'A': 3},
        'F': {'A': 18, 'G': 4},
        'G': {'E': 4, 'C': 8, 'F': 4}
    }

    num_paquete = 1

    # Recibir valores del usuario
    mensaje, tamaño = leer_mensaje()
    vertice_inicio, vertice_fin = leer_entrada(vertices)
    print('-'*40)
    print()

    # Convertir en paquete lo digitado por el usuario
    paquetes = Paquete(mensaje, tamaño)
    lista_paquetes = paquetes.convertir_paquete()
    paquetes_recibidos = []

    # Instanciar clase Dijkstra
    dijkstra = Dijkstra(vertices, grafo)

    # Envio de paquetes
    for paquete in lista_paquetes:
        print(f'Paquete número: {num_paquete} ')
        print('-'*40)
        print(f'Contenido del paquete: {paquete}')
        print('-'*40)
        ant, vist, paquete = dijkstra.buscar_ruta(vertice_inicio, vertice_fin, paquete)
        print(f'La distancia entre {vertice_inicio} a {vertice_fin} es: {vist[vertice_fin]}')
        ruta = dijkstra.generar_ruta(ant, vertice_inicio, vertice_fin)
        print(f'La ruta de {vertice_inicio} a {vertice_fin} es:', ' -> '.join(ruta))
        paquetes_recibidos.extend(paquete)
        print('-'*40)
        print()
        num_paquete += 1

    # Imprimir reensamble del mensaje  
    print(f'El mensaje rearmado es: {paquetes.rearmar_paquete(paquetes_recibidos)}')
    print(paquetes_recibidos)
    print('-'*40) 