class Node:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return isinstance(other, Node) and self.key == other.key

    def __repr__(self):
        return str(self.key)

    def __hash__(self):
        return hash(self.key)


class Matrix:
    def __init__(self, __matrix, parameter=0):
        if isinstance(__matrix, tuple):
            self.x = __matrix[0]
            self.y = __matrix[1]
            matrix = [[parameter for _ in range(self.y)] for _ in range(self.x)]
            self.__matrix = matrix
        else:
            self.x = len(__matrix)
            if not all(len(row) == len(__matrix[0]) for row in __matrix):
                raise ValueError("Wszystkie wiersze muszą mieć tę samą liczbę kolumn")
            self.y = len(__matrix[0]) if __matrix and __matrix[0] else 0
            self.__matrix = __matrix

    def __add__(self, other):
        if self.x == other.x and self.y == other.y:
            add_matrix = [[self.__matrix[i][j] + other.__matrix[i][j] for j in range(self.y)] for i in range(self.x)]
            return Matrix(add_matrix)
        else:
            raise ValueError("tych macierzy się nie da dodać")

    def __mul__(self, other):
        if self.y == other.x:
            mul_matrix = [[sum(self.__matrix[i][k] * other.__matrix[k][j] for k in range(self.y)) for j in range(other.y)] for i in range(self.x)]
            return Matrix(mul_matrix)
        else:
            raise ValueError("Tych macierzy nie da się pomnożyć")

    def transpose(self):
        matrix = [[self.__matrix[i][j] for i in range(self.x)] for j in range(self.y)]
        return Matrix(matrix)

    def __getitem__(self, item):
        return self.__matrix[item]

    def __setitem__(self, key, value):
        self.__matrix[key] = value

    def __eq__(self, other):
        return self.__matrix == other.__matrix

    def __str__(self):
        text_all = ""
        maximum = max(len(str(num)) for row in self.__matrix for num in row)
        for row in self.__matrix:
            text = "| " + " ".join(str(num).rjust(maximum) for num in row) + " |"
            text_all += text + "\n"
        return text_all.rstrip() + "\n"

    def size(self):
        return self.x, self.y

    def get_matrix(self):
        return self.__matrix

    def is_subgraph_isomorphism(self, G, P):
        MG = G.get_adjacency_matrix()
        MP = P.get_adjacency_matrix()
        MT = self.transpose()
        try:
            result = self * MG * MT
        except:
            return False
        return result == MP


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
            row.append(0)
        self.adj_matrix.append([0] * size)

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
        self.adj_matrix[i][j] = 0
        self.adj_matrix[j][i] = 0

    def neighbours(self, vertex):
        i = self.vertex_list.index(vertex)
        return [(self.vertex_list[j], self.adj_matrix[i][j]) for j in range(len(self.vertex_list)) if self.adj_matrix[i][j] != 0]

    def vertices(self):
        return self.vertex_list

    def get_adjacency_matrix(self):
        return Matrix(self.adj_matrix)


def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end=" -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end="; ")
        print()
    print("-------------------")


def ullman(matrix, graph_G, graph_P, act_row=0):
    global liczba_wywolan1, liczba_dopasowan1
    liczba_wywolan1 += 1

    if act_row == matrix.size()[0]:
        m = matrix
        MG = graph_G.get_adjacency_matrix()
        MP = graph_P.get_adjacency_matrix()
        MT = m.transpose()
        if m * MG * MT == MP:
            liczba_dopasowan1 += 1
            print("Znaleziono izomorfizm:")
            print(m)
        return

    for col in range(matrix.size()[1]):
        if all(matrix[i][col] == 0 for i in range(act_row)):
            matrix[act_row] = [0] * matrix.size()[1]
            matrix[act_row][col] = 1
            ullman(matrix, graph_G, graph_P, act_row + 1)
            matrix[act_row][col] = 0


