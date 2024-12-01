from collections import deque
import graph

def bfs(residual_graph, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        u = queue.popleft()
        for v, capacity in residual_graph[u].items():
            if v not in visited and capacity > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False

def edmonds_karp(adj_list, source, sink):
    # Инициализируем остаточный граф
    residual_graph = {u: {} for u in adj_list}
    for u in adj_list:
        for v, capacity in adj_list[u]:
            residual_graph[u][v] = capacity
            if v not in residual_graph:
                residual_graph[v] = {}
            if u not in residual_graph[v]:
                residual_graph[v][u] = 0

    parent = {}
    max_flow = 0

    # Ищем увеличивающие пути с помощью BFS
    while bfs(residual_graph, source, sink, parent):
        path_flow = float('inf')
        s = sink

        # Находим минимальную пропускную способность на найденном пути
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        # Обновляем остаточные ёмкости рёбер и обратных рёбер
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = u

        # Добавляем поток пути к общему потоку
        max_flow += path_flow

    return max_flow

graph = graph.Graph()
filename = input("Введите имя файла для загрузки (JSON): ")
graph.load_from_json(filename)

source = input("Введите начальную вершину: ")
sink = input("Введите конечную вершину: ")

max_flow = edmonds_karp(graph.adj_list, source, sink)
print(f"Максимальный поток из {source} в {sink}: {max_flow}")