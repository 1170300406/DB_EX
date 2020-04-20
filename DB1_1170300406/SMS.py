# coding=utf-8
"""
Created on 2020/3/28 15:55
By cfsfine

"""
import re

import pymysql
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

db = pymysql.connect ("localhost", "root", "cfs99cfs0305", "student_management_system")
cursor = db.cursor (cursor=pymysql.cursors.DictCursor)


# 增加记录功能菜单
def add():
    global t1
    t1 = tk.Toplevel ()
    t1.title ("增加记录")
    t1.geometry ('280x400+420+220')

    l = tk.Label (t1, text='增加记录', bg='yellow')
    l.pack (padx=20, pady=10)
    b = tk.Button (t1, text='增加班级', width=10, height=1, command=add_class, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t1, text='增加辅导员', width=10, height=1, command=add_instructor, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t1, text='增加教师', width=10, height=1, command=add_teacher, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t1, text='增加课程', width=10, height=1, command=add_course, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t1, text='增加学生', width=10, height=1, command=add_student, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t1, text='增加学生成绩', width=10, height=1, command=add_student_result, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t1, text='增加院系', width=10, height=1, command=add_department, bg='yellow')
    b.pack (padx=20, pady=10)

    t1.mainloop ()


# 增加班级
def add_class():
    global t2
    global add_cn
    global add_pn
    t2 = tk.Toplevel ()
    t2.title ("增加一条班级记录")
    t2.geometry ('300x140+440+240')
    frame = tk.Frame (t2)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='班号      ').pack (padx=20, pady=10)
    add_cn = tk.Entry (frame_r, show=None)
    add_cn.pack (padx=20, pady=10)
    tk.Label (frame_l, text='人数        ').pack (padx=20, pady=10)
    add_pn = tk.Entry (frame_r, show=None)
    add_pn.pack (padx=20, pady=10)
    b = tk.Button (t2, text='确定', width=15, height=1, command=insert_class)

    b.pack (padx=20, pady=10)
    t2.mainloop ()


# 增加班级到数据库中
def insert_class():
    s0 = add_cn.get ()
    s1 = add_pn.get ()
    a1 = "insert into 班级(班级号,人数) values ("
    if s0 == '':
        sql1 = a1 + 'null' + ','
    else:
        sql1 = a1 + '\'' + s0 + '\'' + ','
    if s1 == '':
        sql1 = sql1 + 'null' + ')'
    else:
        sql1 = sql1 + '\'' + s1 + '\'' + ')'
    try:
        cursor.execute (sql1)
        db.commit ()
    except Exception as e:
        db.rollback ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        t1.destroy ()
        t2.destroy ()
        return
    db.commit ()
    tk.messagebox.showinfo ('温馨提醒', message='增加成功！')
    t1.destroy ()
    t2.destroy ()
    update_classgrades ()


# 增加院系
def add_department():
    global t3
    global add_dn
    global add_ana
    global add_dna
    t3 = tk.Toplevel ()
    t3.title ("增加一条院系记录")
    t3.geometry ('300x180+440+240')
    frame = tk.Frame (t3)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='系号      ').pack (padx=20, pady=10)
    add_dn = tk.Entry (frame_r, show=None)
    add_dn.pack (padx=20, pady=10)
    tk.Label (frame_l, text='学院名    ').pack (padx=20, pady=10)
    add_ana = tk.Entry (frame_r, show=None)
    add_ana.pack (padx=20, pady=10)
    tk.Label (frame_l, text='系名      ').pack (padx=20, pady=10)
    add_dna = tk.Entry (frame_r, show=None)
    add_dna.pack (padx=20, pady=10)

    b = tk.Button (t3, text='确定', width=15, height=1, command=insert_department)
    b.pack (padx=20, pady=10)
    t3.mainloop ()


# 插入院系到数据库中
def insert_department():
    s0 = add_dn.get ()
    s1 = add_ana.get ()
    s2 = add_dna.get ()
    a1 = "insert into 院系(系号,学院名,系名) values ("
    if s0 == '':
        sql1 = a1 + 'null' + ','
    else:
        sql1 = a1 + '\'' + s0 + '\'' + ','
    if s1 == '':
        sql1 = sql1 + 'null' + ','
    else:
        sql1 = sql1 + '\'' + s1 + '\'' + ','
    if s2 == '':
        sql1 = sql1 + 'null' + ')'
    else:
        sql1 = sql1 + '\'' + s2 + '\'' + ')'
    try:
        cursor.execute (sql1)
        db.commit ()
    except Exception as e:
        db.rollback ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        t1.destroy ()
        t3.destroy ()
        return
    db.commit ()
    tk.messagebox.showinfo ('温馨提醒', message='增加成功！')
    t1.destroy ()
    t3.destroy ()
    update_classgrades ()


# 增加辅导员
def add_instructor():
    global t4
    global add_dn1
    global add_in
    global add_ina
    global add_is
    global add_tel

    t4 = tk.Toplevel ()
    t4.title ("增加一条辅导员记录")
    t4.geometry ('300x280+440+240')
    frame = tk.Frame (t4)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='系号      ').pack (padx=20, pady=10)
    add_dn1 = tk.Entry (frame_r, show=None)
    add_dn1.pack (padx=20, pady=10)
    tk.Label (frame_l, text='辅导员编号').pack (padx=20, pady=10)
    add_in = tk.Entry (frame_r, show=None)
    add_in.pack (padx=20, pady=10)
    tk.Label (frame_l, text='姓名      ').pack (padx=20, pady=10)
    add_ina = tk.Entry (frame_r, show=None)
    add_ina.pack (padx=20, pady=10)
    tk.Label (frame_l, text='性别      ').pack (padx=20, pady=10)
    add_is = tk.Entry (frame_r, show=None)
    add_is.pack (padx=20, pady=10)
    tk.Label (frame_l, text='电话      ').pack (padx=20, pady=10)
    add_tel = tk.Entry (frame_r, show=None)
    add_tel.pack (padx=20, pady=10)

    b = tk.Button (t4, text='确定', width=15, height=1, command=insert_instructor)
    b.pack (padx=20, pady=10)
    t4.mainloop ()


# 插入辅导员到数据库中
def insert_instructor():
    s0 = add_dn1.get ()
    s1 = add_in.get ()
    s2 = add_ina.get ()
    s3 = add_is.get ()
    s4 = add_tel.get ()
    a1 = "insert into 辅导员(系号,辅导员编号,姓名,性别,电话) values ("
    if s0 == '':
        sql1 = a1 + 'null' + ','
    else:
        sql1 = a1 + '\'' + s0 + '\'' + ','
    if s1 == '':
        sql1 = sql1 + 'null' + ','
    else:
        sql1 = sql1 + '\'' + s1 + '\'' + ','
    if s2 == '':
        sql1 = sql1 + 'null' + ','
    else:
        sql1 = sql1 + '\'' + s2 + '\'' + ','
    if s3 == '':
        sql1 = sql1 + 'null' + ','
    else:
        sql1 = sql1 + '\'' + s3 + '\'' + ','
    if s4 == '':
        sql1 = sql1 + 'null' + ')'
    else:
        sql1 = sql1 + '\'' + s4 + '\'' + ')'

    try:
        cursor.execute (sql1)
        db.commit ()
    except Exception as e:
        db.rollback ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        t1.destroy ()
        t4.destroy ()
        return
    db.commit ()
    tk.messagebox.showinfo ('温馨提醒', message='增加成功！')
    t1.destroy ()
    t4.destroy ()
    update_classgrades ()


# 增加老师
def add_teacher():
    global t5
    global add_tn
    global add_dn2
    global add_tna
    global add_ts
    global add_ty

    t5 = tk.Toplevel ()
    t5.title ("增加一条教师记录")
    t5.geometry ('300x280+440+240')
    frame = tk.Frame (t5)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='教师编号  ').pack (padx=20, pady=10)
    add_tn = tk.Entry (frame_r, show=None)
    add_tn.pack (padx=20, pady=10)
    tk.Label (frame_l, text='系号      ').pack (padx=20, pady=10)
    add_dn2 = tk.Entry (frame_r, show=None)
    add_dn2.pack (padx=20, pady=10)
    tk.Label (frame_l, text='姓名      ').pack (padx=20, pady=10)
    add_tna = tk.Entry (frame_r, show=None)
    add_tna.pack (padx=20, pady=10)
    tk.Label (frame_l, text='性别      ').pack (padx=20, pady=10)
    add_ts = tk.Entry (frame_r, show=None)
    add_ts.pack (padx=20, pady=10)
    tk.Label (frame_l, text='年龄      ').pack (padx=20, pady=10)
    add_ty = tk.Entry (frame_r, show=None)
    add_ty.pack (padx=20, pady=10)

    b = tk.Button (t5, text='确定', width=15, height=1, command=insert_teacher)
    b.pack (padx=20, pady=10)
    t5.mainloop ()


# 将老师插入到数据库中
def insert_teacher():
    s0 = add_tn.get ()
    s1 = add_dn2.get ()
    s2 = add_tna.get ()
    s3 = add_ts.get ()
    s4 = add_ty.get ()
    a1 = "insert into 教师(教师编号,系号,姓名,性别,年龄) values ("
    if s0 == '':
        sql1 = a1 + 'null' + ','
    else:
        sql1 = a1 + '\'' + s0 + '\'' + ','
    if s1 == '':
        sql1 = sql1 + 'null' + ','
    else:
        sql1 = sql1 + '\'' + s1 + '\'' + ','
    if s2 == '':
        sql1 = sql1 + 'null' + ','
    else:
        sql1 = sql1 + '\'' + s2 + '\'' + ','
    if s3 == '':
        sql1 = sql1 + 'null' + ','
    else:
        sql1 = sql1 + '\'' + s3 + '\'' + ','
    if s4 == '':
        sql1 = sql1 + 'null' + ')'
    else:
        sql1 = sql1 + '\'' + s4 + '\'' + ')'
    try:
        cursor.execute (sql1)
        db.commit ()
    except Exception as e:
        db.rollback ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        t1.destroy ()
        t5.destroy ()
        return
    db.commit ()
    tk.messagebox.showinfo ('温馨提醒', message='增加成功！')
    t1.destroy ()
    t5.destroy ()
    update_classgrades ()


