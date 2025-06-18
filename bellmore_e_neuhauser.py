def bellmore_neuhauser(cost_matrix):
    """
    Implementa a heurística de Bellmore e Neuhauser para o Problema do Caixeiro Viajante (TSP).

    Esta heurística constrói a solução em etapas:
    1. Inicia com um circuito de 2 ou 3 cidades
    2. Seleciona iterativamente a cidade com maior "arrependimento" (diferença entre os dois melhores pontos de inserção)
    3. Insere a cidade no local que causa o menor aumento no custo total

    Parâmetros:
    cost_matrix : list[list[float]]
        Matriz de custos/distancias entre cidades (deve ser quadrada e simétrica)

    Retorno:
    total_cost : float
        Custo total do circuito encontrado
    tour : list[int]
        Ordem das cidades no circuito (começa e termina na mesma cidade)
    """

    n = len(cost_matrix)
    if n == 0:
        return 0, []

    # Controle de cidades visitadas e circuito inicial
    visited = [False] * n
    tour = [0]  # Começa pela cidade 0
    visited[0] = True

    # Caso trivial: 1 cidade
    if n == 1:
        return 0, tour

    # ETAPA 1: Construção do circuito inicial
    # --------------------------------------------------
    # Passo 1: Encontra cidade mais próxima da origem
    min_cost, candidate = float('inf'), None
    for j in range(1, n):
        if cost_matrix[0][j] < min_cost:
            min_cost = cost_matrix[0][j]
            candidate = j

    # Fallback para grafos desconexos
    if candidate is None:
        candidate = 1

    visited[candidate] = True

    # Caso especial: 2 cidades
    if n == 2:
        tour.append(candidate)
    else:
        # Passo 2: Seleciona terceira cidade para minimizar o circuito
        min_cost2, candidate2 = float('inf'), None
        for k in range(1, n):
            if visited[k]:
                continue
            # Custo do caminho: 0 -> candidate -> k -> 0
            new_cost = cost_matrix[candidate][k] + cost_matrix[k][0]
            if new_cost < min_cost2:
                min_cost2 = new_cost
                candidate2 = k

        # Fallback se não encontrou cidade válida
        if candidate2 is None:
            for k in range(1, n):
                if not visited[k]:
                    candidate2 = k
                    break

        visited[candidate2] = True
        tour.extend([candidate, candidate2])  # Circuito inicial: [0, candidate, candidate2]

    # ETAPA 2: Inserção por arrependimento
    # --------------------------------------------------
    unvisited_count = n - len(tour)
    while unvisited_count > 0:
        regrets = {}

        # Calcula arrependimento para cada cidade não visitada
        for u in range(n):
            if visited[u]:
                continue

            # Coleta distâncias para todas as cidades no circuito
            dists = [cost_matrix[u][city] for city in tour]
            dists.sort()

            # Arrependimento = diferença entre 1ª e 2ª melhores conexões
            regret = dists[1] - dists[0] if len(dists) > 1 else 0
            regrets[u] = regret

        # Seleciona cidade com menor arrependimento (desempate por menor índice)
        u = min(regrets.keys(), key=lambda x: (regrets[x], x))

        # Encontra posição ótima para inserção
        min_increase = float('inf')
        best_pos = -1
        m = len(tour)

        for i in range(m):
            # Cidades consecutivas no circuito atual
            city_i = tour[i]
            city_j = tour[(i + 1) % m]

            # Custo atual: city_i -> city_j
            # Novo custo: city_i -> u -> city_j
            cost_increase = cost_matrix[city_i][u] + cost_matrix[u][city_j] - cost_matrix[city_i][city_j]

            if cost_increase < min_increase:
                min_increase = cost_increase
                best_pos = i

        # Insere nova cidade entre city_i e city_j
        tour.insert(best_pos + 1, u)
        visited[u] = True
        unvisited_count -= 1

    # Calcula custo total do circuito fechado
    total_cost = 0
    for i in range(len(tour)):
        total_cost += cost_matrix[tour[i]][tour[(i + 1) % len(tour)]]

    return total_cost, tour


# -------------------------- EXEMPLO DE USO ---------------------------
if __name__ == "__main__":
    # Matriz de custos simétrica (4 cidades)
    cost_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    total_cost, tour = bellmore_neuhauser(cost_matrix)

    print(f"Custo total: {total_cost}")
    print(f"Circuito: {' → '.join(map(str, tour))} → {tour[0]}")
    # Saída esperada para este exemplo:
    # Custo total: 80
    # Circuito: 0 → 1 → 3 → 2 → 0