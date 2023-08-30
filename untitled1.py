# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 20:11:59 2023

@author: Vapor
"""

import xlwt

book = xlwt.Workbook()
sheet = book.add_sheet('国产')
style = xlwt.XFStyle()
alignment = xlwt.Alignment() # 对齐方式：水平垂直居中
alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平居中
alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直居中
style.alignment = alignment
font = xlwt.Font()  # 字体加粗
font.name = '微软雅黑'
font.bold = True
col_names = ['剧名', '链接']  # 列名称
for index, name in enumerate(col_names):
    sheet.write(0, index, name)
sheet.col(0).width = 256 *100  # 设置第1列的宽度为20个字符宽度
sheet.col(1).width = 256 *100  # 设置第1列的宽度为20个字符宽度
tall_style = xlwt.easyxf('font:height 720;') # 36pt,类型小初的字号
sheet.row(0).set_style(tall_style)  # 设置第1行的行高是36*20
sheet = book.add_sheet('动漫')
style = xlwt.XFStyle()
alignment = xlwt.Alignment() # 对齐方式：水平垂直居中
alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平居中
alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直居中
style.alignment = alignment
font = xlwt.Font()  # 字体加粗
font.name = '微软雅黑'
font.bold = True
col_names = ['剧名', '链接']  # 列名称
for index, name in enumerate(col_names):
    sheet.write(0, index, name)
sheet.col(0).width = 256 *100  # 设置第1列的宽度为20个字符宽度
sheet.col(1).width = 256 *100  # 设置第1列的宽度为20个字符宽度
tall_style = xlwt.easyxf('font:height 720;') # 36pt,类型小初的字号
sheet.row(0).set_style(tall_style)  # 设置第1行的行高是36*20
sheet = book.add_sheet('欧美')
style = xlwt.XFStyle()
alignment = xlwt.Alignment() # 对齐方式：水平垂直居中
alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平居中
alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直居中
style.alignment = alignment
font = xlwt.Font()  # 字体加粗
font.name = '微软雅黑'
font.bold = True
col_names = ['剧名', '链接']  # 列名称
for index, name in enumerate(col_names):
    sheet.write(0, index, name)
sheet.col(0).width = 256 *100  # 设置第1列的宽度为20个字符宽度
sheet.col(1).width = 256 *100  # 设置第1列的宽度为20个字符宽度
tall_style = xlwt.easyxf('font:height 720;') # 36pt,类型小初的字号
sheet.row(0).set_style(tall_style)  # 设置第1行的行高是36*20
book.save('t1.xls')