# 增加一个学生
def add_student():
    global t6
    global add_sn
    global add_cn1
    global add_sna
    global add_ss
    global add_sy
    global add_dn3

    t6 = tk.Toplevel ()
    t6.title ("增加一条学生记录")
    t6.geometry ('300x310+440+240')
    frame = tk.Frame (t6)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='学号      ').pack (padx=20, pady=10)
    add_sn = tk.Entry (frame_r, show=None)
    add_sn.pack (padx=20, pady=10)
    tk.Label (frame_l, text='班级号    ').pack (padx=20, pady=10)
    add_cn1 = tk.Entry (frame_r, show=None)
    add_cn1.pack (padx=20, pady=10)
    tk.Label (frame_l, text='姓名      ').pack (padx=20, pady=10)
    add_sna = tk.Entry (frame_r, show=None)
    add_sna.pack (padx=20, pady=10)
    tk.Label (frame_l, text='性别      ').pack (padx=20, pady=10)
    add_ss = tk.Entry (frame_r, show=None)
    add_ss.pack (padx=20, pady=10)
    tk.Label (frame_l, text='年龄      ').pack (padx=20, pady=10)
    add_sy = tk.Entry (frame_r, show=None)
    add_sy.pack (padx=20, pady=10)
    tk.Label (frame_l, text='系号      ').pack (padx=20, pady=10)
    add_dn3 = tk.Entry (frame_r, show=None)
    add_dn3.pack (padx=20, pady=10)

    b = tk.Button (t6, text='确定', width=15, height=1, command=insert_student)
    b.pack (padx=20, pady=10)
    t6.mainloop ()


# 将学生插入到数据库中
def insert_student():
    s0 = add_sn.get ()
    s1 = add_cn1.get ()
    s2 = add_sna.get ()
    s3 = add_ss.get ()
    s4 = add_sy.get ()
    s5 = add_dn3.get ()

    a1 = "insert into 学生(学号,班级号,姓名,性别,年龄,系号) values ("
    if s0 == '':
        sql1 = a1 + 'null' + ','
    else:
        sql1 = a1 + '\'' + s0 + '\'' + ','
    if s1 == '':
        sql1 = sql1 + 'null' + ','
    else:
        sql1 = sql1 + '\'' + s1 + '\'' + ','
    if s2 == '':
        sql1 = sql1 + 'null' + ','
    else:
        sql1 = sql1 + '\'' + s2 + '\'' + ','
    if s3 == '':
        sql1 = sql1 + 'null' + ','
    else:
        sql1 = sql1 + '\'' + s3 + '\'' + ','
    if s4 == '':
        sql1 = sql1 + 'null' + ','
    else:
        sql1 = sql1 + '\'' + s4 + '\'' + ','
    if s5 == '':
        sql1 = sql1 + 'null' + ')'
    else:
        sql1 = sql1 + '\'' + s5 + '\'' + ')'
    try:
        cursor.execute (sql1)
        db.commit ()
    except Exception as e:
        db.rollback ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        t1.destroy ()
        t6.destroy ()
        return
    db.commit ()
    tk.messagebox.showinfo ('温馨提醒', message='增加成功！')
    t1.destroy ()
    t6.destroy ()
    update_classgrades ()


# 增加课程
def add_course():
    global t7
    global add_con
    global add_cona
    global add_tn1
    global add_coc
    global add_cot
    global add_dn4

    t7 = tk.Toplevel ()
    t7.title ("增加一条课程记录")
    t7.geometry ('300x310+440+240')
    frame = tk.Frame (t7)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='课号      ').pack (padx=20, pady=10)
    add_con = tk.Entry (frame_r, show=None)
    add_con.pack (padx=20, pady=10)
    tk.Label (frame_l, text='课程名    ').pack (padx=20, pady=10)
    add_cona = tk.Entry (frame_r, show=None)
    add_cona.pack (padx=20, pady=10)
    tk.Label (frame_l, text='教师编号  ').pack (padx=20, pady=10)
    add_tn1 = tk.Entry (frame_r, show=None)
    add_tn1.pack (padx=20, pady=10)
    tk.Label (frame_l, text='学分      ').pack (padx=20, pady=10)
    add_coc = tk.Entry (frame_r, show=None)
    add_coc.pack (padx=20, pady=10)
    tk.Label (frame_l, text='学时      ').pack (padx=20, pady=10)
    add_cot = tk.Entry (frame_r, show=None)
    add_cot.pack (padx=20, pady=10)
    tk.Label (frame_l, text='系号      ').pack (padx=20, pady=10)
    add_dn4 = tk.Entry (frame_r, show=None)
    add_dn4.pack (padx=20, pady=10)

    b = tk.Button (t7, text='确定', width=15, height=1, command=insert_course)
    b.pack (padx=20, pady=10)
    t7.mainloop ()


# 将课程插入到数据库中
def insert_course():
    s0 = add_con.get ()
    s1 = add_cona.get ()
    s2 = add_tn1.get ()
    s3 = add_coc.get ()
    s4 = add_cot.get ()
    s5 = add_dn4.get ()

    a1 = "insert into 课程(课号,课程名,教师编号,学分,学时,系号) values ("
    if s0 == '':
        sql1 = a1 + 'null' + ','
    else:
        sql1 = a1 + '\'' + s0 + '\'' + ','
    if s1 == '':
        sql1 = sql1 + 'null' + ','
    else:
        sql1 = sql1 + '\'' + s1 + '\'' + ','
    if s2 == '':
        sql1 = sql1 + 'null' + ','
    else:
        sql1 = sql1 + '\'' + s2 + '\'' + ','
    if s3 == '':
        sql1 = sql1 + 'null' + ','
    else:
        sql1 = sql1 + '\'' + s3 + '\'' + ','
    if s4 == '':
        sql1 = sql1 + 'null' + ','
    else:
        sql1 = sql1 + '\'' + s4 + '\'' + ','
    if s5 == '':
        sql1 = sql1 + 'null' + ')'
    else:
        sql1 = sql1 + '\'' + s5 + '\'' + ')'
    try:
        cursor.execute (sql1)
        db.commit ()
    except Exception as e:
        db.rollback ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        t1.destroy ()
        t7.destroy ()
        return
    db.commit ()
    tk.messagebox.showinfo ('温馨提醒', message='增加成功！')
    t1.destroy ()
    t7.destroy ()
    update_classgrades ()


# 增加学生成绩
def add_student_result():
    global t8
    global add_sn1
    global add_con1
    global add_sr
    t8 = tk.Toplevel ()
    t8.title ("增加一条学生成绩记录")
    t8.geometry ('300x180+440+240')
    frame = tk.Frame (t8)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='学号      ').pack (padx=20, pady=10)
    add_sn1 = tk.Entry (frame_r, show=None)
    add_sn1.pack (padx=20, pady=10)
    tk.Label (frame_l, text='课号      ').pack (padx=20, pady=10)
    add_con1 = tk.Entry (frame_r, show=None)
    add_con1.pack (padx=20, pady=10)
    tk.Label (frame_l, text='成绩      ').pack (padx=20, pady=10)
    add_sr = tk.Entry (frame_r, show=None)
    add_sr.pack (padx=20, pady=10)

    b = tk.Button (t8, text='确定', width=15, height=1, command=insert_student_result)
    b.pack (padx=20, pady=10)
    t8.mainloop ()


# 插入学生成绩到数据库中
def insert_student_result():
    s0 = add_sn1.get ()
    s1 = add_con1.get ()
    s2 = add_sr.get ()
    a1 = "insert into 学生成绩(学号,课号,成绩) values ("
    if s0 == '':
        sql1 = a1 + 'null' + ','
    else:
        sql1 = a1 + '\'' + s0 + '\'' + ','
    if s1 == '':
        sql1 = sql1 + 'null' + ','
    else:
        sql1 = sql1 + '\'' + s1 + '\'' + ','
    if s2 == '':
        sql1 = sql1 + 'null' + ')'
    else:
        sql1 = sql1 + '\'' + s2 + '\'' + ')'
    try:
        cursor.execute (sql1)
        db.commit ()
    except Exception as e:
        db.rollback ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        t1.destroy ()
        t8.destroy ()
        return
    db.commit ()
    tk.messagebox.showinfo ('温馨提醒', message='增加成功！')
    t1.destroy ()
    t8.destroy ()
    update_classgrades ()


# 删除目录
def delete():
    global t01
    t01 = tk.Toplevel ()
    t01.title ("删除记录")
    t01.geometry ('280x400+420+220')

    l = tk.Label (t01, text='删除记录', bg='yellow')
    l.pack (padx=20, pady=10)
    b = tk.Button (t01, text='删除班级', width=10, height=1, command=delete_class, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t01, text='删除辅导员', width=10, height=1, command=delete_instructor, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t01, text='删除教师', width=10, height=1, command=delete_teacher, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t01, text='删除课程', width=10, height=1, command=delete_course, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t01, text='删除学生', width=10, height=1, command=delete_student, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t01, text='删除学生成绩', width=10, height=1, command=delete_student_result, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t01, text='删除院系', width=10, height=1, command=delete_department, bg='yellow')
    b.pack (padx=20, pady=10)

    t01.mainloop ()


