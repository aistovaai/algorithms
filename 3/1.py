def criticalConnections(n: int, connections):
    def dfs(node, parent, visited, low, time, graph, result):
        visited[node] = low[node] = time[0]
        time[0] += 1

        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if visited[neighbor] == -1:
                dfs(neighbor, node, visited, low, time, graph, result)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > visited[node]:
                    result.append([node, neighbor])
            else:
                # Если сосед уже посещён, обновляем мин время
                low[node] = min(low[node], visited[neighbor])

    graph = [[] for _ in range(n)]
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    visited = [-1] * n
    low = [-1] * n
    time = [0]
    result = []

    dfs(0, -1, visited, low, time, graph, result)

    return result
