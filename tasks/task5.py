# 14. Найти сильно связные компоненты орграфа.

import graph

graph = graph.Graph()
filename = input("Enter filename to load (JSON): ")
graph.load_from_json(filename)

lst = graph.adj_list
ver = list(lst.keys())
reb = 0
for el in lst.values():
    reb += len(el)

dic = {}
for v in ver:
    smezh = []
    for el in lst[v]:
        smezh.append(el[0])
    dic[v] = smezh

for k, v in dic.items():
    print(f"{k}: {v}")

def dfs(vertex, visited, stack):
    visited.add(vertex)
    for neighbor in dic[vertex]:
        if neighbor not in visited:
            dfs(neighbor, visited, stack)
    stack.append(vertex)

def transpose_graph():
    transposed = {}
    for vertex in dic:
        transposed[vertex] = []
    for vertex, neighbors in dic.items():
        for neighbor in neighbors:
            transposed[neighbor].append(vertex)
    return transposed

def find_scc():
    stack = []
    visited = set()

    for vertex in dic:
        if vertex not in visited:
            dfs(vertex, visited, stack)

    transposed_dic = transpose_graph()

    visited.clear()
    strongly_connected_components = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            component = []
            dfs_scc(vertex, visited, transposed_dic, component)
            strongly_connected_components.append(component)

    return strongly_connected_components


def dfs_scc(vertex, visited, transposed, component):
    visited.add(vertex)
    component.append(vertex)
    for neighbor in transposed[vertex]:
        if neighbor not in visited:
            dfs_scc(neighbor, visited, transposed, component)


scc = find_scc()
print("Сильно связные компоненты:")
for component in scc:
    print(component)
