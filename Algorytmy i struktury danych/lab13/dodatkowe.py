class Node:
    def __init__(self):
        self.children = {}
        self.indices = []

class SuffixTree:
    def __init__(self, text):
        self.text = text
        self.root = Node()
        self._build_tree()

    def _build_tree(self):
        for i in range(len(self.text)):
            current = self.root
            for c in self.text[i:]:
                if c not in current.children:
                    current.children[c] = Node()
                current = current.children[c]
                current.indices.append(i)

    def search(self, pattern):
        current = self.root
        for c in pattern:
            if c not in current.children:
                return []
            current = current.children[c]
        return current.indices

    def print_tree(self, node=None, prefix=''):
        if node is None:
            node = self.root
        for c, child in node.children.items():
            print(prefix + c)
            self.print_tree(child, prefix + '  ')

T = "banana\0"
tree = SuffixTree(T)
tree._build_tree()
tree.print_tree()





for pat in ["ana", "na", "x"]:
    print(f"'{pat}' występuje na pozycjach:", tree.search(pat))
def suffix_array(text):
    return sorted(range(len(text)), key=lambda i: text[i:])

def binary_search(pattern, text, sa):
    left, right = 0, len(sa) - 1
    while left <= right:
        mid = (left + right) // 2
        suffix = text[sa[mid]:]
        if suffix.startswith(pattern):
            return sa[mid]
        elif pattern < suffix:
            right = mid - 1
        else:
            left = mid + 1
    return -1

T = "banana\0"
sa = suffix_array(T)
print("Tablica sufiksowa:", sa)
for pat in ["ana", "na", "x"]:
    idx = binary_search(pat, T, sa)
    print(f"'{pat}' znaleziono na pozycji:", idx if idx != -1 else "nie występuje")