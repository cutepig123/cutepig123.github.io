---
categories: python
---
# Summary

| 方法                                                  | 安全程度 | 破解方案                       | Comment                        |
| ----------------------------------------------------- | -------- | ------------------------------ | ------------------------------ |
| 編譯為pyc                                             | 低       | uncompyle6，成功率高           |                                |
| 使用pyminifier作代碼混淆                              | 中高     | No tools, manual code analysis | 工具不穩定                     |
| 使用sourcedefender加密代碼with AES 256-bit Encryption | 高(?)    | Unknown                        | 商業軟件，收費<br />Test fails |
| [pyconcrete](https://github.com/Falldog/pyconcrete)   | 高(?)    | Unknown                        | Test passes                    |



# Proposal

- Use pyminifier + [pyconcrete](https://github.com/Falldog/pyconcrete)
- Implement a standalone tool to one click encrypt all files in specified folder



# TODO

- [x] Python security –Compile to .pyc files
- [x] Python security – obsufsion pyminifier
- [ ] Consult SW group (wait Bo)
- [x] study sourcedefender (fails)
- [x] study pyconcrete
- [ ] ~~study py2exe~~
- [ ] ~~study pyinstaller~~

# [pyconcrete](https://github.com/Falldog/pyconcrete)

Open source

## Install fails (VS2010)

```bash
C:\Python36\Python36>python -m pip install pyconcrete --install-option="--passph
rase=test"
C:\Python36\Python36\lib\site-packages\pip\_internal\commands\install.py:243: Us
erWarning: Disabling all use of wheels due to the use of --build-options / --glo
bal-options / --install-options.
  cmdoptions.check_install_build_global(options)
Collecting pyconcrete
  Using cached https://files.pythonhosted.org/packages/a5/be/2bf8d1edc9a0688d5f9
be89495d263566f30b50b368256fc9602685793cd/pyconcrete-0.12.1.tar.gz
Skipping bdist_wheel for pyconcrete, due to binaries being disabled for it.
Installing collected packages: pyconcrete
  Running setup.py install for pyconcrete ... error
    ERROR: Command errored out with exit status 1:
     command: 'C:\Python36\Python36\python.exe' -u -c 'import sys, setuptools, t
okenize; sys.argv[0] = '"'"'C:\\Users\\aeejshe\\AppData\\Local\\Temp\\pip-instal
l-4zoeaqy_\\pyconcrete\\setup.py'"'"'; __file__='"'"'C:\\Users\\aeejshe\\AppData
\\Local\\Temp\\pip-install-4zoeaqy_\\pyconcrete\\setup.py'"'"';f=getattr(tokeniz
e, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n
'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record
 'C:\Users\aeejshe\AppData\Local\Temp\pip-record-_o8exw_s\install-record.txt' --
single-version-externally-managed --compile --passphrase=test
         cwd: C:\Users\aeejshe\AppData\Local\Temp\pip-install-4zoeaqy_\pyconcret
e\
    Complete output (6 lines):
    usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
       or: setup.py --help [cmd1 cmd2 ...]
       or: setup.py --help-commands
       or: setup.py cmd --help

    error: option --single-version-externally-managed not recognized
    ----------------------------------------
ERROR: Command errored out with exit status 1: 'C:\Python36\Python36\python.exe'
 -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\aeejshe\
\AppData\\Local\\Temp\\pip-install-4zoeaqy_\\pyconcrete\\setup.py'"'"'; __file__
='"'"'C:\\Users\\aeejshe\\AppData\\Local\\Temp\\pip-install-4zoeaqy_\\pyconcrete
\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read(
).replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '
"'"'exec'"'"'))' install --record 'C:\Users\aeejshe\AppData\Local\Temp\pip-recor
d-_o8exw_s\install-record.txt' --single-version-externally-managed --compile --p
assphrase=test Check the logs for full command output.
```



download source code & install, fails

```bash
C:\Users\aeejshe\Downloads\pyconcrete-0.12.1\pyconcrete-0.12.1>\Python36\Python3
6\python setup.py install
running install
running build
running build_py
running build_ext
building 'pyconcrete._pyconcrete' extension
error: Unable to find vcvarsall.bat
```



searching from web & try, fails

```bash
C:\Users\aeejshe\Downloads\pyconcrete-0.12.1\pyconcrete-0.12.1>set DISTUTILS_USE
_SDK=1

C:\Users\aeejshe\Downloads\pyconcrete-0.12.1\pyconcrete-0.12.1>\Python36\Python3
6\python setup.py install
running install
running build
running build_py
running build_ext
building 'pyconcrete._pyconcrete' extension
creating build\temp.win-amd64-3.6
creating build\temp.win-amd64-3.6\Release
creating build\temp.win-amd64-3.6\Release\src
creating build\temp.win-amd64-3.6\Release\src\pyconcrete_ext
creating build\temp.win-amd64-3.6\Release\src\pyconcrete_ext\openaes
creating build\temp.win-amd64-3.6\Release\src\pyconcrete_ext\openaes\src
C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\BIN\amd64\cl.exe /c /nolo
go /Ox /W3 /GL /DNDEBUG /MT -Isrc\pyconcrete_ext -Isrc\pyconcrete_ext\openaes\in
c -IC:\Python36\Python36\include -IC:\Python36\Python36\include "-IC:\Program Fi
les (x86)\Microsoft Visual Studio 10.0\VC\INCLUDE" "-IC:\Program Files (x86)\Mic
rosoft Visual Studio 10.0\VC\ATLMFC\INCLUDE" "-IC:\Program Files (x86)\Microsoft
 SDKs\Windows\v7.0A\include" /Tcsrc\pyconcrete_ext\pyconcrete.c /Fobuild\temp.wi
n-amd64-3.6\Release\src\pyconcrete_ext\pyconcrete.obj
pyconcrete.c
c:\python36\python36\include\pyport.h(6) : fatal error C1083: Cannot open includ
e file: 'inttypes.h': No such file or directory
error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio 10.0\\VC\\BIN\\
amd64\\cl.exe' failed with exit status 2
```



## Install OK (VS2015)

* Open VS2015 Build Tools Command Prompt

```cpp
set DISTUTILS_USE_SDK=1
    
C:\pyconcrete-0.12.1>\Python36\Python36\python.exe setup.py install
....
Generating code
Finished generating code
copying build\scripts-3.6\pyconcrete.exe -> C:\Python36\Python36\Scripts
creating C:\Python36\Python36\Lib\site-packages\pyconcrete.pth
  
C:\pyconcrete-0.12.1>\Python36\Python36\python.exe pyconcrete-admin.py compile --source=test.py --pye  
    
C:\pyconcrete-0.12.1>\Python36\Python36\Scripts\pyconcrete.exe test.pye
hello!
Press any key to continue . . .
```



original file

```python
import os

print('hello!')
os.system('pause')
```



pye file

![1572399800646](1572399800646.png)

# [sourcedefender](https://pypi.org/project/sourcedefender/)

protect your plaintext Python source code with AES 256-bit Encryption by  we hook directly into the import process

收費Billing

| Usage                                      | Billing                                                      |
| ------------------------------------------ | ------------------------------------------------------------ |
| Encryption： encrypt files                 | 每個月為 £50.00 GBP 1 Device  Auto Billing  Commercial License |
| Runtime：distribute and run encrypted code | No need                                                      |

Test Fails

```bash
C:\Python36\Python36>python -m pip install sourcedefender
Collecting sourcedefender
  Downloading https://files.pythonhosted.org/packages/29/51/9b4d937300294e015b7e
8d07abcee6eb6fd4de37cc11a172c47bf32a8188/sourcedefender-5.0.4.tar.gz (4.9MB)
     |████████████████████████████████| 5.0MB 2.2MB/s
Collecting atomicwrites==1.3.0 (from sourcedefender)
  Downloading https://files.pythonhosted.org/packages/52/90/6155aa926f43f2b2a22b
01be7241be3bfd1ceaf7d0b3267213e8127d41f4/atomicwrites-1.3.0-py2.py3-none-any.whl

Collecting beautifulsoup4==4.8.0 (from sourcedefender)
  Downloading https://files.pythonhosted.org/packages/1a/b7/34eec2fe5a49718944e2
15fde81288eec1fa04638aa3fb57c1c6cd0f98c3/beautifulsoup4-4.8.0-py3-none-any.whl (
97kB)
     |████████████████████████████████| 102kB 1.6MB/s
Collecting boltons==19.1.0 (from sourcedefender)
  Downloading https://files.pythonhosted.org/packages/32/e8/f1fcb6ba6b70d2582e7d
5cb4710b4ac39f6da1976286f5306be79913d545/boltons-19.1.0-py2.py3-none-any.whl (16
3kB)
     |████████████████████████████████| 174kB 2.2MB/s
Collecting Cython==0.29.13 (from sourcedefender)
  Downloading https://files.pythonhosted.org/packages/f8/87/a6c730d63512a00cf538
4cdc07dc09cf7285a1f79395afd9956af37a9d1e/Cython-0.29.13-cp36-cp36m-win_amd64.whl
 (1.7MB)
     |████████████████████████████████| 1.7MB 2.2MB/s
Collecting docopt==0.6.2 (from sourcedefender)
  Downloading https://files.pythonhosted.org/packages/a2/55/8f8cab2afd404cf57813
6ef2cc5dfb50baa1761b68c9da1fb1e4eed343c9/docopt-0.6.2.tar.gz
Collecting html5lib==1.0.1 (from sourcedefender)
  Downloading https://files.pythonhosted.org/packages/a5/62/bbd2be0e7943ec8504b5
17e62bab011b4946e1258842bc159e5dfde15b96/html5lib-1.0.1-py2.py3-none-any.whl (11
7kB)
     |████████████████████████████████| 122kB 2.2MB/s
Collecting pendulum==2.0.5 (from sourcedefender)
  Downloading https://files.pythonhosted.org/packages/e0/f9/ea90c2c8f0d9b6a733f6
231fac6d07476b68271bcf02bab0053888ea0fb3/pendulum-2.0.5.tar.gz (77kB)
     |████████████████████████████████| 81kB 5.5MB/s
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
    Preparing wheel metadata ... done
Collecting PySocks==1.7.0 (from sourcedefender)
  Downloading https://files.pythonhosted.org/packages/cd/18/102cc70347486e75235a
29a6543f002cf758042189cb063ec25334993e36/PySocks-1.7.0-py3-none-any.whl
Collecting TgCrypto==1.2.0 (from sourcedefender)
  Downloading https://files.pythonhosted.org/packages/cb/7e/277b75bcbb297713eb08
4a67478379c971a87ca599dc49e155466c6efa22/TgCrypto-1.2.0-cp36-cp36m-win_amd64.whl
 (44kB)
     |████████████████████████████████| 51kB 3.2MB/s
Collecting soupsieve>=1.2 (from beautifulsoup4==4.8.0->sourcedefender)
  Downloading https://files.pythonhosted.org/packages/5d/42/d821581cf568e9b7dfc5
b415aa61952b0f5e3dede4f3cbd650e3a1082992/soupsieve-1.9.4-py2.py3-none-any.whl
Collecting webencodings (from html5lib==1.0.1->sourcedefender)
  Using cached https://files.pythonhosted.org/packages/f4/24/2a3e3df732393fed8b3
ebf2ec078f05546de641fe1b667ee316ec1dcf3b7/webencodings-0.5.1-py2.py3-none-any.wh
l
Requirement already satisfied: six>=1.9 in c:\python36\python36\lib\site-package
s (from html5lib==1.0.1->sourcedefender) (1.11.0)
Collecting pytzdata>=2018.3 (from pendulum==2.0.5->sourcedefender)
  Using cached https://files.pythonhosted.org/packages/7f/f9/cdd39831b0465285c02
ed90cfbf0db25bb951cb2a35ded0e69222375bea3/pytzdata-2019.3-py2.py3-none-any.whl
Requirement already satisfied: python-dateutil<3.0,>=2.6 in c:\python36\python36
\lib\site-packages (from pendulum==2.0.5->sourcedefender) (2.7.2)
Building wheels for collected packages: pendulum
  Building wheel for pendulum (PEP 517) ... error
  ERROR: Command errored out with exit status 1:
   command: 'C:\Python36\Python36\python.exe' 'C:\Python36\Python36\lib\site-pac
kages\pip\_vendor\pep517\_in_process.py' build_wheel 'C:\Users\aeejshe\AppData\L
ocal\Temp\tmpw52yulks'
       cwd: C:\Users\aeejshe\AppData\Local\Temp\pip-install-3u4fx__v\pendulum
  Complete output (32 lines):
  Traceback (most recent call last):
    File "C:\Users\aeejshe\AppData\Local\Temp\pip-build-env-tx68ntxm\overlay\Lib
\site-packages\poetry\utils\env.py", line 385, in run
      cmd, stderr=subprocess.STDOUT, **kwargs
    File "C:\Python36\Python36\lib\subprocess.py", line 336, in check_output
      **kwargs).stdout
    File "C:\Python36\Python36\lib\subprocess.py", line 418, in run
      output=stdout, stderr=stderr)
  subprocess.CalledProcessError: Command '['python', 'setup.py', 'build', '-b',
'build']' returned non-zero exit status 1.

  During handling of the above exception, another exception occurred:

  Traceback (most recent call last):
    File "C:\Python36\Python36\lib\site-packages\pip\_vendor\pep517\_in_process.
py", line 207, in <module>
      main()
    File "C:\Python36\Python36\lib\site-packages\pip\_vendor\pep517\_in_process.
py", line 197, in main
      json_out['return_val'] = hook(**hook_input['kwargs'])
    File "C:\Python36\Python36\lib\site-packages\pip\_vendor\pep517\_in_process.
py", line 141, in build_wheel
      metadata_directory)
    File "C:\Users\aeejshe\AppData\Local\Temp\pip-build-env-tx68ntxm\overlay\Lib
\site-packages\poetry\masonry\api.py", line 60, in build_wheel
      poetry, SystemEnv(Path(sys.prefix)), NullIO(), Path(wheel_directory)
    File "C:\Users\aeejshe\AppData\Local\Temp\pip-build-env-tx68ntxm\overlay\Lib
\site-packages\poetry\masonry\builders\wheel.py", line 50, in make_in
      wb.build()
    File "C:\Users\aeejshe\AppData\Local\Temp\pip-build-env-tx68ntxm\overlay\Lib
\site-packages\poetry\masonry\builders\wheel.py", line 76, in build
      self._build(zip_file)
    File "C:\Users\aeejshe\AppData\Local\Temp\pip-build-env-tx68ntxm\overlay\Lib
\site-packages\poetry\masonry\builders\wheel.py", line 97, in _build
      "python", str(setup), "build", "-b", str(self._path / "build")
    File "C:\Users\aeejshe\AppData\Local\Temp\pip-build-env-tx68ntxm\overlay\Lib
\site-packages\poetry\utils\env.py", line 388, in run
      raise EnvCommandError(e, input=input_)
  poetry.utils.env.EnvCommandError: Command ['python', 'setup.py', 'build', '-b'
, 'build'] errored with the following return code 1, and output:
  'python' is not recognized as an internal or external command,
  operable program or batch file.

  ----------------------------------------
  ERROR: Failed building wheel for pendulum
  Running setup.py clean for pendulum
Failed to build pendulum
Building wheels for collected packages: sourcedefender, docopt
  Building wheel for sourcedefender (setup.py) ... done
  Created wheel for sourcedefender: filename=sourcedefender-5.0.4-cp36-none-any.
whl size=226165 sha256=2d40474c1372bd4ccb3b6f7e9513e9f6f7f0e83ecb895ffac4a9be8ae
7ab8700
  Stored in directory: C:\Users\aeejshe\AppData\Local\pip\Cache\wheels\41\41\b4\
a67ec0d13d5e5061b76eee596eba70bbfe17acc60d1d446d63
  Building wheel for docopt (setup.py) ... done
  Created wheel for docopt: filename=docopt-0.6.2-py2.py3-none-any.whl size=1287
7 sha256=cdf363a3f6a300270fba2ccc0a359c0a3279f28712a89859615482c0bf8d526d
  Stored in directory: C:\Users\aeejshe\AppData\Local\pip\Cache\wheels\9b\04\dd\
7daf4150b6d9b12949298737de9431a324d4b797ffd63f526e
Successfully built sourcedefender docopt
ERROR: Could not build wheels for pendulum which use PEP 517 and cannot be insta
lled directly
```