# 删除班级
def delete_class():
    global del_cn
    global t02
    t02 = tk.Toplevel ()
    t02.title ("删除一条班级记录")
    t02.geometry ('300x100+440+240')
    frame = tk.Frame (t02)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='班级号    ').pack (padx=20, pady=10)
    del_cn = tk.Entry (frame_r, show=None)
    del_cn.pack (padx=20, pady=10)

    b = tk.Button (t02, text='确定', width=15, height=1, command=deleteDb_class)
    b.pack (padx=20, pady=10)
    t02.mainloop ()


# 在数据库中删除班级
def deleteDb_class():
    id1 = del_cn.get ()
    if id1 != '':
        sql1 = "delete from 班级 where 班级号=" + '\'' + id1 + '\''
    else:
        sql1 = "delete from 班级 where 班级号=" + 'null'

    try:
        i = cursor.execute (sql1)
    except Exception as e:
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        t01.destroy ()
        t02.destroy ()
        return
    if i != 0:  # mysql会返回一个值，当命令执行成功为1，失败为0
        db.commit ()
    else:
        db.rollback ()
        tk.messagebox.showinfo (title='温馨提醒', message="删除失败")
        t01.destroy ()
        t02.destroy ()
        return
    tk.messagebox.showinfo (title='温馨提醒', message="删除成功")
    t01.destroy ()
    t02.destroy ()
    update_classgrades ()


# 删除院系
def delete_department():
    global del_dn
    global t03
    t03 = tk.Toplevel ()
    t03.title ("删除一条院系记录")
    t03.geometry ('300x100+440+240')
    frame = tk.Frame (t03)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='系号    ').pack (padx=20, pady=10)
    del_dn = tk.Entry (frame_r, show=None)
    del_dn.pack (padx=20, pady=10)

    b = tk.Button (t03, text='确定', width=15, height=1, command=deleteDb_department)
    b.pack (padx=20, pady=10)
    t03.mainloop ()


# 在数据库中删除院系
def deleteDb_department():
    id1 = del_dn.get ()
    if id1 != '':
        sql1 = "delete from 院系 where 系号=" + '\'' + id1 + '\''
    else:
        sql1 = "delete from 院系 where 系号=" + 'null'
    try:
        i = cursor.execute (sql1)
    except Exception as e:
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        t01.destroy ()
        t03.destroy ()
        return
    if i != 0:  # mysql会返回一个值，当命令执行成功为1，失败为0
        db.commit ()
    else:
        db.rollback ()
        tk.messagebox.showinfo (title='温馨提醒', message="删除失败")
        t01.destroy ()
        t03.destroy ()
        return
    tk.messagebox.showinfo (title='温馨提醒', message="删除成功")
    t01.destroy ()
    t03.destroy ()
    update_classgrades ()


# 删除辅导员
def delete_instructor():
    global del_dn1
    global del_in
    global t04
    t04 = tk.Toplevel ()
    t04.title ("删除一条辅导员记录")
    t04.geometry ('300x140+440+240')
    frame = tk.Frame (t04)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='系号      ').pack (padx=20, pady=10)
    del_dn1 = tk.Entry (frame_r, show=None)
    del_dn1.pack (padx=20, pady=10)
    tk.Label (frame_l, text='辅导员编号').pack (padx=20, pady=10)
    del_in = tk.Entry (frame_r, show=None)
    del_in.pack (padx=20, pady=10)

    b = tk.Button (t04, text='确定', width=15, height=1, command=deleteDb_instructor)
    b.pack (padx=20, pady=10)
    t04.mainloop ()


# 在数据库中删除辅导员
def deleteDb_instructor():
    id1 = del_dn1.get ()
    id2 = del_in.get ()
    if id1 != '':
        sql1 = "delete from 辅导员 where (系号,辅导员编号)=(" + '\'' + id1 + '\'' + ','
    else:
        sql1 = "delete from 辅导员 where (系号,辅导员编号)=(" + 'null' + ','
    if id2 != '':
        sql1 = sql1 + '\'' + id2 + '\'' + ')'
    else:
        sql1 = sql1 + 'null' + ')'

    try:
        i = cursor.execute (sql1)
    except Exception as e:
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        t01.destroy ()
        t04.destroy ()
        return
    if i != 0:  # mysql会返回一个值，当命令执行成功为1，失败为0
        db.commit ()
    else:
        db.rollback ()
        tk.messagebox.showinfo (title='温馨提醒', message="删除失败")
        t01.destroy ()
        t04.destroy ()
        return
    tk.messagebox.showinfo (title='温馨提醒', message="删除成功")
    t01.destroy ()
    t04.destroy ()
    update_classgrades ()


# 删除教师
def delete_teacher():
    global del_tn
    global t05
    t05 = tk.Toplevel ()
    t05.title ("删除一条教师记录")
    t05.geometry ('300x100+440+240')
    frame = tk.Frame (t05)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='教师编号  ').pack (padx=20, pady=10)
    del_tn = tk.Entry (frame_r, show=None)
    del_tn.pack (padx=20, pady=10)

    b = tk.Button (t05, text='确定', width=15, height=1, command=deleteDb_teacher)
    b.pack (padx=20, pady=10)
    t05.mainloop ()


# 在数据库中删除教师
def deleteDb_teacher():
    id1 = del_tn.get ()
    if id1 != '':
        sql1 = "delete from 教师 where 教师编号=" + '\'' + id1 + '\''
    else:
        sql1 = "delete from 教师 where 教师编号=" + 'null'
    try:
        i = cursor.execute (sql1)
    except Exception as e:
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        t01.destroy ()
        t05.destroy ()
        return
    if i != 0:  # mysql会返回一个值，当命令执行成功为1，失败为0
        db.commit ()
    else:
        db.rollback ()
        tk.messagebox.showinfo (title='温馨提醒', message="删除失败")
        t01.destroy ()
        t05.destroy ()
        return
    tk.messagebox.showinfo (title='温馨提醒', message="删除成功")
    t01.destroy ()
    t05.destroy ()
    update_classgrades ()


# 删除学生
def delete_student():
    global del_sn
    global t06
    t06 = tk.Toplevel ()
    t06.title ("删除一条学生记录")
    t06.geometry ('300x100+440+240')
    frame = tk.Frame (t06)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='学号      ').pack (padx=20, pady=10)
    del_sn = tk.Entry (frame_r, show=None)
    del_sn.pack (padx=20, pady=10)

    b = tk.Button (t06, text='确定', width=15, height=1, command=deleteDb_student)
    b.pack (padx=20, pady=10)
    t06.mainloop ()


# 在数据库中删除学生
def deleteDb_student():
    id1 = del_sn.get ()
    if id1 != '':
        sql1 = "delete from 学生 where 学号=" + '\'' + id1 + '\''
    else:
        sql1 = "delete from 学生 where 学号=" + 'null'
    try:
        i = cursor.execute (sql1)
    except Exception as e:
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        t01.destroy ()
        t06.destroy ()
        return
    if i != 0:  # mysql会返回一个值，当命令执行成功为1，失败为0
        db.commit ()
    else:
        db.rollback ()
        tk.messagebox.showinfo (title='温馨提醒', message="删除失败")
        t01.destroy ()
        t06.destroy ()
        return
    tk.messagebox.showinfo (title='温馨提醒', message="删除成功")
    t01.destroy ()
    t06.destroy ()
    update_classgrades ()


# 删除课程
def delete_course():
    global del_con
    global t07
    t07 = tk.Toplevel ()
    t07.title ("删除一条课程记录")
    t07.geometry ('300x100+440+240')
    frame = tk.Frame (t07)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='课号      ').pack (padx=20, pady=10)
    del_con = tk.Entry (frame_r, show=None)
    del_con.pack (padx=20, pady=10)

    b = tk.Button (t07, text='确定', width=15, height=1, command=deleteDb_course)
    b.pack (padx=20, pady=10)
    t07.mainloop ()


# 在数据库中删除课程
def deleteDb_course():
    id1 = del_con.get ()
    if id1 != '':
        sql1 = "delete from 课程 where 课号=" + '\'' + id1 + '\''
    else:
        sql1 = "delete from 课程 where 课号=" + 'null'
    try:
        i = cursor.execute (sql1)
    except Exception as e:
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        t01.destroy ()
        t07.destroy ()
        return
    if i != 0:  # mysql会返回一个值，当命令执行成功为1，失败为0
        db.commit ()
    else:
        db.rollback ()
        tk.messagebox.showinfo (title='温馨提醒', message="删除失败")
        t01.destroy ()
        t07.destroy ()
        return
    tk.messagebox.showinfo (title='温馨提醒', message="删除成功")
    t01.destroy ()
    t07.destroy ()
    update_classgrades ()


# 删除学生成绩
def delete_student_result():
    global del_sn1
    global del_con1
    global t08
    t08 = tk.Toplevel ()
    t08.title ("删除一条学生成绩记录")
    t08.geometry ('300x140+440+240')
    frame = tk.Frame (t08)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='学号      ').pack (padx=20, pady=10)
    del_sn1 = tk.Entry (frame_r, show=None)
    del_sn1.pack (padx=20, pady=10)
    tk.Label (frame_l, text='课号      ').pack (padx=20, pady=10)
    del_con1 = tk.Entry (frame_r, show=None)
    del_con1.pack (padx=20, pady=10)

    b = tk.Button (t08, text='确定', width=15, height=1, command=deleteDb_student_result)
    b.pack (padx=20, pady=10)
    t08.mainloop ()


