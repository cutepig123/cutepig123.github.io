---
categories: windows
---
BEGIN_MESSAGE_MAP(CtestDialogDlg, CDialog)<br>ON_WM_CTLCOLOR()<br>END_MESSAGE_MAP()<br><br>HBRUSH CtestDialogDlg::OnCtlColor(CDC* pDC, CWnd* pWnd, UINT nCtlColor)<br>{<br>&nbsp;&nbsp; &nbsp;HBRUSH hbr = CDialog::OnCtlColor(pDC, pWnd, nCtlColor);<br><br>&nbsp;&nbsp; &nbsp;// TODO:&nbsp; 在此更改 DC 的任何属性<br>&nbsp;&nbsp; &nbsp;pDC-&gt;SetTextColor(RGB(255,0,0));<br>&nbsp;&nbsp; &nbsp;// TODO:&nbsp; 如果默认的不是所需画笔，则返回另一个画笔<br>&nbsp;&nbsp; &nbsp;//return hbr;<br>&nbsp;&nbsp; &nbsp;return&nbsp;&nbsp; m_hbrush;&nbsp; &nbsp;<br>}