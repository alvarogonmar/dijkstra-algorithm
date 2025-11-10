class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.graph} # Diccionario con las distancias mas cortas
        distances[start] = 0 # El nodo inicizl le ponemos distancia de 0 porque no hay distancia hacia el mismo

        visited = [] # Array para guardar los nodos que ya visitamos

        previous_path =  {node: None for node in self.graph} # Guardar el camino anterior

        while len(visited) < len(self.graph): # Mientras no hemos visitado todos los nodos
            min_non_visited_node = None
            for node in self.graph:
                if node not in visited:
                    if min_non_visited_node is None or distances[node] < distances[min_non_visited_node]: # buscar el nodo no visitado con la distancia mas corta
                        min_non_visited_node = node
            
            if min_non_visited_node is None: # si ya no hay nodos por visitar terminar el for
                break
        
            for neighbor, weight in self.graph[min_non_visited_node]: # recorrer vecinos del nodo actual
                new_distance = distances[min_non_visited_node] + weight # nueva distancia al vecino tomando en cuenta el nodo actual
                if new_distance < distances[neighbor]: # si la nueva distancia es menor que la que ya teniamos
                    distances[neighbor] = new_distance # guardar la nueva distancia
                    previous_path[neighbor] = min_non_visited_node
            visited.append(min_non_visited_node) # marcar el nodo como visitado
        return distances, previous_path

    def print_graph(self):
        print("Grafo:\n")
        for node, edges in self.graph.items():
            print(f"{node}: {edges}")
        