# 在数据库中删除学生成绩
def deleteDb_student_result():
    id1 = del_sn1.get ()
    id2 = del_con1.get ()
    if id1 != '':
        sql1 = "delete from 学生成绩 where (学号,课号)=(" + '\'' + id1 + '\'' + ','
    else:
        sql1 = "delete from 学生成绩 where (学号,课号)=(" + 'null' + ','
    if id2 != '':
        sql1 = sql1 + '\'' + id2 + '\'' + ')'
    else:
        sql1 = sql1 + 'null' + ')'
    try:
        i = cursor.execute (sql1)
    except Exception as e:
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        t01.destroy ()
        t08.destroy ()
        return
    if i != 0:  # mysql会返回一个值，当命令执行成功为1，失败为0
        db.commit ()
    else:
        db.rollback ()
        tk.messagebox.showinfo (title='温馨提醒', message="删除失败")
        t01.destroy ()
        t08.destroy ()
        return
    tk.messagebox.showinfo (title='温馨提醒', message="删除成功")
    t01.destroy ()
    t08.destroy ()
    update_classgrades ()


# 修改数据目录
def modify():
    global t11
    t11 = tk.Toplevel ()
    t11.title ("修改记录")
    t11.geometry ('280x400+420+220')

    l = tk.Label (t11, text='修改记录', bg='yellow')
    l.pack (padx=20, pady=10)
    b = tk.Button (t11, text='修改班级', width=10, height=1, command=modify_class, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t11, text='修改辅导员', width=10, height=1, command=modify_instructor, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t11, text='修改教师', width=10, height=1, command=modify_teacher, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t11, text='修改课程', width=10, height=1, command=modify_course, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t11, text='修改学生', width=10, height=1, command=modify_student, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t11, text='修改学生成绩', width=10, height=1, command=modify_student_result, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t11, text='修改院系', width=10, height=1, command=modify_department, bg='yellow')
    b.pack (padx=20, pady=10)

    t11.mainloop ()


# 修改班级
def modify_class():
    global t12
    global modify_cn
    global modify_pn
    t12 = tk.Toplevel ()
    t12.title ("修改一条班级记录")
    t12.geometry ('300x140+440+240')
    frame = tk.Frame (t12)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='班号      ').pack (padx=20, pady=10)
    modify_cn = tk.Entry (frame_r, show=None)
    modify_cn.pack (padx=20, pady=10)
    tk.Label (frame_l, text='人数        ').pack (padx=20, pady=10)
    modify_pn = tk.Entry (frame_r, show=None)
    modify_pn.pack (padx=20, pady=10)
    b = tk.Button (t12, text='确定', width=15, height=1, command=modifyDb_class)

    b.pack (padx=20, pady=10)
    t12.mainloop ()


# 在数据库中修改班级
def modifyDb_class():
    s0 = modify_cn.get ()
    s1 = modify_pn.get ()
    a1 = "update 班级 set 人数="
    if s1 == '':
        sql1 = a1 + 'null'
    else:
        sql1 = a1 + '\'' + s1 + '\''

    sql1 = sql1 + " where 班级号=" + '\'' + s0 + '\''

    try:
        cursor.execute (sql1)
        db.commit ()
    except Exception as e:
        db.rollback ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        t11.destroy ()
        t12.destroy ()
        return
    db.commit ()
    tk.messagebox.showinfo ('温馨提醒', message='修改成功！')
    t11.destroy ()
    t12.destroy ()
    update_classgrades ()


# 修改辅导员
def modify_instructor():
    global t14
    global modify_dn1
    global modify_in
    global modify_ina
    global modify_is
    global modify_tel

    t14 = tk.Toplevel ()
    t14.title ("修改一条辅导员记录")
    t14.geometry ('300x280+440+240')
    frame = tk.Frame (t14)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='系号      ').pack (padx=20, pady=10)
    modify_dn1 = tk.Entry (frame_r, show=None)
    modify_dn1.pack (padx=20, pady=10)
    tk.Label (frame_l, text='辅导员编号').pack (padx=20, pady=10)
    modify_in = tk.Entry (frame_r, show=None)
    modify_in.pack (padx=20, pady=10)
    tk.Label (frame_l, text='姓名      ').pack (padx=20, pady=10)
    modify_ina = tk.Entry (frame_r, show=None)
    modify_ina.pack (padx=20, pady=10)
    tk.Label (frame_l, text='性别      ').pack (padx=20, pady=10)
    modify_is = tk.Entry (frame_r, show=None)
    modify_is.pack (padx=20, pady=10)
    tk.Label (frame_l, text='电话      ').pack (padx=20, pady=10)
    modify_tel = tk.Entry (frame_r, show=None)
    modify_tel.pack (padx=20, pady=10)

    b = tk.Button (t14, text='确定', width=15, height=1, command=modify_instructor_Db)
    b.pack (padx=20, pady=10)
    t14.mainloop ()


# 在数据库中修改辅导员
def modify_instructor_Db():
    s0 = modify_dn1.get ()
    s1 = modify_in.get ()
    s2 = modify_ina.get ()
    s3 = modify_is.get ()
    s4 = modify_tel.get ()
    a1 = "update 辅导员 set 姓名="
    if s2 == '':
        sql1 = a1 + 'null,'
    else:
        sql1 = a1 + '\'' + s2 + '\','
    if s3 == '':
        sql1 = sql1 + '性别=null,'
    else:
        sql1 = sql1 + '性别=\'' + s3 + '\','
    if s4 == '':
        sql1 = sql1 + '电话=null'
    else:
        sql1 = sql1 + '电话=\'' + s4 + '\''

    sql1 = sql1 + " where (系号,辅导员编号)=" + '(\'' + s0 + '\',\'' + s1 + '\')'

    try:
        cursor.execute (sql1)
        db.commit ()
    except Exception as e:
        db.rollback ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        t11.destroy ()
        t14.destroy ()
        return
    db.commit ()
    tk.messagebox.showinfo ('温馨提醒', message='修改成功！')
    t11.destroy ()
    t14.destroy ()
    update_classgrades ()


# 修改教师
def modify_teacher():
    global t15
    global modify_tn
    global modify_dn2
    global modify_tna
    global modify_ts
    global modify_ty

    t15 = tk.Toplevel ()
    t15.title ("修改一条教师记录")
    t15.geometry ('300x280+440+240')
    frame = tk.Frame (t15)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='教师编号  ').pack (padx=20, pady=10)
    modify_tn = tk.Entry (frame_r, show=None)
    modify_tn.pack (padx=20, pady=10)
    tk.Label (frame_l, text='系号      ').pack (padx=20, pady=10)
    modify_dn2 = tk.Entry (frame_r, show=None)
    modify_dn2.pack (padx=20, pady=10)
    tk.Label (frame_l, text='姓名      ').pack (padx=20, pady=10)
    modify_tna = tk.Entry (frame_r, show=None)
    modify_tna.pack (padx=20, pady=10)
    tk.Label (frame_l, text='性别      ').pack (padx=20, pady=10)
    modify_ts = tk.Entry (frame_r, show=None)
    modify_ts.pack (padx=20, pady=10)
    tk.Label (frame_l, text='年龄      ').pack (padx=20, pady=10)
    modify_ty = tk.Entry (frame_r, show=None)
    modify_ty.pack (padx=20, pady=10)

    b = tk.Button (t15, text='确定', width=15, height=1, command=modifyDb_teacher)
    b.pack (padx=20, pady=10)
    t15.mainloop ()


# 在数据库中修改教师
def modifyDb_teacher():
    s0 = modify_tn.get ()
    s1 = modify_dn2.get ()
    s2 = modify_tna.get ()
    s3 = modify_ts.get ()
    s4 = modify_ty.get ()
    a1 = "update 教师 set 系号="
    if s1 == '':
        sql1 = a1 + 'null,'
    else:
        sql1 = a1 + '\'' + s1 + '\','
    if s2 == '':
        sql1 = sql1 + '姓名=null,'
    else:
        sql1 = sql1 + '姓名=\'' + s2 + '\','
    if s3 == '':
        sql1 = sql1 + '性别=null,'
    else:
        sql1 = sql1 + '性别=\'' + s3 + '\','
    if s4 == '':
        sql1 = sql1 + '年龄=null'
    else:
        sql1 = sql1 + '年龄=\'' + s4 + '\''

    sql1 = sql1 + " where 教师编号=" + '\'' + s0 + '\''

    try:
        cursor.execute (sql1)
        db.commit ()
    except Exception as e:
        db.rollback ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        t11.destroy ()
        t15.destroy ()
        return
    db.commit ()
    tk.messagebox.showinfo ('温馨提醒', message='修改成功！')
    t11.destroy ()
    t15.destroy ()
    update_classgrades ()