def ullman2(M, G, P, act_row=0, M0=None, used_cols=None):
    global liczba_wywolan2, liczba_dopasowan2
    if used_cols is None:
        used_cols = [False] * len(G.vertices())
    if M0 is None:
        M0 = M

    liczba_wywolan2 += 1

    if act_row >= len(P.vertices()):
        if M.is_subgraph_isomorphism(G, P):
            liczba_dopasowan2 += 1
        return

    for col in range(len(G.vertices())):
        if not used_cols[col] and M0[act_row][col] != 0:
            m_copy = Matrix([row[:] for row in M.get_matrix()])
            m_copy[act_row] = [0] * len(G.vertices())
            m_copy[act_row][col] = 1
            used_cols[col] = True
            ullman2(m_copy, G, P, act_row + 1, M0, used_cols)
            used_cols[col] = False


def prune(M, G, P):
    change = True
    while change:
        change = False
        for i in range(M.size()[0]):
            for j in range(M.size()[1]):
                if M[i][j] == 1:
                    for k in range(M.size()[0]):
                        if k == i:
                            continue
                        has_support = False
                        for l in range(M.size()[1]):
                            if M[k][l] == 1:
                                if P.get_adjacency_matrix()[i][k] <= G.get_adjacency_matrix()[j][l]:
                                    has_support = True
                                    break
                        if not has_support:
                            M[i][j] = 0
                            change = True
                            break


def ullman3(M, G, P, act_row=0, used_cols=None):
    global liczba_wywolan3, liczba_dopasowan3
    if used_cols is None:
        used_cols = [False] * len(G.vertices())

    liczba_wywolan3 += 1

    if act_row == M.size()[0]:
        if M.is_subgraph_isomorphism(G, P):
            liczba_dopasowan3 += 1
        return

    for col in range(M.size()[1]):
        if not used_cols[col] and M[act_row][col] == 1:
            m_copy = Matrix([row[:] for row in M.get_matrix()])
            m_copy[act_row] = [0] * M.size()[1]
            m_copy[act_row][col] = 1
            used_cols[col] = True
            prune(m_copy, G, P)
            ullman3(m_copy, G, P, act_row + 1, used_cols)
            used_cols[col] = False


def create_M0(graph_P, graph_G):
    m0 = Matrix((len(graph_P.vertices()), len(graph_G.vertices())))
    for i, vp in enumerate(graph_P.vertices()):
        deg_p = len(graph_P.neighbours(vp))
        for j, vg in enumerate(graph_G.vertices()):
            deg_g = len(graph_G.neighbours(vg))
            if deg_p <= deg_g:
                m0[i][j] = 1
    return m0


if __name__ == "__main__":
    liczba_wywolan1 = 0
    liczba_dopasowan1 = 0
    liczba_wywolan2 = 0
    liczba_dopasowan2 = 0
    liczba_wywolan3 = 0
    liczba_dopasowan3 = 0

    graph_1 = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
    graph_2 = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]

    graph_G = GraphM()
    for letter in ['A', 'B', 'C', 'D', 'E', 'F']:
        graph_G.insert_vertex(letter)
    for a, b, w in graph_1:
        graph_G.insert_edge(a, b, w)

    graph_P = GraphM()
    for letter in ['A', 'B', 'C']:
        graph_P.insert_vertex(letter)
    for a, b, w in graph_2:
        graph_P.insert_edge(a, b, w)

    print("Algorytm Ullman 1.0")
    M1 = Matrix((len(graph_P.vertices()), len(graph_G.vertices())))
    ullman(M1, graph_G, graph_P)
    print(f"Liczba wywołań: {liczba_wywolan1}")
    print(f"Liczba dopasowań: {liczba_dopasowan1}")

    print("\nAlgorytm Ullman 2.0")
    M0 = create_M0(graph_P, graph_G)
    ullman2(M0, graph_G, graph_P, M0=M0)
    print(f"Liczba wywołań: {liczba_wywolan2}")
    print(f"Liczba dopasowań: {liczba_dopasowan2}")

    print("\nAlgorytm Ullman 3.0")
    M0_filtered = create_M0(graph_P, graph_G)
    prune(M0_filtered, graph_G, graph_P)
    ullman3(M0_filtered, graph_G, graph_P)
    print(f"Liczba wywołań: {liczba_wywolan3}")
    print(f"Liczba dopasowań: {liczba_dopasowan3}")
