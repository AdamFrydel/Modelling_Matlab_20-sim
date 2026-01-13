# with open('text.txt', 'r') as plik:
#     reader = plik.readlines()
# print(reader)

#zad 2
n = 5
with open('text.txt', 'r') as plik:
    for _ in range(n):
        linia = plik.readline()
        if not linia:
            break  # koniec pliku
        print(linia.strip())