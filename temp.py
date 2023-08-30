# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import re
dic={}
namer=[]
linker=[]
#query=input("输入页数")
for i in range(2,190,1):
    
    url=f"https://www.99tv105.xyz/Html/60/index-{i}.html"
    head={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36"
        }
    resp=requests.get(url,headers=head)
    resp.close()
    resp.encoding="utf-8"#指定字符集
    #print(resp.text)
    obj1=re.compile(r"笔笔存笔笔送.*?<div>(?P<ul>.*?)<strong>",re.S)
    result1=obj1.finditer(resp.text)
    #print(result)
    for i in result1:
        ul=i.group("ul")
        #print(ul)
    list1=[]
    
    obj2=re.compile(r"<a href=(?P<href>.*?)class",re.S)
    result2=obj2.finditer(ul)
    for it in result2:
        href=it.group('href')
        list1.append(href)
        #print(href)
    list1.pop(4)
    #print(list1)
    list3=[]
    for i in list1:
        list2=list(i)
        list2.pop(0)
        list2.pop(-1)
        list2.pop(-1)
        #print(list2)
        i="".join(list2)
        i="https://www.99tv105.xyz/"+i
        #print(i)
        list3.append(i)
    #print(list3)
        
        
    for i in list3:
        child_resp=requests.get(i,headers=head)
        child_resp.encoding="utf-8"
        #print(child_resp.text)
        obj4=re.compile(r"<h4>(?P<name>.*?)</h4>",re.S)
        result4=obj4.finditer(child_resp.text)
        for i in result4:
            name=i.group("name")
        print(name)
        namer.append(name)
        obj3=re.compile(r"在线播放：</span>.*?<ul>.*?<a .*?href='(?P<link>.*?)'>线路一",re.S)
        result3=obj3.finditer(child_resp.text)
        for i in result3:
            link=i.group("link")
            #print(link)
        link="https://www.99tv773.xyz/"+link
        print(link)
        linker.append(link)
print(namer)
print(linker)


import xlwt

book = xlwt.Workbook()
sheet1 = book.add_sheet('国产')
style = xlwt.XFStyle()
alignment = xlwt.Alignment() # 对齐方式：水平垂直居中
alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平居中
alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直居中
style.alignment = alignment
font = xlwt.Font()  # 字体加粗
font.name = '微软雅黑'
font.bold = True
sheet1.col(0).width = 256 *100  # 设置第1列的宽度为20个字符宽度
sheet1.col(1).width = 256 *100  # 设置第1列的宽度为20个字符宽度
tall_style = xlwt.easyxf('font:height 720;') # 36pt,类型小初的字号
sheet1.row(0).set_style(tall_style)  # 设置第1行的行高是36*20


for i in namer:
    sheet1.write(namer.index(i)+1,0,i)
for i in linker:
    sheet1.write(linker.index(i)+1,1,i)
book.save('tww1.xls')




    






































#print(resp.content.decode("UTF-8"))#字节转化为str

#with open("pais.html",mode="w",encoding="UTF-8") as f:
#    f.write(resp.text)
                               