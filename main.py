from Dijkstra import Dijkstra
from Paquete import Paquete
from Entrada import leer_entrada, leer_mensaje
from random import randrange

def calcular_peso(tamaño, latencia_segundos):
    '''
    Calcula el peso en las aristas, utilizando el tamaño de la ventana
    y la latencia por cada medio
    '''
    return round(tamaño/latencia_segundos, 2)

def peso_nodo(vertices, tamaño):
    '''
    Esta función permite calcular el peso en cada arista a partir de 
    la formula, para calcular la banda ancha utilizando la función 
    creada, calcular_peso.
    '''
    pesos = []
    for vertice in vertices:
        valor_peso = calcular_peso(tamaño, randrange(1,20))
        pesos.append(valor_peso)

    return pesos
    
if __name__ == '__main__':
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    num_paquete = 1

    # Recibir valores del usuario
    mensaje, tamaño = leer_mensaje()
    vertice_inicio, vertice_fin = leer_entrada(vertices)
    print()

    # Convertir en paquete lo digitado por el usuario
    paquetes = Paquete(mensaje, tamaño)
    lista_paquetes = paquetes.convertir_paquete()
    paquetes_recibidos = []

    # Envio de paquetes
    for paquete in lista_paquetes:
        # A[0], B[1], C[2], D[3], E[4], F[5], G[6]
        x = peso_nodo(vertices, tamaño)

        grafo = {
        'A': {'B': x[1], 'E': x[4], 'F': x[5]},
        'B': {'A': x[0], 'C': x[2], 'D': x[3]},
        'C': {'B': x[1], 'G': x[6]},
        'D': {'B': x[1], 'E': x[4]},
        'E': {'D': x[3], 'G': x[6], 'A': x[0]},
        'F': {'A': x[0], 'G': x[6]},
        'G': {'E': x[4], 'C': x[2], 'F': x[5]}
        }

        # Instanciar clase Dijkstra
        dijkstra = Dijkstra(vertices, grafo)
        print('#'*60)
        print('-'*60)
        print(f'- Paquete número: {num_paquete} ')
        print('-'*60)
        print(f'- Contenido del paquete: {paquete}')
        print('-'*60)
        ant, vist, paquete = dijkstra.buscar_ruta(vertice_inicio, vertice_fin, paquete)
        print(f'- La distancia entre {vertice_inicio} a {vertice_fin} es: {vist[vertice_fin]}')
        ruta = dijkstra.generar_ruta(ant, vertice_inicio, vertice_fin)
        print(f'- La ruta de {vertice_inicio} a {vertice_fin} es:', ' -> '.join(ruta))
        paquetes_recibidos.extend(paquete)
        print('-'*60)
        num_paquete += 1

    # Imprimir reensamble del mensaje
    print('#'*60)
    print(f'- Los paquetes recibidos son: {paquetes_recibidos}')  
    print(f'- El mensaje rearmado es: {paquetes.rearmar_paquete(paquetes_recibidos)}')