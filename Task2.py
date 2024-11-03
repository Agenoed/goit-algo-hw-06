import networkx as nx
import matplotlib.pyplot as plt

# Список ребер з першого завдання
edges = [
    ("Центр", "Північ", {"weight": 5}),
    ("Центр", "Південь", {"weight": 3}),
    ("Центр", "Схід", {"weight": 4}),
    ("Центр", "Захід", {"weight": 6}),
    ("Північ", "Схід", {"weight": 2}),
    ("Південь", "Захід", {"weight": 3}),
    ("Схід", "Захід", {"weight": 5}),
]

# Створення графа
graph = nx.Graph()
graph.add_edges_from(edges)

# Алгоритм DFS
def dfs(graph, start_node):
    visited = set()
    path = []
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            path.append(node)
            neighbors = list(graph.neighbors(node))
            neighbors.reverse()  # Зміна порядку сусідів для узгодження з рекурсивним DFS
            stack.extend(neighbors)
    return path

# Алгоритм BFS
def bfs(graph, start_node):
    visited = set()
    path = []
    queue = [start_node]
    visited.add(start_node)
    while queue:
        node = queue.pop(0)
        path.append(node)
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return path

# Знаходження шляхів з вершини "Центр"
start_node = "Центр"
dfs_path = dfs(graph, start_node)
bfs_path = bfs(graph, start_node)

# Виведення результатів
print("Шлях DFS:", dfs_path)
print("Шлях BFS:", bfs_path)

# Візуалізація графа з виділеними шляхами
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, node_size=700, node_color="skyblue")
labels = nx.get_edge_attributes(graph, "weight")
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

# Виділення шляхів DFS і BFS
nx.draw_networkx_edges(graph, pos, edgelist=list(zip(dfs_path, dfs_path[1:])), edge_color="red", width=2)
nx.draw_networkx_edges(graph, pos, edgelist=list(zip(bfs_path, bfs_path[1:])), edge_color="green", width=2)

plt.title("Транспортна мережа міста з шляхами DFS і BFS")
plt.show()