<div>https://applefreak111.wordpress.com/2013/03/12/howtoopenwrt-lamp-stack%E5%AE%89%E8%A3%9D/</div><p>&nbsp;</p><p><div>opkg update<br />安裝Lighttpd, MySQL 5, 和PHP 5。<br />opkg install lighttpd lighttpd-mod-cgi lighttpd-mod-fastcgi<br />vi /etc/lighttpd/lighttpd.conf<br />&nbsp;cgi.assign = ( &#8220;.php&#8221; =&gt; &#8220;/usr/bin/php-cgi&#8221; )<br />&nbsp;index-file.names = ( &#8220;index.html&#8221;, &#8220;default.html&#8221;, &#8220;index.htm&#8221;, &#8220;default.htm&#8221;, &#8220;index.php&#8221; )<br />modify port<br />opkg install php5 php5-cgi<br />vi /etc/php.ini<br />&nbsp;doc_root = &#8220;/www1&#8243;<br />mkdir /www1<br />echo &#8220;&lt;?php phpinfo(); ?&gt;&#8221; &gt; /www1/index.php<br /><br />/etc/init.d/lighttpd restart<br /></div><br /> </p>