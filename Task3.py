import networkx as nx


edges = [
    ("Центр", "Північ", {"weight": 5}),
    ("Центр", "Південь", {"weight": 3}),
    ("Центр", "Схід", {"weight": 4}),
    ("Центр", "Захід", {"weight": 6}),
    ("Північ", "Схід", {"weight": 2}),
    ("Південь", "Захід", {"weight": 3}),
    ("Схід", "Захід", {"weight": 5}),
]


graph = nx.Graph()
graph.add_edges_from(edges)

# Алгоритм Дейкстри
def dijkstra(graph, start_node):
  
    distances = {node: float('inf') for node in graph.nodes()}
    distances[start_node] = 0
    visited = set()

    while len(visited) < len(graph.nodes()):
        current_node = min((node for node in graph.nodes() if node not in visited), key=lambda node: distances[node])
        visited.add(current_node)

        for neighbor in graph.neighbors(current_node):
            new_distance = distances[current_node] + graph[current_node][neighbor]['weight']
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances

# Знаходження найкоротших шляхів між усіма вершинами
shortest_paths = {}
for node in graph.nodes():
    shortest_paths[node] = dijkstra(graph, node)

# Виведення результатів
for start_node, paths in shortest_paths.items():
    print(f"Найкоротші шляхи від вершини {start_node}: {paths}")