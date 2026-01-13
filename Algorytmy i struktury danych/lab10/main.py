class Edge:
    def __init__(self, capacity, is_real):
        self.capacity = capacity
        self.is_real = is_real
        self.flow = 0
        if is_real:
            self.capacity_rest = capacity
        else:
            self.capacity_rest = 0

    def __repr__(self):
        return f'{self.capacity} {self.flow} {self.capacity_rest} {self.is_real}'

class Node:
    def __init__(self, key, bright = "grey"):
        self.key = key
        self.bright = bright
        self.intree = 0
        self.distance = float("inf")
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

    def insert_edge(self, vertex1, vertex2, capacity):
        if vertex1 in self.graph and vertex2 in self.graph:
            edge1 = Edge(capacity, True)
            edge2 = Edge(0, False)

            self.graph[vertex1][vertex2] = edge1
            self.graph[vertex2][vertex1] = edge2


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
    def get_edge(self, vertex1, vertex2):
        return self.graph[vertex1][vertex2]



def bfs(graph, start):
    visited = set()
    parent = {}
    queue = [start]
    visited.add(start)
    while queue:
        vertex = queue.pop(0)
        vertex_neighbours = graph.neighbours(vertex)
        for neighbour, edge in vertex_neighbours:
            if neighbour not in visited and edge.capacity_rest > 0:
                queue.append(neighbour)
                visited.add(neighbour)
                parent[neighbour] = vertex
    return parent


def path_analize(graph, start, end, parent):
    if end not in parent:
        return 0
    vertex = end
    min_edge = float("inf")
    while vertex != start:
        prev = parent[vertex]
        edge = graph.get_edge(prev, vertex)
        if edge.capacity_rest < min_edge:
            min_edge = edge.capacity_rest
        vertex = prev
    return min_edge

def path_augmentation(graph, start, end, parent, min_edge):
    vertex = end
    while vertex != start:
        u = parent[vertex]
        edge_forward = graph.get_edge(u, vertex)
        edge_backward = graph.get_edge(vertex, u)

        if edge_forward.is_real:
            edge_forward.flow += min_edge
        edge_forward.capacity_rest -= min_edge

        if not edge_forward.is_real:
            edge_backward.flow -= min_edge
        edge_backward.capacity_rest += min_edge

        vertex = u


def max_flow(graph, start, end):
    while True:
        parent = bfs(graph, start)
        if end not in parent:
            break
        min_edge = path_analize(graph, start, end, parent)
        path_augmentation(graph, start, end, parent, min_edge)

    flow = 0
    for (nbr, edge) in graph.neighbours(start):
        flow += edge.flow
    return flow

def printgraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end=" -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")

def create_graph(edges):
    g = GraphL()
    for e in edges:
        u, v, c = e[0], e[1], e[2]
        is_bidirectional = e[3] if len(e) == 4 else False
        g.insert_vertex(u)
        g.insert_vertex(v)
        g.insert_edge(u, v, c)
        if is_bidirectional:
            g.insert_edge(v, u, c)
    return g
def outflow_from_node(graph, node):
    flow = 0
    for (nbr, edge) in graph.neighbours(node):
        if edge.is_real:
            flow += edge.flow if hasattr(edge, 'flow') else (edge.capacity - edge.capacity_rest)
    return flow

if __name__ == "__main__":
    grafy = [
        ([('s', 'u', 2, False), ('u', 't', 1, False), ('u', 'v', 3, False), ('s', 'v', 1, False), ('v', 't', 2, False)],
         'u'),

        ([('s', 'a', 16, False), ('s', 'c', 13, False),
          ('a', 'c', 10, False), ('c', 'a', 4, False),
          ('a', 'b', 12, False), ('b', 'c', 9, False),
          ('b', 't', 20, False), ('c', 'd', 14, False),
          ('d', 'b', 7, False), ('d', 't', 4, False)], 'a'),

        ([('s', 'a', 3, False), ('s', 'c', 3, False),
          ('a', 'b', 4, False), ('b', 's', 3, False),
          ('b', 'c', 1, False), ('b', 'd', 2, False),
          ('c', 'e', 6, False), ('c', 'd', 2, False),
          ('d', 't', 1, False), ('e', 't', 9, False)], 'a'),

        ([('s', 'a', 3, False), ('s', 'd', 2, False),
          ('a', 'b', 4, False), ('b', 'c', 5, False),
          ('c', 't', 6, False), ('a', 'f', 3, False),
          ('f', 't', 3, False), ('d', 'e', 2, False),
          ('e', 'f', 2, False)], 'a')
    ]

    for i,(edges, node_for_outflow) in enumerate(grafy):
        print(f"Test {i}:")
        g = create_graph(edges)
        flow = max_flow(g, 's', 't')
        print(flow)
        printgraph(g)
        real_flow = 0
        for (nbr, edge) in g.neighbours(node_for_outflow):
            if edge.is_real:
                real_flow += edge.capacity - edge.capacity_rest
        print(real_flow)
        print()