# Algoritmo de BFS (Original) 
def breadth_first_search_tree(graph, start):
    adjacency_list = {i: [j for j in range(len(graph[i])) if graph[i][j] == 1] for i in range(len(graph))}  # Lista de adjacência
    visited = [False] * len(graph)  # Lista de nós visitados
    queue = [start]  # Fila de nós a serem visitados
    visited[start] = True  # Marca o nó inicial como visitado
    bfs_tree_edges = []  # Arestas da árvore BFS
    bfs_nodes = [start]  # Nós visitados pela BFS
    parent = {start: None}  # Dicionário para armazenar os pais dos nós

    # BFS
    while queue: # Enquanto a fila não estiver vazia
        node = queue.pop(0) # Remove o primeiro nó da fila
        for neighbour in adjacency_list[node]: # Para cada vizinho do nó
            if not visited[neighbour]: # Se o vizinho não foi visitado
                queue.append(neighbour) # Adiciona o vizinho na fila
                visited[neighbour] = True # Marca o vizinho como visitado
                bfs_tree_edges.append((node, neighbour)) # Adiciona a aresta na árvore BFS (opcional)
                bfs_nodes.append(neighbour) # Adiciona o vizinho na lista de nós visitados
                parent[neighbour] = node # Salva o pai do vizinho

    return bfs_tree_edges, bfs_nodes, parent

# Exemplo de uso
graph = [[0, 1, 1, 0, 0, 0],
         [1, 0, 0, 1, 1, 0],
         [1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 1, 1],
         [0, 1, 1, 1, 0, 1],
         [0, 0, 0, 1, 1, 0]]

start_node = 0
bfs_edges, bfs_nodes, parent = breadth_first_search_tree(graph, start_node)

print("Arestas da árvore BFS:", bfs_edges)
print("Nós visitados na BFS:", bfs_nodes)
print("Pais dos nós:", parent)