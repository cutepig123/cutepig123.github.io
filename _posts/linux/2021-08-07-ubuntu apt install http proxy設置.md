

# 目標

可以通過ssh鏈接過去，繼而可以sftp甚至rdp

需要解決的問題

- 安裝軟件需要經過http代理
- 需要-練到内網

# apt install http proxy設置

https://www.serverlab.ca/tutorials/linux/administration-linux/how-to-set-the-proxy-for-apt-for-ubuntu-18-04/

```
sudo vi /etc/apt/apt.conf.d/proxy.conf
```

```
Acquire::http::Proxy "http://user:password@proxy.server:port/";
```

# xrdp設置

https://www.ichiayi.com/wiki/tech/ubuntu_xrdp

```
sudo apt install xfce4 xrdp
```

- 啟動 xrdp 服務

  

  ```
  sudo service xrdp restart
  ```

  

- 確認服務正常運行

  

  ```
  netstat -na | grep 3389
  ```

# ssh

https://www.ewdna.com/2012/06/ubuntu-ssh-server.html



# -方案

- 

# linux monitor tcp traffic

Installable via:

```bsh
sudo apt-get install nethogs
```

Run as root:

```bsh
sudo nethogs
```



OR

ubuntu's systemmonitor, but it can only see overall traffic, cannot see per-process