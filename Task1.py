import networkx as nx
import matplotlib.pyplot as plt

# Список ребер, що представляють дороги між районами міста
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

# Аналіз характеристик графа
num_nodes = graph.number_of_nodes()
num_edges = graph.number_of_edges()
average_degree = sum(dict(graph.degree()).values()) / num_nodes

# Виведення результатів аналізу
print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Середній ступінь вершин: {average_degree:.2f}")

# Візуалізація графа
pos = nx.spring_layout(graph)  # Визначення розташування вершин
nx.draw(graph, pos, with_labels=True, node_size=700, node_color="skyblue")
labels = nx.get_edge_attributes(graph, "weight")
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
plt.title("Транспортна мережа міста")
plt.show()