# 修改课程
def modify_course():
    global t17
    global modify_con
    global modify_cona
    global modify_tn1
    global modify_coc
    global modify_cot
    global modify_dn4

    t17 = tk.Toplevel ()
    t17.title ("修改一条课程记录")
    t17.geometry ('300x310+440+240')
    frame = tk.Frame (t17)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='课号      ').pack (padx=20, pady=10)
    modify_con = tk.Entry (frame_r, show=None)
    modify_con.pack (padx=20, pady=10)
    tk.Label (frame_l, text='课程名    ').pack (padx=20, pady=10)
    modify_cona = tk.Entry (frame_r, show=None)
    modify_cona.pack (padx=20, pady=10)
    tk.Label (frame_l, text='教师编号  ').pack (padx=20, pady=10)
    modify_tn1 = tk.Entry (frame_r, show=None)
    modify_tn1.pack (padx=20, pady=10)
    tk.Label (frame_l, text='学分      ').pack (padx=20, pady=10)
    modify_coc = tk.Entry (frame_r, show=None)
    modify_coc.pack (padx=20, pady=10)
    tk.Label (frame_l, text='学时      ').pack (padx=20, pady=10)
    modify_cot = tk.Entry (frame_r, show=None)
    modify_cot.pack (padx=20, pady=10)
    tk.Label (frame_l, text='系号      ').pack (padx=20, pady=10)
    modify_dn4 = tk.Entry (frame_r, show=None)
    modify_dn4.pack (padx=20, pady=10)

    b = tk.Button (t17, text='确定', width=15, height=1, command=modifyDb_course)
    b.pack (padx=20, pady=10)
    t17.mainloop ()


# 在数据库中修改课程
def modifyDb_course():
    s0 = modify_con.get ()
    s1 = modify_cona.get ()
    s2 = modify_tn1.get ()
    s3 = modify_coc.get ()
    s4 = modify_cot.get ()
    s5 = modify_dn4.get ()

    a1 = "update 课程 set 课程名="
    if s1 == '':
        sql1 = a1 + 'null,'
    else:
        sql1 = a1 + '\'' + s1 + '\','
    if s2 == '':
        sql1 = sql1 + '教师编号=null,'
    else:
        sql1 = sql1 + '教师编号=\'' + s2 + '\','
    if s3 == '':
        sql1 = sql1 + '学分=null,'
    else:
        sql1 = sql1 + '学分=\'' + s3 + '\','
    if s4 == '':
        sql1 = sql1 + '学时=null,'
    else:
        sql1 = sql1 + '学时=\'' + s4 + '\','
    if s5 == '':
        sql1 = sql1 + '系号=null'
    else:
        sql1 = sql1 + '系号=\'' + s5 + '\''

    sql1 = sql1 + " where 课号=" + '\'' + s0 + '\''
    try:
        cursor.execute (sql1)
        db.commit ()
    except Exception as e:
        db.rollback ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        t11.destroy ()
        t17.destroy ()
        return
    db.commit ()
    tk.messagebox.showinfo ('温馨提醒', message='修改成功！')
    t11.destroy ()
    t17.destroy ()
    update_classgrades ()


# 修改学生
def modify_student():
    global t16
    global modify_sn
    global modify_cn1
    global modify_sna
    global modify_ss
    global modify_sy
    global modify_dn3

    t16 = tk.Toplevel ()
    t16.title ("修改一条学生记录")
    t16.geometry ('300x310+440+240')
    frame = tk.Frame (t16)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='学号      ').pack (padx=20, pady=10)
    modify_sn = tk.Entry (frame_r, show=None)
    modify_sn.pack (padx=20, pady=10)
    tk.Label (frame_l, text='班级号    ').pack (padx=20, pady=10)
    modify_cn1 = tk.Entry (frame_r, show=None)
    modify_cn1.pack (padx=20, pady=10)
    tk.Label (frame_l, text='姓名      ').pack (padx=20, pady=10)
    modify_sna = tk.Entry (frame_r, show=None)
    modify_sna.pack (padx=20, pady=10)
    tk.Label (frame_l, text='性别      ').pack (padx=20, pady=10)
    modify_ss = tk.Entry (frame_r, show=None)
    modify_ss.pack (padx=20, pady=10)
    tk.Label (frame_l, text='年龄      ').pack (padx=20, pady=10)
    modify_sy = tk.Entry (frame_r, show=None)
    modify_sy.pack (padx=20, pady=10)
    tk.Label (frame_l, text='系号      ').pack (padx=20, pady=10)
    modify_dn3 = tk.Entry (frame_r, show=None)
    modify_dn3.pack (padx=20, pady=10)

    b = tk.Button (t16, text='确定', width=15, height=1, command=modifyDb_student)
    b.pack (padx=20, pady=10)
    t16.mainloop ()


# 在数据库中修改学生
def modifyDb_student():
    s0 = modify_sn.get ()
    s1 = modify_cn1.get ()
    s2 = modify_sna.get ()
    s3 = modify_ss.get ()
    s4 = modify_sy.get ()
    s5 = modify_dn3.get ()

    a1 = "update 学生 set 班级号="
    if s1 == '':
        sql1 = a1 + 'null,'
    else:
        sql1 = a1 + '\'' + s1 + '\','
    if s2 == '':
        sql1 = sql1 + '姓名=null,'
    else:
        sql1 = sql1 + '姓名=\'' + s2 + '\','
    if s3 == '':
        sql1 = sql1 + '性别=null,'
    else:
        sql1 = sql1 + '性别=\'' + s3 + '\','
    if s4 == '':
        sql1 = sql1 + '年龄=null,'
    else:
        sql1 = sql1 + '年龄=\'' + s4 + '\','
    if s5 == '':
        sql1 = sql1 + '系号=null'
    else:
        sql1 = sql1 + '系号=\'' + s5 + '\''

    sql1 = sql1 + " where 学号=" + '\'' + s0 + '\''
    try:
        cursor.execute (sql1)
        db.commit ()
    except Exception as e:
        db.rollback ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        t11.destroy ()
        t16.destroy ()
        return
    db.commit ()
    tk.messagebox.showinfo ('温馨提醒', message='修改成功！')
    t11.destroy ()
    t16.destroy ()
    update_classgrades ()


# 修改学生成绩
def modify_student_result():
    global t18
    global modify_sn1
    global modify_con1
    global modify_sr
    t18 = tk.Toplevel ()
    t18.title ("修改一条学生成绩记录")
    t18.geometry ('300x180+440+240')
    frame = tk.Frame (t18)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='学号      ').pack (padx=20, pady=10)
    modify_sn1 = tk.Entry (frame_r, show=None)
    modify_sn1.pack (padx=20, pady=10)
    tk.Label (frame_l, text='课号      ').pack (padx=20, pady=10)
    modify_con1 = tk.Entry (frame_r, show=None)
    modify_con1.pack (padx=20, pady=10)
    tk.Label (frame_l, text='成绩      ').pack (padx=20, pady=10)
    modify_sr = tk.Entry (frame_r, show=None)
    modify_sr.pack (padx=20, pady=10)

    b = tk.Button (t18, text='确定', width=15, height=1, command=modifyDb_student_result)
    b.pack (padx=20, pady=10)
    t18.mainloop ()


# 在数据库中修改学生成绩
def modifyDb_student_result():
    s0 = modify_sn1.get ()
    s1 = modify_con1.get ()
    s2 = modify_sr.get ()
    a1 = "update 学生成绩 set 成绩="
    if s2 == '':
        sql1 = a1 + 'null'
    else:
        sql1 = a1 + '\'' + s2 + '\''
    sql1 = sql1 + " where (学号,课号)=" + '(\'' + s0 + '\',\'' + s1 + '\')'
    try:
        cursor.execute (sql1)
        db.commit ()
    except Exception as e:
        db.rollback ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        t11.destroy ()
        t18.destroy ()
        return
    db.commit ()
    tk.messagebox.showinfo ('温馨提醒', message='修改成功！')
    t11.destroy ()
    t18.destroy ()
    update_classgrades ()


# 修改院系
def modify_department():
    global t13
    global modify_dn
    global modify_ana
    global modify_dna
    t13 = tk.Toplevel ()
    t13.title ("修改一条院系记录")
    t13.geometry ('300x180+440+240')
    frame = tk.Frame (t13)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='系号      ').pack (padx=20, pady=10)
    modify_dn = tk.Entry (frame_r, show=None)
    modify_dn.pack (padx=20, pady=10)
    tk.Label (frame_l, text='学院名    ').pack (padx=20, pady=10)
    modify_ana = tk.Entry (frame_r, show=None)
    modify_ana.pack (padx=20, pady=10)
    tk.Label (frame_l, text='系名      ').pack (padx=20, pady=10)
    modify_dna = tk.Entry (frame_r, show=None)
    modify_dna.pack (padx=20, pady=10)

    b = tk.Button (t13, text='确定', width=15, height=1, command=modifyDb_department)
    b.pack (padx=20, pady=10)
    t13.mainloop ()


# 在数据库中修改院系
def modifyDb_department():
    s0 = modify_dn.get ()
    s1 = modify_ana.get ()
    s2 = modify_dna.get ()
    a1 = "update 院系 set 学院名="
    if s1 == '':
        sql1 = a1 + 'null,'
    else:
        sql1 = a1 + '\'' + s1 + '\','
    if s2 == '':
        sql1 = sql1 + '系名=null'
    else:
        sql1 = sql1 + '系名=\'' + s2 + '\''

    sql1 = sql1 + " where 系号=" + '\'' + s0 + '\''

    try:
        cursor.execute (sql1)
        db.commit ()
    except Exception as e:
        db.rollback ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        t11.destroy ()
        t13.destroy ()
        return
    db.commit ()
    tk.messagebox.showinfo ('温馨提醒', message='修改成功！')
    t11.destroy ()
    t13.destroy ()
    update_classgrades ()


# 查询功能目录
def qury():
    global t21
    t21 = tk.Toplevel ()
    t21.title ("查询记录")
    t21.geometry ('280x220+420+220')

    l = tk.Label (t21, text='查询记录', bg='yellow')
    l.pack (padx=20, pady=10)
    b = tk.Button (t21, text='sql语句查询(开发者选项)', width=20, height=1, command=sql_qury, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t21, text='用户查询功能', width=20, height=1, command=quick_qury, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t21, text='学生成绩详细查询', width=20, height=1, command=student_qury, bg='yellow')
    b.pack (padx=20, pady=10)
    t21.mainloop ()


