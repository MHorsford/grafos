def fleury(graph, start):
    """
    Implementa o algoritmo de Fleury para encontrar um ciclo Euleriano em um grafo não direcionado.

    Parâmetros:
    - graph (dict): Dicionário de adjacência. Formato: {vértice: {vizinho: quantidade_arestas}}
    - start (hashable): Vértice inicial do ciclo.

    Retorna:
    - list: Lista com o caminho do ciclo Euleriano.
    """

    # Função auxiliar que verifica se a aresta (u, v) é uma ponte
    def is_bridge(u, v):
        # Se há múltiplas arestas, não pode ser ponte
        if graph[u][v] > 1:
            return False

        # Remove temporariamente a aresta
        original = graph[u][v]
        graph[u][v] -= 1
        graph[v][u] -= 1

        # Verifica conectividade com DFS
        visited = set()
        stack = [u]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                for neighbor, count in graph[node].items():
                    if count > 0 and neighbor not in visited:
                        stack.append(neighbor)

        # Restaura a aresta
        graph[u][v] += 1
        graph[v][u] += 1

        # Se 'v' ficou inacessível, a aresta é ponte
        return v not in visited

    # Cria cópia segura do grafo
    from copy import deepcopy
    graph = deepcopy(graph)

    # Verifica graus pares para todos os vértices
    for node in graph:
        grau = sum(graph[node].values())
        if grau % 2 != 0:
            raise ValueError(f"Grafo não Euleriano: vértice '{node}' tem grau ímpar.")

    # Inicializa estruturas
    path = [start]
    current = start
    total_edges = sum(sum(neigh.values()) for neigh in graph.values()) // 2  # Arestas totais

    for _ in range(total_edges):
        # Vizinhos com arestas disponíveis
        neighbors = [v for v in graph[current] if graph[current][v] > 0]

        if not neighbors:
            break  # Sem arestas restantes

        # Escolhe estratégia baseada no número de vizinhos
        if len(neighbors) == 1:
            next_vertex = neighbors[0]
        else:
            # Prefere arestas que não são pontes
            for v in neighbors:
                if not is_bridge(current, v):
                    next_vertex = v
                    break
            else:
                next_vertex = neighbors[0]  # Usa qualquer aresta se todas forem pontes

        # Atualiza caminho e remove aresta
        path.append(next_vertex)
        graph[current][next_vertex] -= 1
        graph[next_vertex][current] -= 1
        current = next_vertex

    return path


# ========== EXEMPLOS DE TESTE ==========
if __name__ == "__main__":
    # Exemplo 1: Ciclo Euleriano (triângulo)
    grafo_triangulo = {
        'A': {'B': 1, 'C': 1},
        'B': {'A': 1, 'C': 1},
        'C': {'A': 1, 'B': 1}
    }
    print("Triângulo:", fleury(grafo_triangulo, 'A'))  # Ex: ['A','B','C','A']

    # Exemplo 2: Grafo com arestas paralelas
    grafo_paralelo = {
        'A': {'B': 2},
        'B': {'A': 2}
    }
    print("Arestas Paralelas:", fleury(grafo_paralelo, 'A'))  # Ex: ['A','B','A']

    # Exemplo 3: Grafo inválido (graus ímpares)
    grafo_estrela = {
        'A': {'B': 1, 'C': 1},
        'B': {'A': 1},
        'C': {'A': 1}
    }
    try:
        print("Estrela:", fleury(grafo_estrela, 'A'))
    except ValueError as e:
        print("Estrela:", e)  # Erro esperado