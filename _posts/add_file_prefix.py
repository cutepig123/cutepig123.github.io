import os, sys, re, time

def MySystem(cmd):
    print(cmd)
    os.system(cmd)

def MyRename(src, des):
    MySystem('rename "%s" "%s"'%(src, des))

pattern = re.compile("^\d\d\d\d-.*")
for fname in os.listdir('.'):
    if os.path.isfile(fname):
        if not pattern.match(fname) and fname.lower().endswith('.md'):
            print(fname)
            
            mtimestr = time.strftime('%Y-%m-%d-', time.gmtime(os.path.getmtime(fname)))
            des_fname = mtimestr + fname
            #print(des_fname)
            MyRename(fname, des_fname)