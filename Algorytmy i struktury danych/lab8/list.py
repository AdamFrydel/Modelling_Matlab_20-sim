import polska
class Node:
    def __init__(self, key):
        self.key = key

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


class GraphM:
    def __init__(self):
        self.vertex_list = []
        self.adj_matrix = []

    def is_empty(self):
        return len(self.vertex_list) == 0

    def insert_vertex(self, vertex):
        if vertex in self.vertex_list:
            return
        self.vertex_list.append(vertex)
        size = len(self.vertex_list)
        for row in self.adj_matrix:
            row.append(None)
        self.adj_matrix.append([None] * size)

    def insert_edge(self, vertex1, vertex2, edge):
        if vertex1 not in self.vertex_list or vertex2 not in self.vertex_list:
            return
        i = self.vertex_list.index(vertex1)
        j = self.vertex_list.index(vertex2)
        self.adj_matrix[i][j] = edge
        self.adj_matrix[j][i] = edge

    def delete_vertex(self, vertex):
        if vertex not in self.vertex_list:
            return
        idx = self.vertex_list.index(vertex)
        del self.vertex_list[idx]
        del self.adj_matrix[idx]
        for row in self.adj_matrix:
            del row[idx]

    def delete_edge(self, vertex1, vertex2):
        i = self.vertex_list.index(vertex1)
        j = self.vertex_list.index(vertex2)
        self.adj_matrix[i][j] = None
        self.adj_matrix[j][i] = None

    def neighbours(self, vertex):
        i = self.vertex_list.index(vertex)
        return [(self.vertex_list[j], self.adj_matrix[i][j]) for j in range(len(self.vertex_list)) if self.adj_matrix[i][j] is not None]

    def vertices(self):
        return self.vertex_list

    def get_vertex(self, vertex):
        return vertex


def utworz_graf(graphclass):
    g = graphclass()

    unikalne = set()
    for v1, v2 in polska.graf:
        unikalne.add(v1)
        unikalne.add(v2)
    for v in unikalne:
        g.insert_vertex(Node(v))

    for v1, v2 in polska.graf:
        g.insert_edge(Node(v1), Node(v2), 1)

    g.delete_vertex(Node('K'))

    g.delete_edge(Node('W'), Node('E'))

    return g

if __name__ == "__main__":
    grafL = utworz_graf(GraphL)
    grafM = utworz_graf(GraphM)

    polska.draw_map(grafL)
    polska.draw_map(grafM)