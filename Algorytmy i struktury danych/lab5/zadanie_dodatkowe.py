class NodeTree:
    def __init__(self, key, value, left_child=None, right_child=None, lvl=1):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.lvl = lvl
        self.weight = 0
        self.update()

    def update(self):
        left_lvl = self.left_child.lvl if self.left_child else 0
        right_lvl = self.right_child.lvl if self.right_child else 0
        self.lvl = 1 + max(left_lvl, right_lvl)
        self.weight = right_lvl - left_lvl

def rotation(node):
    node.update()
    if node.weight == -2:
        if node.left_child.weight <= 0:
            return ll(node)
        else:
            return lr(node)
    elif node.weight == 2:
        if node.right_child.weight >= 0:
            return rr(node)
        else:
            return rl(node)
    return node

class TreeBst:
    def __init__(self):
        self.root = None

    def search(self, key):
        def search(node):
            if node is None:
                return None
            if node.key == key:
                return node.value
            elif node.key < key:
                return search(node.right_child)
            else:
                return search(node.left_child)

        return search(self.root)

    def insert(self, key, value):
        def insert(node):
            if node is None:
                return NodeTree(key, value)

            if key < node.key:
                node.left_child = insert(node.left_child)
            elif key > node.key:
                node.right_child = insert(node.right_child)
            else:
                node.value = value

            return rotation(node)

        self.root = insert(self.root)

    def delete(self, key):
        def delete_node(node, key):
            if node is None:
                return None

            if key < node.key:
                node.left_child = delete_node(node.left_child, key)
            elif key > node.key:
                node.right_child = delete_node(node.right_child, key)
            else:
                if node.left_child is None:
                    return node.right_child
                elif node.right_child is None:
                    return node.left_child

                successor = self._get_min(node.right_child)
                node.key, node.value = successor.key, successor.value
                node.right_child = delete_node(node.right_child, successor.key)

            return rotation(node)

        self.root = delete_node(self.root, key)

    def _get_min(self, node):
        while node.left_child is not None:
            node = node.left_child
        return node

    def __str__(self):
        result = []
        def traverse(node):
            if node:
                traverse(node.left_child)
                result.append(f"{node.key} {node.value}")
                traverse(node.right_child)
        traverse(self.root)
        return ', '.join(result)

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node is not None:
            self.__print_tree(node.right_child, lvl + 5)
            print()
            print(lvl * " ", node.key, node.value)
            self.__print_tree(node.left_child, lvl + 5)

    def height(self):
        def height(node):
            if node is None:
                return 0
            current_root = node
            left_height = height(current_root.left_child)
            right_height = height(current_root.right_child)
            return 1 + max(left_height, right_height)

        return height(self.root)

def ll(node):
    new_root = node.left_child
    node.left_child = new_root.right_child
    new_root.right_child = node
    node.update()
    new_root.update()
    return new_root

def rr(node):
    new_root = node.right_child
    node.right_child = new_root.left_child
    new_root.left_child = node
    node.update()
    new_root.update()
    return new_root

def lr(node):
    node.left_child = rr(node.left_child)
    return ll(node)

def rl(node):
    node.right_child = ll(node.right_child)
    return rr(node)


drzewo = TreeBst()
drzewo.insert(50,'A')
drzewo.insert(15,'B')
drzewo.insert(62,'C')
drzewo.insert(5,'D')
drzewo.insert(2,'E')
drzewo.insert(1,'F')
drzewo.insert(11,'G')
drzewo.insert(100,'H')
drzewo.insert(7,'I')
drzewo.insert(6,'J')
drzewo.insert(55,'K')
drzewo.insert(52,'L')
drzewo.insert(51,'M')
drzewo.insert(57,'N')
drzewo.insert(8,'O')
drzewo.insert(9,'P')
drzewo.insert(10,'R')
drzewo.insert(99,'S')
drzewo.insert(12,'T')

drzewo.print_tree()
print(drzewo)

drzewo.delete(50)
drzewo.delete(52)
drzewo.delete(11)
drzewo.delete(57)
drzewo.delete(1)
drzewo.delete(12)

drzewo.insert(3,'AA')
drzewo.insert(4,'BB')
drzewo.delete(7)
drzewo.delete(8)
drzewo.print_tree()

print(drzewo)