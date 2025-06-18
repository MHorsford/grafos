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

        # Verifica se o grafo continua conectado (BFS)
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

        # Se o vértice v não foi visitado, a aresta era essencial → ponte
        return v not in visited

    # Cria uma cópia do grafo para não alterar o original
    from copy import deepcopy
    graph = deepcopy(graph)

    # Verifica se todos os vértices têm grau par
    for node in graph:
        grau = sum(graph[node].values())
        if grau % 2 != 0:
            raise ValueError(f"O grafo não possui ciclo Euleriano: vértice '{node}' tem grau ímpar.")

    # Inicializa o caminho e o vértice atual
    path = [start]
    current = start

    # Conta o total de arestas (dividido por 2 pois é grafo não direcionado)
    total_edges = sum(sum(neigh.values()) for neigh in graph.values()) // 2

    for _ in range(total_edges):
        # Pega vizinhos com arestas restantes
        neighbors = [v for v in graph[current] if graph[current][v] > 0]

        if not neighbors:
            break  # Nenhuma aresta disponível

        # Se só tem um vizinho, segue direto
        if len(neighbors) == 1:
            next_vertex = neighbors[0]
        else:
            # Escolhe uma aresta que não seja ponte
            for v in neighbors:
                if not is_bridge(current, v):
                    next_vertex = v
                    break
            else:
                # Se todas são pontes, pega a primeira mesmo
                next_vertex = neighbors[0]

        # Atualiza o caminho e remove a aresta usada
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
    print("Triângulo:", fleury(grafo_triangulo, 'A'))  # Deve retornar um ciclo completo

    # Exemplo 2: Grafo com arestas paralelas (válido)
    grafo_paralelo = {
        'A': {'B': 2},
        'B': {'A': 2}
    }
    print("Paralelas:", fleury(grafo_paralelo, 'A'))

    # Exemplo 3: Grafo inválido (graus ímpares)
    grafo_estrela = {
        'A': {'B': 1, 'C': 1},
        'B': {'A': 1},
        'C': {'A': 1}
    }
    try:
        print("Estrela:", fleury(grafo_estrela, 'A'))
    except ValueError as e:
        print("Estrela:", e)  # Deve informar que não há ciclo Euleriano
