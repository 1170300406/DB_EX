# coding=utf-8
"""
Created on 2020/4/29 11:39
By cfsfine

"""
import re

# 将一万条记录读入
import struct
import time


def b_sort(arr):
    n = len (arr)
    # 遍历所有数组元素
    for i in range (n):
        for j in range (0, n - i - 1):
            if arr[j][0] < arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# 模拟内存，每块能存放25条记录，21块，总共最大只能放入525条记录
# 需要排序400个数据块，20个数据块作为一个子集
# 20路归并
cache = []
n = 10000
for i in range (21):
    cache.append ([])

start = time.time ()
# 第一趟归并，划分子集
l = []
with open ('data.bin', 'rb') as w:
    with open ('data1.bin', 'wb') as f:
        for i in range (20):
            for j in range (500):
                t = ''
                t = t + str (struct.unpack ('i', w.read (4))[0])
                t = t + ' ' + str (struct.unpack ('12s', w.read (12))[0])[2:-1]
                l1 = t.split (' ')
                cache[0].append ([int (l1[0]), l1[1]])
            b_sort (cache[0])
            for i in range (500):
                f.write (struct.pack ('i', int (cache[0][i][0])))
                f.write (struct.pack ('12s', cache[0][i][1].encode ('utf-8')))
            cache[0].clear ()
d1 = []
with open ('data1.bin', 'rb') as f:
    for i in range (n):
        t1 = int (struct.unpack ('i', f.read (4))[0])
        t2 = str (struct.unpack ('12s', f.read (12))[0])[2:-1]
        d1.append ([t1, t2])

dr = []

# 记录对于每一个子集取到第几块了
flag = [0] * 20
flag_b = 0
# 第二趟，20路归并
# 初始化，将每个子集中第一块放入cache
with open ('data2.bin', 'wb') as w:
    for i in range (20):
        cache[i].extend (d1[(i + 1) * 500 - (flag[i] + 1) * 25:(i + 1) * 500 - (flag[i] + 1) * 25 + 25])
    while True:
        min_w = min (cache[0:20], key=lambda x: x[-1])
        t = min_w.pop ()
        cache[20].append (t)
        # 判断输出块是否已满，满了就将当前结果写入
        if len (cache[20]) == 25:
            dr.extend (cache[20])
            for c in cache[20]:
                w.write (struct.pack ('i', int (c[0])))
                w.write (struct.pack ('12s', c[1].encode ('utf-8')))
            cache[20].clear ()
        if len (min_w) == 0:
            i = cache.index (min_w)
            if flag[i] < 19:
                i = cache.index (min_w)
                flag[i] = flag[i] + 1
                min_w.extend (d1[(i + 1) * 500 - (flag[i] + 1) * 25:(i + 1) * 500 - (flag[i] + 1) * 25 + 25])
            else:
                min_w.append ([100000, ''])
                flag_b += 1
        if flag_b == 20:
            break
end = time.time ()

print (len (dr))
for i in dr:
    print (i)
print (end - start)
#
# start = time.time ()
# b_sort (d)
# end = time.time ()
#
# print (end - start)
