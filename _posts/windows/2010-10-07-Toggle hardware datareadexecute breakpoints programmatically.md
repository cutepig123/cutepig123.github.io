---
categories: windows
---
<p><a title="http://www.codeproject.com/KB/debug/hardwarebreakpoint.aspx" href="http://www.codeproject.com/KB/debug/hardwarebreakpoint.aspx">http://www.codeproject.com/KB/debug/hardwarebreakpoint.aspx</a></p><p>&nbsp;<br /></p>

## 介绍

我决定写这篇关于硬件断点的文章，原因如下：

- Visual C ++仅支持只写数据断点。您可能还希望在读取数据时触发中断。
- 您可能没有使用Visual C ++，因此调试器很可能会使用一些基于软件的慢速机制。
- 您可能需要以编程方式设置/删除断点。
- 您可能对低级CPU感兴趣！

## 特征

- 适用于x86和x64。
- 每个线程最多支持4个硬件断点。