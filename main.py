from tree_class_us import *
from tree_class_red_black import *
from tree_class_avl import *
import random
import time
import numpy
def main():

    x = int(input('Введите количество элементов, для которых необходимо рассчитать время: '))
    tree_rb = Tree_r_b()
    tree_avl = Tree_avl()
    tree = Tree()

    time_tree_rb = ' '
    time_tree_avl = ' '

    root = None
    time_rb = 0
    time_avl = 0

    for j in range(x):
            a = random.expovariate(1)

            start = time.time()
            tree_rb.add(a)
            end = time.time()
            time_rb = time_rb + end - start

            start = time.time()
            root = tree_avl.add(root,a)
            end = time.time()
            time_avl = time_avl + end - start

            tree.add(a)


    print('\nЭкспоненциальное распределение\nКрасно-чёрное дерево: ',str(time_rb), 'сек', '\nВысота дерева:', tree_rb.RBTreeLength(tree_rb.getRoot()))
    print('АВЛ дерево: ',str(time_avl),'сек', '\nВысота дерева:', tree_avl.AVLTreeLength(root))
    print(tree.get_height(tree.getRoot()))

    for j in range(x):
            a = random.randint(1, 10000000)

            start = time.time()
            tree_rb.add(a)
            end = time.time()
            time_rb = time_rb + end - start

            start = time.time()
            root = tree_avl.add(root,a)
            end = time.time()
            time_avl = time_avl + end - start

            tree.add(a)

    print('\nРавномерное распределение \nКрасно-чёрное дерево: ', str(time_rb),'сек', '\nВысота дерева:', tree_rb.RBTreeLength(tree_rb.getRoot()))
    print('АВЛ дерево: ',str(time_avl),'сек', '\nВысота дерева:', tree_avl.AVLTreeLength(root))

    print(tree.get_height(tree.getRoot()))


main()