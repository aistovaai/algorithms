def are_reachable(adj_list, v, u):
    def dfs(start, target, visited):
        if start == target:
            return True
        visited.add(start)
        for neighbor in adj_list.get(start, []):
            if neighbor not in visited:
                if dfs(neighbor, target, visited):
                    return True
        return False

    # Проверяем достижимость из v в u
    visited_from_v = set()
    reachable_from_v = dfs(v, u, visited_from_v)

    # Проверяем достижимость из u в v
    visited_from_u = set()
    reachable_from_u = dfs(u, v, visited_from_u)

    return reachable_from_v and reachable_from_u


adjacency_list = {
    0: [1],
    1: [2, 3],
    2: [0],
    3: []
}
v, u = 0, 2
print(are_reachable(adjacency_list, v, u))
