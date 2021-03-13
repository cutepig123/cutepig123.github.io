```python
import os, sys, json
import sqlite3
import pprint,time, datetime

def flattenX(candidates):
    ret = []
    for candidate in candidates:
        if 'children' in candidate:
            ret.extend(flattenX(candidate['children']))
        else:
            ret.append(candidate)
    return ret

def date_from_webkit(webkit_timestamp):
    epoch_start = datetime.datetime(1601,1,1)
    delta = datetime.timedelta(microseconds=int(webkit_timestamp))
    return (epoch_start + delta) # py3 requires () for print

def listX(data):
    candidates = []
    for item in data['roots']:
        candidates.append(data['roots'][item])
        #children = data['roots'][item]['children']
    children = flattenX(candidates)
    print (len(children))
    children = sorted(children, key=lambda x: x['date_added'], reverse=True)
    #pprint.pprint(children[:10])
    #print(json.dumps(children[:10], indent=4, sort_keys=True))
    for i in children[:50]:
        #t = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(int(i['date_added'])/1000000))
        t = date_from_webkit(int(i['date_added']))
        print(i['name'], i['url'], t)

def chrome():
    paths = [
        os.path.expanduser("~/.config/google-chrome/Default/Bookmarks"),
        os.path.expanduser(
            "~/Library/Application Support/Google/Chrome/Default/Bookmarks"),
        os.path.expanduser(
            "~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Bookmarks")
    ]
    path = ""
    if "linux" in sys.platform.lower():
        path = "~/.config/google-chrome/Default/Bookmarks"
    if "darwin" in sys.platform.lower():
        path = "~/Library/Application Support/Google/Chrome/Default/Bookmarks"
    if "win32" in sys.platform.lower():
        path = "~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Bookmarks"
    path = os.path.expanduser(path)

    folders = []
    urls = []

    for f in paths:
        if os.path.exists(f):
            print(f)
            data = json.loads(open(f, encoding='utf-8').read())
            #print(json.dumps(data, indent=4, sort_keys=True))
            listX(data)

# execute a query on sqlite cursor
def execute_query(cursor, query):
    try:
        cursor.execute(query)
    except Exception as error:
        print(str(error) + "\n " + query)
# get bookmarks from firefox sqlite database file and print all
def get_bookmarks(cursor):
    bookmarks_query = """select url, moz_places.title, rev_host, frecency,
    last_visit_date from moz_places  join  \
    moz_bookmarks on moz_bookmarks.fk=moz_places.id where visit_count>0
    and moz_places.url  like 'http%'
    order by dateAdded desc;"""

    bookmarks_query = """select DISTINCT url, moz_places.title, rev_host, frecency,
    last_visit_date, dateAdded from moz_places  join  
    moz_bookmarks on moz_bookmarks.fk=moz_places.id 
	where visit_count>0
    order by dateAdded desc limit 50;"""
    execute_query(cursor, bookmarks_query)
    for row in cursor:
        [link, title, rev_host, frecency, last_visit_date, dateAdded] = row
        #link = row[0]
        #title = row[1]
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(dateAdded/1000000))
        print(title, link, rev_host, frecency, last_visit_date, t )

def firefox():
    path = "~\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles"
    bookmarks_path = os.path.expanduser(path)

    # get firefox profile
    profiles = []
    for i in os.listdir(bookmarks_path):
        sqlite_path = '%s\\%s\\places.sqlite'%(bookmarks_path, i)
        if os.path.isfile(sqlite_path):
            profiles.append(sqlite_path)
        
        firefox_connection = sqlite3.connect(sqlite_path)
        cursor = firefox_connection.cursor()
        get_bookmarks(cursor)
        cursor.close()

firefox()
print('----------------------------')
chrome()


```