def student_qury():
    global t25
    global qury_13
    global qury_14
    global qury_15
    global qury_16
    global qury_17
    global qury_18
    global qury_19
    global qury_20
    global text1
    global text2
    global table1

    t42 = tk.Toplevel ()
    t42.title ("学生成绩详细查询")
    t42.geometry ('980x600+460+260')
    tl1 = tk.Label (t42, text='系号', bg='yellow')
    tl1.place (x=20, y=20, width=100, height=20)
    qury_13 = tk.Entry (t42, show=None)
    qury_13.place (x=140, y=20, width=100, height=20)
    tl1 = tk.Label (t42, text='班级号', bg='yellow')
    tl1.place (x=260, y=20, width=100, height=20)
    qury_14 = tk.Entry (t42, show=None)
    qury_14.place (x=380, y=20, width=100, height=20)
    tl1 = tk.Label (t42, text='学号', bg='yellow')
    tl1.place (x=500, y=20, width=100, height=20)
    qury_15 = tk.Entry (t42, show=None)
    qury_15.place (x=620, y=20, width=100, height=20)
    tl1 = tk.Label (t42, text='姓名', bg='yellow')
    tl1.place (x=740, y=20, width=100, height=20)
    qury_16 = tk.Entry (t42, show=None)
    qury_16.place (x=860, y=20, width=100, height=20)
    tl1 = tk.Label (t42, text='课号', bg='yellow')
    tl1.place (x=20, y=60, width=100, height=20)
    qury_17 = tk.Entry (t42, show=None)
    qury_17.place (x=140, y=60, width=100, height=20)
    tl1 = tk.Label (t42, text='课程名', bg='yellow')
    tl1.place (x=260, y=60, width=100, height=20)
    qury_18 = tk.Entry (t42, show=None)
    qury_18.place (x=380, y=60, width=100, height=20)
    tl1 = tk.Label (t42, text='成绩区间', bg='yellow')
    tl1.place (x=500, y=60, width=100, height=20)
    qury_19 = tk.Entry (t42, show=None)
    qury_19.place (x=620, y=60, width=100, height=20)
    tl1 = tk.Label (t42, text='-', bg='yellow')
    tl1.place (x=730, y=60, width=20, height=20)
    qury_20 = tk.Entry (t42, show=None)
    qury_20.place (x=760, y=60, width=100, height=20)
    b = tk.Button (t42, text='查询', width=30, height=1, command=student_qury_1)
    b.place (x=880, y=60, width=80, height=20)
    tl1 = tk.Label (t42, text='sql语句动态显示', bg='yellow')
    tl1.place (x=20, y=110, width=150, height=20)
    text1 = tk.Text (t42)
    text1.place (x=200, y=100, width=760, height=40)
    tl1 = tk.Label (t42, text='学生成绩信息的查询结果', bg='yellow')
    tl1.place (x=390, y=150, width=150, height=20)
    table1 = ttk.Treeview (t42)
    table1['columns'] = ['系号', '班级号', '学号', '姓名', '课号', '课程名', '成绩']
    table1.column ('系号', width=100)
    table1.column ('班级号', width=100)
    table1.column ('学号', width=100)
    table1.column ('姓名', width=100)
    table1.column ('课号', width=100)
    table1.column ('课程名', width=100)
    table1.column ('成绩', width=100)
    table1.heading ('系号', text='系号')
    table1.heading ('班级号', text='班级号')
    table1.heading ('学号', text='学号')
    table1.heading ('姓名', text='姓名')
    table1.heading ('课号', text='课号')
    table1.heading ('课程名', text='课程名')
    table1.heading ('成绩', text='成绩')
    table1.place (x=30, y=180, width=910, height=380)
    t42.mainloop ()


def student_qury_1():
    t1 = qury_13.get ()
    t2 = qury_14.get ()
    t3 = qury_15.get ()
    t4 = qury_16.get ()
    t5 = qury_17.get ()
    t6 = qury_18.get ()
    t7 = qury_19.get ()
    t8 = qury_20.get ()

    order = 'select * from 学生成绩（姓名）'
    if t1 == '' and t2 == '' and t3 == '' and t4 == '' and t5 == '' and t6 == '' and t7 == '' and t8 == '':
        order = order
    else:
        order = order + ' where'
        flag = 0
        if t1 != '':
            order = order + ' 系号 like ' + '\'' + t1 + '\''
            flag = 1
        if t2 != '':
            if flag == 1:
                order = order + ' and 班级号 like ' + '\'' + t2 + '\''
            else:
                order = order + ' 班级号 like ' + '\'' + t2 + '\''
                flag = 1
        if t3 != '':
            if flag == 1:
                order = order + ' and 学号 like ' + '\'' + t3 + '\''
            else:
                order = order + ' 学号 like ' + '\'' + t3 + '\''
                flag = 1
        if t4 != '':
            if flag == 1:
                order = order + ' and 姓名 like ' + '\'' + t4 + '\''
            else:
                order = order + ' 姓名 like ' + '\'' + t4 + '\''
                flag = 1
        if t5 != '':
            if flag == 1:
                order = order + ' and 课号 like ' + '\'' + t5 + '\''
            else:
                order = order + ' 课号 like ' + '\'' + t5 + '\''
                flag = 1
        if t6 != '':
            if flag == 1:
                order = order + ' and 课程名 like ' + '\'' + t6 + '\''
            else:
                order = order + ' 课程名 like ' + '\'' + t6 + '\''
                flag = 1
        if t7 != '' and t8 != '':
            if flag == 1:
                order = order + ' and 成绩 >=' + t7 + ' and 成绩 <= ' + t8
            else:
                order = order + ' 成绩 >= ' + t7 + ' and 成绩 <= ' + t8
        elif t7 != '' and t8 == '':
            if flag == 1:
                order = order + ' and 成绩 >=' + t7
            else:
                order = order + ' 成绩 >= ' + t7
        elif t7 == '' and t8 != '':
            if flag == 1:
                order = order + ' and 成绩 <= ' + t8
            else:
                order = order + ' 成绩 <= ' + t8
    try:
        text1.delete (1.0, tk.END)
        text1.insert (1.0, order)
        cursor.execute (order)
        result = cursor.fetchall ()
        num = 0
        x = table1.get_children ()
        for item in x:
            table1.delete (item)
        for r in result:
            table1.insert ('', num, text=str (num), values=(
                r.get ('系号'), r.get ('班级号'), r.get ('学号'), r.get ('姓名'), r.get ('课号'), r.get ('课程名'), r.get ('成绩')))
            num += 1
    except Exception as e:
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        return


# 输入sql语句查询
def sql_qury():
    global select_s
    global t22
    t22 = tk.Toplevel ()
    t22.title ("sql语句查询")
    t22.geometry ('300x140+440+240')
    tk.Label (t22, text='请输入您的查询语句').pack ()
    select_s = tk.Entry (t22, show=None)
    select_s.pack (padx=20, pady=10)
    b1 = tk.Button (t22, text='确定', width=15, height=1, command=sql_qury1)
    b1.pack (padx=20, pady=10)
    t22.mainloop ()


# 在数据库中执行sql语句并返回结果
def sql_qury1():
    t23 = tk.Toplevel ()
    t23.geometry ('600x300+460+260')
    tt = tk.Text (t23, height=20)
    tt.pack ()
    order = select_s.get ()
    try:
        cursor.execute (order)
    except Exception as e:
        t21.destroy ()
        t22.destroy ()
        t23.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        return
    result = cursor.fetchall ()
    flag = 1
    for i in result:
        tt.insert ('end', '%d' % flag + '. ' + str (i))
        tt.insert ('end', '\n')
        flag += 1
    t21.destroy ()
    t22.destroy ()


# 快速查询
def quick_qury():
    global t24
    t24 = tk.Toplevel ()
    t24.title ("快速查询")
    t24.geometry ('300x370+440+240')

    l = tk.Label (t24, text='查询功能选择', bg='yellow')
    l.pack (padx=20, pady=10)
    b = tk.Button (t24, text='查询院系辅导员', width=40, height=1, command=quick_qury1, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t24, text='查询教师教授课程', width=40, height=1, command=quick_qury2, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t24, text='查询某院系的全部学生信息', width=40, height=1, command=quick_qury6, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t24, text='查询学生成绩', width=40, height=1, command=quick_qury3, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t24, text='查询班级平均成绩', width=40, height=1, command=quick_qury4, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t24, text='查询有n门及以上不及格课程的同学的平均成绩', width=40, height=1, command=quick_qury5, bg='yellow')
    b.pack (padx=20, pady=10)

    t24.mainloop ()


# 查询院系辅导员
def quick_qury1():
    global t25
    global qury_1
    global qury_2

    t25 = tk.Toplevel ()
    t25.title ("查询院系辅导员")
    t25.geometry ('300x240+460+260')
    frame = tk.Frame (t25)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    l = tk.Label (t25, text='通过辅导员姓名或编号进行查询', bg='yellow')
    l.pack (padx=20, pady=10)
    tk.Label (frame_l, text='辅导员姓名').pack (padx=20, pady=10)
    qury_1 = tk.Entry (frame_r, show=None)
    qury_1.pack (padx=20, pady=10)
    b = tk.Button (t25, text='输入辅导员姓名请点击这个按钮', width=30, height=1, command=quick_qury11)
    b.pack (padx=20, pady=10)
    tk.Label (frame_l, text='辅导员编号').pack (padx=20, pady=10)
    qury_2 = tk.Entry (frame_r, show=None)
    qury_2.pack (padx=20, pady=10)
    b = tk.Button (t25, text='输入辅导员编号请点击这个按钮', width=30, height=1, command=quick_qury12)
    b.pack (padx=20, pady=10)
    t25.mainloop ()


