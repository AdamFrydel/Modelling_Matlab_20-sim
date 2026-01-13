import time
with open("lotr.txt", encoding='utf-8') as f:
    text = f.readlines()

S = ' '.join(text).lower()

W_list = ['gandalf', 'looking', 'blocked', 'comment', 'pouring', 'finally',
          'hundred', 'hobbits', 'however', 'popular', 'nothing', 'enjoyed',
          'stuffed', 'relaxed', 'himself', 'present', 'deliver', 'welcome',
          'baggins', 'further']

d = 256
q = 101


def hash(word):
    hw = 0
    for i in range(len(word)):
        hw = (hw * d + ord(word[i])) % q
    return hw


def rabin_karp_multi(S, W_list):
    N = len(W_list[0])
    M = len(S)

    # precompute d^(N-1) % q
    h = 1
    for i in range(N - 1):
        h = (h * d) % q

    pattern_hashes = {}
    for word in W_list:
        hw = hash(word)
        if hw not in pattern_hashes:
            pattern_hashes[hw] = []
        pattern_hashes[hw].append(word)

    counts = {word: 0 for word in W_list}
    collisions = 0
    comparisons = 0

    hS = hash(S[:N])

    for m in range(M - N + 1):
        if hS in pattern_hashes:
            for pat in pattern_hashes[hS]:
                comparisons += 1
                if S[m:m + N] == pat:
                    counts[pat] += 1
                else:
                    collisions += 1
        if m < M - N:
            hS = (d * (hS - ord(S[m]) * h) + ord(S[m + N])) % q
            if hS < 0:
                hS += q

    return counts, comparisons, collisions



start1 = time.time()
rabin_karp_multi(S, ['gandalf'])
end1 = time.time()
czas1 = end1 - start1

start2 = time.time()
rabin_karp_multi(S, W_list)
end2 = time.time()
czas2 = end2 - start2

print("Test 1:")
print(f"Czas dla jednego wzorca: {czas1:.6f} s")
print(f"Czas dla wszystkich wzorców: {czas2:.6f} s")

counts, comparisons, collisions = rabin_karp_multi(S, W_list)

print("\nTest 2:")
for word in W_list:
    print(f"{word}: {counts[word]}")

print(f"\nLiczba wszystkich poprawnie znalezionych wzorców: {sum(counts.values())}")
print(f"Liczba detekcji fałszywie pozytywnych: {collisions}")
