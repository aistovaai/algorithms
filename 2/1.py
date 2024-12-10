from collections import defaultdict, deque

def topological_sort(g):
    # Считаем входные степени
    in_degree = defaultdict(int)
    for node in g:
        for dependent in g[node]:
            in_degree[dependent] += 1

    # Очередь с вершинами, у которых нет входных рёбер
    queue = deque([node for node in g if in_degree[node] == 0])

    sorted_list = []

    # Идем по всем вершинам в очереди
    while queue:
        node = queue.popleft()
        sorted_list.append(node)

        # Обрабатываем смежные
        for dependent in g[node]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)

    # Проверка, все ли обработаны
    if len(sorted_list) != len(g):
        return None  # Существует цикл

    return sorted_list
