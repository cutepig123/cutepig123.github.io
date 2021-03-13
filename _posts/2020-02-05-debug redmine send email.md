# debug redmine send email

## procedure

production.log shows

```cpp
Email delivery error: 535 5.7.3 Authentication unsuccessful
```

modify password in /redmine/config/configuration.yml

reboot remine

# How to config the logger level

https://www.redmine.org/boards/2/topics/50077

`config.log_level = :info`
in /config/environments/production.rb

or :debug, or :error

This will override the default setting defined in /config/application.rb, as mentioned in the comments of the latter file.



# BitNami Redmine 搬家

双击use_redmine.bat，在弹出的命令行窗口种输入：

`mysqldump -u root -p bitnami_redmine > backup.sql`

这样整个redmine系统的数据都会被备份到backup.sql数据库文件中了，这个文件就在redmine的根目录下面。注意这里root的密码和你admin的密码是一样的。
