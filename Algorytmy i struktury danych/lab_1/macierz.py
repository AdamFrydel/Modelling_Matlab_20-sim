class macierz:
    def __init__(self,__matrix,parameter = 0):

        if isinstance(__matrix,tuple):
            self.x = __matrix[0]
            self.y = __matrix[1]
            matrix = [[parameter for i in range(self.y)] for j in range(self.x)]

            self.__matrix = matrix

        else:

            self.x = len(__matrix)
            if not all(len(row) == len(__matrix[0]) for row in __matrix):
                raise ValueError("Wszystkie wiersze muszą mieć tę samą liczbę kolumn")
            self.y = len(__matrix[0]) if __matrix and __matrix[0] else 0
            self.__matrix = __matrix


    def __add__(self, other):
        if self.x == other.x and self.y == other.y:
            add_matrix = [[0 for i in range(self.y)] for j in range(self.x)]
            for i in range(self.x):
                for j in range(self.y):
                    add_matrix[i][j] = self.__matrix[i][j]+other.__matrix[i][j]
            return macierz(add_matrix)
        else:
            raise ValueError("tych macierzy się nie da dodac")

    def __mul__(self, other):
        if self.y == other.x:
            mul_matrix = [[0 for j in range(other.y)] for i in range(self.x)]
            for i in range(self.x):
                for j in range(other.y):
                    mul_matrix[i][j] = sum(self.__matrix[i][k] * other.__matrix[k][j] for k in range(self.y))
            return macierz(mul_matrix)
        else:
            raise ValueError("Tych macierzy nie da się pomnożyć")

    def __getitem__(self, item):
        if isinstance(item,tuple) and len(item) == 2:
            i, j = item
            return self.__matrix[i][j] if 0 <= i < self.x and 0 <= j < self.y else 0
        else:
            raise TypeError("To nie jest indeks")

    def __str__(self):
        text_all = ""
        maximum = max(len(str(num)) for row in self.__matrix for num in row)

        for row in self.__matrix:
            text = "| " + " ".join(str(num).rjust(maximum) for num in row) + " |"
            text_all += text + "\n"

        return text_all.rstrip() + "\n"


    def size(self):
        return self.x,self.y

    def get_matrix(self):
        return self.__matrix

def transpose_matrix(matrix):
    mat = matrix.get_matrix()
    if not mat or not mat[0]:
        raise ValueError("To nie jest macierz")
    x = len(mat())
    y = len(mat[0])
    new_matrix = [[0 for j in range(x)] for i in range(y)]
    for i in range(x):
        for j in range(y):
            new_matrix[j][i] = mat()[i][j]
    return macierz(new_matrix)


def determinant_chio(matrix):
    mat = matrix.get_matrix()
    n = len(mat)
    if len(mat) != len(mat[0]):
        raise ValueError("To nie jest macierz kwadratowa - nie da się obliczyć jej wyznacznika metoda Chio")
    if n == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

    if mat[0][0] == 0:
        raise ValueError("pierwszy element macierzy nie może być równy 0")

    sub_matrix = [[0 for i in range(n - 1)] for j in range(n - 1)]
    for i in range(1, n):
        for j in range(1, n):
            sub_matrix[i - 1][j - 1] = mat[i][j] * mat[0][0] - mat[i][0] * mat[0][j]

    return determinant_chio(macierz(sub_matrix)) / (mat[0][0] ** (n - 2))

def laplace_method(matrix):
    mat = matrix.get_matrix()

    n = len(mat)
    if len(mat) != len(mat[0]):
        raise ValueError("To nie jest macierz kwadratowa")
    if n == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    coeff = -1
    suma_list = []
    for i in range(n):
            coeff = coeff * (-1)
            sub_matrix = [row[1:] for row in mat[:i] + mat[i+1:]]
            suma_list.append(laplace_method(macierz(sub_matrix)) * (coeff * mat[i][0]))
    suma = sum(suma_list)
    return suma














