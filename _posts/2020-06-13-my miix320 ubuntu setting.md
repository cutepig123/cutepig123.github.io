miis320 ubuntu

my miix320 ubuntu setting

# how to install ubuntu

# 下载ubuntu usb

# 制作usb启动盘

tools

- https://help.ubuntu.com/community/Installation/FromUSBStick
- [Download Rufus](https://rufus.ie/).
  - G:\rufus-3.10p.exe

![image-20200628155406120](image-20200628155406120.png)



# miix boot from usb

Press Fn + F12 during boot

# grub

https://esc.sh/blog/linux-on-lenovo-miix-320/

```bash
sudo nano /etc/default/grub

#GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
#GRUB_CMDLINE_LINUX="nomodeset fbcon=rotate:1"
GRUB_CMDLINE_LINUX_DEFAULT=""
GRUB_CMDLINE_LINUX="fbcon=rotate:1"
GRUB_GFXPAYLOAD_LINUX=keep

sudo update-grub
```

# xwindow

## Install xubuntu

## solve orientation

https://askubuntu.com/questions/637911/how-to-run-xrandr-commands-at-startup-in-ubuntu

```bash
sudo gedit /etc/X11/Xsession.d/45custom_xrandr-settings

xrandr -o right
```



# rust

install rust

install buildessential

install vscode

install rust plugin, lldb plugin

[安装 Rust](https://www.rust-lang.org/tools/install)
 [安装 Visual Studio Code](https://code.visualstudio.com/download)

[codelldb（OS X/Linux）](https://marketplace.visualstudio.com/items?itemName=vadimcn.vscode-lldb)

还要继续安装[Rust 扩展](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust)。

http://llever.com/2019/08/30/%E5%A6%82%E4%BD%95%E7%94%A8vscode%E8%B0%83%E8%AF%95rust%E8%AF%91/

https://hoverbear.org/blog/setting-up-a-rust-devenv/

# taskbar

![image-20200613205221233](/home/hejs/Documents/image-20200613205221233.png)
