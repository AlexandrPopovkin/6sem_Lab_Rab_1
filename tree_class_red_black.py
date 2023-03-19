class Node_r_b:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
        self.c = 0 #Red
        self.uncle = None
        self.dad = None
        self.g_dad = None
class Tree_r_b:
    def __init__(self):
        self.root = None
    def getRoot(self):
        return self.root
    def add(self, val):
        if self.root is None:
            self.root = Node_r_b(val)
            self.root.l = Node_r_b(None)
            self.root.l.c = 1
            self.root.r = Node_r_b(None)
            self.root.r.c = 1
            self.root.c = 1 #black
        else:
            self._add(val, self.root)
    def _add(self, val, node):

        if val < node.v:
            if node.l.v is not None:
                self._add(val, node.l)
            else:
                node.l.v = val
                node.l.c = 0
                node.l.l= Node_r_b(None)
                node.l.l.c = 1
                node.l.r = Node_r_b(None)
                node.l.r.c = 1
                node.l.dad = node
        else:
            if node.r.v is not None:
                self._add(val, node.r)
            else:
                node.r.v = val
                node.r.c = 0
                node.r.l = Node_r_b(None)
                node.r.l.c = 1
                node.r.r = Node_r_b(None)
                node.r.r.c = 1
                node.r.dad = node
        self.balance(node)

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            if node == self.root:
                print('it is root ' , node.v, ' ' + str(node.c) + ' ')
            elif node.v:
                print(str(node.v) + ' ' + str(node.c) + ' ')
            self._printTree(node.r)

    def balance(self, node):
        tmp = 1
        while tmp == 1:
            if (node.r.c == 0) and (node.l.c == 1):
                self.left_rotate(node)
                node = node.dad
            elif (node.l.c == 0) and (node.l.l.c == 0):
                self.right_rotate(node)
                node = node.dad

            elif (node.r.c == 0) and (node.l.c == 0):
                if node!=self.root:
                    node.c = abs(node.c - 1)
                node.l.c = abs(node.l.c - 1)
                node.r.c = abs(node.r.c - 1)
            else: tmp = 0
    def left_rotate(self, node):
            dad = node.dad
            right = node.r

            node.r = right.l
            if node.r:
                node.r.dad = node

            right.l = node
            node.dad = right

            right.dad = dad
            if not dad:
                tmp = self.root.c
                self.root.c = right.c
                right.c = tmp
                self.root = right
                self.balance(self.root)

            else:
                if dad.l == node:
                    tmp = dad.l.c
                    dad.l.c = right.c
                    right.c = tmp
                    dad.l = right

                else:
                    tmp = dad.r.c
                    dad.r.c = right.c
                    right.c = tmp
                    dad.r = right

            self.balance(node)
            pass

    def right_rotate(self, node):
            dad = node.dad
            left = node.l
            node.l = left.r
            if node.l:
                node.l.dad = node

            left.r = node
            node.dad = left

            left.dad = dad
            if not dad:
                tmp = self.root.c
                self.root.c = left.c
                left.c = tmp
                self.root = left
                self.balance(self.root)

            else:
                if dad.l == node:
                    tmp = dad.l.c
                    dad.l.c = left.c
                    left.c = tmp
                    dad.l = left

                else:
                    tmp = dad.r.c
                    dad.r.c = left.c
                    left.c = tmp
                    dad.r = left

            self.balance(node)
            pass

    def RBTreeLength(self, node):
        if not node:
            return 0
        else:
            left_height = self.RBTreeLength(node.l)
            right_height = self.RBTreeLength(node.r)
            if node.c == 1:
                return max(left_height, right_height) + 1
            else:
                return max(left_height, right_height)

    def get_width(self, node, c):
        while node.l:
            c=c+node.c
            node=node.l
        return c
