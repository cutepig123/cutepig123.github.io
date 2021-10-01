## 尚未测试过

使用distpart来mount一个盘符为c:\users

修改注册表一个profilelists [link](https://cloud.tencent.com/developer/article/1773472)

https://www.win10set.com/win10/117739.html

如何转移C:\Users\Administrator\AppData文件夹
整个AppData目录挪到D盘方法：

一、打开注册表，然后定位到

HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders以及HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders;

二、修改里面AppData对应的路径到你自定义的地方，

三、接着把原AppData目录中的所有数据复制过去，最后重启电脑。


https://blog.csdn.net/qq_45392321/article/details/105300036

设置，系统，存储，更改新内容的保存位置
可以修改应用，文档，音乐，照片视频的位置

## mklink (测试过，对于users\xxx不ok，对于users下一层ok，比如uses\xxx\appdata, etc OK)

https://www.zhihu.com/question/35138451
作者：郭宇
链接：https://www.zhihu.com/question/35138451/answer/140931550
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

移动用户文件夹，用命令行的方式，是最完美的方式，经过自已多次使用，特此分享出来，如下所述：mklink /j "C:\Users\你的用户名\Desktop" "D:\MyData\Desktop"mklink /j "C:\Users\你的用户名\Documents" "D:\MyData\Documents"mklink /j "C:\Users\你的用户名\Pictures" "D:\MyData\Pictures" mklink /j "C:\Users\你的用户名\Videos" "D:\MyData\Videos" mklink /j "C:\Users\你的用户名\Downloads" "D:\MyData\Downloads"mklink /j "C:\Users\你的用户名\Music" D:\MyData\Music"把上述第一个文件夹移动到第二个文件夹，然后用管理员权限上述执行命令这是用硬连接的方式，不会有什么后遗症，也不会有兼容性的问题。用系统上的功能移动与软件移动，总是有软件认不出来还是会放到之前的位置，这种方式是欺骗系统文件还在那里，其实实际文件已经存到别的地方去了当然，这命令的第二个目录，你可以改成你需要的再执行。

```
echo robocopy /e /copyall "c:\%~1" "g:\%~1"
robocopy /e /copyall /w:0 /r:0 "c:\%~1" "g:\%~1"
pause
rem rd/s/q "c:\%~1"
echo move "c:\%1" "c:\%~1.bkup"
move "c:\%1" "c:\%~1.bkup"
pause
echo mklink/j "c:\%~1" "g:\%~1"
mklink/j "c:\%~1" "g:\%~1"
pause
```

## ProgramFilesDir (测试过，OK)

只要打开注册表编辑器，找到“HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\”分选择“CurrentVersion”项，双击右侧窗口”中的“ProgramFilesDir”，将“数值数据”修改为你自己需要的路 径如“D:\Program Files”，以后安装软件的默认位置便是这个设置的文件夹了呀。

作者：橘子两斤
链接：https://www.zhihu.com/question/308162796/answer/651468314
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

