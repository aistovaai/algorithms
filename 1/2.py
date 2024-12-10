from enum import Enum

class Color(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2

def has_cycle(g: list[list[int]]) -> bool:
    """ Проверяет наличие цикла в неориентированном графе, проходящего только через нечётные вершины """
    c = [Color.WHITE] * len(g)

    def dfs(v: int, parent: int) -> bool:
        if c[v] == Color.GRAY:
            return True
        if v % 2 == 0:  # Пропускаем чётные вершины
            return False

        c[v] = Color.GRAY
        for u in g[v]:
            if u != parent and (c[u] == Color.GRAY or dfs(u, v)):  # Исключаем ребро ведущее обратно к родителю
                return True
        c[v] = Color.BLACK
        return False

    for v in range(len(g)):
        if v % 2 == 1 and c[v] == Color.WHITE:  # Запускаем только с неч вершин
            if dfs(v, -1):
                return True

    return False

# Вершины с нечётными номерами: 1, 3, 5
# Граф содержит цикл 1 - 3 - 5 - 1
graph = [
    [1],       # 0
    [0, 3, 5], # 1
    [],        # 2
    [1, 5],    # 3
    [],        # 4
    [1, 3]     # 5
]

result = has_cycle(graph)
print("Цикл с нечётными вершинами существует:" if result else "Цикл с нечётными вершинами не существует.")
