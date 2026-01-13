from macierz import macierz, transpose_matrix, determinant_chio, laplace_method

# m1 = macierz(
#     [[1, 0, 2],
#      [-1, 3, 1]]
# )
#
# m2 = macierz(
#     [[1, 1, 1],
#      [1, 1, 1]]
# )
#
# m3 = macierz(
#     [[3, 1],
#      [2, 1],
#      [1, 0]]
# )
#
#
#
# transposed_m1 = transpose_matrix(m1)
# print(m1)
# print(transposed_m1)
#
# print(m1 + m2)
# print(m1 * m3)

m4 = macierz([

[5 , 1 , 1 , 2 , 3],

[4 , 2 , 1 , 7 , 3],

[2 , 1 , 2 , 4 , 7],

[9 , 1 , 0 , 7 , 0],

[1 , 4 , 7 , 2 , 2]

])
print(determinant_chio(m4))

m5 = macierz([
    [0, 1, 1, 2, 3],
    [4, 2, 1, 7, 3],
    [2, 1, 2, 4, 7],
    [9, 1, 0, 7, 0],
    [1, 4, 7, 2, 2]
])
print(laplace_method(m5))