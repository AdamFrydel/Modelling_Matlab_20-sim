class Elem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key}:{self.value}"

class Mixing:
    def __init__(self, size, c1=1, c2=0):
        self.c1 = c1
        self.c2 = c2
        self.size = size
        self.tab = [Elem(None, None) for _ in range(size)]

    def mixing(self, number):
        if isinstance(number, str):
            return sum(ord(char) for char in number) % self.size
        elif isinstance(number, int):
            return number % self.size
        else:
            raise ValueError("Number must be either str or int")

    def colision(self, key, tries_nb):
        return (self.mixing(key) + self.c1 * tries_nb + self.c2 * tries_nb**2) % self.size

    def search(self, key):
        key_hash = self.mixing(key)
        try_count = 0
        while try_count < self.size:
            if self.tab[key_hash].key == key:
                return self.tab[key_hash].value

            try_count += 1
            key_hash = self.colision(key, try_count)
        return None

    def insert(self, key, value):
        ind = self.mixing(key)
        try_count = 0
        while try_count < self.size:
            if self.tab[ind].key is None or self.tab[ind].key == key:
                self.tab[ind] = Elem(key, value)
                return
            try_count += 1
            ind = self.colision(key, try_count)
        print("Brak miejsca dla key i value",key, value)




    def remove(self, key):
        try:
            ind = self.mixing(key)
            try_count = 0
            while try_count < self.size:
                if self.tab[ind].key == key:
                    self.tab[ind] = Elem(None, None)
                    return True
                try_count += 1
                ind = self.colision(key, try_count)
            print("Brak danej")
        except KeyError:
            print("Brak danej")

    def __str__(self):
        return str([f"{elem.key}:{elem.value}" if elem.key is not None else "None:None" for elem in self.tab])


def sprawdzenie_1(c1,c2):
    tab_mix = Mixing(13, c1, c2)
    for i in range(15):
        key = i + 1
        if i == 5:
            key = 18
        elif i == 6:
            key = 31
        tab_mix.insert(key, chr(ord('A') + i))
    print(tab_mix)
    print(tab_mix.search(5))
    print(tab_mix.search(14))
    tab_mix.insert(5, 'Z')
    print(tab_mix.search(5))
    tab_mix.remove(5)
    print(tab_mix)
    print(tab_mix.search(31))
    tab_mix.insert('test', 'W')
    print(tab_mix)

print("DZIAŁANIE PIERWSZEJ FUNKCJI Z PRÓBKOWANIEM LINIOWYM")
sprawdzenie_1(1,0)


def sprawdzenie_2(c1,c2):

    tab_mix2 = Mixing(13, c1, c2)
    for i in range(0,182,13):
        key = i + 13
        tab_mix2.insert(key, chr(ord('A') + i // 13))
    print(tab_mix2)

print("DZIAŁANIE DRUGIEJ FUNKCJI Z PRÓBKOWANIEM LINIOWYM")

sprawdzenie_2(1,0)
print("DZIAŁANIE DRUGIEJ FUNKCJI Z PRÓBKOWANIEM KWADRATOWYM")

sprawdzenie_2(0,1)
print("DZIAŁANIE PIERWSZEJ FUNKCJI Z PRÓBKOWANIEM KWADRATOWYM")
sprawdzenie_1(0,1)
