def adj_list_to_adj_matrix(adj_list):
    """Преобразование из списка смежности в матрицу смежности"""
    n = len(adj_list)
    adj_matrix = [[0] * n for _ in range(n)]
    for i, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            adj_matrix[i][neighbor] = 1
    return adj_matrix

def adj_list_to_edge_list(adj_list):
    """Преобразование из списка смежности в список ребер"""
    edge_list = []
    for i, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            edge_list.append((i, neighbor))
    return edge_list

def adj_matrix_to_adj_list(adj_matrix):
    """Преобразование из матрицы смежности в список смежности"""
    adj_list = []
    for i, row in enumerate(adj_matrix):
        neighbors = [j for j, val in enumerate(row) if val == 1]
        adj_list.append(neighbors)
    return adj_list

def adj_matrix_to_edge_list(adj_matrix):
    """Преобразование из матрицы смежности в список ребер"""
    edge_list = []
    for i, row in enumerate(adj_matrix):
        for j, val in enumerate(row):
            if val == 1:
                edge_list.append((i, j))
    return edge_list

def edge_list_to_adj_list(edge_list, n):
    """Преобразование из списка ребер в список смежности"""
    adj_list = [[] for _ in range(n)]
    for u, v in edge_list:
        adj_list[u].append(v)
    return adj_list

def edge_list_to_adj_matrix(edge_list, n):
    """Преобразование из списка ребер в матрицу смежности"""
    adj_matrix = [[0] * n for _ in range(n)]
    for u, v in edge_list:
        adj_matrix[u][v] = 1
    return adj_matrix
