---
categories: work
---
shared memory



- http://wiedi.frubar.net/blog/2008/03/08/libmaia-xml-rpc-with-qt4/)



# How C++ interact with python

## Client-c++

- visionnt.exe
- share memory: 
  - call windows function, 
  - ex: C:\xxxx\codes\rpc\test_rpc\test_rpc\sm-client.cpp
- RPC: 
  - use C:\Users\aeexxxx\Downloads\XmlRpcC4Win1.0.15\TimXml\timxmlrpc.h

## Server-python

- python.exe
- share memory: 
  - use multiprocessing.shared_memory, 
  - ex: C:\xxxx\codes\rpc\test_rpc\test_rpc\sm-server.py
- RPC: 
  - use xmlrpc.server.SimpleXMLRPCServer, 
  - ex: C:\xxxx\codes\rpc\test_rpc\test_rpc\pyrpcserver.py

## idea

```sequence
client -> client: allocate image in share memory
client -> client: grab images to share memory directly
client -> client: fill rpc input, including image, \nimage is represented by a string, share memory name
client -> server: rpc
server -> server: get rpc input, where image buffer \nshould be get by calling share mem function 
server -> server: algorithm
server --> client: reply
```

# Ref

Ref: How to check share memory usage in windows

https://stackoverflow.com/questions/465378/program-to-view-shared-memory-in-windows

I think [Accesschk](http://technet.microsoft.com/en-us/sysinternals/bb664922.aspx) can do this.

From the commandline: `accesschk.exe -osv > objects.txt`

Search for: "Type: Section"



Ref: Test of  several libs

C:\xxxx\codes\anyrpc cmake fails due to missing dependencies

C:\Users\aeexxxx\Downloads\xmlrpc-c-1.51.07 there is vcproject but build fails

C:\Users\aeexxxx\Downloads\xmlrpc++0.7 upgrade vsproj fails

C:\Users\aeexxxx\Downloads\XmlRpcC4Win1.0.15\TimXml 



Ref: libs

- [Libiqxmlrpc](http://libiqxmlrpc.sourceforge.net/)
- [Ultra lightweight XML-RPC library for C++](http://ulxmlrpcpp.sourceforge.net/)
- [XML-RPC for C and C++](http://xmlrpc-c.sourceforge.net/)
- [XmlRpc++](http://xmlrpcpp.sourceforge.net/)
- [XmlRpc C++ client for Windows](https://sourceforge.net/projects/xmlrpcc4win/)
- [gSOAP toolkit for C and C++ supporting XML-RPC and more](http://www.cs.fsu.edu/~engelen/soap.html)
- [libmaia: XML-RPC for Qt/C++](