import numpy as np
def rec_var(P,T,i = None , j = None):
    if i is None or j is None:
        i = len(P)
        j = len(T)

    if i == 0:
        return j
    if j == 0 :
        return i


    if T[j - 1] == P[i - 1]:
        cost = 0
    else:
        cost = 1

    insert_cost = 1 + rec_var(P,T,i,j - 1)
    del_cost = 1 + rec_var(P,T,i -1,j )
    exc_cost = cost + rec_var(P,T,i - 1,j - 1)

    return min(insert_cost,del_cost,exc_cost)

print("Różnica pomiędzy kotem a psem dla wariantu rekurencyjnego")
P = ' kot'
T = ' pies'

print(rec_var(P,T))

def pd(P,T,i = None , j = None):
    D = np.zeros((len(P)+1, len(T)+1), dtype=int)
    if i is None or j is None:
        i = len(P)
        j = len(T)

    for ii in range(len(T) + 1):
        D[0][ii] = ii
    for ii in range(len(P) + 1):
        D[ii][0] = ii

    X = np.full((len(P) + 1, len(T) + 1), "X", dtype=str)
    for jj in range(1, len(T) + 1):
        X[0][jj] = "I"
    for ii in range(1, len(P) + 1):
        X[ii][0] = "D"

    for ii in range(1, len(P) + 1):
        for jj in range(1, len(T) + 1):
            insert_cost = 1 + D[ii][jj-1]
            del_cost = 1 + D[ii - 1][jj]
            exc_cost = D[ii - 1][jj - 1] + (P[ii - 1]!=T[jj - 1])
            D[ii][jj] = min(insert_cost,del_cost,exc_cost)
            if P[ii - 1] == T[jj - 1]:
                X[ii][jj] = "M"
            elif D[ii][jj] == exc_cost:
                X[ii][jj] = "S"
            elif D[ii][jj] == insert_cost:
                X[ii][jj] = "I"
            else:
                X[ii][jj] = "D"

    lista = []
    a = X[len(P)][len(T)]
    i = len(P)
    j = len(T)
    while a != "X" :
        lista.append(a)
        if a == "S" or a == "M":
            i = i - 1
            j = j - 1
            a = X[i][j]
        elif a == "I":
            j = j - 1
            a = X[i][j]
        elif a == "D":
            i = i - 1
            a = X[i][j]


    lista.reverse()
    lista = ''.join(lista)
    print(lista)
    return D[len(P)][len(T)]
print("---------------------------------")

print("autobusy oraz you should not dla metody pd")
P1 = ' biały autobus'
T1 = ' czarny autokar'
print(pd(P1,T1))

P2 = ' thou shalt not'
T2 = ' you should not'

print(pd(P2,T2))

def wysz_podc(P,T,i = None , j = None):
    global min_index
    D = np.zeros((len(P)+1, len(T)+1), dtype=int)
    if i is None or j is None:
        i = len(P)
        j = len(T)

    # for ii in range(len(T) + 1):
    #     D[0][ii] = ii
    for ii in range(len(P) + 1):
        D[ii][0] = ii

    X = np.full((len(P) + 1, len(T) + 1), "X", dtype=str)
    # for jj in range(1, len(T) + 1):
    #     X[0][jj] = "I"
    for ii in range(1, len(P) + 1):
        X[ii][0] = "D"

    for ii in range(1, len(P) + 1):
        for jj in range(1, len(T) + 1):
            insert_cost = 1 + D[ii][jj-1]
            del_cost = 1 + D[ii - 1][jj]
            exc_cost = D[ii - 1][jj - 1] + (P[ii - 1]!=T[jj - 1])
            D[ii][jj] = min(insert_cost,del_cost,exc_cost)
            if P[ii - 1] == T[jj - 1]:
                X[ii][jj] = "M"
            elif D[ii][jj] == exc_cost:
                X[ii][jj] = "S"
            elif D[ii][jj] == insert_cost:
                X[ii][jj] = "I"
            else:
                X[ii][jj] = "D"

    # lista = []
    # a = X[len(P)][len(T)]
    # i = len(P)
    # j = len(T)
    # while a != "X" :
    #     lista.append(a)
    #     if a == "S" or a == "M":
    #         i = i - 1
    #         j = j - 1
    #         a = X[i][j]
    #     elif a == "I":
    #         j = j - 1
    #         a = X[i][j]
    #     elif a == "D":
    #         i = i - 1
    #         a = X[i][j]
    minimum = float('inf')
    for ii in range(len(D[len(P)])):
        if D[len(P)][ii] < minimum:
            minimum = D[len(P)][ii]
            min_index = ii
    start_index = min_index - len(P) + 1

    # lista.reverse()
    # lista = ''.join(lista)
    # print(lista)
    return start_index

P3 = ' ban'
T3 = ' mokeyssbanana'
print("---------------------------------")
print("Szukanie ban dla metody wyszukiwania podciągów")
print(wysz_podc(P3,T3))

def najdl_sekw(P,T,i = None , j = None):
    D = np.zeros((len(P)+1, len(T)+1), dtype=int)
    if i is None or j is None:
        i = len(P)
        j = len(T)

    for ii in range(len(T) + 1):
        D[0][ii] = 0
    for ii in range(len(P) + 1):
        D[ii][0] = 0

    X = np.full((len(P) + 1, len(T) + 1), "X", dtype=str)
    for jj in range(1, len(T) + 1):
        X[0][jj] = "X"
    for ii in range(1, len(P) + 1):
        X[ii][0] = "X"

    for ii in range(1, len(P) + 1):
        for jj in range(1, len(T) + 1):
            if P[ii - 1] == T[jj - 1]:
                D[ii][jj] = D[ii - 1][jj - 1] + 1
                X[ii][jj] = "M"
            elif D[ii - 1][jj] >= D[ii][jj - 1]:
                D[ii][jj] = D[ii - 1][jj]
                X[ii][jj] = "D"
            else:
                D[ii][jj] = D[ii][jj - 1]
                X[ii][jj] = "I"

    lista = []
    a = X[len(P)][len(T)]
    i = len(P)
    j = len(T)
    while i > 0 and j > 0:
        a = X[i][j]
        if  a == "M":
            lista.append(P[i - 1])
            i = i - 1
            j = j - 1
            a = X[i][j]
        elif a == "I":
            j = j - 1

        elif a == "D":
            i = i - 1
    lista.reverse()
    print(''.join(lista))

P4 = ' democrat'
T4 = ' republican'
print("---------------------------------")
print("Szukanie najdłuższej zgodności")
najdl_sekw(P4,T4)
print("---------------------------------")
print("Szukanie podsekwencji monotonicznej")
T = ' 243517698'
P = ' ' + ''.join(sorted(T[1:]))

najdl_sekw(P, T)