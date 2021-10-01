from Dijkstra import Dijkstra
from Paquete import Paquete
from Entrada import leer_entrada, leer_mensaje
from Operacion import peso_nodo
    
if __name__ == '__main__':
    vertices = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
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
        x = peso_nodo(tamaño)

        grafo = {
        'A': {'B': x[0], 'E': x[1], 'F': x[2]},
        'B': {'A': x[0], 'C': x[3], 'D': x[4]},
        'C': {'B': x[3], 'G': x[7]},
        'D': {'B': x[4], 'E': x[5]},
        'E': {'D': x[5], 'G': x[6], 'A': x[1]},
        'F': {'A': x[2], 'G': x[8]},
        'G': {'E': x[6], 'C': x[7], 'F': x[8]}
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
        print(f'- La distancia (latencia) entre {vertice_inicio} a {vertice_fin} es: {vist[vertice_fin]}')
        ruta = dijkstra.generar_ruta(ant, vertice_inicio, vertice_fin)
        print(f'- La ruta de {vertice_inicio} a {vertice_fin} es:', ' -> '.join(ruta))
        paquetes_recibidos.extend(paquete)
        print('-'*60)
        num_paquete += 1
        #print(dijkstra.grafo)

    # Imprimir reensamble del mensaje
    print('#'*60)
    print(f'- Los paquetes recibidos son: {paquetes_recibidos}')  
    print(f'- El mensaje rearmado es: {paquetes.rearmar_paquete(paquetes_recibidos)}')