# extract backuped cnblogs file to this folder

import os

class TextFinder:
    def __init__(self, text):
        self.p = 0
        self.text = text

    def find_between(self, head, tail):
        p1 = text.find(head, self.p)
        if p1>=0:
            p1 += len(head)
            p2 = text.find(tail, p1)
            if p2>0:
                self.p = p2 + len(tail)
                return text[p1:p2]
        return None

text = open('g:\\CNBlogs_BlogBackup_131_200706_202103.xml','r',encoding='utf-8').read()
finder  = TextFinder(text)

def write(title, description):
    f = open(title, 'w',encoding='utf-8')
    f.write(description)
    f.close()

def find_date(link):
    p = link.find('archive')
    if p>=0:
        p += len('archive/')
        date = link[p:(p+len('2021/02/21'))]
        date = date.replace('/','-')
        return date
    return None

def find_all_cnt(text, key):
    p=0
    n=0
    while True:
        p = text.find(key, p)
        if p>=0:
            n = n+1
            p += len(key)
        else:
            return n

def make_valid_fname(fname):
    keys='/\\*"\':?|'
    for k in keys:
        fname = fname.replace(k,'')
    return fname

while True:
    title = finder.find_between('<item><title>', '</title>')
    if title is None: break

    link = finder.find_between('<link>', '</link>')
    if link is None: break

    date = find_date(link)
    assert date is not None

    description = finder.find_between('<description><![CDATA[', ']]></description>')
    if description is None: break

    n = find_all_cnt(description, '</')
    ext = 'md'
    if n>5: ext = '.html'

    title2 = '%s-%s.%s'%(date, title, ext)
    title2 = make_valid_fname(title2)
    
    if not os.path.isfile(title2):
        print(title2)
        write(title2, description)