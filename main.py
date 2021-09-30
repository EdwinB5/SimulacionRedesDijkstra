from Dijkstra import Dijkstra
from Paquete import Paquete
from Entrada import leer_entrada, leer_mensaje

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