---
categories: windows
---
https://stackoverflow.com/questions/1420965/redirect-windows-cmd-stdout-and-stderr-to-a-single-file

You want:

dir > a.txt 2>&1
The syntax 2>&1 will redirect 2 (stderr) to 1 (stdout). You can also hide messages by redirecting to NUL, more explanation and examples on MSDN
