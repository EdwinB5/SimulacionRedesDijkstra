def convertir_paquete(mensaje, tamaño):
    '''
    Con el mensaje, lo divide y almacena en un arreglo en
    tamaños iguales según el tamaño indicado por el usuario
    devuelve un arreglo
    '''
    paquetes = []
    inicio = 0
    fin = tamaño

    for i in range(len(mensaje)):
        if len(mensaje) < tamaño:
            paquetes.append(mensaje)
            break

        if fin > len(mensaje):
            break
        tmp = mensaje[inicio:fin]
        paquetes.append(tmp)

        inicio = fin
        fin += tamaño

    if len(mensaje) % tamaño != 0:
        paquetes.append(mensaje[inicio:])

    return paquetes

def rearmar_paquete(paquetes):
        '''
        A partir de la lista de paquetes, reensambla el mensaje
        devolviendo una cadena de carácteres
        '''
        mensaje_rearmado = ''.join(paquetes)
        return mensaje_rearmado

if __name__ == '__main__':
    '''mensaje = 'hola'
                tamaño = 2
                lista = convertir_paquete(mensaje, tamaño)
                texto_rearmado = rearmar_paquete(lista)
                print(f'La lista es {lista}')
                print(f'El mensaje rearmado es: {texto_rearmado}')'''
    mensaje = 'hola'
    contenido = [1, '']
    contenido[1] += mensaje
    print(contenido)

    

    