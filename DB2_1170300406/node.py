# coding=utf-8
"""
Created on 2020/4/23 20:24
By cfsfine

"""


class Node (object):
    def __init__(self, parent, max_p):
        self.parent = parent
        self.max_p = max_p
        self.values = list ()
        self.children = list ()
        self.t = 'node'

    # 保证每个节点的利用率大于等于50%
    def property(self):
        return len (self.children) >= int (self.max_p / 2)

    # 简单的插入操作，一个value值，两个孩子
    def simple_insert(self, value, child1, child2):
        self.values.append (value)
        self.children.append (child1)
        self.children.append (child2)

    # 更新values
    def update_values(self):
        # 如果高度为二的点
        if self.children[0].t == 'leaf':
            # 利用率达标则更新value值
            if self.property ():
                l = list ()
                for child in self.children:
                    if len (child.values) != 0:
                        l.append (child.values[-1])
                self.values = l[: len (self.children) - 1]
            else:
                # 利用率不达标则调整
                self.merge_adjust ()
        else:
            # 利用率达标则更新value值
            if self.property ():
                l = list ()
                for child in self.children:
                    l.append (child.children[-1].values[-1])
                self.values = l[: len (self.children) - 1]
            else:
                # 利用率不达标则调整
                self.merge_adjust ()

    # 插入一个值
    def insert(self, value, child):
        flag = 0
        for i in range (len (self.values)):
            if self.values[i] > value:
                self.values = self.values[:i] + [value] + self.values[i:]
                # 插入values后，对应children的变化有两种情况
                if self.children[i].values[-1] > child.values[0]:
                    self.children = self.children[:i] + [child] + self.children[i:]
                else:
                    self.children = self.children[:i + 1] + [child] + self.children[i + 1:]
                flag = 1
                break
        # 如果不在中间插入，就是在末尾插入value值
        if flag == 0:
            self.values.append (value)
            self.children.append (child)
        # 如果插入后键值已满，则需要分裂
        if len (self.values) >= self.max_p:
            root = self.split_adjust ()
        else:
            root = 0
        if child.t == 'leaf':
            self.update_values ()
        return root

    # 分裂节点
    def split_adjust(self):
        # 这里整除，将values填满的节点一分为二，且都保证利用率大于等于50%
        index = (self.max_p + 1) // 2
        r = self.values[index - 1]
        new_node = Node (self.parent, self.max_p)
        new_node.values = self.values[index:]
        self.values = self.values[:index - 1]
        new_node.children = self.children[index:]
        for child in new_node.children:
            child.parent = new_node
        self.children = self.children[:index]
        # 如果是根节点分裂
        if self.parent is None:
            node_p = Node (None, self.max_p)
            node_p.simple_insert (r, self, new_node)
            self.parent = node_p
            new_node.parent = node_p
            return node_p
        else:
            root = self.parent.insert (r, new_node)
            return root

    # 删除一个节点之后需要进行的调整
    def remove_adjust(self):
        if self.children[0].t == 'leaf':
            self.update_values ()
            if self.parent is None:
                return self.children[0].parent
        if self.parent.parent is None:
            return self.parent
        else:
            return self.parent.remove_adjust ()

    # 如果节点利用率不达标，需要合并调整。
    def merge_adjust(self):
        if self.parent is None:
            if len (self.values) == 1:
                self.values = self.children[0].values
                tchildren = []
                for i in self.children[0].children:
                    tchildren.append (i)
                self.children = []
                self.children.extend (tchildren)
                self.update_values ()
            else:
                self.values.pop ()
                self.update_values ()
        elif len (self.parent.values) == 1:
            ind = self.parent.children.index (self)
            t = ind
            if self.parent.children.index (self) == 0:
                left_node = self.parent.children[1]
                self.values.extend (self.parent.values)
                self.merge (left_node, 1)
                t += 1
            else:
                left_node = self.parent.children[0]
                left_node.values.extend (self.parent.values)
                self.merge (left_node, -1)
                t -= 1
            for child in self.children:
                child.parent = self

            self.update_values ()
            if len (self.values) >= self.max_p:
                self.split_adjust ()
            # self.parent = self.parent.parent
            # self.parent.values.pop (ind)
            self.parent.children.pop (t)
            self.parent.merge_adjust ()
        else:
            ind = self.parent.children.index (self)
            t = 0
            if ind < len (self.parent.children) - 1:
                right_node = self.parent.children[ind + 1]
                # self.values.append (self.parent.values[ind])
                self.merge (right_node, 1)
                t = ind + 1
            else:
                left_node = self.parent.children[ind - 1]
                # left_node.values.append (self.parent.values[ind])
                self.merge (left_node, -1)
                t = ind - 1
            for child in self.children:
                child.parent = self
            self.update_values ()
            if len (self.values) >= self.max_p:
                self.split_adjust ()
            self.parent.values.pop (ind)
            self.parent.children.pop (t)

    # 对节点进行合并，两种情况。
    def merge(self, node, order):
        if order == 1:
            self.values = self.values + node.values
            self.children[0].next_leaf = node.children[0]
            node.children[0].previous_leaf = self.children[0]
            self.children = self.children + node.children
        else:
            self.values = node.values + self.values
            node.children[0].next_leaf = self.children[0]
            self.children[0].previous_leaf = node.children[0]
            self.children = node.children + self.children

    def to_string(self):
        s = '[ '
        for i in range (len (self.values) - 1):
            s = s + str (self.values[i]) + ' | '
        s = s + str (self.values[len (self.values) - 1]) + ' ]'
        return s


