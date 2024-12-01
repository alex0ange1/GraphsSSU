import json


class Graph():
	def __init__(self, directed=False, weighted=False):
		self.directed = directed
		self.weighted = weighted
		self.adj_list = {}

	def __copy__(self):
		new_graph = Graph(self, self.directed, self.weighted)
		new_graph.adj_list = {k: v.copy for k, v in self.adj_list.items()}
		return new_graph

	def add_vertex(self, value):
		if value not in self.adj_list:
			self.adj_list[value] = []

	def add_edge(self, from_vertex, to_vertex, newweight=None):
		if from_vertex not in self.adj_list:
			self.add_vertex(from_vertex)
		if to_vertex not in self.adj_list:
			self.add_vertex(to_vertex)

		if self.weighted and newweight is None:
			raise ValueError("Weight must be provided for a weighted graph.")
		if not self.weighted and newweight is not None:
			print("Weight must not be provided for a weighted graph.")
			newweight = None

		for i, (v, w) in enumerate(self.adj_list[from_vertex]):
			if v == to_vertex:
				self.adj_list[from_vertex][i] = (to_vertex, newweight)
				break
		else:
			self.adj_list[from_vertex].append((to_vertex, newweight))

		if not self.directed:
			for i, (v, w) in enumerate(self.adj_list[to_vertex]):
				if v == from_vertex:
					self.adj_list[to_vertex][i] = (from_vertex, newweight)
					break
			else:
				self.adj_list[to_vertex].append((from_vertex, newweight))

	def remove_vertex(self, vertex):
		if vertex in self.adj_list:
			del self.adj_list[vertex]
			for v in self.adj_list:
				self.adj_list[v] = [edge for edge in self.adj_list[v] if edge[0] != vertex]
		else:
			print(f"There is no such vertex")

	def remove_edge(self, from_vertex, to_vertex):
		if from_vertex in self.adj_list:
			self.adj_list[from_vertex] = [
				edge for edge in self.adj_list[from_vertex] if edge[0] != to_vertex
			]
			if not self.directed and to_vertex in self.adj_list:
				self.adj_list[to_vertex] = [
					edge for edge in self.adj_list[to_vertex] if edge[0] != from_vertex
				]

	def print_adj_list(self):
		for v in sorted(self.adj_list.keys()):
			sorted_edges = sorted(self.adj_list[v], key=lambda x: x[0])
			if self.weighted:
				formatted_edges = [
					f"({edge[0]}, {edge[1]})" for edge in sorted_edges if edge[1] is not None
				]
			else:
				formatted_edges = [
					f"({edge[0]})" for edge in sorted_edges
				]
			print(f"{v}: {', '.join(formatted_edges)}")

	def load_from_json(self, filename):
		with open(filename, 'r') as file:
			graph_data = json.load(file)
			self.directed = graph_data["directed"]
			self.weighted = graph_data.get("weighted")
			self.adj_list = {}

			for vertex, edges in graph_data["adj_list"].items():
				self.add_vertex(vertex)
				for edge in edges:
					to_vertex = edge["to"]
					weight = edge.get("weight")
					if not self.weighted:
						weight = None
					self.add_edge(vertex, to_vertex, weight)

	def save_to_json(self, filename):
		graph_data = {
			"directed": self.directed,
			"weighted": self.weighted,
			"adj_list": {}
		}

		for vertex, edges in self.adj_list.items():
			graph_data["adj_list"][vertex] = []
			for edge in edges:
				edge_entry = {"to": edge[0]}
				if self.weighted and edge[1] is not None:
					edge_entry["weight"] = edge[1]
				graph_data["adj_list"][vertex].append(edge_entry)

		with open(filename, 'w') as file:
			json.dump(graph_data, file, indent=4)
