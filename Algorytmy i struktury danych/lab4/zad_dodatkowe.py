import random

class Node:
    def __init__(self, key, data, level):
        self.key = key
        self.data = data
        self.level = level
        self.tab = [None] * level

class SkipList:
    def __init__(self, max_level):
        self.max_level = max_level
        self.head = Node(-1, None, max_level)

    def randomlevel(self, p=0.5):
        lvl = 1
        while random.random() < p and lvl < self.max_level:
            lvl += 1
        return lvl

    def search_recursive(self, node, level, key):
        if level < 0:
            return None

        if node.tab[level] and node.tab[level].key < key:
            return self.search_recursive(node.tab[level], level, key)
        elif node.tab[level] and node.tab[level].key == key:
            return node.tab[level].data
        else:
            return self.search_recursive(node, level - 1, key)

    def search(self, key):
        return self.search_recursive(self.head, self.max_level - 1, key)

    def insert(self, key, data):
        def find_predecessors(node, level, key, predecessors=None):
            if predecessors is None:
                predecessors = [None] * self.max_level
            if level < 0:
                return predecessors
            while node.tab[level] and node.tab[level].key < key:
                node = node.tab[level]
            predecessors[level] = node
            return find_predecessors(node, level - 1, key, predecessors)

        predecessors = find_predecessors(self.head, self.max_level - 1, key)
        next_node = predecessors[0].tab[0]

        if next_node and next_node.key == key:
            next_node.data = data
        else:
            lvl = self.randomlevel()
            new_node = Node(key, data, lvl)
            for i in range(lvl):
                new_node.tab[i], predecessors[i].tab[i] = predecessors[i].tab[i], new_node

    def remove(self, key):
        def find_predecessors(node, level, key, predecessors=None):
            if predecessors is None:
                predecessors = [None] * self.max_level
            if level < 0:
                return predecessors
            while node.tab[level] and node.tab[level].key < key:
                node = node.tab[level]
            predecessors[level] = node
            return find_predecessors(node, level - 1, key, predecessors)

        predecessors = find_predecessors(self.head, self.max_level - 1, key)
        target = predecessors[0].tab[0]

        if target and target.key == key:
            for i in range(len(target.tab)):
                if predecessors[i].tab[i] == target:
                    predecessors[i].tab[i] = target.tab[i]

    def __str__(self):
        node = self.head.tab[0]
        result = []
        while node:
            result.append(f"({node.key}:{node.data})")
            node = node.tab[0]
        return " -> " .join(result)

    def displaylist(self):
        node = self.head.tab[0]
        keys = []
        while node:
            keys.append(node.key)
            node = node.tab[0]
        for lvl in range(self.max_level - 1, -1, -1):
            print(f"{lvl}  ", end=" ")
            node = self.head.tab[lvl]
            idx = 0
            while node:
                while idx < len(keys) and node.key > keys[idx]:
                    print("     ", end="")
                    idx += 1
                idx += 1
                print(f"{node.key:2d}:{str(node.data):2s}", end=" ")
                node = node.tab[lvl]
            print()

#Pierwszy wariant
random.seed(42)
skip_list = SkipList(4)
for i in range(15):
    key = i + 1
    skip_list.insert(key, chr(ord('A') + i))
print(skip_list)
print(skip_list.search(2))


skip_list.insert(2, 'Z')
print(skip_list.search(2))


for key in [5, 6, 7]:
    skip_list.remove(key)
print(skip_list)
skip_list.insert(6, 'W')
print(skip_list)

#Drugi Wariant
skip_list2 = SkipList(4)
for i, letter in zip(range(15, 0, -1), "ABCDEFGHIJKLMNO"):
    skip_list.insert(i, letter)
print(skip_list)
print(skip_list.search(2))
skip_list.insert(2, 'Z')
print(skip_list.search(2))
for key in [5, 6, 7]:
    skip_list.remove(key)
print(skip_list)
skip_list.insert(6, 'W')
print(skip_list)