# Esse algoritmo é uma versão buffada do BFS, ele faz:
# - Gera a árvore de busca em largura (BFS Tree)
# - Registra os pais de cada nó
# - Reconstrói o caminho mais curto

import networkx as nx # A biblioteca NetworkX é uma biblioteca de Python usada para a criação, manipulação e estudo de estruturas de grafos e redes complexas.
import matplotlib.pyplot as plt
import os

# Criar diretório de saída se não existir
output_dir = "AlgoritmoBFS/output"
os.makedirs(output_dir, exist_ok=True)

# Função para converter matriz de adjacência em grafo do NetworkX
def create_graph(graph):
    G = nx.Graph()
    for i in range(len(graph)):
        for j in range(i, len(graph[i])):
            if graph[i][j] == 1:
                G.add_edge(i, j)
    return G

# Função para salvar imagem do grafo
def plot_and_save_graph(G, filename, highlight_edges=None, highlight_nodes=None, path_edges=None):
    pos = nx.spring_layout(G) 
    plt.figure(figsize=(6, 6))

    # Desenha todas as arestas normalmente
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)

    # Destaca arestas da árvore BFS
    if highlight_edges:
        nx.draw_networkx_edges(G, pos, edgelist=highlight_edges, edge_color='red', width=2)

    # Destaca nós visitados pelo BFS 
    if highlight_nodes:
        nx.draw_networkx_nodes(G, pos, nodelist=highlight_nodes, node_color='orange', node_size=2000)

    # Destaca caminho mais curto em verde
    if path_edges:
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='green', width=3, style="dashed")

    plt.savefig(os.path.join(output_dir, filename)) 
    plt.close()

# Função para reconstruir o caminho mais curto até um nó
def shortest_path(parent, target):
    path = []
    while target is not None:
        path.append(target)
        target = parent[target]
    path.reverse()
    return path

# Função para criar lista de adjacência
def create_adjacency_list(graph):
    adjacency_list = {}
    for i in range(len(graph)):
        adjacency_list[i] = []
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                adjacency_list[i].append(j)
    return adjacency_list

# Algoritmo de BFS
def breadth_first_search_tree(graph, start):
    adjacency_list = create_adjacency_list(graph)
    visited = [False] * len(graph)
    queue = [start]
    visited[start] = True
    bfs_tree_edges = []
    bfs_nodes = [start]
    parent = {start: None}

    while queue:
        node = queue.pop(0)
        for neighbour in adjacency_list[node]:
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = True
                bfs_tree_edges.append((node, neighbour))
                bfs_nodes.append(neighbour)
                parent[neighbour] = node

    return bfs_tree_edges, bfs_nodes, parent

# Exemplo de uso
graph = [[0, 1, 1, 0, 0, 0],
         [1, 0, 0, 1, 1, 0],
         [1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 1, 1],
         [0, 1, 1, 1, 0, 1],
         [0, 0, 0, 1, 1, 0]]

start_node = 0
target_node = 5

# Cria grafo e salva imagem
G = create_graph(graph)
plot_and_save_graph(G, "grafo_original.png")

# Executa BFS e salva imagem da árvore BFS
bfs_edges, bfs_nodes, parent = breadth_first_search_tree(graph, start_node)
plot_and_save_graph(G, "arvore_bfs.png", highlight_edges=bfs_edges, highlight_nodes=bfs_nodes)

# Cria lista de adjacência e encontra caminho mais curto
adj_list = create_adjacency_list(graph)
print("\nLista de Adjacência:")
for node, neighbors in adj_list.items():
    print(f"{node}: {neighbors}")

# Reconstrói caminho mais curto
shortest_path_nodes = shortest_path(parent, target_node)
path_edges = [(shortest_path_nodes[i], shortest_path_nodes[i+1]) for i in range(len(shortest_path_nodes)-1)]

print(f"\nCaminho mais curto de {start_node} até {target_node}: {shortest_path_nodes}")
plot_and_save_graph(G, "caminho_mais_curto.png", path_edges=path_edges, highlight_nodes=shortest_path_nodes)

print("\nImagens salvas em 'AlgoritmoBFS/output': 'grafo_original.png', 'arvore_bfs.png' e 'caminho_mais_curto.png'")