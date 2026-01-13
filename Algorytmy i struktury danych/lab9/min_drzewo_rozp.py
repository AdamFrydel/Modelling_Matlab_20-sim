import cv2
import numpy as np
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



if __name__ == "__main__":
    def dfs_color(graph, start, color, IS, width):
        stack = [start]
        visited = set()
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            y = current.key // width
            x = current.key % width
            IS[y, x] = color
            for neighbor, _ in graph.neighbours(current):
                if neighbor not in visited:
                    stack.append(neighbor)


    def remove_max_edge(g):
        max_weight = -1
        max_edge = (None, None)
        visited = set()
        for v in g.vertices():
            for u, weight in g.neighbours(v):
                if (v, u) in visited or (u, v) in visited:
                    continue
                visited.add((v, u))
                if weight > max_weight:
                    max_weight = weight
                    max_edge = (v, u)
        if max_edge[0] and max_edge[1]:
            g.delete_edge(max_edge[0], max_edge[1])
        return max_edge


    if __name__ == "__main__":
        g = GraphL()
        I = cv2.imread('sample.png', cv2.IMREAD_GRAYSCALE)
        height, width = I.shape

        for y in range(height):
            for x in range(width):
                idx = width * y + x
                v = Node(idx)
                v.color = I[y, x]
                g.insert_vertex(v)

        index_map = {}
        for v in g.vertices():
            index_map[v.key] = v

        for y in range(1, height - 1):
            for x in range(1, width - 1):
                idx = width * y + x
                current = index_map[idx]
                neighbors = [
                    (y - 1, x - 1), (y - 1, x), (y - 1, x + 1),
                    (y, x - 1), (y, x + 1),
                    (y + 1, x - 1), (y + 1, x), (y + 1, x + 1)
                ]
                for ny, nx in neighbors:
                    n_idx = width * ny + nx
                    neighbor = index_map[n_idx]
                    weight = abs(int(current.color) - int(neighbor.color))
                    g.insert_edge(current, neighbor, weight)

        mst_tree = g.mst()
        v1, v2 = remove_max_edge(mst_tree)

        IS = np.zeros((height, width), dtype='uint8')
        dfs_color(mst_tree, v1, 100, IS, width)
        dfs_color(mst_tree, v2, 200, IS, width)

        print("Rozmiar obrazu:", I.shape)
        print("Rozmiar obrazu:", IS.shape)
        scaled = cv2.resize(IS, None, fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
        cv2.imshow("Wynik", scaled)
        cv2.waitKey()
        cv2.destroyAllWindows()

