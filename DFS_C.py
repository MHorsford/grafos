"""
    Nome da Tarefa: Empregando o Alg. DFS para encontrar um Ciclo

    Descrição: Altere o Alg. DFS de Cormen et al. para  encontrar um ciclo  e apresentar o ciclo
    encontrado. O algoritmo deve parar assim que encontrar o primeiro ciclo. O Algortimo deve ser
    implementado e testado.
"""

from collections import defaultdict

class DFS_Cycle_Finder:
    """
    Implementa o algoritmo DFS modificado para encontrar o primeiro ciclo
    em um grafo direcionado, parar a execução e retornar o ciclo.
    """
    def __init__(self, graph):
        self.graph = graph
        self.vertices = list(graph.keys())
        self.color = {}  # Estado de cada vértice: BRANCO, CINZA, PRETO
        self.pi = {}     # Dicionário de predecessores para reconstruir o ciclo

    def _initialize(self):
        """Inicializa as estruturas de dados para cada execução."""
        for vertex in self.vertices:
            self.color[vertex] = 'BRANCO'
            self.pi[vertex] = None

    def find_first_cycle(self):
        """
        Executa a busca em profundidade no grafo para encontrar um ciclo.
        Retorna uma lista de nós representando o primeiro ciclo encontrado,
        ou None se o grafo for acíclico.
        """
        self._initialize()
        # Itera sobre todos os vértices para lidar com grafos desconexos
        for u in sorted(self.vertices):  # Ordem determinística
            if self.color[u] == 'BRANCO':
                # Inicia uma nova árvore DFS
                cycle = self._dfs_visit_cycle(u)
                if cycle:
                    # Se um ciclo foi retornado, interrompe a busca e o retorna
                    return cycle
        return None  # Nenhum ciclo encontrado em todo o grafo

    def _dfs_visit_cycle(self, u):
        """
        Função recursiva da DFS que detecta e reconstrói o ciclo.
        """
        self.color[u] = 'CINZA'  # Nó sendo visitado (na pilha de recursão)

        for v in sorted(self.graph.get(u, [])):  # Vizinhos de u
            if self.color[v] == 'CINZA':
                # Aresta de retorno detectada: ciclo!
                reconstructed_cycle = [v]
                current = u
                while current != v:
                    reconstructed_cycle.insert(1, current)
                    current = self.pi[current]
                return reconstructed_cycle

            if self.color[v] == 'BRANCO':
                self.pi[v] = u
                cycle_found = self._dfs_visit_cycle(v)
                if cycle_found:
                    return cycle_found  # Propaga ciclo encontrado

        self.color[u] = 'PRETO'  # Finaliza visita
        return None

if __name__ == "__main__":
    # Teste 1: Grafo com ciclo simples
    grafo_com_ciclo = {
        'A': ['B'],
        'B': ['D'],
        'C': [],
        'D': ['A']
    }

    print("Teste 1: Grafo com ciclo simples")
    finder1 = DFS_Cycle_Finder(grafo_com_ciclo)
    ciclo1 = finder1.find_first_cycle()
    print(f"Ciclo encontrado: {ciclo1}\n")

    # Teste 2: Grafo sem ciclo (DAG)
    grafo_sem_ciclo = {
        'A': ['B'],
        'B': ['C'],
        'C': [],
        'D': []
    }

    print("Teste 2: Grafo sem ciclo (DAG)")
    finder2 = DFS_Cycle_Finder(grafo_sem_ciclo)
    ciclo2 = finder2.find_first_cycle()
    print(f"Ciclo encontrado: {ciclo2}\n")

    # Teste 3: Grafo Usado no DFS sem detecção de ciclos
    grafo_complexo = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': ['A'],  # cria um ciclo
        'E': ['F', 'G'],
        'F': ['G'],
        'G': [],
        'H': []
    }

    print("Teste 3: Grafo Do Algoritmo DFS sem detecção de Ciclos")
    finder3 = DFS_Cycle_Finder(grafo_complexo)
    ciclo3 = finder3.find_first_cycle()
    print(f"Ciclo encontrado: {ciclo3}")