# 若输入为辅导员姓名，将查询院系辅导员的sql语句传入数据库，并返回结果
def quick_qury11():
    t26 = tk.Toplevel ()
    t26.geometry ('600x300+480+280')
    tt = tk.Text (t26, height=20)
    tt.pack ()
    try:
        order = qury_1.get ()
        cursor.execute ("select * from 院系辅导员联系方式 where 姓名 = " + '\'' + order + '\'')
    except Exception as e:
        t21.destroy ()
        t24.destroy ()
        t25.destroy ()
        t26.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        return
    result = cursor.fetchall ()
    if len (result) == 0:
        t21.destroy ()
        t24.destroy ()
        t25.destroy ()
        t26.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message="There is no result you expect, please check the input!")
    flag = 1
    for i in result:
        tt.insert ('end', '%d' % flag + '. ' + str (i))
        tt.insert ('end', '\n')
        flag += 1
    t21.destroy ()
    t24.destroy ()
    t25.destroy ()


# 若输入为辅导员编号，将查询院系辅导员的sql语句传入数据库，并返回结果
def quick_qury12():
    t27 = tk.Toplevel ()
    t27.geometry ('600x300+480+280')
    tt = tk.Text (t27, height=20)
    tt.pack ()
    try:
        order = qury_2.get ()
        cursor.execute ("select * from 院系辅导员联系方式 where 辅导员编号=" + '\'' + order + '\'')
    except Exception as e:
        t21.destroy ()
        t24.destroy ()
        t25.destroy ()
        t27.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        return
    result = cursor.fetchall ()
    if len (result) == 0:
        t21.destroy ()
        t24.destroy ()
        t25.destroy ()
        t27.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message="There is no result you expect, please check the input!")
        return
    flag = 1
    for i in result:
        tt.insert ('end', '%d' % flag + '. ' + str (i))
        tt.insert ('end', '\n')
        flag += 1
    t21.destroy ()
    t24.destroy ()
    t25.destroy ()


# 查询教师教授课程
def quick_qury2():
    global t28
    global qury_3
    global qury_4

    t28 = tk.Toplevel ()
    t28.title ("查询教师教授课程")
    t28.geometry ('300x240+460+260')
    frame = tk.Frame (t28)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    l = tk.Label (t28, text='通过教师姓名或编号进行查询', bg='yellow')
    l.pack (padx=20, pady=10)
    tk.Label (frame_l, text='教师姓名  ').pack (padx=20, pady=10)
    qury_3 = tk.Entry (frame_r, show=None)
    qury_3.pack (padx=20, pady=10)
    b = tk.Button (t28, text='输入教师姓名请点击这个按钮', width=30, height=1, command=quick_qury21)
    b.pack (padx=20, pady=10)
    tk.Label (frame_l, text='教师编号  ').pack (padx=20, pady=10)
    qury_4 = tk.Entry (frame_r, show=None)
    qury_4.pack (padx=20, pady=10)
    b = tk.Button (t28, text='输入教师编号请点击这个按钮', width=30, height=1, command=quick_qury22)
    b.pack (padx=20, pady=10)
    t28.mainloop ()


# 若输入为教师姓名，将教师教授课程的sql语句传入数据库，并返回结果
def quick_qury21():
    t29 = tk.Toplevel ()
    t29.geometry ('600x300+480+280')
    tt = tk.Text (t29, height=20)
    tt.pack ()
    try:
        order = qury_3.get ()
        cursor.execute ("select * from 教师教授课程 where 姓名 = " + '\'' + order + '\'')
    except Exception as e:
        t21.destroy ()
        t24.destroy ()
        t28.destroy ()
        t29.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        return
    result = cursor.fetchall ()
    if len (result) == 0:
        t21.destroy ()
        t24.destroy ()
        t28.destroy ()
        t29.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message="There is no result you expect, please check the input!")
    flag = 1
    for i in result:
        tt.insert ('end', '%d' % flag + '. ' + str (i))
        tt.insert ('end', '\n')
        flag += 1
    t21.destroy ()
    t24.destroy ()
    t28.destroy ()


# 若输入为教师编号，将查询教师教授课程的sql语句传入数据库，并返回结果
def quick_qury22():
    t30 = tk.Toplevel ()
    t30.geometry ('600x300+480+280')
    tt = tk.Text (t30, height=20)
    tt.pack ()
    try:
        order = qury_4.get ()
        cursor.execute ("select * from 教师教授课程 where 教师编号=" + '\'' + order + '\'')
    except Exception as e:
        t21.destroy ()
        t24.destroy ()
        t28.destroy ()
        t30.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        return
    result = cursor.fetchall ()
    if len (result) == 0:
        t21.destroy ()
        t24.destroy ()
        t28.destroy ()
        t30.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message="There is no result you expect, please check the input!")
        return
    flag = 1
    for i in result:
        tt.insert ('end', '%d' % flag + '. ' + str (i))
        tt.insert ('end', '\n')
        flag += 1
    t21.destroy ()
    t24.destroy ()
    t28.destroy ()


# 查询学生成绩
def quick_qury3():
    global t31
    global qury_5
    global qury_6

    t31 = tk.Toplevel ()
    t31.title ("查询学生成绩（学号，姓名，课号，课程名，成绩）")
    t31.geometry ('300x240+460+260')
    frame = tk.Frame (t31)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    l = tk.Label (t31, text='通过学生姓名或学号进行查询', bg='yellow')
    l.pack (padx=20, pady=10)
    tk.Label (frame_l, text='姓名      ').pack (padx=20, pady=10)
    qury_5 = tk.Entry (frame_r, show=None)
    qury_5.pack (padx=20, pady=10)
    b = tk.Button (t31, text='输入姓名请点击这个按钮', width=30, height=1, command=quick_qury31)
    b.pack (padx=20, pady=10)
    tk.Label (frame_l, text='学号      ').pack (padx=20, pady=10)
    qury_6 = tk.Entry (frame_r, show=None)
    qury_6.pack (padx=20, pady=10)
    b = tk.Button (t31, text='输入学号请点击这个按钮', width=30, height=1, command=quick_qury32)
    b.pack (padx=20, pady=10)
    t31.mainloop ()


# 若输入为学生姓名，将查询学生成绩的sql语句传入数据库，并返回结果
def quick_qury31():
    t32 = tk.Toplevel ()
    t32.geometry ('600x300+480+280')
    tt = tk.Text (t32, height=20)
    tt.pack ()
    try:
        order = qury_5.get ()
        cursor.execute ("select * from 学生成绩（姓名） where 姓名 = " + '\'' + order + '\'')
    except Exception as e:
        t21.destroy ()
        t24.destroy ()
        t31.destroy ()
        t32.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        return
    result = cursor.fetchall ()
    if len (result) == 0:
        t21.destroy ()
        t24.destroy ()
        t31.destroy ()
        t32.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message="There is no result you expect, please check the input!")
    flag = 1
    for i in result:
        tt.insert ('end', '%d' % flag + '. ' + str (i))
        tt.insert ('end', '\n')
        flag += 1
    t21.destroy ()
    t24.destroy ()
    t31.destroy ()


# 若输入为学号，将查询学生成绩的sql语句传入数据库，并返回结果
def quick_qury32():
    t33 = tk.Toplevel ()
    t33.geometry ('600x300+480+280')
    tt = tk.Text (t33, height=20)
    tt.pack ()
    try:
        order = qury_6.get ()
        cursor.execute ("select * from 学生成绩（姓名） where 学号 = " + '\'' + order + '\'')
    except Exception as e:
        t21.destroy ()
        t24.destroy ()
        t31.destroy ()
        t33.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        return
    result = cursor.fetchall ()
    if len (result) == 0:
        t21.destroy ()
        t24.destroy ()
        t31.destroy ()
        t33.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message="There is no result you expect, please check the input!")
    flag = 1
    for i in result:
        tt.insert ('end', '%d' % flag + '. ' + str (i))
        tt.insert ('end', '\n')
        flag += 1
    t21.destroy ()
    t24.destroy ()
    t31.destroy ()


# 查询班级平均成绩
def quick_qury4():
    global t34
    global qury_7
    global qury_8
    global qury_9

    t34 = tk.Toplevel ()
    t34.title ("查询班级平均成绩")
    t34.geometry ('300x280+460+260')
    frame = tk.Frame (t34)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    l = tk.Label (t34, text='输入班级号和课号（或者课程名）进行查询', bg='yellow')
    l.pack (padx=20, pady=10)
    tk.Label (frame_l, text='班级号').pack (padx=20, pady=10)
    qury_7 = tk.Entry (frame_r, show=None)
    qury_7.pack (padx=20, pady=10)
    b = tk.Button (t34, text='输入（班级号，课号）请点击这个按钮', width=30, height=1, command=quick_qury41)
    b.pack (padx=20, pady=10)
    tk.Label (frame_l, text='课号').pack (padx=20, pady=10)
    qury_8 = tk.Entry (frame_r, show=None)
    qury_8.pack (padx=20, pady=10)
    tk.Label (frame_l, text='课程名').pack (padx=20, pady=10)
    qury_9 = tk.Entry (frame_r, show=None)
    qury_9.pack (padx=20, pady=10)
    b = tk.Button (t34, text='输入（班级号，课程名）请点击这个按钮', width=30, height=1, command=quick_qury42)
    b.pack (padx=20, pady=10)
    t34.mainloop ()


