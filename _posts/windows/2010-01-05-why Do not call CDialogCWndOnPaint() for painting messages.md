---
categories: windows
---
<p>http://social.msdn.microsoft.com/Forums/en-US/vcgeneral/thread/b688fe19-8517-473e-9183-83289f650281&nbsp;</p><p> Several things happen behind the scenes with CPaintDC.&nbsp;Its constructor calls BeginPaint, which issues an erase background message.&nbsp; So creating two CPaintDC causes interference between them.&nbsp; You can read about the BeginPaint/EndPaint APIs for more understanding of erasing and clipping.</p><br />If you want to paint in derived classes and base classes do it the way MFC does with CView.&nbsp; Create the CPaintDC&nbsp;only one time and place and pass it by reference to descendant&nbsp;classes using something like OnDraw(CDC* pDC)