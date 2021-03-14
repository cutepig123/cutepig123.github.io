如何能用windows把其他協議map成folder

# 背景/目的

什麼時候有這個需要?

- 如果服務器，或者对方设备沒有開啟smb或者webdav服務
- 并且，我們沒有權限在服務器上打開此類服務
- 并且，我們想讓本地程序比如python，copy，word能以file io的方式直接操作服務器上的文件

# 目标

支持

- ftp
- android手机

# 原理

windows本身支持map成drive的协议有

- smb, cifs
- webdav
- ??

所以思路

- 思路1. 在對方機器打開smb或者webdav服務。這個不是一定有條件
- 思路2。用python寫一個webdav到ftp的轉換服務
- 思路3。？？

# python行不行？

发现python有几个lib貌似不错

## [PyWebDAV3](https://github.com/andrewleech/PyWebDAV3)

功能：实现一个webdav server

测试ok

`python -m pywebdav.server.server -D g:\  -n`