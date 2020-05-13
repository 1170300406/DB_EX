# coding=utf-8
"""
Created on 2020/4/24 10:37
By cfsfine

"""

from node import Leaf, Node


class Bplustree (object):
    def __init__(self, max_p):
        self.max_p = max_p
        self.root = Leaf (None, None, None, self.max_p)
        self.r = ''

    def search(self, value, node):
        while node.t != 'leaf':
            flag = 0
            for i in range (len (node.values)):
                if node.values[i] >= value:
                    node = node.children[i]
                    flag = 1
                    break
            if flag == 0 and len (node.children) > len (node.values):
                node = node.children[len (node.values)]
        try:
            index = node.values.index (value)
            return index, node, 1
        except:
            return 0, node, 0

    def insert(self, value, string):
        d, node, r = self.search (value, self.root)
        if r != 1:
            l = node.insert (value, string)
            if l != 0:
                self.root = l

    def delete(self, value):
        d, leaf, r = self.search (value, self.root)
        if r == 1:
            l = leaf.remove (value)
            if l != 0:
                self.root = l
            return 1
        return 0

    def print_tree(self, node, dl, count):
        if node.t == 'node':
            self.r = self.r + dl * count + str (node.values) + '\n'
            # print (dl * count, node.values)
        else:
            self.r = self.r + dl * count + str (node.values) + str (node.datas) + '\n'
            # print (dl * count, node.values, node.datas)
        count += 1
        if node.t == 'node':
            for child in node.children:
                self.print_tree (child, dl, count)


if __name__ == '__main__':
    # 一个简单的测试
    tree = Bplustree (4)
    tree.insert (1, 'str1')
    tree.insert (2, 'str2')
    tree.insert (3, 'str3')
    tree.insert (4, 'str4')
    tree.insert (5, 'str5')
    tree.insert (6, 'str6')
    tree.insert (7, 'str7')
    tree.insert (8, 'str8')
    tree.insert (9, 'str9')
    tree.insert (10, 'str10')
    tree.insert (11, 'str11')
    tree.insert (12, 'str12')
    tree.insert (13, 'str13')
    tree.insert (14, 'str14')
    tree.insert (15, 'str15')
    tree.insert (16, 'str16')
    tree.insert (17, 'str17')
    tree.insert (18, 'str18')
    tree.insert (19, 'str19')
    tree.insert (20, 'str20')
    tree.insert (21, 'str21')
    tree.insert (22, 'str22')
    tree.insert (23, 'str23')
    tree.r = ''
    tree.print_tree (tree.root, '   ', 0)
    print (tree.r)
    print (tree.search (5, tree.root))

    tree.delete (1)
    tree.r = ''
    tree.print_tree (tree.root, '   ', 0)
    print (tree.r)

    print (tree.search (5, tree.root))
