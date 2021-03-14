import os, sys, re, time

def MySystem(cmd):
    print(cmd)
    os.system(cmd)

def MyRename(src, des):
    MySystem('rename "%s" "%s"'%(src, des))

def add_prefix():
    pattern = re.compile("^\d\d\d\d-.*")
    for fname in os.listdir('.'):
        if not os.path.isfile(fname) or not fname.lower().endswith('.md'): continue
        if not pattern.match(fname):
            print(fname)
            
            mtimestr = time.strftime('%Y-%m-%d-', time.gmtime(os.path.getmtime(fname)))
            des_fname = mtimestr + fname
            #print(des_fname)
            MyRename(fname, des_fname)
        elif False:
            mtimestr = time.strftime('%Y-%m-%d-', time.gmtime(os.path.getmtime(fname)))
            fname_no_prefix = fname[len('2020-01-01-'):]
            des_fname = mtimestr + fname_no_prefix
            #print(des_fname)
            #MyRename(fname, des_fname)
            MyRename(fname, des_fname)

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

def add_categories():
    for folder in os.listdir('.'):
        if not os.path.isdir(folder): continue
        for fname in os.listdir(folder):
            fpath = '%s\\%s'%(folder, fname)
            if not os.path.isfile(fpath) or not fname.lower().endswith('.md'): continue
            print(fpath)
            lines = open(fpath, 'r', encoding='utf-8').readlines()
            [head, data] = split_header_content(lines)
            print(head)
            if not 'categories' in head:
                head['categories'] = folder
            elif head['categories'].find(folder)<0:
                head['categories'] += ' ' + folder
            fw = open(fpath, 'w', encoding='utf-8')

            fw.write('---\n')
            for k in head:
                fw.write('%s: %s\n'%(k, head[k]))
            fw.write('---\n')

            fw.writelines(data)

            fw.close()
add_prefix()
add_categories()
