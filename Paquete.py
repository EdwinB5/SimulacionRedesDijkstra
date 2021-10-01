class Paquete:
    '''
    Esta clase manipula el mensaje, convirtiendolo en 
    paquetes del mismo tamaño, para ser enviados por la red
    '''
    def __init__(self, mensaje, tamaño):
        '''
        Constructor, recibe el mensaje y el tamaño de los paquetes
        (ventana)
        '''
        self.mensaje = mensaje
        self.tamaño = tamaño

    def convertir_paquete(self):
        '''
        Con el mensaje, lo divide y almacena en un arreglo en
        tamaños iguales según el tamaño indicado por el usuario
        devuelve un arreglo
        '''
        paquetes = []
        inicio = 0
        fin = self.tamaño

        for i in range(len(self.mensaje)):
            if len(self.mensaje) < self.tamaño:
                paquetes.append(self.mensaje)
                break
            if fin > len(self.mensaje):
                break
            tmp = self.mensaje[inicio:fin]
            paquetes.append(tmp)

            inicio = fin
            fin += self.tamaño
        
        if len(self.mensaje) % self.tamaño != 0:
            paquetes.append(self.mensaje[inicio:])

        return paquetes
    
    @staticmethod
    def rearmar_paquete(paquetes):
        '''
        A partir de la lista de paquetes generada, reensambla el 
        mensaje devolviendo una cadena de carácteres
        '''
        mensaje_rearmado = ''.join(paquetes)
        return mensaje_rearmado
