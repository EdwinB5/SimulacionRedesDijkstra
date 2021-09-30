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
            print('-'*37)
            print('Por favor, digite nodos validos...')
            print('-'*37)

    return inicio, fin

def leer_mensaje():
    '''
    Esta función lee el mensaje que sera enviada a través de la
    red de nodos
    '''
    texto = str(input('Digite el mensaje que desea enviar al nodo: '))
    return texto


if __name__ == '__main__':
    mensaje = 'Holas'
    tamaño = 2
    paquetes = Paquete(mensaje, tamaño)
    lista_paquetes = paquetes.convertir_paquete()
    print(lista_paquetes)
    print(paquetes.rearmar_paquete(lista_paquetes))

    '''
    vertices = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    grafo = {
        'A': {'B': 5, 'E': 3, 'F': 18},
        'B': {'A': 5, 'C': 1, 'D': 3},
        'C': {'B': 1, 'G': 8},
        'D': {'B': 3, 'E': 14},
        'E': {'D': 14, 'G': 4, 'A': 3},
        'F': {'A': 18, 'G': 4},
        'G': {'E': 4, 'C': 8, 'F': 4}
    }
    vertice_inicio, vertice_fin = leer_entrada(vertices)

    dijkstra = Dijkstra(vertices, grafo) #Instancia dijkstra
    ant, vist = dijkstra.buscar_ruta(vertice_inicio, vertice_fin)
    print(f'La distancia entre {vertice_inicio} a {vertice_fin} es: {vist[vertice_fin]}')
    ruta = dijkstra.generar_ruta(ant, vertice_inicio, vertice_fin)
    print(f'La ruta de {vertice_inicio} a {vertice_fin} es:', ' -> '.join(ruta))
    '''
    
    