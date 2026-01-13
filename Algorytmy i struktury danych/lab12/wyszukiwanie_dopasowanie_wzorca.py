import time

with open("lotr.txt", encoding='utf-8') as f:
    text = f.readlines()
S = ' '.join(text).lower()
W = "time."

d = 256
q = 101
def naive():

    i = 0
    counter = 0
    compare = 0
    while i <= len(S) - len(W):
        check_S_text = S[i:i+len(W) - 1]
        j = 0
        while j <= len(check_S_text) - 1:
            compare += 1
            if check_S_text[j] != W[j]:
                break
            if j == len(check_S_text) - 1 and check_S_text[j] == W[j]:
                counter += 1
            j += 1

        i += 1
    return counter,compare

def hash(word):
    hw = 0
    for i in range(len(word)):
        hw = (hw * d + ord(word[i])) % q
    return hw
def rabin_karp1(S, W):
    N = len(W)
    hW = hash(W)
    counter = 0
    compare = 0
    colizions = 0
    for m in range(len(S) - N + 1):
        hS = hash(S[m:m+N])
        compare += 1
        if hS == hW:
            if S[m:m+N] == W:
                counter += 1
            else:
                colizions += 1
    return counter, compare, colizions

def rabin_karp2(S, W):
    N = len(W)
    M = len(S)
    h = 1
    for i in range(N - 1):
        h = (h * d) % q

    hW = hash(W)
    hS = hash(S[:N])
    counter = 0
    compare = 1
    colizions = 0

    for m in range(M - N + 1):
        if hS == hW:
            if S[m:m+N] == W:
                counter += 1
            else:
                colizions += 1
        if m < M - N:
            hS = (d * (hS - ord(S[m]) * h) + ord(S[m + N])) % q
            if hS < 0:
                hS += q
            compare += 1
    return counter, compare, colizions


def T_var(W):
    T = [-1] + [0] * len(W)
    pos = 1
    cnd = 0
    while pos < len(W):
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos = pos + 1
        cnd = cnd + 1
    T[pos] = cnd
    return T

def kmp(S, W):
    m = 0
    i = 0
    T = T_var(W)
    P = []
    comparisons = 0
    while m < len(S):
        comparisons += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            if i == len(W):
                P.append(m - i)
                i = T[i]
        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1
    return len(P),comparisons, T


t_start = time.perf_counter()
counter, compare = naive()
t_stop = time.perf_counter()
print("Dla metody naiwnej")
print(f"{counter};{compare};{t_stop - t_start:.7f}")

t_start = time.perf_counter()
counter, compare, colizions = rabin_karp1(S, W)
t_stop = time.perf_counter()
print("Dla metody Rabin-Karp 1")
print(f"{counter};{compare};{colizions};{t_stop - t_start:.7f}")

t_start = time.perf_counter()
counter, compare, colizions = rabin_karp2(S, W)
t_stop = time.perf_counter()
print("Dla metody Rabin-Karp 2")
print(f"{counter};{compare};{colizions};{t_stop - t_start:.7f}")

start = time.time()
count, comparisons, T = kmp(S, W)
end = time.time()
print("Dla metody KMP")
print(f"{count};{comparisons};{T}")