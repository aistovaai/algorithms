def findCircleNum(isConnected) -> int:
    def dfs(city, visited):
        visited[city] = True
        for neighbor in range(len(isConnected)):
            if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor, visited)

    n = len(isConnected)
    visited = [False] * n
    provinces = 0

    for city in range(n):
        if not visited[city]:
            provinces += 1
            dfs(city, visited)

    return provinces