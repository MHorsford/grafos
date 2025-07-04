"""
    Nome da Tarefa: Implementação do Alg. BFS e Caminho

    Descrição: Baseado na representação de grafos (por matrizes de adjacência ou listas de adjacência)
    implementadas no trabalho anterior, implemente o Alg. BFS de Cormen et. al.  Adicionalmente, a fim
    de encontrar um determinado caminho, o usuário deve informar o vértice inicial e um vértice qualquer.
    O programa deve então retornar o tamanho do caminho entre o vértice incial e o outro vértice.
"""

import collections
import math

class GraphAdjList:
    def __init__(self, vertices, directed=False):
        self.vertices = set(vertices)
        self.adj = {v: [] for v in vertices}
        self.directed = directed

    def add_edge(self, u, v):
        if u not in self.vertices or v not in self.vertices:
            raise ValueError("Vértices devem pertencer ao grafo.")
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def get_neighbors(self, u):
        return self.adj.get(u, [])


# Algoritmo BFS (CLRS)
def bfs(graph, start_node):
    if start_node not in graph.vertices:
        raise ValueError("O vértice inicial não pertence ao grafo.")

    color = {v: 'WHITE' for v in graph.vertices}
    distance = {v: math.inf for v in graph.vertices}
    predecessor = {v: None for v in graph.vertices}

    color[start_node] = 'GRAY'
    distance[start_node] = 0
    queue = collections.deque([start_node])

    while queue:
        u = queue.popleft()
        for v in graph.get_neighbors(u):
            if color[v] == 'WHITE':
                color[v] = 'GRAY'
                distance[v] = distance[u] + 1
                predecessor[v] = u
                queue.append(v)
        color[u] = 'BLACK'

    return distance, predecessor


# Reconstrução do Caminho
def reconstruct_path(predecessor, start_node, end_node):
    if predecessor.get(end_node) is None and start_node != end_node:
        return None
    path = []
    current_node = end_node
    while current_node is not None:
        path.append(current_node)
        current_node = predecessor[current_node]
    return path[::-1]


# Programa principal
if __name__ == "__main__":
    # Definir os vértices e arestas do grafo
    vertices = ["A", "B", "C", "D", "E", "F"]
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("E", "F")]

    # Criar o grafo
    g = GraphAdjList(vertices)

    for u, v in edges:
        g.add_edge(u, v)

    print("Grafo criado com os vértices:", sorted(g.vertices))

    try:
        start_vertex = input("Digite o vértice inicial: ").strip().upper()
        end_vertex = input("Digite o vértice final: ").strip().upper()

        if start_vertex not in g.vertices or end_vertex not in g.vertices:
            print("Erro: Um ou ambos os vértices não existem no grafo.")
        else:
            distances, predecessors = bfs(g, start_vertex)
            path_length = distances[end_vertex]

            if path_length == math.inf:
                print(f"Não existe caminho entre {start_vertex} e {end_vertex}.")
            else:
                print(f"O comprimento do caminho mais curto de {start_vertex} a {end_vertex} é: {path_length}")
                path = reconstruct_path(predecessors, start_vertex, end_vertex)
                if path:
                    print("O caminho é:", " -> ".join(path))

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
