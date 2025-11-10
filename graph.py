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
        distances[start] = 0

        visited = [] # Array para guardar los nodos que ya visitamos

        previous_path =  {node: None for node in self.graph} # Guardar el camino anterior

        while len(visited) < len(self.graph): # Mientras no hemos visitado todos los nodos
            
