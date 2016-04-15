# _*_ coding:utf-8 _*_ 

import re
import os
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Write():
    def __init__(self,item,path):
        self.item=item
        self.path=path
        self.key=["电影效果","电影剧情","演员演技"]
        self.value=[0.05,0.06,0.05]
        self.detailkey=["特效,效果,特写,镜头,画面,渲染,视觉,感官,绚丽,3D,震撼","开场,故事,接下来,编剧,剧情,题材,讲述,告诉,气氛,渲染,故事线,视角,主题,理解,撼人心魄,感染观众,结尾,结局,最后,线索,叙事,节奏","主角,一号,二号,表情,动作,感情,性格,戏份"]
    def run(self):
        tmp=[]
        tmppath =self.path+u'/电影'
        if not os.path.isdir(tmppath):
            os.mkdir(tmppath)

        tmppath = tmppath +'/%s'% self.item['movie_name']
        if not os.path.isdir(tmppath):
            os.mkdir(tmppath)
        for k in range(len(self.detailkey)):
            tmp.append(tmppath+'/%s.txt'%self.key[k].decode('utf-8'))
        for string in self.item['comment_detail']:
            for i in range(len(self.detailkey)):
                s=re.split(',',self.detailkey[i])
                n=0
                str=""
                for j in range(len(s)):
                    n=n+string.count(s[j])
                    str=str+s[j]
                f = codecs.open(tmp[i],'a',encoding='utf-8')
                if n*len(str)/(float(len(self.detailkey))*len(string))>self.value[i] and len(string)>50 :
                    f.write((string+'('+self.item['movie_name']+')').encode("utf-8"))
                    f.write("\n")
                    f.write("\n")
                f.close()
