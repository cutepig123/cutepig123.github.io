---
categories: networking
---
<div>///what to do?<br />A(inside company) connect to cnblogs by http_proxy and post a document with content public_addr, private_addr, and find whether any other clients connect it too.<br />If find, then try to connect them, and display the information of them<br />later, user can select another client, and send files or message<br /><br />///python send file by http<br />http://stackoverflow.com/questions/68477/send-file-using-post-from-a-python-script<br />http://stackoverflow.com/questions/150517/send-file-using-post-from-a-python-script<br /><br />///python using http proxy<br /><br /># http://stackoverflow.com/questions/34079/how-to-specify-an-authenticated-proxy-for-a-python-http-connection<br /><br /># import os, urllib<br />#os.environ["http_proxy"] = "http://proxyserver:3128"<br /># data = urllib.urlopen("http://www.google.com").read()<br /># print data<br /><br /># import urllib2, urllib<br /><br /># proxy = urllib2.ProxyHandler({'http': 'http://aaants10.aaaex.asmpt.com:80'})<br /># auth = urllib2.HTTPBasicAuthHandler()<br /># opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)<br /># urllib2.install_opener(opener)<br /><br /># conn = urllib2.urlopen('http://python.org')<br /># return_str = conn.read()<br /># print return_str<br /><br />import urllib2<br /><br />def get_proxy_opener(proxyurl='http://aaants10.aaaex.asmpt.com:80', proxyuser="aaaex\\aeejshe", proxypass="hejinshou", proxyscheme="http"):<br />&nbsp;&nbsp;&nbsp; password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()<br />&nbsp;&nbsp;&nbsp; password_mgr.add_password(None, proxyurl, proxyuser, proxypass)<br /><br />&nbsp;&nbsp;&nbsp; proxy_handler = urllib2.ProxyHandler({proxyscheme: proxyurl})<br />&nbsp;&nbsp;&nbsp; proxy_auth_handler = urllib2.ProxyBasicAuthHandler(password_mgr)<br /><br />&nbsp;&nbsp;&nbsp; return urllib2.build_opener(proxy_handler, proxy_auth_handler)<br /><br />if __name__ == "__main__":<br />&nbsp;&nbsp;&nbsp; import sys<br />&nbsp;&nbsp;&nbsp; url_opener = get_proxy_opener()<br />#&nbsp;&nbsp;&nbsp; print url_opener.open('http://www.google.com').read()<br />&nbsp;&nbsp;&nbsp; urllib2.install_opener(url_opener)<br />&nbsp;&nbsp;&nbsp; print urllib2.urlopen('http://www.google.com').read()<br /><br />&nbsp;&nbsp;&nbsp; #if len(sys.argv) &gt; 4:<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; #url_opener = get_proxy_opener(*sys.argv[1:4])<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; #for url in sys.argv[4:]:<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; #&nbsp;&nbsp;&nbsp; print url_opener.open(url).headers<br />&nbsp;&nbsp;&nbsp; #else:<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # print "Usage:", sys.argv[0], "proxy user pass fetchurls..."<br /><br /><br />///NAT穿越 NAT traversal<br /><br />http://zh.wikipedia.org/wiki/NAT%E7%A9%BF%E9%80%8F<br />兩種常用的NAT穿越技術是：UDP打洞和STUN。除此之外，還有TURN, ICE, ALG，以及SBC。<br />NAT 穿透技術與 NAT 行為<br /><br />&nbsp;&nbsp;&nbsp; * Session Traversal Utilities for NAT (STUN)<br />&nbsp;&nbsp;&nbsp; * Traversal Using Relay NAT (TURN)<br />&nbsp;&nbsp;&nbsp; * NAT-T Negotiation of NAT-Traversal in the IKE<br />&nbsp;&nbsp;&nbsp; * Teredo tunneling uses NAT traversal to provide IPv6 connectivity.<br />&nbsp;&nbsp;&nbsp; * Session Border Controller (SBC)<br />&nbsp;&nbsp;&nbsp; * UDP打洞（UDP hole punching）<br />&nbsp;&nbsp;&nbsp; * TCP打洞（TCP hole punching）<br /><br />[編輯] NAT 穿透基於 NAT 控制<br /><br />&nbsp;&nbsp;&nbsp; * Realm-Specific IP (RSIP)<br />&nbsp;&nbsp;&nbsp; * Middlebox Communications (MIDCOM)<br />&nbsp;&nbsp;&nbsp; * SOCKS<br />&nbsp;&nbsp;&nbsp; * NAT Port Mapping Protocol (NAT PMP)<br />&nbsp;&nbsp;&nbsp; * Internet Gateway Device (IGD) Protocol, defined by the Universal Plug and Play (UPnP) Forum.<br />&nbsp;&nbsp;&nbsp; * Application Layer Gateway (ALG)<br /><br />[編輯] NAT 穿透整合技術<br /><br />&nbsp;&nbsp;&nbsp; * Interactive Connectivity Establishment (ICE)<br />&nbsp;<br />UDP打洞 udp hole punching<br />這項技術需要一個完全圓錐型NAT (Full-cone NAT, also known as one-to-one NAT) 設備才能夠正常工作。受限圓錐型NAT和對稱型NAT都不能使用這項技術。<br /><br />這項技術在P2P軟體和VoIP電話領域被廣泛採用。它是Skype用以繞過防火牆和NAT設備的技術之一。<br /><br />假設有兩台分別處於各自的私有網路中的主機：A和B；N1和N2是兩個NAT設備；S是一個使用了一個眾所周知的、從全球任何地方都能訪問得到的IP位址的公共伺服器<br /><br />步驟一：A和B分別和S建立UDP連接；NAT設備N1和N2創建UDP轉換狀態並分配臨時的外部埠號<br /><br />步驟二：S將這些埠號傳回A和B<br /><br />步驟三：A和B通過轉換好的埠直接聯繫到對方的NAT設備；NAT設備則利用先前創建的轉換狀態將分組發往A和B<br /><br /><br />XSTUNT 函式庫(C/C++ TCP 穿透 NAT 函式庫)<br />http://www.cis.nctu.edu.tw/~gis87577/xDreaming/XSTUNT/index_chinese.html<br /><br /><br />blogs<br />http://javascript.iteye.com/blog/151463<br /><br />source codes<br />http://www.cnblogs.com/yrh2847189/archive/2007/06/20/790013.html<br />http://blog.csdn.net/markman101/archive/2010/08/31/5853703.aspx<br />https://gist.github.com/224795<br /><br /><br />#!/usr/bin/env python<br />#<br /># udp_hole_punch_tester.py - UDP Hole Punching test tool<br />#<br /># Usage: udp_hole_punch_tester.py remote_host remote_port<br />#<br /># Run this script simultaneously on 2 hosts to test if they can punch<br /># a UDP hole to each other.<br />#<br /># * remote_port should be identical on 2 hosts.<br /># * if remote_port &lt; 1024, must be root.<br /># * tested on python 2.5.<br />#<br /># Copyright (C) 2009 Dmitriy Samovskiy, http://somic.org<br />#<br /># License: Apache License, Version 2.0<br /># http://www.apache.org/licenses/<br />#<br /><br />import sys, os, time, socket, random<br />from select import select<br /><br />def log(*args):<br />&nbsp;&nbsp;&nbsp; print time.asctime(), ' '.join([str(x) for x in args])<br /><br />def puncher(remote_host, port):<br />&nbsp;&nbsp;&nbsp; sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)<br />&nbsp;&nbsp;&nbsp; sock.bind(('', port))<br /><br />&nbsp;&nbsp;&nbsp; my_token = str(random.random())<br />&nbsp;&nbsp;&nbsp; log("my_token =", my_token)<br />&nbsp;&nbsp;&nbsp; remote_token = "_"<br /><br />&nbsp;&nbsp;&nbsp; sock.setblocking(0)<br />&nbsp;&nbsp;&nbsp; sock.settimeout(5)<br /><br />&nbsp;&nbsp;&nbsp; remote_knows_our_token = False<br /><br />&nbsp;&nbsp;&nbsp; for i in range(60):<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; r,w,x = select([sock], [sock], [], 0)<br /><br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if remote_token != "_" and remote_knows_our_token:<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log("we are done - hole was punched from both ends")<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; break<br /><br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if r:<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data, addr = sock.recvfrom(1024)<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log("recv:", data)<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if remote_token == "_":<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; remote_token = data.split()[0]<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log("remote_token is now", remote_token)<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if len(data.split()) == 3:<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log("remote end signals it knows our token")<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; remote_knows_our_token = True<br /><br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if w:<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data = "%s %s" % (my_token, remote_token)<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if remote_token != "_": data += " ok"<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log("sending:", data)<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; sock.sendto(data, (remote_host, port))<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log("sent", i)<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; time.sleep(0.5)<br /><br />&nbsp;&nbsp;&nbsp; log("done")<br />&nbsp;&nbsp;&nbsp; sock.close()<br /><br />&nbsp;&nbsp;&nbsp; return remote_token != "_"<br /><br />if __name__ == '__main__':<br />&nbsp;&nbsp;&nbsp; remote_host = sys.argv[1]<br />&nbsp;&nbsp;&nbsp; port = int(sys.argv[2])<br /><br />&nbsp;&nbsp;&nbsp; if puncher(remote_host, port):<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log("Punched UDP hole to %s:%d successfully" % (remote_host, port))<br />&nbsp;&nbsp;&nbsp; else:<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; log("Failed to punch hole")</div><p>&nbsp;</p><p><div>tcp穿透nat<br />http://nutss.gforge.cis.cornell.edu//jstunt-examples.php<br />Echo Server and Echo Client<br /><br />&nbsp;&nbsp;&nbsp; Download and install Java 1.5.0 or later<br />&nbsp;&nbsp;&nbsp; Download the JAR package that contains the STUNT library and example server/client applications.<br />&nbsp;&nbsp;&nbsp; The source code for the sample applications is at EchoServer.java and EchoClient.java.<br />&nbsp;&nbsp;&nbsp; Start the server, on a host behind a NAT, by executing: java -cp stunt.jar EchoServer you@your.domain.com<br />&nbsp;&nbsp;&nbsp; Connect the client to your echoserver by executing: java -cp stunt.jar EchoClient you@your.domain.com<br />&nbsp;&nbsp;&nbsp; To connect to the Cornell EchoServer, use echo@nutss.net as the destination when starting the client.<br />&nbsp;&nbsp;&nbsp; If everything goes well, you'll see something along the lines of: Server: Accepted saikat930@ed.u.cs.cornell.edu, and Client: Greetings saikat930@ed.u.cs.cornell.edu, this is the EchoServer at echo@nutss.net. Now you say something.<br />&nbsp;&nbsp;&nbsp; You'll be able to type lines at the Client's console and have them be echoed by the server when you press enter.<br />&nbsp;&nbsp;&nbsp; The library takes between 200ms to 1 second to connect, but slow DNS (sometimes due to the NAT) can increase the connection time by a bit.<br />Hi all,<br />(apologies if you get multiple copies of this)<br /><br />I am pleased to announce the availability of our open-source TCP NAT<br />Traversal/Hole-Punching library based on our research published in [1].<br /><br />[1] "Characterization and Measurement of TCP Traversal through NATs <br />&nbsp;&nbsp;&nbsp;&nbsp; and Firewalls", S. Guha and P. Francis. IMC 2005.<br />http://nutss.net/pub/imc05-tcpnat.pdf<br /><br />The key result of the paper is: TCP NAT traversal can work 85%-90% of<br />the time today (without any special assumptions about NATs), and 100% of<br />the time between pairs of certain popular, well-behaved NATs. See [1]<br />for more details.<br /><br />An open-source Java library for TCP NAT Traversal is now available:<br />&nbsp;webpage: http://nutss.net/stunt.php<br />&nbsp;faq: http://nutss.net/jstunt-faq.php<br />&nbsp;library and example: http://nutss.net/jstunt-examples.php<br /><br />The above library has been tested for pair-wise connectivity across 11<br />brands of NATs from Windows and Linux hosts. NATs tested were Linksys,<br />DLink, Netgear, Belkin, 3Com, Netopia, Allied Telesyn, SMC, Trendnet,<br />USR, Buffalo Tech. Out of the 121 possible pair-wise combinations, 113<br />connections are successful. The only ones that failed are when both the<br />endpoints are behind the _same_ NAT device that does not support TCP<br />hairpin-behavior yet (see [1]). <br /><br />The java library is released under LGPL; contact me if this does not<br />meet your needs. Feel free to extend it/port it etc.<br /><br />Q: I am a P2P developer/researcher. How does this help me?<br />A: The library adds TCP NAT traversal out-of-the-box. This increases the<br />connectivity in your P2P network since two users behind their NATs can<br />now exchange data without having to go through an intermediary node. You<br />can:<br />- Use this library as is (for development of P2P software, research,<br />&nbsp; small deployments, etc in java)<br />- Study it to provide TCP NAT Traversal in your existing P2P<br />&nbsp; applications in your language of choice.<br />- etc.<br /><br />If you have any questions, comments, suggestions, or problems, do not<br />hesitate to contact me. Cheers,<br />-- <br />Saikat<br /><br />Attachment: signature.asc<br />Description: This is a digitally signed message part</div>&nbsp;</p>