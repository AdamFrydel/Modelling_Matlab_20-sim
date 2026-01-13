import random
import time
import string

class Elem:
    def __init__(self, priorytet, dane  ):
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
    def __init__(self, to_sort=None):
        if to_sort is None:
            self.tab = []
            self.size = 0
        else:
            self.tab = to_sort
            self.size = len(to_sort)  # <- TO MUSI BYĆ
            for i in range(self.parent(self.size - 1), -1, -1):
                self.repairing(i)

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
        self.tab[0],self.tab[self.size - 1] = self.tab[self.size - 1], self.tab[0]
        self.size -= 1
        self.repairing(0)
        return taken_elem

    def repairing(self, index):
        while index < self.size:
            child_index = index * 2 + 1
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

    def heapsort(self):
        result = []
        original_size = self.size
        for _ in range(self.size):
            result.append(self.dequeue())
        self.size = original_size
        return result
    def print_tab(self):
        print('{', end=' ')
        print(*self.tab[:self.size], sep=', ', end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx])
            self.print_tree(self.left(idx), lvl + 1)




def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and not lst[j] < key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    lst = [x for x in lst if x is not None]
    return lst


def shell_sort(lst):
    nb_elem_3 = len(lst) // 3
    shell_nb = 0
    prev_shell = 0
    k = 1
    while shell_nb < nb_elem_3:
        prev_shell = shell_nb
        shell_nb = (3 ** k - 1) // 2
        k += 1
    shell_nb = prev_shell

    while shell_nb >= 1:
        for i in range(shell_nb, len(lst)):
            current = lst[i]
            j = i
            while j >= shell_nb and lst[j - shell_nb] < current:
                lst[j] = lst[j - shell_nb]
                j -= shell_nb
            lst[j] = current
        shell_nb = shell_nb // 3
    return lst




list_to_sort = []
list_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G','H','I','J']
list_nb = [5,5,7,2,5,1,7,5,1,2]

for i in range(0, len(list_letters)):
    list_to_sort.append(Elem(list_nb[i], list_letters[i]))

t_start = time.perf_counter()
list_insert = insertion_sort(list_to_sort.copy())
t_stop = time.perf_counter()
print("Czas obliczeń dla metody insert:", "{:.7f}".format(t_stop - t_start))
print("insertion:", list_insert)


t_start = time.perf_counter()

list_shell = shell_sort(list_to_sort.copy())
t_stop = time.perf_counter()
print("Czas obliczeń dla metody shell:", "{:.7f}".format(t_stop - t_start))

print("shell:", list_shell)



list_10000 = []

for i in range(10000):
    list_10000.append(Elem(random.randrange(0, 100), random.choice(string.ascii_uppercase)))

#sortowanie kopcem
t_start = time.perf_counter()
mound_test = MoundQueue(list_10000.copy())
t_stop = time.perf_counter()
print("Czas obliczeń dla metody kopcowania dla 10000 elementow:", "{:.7f}".format(t_stop - t_start))

#metoda insert
t_start = time.perf_counter()
list_insert = insertion_sort(list_10000.copy())
t_stop = time.perf_counter()
print("Czas obliczeń dla metody wstawiania dla 10000 elementow:", "{:.7f}".format(t_stop - t_start))


#metoda shell
t_start = time.perf_counter()
list_shell = shell_sort(list_10000.copy())
t_stop = time.perf_counter()
print("Czas obliczeń dla metody shell dla 10000 elementow:", "{:.7f}".format(t_stop - t_start))