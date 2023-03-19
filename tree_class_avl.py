class Node_avl:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.v = val
        self.height = 1
        self.dad = None
class Tree_avl:
    def __init__(self):
        self.root = None
    def getRoot(self):
        return self.root

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            if node == self.root:
                print('it is root ' , node.v)
            elif node.v:
                print(str(node.v) )
            self._printTree(node.r)

    def add(self, root, v):
        if not root:
            return Node_avl(v)
        elif v < root.v:
            root.left = self.add(root.left, v)
        else:
            root.right = self.add(root.right, v)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and v < root.left.v:
            return self.rotateR(root)

        if balance < -1 and v > root.right.v:
            return self.rotateL(root)

        if balance > 1 and v > root.left.v:
            root.left = self.rotateL(root.left)
            return self.rotateR(root)

        if balance < -1 and v < root.right.v:
            root.right = self.rotateR(root.right)
            return self.rotateL(root)

        return root

    def AVLTreeLength(self, node):
        if not node:
            return 0
        else:
            left_height = self.AVLTreeLength(node.left)
            right_height = self.AVLTreeLength(node.right)
            return max(left_height, right_height) + 1

    def right_rotate(self, z):
            y = z.left
            T3 = y.right

            y.right = z
            z.left = T3

            z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
            y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

            return y

    def left_rotate(self, z):
            y = z.right
            T2 = y.left

            y.left = z
            z.right = T2

            z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
            y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

            return y

    def get_height(self, node):
        if not node:
            return 0

        return node.height

    def get_balance(self, node):
        if not node:
            return 0

        return self.get_height(node.left) - self.get_height(node.right)

    def height(self, Node):
        if Node is None:
            return 0
        else:
            return Node.height

    def rotateR(self, Node):
        a = Node.left
        b = a.right
        a.right = Node
        Node.left = b
        Node.height = 1 + max(self.height(Node.left), self.height(Node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a

    def rotateL(self, Node):
        a = Node.right
        b = a.left
        a.left = Node
        Node.right = b
        Node.height = 1 + max(self.height(Node.left), self.height(Node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a
"""

    def right_rotate(self, z):
            y = z.left
            T3 = y.right

            y.right = z
            z.left = T3

            z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
            y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

            return y

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y


        def get_height(self, node):
            if not node:
                return 0

            return node.height

    def rotateL(self, Node):
        a = Node.r
        b = a.l
        a.l = Node
        Node.r = b
        Node.h = 1 + max(self.height(Node.l), self.height(Node.r))
        a.h = 1 + max(self.height(a.l), self.height(a.r))
        return a


    def balance(self, Node):
        if Node is None:
            return 0
        else:
            return self.height(Node.l) - self.height(Node.r)

    def height(self, Node):
        if Node is None:
            return 0
        else:
            return Node.h

    def get_width(self, node, c):
        while node.l:
            c=c+node.c
            node=node.l
        return c

    def add(self, val):
            if self.root is None:
                self.root = Node_avl(val)
            else:
                self._add(val, self.root)

    def _add(self, val, node):
            if val < node.v:
                if node.l is not None:
                    self._add(val, node.l)
                else:
                    node.l = Node_avl(val)
                    node.l.dad = node
            else:
                if node.r is not None:
                    self._add(val, node.r)
                else:
                    node.r = Node_avl(val)
                    node.r.dad = node

            node.h = 1 + max(self.height(node.l), self.height(node.r))
            balance = self.balance(node)
            if balance > 1 and node.l.v > val:
                return self.right_rotate(node)
            if balance < -1 and val > node.r.v:
                return self.left_rotate(node)
            if balance > 1 and val > node.l.v:
                node.l = self.left_rotate(node.l)
                return self.right_rotate(node)
            if balance < -1 and val < node.r.v:
                node.r = self.right_rotate(node.r)
                return self.left_rotate(node)
            return node

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
                self.root = right

            else:
                if dad.l == node:
                    dad.l = right

                else:
                    dad.r = right
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
                self.root = left
            else:
                if dad.l == node:
                    dad.l = left
                else:
                    dad.r = left
            pass



class node:
    def __init__(self, num):
        self.value = num
        self.left = None
        self.right = None
        self.height = 1

class AVL:

    def height(self, Node):
        if Node is None:
            return 0
        else:
            return Node.height

    def balance(self, Node):
        if Node is None:
            return 0
        else:
            return self.height(Node.left) - self.height(Node.right)

    def MinimumValueNode(self, Node):
        if Node is None or Node.left is None:
            return Node
        else:
            return self.MinimumValueNode(Node.left)

    def rotateR(self, Node):
        a = Node.left
        b = a.right
        a.right = Node
        Node.left = b
        Node.height = 1 + max(self.height(Node.left), self.height(Node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a

    def rotateL(self, Node):
        a = Node.right
        b = a.left
        a.left = Node
        Node.right = b
        Node.height = 1 + max(self.height(Node.left), self.height(Node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a

    def add(self, val, root):
        if root is None:
            return node(val)
        elif val <= root.value:
            root.left = self.add(val, root.left)
        elif val > root.value:
            root.right = self.add(val, root.right)
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)
        if balance > 1 and root.left.value > val:
            return self.rotateR(root)
        if balance < -1 and val > root.right.value:
            return self.rotateL(root)
        if balance > 1 and val > root.left.value:
            root.left = self.rotateL(root.left)
            return self.rotateR(root)
        if balance < -1 and val < root.right.value:
            root.right = self.rotateR(root.right)
            return self.rotateL(root)
        return root

    def preorder(self, root):
        if root is None:
            return
        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)

    def delete(self, val, Node):
        if Node is None:
            return Node
        elif val < Node.value:
            Node.left = self.delete(val, Node.left)
        elif val > Node.value:
            Node.right = self.delete(val, Node.right)
        else:
            if Node.left is None:
                lt = Node.right
                Node = None
                return lt
            elif Node.right is None:
                lt = Node.left
                Node = None
                return lt
            rgt = self.MinimumValueNode(Node.right)
            Node.value = rgt.value
            Node.right = self.delete(rgt.value, Node.right)
        if Node is None:
            return Node
        Node.height = 1 + max(self.height(Node.left), self.height(Node.right))
        balance = self.balance(Node)
        if balance > 1 and self.balance(Node.left) >= 0:
            return self.rotateR(Node)
        if balance < -1 and self.balance(Node.right) <= 0:
            return self.rotateL(Node)
        if balance > 1 and self.balance(Node.left) < 0:
            Node.left = self.rotateL(Node.left)
            return self.rotateR(Node)
        if balance < -1 and self.balance(Node.right) > 0:
            Node.right = self.rotateR(Node.right)
            return self.rotateL(Node)
        return Node

Tree = AVL()
rt = None
rt = Tree.add(3, rt)
Tree.preorder(rt)
rt = Tree.add(5, rt)
rt = Tree.add(7, rt)
print("PREORDER")
Tree.preorder(rt)
rt = Tree.add(1, rt)
rt = Tree.add(2, rt)
print("PREORDER")
Tree.preorder(rt)
rt = Tree.add(4, rt)
rt = Tree.add(6, rt)
rt = Tree.delete(7, rt)
rt = Tree.add(8, rt)
rt = Tree.add(9, rt)
print("PREORDER")
Tree.preorder(rt)
rt = Tree.delete(3, rt)
print("PREORDER")
Tree.preorder(rt)
"""