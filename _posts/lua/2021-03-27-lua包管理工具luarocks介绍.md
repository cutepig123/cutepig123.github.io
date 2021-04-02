---
categories: lua
---
lua包管理工具luarocks介绍

# 安装

下载[luarocks-3.5.0-windows-64.zip](http://luarocks.github.io/luarocks/releases/luarocks-3.5.0-windows-64.zip) (luarocks.exe stand-alone Windows 64-bit binary)

运行luarocks

Q：`Warning: Lua 5.3 interpreter not found at F:\Download\trans\luarocks-3.5.0-windows-64`怎么处理

下载lua from https://www.lua.org/download.html --》 http://luabinaries.sourceforge.net/ --》https://sourceforge.net/projects/luabinaries/files/5.3.6/Tools%20Executables/

下载lua的lib

最终文件目录如下

```
F:.
│  lua53.dll
│  lua53.exe
│  lua53.lib
│  luac53.exe
│  luarocks-admin.exe
│  luarocks.exe
│  wlua53.exe
│
└─include
        lauxlib.h
        lua.h
        lua.hpp
        luaconf.h
        lualib.h
```

在msvc的命令行下运行luarocks

安装socket模块

`luarocks install luasocket`

设置lua module路径

```
luarocks path >1.bat

1.bat
```

运行测试程序

`lua53 C:\Users\cutep\AppData\Roaming\luarocks\lib\luarocks\rocks-5.3\luasocket\3.0rc1-2\samples\echosrvr.lua`

# FAQ

运行luarocks显示如下

```
F:\Download\trans\luarocks-3.5.0-windows-64>luarocks.exe

Usage: luarocks [-h] [--version] [--dev] [--server <server>]
       [--only-server <server>] [--only-sources <url>]
       [--namespace <namespace>] [--lua-dir <prefix>]
       [--lua-version <ver>] [--tree <tree>] [--local] [--global]
       [--verbose] [--timeout <seconds>] [--pin] [<command>] ...

LuaRocks 3.5.0, the Lua package manager

luarocks - LuaRocks main command-line interface

Options:
   -h, --help            Show this help message and exit.
   --version             Show version info and exit.
   --dev                 Enable the sub-repositories in rocks servers for
                         rockspecs of in-development versions.
   --server <server>     Fetch rocks/rockspecs from this server (takes priority
                         over config file).
   --only-server <server>
                         Fetch rocks/rockspecs from this server only (overrides
                         any entries in the config file).
   --only-sources <url>  Restrict downloads to paths matching the given URL.
   --namespace <namespace>
                         Specify the rocks server namespace to use.
   --lua-dir <prefix>    Which Lua installation to use.
   --lua-version <ver>   Which Lua version to use.
   --tree <tree>         Which tree to operate on.
   --local               Use the tree in the user's home directory.
                         To enable it, see 'luarocks help path'.
   --global              Use the system tree when `local_by_default` is `true`.
   --verbose             Display verbose output of commands executed.
   --timeout <seconds>   Timeout on network operations, in seconds.
                         0 means no timeout (wait forever). Default is 30.
   --pin                 Create a luarocks.lock file listing the exact versions
                         of each dependency found for this rock (recursively),
                         and store it in the rock's directory. Ignores any
                         existing luarocks.lock file in the rock's sources.

Commands:
   help                  Show help for commands.
   completion            Output a shell completion script.
   build                 Build/compile a rock.
   config                Query information about the LuaRocks configuration.
   doc                   Show documentation for an installed rock.
   download              Download a specific rock file from a rocks server.
   init                  Initialize a directory for a Lua project using
                         LuaRocks.
   install               Install a rock.
   lint                  Check syntax of a rockspec.
   list                  List currently installed rocks.
   make                  Compile package in current directory using a rockspec.
   new_version           Auto-write a rockspec for a new version of a rock.
   pack                  Create a rock, packing sources or binaries.
   path                  Return the currently configured package path.
   purge                 Remove all installed rocks from a tree.
   remove                Uninstall a rock.
   search                Query the LuaRocks servers.
   show                  Show information about an installed rock.
   test                  Run the test suite in the current directory.
   unpack                Unpack the contents of a rock.
   upload                Upload a rockspec to the public rocks repository.
   which                 Tell which file corresponds to a given module name.
   write_rockspec        Write a template for a rockspec file.

Variables:
   Variables from the "variables" table of the configuration file can be
   overridden with VAR=VALUE assignments.

Configuration:
   Lua:
      Version    : 5.3
      Interpreter: F:\Download\trans\luarocks-3.5.0-windows-64/luarocks.exe (ok)
      LUA_DIR    : F:\Download\trans\luarocks-3.5.0-windows-64 (ok)
      LUA_BINDIR : F:\Download\trans\luarocks-3.5.0-windows-64 (ok)
      LUA_INCDIR : F:\Download\trans\luarocks-3.5.0-windows-64/include (ok)
      LUA_LIBDIR : F:\Download\trans\luarocks-3.5.0-windows-64 (ok)

   Configuration files:
      System  : C:/Program Files/luarocks/config-5.3.lua (not found)
      User    : C:/Users/cutep/AppData/Roaming/luarocks/config-5.3.lua (not
      found)

   Rocks trees in use:
      C:\Users\cutep\AppData\Roaming/luarocks ("user")

```

 

## Q: 如何让luarocks用msvc而不是mingw？

`luarocks install luasocket`



```
F:\Download\trans\luarocks-3.5.0-windows-64>luarocks install luasocket
Installing https://luarocks.org/luasocket-3.0rc1-2.src.rock

luasocket 3.0rc1-2 depends on lua >= 5.1 (5.3-1 provided by VM)
mingw32-gcc -O2 -c -o src/luasocket.o -IF:\Download\trans\luarocks-3.5.0-windows-64/include src/luasocket.c -DLUA_COMPAT_APIINTCASTS -DLUASOCKET_DEBUG -DLUASOCKET_INET_PTON -DWINVER=0x0501 -DLUASOCKET_API=__declspec(dllexport) -DMIME_API=__declspec(dllexport) -Ic:/windows/system32/include
'mingw32-gcc' is not recognized as an internal or external command,
operable program or batch file.

Error: Build error: Failed compiling object src/luasocket.o
```



A： 需要在msvc的命令行下运行luarocks

参考https://github.com/luarocks/luarocks/issues/1039

```
F:\Download\trans\luarocks-3.5.0-windows-64>luarocks install luasocket
Installing https://luarocks.org/luasocket-3.0rc1-2.src.rock

luasocket 3.0rc1-2 depends on lua >= 5.1 (5.3-1 provided by VM)
cl /nologo /MD /O2 -c -Fosrc/mime.obj -IF:\Download\trans\luarocks-3.5.0-windows-64/include src/mime.c -DLUA_COMPAT_APIINTCASTS -DLUASOCKET_DEBUG -DNDEBUG -DLUASOCKET_API=__declspec(dllexport) -DMIME_API=__declspec(dllexport)
mime.c
link -dll -def:core.def -out:mime/core.dll F:\Download\trans\luarocks-3.5.0-windows-64/lua53.lib src/mime.obj
Microsoft (R) Incremental Linker Version 14.27.29112.0
Copyright (C) Microsoft Corporation.  All rights reserved.

   Creating library mime\core.lib and object mime\core.exp
LINK : warning LNK4098: defaultlib 'LIBCMT' conflicts with use of other libs; use /NODEFAULTLIB:library
cl /nologo /MD /O2 -c -Fosrc/luasocket.obj -IF:\Download\trans\luarocks-3.5.0-windows-64/include src/luasocket.c -DLUA_COMPAT_APIINTCASTS -DLUASOCKET_DEBUG -DNDEBUG -DLUASOCKET_API=__declspec(dllexport) -DMIME_API=__declspec(dllexport) -Ic:/windows/system32/include
luasocket.c
cl /nologo /MD /O2 -c -Fosrc/timeout.obj -IF:\Download\trans\luarocks-3.5.0-windows-64/include src/timeout.c -DLUA_COMPAT_APIINTCASTS -DLUASOCKET_DEBUG -DNDEBUG -DLUASOCKET_API=__declspec(dllexport) -DMIME_API=__declspec(dllexport) -Ic:/windows/system32/include
timeout.c
cl /nologo /MD /O2 -c -Fosrc/buffer.obj -IF:\Download\trans\luarocks-3.5.0-windows-64/include src/buffer.c -DLUA_COMPAT_APIINTCASTS -DLUASOCKET_DEBUG -DNDEBUG -DLUASOCKET_API=__declspec(dllexport) -DMIME_API=__declspec(dllexport) -Ic:/windows/system32/include
buffer.c
cl /nologo /MD /O2 -c -Fosrc/io.obj -IF:\Download\trans\luarocks-3.5.0-windows-64/include src/io.c -DLUA_COMPAT_APIINTCASTS -DLUASOCKET_DEBUG -DNDEBUG -DLUASOCKET_API=__declspec(dllexport) -DMIME_API=__declspec(dllexport) -Ic:/windows/system32/include
io.c
cl /nologo /MD /O2 -c -Fosrc/auxiliar.obj -IF:\Download\trans\luarocks-3.5.0-windows-64/include src/auxiliar.c -DLUA_COMPAT_APIINTCASTS -DLUASOCKET_DEBUG -DNDEBUG -DLUASOCKET_API=__declspec(dllexport) -DMIME_API=__declspec(dllexport) -Ic:/windows/system32/include
auxiliar.c
cl /nologo /MD /O2 -c -Fosrc/options.obj -IF:\Download\trans\luarocks-3.5.0-windows-64/include src/options.c -DLUA_COMPAT_APIINTCASTS -DLUASOCKET_DEBUG -DNDEBUG -DLUASOCKET_API=__declspec(dllexport) -DMIME_API=__declspec(dllexport) -Ic:/windows/system32/include
options.c
cl /nologo /MD /O2 -c -Fosrc/inet.obj -IF:\Download\trans\luarocks-3.5.0-windows-64/include src/inet.c -DLUA_COMPAT_APIINTCASTS -DLUASOCKET_DEBUG -DNDEBUG -DLUASOCKET_API=__declspec(dllexport) -DMIME_API=__declspec(dllexport) -Ic:/windows/system32/include
inet.c
cl /nologo /MD /O2 -c -Fosrc/except.obj -IF:\Download\trans\luarocks-3.5.0-windows-64/include src/except.c -DLUA_COMPAT_APIINTCASTS -DLUASOCKET_DEBUG -DNDEBUG -DLUASOCKET_API=__declspec(dllexport) -DMIME_API=__declspec(dllexport) -Ic:/windows/system32/include
except.c
cl /nologo /MD /O2 -c -Fosrc/select.obj -IF:\Download\trans\luarocks-3.5.0-windows-64/include src/select.c -DLUA_COMPAT_APIINTCASTS -DLUASOCKET_DEBUG -DNDEBUG -DLUASOCKET_API=__declspec(dllexport) -DMIME_API=__declspec(dllexport) -Ic:/windows/system32/include
select.c
cl /nologo /MD /O2 -c -Fosrc/tcp.obj -IF:\Download\trans\luarocks-3.5.0-windows-64/include src/tcp.c -DLUA_COMPAT_APIINTCASTS -DLUASOCKET_DEBUG -DNDEBUG -DLUASOCKET_API=__declspec(dllexport) -DMIME_API=__declspec(dllexport) -Ic:/windows/system32/include
tcp.c
cl /nologo /MD /O2 -c -Fosrc/udp.obj -IF:\Download\trans\luarocks-3.5.0-windows-64/include src/udp.c -DLUA_COMPAT_APIINTCASTS -DLUASOCKET_DEBUG -DNDEBUG -DLUASOCKET_API=__declspec(dllexport) -DMIME_API=__declspec(dllexport) -Ic:/windows/system32/include
udp.c
cl /nologo /MD /O2 -c -Fosrc/wsocket.obj -IF:\Download\trans\luarocks-3.5.0-windows-64/include src/wsocket.c -DLUA_COMPAT_APIINTCASTS -DLUASOCKET_DEBUG -DNDEBUG -DLUASOCKET_API=__declspec(dllexport) -DMIME_API=__declspec(dllexport) -Ic:/windows/system32/include
wsocket.c
link -dll -def:core.def -out:socket/core.dll F:\Download\trans\luarocks-3.5.0-windows-64/lua53.lib src/luasocket.obj src/timeout.obj src/buffer.obj src/io.obj src/auxiliar.obj src/options.obj src/inet.obj src/except.obj src/select.obj src/tcp.obj src/udp.obj src/wsocket.obj -libpath:c:/windows/system32 ws2_32.lib
Microsoft (R) Incremental Linker Version 14.27.29112.0
Copyright (C) Microsoft Corporation.  All rights reserved.

   Creating library socket\core.lib and object socket\core.exp
LINK : warning LNK4098: defaultlib 'LIBCMT' conflicts with use of other libs; use /NODEFAULTLIB:library
No existing manifest. Attempting to rebuild...
luasocket 3.0rc1-2 is now installed in C:\Users\cutep\AppData\Roaming/luarocks (license: MIT)
```


## Q: 如何解决找不到lua的包的路径？

```
F:\Download\trans\luarocks-3.5.0-windows-64>lua53 C:\Users\cutep\AppData\Roaming\luarocks\lib\luarocks\rocks-5.3\luasocket\3.0rc1-2\samples\echosrvr.lua
lua53: ...arocks\rocks-5.3\luasocket\3.0rc1-2\samples\echosrvr.lua:6: module 'socket' not found:
        no field package.preload['socket']
        no file 'F:\Download\trans\luarocks-3.5.0-windows-64\lua\socket.lua'
        no file 'F:\Download\trans\luarocks-3.5.0-windows-64\lua\socket\init.lua'
        no file 'F:\Download\trans\luarocks-3.5.0-windows-64\socket.lua'
        no file 'F:\Download\trans\luarocks-3.5.0-windows-64\socket\init.lua'
        no file 'F:\Download\trans\luarocks-3.5.0-windows-64\..\share\lua\5.3\socket.lua'
        no file 'F:\Download\trans\luarocks-3.5.0-windows-64\..\share\lua\5.3\socket\init.lua'
        no file '.\socket.lua'
        no file '.\socket\init.lua'
        no file 'F:\Download\trans\luarocks-3.5.0-windows-64\socket.dll'
        no file 'F:\Download\trans\luarocks-3.5.0-windows-64\..\lib\lua\5.3\socket.dll'
        no file 'F:\Download\trans\luarocks-3.5.0-windows-64\loadall.dll'
        no file '.\socket.dll'
        no file 'F:\Download\trans\luarocks-3.5.0-windows-64\socket53.dll'
        no file '.\socket53.dll'
stack traceback:
        [C]: in function 'require'
        ...arocks\rocks-5.3\luasocket\3.0rc1-2\samples\echosrvr.lua:6: in main chunk
        [C]: in ?

```

A:

设置lua module路径

参考https://leafo.net/guides/customizing-the-luarocks-tree.html

```
luarocks path >1.bat

1.bat
```



## Q: 如何使用luajit？

需要人手设置luajit路径

```
F:\Download\trans\luarocks-3.5.0-windows-64>luarocks  --lua-dir F:\Download\trans\luarocks-3.5.0-windows-64 install lpeg
```

我的目录文件结构如下

```
Folder PATH listing for volume ll5_bkup
Volume serial number is 000000C3 12D5:571E
F:.
│  1.bat
│  1.txt
│  lua51.dll
│  lua51.lib
│  luajit.exe
│  luajit.lib
│  luarocks-admin.exe
│  luarocks.exe
│  minilua.lib
│  
├─include
│      lauxlib.h
│      lj_alloc.h
│      lj_arch.h
│      lj_asm.h
│      lj_asm_arm.h
│      lj_asm_arm64.h
│      lj_asm_mips.h
│      lj_asm_ppc.h
│      lj_asm_x86.h
│      lj_bc.h
│      lj_bcdump.h
│      lj_buf.h
│      lj_carith.h
│      lj_ccall.h
│      lj_ccallback.h
│      lj_cconv.h
│      lj_cdata.h
│      lj_char.h
│      lj_clib.h
│      lj_cparse.h
│      lj_crecord.h
│      lj_ctype.h
│      lj_debug.h
│      lj_def.h
│      lj_dispatch.h
│      lj_emit_arm.h
│      lj_emit_arm64.h
│      lj_emit_mips.h
│      lj_emit_ppc.h
│      lj_emit_x86.h
│      lj_err.h
│      lj_errmsg.h
│      lj_ff.h
│      lj_ffrecord.h
│      lj_frame.h
│      lj_func.h
│      lj_gc.h
│      lj_gdbjit.h
│      lj_ir.h
│      lj_ircall.h
│      lj_iropt.h
│      lj_jit.h
│      lj_lex.h
│      lj_lib.h
│      lj_mcode.h
│      lj_meta.h
│      lj_obj.h
│      lj_parse.h
│      lj_profile.h
│      lj_record.h
│      lj_snap.h
│      lj_state.h
│      lj_str.h
│      lj_strfmt.h
│      lj_strscan.h
│      lj_tab.h
│      lj_target.h
│      lj_target_arm.h
│      lj_target_arm64.h
│      lj_target_mips.h
│      lj_target_ppc.h
│      lj_target_x86.h
│      lj_trace.h
│      lj_traceerr.h
│      lj_udata.h
│      lj_vm.h
│      lj_vmevent.h
│      lua.h
│      lua.hpp
│      luaconf.h
│      luajit.h
│      lualib.h
│      
└─lua53.bkup
    │  lua53.dll
    │  lua53.exe
    │  lua53.lib
    │  luac53.exe
    │  wlua53.exe
    │  
    └─include
            lauxlib.h
            lua.h
            lua.hpp
            luaconf.h
            lualib.h
            

```

