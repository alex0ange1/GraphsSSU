# 6. Найти вершину, сумма длин кратчайших путей от которой до остальных вершин минимальна.
import graph
import math

def floyd_warshall(graph):
    adj_list = graph.adj_list
    vertices = list(adj_list.keys())

    dist = {v: {u: math.inf for u in vertices} for v in vertices}

    for v in vertices:
        dist[v][v] = 0

    for v in adj_list:
        for neighbor, weight in adj_list[v]:
            dist[v][neighbor] = weight

    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def find_central_vertex_floyd(graph):
    dist = floyd_warshall(graph)
    min_sum_distance = math.inf
    ans = []

    for v in dist:
        sum_distances = sum(dist[v].values())

        if sum_distances <= min_sum_distance:
            min_sum_distance = sum_distances
            central_vertex = v

    for v in dist:
        sum_distances = sum(dist[v].values())
        if sum(dist[v].values()) == min_sum_distance:
            ans.append(v)

    return ans, min_sum_distance


graph = graph.Graph()
filename = input("Enter filename to load (JSON): ")
graph.load_from_json(filename)

central_vertexs, min_sum_distance = find_central_vertex_floyd(graph)
print(f"Вершина(ы) с минимальной суммой кратчайших путей:")
for el in central_vertexs:
    print(el)
print(f"Сумма кратчайших путей: {min_sum_distance}")
