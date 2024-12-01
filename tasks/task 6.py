# 16
import graph

def is_acyclic_directed(graph):

    adj_list = graph.adj_list

    in_degree = {vertex: 0 for vertex in adj_list}

    for vertex in adj_list:
        for neighbor, _ in adj_list[vertex]:
            in_degree[neighbor] += 1

    zero_in_degree = [vertex for vertex, degree in in_degree.items() if degree == 0]

    top_order = []
    while zero_in_degree:
        vertex = zero_in_degree.pop(0)
        top_order.append(vertex)

        for neighbor, _ in adj_list[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)

    if len(top_order) == len(adj_list):
        return True
    else:
        return False


def is_acyclic_undirected(graph):
    adj_list = graph.adj_list
    visited = set()

    def dfs(vertex, parent):
        visited.add(vertex)
        for neighbor, _ in adj_list[vertex]:
            if neighbor not in visited:
                if not dfs(neighbor, vertex):
                    return False
            elif neighbor != parent:
                return False
        return True

    for vertex in adj_list:
        if vertex not in visited:
            if not dfs(vertex, None):
                return False

    return True


graph = graph.Graph()
filename = input("Enter filename to load (JSON): ")
graph.load_from_json(filename)

if graph.directed == False:
    if is_acyclic_undirected(graph):
        print("Граф ацикличен.")
    else:
        print("Граф содержит цикл.")
else:
    if is_acyclic_directed(graph):
        print("Орграф ацикличен.")
    else:
        print("Орграф содержит цикл.")

