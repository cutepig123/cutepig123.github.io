# Desc
# 遞歸目錄下的所有文件，
# 如果沒有YYYY-MM-DD-前綴，就根據文件的時間自動加上
# 如果在子目錄下，自動把目錄名加到categories裏面
# 如果是txt文件，生成一個對應的md文件

import os, sys, re, time

def MySystem(cmd):
    print(cmd)
    os.system(cmd)

def MyRename(src, des):
    MySystem('move "%s" "%s"'%(src, des))

def dir_recur(root_path, sub_path, callback):
    full_path = os.path.join(root_path, sub_path)
    for item in os.listdir(full_path):
        if len(item)==item.count('.'): continue
        full_path2 = os.path.join(full_path, item)
        if os.path.isdir(full_path2):
            dir_recur(root_path, os.path.join(sub_path, item), callback)
        else:
            callback(root_path, sub_path, item)

class PrefixChecker:
    def __init__(self):
        self.pattern = re.compile("^\d\d\d\d-.*")
    def check(self, dir_path, file_name):
        if not self.pattern.match(file_name):
            fpath = os.path.join(dir_path, file_name)
            mtimestr = time.strftime('%Y-%m-%d-', time.gmtime(os.path.getmtime(fpath)))
            des_fname = mtimestr + file_name
            des_fpath = os.path.join(dir_path, des_fname)
            return [True, des_fpath]
        else:
            fpath = os.path.join(dir_path, file_name)
            return [False, fpath]

# 如果沒有YYYY-MM-DD-前綴，就根據文件的時間自動加上
def add_prefix():
    prefixChecker = PrefixChecker()

    def callback(root_path, sub_path, fname):
        fpath = os.path.join(root_path, sub_path, fname)
        if not os.path.isfile(fpath) or not fpath.lower().endswith('.md'): return
        
        [is_rename_needed, des_fpath] = prefixChecker.check(os.path.join(root_path, sub_path), fname)
        print(des_fpath)
        if is_rename_needed:
            print(fname)
           
            MyRename(fpath, des_fpath)
            
    dir_recur('.', '', callback)
    

def split_header_content(lines):
    state = 0   #Find start of head
        #1: find end of head
        #2: content
    head={}
    data=[]
    for line in lines:
        stripedline = line.strip()
        if state==0:
            if stripedline=='---': 
                state = 1
            else:
                state = 2
                data.append(line)
        elif state == 1:
            if stripedline=='---': 
                state = 2
            else:
                kv = stripedline.split(':')
                assert len(kv)==2
                head[kv[0].strip()] = kv[1].strip()
        else:
            data.append(line)
    return [head, data]

def add_categorie_to_file(fpath, categories):
    lines = open(fpath, 'r', encoding='utf-8').readlines()
    [head, data] = split_header_content(lines)
    print(head)
    
    categories_str = ' '.join(categories)
    if len(categories_str.strip())==0: return

    if not 'categories' in head:
        head['categories'] = categories_str
    elif head['categories'].find(categories_str)<0:
        head['categories'] += categories_str
    else:
        return

    fw = open(fpath, 'w', encoding='utf-8')

    fw.write('---\n')
    for k in head:
        fw.write('%s: %s\n'%(k, head[k]))
    fw.write('---\n')

    fw.writelines(data)

    fw.close()

def add_categories():
    def callback(root_path, sub_path, item):
        fpath = os.path.join(root_path, sub_path, item)
        
        if not os.path.isfile(fpath) or not fpath.lower().endswith('.md'): return
        
        categories = sub_path.split('\\')
        categories = [x for x in categories if len(x)>0]
        print(fpath, categories)
        add_categorie_to_file(fpath, categories)

    dir_recur('.', '', callback)

def convert_txt_to_markdown():
    prefixChecker = PrefixChecker()

    def ConvertToMD(src, des):
        df = open(des,'w')
        for line in open(src,'r').readlines():
            df.write(line)
            df.write('\n')
        df.close()

    def callback(root_path, sub_path, item):
        fpath = os.path.join(root_path, sub_path, item)
        
        if not os.path.isfile(fpath) or not fpath.lower().endswith('.txt'): return
        
        [is_rename_needed, des_fpath] = prefixChecker.check(os.path.join(root_path, sub_path), item)
        if is_rename_needed and not os.path.isfile(des_fpath):
            des_fpath = des_fpath[:-3] + 'md'
            print('convert to ', des_fpath)
            ConvertToMD(fpath, des_fpath)

    dir_recur('.', '', callback)

# 如果沒有YYYY-MM-DD-前綴，就根據文件的時間自動加上
#add_prefix()
# 如果在子目錄下，自動把目錄名加到categories裏面
#add_categories()
#dir_recur('.', '',lambda x,y:print(x,y))
# 如果是txt文件，生成一個對應的md文件
convert_txt_to_markdown()