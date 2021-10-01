---
categories: python
---
# Summary

| 方法                     | 安全程度 | 破解方案             |
| ------------------------ | -------- | -------------------- |
| 編譯為pyc                | 低       | uncompyle6，成功率高 |
| 使用pyminifier作代碼混淆 | 中高     | 無                   |
|                          |          |                      |





# Python security –Compile to .pyc files



## Requirements

Test decompiler performance



## python-uncompyle6

link: https://github.com/rocky/python-uncompyle6/



Test1.py

```python
C:\Python36\Python36>type test1.py
def f(a,b,c):
        print(a,b,c)

f(b=1,a=2,c=3)
```



Generate .pyc file

```bash

C:\Python36\Python36>python -m test1
2 1 3

C:\Python36\Python36>dir __pycache__
 Volume in drive C has no label.
 Volume Serial Number is 5216-2CC6

 Directory of C:\Python36\Python36\__pycache__

10/08/2019  01:32 PM    <DIR>          .
10/08/2019  01:32 PM    <DIR>          ..
10/08/2019  01:32 PM               269 test1.cpython-36.pyc
               1 File(s)            269 bytes
               2 Dir(s)   5,840,228,352 bytes free
```



uncompile

```python
C:\Python36\Python36>Scripts\uncompyle6.exe C:\Python36\Python36\__pycache__\test1.cpython-36.pyc
# uncompyle6 version 3.4.0
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSCv.1900 64 bit (AMD64)]
# Embedded file name: C:\Python36\Python36\test1.py
# Compiled at: 2019-10-03 18:52:50
# Size of source mod 2**32: 48 bytes


def f(a, b, c):
    print(a, b, c)


f(b=1, a=2, c=3)
# okay decompiling C:\Python36\Python36\__pycache__\test1.cpython-36.pyc
```

# Python security – obsufsion

## Requirements

Test obsufsion performance

## pyminifier

link: https://liftoff.github.io/pyminifier/

Function names are renamed, variable names keep

```python
C:\Python36\Python36>type test1.py
def MyPrint(axxx,b,c):
 a = axxx
 print(a,b,c)

MyPrint(b=1,axxx=2,c=3)

def MyPrint2(axxx,b,c):
 a = axxx
 print(a,b,c)

MyPrint2(3,2,1)

C:\Python36\Python36>python -m pyminifier -O test1.py
def b(axxx,b,c):
 a=axxx
 print(a,b,c)
b(b=1,axxx=2,c=3)
def C(axxx,b,c):
 a=axxx
 print(a,b,c)
C(3,2,1)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
```



Q: Why parameter name is not renamed?

https://github.com/liftoff/pyminifier/issues/98



The tool is not stable. sometimes may fail. eg

```python
C:\Python36\Python36>type test1.py
def MyPrint(axxx,b,c):
        a = axxx
        print(a,b,c)

MyPrint(b=1,axxx=2,c=3)

C:\Python36\Python36>python -m pyminifier -O test1.py

Traceback (most recent call last):
  File "C:\Python36\Python36\lib\runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "C:\Python36\Python36\lib\runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "C:\Python36\Python36\lib\site-packages\pyminifier\__main__.py", line 175, in <module>
    main()
  File "C:\Python36\Python36\lib\site-packages\pyminifier\__main__.py", line 171, in main
    pyminify(options, files)
  File "C:\Python36\Python36\lib\site-packages\pyminifier\__init__.py", line 284, in pyminify
    source = minification.minify(tokens, options)
  File "C:\Python36\Python36\lib\site-packages\pyminifier\minification.py", line 413, in minify
    result = join_multiline_pairs(result)
  File "C:\Python36\Python36\lib\site-packages\pyminifier\minification.py", line 265, in join_multiline_pairs
    for tok in tokenize.generate_tokens(io_obj.readline):
  File "C:\Python36\Python36\lib\tokenize.py", line 578, in _tokenize
    ("<tokenize>", lnum, pos, line))
  File "<tokenize>", line 3
    print(a,b,c)
    ^
IndentationError: unindent does not match any outer indentation level
```



# TODO

- Consult SW group (wait Bo)
- study ipepycrypter
- study sourcedefender
- study py2exe
- study pyinstaller