# Idea

原本想使用powershell+python，后来发现不会用powershell啊，光是args就查了半天，算了不搞了

call $powershell $to get system path. call powershell to set system path



第二思路是完全使用python

Write a python script as main program

# FAQ

## Powershell无法执行脚本怎麽办

[关于执行策略 - PowerShell | Microsoft Docs](https://docs.microsoft.com/zh-cn/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.1)

`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

## 如何把脚本加到右键菜单

编写一个reg文件如下

```ini
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\*\shell\Command Prompt\command]
@="cmd.exe"


[HKEY_CLASSES_ROOT\*\shell\Notepad\command]
@="\"F:\\Program Files\\Notepad++\\notepad++.exe\" %1"

[HKEY_CLASSES_ROOT\*\shell\AddToPath\command]
@="PathOfPython G:\\sw\\add_sys_path.py \"%1\""
```

# APPENDIX

最终脚本如下

```python
import subprocess, sys
from functools import reduce
import os
import winreg
from os import system, environ
import win32con
from win32gui import SendMessage
from winreg import (
    CloseKey, OpenKey, QueryValueEx, SetValueEx,
    HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE,
    KEY_ALL_ACCESS, KEY_READ, REG_EXPAND_SZ, REG_SZ
)

def RunCmd(args):
	print('>>', args)
	#out_bytes = subprocess.check_output(args)
	ret = subprocess.run(args, capture_output=True)
	out_bytes = ret.stdout + ret.stderr
	out_text = out_bytes.decode('utf-8')
	return out_text

def Unique(your_list):
	return reduce(lambda x,y: x+[y] if not y in x else x, your_list,[])
	

def env_keys(user=True):
    if user:
        root = HKEY_CURRENT_USER
        subkey = 'Environment'
    else:
        root = HKEY_LOCAL_MACHINE
        subkey = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
    return root, subkey


def get_env(name, user=True):
    root, subkey = env_keys(user)
    key = OpenKey(root, subkey, 0, KEY_READ)
    try:
        value, _ = QueryValueEx(key, name)
    except WindowsError:
        return ''
    return value


def set_env(name, value):
    key = OpenKey(HKEY_CURRENT_USER, 'Environment', 0, KEY_ALL_ACCESS)
    SetValueEx(key, name, 0, REG_EXPAND_SZ, value)
    CloseKey(key)
    SendMessage(
        win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')


def remove(paths, value):
    while value in paths:
        paths.remove(value)


def unique(paths):
    unique = []
    for value in paths:
        if value not in unique:
            unique.append(value)
    return unique


def prepend_env(name, values):
    for value in values:
        paths = get_env(name).split(';')
        remove(paths, '')
        paths = unique(paths)
        remove(paths, value)
        paths.insert(0, value)
        set_env(name, ';'.join(paths))


def prepend_env_pathext(values):
    prepend_env('PathExt_User', values)
    pathext = ';'.join([
        get_env('PathExt_User'),
        get_env('PathExt', user=False)
    ])
    set_env('PathExt', pathext)

def GetDir(file):
	if os.path.isfile(file):
		return os.path.dirname(file)
	return file
	
if 0:
	set_env('Home', '%HomeDrive%%HomePath%')
	set_env('Docs', '%HomeDrive%%HomePath%\docs')
	set_env('Prompt', '$P$_$G$S')

	prepend_env('Path', [
		r'%SystemDrive%\cygwin\bin', # Add cygwin binaries to path
		r'%HomeDrive%%HomePath%\bin', # shortcuts and 'pass-through' bat files
		r'%HomeDrive%%HomePath%\docs\bin\mswin', # copies of standalone executables
	])

	# allow running of these filetypes without having to type the extension
	prepend_env_pathext(['.lnk', '.exe.lnk', '.py'])
	
if 1:
	out_text = get_env('path')
	paths = out_text.split(';')
	paths = list(map(lambda x:x.strip(), paths))
	unique_paths = list(Unique(paths))
	exist_paths = list(filter(lambda x:os.path.isdir(x), unique_paths))
	#print('original', paths)
	#print('unique_paths', unique_paths)
	#print('exist_paths',exist_paths)

	if len(sys.argv)>1:
		path_to_add = sys.argv[1:]
		path_to_add = list(map(GetDir, path_to_add))
		print('will add following paths', path_to_add)
		exist_paths = exist_paths + path_to_add
		print('modified path', exist_paths)
		os.system('pause')
		
		set_env('path', ';'.join(exist_paths))

```
