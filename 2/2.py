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



# Вершины и рёбра
V = {"Пиджак", "Часы", "Брюки", "Рубашка", "Трусы", "Носки", "Туфли", "Галстук", "Ремень"}
E = {("Галстук", "Пиджак"), ("Носки", "Туфли"), ("Рубашка", "Ремень"),
     ("Рубашка", "Галстук"), ("Ремень", "Пиджак"), ("Трусы", "Брюки"),
     ("Трусы", "Туфли"), ("Брюки", "Туфли"), ("Брюки", "Ремень")}

# Строим граф из вершин и рёбер
clothing_graph = defaultdict(list)
for a, b in E:
    clothing_graph[a].append(b)
for vertex in V:
    if vertex not in clothing_graph:
        clothing_graph[vertex] = []  # Добавляем вершину без рёбер

# Применяем топологическую сортировку
order = topological_sort(clothing_graph)

if order:
    print("Последовательность надевания одежды:")
    print(order)
else:
    print("Ошибка: граф содержит цикл!")