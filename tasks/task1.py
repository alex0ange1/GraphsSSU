import graph

graph = graph.Graph()
filename = input("Enter filename to load (JSON): ")
graph.load_from_json(filename)

lst = graph.adj_list
ver = list(lst.keys())
i = 0
print("Вершины с петлями: ")
for v in list(lst.values()):
	for el in v:
		el = list(el)[0]
		if el == ver[i]:
			print(el)
	i += 1
