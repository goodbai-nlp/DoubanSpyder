# _*_ coding:utf-8 _*_ 

import os
import os.path
import re
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf8')
endpath = os.path.realpath(__file__)[:-8]+'/spider_products'
if not os.path.isdir(endpath+'/End'):
    os.mkdir(endpath+'/End')
rootdir = os.path.realpath(__file__)[:-8]+'/spider_products'+u'/电影'
name=[]
path =[]
dirn=[]
#print rootdir# 指明被遍历的文件夹
for parent,dirnames,filenames in os.walk(rootdir): #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for dirname in  dirnames:
        dirn.append(dirname)
    for filename in filenames:
        name.append( filename)
        path.append(os.path.join(parent,filename)) #输出文件路径信息
for i in range(len(path)):
    fg = codecs.open(path[i])
    strs=fg.read()
    f = codecs.open(endpath+'/End/'+dirn[i/2]+'.txt','a',encoding='utf-8')
    f.write((name[i][:-4]+':').encode("utf-8"))
    f.write("\n")
    f.write(strs)
    f.write("\n")
    f.close()
