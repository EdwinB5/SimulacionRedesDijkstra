class Dijkstra:
	'''
	Algoritmo de Dijkstra
	'''
	def __init__(self, vertices, grafo):
		'''
		Constructor, recibe los vertices y el grafo 
		completo
		'''
		self.vertices = vertices
		self.grafo = grafo

	def buscar_ruta(self, inicio, fin, mensaje):
		'''
		Busca la ruta según los vertices introducidos,
		haciendo un recorrido por todo el grafo
		'''
		no_visitado = {n: float('inf') for n in self.vertices}
		no_visitado[inicio] = 0
		visitado = {}
		anteriores = {}
		paquetes = {n: [] for n in self.vertices}
		while no_visitado:

			vertice_minimo = min(no_visitado, key=no_visitado.get)
			for anterior, contenido in self.grafo.get(vertice_minimo, {}).items():
				if anterior in visitado:
					continue
				# print(self.grafo[vertice_minimo].get(anterior, float('inf')))
				distancia = no_visitado[vertice_minimo] + self.grafo[vertice_minimo].get(anterior, float('inf'))
				if distancia < no_visitado[anterior]:
					no_visitado[anterior] = distancia
					anteriores[anterior] = vertice_minimo
			visitado[vertice_minimo] = no_visitado[vertice_minimo]
			no_visitado.pop(vertice_minimo)
			if vertice_minimo == fin:
				paquetes[vertice_minimo].append(mensaje)
				paquete_entregado = f"{vertice_minimo}:{paquetes[vertice_minimo]}"

		return anteriores, visitado, paquete_entregado

	@staticmethod
	def generar_ruta(anteriores, inicio, fin):
		'''
		Método estático del algoritmo, recibe los 
		vertices anteriores, añadidos durante la 
		búsqueda de la ruta, el vertice inicial y final
		'''
		ruta = [fin]
 
		while True:
			llave = anteriores[ruta[0]]
			ruta.insert(0, llave)
			if llave == inicio:
				break
		return ruta