with open(' graph.txt', 'r') as f:
    data = [[int(i) for i in j.strip().split(',')] for j in f.readlines()]

n = len(data)
d = [set() for _ in range(n)]

for i in range(n):
    for j in range(n):
        if data[i][j] != 0:
            d[i].add(j)

print(len(max(d, key=len)))
# ANS = 6




