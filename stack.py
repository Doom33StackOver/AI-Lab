def dfs(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        current_node = stack.pop()  # Remove from the top of the stack

        if current_node not in visited:
            print(f"Exploring Node: {current_node}")
            visited.append(current_node)

            # Reverse so traversal follows the input order
            for neighbour in reversed(graph.get(current_node, [])):
                if neighbour not in visited:
                    stack.append(neighbour)

    return visited


print("---Build Your Graph---")
student_graph = {}

num_edges = int(input("How many edges does your graph have? "))

print("Enter each edge separated by a space (e.g., A B):")

for i in range(num_edges):
    u, v = input(f"Edge {i + 1}: ").split()

    if u not in student_graph:
        student_graph[u] = []

    if v not in student_graph:
        student_graph[v] = []

    student_graph[u].append(v)
    student_graph[v].append(u)   # Remove this line if the graph is directed

start = input("Enter the starting node for DFS: ")

print(f"\nYour Graph Dictionary: {student_graph}")
print("Starting DFS Traversal...")

visited_nodes = dfs(student_graph, start)

print("\nDFS Traversal:", " -> ".join(visited_nodes))