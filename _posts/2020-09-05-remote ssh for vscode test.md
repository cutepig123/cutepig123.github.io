remote ssh for vscode test

# Procedure

Follow https://www.cnblogs.com/lxz365/p/12705028.html

# 出現的問題

## 提示找不到ssh

需要把git里面的ssh目錄放到系統path裏面

## 出錯

俺發現這個不影響最終使用。

```bash
[11:41:27.741] Log Level: 2
[11:41:27.744] remote-ssh@0.51.0
[11:41:27.744] win32 x64
[11:41:27.747] SSH Resolver called for "ssh-remote+192.168.1.115", attempt 1
[11:41:27.748] SSH Resolver called for host: 192.168.1.115
[11:41:27.748] Setting up SSH remote "192.168.1.115"
[11:41:27.777] Using commit id "a0479759d6e9ea56afa657e454193f72aef85bd0" and quality "stable" for server
[11:41:27.780] Install and start server if needed
[11:41:28.817] Checking ssh with "ssh -V"
[11:41:28.880] > OpenSSH_8.3p1, OpenSSL 1.1.1g  21 Apr 2020
[11:41:28.884] Running script with connection command: ssh -T -D 65427 192.168.1.115 bash
[11:41:28.891] Terminal shell path: C:\WINDOWS\System32\cmd.exe
[11:41:29.046] > 
[11:41:29.047] Got some output, clearing connection timeout
[11:41:29.361] > pi@192.168.1.115's password:
[11:41:29.362] Showing password prompt
[11:41:33.925] Got password response
[11:41:33.926] "install" wrote data to terminal: "*********"
[11:41:33.958] > 
> 
[11:41:34.419] > 709072e0f328: running
> 
[11:41:34.558] > Acquiring lock on /home/pi/.vscode-server/bin/a0479759d6e9ea56afa657e454193f72ae
> f85bd0/vscode-remote-lock.pi.a0479759d6e9ea56afa657e454193f72aef85bd0
> 
[11:41:34.584] > \ln /home/pi/.vscode-server/bin/a0479759d6e9ea56afa657e454193f72aef85bd0/vscode-
> remote-lock.pi.a0479759d6e9ea56afa657e454193f72aef85bd0.target /home/pi/.vscode-
> server/bin/a0479759d6e9ea56afa657e454193f72aef85bd0/vscode-remote-lock.pi.a04797
> 59d6e9ea56afa657e454193f72aef85bd0
> 
[11:41:34.608] > Found existing installation at /home/pi/.vscode-server/bin/a0479759d6e9ea56afa65
> 7e454193f72aef85bd0...
> 
[11:41:34.705] > Found running server...
> 
> *
> * Reminder: You may only use this software with Visual Studio family products,
> * as described in the license (https://go.microsoft.com/fwlink/?linkid=2077057)
> *
> 
> 
[11:41:34.783] > Checking server status on port 38117 with wget
> 
[11:41:34.861] > 709072e0f328: start
> sshAuthSock====
> agentPort==38117==
> osReleaseId==raspbian==
> arch==armv7l==
> webUiAccessToken====
> tmpDir==/run/user/1000==
> platform==linux==
> 709072e0f328: end
> 
[11:41:34.862] Received install output: 
sshAuthSock====
agentPort==38117==
osReleaseId==raspbian==
arch==armv7l==
webUiAccessToken====
tmpDir==/run/user/1000==
platform==linux==

[11:41:34.865] Remote server is listening on port 38117
[11:41:34.865] Parsed server configuration: {"agentPort":38117,"osReleaseId":"raspbian","arch":"armv7l","webUiAccessToken":"","sshAuthSock":"","tmpDir":"/run/user/1000","platform":"linux"}
[11:41:34.868] Starting forwarding server. localPort 65430 -> socksPort 65427 -> remotePort 38117
[11:41:34.869] Forwarding server listening on 65430
[11:41:34.870] Waiting for ssh - to be ready
[11:41:34.873] -ed remote port 38117 to local port 65430
[11:41:34.874] Resolved "ssh-remote+192.168.1.115" to "127.0.0.1:65430"
[11:41:34.877] [Forwarding server 65430] Got connection 0
[11:41:34.902] ------




[11:41:34.950] [Forwarding server 65430] Got connection 1
[11:41:34.951] [Forwarding server 65430] Got connection 2
[11:41:38.958] Unhandled rejection: Error: Unable to write to User Settings because remote.SSH.remotePlatform is not a registered configuration.
    at D.reject (file:///D:/Users/cutep/AppData/Local/Programs/Microsoft VS Code/resources/app/out/vs/workbench/workbench.desktop.main.js:5545:245)
    at D.resolveAndValidate (file:///D:/Users/cutep/AppData/Local/Programs/Microsoft VS Code/resources/app/out/vs/workbench/workbench.desktop.main.js:5548:116)
    at D.doWriteConfiguration (file:///D:/Users/cutep/AppData/Local/Programs/Microsoft VS Code/resources/app/out/vs/workbench/workbench.desktop.main.js:5542:414)
    at Object.factory (file:///D:/Users/cutep/AppData/Local/Programs/Microsoft VS Code/resources/app/out/vs/workbench/workbench.desktop.main.js:5542:190)
    at u.consume (file:///D:/Users/cutep/AppData/Local/Programs/Microsoft VS Code/resources/app/out/vs/workbench/workbench.desktop.main.js:130:421)
    at file:///D:/Users/cutep/AppData/Local/Programs/Microsoft VS Code/resources/app/out/vs/workbench/workbench.desktop.main.js:130:236
    at new Promise (<anonymous>)
    at u.queue (file:///D:/Users/cutep/AppData/Local/Programs/Microsoft VS Code/resources/app/out/vs/workbench/workbench.desktop.main.js:130:160)
    at D.writeConfiguration (file:///D:/Users/cutep/AppData/Local/Programs/Microsoft VS Code/resources/app/out/vs/workbench/workbench.desktop.main.js:5542:175)
    at C.writeConfigurationValue (file:///D:/Users/cutep/AppData/Local/Programs/Microsoft VS Code/resources/app/out/vs/workbench/workbench.desktop.main.js:5570:356)
    at file:///D:/Users/cutep/AppData/Local/Programs/Microsoft VS Code/resources/app/out/vs/workbench/workbench.desktop.main.js:5558:594
    at processTicksAndRejections (internal/process/task_queues.js:85:5)

```

# 欣賞最終的截圖

連接界面 

![image-20200905120056566](remote%20ssh%20for%20vscode%20test.assets/image-20200905120056566.png)

運行python程序

![image-20200905120124481](remote%20ssh%20for%20vscode%20test.assets/image-20200905120124481.png)

debug python程序

![image-20200905120152083](remote%20ssh%20for%20vscode%20test.assets/image-20200905120152083.png)