def bellman_ford(vertices, arestas, fonte):
    """
    Algoritmo de Bellman-Ford para encontrar os menores caminhos em grafos,
    mesmo com arestas de peso negativo.

    Args:
        vertices (list): Lista dos vértices do grafo.
        arestas (list): Lista de tuplas (u, v, peso) representando as arestas.
        fonte (int): Vértice de origem.

    Returns:
        dict: Dicionário com as menores distâncias da fonte para cada vértice.
              Retorna None se houver ciclo negativo.
    """
    # Inicializa distâncias
    dist = {v: float('inf') for v in vertices}
    dist[fonte] = 0

    # Relaxa arestas |V|-1 vezes
    for _ in range(len(vertices) - 1):
        atualizado = False
        for u, v, peso in arestas:
            if dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                atualizado = True
        # Se não houve atualização, pode parar cedo
        if not atualizado:
            break

    # Verifica ciclo negativo
    for u, v, peso in arestas:
        if dist[u] + peso < dist[v]:
            print("O grafo contém ciclo negativo!")
            return None

    return dist

# EXEMPLOS DE USO

def testar_exemplo(nome, vertices, arestas, fonte):
    print(f"\n=== {nome} ===")
    resultado = bellman_ford(vertices, arestas, fonte)
    print("Resultado:", resultado)


if __name__ == "__main__":

    vertices1 = [0, 1, 2, 3, 4]
    arestas1 = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (1, 4, 2),
        (3, 2, 5),
        (3, 1, 1),
        (4, 3, -3),
    ]

    vertices2 = [0, 1, 2, 3]
    arestas2 = [
        (0, 1, 4),
        (0, 2, 5),
        (1, 2, -2),
        (2, 3, 3)
    ]

    vertices3 = [0, 1, 2]
    arestas3 = [
        (0, 1, 1),
        (1, 2, -1),
        (2, 0, -1) 
    ]

    vertices4 = [0, 1, 2, 3, 4, 5]
    arestas4 = [
        (0, 1, 6),
        (0, 2, 5),
        (0, 3, 5),
        (1, 4, -1),
        (2, 1, -2),
        (2, 4, 1),
        (3, 2, -2),
        (3, 5, -1),
        (4, 5, 3)
    ]

    # Rodando os exemplos
    testar_exemplo("Exemplo 1", vertices1, arestas1, 0)
    testar_exemplo("Exemplo 2", vertices2, arestas2, 0)
    testar_exemplo("Exemplo 3", vertices3, arestas3, 0)
    testar_exemplo("Exemplo 4", vertices4, arestas4, 0)
