import networkx as nx

with open(' graph.txt', 'r') as f:
    data = [[int(i) for i in j.strip().split(',')] for j in f.readlines()]

n = len(data)
d = [set() for _ in range(n)]

for i in range(n):
    for j in range(n):
        if data[i][j] != 0:
            d[i].add(j)

# print(len(max(d, key=len)))
# ANS = 6


G = nx.Graph()

for i in range(n):
    G.add_node(i)
    for j in d[i]:
        G.add_edge(i, j)

# print(G)

print(nx.has_path(G, 81, 52))
print(nx.has_path(G, 86, 89))
print(nx.has_path(G, 21, 12))
print(nx.has_path(G, 16, 43))
print(nx.has_path(G, 1, 6))

print(nx.number_connected_components(G))