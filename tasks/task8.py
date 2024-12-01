# 4. Вывести длины кратчайших путей от u до v1 и v2.
import graph
import heapq


def dijkstra(graph, start_vertex):
    adj_list = graph.adj_list
    distances = {vertex: float('infinity') for vertex in adj_list}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in adj_list[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def find_shortest_paths(graph, u, v1, v2):
    distances = dijkstra(graph, u)
    distance_to_v1 = distances[v1] if v1 in distances else float('infinity')
    distance_to_v2 = distances[v2] if v2 in distances else float('infinity')

    return distance_to_v1, distance_to_v2

graph_instance = graph.Graph()
filename = input("Enter filename to load (JSON): ")
graph_instance.load_from_json(filename)

u = input("Введите начальную вершину (u): ")
v1 = input("Введите конечную вершину (v1): ")
v2 = input("Введите конечную вершину (v2): ")
if u not in graph_instance.adj_list.keys():
    print(print(f"Вершины {u} нет в графе!"))
elif v1 not in graph_instance.adj_list.keys() and v2 not in graph_instance.adj_list.keys():
    print(f"Вершин {v1} и {v2} нет в графе!")
elif v1 not in graph_instance.adj_list.keys():
    print(f"Вершины {v1} нет в графе!")
    distance_to_v1, distance_to_v2 = find_shortest_paths(graph_instance, u, v1, v2)
    print(f"Кратчайший путь от {u} до {v2}: {distance_to_v2}")
elif v2 not in graph_instance.adj_list.keys():
    print(f"Вершины {v2} нет в графе!")
    distance_to_v1, distance_to_v2 = find_shortest_paths(graph_instance, u, v1, v2)
    print(f"Кратчайший путь от {u} до {v1}: {distance_to_v1}")
else:
    distance_to_v1, distance_to_v2 = find_shortest_paths(graph_instance, u, v1, v2)
    print(f"Кратчайший путь от {u} до {v1}: {distance_to_v1}")
    print(f"Кратчайший путь от {u} до {v2}: {distance_to_v2}")
