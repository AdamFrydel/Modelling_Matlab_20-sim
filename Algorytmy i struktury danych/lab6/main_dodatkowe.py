class ElemB:
    def __init__(self):
        self.keys = []
        self.children = []

    def is_leaf(self):
        return len(self.children) == 0


class Btree:
    def __init__(self, max_child):
        self.max_child = max_child
        self.max_keys = max_child - 1
        self.root = ElemB()

    def insert(self, key):
        result = self._insert(self.root, key)
        if result:
            middle_key, left, right = result
            new_root = ElemB()
            new_root.keys = [middle_key]
            new_root.children = [left, right]
            self.root = new_root

    def _insert(self, node, key):
        if node.is_leaf():
            node.keys.append(key)
            node.keys.sort()
        else:
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            result = self._insert(node.children[i], key)
            if result:
                middle_key, left, right = result
                node.keys.insert(i, middle_key)
                node.children[i] = left
                node.children.insert(i + 1, right)

        if len(node.keys) > self.max_keys:
            return self._split(node)
        return None

    def _split(self, node):
        mid = len(node.keys) // 2
        middle_key = node.keys[mid]

        left = ElemB()
        right = ElemB()

        left.keys = node.keys[:mid]
        right.keys = node.keys[mid + 1:]

        if node.children:
            left.children = node.children[:mid + 1]
            right.children = node.children[mid + 1:]

        return middle_key, left, right

    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            if node.children:
                self._print_tree(node.children[-1], lvl + 1)
            for i in range(len(node.keys) - 1, -1, -1):
                print("  " * lvl + str(node.keys[i]))
                if node.children:
                    self._print_tree(node.children[i], lvl + 1)


if __name__ == "__main__":
    t1 = Btree(4)
    keys1 = [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18, 15, 10, 19]
    for k in keys1:
        t1.insert(k)
        t1.print_tree()
