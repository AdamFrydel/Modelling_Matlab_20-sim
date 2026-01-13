import random
import time
class Elem:
    def __init__(self, priorytet, dane ):
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
        for i in range(self.size - 1, 0, -1):
            self.tab[0], self.tab[i] = self.tab[i], self.tab[0]
            self.size -= 1
            self.repairing(0)
        self.size = len(self.tab)
        return self.tab
    def print_tab(self):
        print('{', end=' ')
        print(*self.tab[:self.size], sep=', ', end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx])
            self.print_tree(self.left(idx), lvl + 1)


#test 1 dla algorytmu

list_to_mound = [Elem(key, value) for key,value in [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
mound_test = MoundQueue(list_to_mound)

mound_test.print_tab()
mound_test.print_tree(0, 0)
print(mound_test.heapsort())

print("NIESTABILNE")


def swap(list):
    if list is None:
        return None

    for i in range(len(list)):
        max_value = i
        for j in range(i + 1, len(list)):
            if list[max_value] > list[j]:
                max_value = j
        list[i], list[max_value] = list[max_value], list[i]


def shift(list):
    if list is None:
        return None
    for i in range(len(list)):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        min_value = list.pop(min_index)
        list.insert(i, min_value)



original = [Elem(5,'A'), Elem(5,'B'), Elem(7,'C'), Elem(2,'D'), Elem(5,'E'), Elem(1,'F'), Elem(7,'G'), Elem(5,'H'), Elem(1,'I'), Elem(2,'J')]

# test SWAP
data_swap = original.copy()
swap(data_swap)
print("Po sortowaniu swap:", data_swap)

print("NIESTABILNE" )

# test SHIFT
data_shift = original.copy()
shift(data_shift)
print("Po sortowaniu shift:", data_shift)

print("STABILNE")

# --- TEST 2: Pomiar czasu dla sortowania 10 000 liczb ---

arr = [int(random.random() * 100) for _ in range(10000)]

mound = MoundQueue(original)
t_start = time.perf_counter()
sorted_mound = mound.heapsort()
t_stop = time.perf_counter()
print("Czas obliczeń (kopiec):", "{:.7f}".format(t_stop - t_start))

swap_arr = arr.copy()
t_start = time.perf_counter()
swap(swap_arr)
t_stop = time.perf_counter()
print("Czas obliczeń (swap):", "{:.7f}".format(t_stop - t_start))

shift_arr = arr.copy()
t_start = time.perf_counter()
shift(shift_arr)
t_stop = time.perf_counter()
print("Czas obliczeń (shift):", "{:.7f}".format(t_stop - t_start))