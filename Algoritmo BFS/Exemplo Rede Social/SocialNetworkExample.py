import networkx as nx
import matplotlib.pyplot as plt

# Função para criar o grafo a partir de uma matriz de adjacência
def create_graph(graph):
    G = nx.Graph()
    for i in range(len(graph)):
        for j in range(i, len(graph[i])):  # Evita adicionar arestas duplicadas
            if graph[i][j] == 1:
                G.add_edge(i, j)
    return G

# Função para salvar a imagem do grafo
def plot_and_save_graph(G, filename, highlight_edges=None, highlight_nodes=None, path_edges=None):
    pos = nx.spring_layout(G)  # Define a posição dos nós
    plt.figure(figsize=(8, 8))

    # Desenha todas as arestas normalmente
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)

    # Destaca arestas da árvore BFS (se houver)
    if highlight_edges:
        nx.draw_networkx_edges(G, pos, edgelist=highlight_edges, edge_color='red', width=2)

    # Destaca nós visitados pela BFS (se houver)
    if highlight_nodes:
        nx.draw_networkx_nodes(G, pos, nodelist=highlight_nodes, node_color='orange', node_size=2000)

    # Destaca caminho mais curto em verde (se houver)
    if path_edges:
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='green', width=3, style="dashed")

    plt.savefig(filename)  # Salva a imagem
    plt.close()

# Função para criar lista de adjacência
def create_adjacency_list(graph):
    adjacency_list = {}
    for i in range(len(graph)):
        adjacency_list[i] = []
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                adjacency_list[i].append(j)
    return adjacency_list

# Algoritmo de BFS que também encontra caminhos mínimos
def breadth_first_search_tree(graph, start):
    adjacency_list = create_adjacency_list(graph)
    visited = [False] * len(graph)
    queue = [start]
    visited[start] = True
    bfs_tree_edges = []
    bfs_nodes = [start]
    parent = {start: None}  # Dicionário para armazenar os pais dos nós

    while queue:
        node = queue.pop(0)
        for neighbour in adjacency_list[node]:
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = True
                bfs_tree_edges.append((node, neighbour))
                bfs_nodes.append(neighbour)
                parent[neighbour] = node  # Registra o pai do nó

    return bfs_tree_edges, bfs_nodes, parent

# Função para reconstruir o caminho mais curto até um nó
def shortest_path(parent, target):
    path = []
    while target is not None:
        path.append(target)
        target = parent[target]
    path.reverse()
    return path

# Exemplo de rede social (matriz de adjacência)
# Nós: 0 = Alfredo, 1 = Bruna, 2 = Carol, 3 = Daniel, 4 = Erica, 5 = Fernando
graph = [
    [0, 1, 1, 0, 0, 0],  # Alfredo: Bruna e Carol
    [1, 0, 0, 1, 1, 0],  # Bruna: Alfredo, Daniel e Erick
    [1, 0, 0, 0, 1, 0],  # Carol: Alfredo e Erick
    [0, 1, 0, 0, 1, 1],  # Daniel: Bruna, Erick e Fernando
    [0, 1, 1, 1, 0, 1],  # Erick: Bruna, Carol, Daniel e Fernando
    [0, 0, 0, 1, 1, 0]   # Fernando: Daniel e Erick
]

# Criar o grafo original e salvar imagem
G = create_graph(graph)
plot_and_save_graph(G, "rede_social_original.png")

# Definir o nó inicial (Alfredo) e o nó de destino (Fernando)
start_node = 0  # Alfredo
target_node = 5  # Fernando

# Rodar BFS e capturar árvore BFS e os pais dos nós
bfs_edges, bfs_nodes, parent = breadth_first_search_tree(graph, start_node)

# Gerar e salvar a imagem da árvore BFS
plot_and_save_graph(G, "arvore_bfs_rede_social.png", highlight_edges=bfs_edges, highlight_nodes=bfs_nodes)

# Encontrar e exibir caminho mais curto
shortest_path_nodes = shortest_path(parent, target_node)
path_edges = [(shortest_path_nodes[i], shortest_path_nodes[i+1]) for i in range(len(shortest_path_nodes)-1)]

print(f"\nCaminho mais curto de {start_node} (Alfredo) até {target_node} (Fernando): {shortest_path_nodes}")

# Gerar e salvar imagem do caminho mais curto
plot_and_save_graph(G, "caminho_mais_curto_rede_social.png", path_edges=path_edges, highlight_nodes=shortest_path_nodes)

print("\nImagens salvas:")
print("- 'rede_social_original.png': Grafo original da rede social.")
print("- 'arvore_bfs_rede_social.png': Árvore BFS a partir de Alfredo.")
print("- 'caminho_mais_curto_rede_social.png': Caminho mais curto de Alfredo até Fernando.")