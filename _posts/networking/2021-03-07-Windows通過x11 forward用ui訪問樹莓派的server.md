---
categories: networking tool 樹莓派
---
Windows通過x11 forward用ui訪問linux樹莓派的server

# 背景

如果linux端沒有打開gui，一般情況衹能ssh訪問命令行。能不能通過ssh訪問gui呢？

# 軟件

putty：	ssh鏈接軟件

xming：	windows x server

# procedure

參考https://raspberrytw.tumblr.com/

很簡單，主要是改一改putty的設置，安裝xming就可以了



# 問題

無，非常順利

# 效果截圖

ssh運行geany

![image-20200905121421755](../images/2021-03-07-Windows%E9%80%9A%E9%81%8Ex11%20forward%E7%94%A8ui%E8%A8%AA%E5%95%8F%E6%A8%B9%E8%8E%93%E6%B4%BE%E7%9A%84server/image-20200905121421755.png)

在windows看到geany界面

![image-20200905121446156](../images/2021-03-07-Windows%E9%80%9A%E9%81%8Ex11%20forward%E7%94%A8ui%E8%A8%AA%E5%95%8F%E6%A8%B9%E8%8E%93%E6%B4%BE%E7%9A%84server/image-20200905121446156.png)

xming

![image-20200905121505872](../images/Windows%E9%80%9A%E9%81%8Ex11%20forward%E7%94%A8ui%E8%A8%AA%E5%95%8F%E6%A8%B9%E8%8E%93%E6%B4%BE%E7%9A%84server.assets/image-20200905121505872.png)

# 树莓派设置开机不加载图形化界面

可以使用 raspi-config 进入设置
“Boot Options” -> “Desktop / CLI” -> “Console”

在命令行下进入图形化界面
startx