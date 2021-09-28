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

	def buscar_ruta(self, inicio, fin):
		'''
		Busca la ruta según los vertices introducidos,
		haciendo un recorrido por todo el grafo
		'''
		no_visitado = {n: float('inf') for n in self.vertices}
		no_visitado[inicio] = 0
		visitado = {}
		anteriores = {}
		while no_visitado:
			vertice_minimo = min(no_visitado, key=no_visitado.get)
			for anterior, contenido in self.grafo.get(vertice_minimo, {}).items():
				if anterior in visitado:
					continue
				distancia = no_visitado[vertice_minimo] + self.grafo[vertice_minimo].get(anterior, float('inf'))
				if distancia < no_visitado[anterior]:
					no_visitado[anterior] = distancia
					anteriores[anterior] = vertice_minimo
			visitado[vertice_minimo] = no_visitado[vertice_minimo]
			no_visitado.pop(vertice_minimo)
			if vertice_minimo == fin:
				break

		return anteriores, visitado

	@staticmethod
	def generar_ruta(anteriores, inicio, fin):
		'''
		Método estático del algoritmo, recibe los 
		vertices anteriores, añadidos durante la 
		búsqueda de la ruta, el vertice inicial
		y final
		'''
		ruta = [fin]
 
		while True:
			llave = anteriores[ruta[0]]
			ruta.insert(0, llave)
			if llave == inicio:
				break
		return ruta

if __name__ == '__main__':
	input_vertices = ("A", "B", "C", "D", "E", "F", "G")
	input_graph = {
        "A": {"B": 5, "D": 3, "E": 12, "F": 5},
        "B": {"A": 5, "D": 1, "G": 2},
        "C": {"E": 1, "F": 16, "G": 2},
        "D": {"A": 3, "B": 1, "E": 1, "G": 1},
        "E": {"A": 12, "C": 1, "D": 1, "F": 2},
        "F": {"A": 5, "C": 16, "E": 2},
        "G": {"B": 2, "C": 2, "D": 1}
    }
	start_vertex = "F"
	end_vertex= "E"
    
	dijkstra = Dijkstra(input_vertices, input_graph)
	p, v = dijkstra.buscar_ruta(start_vertex, end_vertex)
	print(v)
	print(p)
	    
	print("Distance from %s to %s is: %.2f" % (start_vertex, end_vertex, v[end_vertex]))
	se = dijkstra.generar_ruta(p, start_vertex, end_vertex)
	print(se)
	print("Path from %s to %s is: %s" % (start_vertex, end_vertex, " -> ".join(se)))
    