# п
import graph
import heapq


def prim(graph, start_vertex):
	mst = []
	total_weight = 0
	visited = set()
	min_heap = []

	visited.add(start_vertex)
	for neighbor, weight in graph.adj_list[start_vertex]:
		heapq.heappush(min_heap, (weight, start_vertex, neighbor))

	while min_heap:
		weight, from_vertex, to_vertex = heapq.heappop(min_heap)
		if to_vertex not in visited:
			visited.add(to_vertex)
			mst.append((from_vertex, to_vertex, weight))
			total_weight += weight

			for neighbor, weight in graph.adj_list[to_vertex]:
				if neighbor not in visited:
					heapq.heappush(min_heap, (weight, to_vertex, neighbor))
	return mst, total_weight

graph = graph.Graph()
filename = input("Enter filename to load (JSON): ")
graph.load_from_json(filename)


mst, total_weight = prim(graph, 'A')
print("Минимальный остовной каркас:", mst)
print("Суммарный вес каркаса:", total_weight)
