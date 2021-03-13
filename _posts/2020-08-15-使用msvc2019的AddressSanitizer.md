[TOC]

使用msvc2019的AddressSanitizer

# 总结

这是至今为止我使用过的几乎最强内存检测工具，能力大大强于application verifier, MSVC CRT, 速度远远快于boundschecker

原创论文 https://static.googleusercontent.com/media/research.google.com/zh-CN//pubs/archive/37752.pdf

msvc工具介绍 https://devblogs.microsoft.com/cppblog/asan-for-windows-x64-and-debug-build-support/ https://devblogs.microsoft.com/cppblog/addresssanitizer-asan-for-windows-with-msvc/

# 功能

它的原理是使用bitmap记录每一个字节的状况，比如能否写入，在编译器每次读取

- stack-use-after-scope
- stack-buffer-overflow
- stack-buffer-underflow
- heap-buffer-overflow (no underflow)
- heap-use-after-free
- calloc-overflow
- dynamic-stack-buffer-overflow (alloca)
- global-overflow (C++ source code)
- new-delete-type-mismatch
- memcpy-param-overlap
- allocation-size-too-big
- invalid-aligned-alloc-alignment
- use-after-poison
- Intra-object-overflow
- Initialization-order-fiasco
- double-free
- alloc-dealloc-mismatch

# 性能

AddressSanitizer achieves efficiency without sacrific- ing comprehensiveness. Its average slowdown is just 73% yet it accurately detects bugs at the point of occur- rence. It has found over 300 previously unknown bugs in the Chromium browser and many bugs in other software.

AddressSanitizer在不牺牲全面性的情况下实现了效率。 **它的平均速度仅慢了73％**，但它可以在发生时准确地检测到错误。 它在Chromium浏览器中发现了300多个以前未知的错误，在其他软件中也发现了许多错误。



AddressSanitizer可以发现越界访问（用于堆，堆栈和全局对象）和释放的堆内存的使用，相对较低的成本降低了73％，并且**内存使用量增加了3.4倍**，使其成为测试广泛范围的理想选择C / C ++应用程序。

# 原理

AddressSanitizer由两部分组成：一个指令模块和一个运行时库。指令模块修改代码以检查每次内存访问的影子状态，并在堆栈和全局对象周围创建中毒的红色区域，以检测上溢和下溢。当前的实现基于LLVM [4]编译器基础结构。运行时库替换malloc，free和相关函数，在分配的堆区域周围创建有毒的Redzone，延迟释放的堆区域的重用，并进行错误报告

# 不能做到的事情

- 未初始化内存
- 某些巧妙的溢出。比如溢出到其他变量区域，却没有擦花红色区域

# 使用

打开检测，注意打开它和Edit and continue功能冲突，需要关闭后者



![Enabling ASan in the MSBuild project properties](%E4%BD%BF%E7%94%A8msvc2019%E7%9A%84AddressSanitizer.assets/ASAN-Blog-Post-Image-2.png)

测试代码

```cpp
void ff(double (*t[])(int)) {
    int x;
    char a[2];
    a[2] = 1;
}
```

运行报如下错

