class ElemUnrolled:
    SIZE = 6

    def __init__(self):
        self.list = [None] * self.SIZE
        self.actFill = 0
        self.nextElem = None

    def add_elem(self, ind, elem):
        if ind < 0 or ind > self.actFill:
            raise IndexError("Indeks poza zakresem")

        if self.actFill < self.SIZE:
            for i in range(self.actFill, ind, -1):
                self.list[i] = self.list[i - 1]
            self.list[ind] = elem
            self.actFill += 1
        else:
            mid = self.SIZE // 2
            self.nextElem = ElemUnrolled()
            self.nextElem.list[:self.SIZE - mid] = self.list[mid:]
            self.nextElem.actFill = self.SIZE - mid
            self.list[mid:] = [None] * (self.SIZE - mid)
            self.actFill = mid

            if ind < mid:
                self.add_elem(ind, elem)
            else:
                self.nextElem.add_elem(ind - mid, elem)

    def cancel_elem(self, ind):
        if ind >= self.actFill or ind < 0:
            raise IndexError("Indeks poza zakresem")

        for i in range(ind, self.actFill - 1):
            self.list[i] = self.list[i + 1]

        self.list[self.actFill - 1] = None
        self.actFill -= 1

        if self.actFill < self.SIZE // 2 and self.nextElem is not None:
            list_of_elems = []

            for i in range(min(self.SIZE - self.actFill, self.nextElem.actFill)):
                list_of_elems.append(self.nextElem.list[i])
                self.nextElem.list[i] = None
                self.nextElem.actFill -= 1

            for i in range(len(list_of_elems)):
                if self.actFill + i < self.SIZE:
                    self.list[self.actFill + i] = list_of_elems[i]

            self.actFill += len(list_of_elems)

            if self.nextElem.actFill == 0:
                self.nextElem = self.nextElem.nextElem

class UnrolledList:
    def __init__(self):
        self.head = ElemUnrolled()
        self.size = 0

    def get(self, ind):
        total_elements = 0
        current_elem = self.head
        while current_elem:
            if total_elements + current_elem.actFill > ind:
                return current_elem.list[ind - total_elements]
            total_elements += current_elem.actFill
            current_elem = current_elem.nextElem
        raise IndexError("Indeks poza zakresem")

    def insert(self, ind, elem):
        total_elements = 0
        current_elem = self.head
        prev_elem = None
        while current_elem:
            if total_elements + current_elem.actFill > ind:
                current_elem.add_elem(ind - total_elements, elem)
                return
            total_elements += current_elem.actFill
            prev_elem = current_elem
            current_elem = current_elem.nextElem

        prev_elem.add_elem(prev_elem.actFill, elem)

    def delete(self, ind):
        total_elements = 0
        current_elem = self.head
        while current_elem:
            if total_elements + current_elem.actFill > ind:
                current_elem.cancel_elem(ind - total_elements)
                return
            total_elements += current_elem.actFill
            current_elem = current_elem.nextElem

    def __str__(self):
        result = []
        current_elem = self.head
        while current_elem:
            result.append("[")
            for i in current_elem.list:
                result.append(str(i))
            result.append("]")
            current_elem = current_elem.nextElem
        return " ".join(result)


moja_lista = UnrolledList()
for i in range(9):
    moja_lista.insert(i, i + 1)

print( moja_lista.get(4))

moja_lista.insert(1, 10)
moja_lista.insert(8, 11)
print(moja_lista)

moja_lista.delete(1)
moja_lista.delete(2)

print( moja_lista)
