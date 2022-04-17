# 目的

如何安裝配置LAMP在linux?

# 步驟

```bash
# https://askubuntu.com/questions/785440/how-to-install-lamp-server-on-ubuntu
sudo apt-get install lamp-server^

#https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-ubuntu-18-04
sudo nano /var/www/html/info.php

<?php
phpinfo();

# Visit http://your_domain/info.php

 sudo wget https://github.com/FreshRSS/FreshRSS/archive/master.zip
 sudo unzip master.zip
 # Visit http://your_domain/FreshRSS-master
 
 apt search php7.4
 
 sudo service apache2 restart
 
# https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-20-04
# Setup mysql user, password and DB
sudo mysql
CREATE DATABASE example_database;
CREATE USER 'example_user'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
GRANT ALL ON example_database.* TO 'example_user'@'%';
exit
```

