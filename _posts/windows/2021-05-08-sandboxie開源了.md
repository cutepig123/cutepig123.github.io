---
categories: windows
---
# TODO

閲讀他的源代碼 at https://github.com/sandboxie-plus/Sandboxie

# 簡介

[Sandboxie](https://sandboxie-plus.com/Sandboxie)是用于32位和64位基于Windows NT的操作系统的基于沙盒的隔离软件。自从它成为开源软件以来，它一直由David Xanatos进行开发，在此之前，它由Sophos（从Invincea收购，Invincea后来从原始作者Ronen Tzur收购了它）开发。它创建了一个类似于沙盒的隔离操作环境，您可以在其中运行或安装应用程序而无需永久修改本地或映射驱动器。隔离的虚拟环境允许对不受信任的程序和Web冲浪进行受控测试。

由于Open Sourcing沙盒发布了两种版本，因此经典版本使用基于[MFC](https://en.wikipedia.org/wiki/Microsoft_Foundation_Class_Library)的UI进行构建，此外还合并了新功能和全新的基于[Q't](https://www.qt.io/)的UI。所有新添加的功能都以plus分支为目标，但通常可以通过手动编辑sandboxie.ini文件在经典版本中使用。