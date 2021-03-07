import os, sys, re, time

def MySystem(cmd):
    print(cmd)
    os.system(cmd)

def MyRename(src, des):
    MySystem('rename "%s" "%s"'%(src, des))

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
        