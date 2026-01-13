def orientacja(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

def dystans_kw(p, q):
    return (p[0] - q[0])**2 + (p[1] - q[1])**2

def convex_hull_corrected(punkty):
    if len(punkty) < 3:
        return punkty[:]

    start = min(punkty, key=lambda p: (p[0], p[1]))
    p = start
    otoczka = []

    while True:
        otoczka.append(p)
        q = None
        for r in punkty:
            if r == p:
                continue
            if q is None:
                q = r
                continue
            val = orientacja(p, q, r)
            if val < 0:
                q = r
            elif val == 0:
                if dystans_kw(p, r) > dystans_kw(p, q):
                    q = r
        if q == start:
            break
        p = q

    return otoczka


# Testy
punkty1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
punkty2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]
punkty3 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]

print("Otoczka punkty1:", convex_hull_corrected(punkty1))
print("Otoczka punkty2:", convex_hull_corrected(punkty2))
print("Otoczka punkty3:", convex_hull_corrected(punkty3))
