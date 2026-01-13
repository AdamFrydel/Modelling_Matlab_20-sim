class Node:
    def __init__(self, key, bright = "grey"):
        self.key = key
        self.bright = bright
        self.intree = 0
        self. distance = float("inf")
        self.parent = None


    def __eq__(self, other):
        return isinstance(other, Node) and self.key == other.key

    def __repr__(self):
        return str(self.key)

    def __hash__(self):
        return hash(self.key)


class GraphL:
    def __init__(self):
        self.graph = {}

    def is_empty(self):
        return len(self.graph) == 0

    def insert_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def insert_edge(self, vertex1, vertex2, edge):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1][vertex2] = edge
            self.graph[vertex2][vertex1] = edge

    def delete_vertex(self, vertex):
        if vertex in self.graph:
            for v in self.graph:
                self.graph[v].pop(vertex, None)
            del self.graph[vertex]

    def delete_edge(self, vertex1, vertex2):
        self.graph[vertex1].pop(vertex2, None)
        self.graph[vertex2].pop(vertex1, None)

    def neighbours(self, vertex):
        return self.graph[vertex].items()

    def vertices(self):
        return self.graph.keys()

    def get_vertex(self, vertex):
        return vertex

    def mst(self):
        mst = GraphL()
        vertices = list(self.graph.keys())
        if not vertices:
            return mst

        start = vertices[0]
        start.distance = 0

        while True:
            current = None
            min_dist = float('inf')
            for v in self.graph:
                if not v.intree and v.distance < min_dist:
                    min_dist = v.distance
                    current = v

            if current is None:
                break

            current.intree = 1
            mst.insert_vertex(current)
            if current.parent:
                mst.insert_vertex(current.parent)
                weight = self.graph[current][current.parent]
                mst.insert_edge(current, current.parent, weight)

            for neighbor, weight in self.graph[current].items():
                if not neighbor.intree and weight < neighbor.distance:
                    neighbor.distance = weight
                    neighbor.parent = current

        return mst

def printgraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end=" -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")


edges = [
    ('A','B',4), ('A','C',1), ('A','D',4),
    ('B','E',9), ('B','F',9), ('B','G',7), ('B','C',5),
    ('C','G',9), ('C','D',3),
    ('D', 'G', 10), ('D', 'J', 18),
    ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
    ('F', 'H', 2), ('F', 'G', 8),
    ('G', 'H', 9), ('G', 'J', 8),
    ('H', 'I', 3), ('H','J',9),
    ('I', 'J', 9)
]

nodes = {}
for u, v, _ in edges:
    if u not in nodes:
        nodes[u] = Node(u)
    if v not in nodes:
        nodes[v] = Node(v)

g = GraphL()
for node in nodes.values():
    g.insert_vertex(node)

for u, v, w in edges:
    g.insert_edge(nodes[u], nodes[v], w)

mst = g.mst()

printgraph(mst)