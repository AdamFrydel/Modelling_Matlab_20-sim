class Elem:
    def __init__(self, dane, priorytet):
        self.__dane = dane
        self.__priorytet = priorytet

    def __lt__(self, other):
        return self.__priorytet < other.__priorytet

    def __gt__(self, other):
        return self.__priorytet > other.__priorytet

    def __eq__(self, other):
        return self.__priorytet == other.__priorytet
    def __repr__(self):
        return f"{self.__priorytet} : {self.__dane}"


class MoundQueue:
    def __init__(self):
        self.size = 0
        self.tab = []

    def is_empty(self):
        return self.size == 0

    def peek(self):
        return None if self.is_empty() else self.tab[0]

    def left(self, ind):
        return 2 * ind + 1

    def right(self, ind):
        return 2 * ind + 2

    def parent(self, ind):
        return (ind - 1) // 2

    def dequeue(self):
        if self.is_empty():
            return None
        taken_elem = self.tab[0]
        self.tab[0] = self.tab[self.size - 1]
        self.size -= 1
        self.repairing(0)
        return taken_elem

    def repairing(self, index):
        while index < self.size:
            child_index = index * 2
            if child_index < self.size - 1 and self.tab[child_index] < self.tab[child_index + 1]:
                child_index += 1

            if child_index < self.size and self.tab[child_index] > self.tab[index]:
                self.tab[index], self.tab[child_index] = self.tab[child_index], self.tab[index]
                index = child_index
            else:
                break

    def enqueue(self, elem):
        if self.size == len(self.tab):
            self.tab.append(elem)
        else:
            self.tab[self.size] = elem
        self.size += 1

        ind = self.size - 1
        while ind > 0 and self.tab[self.parent(ind)] < self.tab[ind]:
            p = self.parent(ind)
            self.tab[ind], self.tab[p] = self.tab[p], self.tab[ind]
            ind = p

    def print_tab(self):
        print('{', end=' ')
        print(*self.tab[:self.size], sep=', ', end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx])
            self.print_tree(self.left(idx), lvl + 1)


moja_kolejka = MoundQueue()
nb_list = [7, 5, 1, 2, 5, 3, 4, 8, 9]

let_list = "GRYMOTYLA"

for number in range(len(nb_list)):
    elem = Elem(let_list[number], nb_list[number])
    moja_kolejka.enqueue(elem)

moja_kolejka.print_tree(0,0)
moja_kolejka.print_tab()

remembered_value = moja_kolejka.dequeue()
print(remembered_value)
print(moja_kolejka.peek())

moja_kolejka.print_tab()

print(remembered_value)

while moja_kolejka.is_empty() is False:
    print(moja_kolejka.dequeue())

moja_kolejka.print_tab()



