import matplotlib.pyplot as plt
import networkx as nx


class GraphMatrix:
    """Representação de grafo usando matriz de adjacências"""

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
        print(f"\n🔷 Grafo com Matriz de Adjacências criado ({num_vertices} vértices)")

    def add_edge(self, u, v):
        """Adiciona uma aresta entre dois vértices (não direcionado)"""
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.matrix[u][v] = 1
            self.matrix[v][u] = 1
            print(f"   ➕ Aresta adicionada: ({u} ↔ {v})")
        else:
            print(f"   ⚠️ Erro: Vértices inválidos ({u} ou {v})")

    def vertex_degree(self, v):
        """Calcula o grau do vértice (número de conexões)"""
        if 0 <= v < self.num_vertices:
            return sum(self.matrix[v])
        return -1

    def display(self):
        """Exibe a matriz de forma visual"""
        print("\nMATRIZ DE ADJACÊNCIAS:")
        print("   " + " ".join(str(i) for i in range(self.num_vertices)))
        for i, row in enumerate(self.matrix):
            print(f"{i} | {' '.join('●' if x else '○' for x in row)} |")
        print("Legenda: ● = conexão, ○ = sem conexão")

    def visualize(self):
        """Mostra uma representação gráfica do grafo"""
        G = nx.Graph()
        G.add_nodes_from(range(self.num_vertices))
        for i in range(self.num_vertices):
            for j in range(i + 1, self.num_vertices):
                if self.matrix[i][j]:
                    G.add_edge(i, j)

        plt.figure(figsize=(7, 6))
        plt.title("Representação do Grafo (Matriz)", fontsize=14)
        pos = nx.circular_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=800,
                node_color='#ff7979', edge_color='#5352ed',
                width=2, font_weight='bold')
        plt.show()


class GraphList:
    """Representação de grafo usando lista de adjacências"""

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
        print(f"\n🔶 Grafo com Lista de Adjacências criado ({num_vertices} vértices)")

    def add_edge(self, u, v):
        """Adiciona uma aresta entre dois vértices (não direcionado)"""
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
            print(f"   ➕ Aresta adicionada: ({u} ↔ {v})")
        else:
            print(f"   ⚠️ Erro: Vértices inválidos ({u} ou {v})")

    def vertex_degree(self, v):
        """Calcula o grau do vértice (número de conexões)"""
        if 0 <= v < self.num_vertices:
            return len(self.adj_list[v])
        return -1

    def display(self):
        """Exibe a lista de forma visual"""
        print("\nLISTA DE ADJACÊNCIAS:")
        for i, neighbors in enumerate(self.adj_list):
            print(f"Vértice {i}: → {' → '.join(map(str, neighbors))}" if neighbors else f"Vértice {i}: → Ø")

    def visualize(self):
        """Mostra uma representação gráfica do grafo"""
        G = nx.Graph()
        for i in range(self.num_vertices):
            for neighbor in self.adj_list[i]:
                if i < neighbor:
                    G.add_edge(i, neighbor)

        plt.figure(figsize=(7, 6))
        plt.title("Representação do Grafo (Lista)", fontsize=14)
        pos = nx.spring_layout(G, seed=42)
        nx.draw(G, pos, with_labels=True, node_size=800,
                node_color='#7bed9f', edge_color='#ff6b81',
                width=2, font_weight='bold')
        plt.show()


# Demonstração
if __name__ == "__main__":
    print("\n" + "=" * 55)
    print(" DEMONSTRAÇÃO DE REPRESENTAÇÃO DE GRAFOS ".center(55, '★'))
    print("=" * 55)

    # Criar estruturas
    gm = GraphMatrix(4)
    gl = GraphList(4)

    # Adicionar conexões
    conexoes = [(0, 1), (0, 2), (1, 2), (2, 3)]
    for u, v in conexoes:
        gm.add_edge(u, v)
        gl.add_edge(u, v)

    # Mostrar estruturas
    print("\n" + "-" * 25)
    print(" ESTRUTURAS DE DADOS ".center(25, '■'))
    gm.display()
    print()
    gl.display()

    # Calcular graus
    print("\n" + "-" * 25)
    print(" GRAUS DOS VÉRTICES ".center(25, '■'))
    for v in range(4):
        print(f" Vértice {v}: Matriz = {gm.vertex_degree(v)} | Lista = {gl.vertex_degree(v)}")

    # Gerar visualizações
    print("\n" + "=" * 55)
    print(" VISUALIZAÇÕES GRÁFICAS ".center(55, '★'))
    print("=" * 55)
    print(" Gerando representação visual da matriz...")
    gm.visualize()
    print(" Gerando representação visual da lista...")
    gl.visualize()