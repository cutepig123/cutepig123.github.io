使用QEMU模擬樹莓派Raspberry Pi

# 目標

在qemu上跑樹莓派，

# 注意

windows平臺

不需要安裝TAP網卡



# 步驟



最終脚本

```bash
# windows
#注意需要把這些文件都放到qemu的目錄下，我發現在別的路徑下有問題
#qemu-system-aarch64 -machine help
#rem qemu-system-aarch64 -M raspi3b -append "rw earlyprintk loglevel=8 console=ttyAMA0,115200 dwc_otg.lpm_enable=0 root=/dev/mmcblk0p2 rootdelay=1" -dtb bcm2710-rpi-3-b-plus.dtb -sd 2020-02-13-raspbian-buster.img -kernel kernel8.img -m 1G -smp 4 -serial stdio -usb -device usb-mouse -device usb-kbd
#rem qemu-system-arm   -M versatilepb   -cpu arm1176   -m 256   -hda .\2020-02-13-raspbian-buster.img  -dtb versatile-pb-buster.dtb   -kernel kernel-qemu-4.19.50-buster   -append "root=/dev/sda2 panic=1"   -no-reboot -display vnc=0.0.0.0:1  -netdev user,id=unet -device virtio-net-pci,netdev=unet
qemu-system-arm   -M versatilepb   -cpu arm1176   -m 256   -hda .\2020-02-13-raspbian-buster.img  -dtb versatile-pb-buster.dtb   -kernel kernel-qemu-4.19.50-buster   -append "root=/dev/sda2 panic=1"   -no-reboot  -netdev user,id=unet -device virtio-net-pci,netdev=unet
pause
```



# 參考1

https://ppfocus.com/0/di95e91ee.html

# **1、下載樹莓派系統**

最新版本下載地址 http://downloads.raspberrypi.org/raspbian/images/raspbian-2020-02-14/2020-02-13-raspbian-buster.zip

![img](https://i.ppfocus.com/2020/8/1dbe760.jpg)



# **2、下載kernel-qemu**

https://github.com/dhruvvyas90/qemu-rpi-kernel

下載如下這兩個文件

kernel-qemu-4.19.50-buster

versatile-pb-buster.dtb

![img](https://i.ppfocus.com/2020/8/19a0471.jpg)



![img](https://i.ppfocus.com/2020/8/63feacf.jpg)



![img](https://i.ppfocus.com/2020/8/26b0441.jpg)



# **3、qemu命令行啓動**

```
qemu-system-arm  -M versatilepb  -cpu arm1176  -m 256  -hda ./2020-02-13-raspbian-buster.img -dtb ./versatile-pb-buster.dtb  -kernel ./kernel-qemu-4.19.50-buster  -append &39;  -no-reboot -display vnc=10.20.90.56:1 -netdev user,id=unet -device virtio-net-pci,netdev=unet
```

 

-M versatilepb 

-cpu arm1176 

-m 256 

-hda ./2020-02-13-raspbian-buster.img 

-dtb ./versatile-pb-buster.dtb 

-kernel ./kernel-qemu-4.19.50-buster -append &39; 

-no-reboot 

-display vnc=10.20.90.56:1 

-netdev user,id=unet -device virtio-net-pci,netdev=unet

![img](https://i.ppfocus.com/2020/8/eb2ce0a.jpg)



# **4、體驗樹莓派系統 **

vnc登錄5901埠

![img](https://i.ppfocus.com/2020/8/3fb5dd5.jpg)



![img](https://i.ppfocus.com/2020/8/10eb32f.jpg)



![img](https://i.ppfocus.com/2020/8/9e706f4.jpg)



![img](https://i.ppfocus.com/2020/8/c0c40d3.jpg)



![img](https://i.ppfocus.com/2020/8/5bde3d8.jpg)



![img](https://i.ppfocus.com/2020/8/5b1e690.jpg)



![img](https://i.ppfocus.com/2020/8/df1d178.jpg)



![img](https://i.ppfocus.com/2020/8/5287665.jpg)



lscpu+uname -a可以看到cpu爲arm架構，內核也爲arm版本內核

![img](https://i.ppfocus.com/2020/8/f727711.jpg)



# **5、當然你也可以下載x86架構的鏡像**

# 參考2

1、去树莓派官网下载镜像

https://www.raspberrypi.org/software/operating-systems/#raspberry-pi-os-32-bit

windows下QEMU安装树莓派-1_ios

 

 2、去github上下载

https://github.com/dhruvvyas90/qemu-rpi-kernel

windows下QEMU安装树莓派-1_原创_02

 

windows下QEMU安装树莓派-1_笔记_03

 

 3、下载qemu虚拟机

https://www.qemu.org/download/

windows下QEMU安装树莓派-1_笔记_04

 

 4、将下载的img,dtb,buster放到这个目录下

windows下QEMU安装树莓派-1_ios_05

 

 5、创建start.bat如下

qemu-system-arm -M versatilepb -cpu arm1176 -m 256 -drive "file=2021-05-07-raspios-buster-armhf-lite.img,if=none,index=0,media=disk,format=raw,id=disk0" -device "virtio-blk-pci,drive=disk0,disable-modern=on,disable-legacy=off"  -dtb versatile-pb-buster-5.4.51.dtb -kernel kernel-qemu-5.4.51-buster -append "root=/dev/vda2 panic=1" -no-reboot -net nic -net tap,ifname=TAP2

    1.

6、安装Tap For Windows，群->博客资源有

windows下QEMU安装树莓派-1_原创_06

 

 

　7、启动成功

　windows下QEMU安装树莓派-1_github_07

 


-----------------------------------
windows下QEMU安装树莓派-1
https://blog.51cto.com/u_15127625/3575878