class Leaf (Node):
    def __init__(self, previous_leaf, next_leaf, parent, max_p):
        self.parent = parent
        self.max_p = max_p
        self.previous_leaf = previous_leaf
        self.next_leaf = next_leaf
        self.parent = parent
        self.max_p = max_p
        self.values = list ()
        self.datas = list ()
        self.t = 'leaf'

    def size(self):
        return len (self.values)

    def property(self):
        return len (self.values) >= self.max_p // 2

    def get(self, value):
        try:
            index = self.values.index (value)
            return index, value
        except:
            return -1, value

    # 叶子节点的插入操作，进需要考虑value和存储的具体内容string。
    def insert(self, value, string):
        flag = 0
        for i in range (len (self.values)):
            if self.values[i] > value:
                self.values = self.values[:i] + [value] + self.values[i:]
                self.datas = self.datas[:i] + [string] + self.datas[i:]
                flag = 1
                break
        if flag == 0:
            self.values.append (value)
            self.datas.append (string)
        if len (self.values) >= self.max_p:
            root = self.split_adjust ()
            return root
        else:
            return 0

    # 叶子节点的分裂操作
    def split_adjust(self):
        index = (self.max_p + 1) // 2
        r = self.values[index - 1]
        d = self.datas[index - 1]
        if self.next_leaf is None or len (self.next_leaf.values) + len (self.values) - index > self.max_p - 1:
            new_leaf = Leaf (self, None, self.parent, self.max_p)
            try:
                self.next_leaf.previous_leaf = new_leaf
            except:
                None
            new_leaf.next_leaf = self.next_leaf
            self.next_leaf = new_leaf
            new_leaf.values = self.values[index:]
            new_leaf.datas = self.datas[index:]
            self.values = self.values[:index]
            self.datas = self.datas[:index]
            if self.parent is None:
                node_p = Node (None, self.max_p)
                node_p.simple_insert (r, self, new_leaf)
                self.parent = node_p
                new_leaf.parent = node_p
                return node_p
            else:
                root = self.parent.insert (r, new_leaf)
                return root
        else:
            next_leaf = self.next_leaf
            for j in range (len (self.values[index:])):
                for i in range (len (next_leaf.values)):
                    if next_leaf.values[i] > self.values[index:][j]:
                        next_leaf.values = next_leaf.values[:i] + [self.values[index:][j]] + next_leaf.values[i:]
                        next_leaf.datas = next_leaf.datas[:i] + [self.datas[index:][j]] + next_leaf.datas[i:]
                        flag = 1
                        break
                if flag == 0:
                    next_leaf.values.append (self.values[index:][j])
                    next_leaf.datas.append (self.datas[index:][j])
            self.values = self.values[:index]
            self.datas = self.datas[:index]
            n = self.parent
            n.update_values ()
            while n.parent is not None:
                n = n.parent
            return n

    # 叶子节点的合并，也分为两种情况，左合并和右合并。
    def merge(self, leaf, order):
        if order == 1:
            self.values = self.values + leaf.values
            self.datas = self.datas + leaf.datas
        else:
            self.values = leaf.values + self.values
            self.datas = leaf.datas + self.datas

    # 删除操作，这里需要考虑合并情况和节点位置的变化。
    def remove(self, value):
        c = self.values.index (value)
        self.datas.remove (self.datas[c])
        self.values.remove (value)
        p = self.parent
        if self.property () is False:
            if self.next_leaf is not None:
                if self.next_leaf.parent == p:
                    if len (self.values) + len (self.next_leaf.values) <= self.max_p - 1:
                        self.merge (self.next_leaf, 1)
                        p.children.remove (self.next_leaf)
                        self.next_leaf = self.next_leaf.next_leaf
                    elif (len (self.values) + len (self.next_leaf.values)) // 2 >= self.max_p // 2:
                        count = 0
                        while len (self.values) < self.max_p // 2:
                            self.values.append (self.next_leaf.values[count])
                            self.datas.append (self.next_leaf.datas[count])
                            count += 1
                        self.next_leaf.values = self.next_leaf.values[count:]
                elif self.previous_leaf is not None:
                    if self.previous_leaf.parent == p:
                        if len (self.values) + len (self.previous_leaf.values) <= self.max_p - 1:
                            self.merge (self.previous_leaf, -1)
                            p.children.remove (self.previous_leaf)
                            # self.previous_leaf = self.previous_leaf.previous_leaf
                            self.previous_leaf.next_leaf = self
                        elif (len (self.values) + len (self.previous_leaf.values)) // 2 >= self.max_p // 2:
                            print (self.previous_leaf.values)
                            count = -1
                            while len (self.values) < self.max_p // 2:
                                self.values = [self.previous_leaf.values[count]] + self.values
                                self.datas = [self.previous_leaf.datas[count]] + self.datas
                                count -= 1
                            self.previous_leaf.values = self.previous_leaf.values[:count + 1]
                            print (self.previous_leaf.values)
        if p.parent is None:
            p.update_values ()
            return p
        else:
            return p.remove_adjust ()
