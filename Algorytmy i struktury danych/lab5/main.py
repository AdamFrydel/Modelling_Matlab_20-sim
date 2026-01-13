class NodeTree:
    def __init__(self, key,value,left_child,right_child):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


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
        if self.root is None:
            node = NodeTree(key, value, None, None)
            self.root = node
            return

        def insert(node):
            if node.key == key:
                node.value = value
                return

            if node.key > key:
                if node.left_child is None:
                    node.left_child = NodeTree(key, value, None, None)
                else:
                    insert(node.left_child)

            if node.key < key:
                if node.right_child is None:
                    node.right_child = NodeTree(key, value, None, None)
                else:
                    insert(node.right_child)

        insert(self.root)

    def delete(self, key):
        def delete_node(node, key):
            if node is None:
                return node

            if key < node.key:
                node.left_child = delete_node(node.left_child, key)
            elif key > node.key:
                node.right_child = delete_node(node.right_child, key)
            else:
                if node.left_child is None and node.right_child is None:
                    return None
                elif node.left_child is None:
                    return node.right_child
                elif node.right_child is None:
                    return node.left_child
                else:
                    successor = self._get_min(node.right_child)
                    node.key, node.value = successor.key, successor.value
                    node.right_child = delete_node(node.right_child, successor.key)

            return node

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


drzewo = TreeBst()
drzewo.insert(50,'A')
drzewo.insert(15,'B')
drzewo.insert(62,'C')
drzewo.insert(5,'D')
drzewo.insert(20,'E')
drzewo.insert(58,'F')
drzewo.insert(91,'G')
drzewo.insert(3,'H')
drzewo.insert(8,'I')
drzewo.insert(37,'J')
drzewo.insert(60,'K')
drzewo.insert(24,'L')

drzewo.print_tree()
print(drzewo)

print(drzewo.search(24))
drzewo.insert(20,'AA')
drzewo.insert(6,'M')
drzewo.delete(62)
drzewo.insert(59,'N')
drzewo.insert(100,'P')
drzewo.delete(8)
drzewo.delete(15)
drzewo.insert(55,'R')
drzewo.delete(50)
drzewo.delete(5)
drzewo.delete(24)
print(drzewo.height())
print(drzewo)
drzewo.print_tree()






