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
    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None
    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.l):
            return self._find(val, node.l)
        elif (val > node.v and node.r):
            return self._find(val, node.r)
    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)
    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)
    def findMax(self):
        if self.root:
            return self._findMax(self.root)
        else:
            print('Дерево пустое')
    def _findMax(self,node):
        if node.r:
            self._findMax(node.r)
        else:
            print('Максимум в дереве -', node.v)

    def findMin(self):
        if self.root:
            return self._findMin(self.root)
        else:
            print('Дерево пустое')

    def _findMin(self, node):
        if node.l:
            self._findMin(node.l)
        else:
            print('Минимум в дереве -', node.v)

    def pre_order(self, node):
        if node:
            print(node.v)
            self.pre_order(node.l)
            self.pre_order(node.r)

    def post_order(self, node):
        if node:
            self.post_order(node.l)
            self.post_order(node.r)
            print(node.v)

    def in_order(self, node):
        if node:
            self.post_order(node.l)
            print(node.v)
            self.post_order(node.r)

    def findNP(self, val):
        if self.root is not None:
            temp = self.getRoot().v
            return self._findNP(val, self.root, temp)
        else:
            return None

    def _findNP(self, val, node, temp):
        if val == node.v:
            try:
                print('Предыдущее -', temp ,'\nСледующее -', node.l.v)
                return node
            except:
                print('Предыдущее -', temp ,'\nСледующего нет')
        elif (val < node.v and node.l):
            temp = node.v
            return self._findNP(val, node.l, temp)
        elif (val > node.v and node.r):
            temp = node.v
            return self._findNP(val, node.r, temp)

    def del_uz(self, val):
        if self.root is not None:
            temp = self.getRoot()
            k = 0
            return self._del_uz(val, self.root,temp,k)
        else:
            return None

    def _del_uz(self, val, node,temp,k):
        if ((node.v == val) and (node.l == None) and (node.r == None)):
            if k==1:
                temp.l = None
            elif k==2:
                temp.r= None

        elif (val < node.v and node.l):
            temp = node
            k = 1
            return self._del_uz(val, node.l,temp,k)
        elif (val > node.v and node.r):
            temp = node
            k = 2
            return self._del_uz(val, node.r,temp,k)

    def width(self):
        if self.root is None:
            return
        arr = []
        node = self.getRoot()
        arr.append(node)
        while arr:
            node = arr.pop(0)
            print(node.v)
            if node.l:
                arr.append(node.l)
            if node.r:
                arr.append(node.r)
        return (arr)


def main():
    tree = Tree()
    ch = 1
    while ch != 0 :
        print('\n---------------------------------\n'
              '1. Добавить элемент в дерево\n'
              '2. Отобразить дерево\n'
              '3. Поиск элемента в дереве\n'
              '4. Нахождение минимума\n'
              '5. Нахождение максимума\n'
              '6. Прямой обход\n'
              '7. Центрированный обход\n'
              '8. Обратный обход\n'
              '9. Нахождение предыдущего и следующего элемента\n'
              '10. Удаление элемента\n'
              '11. Обход в ширину\n'
              '0. Выход\n'
              '---------------------------------\n')
        try:
            ch = int(input('Выберите пункт меню: '))
        except:
            print('Введено некорректное значение\n')
        if ((ch>11) or (ch<0)):
            print('Введите корректное значение\n')
        else:
            if ch == 1:
                try:
                    a = int(input('Введите значение элемента: '))
                except:
                    print('Введено некорректное значение\n')
                tree.add(a)

            if ch == 2:
                tree.printTree()

            if ch == 3:
                try:
                    a = int(input('Введите значение искомого элемента: '))
                except:
                    print('Введено некорректное значение\n')

                if (tree.find(a)):
                    print('Искомый элемент есть в дереве')
                else:
                    print('Такого элемента нет')

            if ch == 4:
                tree.findMin()

            if ch == 5:
                tree.findMax()

            if ch == 6:
                tree.pre_order(tree.getRoot())

            if ch == 7:
                tree.in_order(tree.getRoot())

            if ch == 8:
                tree.post_order(tree.getRoot())

            if ch == 9:
                try:
                    a = int(input('Введите значение искомого элемента: '))
                except:
                    print('Введено некорректное значение\n')
                tree.findNP(a)

            if ch == 10:
                try:
                    a = int(input('Введите значение искомого элемента для удаления: '))
                except:
                    print('Введено некорректное значение\n')
                if tree.find(a):
                    tree.del_uz(a)
                else:
                    print("Элемент не найден")

            if ch == 11:
                tree.width()




main()