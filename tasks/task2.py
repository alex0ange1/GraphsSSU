import graph

graph = graph.Graph()
filename = input("Enter filename to load (JSON): ")
graph.load_from_json(filename)

lst = graph.adj_list
ver = list(lst.keys())
i = 0
dic = {}
print("Вершины, не смежные с данной: ")
for v in ver:
    dic[v] = []
    smezh = []
    for el in list(lst[v]):
	    smezh.append(el[0])
    for u in ver:
        if u not in smezh:
            dic[v].append(u)

for v, non_adjacent in dic.items():
    print(f"Вершина {v} не смежна с: {non_adjacent}")
