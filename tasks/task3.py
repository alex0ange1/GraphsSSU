#11 Построить орграф, полученный из исходного удалением изолированных вершин.
import graph

graph = graph.Graph()
filename = input("Enter filename to load (JSON): ")
graph.load_from_json(filename)

lst = graph.adj_list
ver = list(lst.keys())
ver_s_rebr = []
isolated = []
print("Изолированные вершины: ")

for v in ver:
    for el in list(lst[v]):
	    ver_s_rebr.append(v)


for v in ver:
	if v not in ver_s_rebr:
		isolated.append(v)
		print(v)

print(f"1.Сохранить в новый файл")
print(f"2.Удалить в текущем")
choice = int(input())
if choice == 1:
	newname = input("Введите новое название файла: ")
	for el in isolated:
		graph.remove_vertex(el)
	graph.save_to_json(f"{newname}")
elif choice == 2:
	for el in isolated:
		graph.remove_vertex(el)
	graph.save_to_json(f"{filename}")
else:
	print(f"Неверный ввод, повторите попытку")
	choice = int(input())