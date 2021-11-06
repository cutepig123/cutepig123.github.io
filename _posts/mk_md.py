from datetime import datetime
import sys, os
import argparse

parser = argparse.ArgumentParser(description='Create a file')
parser.add_argument('fname', metavar='N', 
                    help='file name')
parser.add_argument('-d', dest='folder', help='folder')

args = parser.parse_args()
file = '%s-%s.md'%(datetime.today().strftime('%Y-%m-%d'), args.fname)
print('create file', file)    

if args.folder:
    file = '%s\\%s'%(args.folder, file)
if os.path.isfile(file):
    print('exist!')
else:    
    fp = open(file,'w')
    fp.close()
    print('created file', file)

os.system('"%s"'%file)