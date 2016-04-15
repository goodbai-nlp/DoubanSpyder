# _*_ coding:utf-8 _*_ 

import re
import os
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def run(path):
    name=[]
    path =[]
    #print rootdir# 指明被遍历的文件夹
    for parent,dirnames,filenames in os.walk(path):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:                        #输出文件信息
            name.append( filename)
            path.append(os.path.join(parent,filename)) #输出文件路径信息
    for i in range(len(path)):
        fg = codecs.open(path[i])
        strs=fg.read()
        f = codecs.open('D:\Douban\Douban\spider_products\End\end.txt','a',encoding='utf-8')
        
        f.write((name[0][:-4]+':').encode("utf-8"))
        f.write("\n")
        f.write(strs.encode("utf-8"))
        f.write("\n")
        f.close()
