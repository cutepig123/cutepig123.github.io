---
categories: windows
---
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

测试能跑服務，edge browser也能鏈接的上，也能map成非網盤。但是沒辦法map成網盤

```
pip install PyWebDAV3
python -m pywebdav.server.server -D g:\  -n -v -l info
```



## ftplib

功能：实现一个ftp client。这个是标准库

测试能跑服務，edge browser也能鏈接的上，也能map成非網盤。但是沒辦法map成網盤

```python
from ftplib import FTP
ftp = FTP('localhost', user='user',passwd='')
t = ftp.dir()
print(f)
ftp.quit()

def ftp_write_file(local_file, ftp, remote_file)：
    with open(local_file, 'wb') as fp:
        ftp.retrbinary('RETR %s'%remote_file, fp.write)
```

# TODO

修改pywebdav内部handler，把请求转发给ftp

## dave-0.4.0-windows-amd64

這是一個webdav服務端，測試失敗

## SMBServer_1.4.8

這是一個smb服務端。

gui沒辦法修改端口，而我又沒有c#編譯器。沒辦法測試

## ftpuse

據説可以能把ftp map成本地硬盤，但是測了下，需要管理員權限

## sshfs-win

據説可以能把sftp map成本地硬盤，沒測

https://segmentfault.com/a/1190000023726408

尽管sshfs-win简单直接，但如果读者需要更多功能（如图形界面、缓存等），就需要其他的替代品来实现同样的功能。这里笔者推荐几款替代品：

- [rclone](https://link.segmentfault.com/?enc=1LZGybpGLMfXYzjdwX%2FBYA%3D%3D.w4uDmVoPlqanXUqrNDGgjdwNxivI%2F9djFQNKzk8VVJU%3D)：一款号称『挂载任何存储服务』的跨平台开源软件，支持范围之广从Amazon S3到Google  Drive，或者是更为传统的FTP、SFTP，甚至内存！rclone提供了超过30种存储目标，并提供充分的自定义选项支持，可以实现缓存、权限等复杂配置。美中不足的是rclone并未提供图形界面，而在Windows下编写服务配置文件较为复杂，因此该软件适合有较多自定义需求的用户使用。
- [raidrive](https://link.segmentfault.com/?enc=6VmGqLbGMqYYllG2pb2c6Q%3D%3D.K81AlT19CVsjP4zSp7EWGxA%2F3fd0wPLYxTr6tq8mUSA%3D): raidrive相对比rclone最大的特色就是提供了图形界面支持，可以更方便地管理挂载目录，但这是一款商业软件，免费套餐只支持较少的挂载目标，也无法支持缓存等高级功能。

类似的软件还有很多，如[SFTP Drive](https://link.segmentfault.com/?enc=flGp%2F3ayarMvsZwUv1UQcQ%3D%3D.AkjlsK645dIIwMcGheBwc7OJQQKVH%2BkYAoCCxBM%2BPWToo6RH%2B1Sz0BA0h5%2F8%2B5g8)等，读者可以根据自己的需求挑选适合自己的软件

## rclone

據説可以吧ftpmap成本地硬盤

```bash
F:\Users\cutepig\Downloads\rclone-v1.57.0-windows-amd64>type C:\Users\cutepig\AppData\Roaming\rclone\rclone.conf
[test]
type = ftp
host = localhost
user = user
port = 21000
pass = nXnuJ8LtwOUOK4qQhz4ubJQBX0o

F:\Users\cutepig\Downloads\rclone-v1.57.0-windows-amd64>rclone mount test:/ a:
2022/03/03 19:05:09 Fatal error: failed to mount FUSE fs: mount stopped before calling Init: mount failed: cgofuse: cannot find winfsp
```

