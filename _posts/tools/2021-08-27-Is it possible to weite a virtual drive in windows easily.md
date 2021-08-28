

someone mentions [pywinfuse](https://code.google.com/archive/p/pywinfuse/). but it seems is a unmaintained google codes



windows support mount FTP as a drive



~~windows has a programming API called [Windows 投影文件系统 (ProjFS)](https://docs.microsoft.com/en-us/windows/win32/projfs/projected-file-system)~~



看看[Dokan](https://dokan-dev.github.io/)是 Windows 的用户模式文件系统。有可用的 Ruby、.NET（和由 3rd 方提供的 Java）绑定，而且我认为编写 Python 绑定也不难。



它是否需要是 Windows 原生的？至少有一种协议既可以由 Windows 资源管理器浏览，也可以由免费的 Python 库提供服务：FTP。把你的程序放在 pyftpdlib 后面，你就完成了。



您可能对[PyFilesystem](http://pyfilesystem.org/)感兴趣；

> *Python的文件系统抽象层*
>
> PyFilesystem 是文件系统的抽象层。就像 Python 的类文件对象提供了一种访问文件的通用方式一样，PyFilesystem 提供了一种访问整个文件系统的通用方式。您可以编写独立于平台的代码来处理本地文件，这些代码也适用于任何受支持的文件系统（zip、ftp、S3 等）。

什么主页上的描述不做广告是，你可以再[暴露](http://docs.pyfilesystem.org/en/latest/expose.html)再次这个抽象的文件系统，其中包括SFTP，FTP（虽然[目前disfunct](https://github.com/PyFilesystem/pyfilesystem/issues/238)，大概[可以解决的](https://github.com/PyFilesystem/pyfilesystem/pull/239)）和[杜坎](http://docs.pyfilesystem.org/en/latest/expose/dokan.html)（[DITO](https://github.com/PyFilesystem/pyfilesystem/issues/236)以及）[保险丝](http://docs.pyfilesystem.org/en/latest/expose/fuse.html)。



https://github.com/billziss-gh/winfsp WinFsp · Windows File System Proxy WinFsp 是一组用于 Windows 计算机的软件组件，允许创建用户模式文件系统。从这个意义上说，它类似于 FUSE（用户空间中的文件系统），后者在类 UNIX 计算机上提供相同的功能。



https://github.com/dokan-dev/dokany 通过使用 Dokan，您可以非常轻松地创建自己的文件系统，而无需编写设备驱动程序。Dokan 类似于 FUSE（用户空间中的 Linux 文件系统），但适用于 Windows。此外，dokany 包含一个[FUSE 包装器](https://github.com/dokan-dev/dokany/wiki/FUSE) ，可帮助您在不更改的情况下移植 FUSE 文件系统。



https://github.com/Scille/winfspy **Tested! It Works!**



对于对此感兴趣的其他开发人员，还有[`winfspy`](https://github.com/Scille/winfspy/tree/master/src/winfspy)用于 winfsp 的[`fusepy`](https://github.com/fusepy/fusepy)python 绑定和用于支持 winfsp 的 FUSE 的 python 绑定。 —— [科本](https://superuser.com/users/471023/coburn) [2019 年 4 月 24 日 7:14](https://superuser.com/questions/179436/is-it-possible-to-use-fuse-with-windows#comment2156747_1428914) 



据我了解，Windows 没有附带任何可以让您定义自己的文件系统而无需向内核添加一些代码（即驱动程序）的东西。所以你需要管理员权限。

在 2010 年[FUSE 常见问题中](http://sourceforge.net/apps/mediawiki/fuse/index.php?title=OperatingSystems#Windows)提到了一些潜在的替代方案，但除了 Dokan 之外，它们都看起来像雾化器。杜坎已被放弃，但一些叉住在：[Dokanx](https://github.com/BenjaminKim/dokanx)，[Dokany](https://github.com/Maxhy/dokany)，和[更多的](https://groups.google.com/d/msg/dokan/j0J7TQAzomU/LxBIPCgYxHIJ)还有至少两个[.NET](https://github.com/apaka/dokan-net) [绑定](https://github.com/dokan-dev/dokan-dotnet)。Dokany 有一个[SSHFS 组件](https://github.com/dokan-dev/dokan-sshfs)。



当 MS 引入[GVFS 时，](https://devblogs.microsoft.com/devops/announcing-gvfs-git-virtual-file-system/)他们创建了一个或多或少类似于 FUSE 的新过滤器驱动程序

> GVFS 依赖于新的 Windows 过滤器驱动程序（在道德上相当于 Linux 中的 FUSE 驱动程序），我们已经与 Windows 团队合作，使该驱动程序尽早可用，以便您可以尝试 GVFS。
>
> [扩展 Git（以及一些背景故事）](https://devblogs.microsoft.com/bharry/scaling-git-and-some-back-story/)

也可以看看

- [Windows、Git、FUSE 和道德对等](https://www.osr.com/blog/2017/02/24/windows-git-fuse-moral-equivalence/)
- [微软宣布推出 Git 虚拟文件系统 (GVFS)](https://www.phoronix.com/scan.php?page=news_item&px=Microsoft-GVFS-Git-Filesystem)





Ref

https://stackoverflow.com/questions/1325568/easiest-way-to-program-a-virtual-file-system-in-windows-with-python

https://superuser.com/questions/179436/is-it-possible-to-use-fuse-with-windows