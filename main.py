from graph import Graph

def console_interface():
    graph = Graph()
    filename = input("Enter filename to load (JSON): ")
    graph.load_from_json(filename)



    print("Graph Operations:")

    while True:
        print("\n1. Add Vertex")
        print("2. Add Edge")
        print("3. Remove Vertex")
        print("4. Remove Edge")
        print("5. Print Adjacency List")
        print("6. Save to JSON")
        print("7. Load from JSON")
        print("8. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            vertex = input("Enter vertex: ")
            graph.add_vertex(vertex)
        elif choice == "2":
            from_vertex = input("Enter from vertex: ")
            to_vertex = input("Enter to vertex: ")
            weight = input("Enter weight (optional, press enter for none): ")
            weight = int(weight) if weight else None
            graph.add_edge(from_vertex, to_vertex, weight)
        elif choice == "3":
            vertex = input("Enter vertex to remove: ")
            graph.remove_vertex(vertex)
        elif choice == "4":
            from_vertex = input("Enter from vertex: ")
            to_vertex = input("Enter to vertex: ")
            graph.remove_edge(from_vertex, to_vertex)
        elif choice == "5":
            print("Current Adjacency List:")
            graph.print_adj_list()
        elif choice == "6":
            filename = input("Enter filename to save (JSON): ")
            graph.save_to_json(filename)
        elif choice == "7":
            filename = input("Enter filename to load (JSON): ")
            graph.load_from_json(filename)
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

console_interface()

#12 12

#2 Вывести те вершины орграфа, в которых есть петли.

#3 Вывести те вершины орграфа, в которых есть петли.

