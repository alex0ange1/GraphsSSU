import graph

def bellman_ford(graph, target_vertex):
    adj_list = graph.adj_list
    vertices = list(adj_list.keys())

    # Инициализируем расстояния до всех вершин как бесконечные, кроме целевой
    dist = {vertex: float('inf') for vertex in vertices}
    dist[target_vertex] = 0

    # Создаем обратный граф
    reverse_adj_list = {vertex: [] for vertex in vertices}
    for vertex in adj_list:
        for neighbor, weight in adj_list[vertex]:
            reverse_adj_list[neighbor].append((vertex, weight))

    # Основной цикл алгоритма
    for _ in range(len(vertices) - 1):
        for vertex in reverse_adj_list:
            for neighbor, weight in reverse_adj_list[vertex]:
                if dist[vertex] != float('inf') and dist[vertex] + weight < dist[neighbor]:
                    dist[neighbor] = dist[vertex] + weight

    # Проверяем на наличие отрицательных циклов
    for vertex in reverse_adj_list:
        for neighbor, weight in reverse_adj_list[vertex]:
            if dist[vertex] != float('inf') and dist[vertex] + weight < dist[neighbor]:
                print("Граф содержит отрицательный цикл")
                return None

    return dist

graph = graph.Graph()
filename = input("Enter filename to load (JSON): ")
graph.load_from_json(filename)

ver = input(f"Введите вершину: ")
if ver in graph.adj_list.keys():
    distances = bellman_ford(graph, ver)

    if distances:
        print(f"Кратчайшие расстояния до вершины {ver}:")
        for vertex, distance in distances.items():
            print(f"От вершины {vertex}: {distance}")
else:
    print(f"В графе нет такой вершины!")