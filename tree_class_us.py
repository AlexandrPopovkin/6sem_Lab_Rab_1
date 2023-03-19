class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
class Tree:
    def __init__(self):
        self.root = None
    def getRoot(self):
        return self.root
    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)
    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)
    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)
    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)

    def get_height(self, root):
        if root is None:
            return 0
        else:
            left_height = self.get_height(root.l)
            right_height = self.get_height(root.r)
            return max(left_height, right_height) + 1
