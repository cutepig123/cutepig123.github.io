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

def add_prefix():
    pattern = re.compile("^\d\d\d\d-.*")

    def callback(root_path, sub_path, fname):
        fpath = os.path.join(root_path, sub_path, fname)
        if not os.path.isfile(fpath) or not fpath.lower().endswith('.md'): return
        if not pattern.match(fname):
            print(fname)
        if not pattern.match(fname):
            print(fname)
            
            mtimestr = time.strftime('%Y-%m-%d-', time.gmtime(os.path.getmtime(fpath)))
            des_fname = mtimestr + fname
            des_fpath = os.path.join(root_path, sub_path, des_fname)
            #print(des_fname)
            MyRename(fpath, des_fpath)
        elif False:
            mtimestr = time.strftime('%Y-%m-%d-', time.gmtime(os.path.getmtime(fpath)))
            fname_no_prefix = fname[len('2020-01-01-'):]
            des_fname = mtimestr + fname_no_prefix
            des_fpath = os.path.join(root_path, sub_path, des_fname)
            #print(des_fname)
            #MyRename(fname, des_fname)
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

add_prefix()
add_categories()
#dir_recur('.', '',lambda x,y:print(x,y))