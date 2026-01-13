class Kruskal:
    def __init__(self,n):
        self.n = n
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self,v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])

        return self.parent[v]

    def union_sets(self, s1, s2):
        root1 = self.find(s1)
        root2 = self.find(s2)

        if root1 == root2:
            return
        if self.size[root1] < self.size[root2]:
            root1, root2 = root2, root1

        self.parent[root2] = root1
        self.size[root1] += self.size[root2]
        return True
    def same_components(self,s1,s2):
        roots1 = self.find(s1)
        roots2 = self.find(s2)

        return roots1 == roots2



kruskal = Kruskal(5)

kruskal.union_sets(0,1)
kruskal.union_sets(3,4)

print(kruskal.same_components(0,1))
print(kruskal.same_components(1,2))
print(kruskal.same_components(3,4))

kruskal.union_sets(2,0)

print(kruskal.same_components(0,1))
print(kruskal.same_components(1,2))
print(kruskal.same_components(3,4))


graf = [
    ('A','B',4), ('A','C',1), ('A','D',4),
    ('B','E',9), ('B','F',9), ('B','G',7), ('B','C',5),
    ('C','G',9), ('C','D',3),
    ('D','G',10), ('D','J',18),
    ('E','I',6), ('E','H',4), ('E','F',2),
    ('F','H',2), ('F','G',8),
    ('G','H',9), ('G','J',8),
    ('H','I',3), ('H','J',9),
    ('I','J',9)
]

def to_index(c):
    return ord(c) - ord('A')

n = 10

sorted_edges = sorted(graf, key=lambda x: x[2])

kruskal = Kruskal(n)
mst = []

for u, v, w in sorted_edges:
    u_idx = to_index(u)
    v_idx = to_index(v)
    if kruskal.union_sets(u_idx, v_idx):
        mst.append((u, v, w))

for edge in mst:
    print(edge)