```bash
nums contains 4 elements.
=================================================================
==14376==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x00b4566ffcf2 at pc 0x7ff7a01238a5 bp 0x00b4566ffcb0 sp 0x00b4566ffcb8
WRITE of size 1 at 0x00b4566ffcf2 thread T0
==14376==WARNING: Failed to use and restart external symbolizer!
    #0 0x7ff7a01238a4 in ff G:\temp\ConsoleApplication1\ConsoleApplication1\ConsoleApplication1.cpp:12
    #1 0x7ff7a0123a86 in main G:\temp\ConsoleApplication1\ConsoleApplication1\ConsoleApplication1.cpp:25
    #2 0x7ff7a01270c8 in invoke_main D:\agent\_work\9\s\src\vctools\crt\vcstartup\src\startup\exe_common.inl:78
    #3 0x7ff7a0126fad in __scrt_common_main_seh D:\agent\_work\9\s\src\vctools\crt\vcstartup\src\startup\exe_common.inl:288
    #4 0x7ff7a0126e6d in __scrt_common_main D:\agent\_work\9\s\src\vctools\crt\vcstartup\src\startup\exe_common.inl:330
    #5 0x7ff7a0127158 in mainCRTStartup D:\agent\_work\9\s\src\vctools\crt\vcstartup\src\startup\exe_main.cpp:16
    #6 0x7fff50ca2773 in BaseThreadInitThunk+0x13 (C:\WINDOWS\System32\KERNEL32.DLL+0x180012773)
    #7 0x7fff52d60d50 in RtlUserThreadStart+0x20 (C:\WINDOWS\SYSTEM32\ntdll.dll+0x180070d50)

Address 0x00b4566ffcf2 is located in stack of thread T0 at offset 34 in frame
    #0 0x7ff7a01212c6 in ILT+705(_get_startup_file_mode)+0x0 (G:\temp\ConsoleApplication1\x64\Debug\ConsoleApplication1.exe+0x1400012c6)

  This frame has 1 object(s):
    [32, 34) 'a' <== Memory access at offset 34 overflows this variable
HINT: this may be a false positive if your program uses some custom stack unwind mechanism, swapcontext or vfork
      (longjmp, SEH and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow G:\temp\ConsoleApplication1\ConsoleApplication1\ConsoleApplication1.cpp:12 in ff
Shadow bytes around the buggy address:
  0x0245b3bdff40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0245b3bdff50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0245b3bdff60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0245b3bdff70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0245b3bdff80: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0245b3bdff90: 00 00 00 00 00 00 00 00 00 00 f1 f1 f1 f1[02]f3
  0x0245b3bdffa0: f3 f3 f3 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0245b3bdffb0: f1 f1 f1 f1 00 00 f2 f2 f2 f2 00 00 f3 f3 f3 f3
  0x0245b3bdffc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0245b3bdffd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0245b3bdffe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==14376==ABORTING

G:\temp\ConsoleApplication1\x64\Debug\ConsoleApplication1.exe (process 14376) exited with code 1.
Press any key to close this window . . .
```

# Bug

## 使用发现这个功能在64bit的时候软件退出的时候总会误报错误，32bit没有问题

## 用msvc debugger run的时候启动crash, callstack如下

```bash
>	ntdll.dll!memset()	Unknown	Non-user code. Symbols loaded.
 	clang_rt.asan_dbg_dynamic-x86_64.dll!__asan::PoisonShadow(unsigned __int64,unsigned __int64,unsigned char)	Unknown	Non-user code. Symbols loaded.
 	clang_rt.asan_dbg_dynamic-x86_64.dll!__asan::AsanMapUnmapCallback::OnMap(unsigned __int64,unsigned __int64)	Unknown	Non-user code. Symbols loaded.
 	clang_rt.asan_dbg_dynamic-x86_64.dll!__asan::Allocator::InitLinkerInitialized(struct __asan::AllocatorOptions const &)	Unknown	Non-user code. Symbols loaded.
 	clang_rt.asan_dbg_dynamic-x86_64.dll!__asan::AsanInitInternal()	Unknown	Non-user code. Symbols loaded.
 	ucrtbased.dll!_initterm(void(*)() * first, void(*)() * last) Line 22	C++	Non-user code. Symbols loaded.
 	clang_rt.asan_dbg_dynamic-x86_64.dll!dllmain_crt_process_attach()	Unknown	Non-user code. Symbols loaded.
 	clang_rt.asan_dbg_dynamic-x86_64.dll!dllmain_crt_dispatch()	Unknown	Non-user code. Symbols loaded.
 	clang_rt.asan_dbg_dynamic-x86_64.dll!dllmain_dispatch()	Unknown	Non-user code. Symbols loaded.
 	clang_rt.asan_dbg_dynamic-x86_64.dll!_DllMainCRTStartup()	Unknown	Non-user code. Symbols loaded.
 	verifier.dll!AVrfpStandardDllEntryPointRoutine()	Unknown	Non-user code. Symbols loaded.
 	vrfcore.dll!VfCoreStandardDllEntryPointRoutine(void *,unsigned long,struct _CONTEXT *)	Unknown	Non-user code. Symbols loaded.
 	ntdll.dll!LdrpCallInitRoutine()	Unknown	Non-user code. Symbols loaded.
 	ntdll.dll!LdrpInitializeNode()	Unknown	Non-user code. Symbols loaded.
 	ntdll.dll!LdrpInitializeGraphRecurse()	Unknown	Non-user code. Symbols loaded.
 	ntdll.dll!LdrpInitializeGraphRecurse()	Unknown	Non-user code. Symbols loaded.
 	ntdll.dll!LdrpInitializeProcess()	Unknown	Non-user code. Symbols loaded.
 	ntdll.dll!_LdrpInitialize()	Unknown	Non-user code. Symbols loaded.
 	ntdll.dll!LdrpInitialize()	Unknown	Non-user code. Symbols loaded.
 	ntdll.dll!LdrInitializeThunk()	Unknown	Non-user code. Symbols loaded.

```
