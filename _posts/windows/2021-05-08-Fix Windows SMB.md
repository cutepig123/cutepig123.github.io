---
categories: windows
---
# 問題

可以訪問`\\localhost`，但無法訪問`\\ip`

# 解決方案

To automate the Twisty Impersonator [solution](https://superuser.com/a/1296023/213131) I have developed a command line program named [ShareFix](https://github.com/filippobottega/ShareFix).

# ref

https://superuser.com/questions/1240213/cannot-connect-to-windows-share-via-local-network-ip-address-but-can-by-localho/1296023

分析

You *cannot* use an IP address to map a Microsoft Net Server (the backend of Windows File Sharing) if NetBIOS over TCP/IP is disabled. You must use the NetBIOS hostname, which is why `\\localhost\temp` works, but `\\192.168.1.2\temp` doesn't.