# 若输入为（班级号，课号），将查询班级课程平均成绩的sql语句传入数据库，并返回结果
def quick_qury41():
    t35 = tk.Toplevel ()
    t35.geometry ('600x300+480+280')
    tt = tk.Text (t35, height=20)
    tt.pack ()
    try:
        order1 = qury_7.get ()
        order2 = qury_8.get ()
        cursor.execute (
            "select 班级号,课号,课程名,平均成绩,不及格人数 from 班级成绩 NATURAL JOIN 课程 where (班级号,课号) = " + '(\'' + order1 + '\',\'' + order2 + '\')')
    except Exception as e:
        t21.destroy ()
        t24.destroy ()
        t34.destroy ()
        t35.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        return
    result = cursor.fetchall ()
    if len (result) == 0:
        t21.destroy ()
        t24.destroy ()
        t34.destroy ()
        t35.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message="There is no result you expect, please check the input!")
    flag = 1
    for i in result:
        tt.insert ('end', '%d' % flag + '. ' + str (i))
        tt.insert ('end', '\n')
        flag += 1
    t21.destroy ()
    t24.destroy ()
    t34.destroy ()


# 若输入为（班级号，课程名），将查询班级课程平均成绩的sql语句传入数据库，并返回结果
def quick_qury42():
    t36 = tk.Toplevel ()
    t36.geometry ('600x300+480+280')
    tt = tk.Text (t36, height=20)
    tt.pack ()
    try:
        order1 = qury_7.get ()
        order2 = qury_9.get ()
        cursor.execute (
            "select 班级号,课号,课程名,平均成绩,不及格人数 from 班级成绩 NATURAL JOIN 课程 where (班级号,课程名) = " + '(\'' + order1 + '\',\'' + order2 + '\')')
    except Exception as e:
        t21.destroy ()
        t24.destroy ()
        t34.destroy ()
        t36.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        return
    result = cursor.fetchall ()
    if len (result) == 0:
        t21.destroy ()
        t24.destroy ()
        t34.destroy ()
        t36.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message="There is no result you expect, please check the input!")
    flag = 1
    for i in result:
        tt.insert ('end', '%d' % flag + '. ' + str (i))
        tt.insert ('end', '\n')
        flag += 1
    t21.destroy ()
    t24.destroy ()
    t34.destroy ()


# 查询有n门及以上不及格课程的同学的平均成绩
def quick_qury5():
    global t37
    global qury_10
    t37 = tk.Toplevel ()
    t37.title ("查询有n门及以上不及格课程的同学的平均成绩")
    t37.geometry ('300x150+460+260')
    frame = tk.Frame (t37)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    tk.Label (frame_l, text='不及格课程数n').pack (padx=20, pady=10)
    qury_10 = tk.Entry (frame_r, show=None)
    qury_10.pack (padx=20, pady=10)
    b = tk.Button (t37, text='请点击这个按钮进行查询', width=30, height=1, command=quick_qury51)
    b.pack (padx=20, pady=10)
    t37.mainloop ()


# 将查询有n门及以上不及格课程的同学的平均成绩的sql语句传入数据库，并返回结果
def quick_qury51():
    t38 = tk.Toplevel ()
    t38.geometry ('600x300+480+280')
    tt = tk.Text (t38, height=20)
    tt.pack ()
    s = qury_10.get ()
    try:
        cursor.execute (
            "select 学生.学号,学生.姓名,avg(成绩) from 学生成绩 inner join 学生 where 学生.学号 = 学生成绩.学号 and "
            "学生成绩.学号 in (select 学号 from 学生成绩 where 成绩<60.0 Group by 学号 Having count(*)>" + str (int (s) - 1) + ") "
                                                                                                               "Group by 学号")
    except Exception as e:
        t21.destroy ()
        t24.destroy ()
        t37.destroy ()
        t38.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        return
    result = cursor.fetchall ()
    if len (result) == 0:
        t21.destroy ()
        t24.destroy ()
        t37.destroy ()
        t38.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message="There is no result you expect, please check the input!")
    flag = 1
    for i in result:
        tt.insert ('end', '%d' % flag + '. ' + str (i))
        tt.insert ('end', '\n')
        flag += 1
    t21.destroy ()
    t24.destroy ()
    t37.destroy ()


# 查询某院系的全部学生信息
def quick_qury6():
    global t39
    global qury_11
    global qury_12
    t39 = tk.Toplevel ()
    t39.title ("查询某院系的全部学生信息")
    t39.geometry ('300x240+460+260')
    frame = tk.Frame (t39)
    frame.pack ()
    frame_l = tk.Frame (frame)
    frame_r = tk.Frame (frame)
    frame_l.pack (side='left')
    frame_r.pack (side='right')
    l = tk.Label (t39, text='通过系号或系名进行查询', bg='yellow')
    l.pack (padx=20, pady=10)
    tk.Label (frame_l, text='系号      ').pack (padx=20, pady=10)
    qury_11 = tk.Entry (frame_r, show=None)
    qury_11.pack (padx=20, pady=10)
    b = tk.Button (t39, text='输入系号请点击这个按钮', width=30, height=1, command=quick_qury61)
    b.pack (padx=20, pady=10)
    tk.Label (frame_l, text='系名     ').pack (padx=20, pady=10)
    qury_12 = tk.Entry (frame_r, show=None)
    qury_12.pack (padx=20, pady=10)
    b = tk.Button (t39, text='输入系名请点击这个按钮', width=30, height=1, command=quick_qury62)
    b.pack (padx=20, pady=10)
    t39.mainloop ()


# 若输入为系号，将查询某院系全部学生信息的sql语句传入数据库，并返回结果
def quick_qury61():
    t40 = tk.Toplevel ()
    t40.geometry ('600x300+480+280')
    tt = tk.Text (t40, height=20)
    tt.pack ()
    a0 = qury_11.get ()
    try:
        cursor.execute ("select * from 学生 where 系号=" + a0)
    except Exception as e:
        t21.destroy ()
        t24.destroy ()
        t39.destroy ()
        t40.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        return
    result = cursor.fetchall ()
    if len (result) == 0:
        t21.destroy ()
        t24.destroy ()
        t39.destroy ()
        t40.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message="There is no result you expect, please check the input!")
    flag = 1
    for i in result:
        tt.insert ('end', '%d' % flag + '. ' + str (i))
        tt.insert ('end', '\n')
        flag += 1
    t21.destroy ()
    t24.destroy ()
    t39.destroy ()


# 若输入为系名，将查询某院系全部学生信息的sql语句传入数据库，并返回结果
def quick_qury62():
    t41 = tk.Toplevel ()
    t41.geometry ('600x300+480+280')
    tt = tk.Text (t41, height=20)
    tt.pack ()
    a0 = qury_12.get ()
    try:
        cursor.execute ("select 学生.* from 学生 inner join 院系 where 学生.系号 = 院系.系号 and 系名 = " + "\"" + a0 + "\"")
    except Exception as e:
        t21.destroy ()
        t24.destroy ()
        t39.destroy ()
        t41.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message=e)
        return
    result = cursor.fetchall ()
    if len (result) == 0:
        t21.destroy ()
        t24.destroy ()
        t39.destroy ()
        t41.destroy ()
        tk.messagebox.showinfo (title='温馨提醒', message="There is no result you expect, please check the input!")
    flag = 1
    for i in result:
        tt.insert ('end', '%d' % flag + '. ' + str (i))
        tt.insert ('end', '\n')
        flag += 1
    t21.destroy ()
    t24.destroy ()
    t39.destroy ()


# 退出程序
def quit():
    t.destroy ()


# 每次更改数据后，更新班级平均成绩
def update_classgrades():
    list_cc = []
    cursor.execute ("select * from 班级成绩")
    result = cursor.fetchall ()
    for i in result:
        for key in i.keys ():
            if key == '班级号':
                temp1 = i.get (key)
            if key == '课号':
                temp2 = i.get (key)
        list_cc.append ((temp1, temp2))
    cursor.execute ("select 班级号,课号,avg(成绩) from 学生成绩（姓名） group by 班级号,课号")
    result1 = cursor.fetchall ()
    list_sum = {}
    for i in list_cc:
        cursor.execute ("select * from 学生成绩（姓名） where 班级号 = " + i[0] + " and 课号 = " + i[1] + " and 成绩<60")
        result2 = cursor.fetchall ()
        list_sum[i] = len (result2)
    for i in list_cc:
        for r in result1:
            if i[0] == r.get ("班级号") and i[1] == r.get ("课号"):
                temp3 = r.get ("avg(成绩)")
        cursor.execute (
            "update 班级成绩 set 不及格人数 = " + str (list_sum[i]) + ", 平均成绩=" + str (temp3) + " where 班级号 =" + i[
                0] + " and 课号 = " + i[
                1])
        db.commit ()


# 主菜单
def mennu():
    global t
    t = tk.Tk ()
    t.title ('微型教务系统')
    t.geometry ('280x300+400+200')
    tk.Label (text='功能菜单', bg='yellow').pack ()
    b = tk.Button (t, text='增加记录', width=10, height=1, command=add, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t, text='删除记录', width=10, height=1, command=delete, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t, text='修改记录', width=10, height=1, command=modify, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t, text='查询记录', width=10, height=1, command=qury, bg='yellow')
    b.pack (padx=20, pady=10)
    b = tk.Button (t, text='退出', width=10, height=1, command=quit, bg='yellow')
    b.pack (padx=20, pady=10)
    t.mainloop ()


mennu ()

