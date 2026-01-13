class Object:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class Uczelnie:
    def __init__(self):
        self.head = None
        self.tail = None

    def destroy(self):
        while self.head is not None:
            temp = self.head
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            del temp
        self.tail = None

    def add(self,data):
        new_object = Object(data)
        new_object.next = self.head
        if self.head is not None:
            self.head.prev = new_object
        self.head = new_object
        if self.tail is None:
            self.tail = self.head

    def append(self,data):
        if self.head is None:
            self.head = Object(data)
            self.tail = self.head
            return
        new_object = Object(data)
        self.tail.next = new_object
        new_object.prev = self.tail
        self.tail = new_object

    def remove(self):
        if self.head is None:
            return None
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
    def remove_end(self):
        if self.tail is None:
            return
        if self.head == self.tail:
            self.remove()
            return
        self.tail = self.tail.prev
        self.tail.next = None


    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def length(self):
        new_object = self.head
        length = 0
        while new_object is not None:
            length += 1
            new_object = new_object.next
        print("Długość listy to", length)
        return length
    def get(self):
        if self.head is None:
            return None
        return self.head.data
    def print(self):
        if self.head is None:
            print('None')
            return
        new_object = self.head
        string = ""
        while new_object is not None:
            string += f"-> {new_object.data}\n"
            new_object = new_object.next
        print(string.rstrip("->"))

    def print_last(self):
        if self.tail is None:
            print('None')
            return
        new_object = self.tail
        str = ""
        while new_object is not None:
            str += f"-> {new_object.data}\n"
            new_object = new_object.prev
        print(str.rstrip("->"))




check_list = [('AGH', 'Kraków', 1919),
              ('UJ', 'Kraków', 1364),
              ('PW', 'Warszawa', 1915),
              ('UW', 'Warszawa', 1915),
              ('UP', 'Poznań', 1919),
              ('PG', 'Gdańsk', 1945)]

obj1 = check_list[0]
obj2 = check_list[1]
obj3 = check_list[2]
obj4 = check_list[3]
obj5 = check_list[4]


uczelnie = Uczelnie()
uczelnie.append(check_list[0])
uczelnie.append(check_list[1])
uczelnie.append(check_list[2])
uczelnie.add(check_list[3])
uczelnie.add(check_list[4])

uczelnie.print()
uczelnie.print_last()
uczelnie.length()

uczelnie.remove()
print("Pierwszy element nowej listy to:", uczelnie.get(), "\n")
uczelnie.remove_end()

uczelnie.print()
uczelnie.print_last()
uczelnie.destroy()
print(uczelnie.is_empty())

uczelnie.remove()
uczelnie.remove_end()
uczelnie.append(check_list[0])
uczelnie.remove_end()
print(uczelnie.is_empty())













