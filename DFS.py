"""
    Nome da Tarefa: Implementação do Alg. DFS

    Descrição: Baseado na representação de grafos (por matrizes de adjacência ou listas de adjacência)
    implementadas no trabalho anterior, implemente o Alg. DFS de Cormen et. al. Obs.: O grafo deve ser
    pré-informado.
"""
class DFS_Runner_List:

    def __init__(self, graph):
        self.graph = graph
        self.vertices = list(graph.keys())

        # Estruturas para o estado dos vértices
        self.color = {}   # Cor de cada vértice (BRANCO, CINZA, PRETO)
        self.pi = {}      # Predecessores
        self.d = {}       # Tempo de descoberta
        self.f = {}       # Tempo de finalização
        self.time = 0     # Contador global de tempo

    def _initialize(self):
        for vertex in self.vertices:
            self.color[vertex] = 'BRANCO'
            self.pi[vertex] = None
        self.time = 0

    def run_dfs(self):
        self._initialize()
        for u in sorted(self.vertices):  # Ordem determinística
            if self.color[u] == 'BRANCO':
                self._dfs_visit(u)
        return self.get_results()

    def _dfs_visit(self, u):
        self.time += 1
        self.d[u] = self.time
        self.color[u] = 'CINZA'

        for v in sorted(self.graph.get(u, [])):  # Itera sobre vizinhos
            if self.color[v] == 'BRANCO':
                self.pi[v] = u
                self._dfs_visit(v)

        self.color[u] = 'PRETO'
        self.time += 1
        self.f[u] = self.time

    def get_results(self):
        return {
            "tempo_descoberta": self.d,
            "tempo_finalizacao": self.f,
            "predecessores": self.pi
        }

if __name__ == "__main__":
    # Grafo de exemplo com ciclo e componentes desconexos
    grafo = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': ['A'],  # cria um ciclo
        'E': ['F', 'G'],
        'F': ['G'],
        'G': [],
        'H': []
    }

    dfs = DFS_Runner_List(grafo)
    resultados = dfs.run_dfs()

    print("Tempo de Descoberta (d):")
    print(resultados["tempo_descoberta"])

    print("\nTempo de Finalização (f):")
    print(resultados["tempo_finalizacao"])

    print("\nPredecessores (π):")
    print(resultados["predecessores"])

