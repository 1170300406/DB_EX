# coding=utf-8
"""
Created on 2020/4/27 11:24
By cfsfine

"""  # 实现btree文本读入，gui显示
import random
import re
import struct
import tkinter as tk
import traceback
from tkinter import messagebox, scrolledtext
from btree import Bplustree

# 主菜单
from node import Leaf


def menu():
    global tree
    global m
    global n
    global p
    global q
    global q1
    global w
    global z
    tree = Bplustree (4)
    t = tk.Tk ()
    t.title ('B+树演示系统')
    t.geometry ('980x600+400+200')
    tk.Label (text='B+树演示系统', bg='yellow').pack ()
    t1 = tk.Label (t, text='记录数目', bg='yellow')
    t1.place (x=20, y=40, width=100, height=20)
    n = tk.Entry (t, show=None)
    n.place (x=140, y=40, width=100, height=20)
    t2 = tk.Label (t, text='键值最大值', bg='yellow')
    t2.place (x=260, y=40, width=100, height=20)
    m = tk.Entry (t, show=None)
    m.place (x=380, y=40, width=100, height=20)
    b = tk.Button (t, text='创建', width=30, height=1, command=build)
    b.place (x=500, y=40, width=100, height=20)
    t3 = tk.Label (t, text='查询记录', bg='yellow')
    t3.place (x=620, y=40, width=100, height=20)
    p = tk.Entry (t, show=None)
    p.place (x=740, y=40, width=100, height=20)
    b = tk.Button (t, text='查询', width=30, height=1, command=qury)
    b.place (x=860, y=40, width=100, height=20)

    t4 = tk.Label (t, text='插入记录', bg='yellow')
    t4.place (x=20, y=70, width=100, height=20)
    q = tk.Entry (t, show=None)
    q.place (x=140, y=70, width=100, height=20)
    q1 = tk.Entry (t, show=None)
    q1.place (x=260, y=70, width=100, height=20)
    b = tk.Button (t, text='插入', width=30, height=1, command=insert)
    b.place (x=380, y=70, width=100, height=20)

    t5 = tk.Label (t, text='删除记录', bg='yellow')
    t5.place (x=500, y=70, width=100, height=20)
    w = tk.Entry (t, show=None)
    w.place (x=620, y=70, width=100, height=20)
    b = tk.Button (t, text='删除', width=30, height=1, command=delete)
    b.place (x=740, y=70, width=100, height=20)

    z = scrolledtext.ScrolledText (t)
    z.place (x=20, y=110, width=940, height=460)

    t.mainloop ()


# 插入记录
def insert():
    try:
        z.delete (1.0, "end")
        tree.r = ''
        tree.print_tree (tree.root, '   ', 0)
        z.insert ("insert", tree.r)
        p = int (q.get ())
        s = str (q1.get ())
        r = tree.search (p, tree.root)[2]

        if r == 1:
            tk.messagebox.showinfo (title='温馨提醒', message='已有此条记录，插入失败！')
        else:
            tk.messagebox.showinfo (title='温馨提醒', message='没有此条记录！插入成功！插入后更新B+树结构如下方文本框所示！')
            tree.insert (p, s)
            z.delete (1.0, "end")
            tree.r = ''
            tree.print_tree (tree.root, '   ', 0)
            z.insert ("insert", tree.r)
    except Exception as e:
        tk.messagebox.showinfo (title='温馨提醒', message=e)


# 删除记录
def delete():
    try:
        z.delete (1.0, "end")
        tree.r = ''
        tree.print_tree (tree.root, '   ', 0)
        z.insert ("insert", tree.r)
        p = int (w.get ())
        r = tree.search (p, tree.root)[2]

        if r == 0:
            tk.messagebox.showinfo (title='温馨提醒', message='没有此条记录，删除失败！')
        else:
            tk.messagebox.showinfo (title='温馨提醒', message='查到此条记录！其数据为：' + str (
                tree.search (p, tree.root)[1].datas[tree.search (p, tree.root)[0]]) + '，删除成功！删除后更新B+树结构如下方文本框所示！')
            tree.delete (p)
            z.delete (1.0, "end")
            tree.r = ''
            tree.print_tree (tree.root, '   ', 0)
            z.insert ("insert", tree.r)
    except Exception as e:
        tk.messagebox.showinfo (title='温馨提醒', message=e)


# 查询记录
def qury():
    try:
        z.delete (1.0, "end")
        tree.r = ''
        tree.print_tree (tree.root, '   ', 0)
        z.insert ("insert", tree.r)
        q = int (p.get ())
        r = tree.search (q, tree.root)[2]
        if r == 0:
            tk.messagebox.showinfo (title='温馨提醒', message='没有此条记录！')
        else:
            tk.messagebox.showinfo (title='温馨提醒', message='查到此条记录！其数据为：' + str (
                tree.search (q, tree.root)[1].datas[tree.search (q, tree.root)[0]]))
    except Exception as e:
        tk.messagebox.showinfo (title='温馨提醒', message=e)


def encode(s):
    return ' '.join ([bin (ord (c)).replace ('0b', '') for c in s])


# 随机生成文件记录，读入创建b+树
def build():
    try:
        p = int (n.get ())
        q = int (m.get ())
        resultList = random.sample (range (0, q + 1), p)
        with open ('data.bin', 'wb') as w:
            for i in range (p):
                w.write (struct.pack ('i', resultList[i]))
                w.write (struct.pack ('12s', generate_random_str ().encode ('utf-8')))

        l = []
        with open ('data.bin', 'rb') as w:
            for i in range (p):
                t = ''
                t = t + str (struct.unpack ('i', w.read (4))[0])
                t = t + ' ' + str (struct.unpack ('12s', w.read (12))[0])[2:-1]
                l.append (t)
        tree.root = Leaf (None, None, None, 4)
        for l1 in l:
            l1 = l1.split (' ')
            tree.insert (int (l1[0]), l1[1])
        try:
            z.delete (1.0, "end")
        except:
            None
        tree.r = ''
        tree.print_tree (tree.root, '   ', 0)
        z.insert ("insert", tree.r)
        tk.messagebox.showinfo (title='温馨提醒', message='创建成功')
    except Exception as e:
        traceback.print_exc ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)


# 随机生成字符串
def generate_random_str(random_length=12):
    random_str = ''
    base_str = 'abcdefghigklmnopqrstuvwxyz0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
    length = len (base_str) - 1
    for i in range (random_length):
        random_str += base_str[random.randint (0, length)]
    return random_str


if __name__ == '__main__':
    menu ()
