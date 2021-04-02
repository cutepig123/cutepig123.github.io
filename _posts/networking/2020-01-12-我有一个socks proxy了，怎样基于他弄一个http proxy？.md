我有一个socks proxy了，怎样基于他弄一个http proxy？



\win32-dg9_9_13\dg9_9_13\DGROOT\bin

配置文件

```python

ADMIN=xxx@yyy.com # mail-address of the administrator of this DeleGate
SERVER=http       # the protocol DeleGate speaks with its clients
-P8080            # the entrance port on which DeleGate waits clients

SOCKS=localhost:1080 # forwarding to a SOCKS server, or


```