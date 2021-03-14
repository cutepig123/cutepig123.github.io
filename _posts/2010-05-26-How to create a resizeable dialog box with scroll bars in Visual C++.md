<p>How to create a resizeable dialog box with scroll bars in Visual C++</p><p><p>http://support.microsoft.com/kb/262954/en-us/</p> </p><p>http://msdn.microsoft.com/en-us/library/bb787531%28v=VS.85%29.aspx#wm_paint&nbsp;</p><p>&nbsp;GetClientRect(m_rect);<br />if(m_rect.bottom&lt;rect.bottom)<br />{<br />&nbsp;&nbsp; &nbsp;m_rect.bottom = rect.bottom-m_rect.Height();<br />&nbsp;&nbsp; &nbsp;SetScrollRange(SB_VERT,0,m_rect.bottom);<br />&nbsp;&nbsp; &nbsp;ShowScrollBar(SB_VERT, TRUE);<br />}<br /><br />void CUsageDisplayTab::OnVScroll(UINT nSBCode, UINT nPos, CScrollBar* pScrollBar)<br />{<br />&nbsp;&nbsp; &nbsp;// TODO: Add your message handler code here and/or call default<br />&nbsp;&nbsp; &nbsp;// TODO: Add your message handler code here and/or call default<br />&nbsp;&nbsp; &nbsp;int nDelta;<br />&nbsp;&nbsp; &nbsp;int nMaxPos = m_rect.Height() /*- m_nCurHeight*/;<br /><br />&nbsp;&nbsp; &nbsp;switch (nSBCode)<br />&nbsp;&nbsp; &nbsp;{<br />&nbsp;&nbsp; &nbsp;case SB_LINEDOWN:<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;if (m_nScrollPos &gt;= nMaxPos)<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;return;<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;nDelta = min(nMaxPos/100,nMaxPos-m_nScrollPos);<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;break;<br /><br />&nbsp;&nbsp; &nbsp;case SB_LINEUP:<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;if (m_nScrollPos &lt;= 0)<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;return;<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;nDelta = -min(nMaxPos/100,m_nScrollPos);<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;break;<br /><br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; case SB_PAGEDOWN:<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;if (m_nScrollPos &gt;= nMaxPos)<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;return;<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;nDelta = min(nMaxPos/10,nMaxPos-m_nScrollPos);<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;break;<br /><br />&nbsp;&nbsp; &nbsp;case SB_THUMBPOSITION:<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;nDelta = (int)nPos - m_nScrollPos;<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;break;<br /><br />&nbsp;&nbsp; &nbsp;case SB_PAGEUP:<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;if (m_nScrollPos &lt;= 0)<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;return;<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;nDelta = -min(nMaxPos/10,m_nScrollPos);<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;break;<br />&nbsp;&nbsp; &nbsp;<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; default:<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;return;<br />&nbsp;&nbsp; &nbsp;}<br />&nbsp;&nbsp; &nbsp;m_nScrollPos += nDelta;<br />&nbsp;&nbsp; &nbsp;SetScrollPos(SB_VERT,m_nScrollPos,TRUE);<br />&nbsp;&nbsp; &nbsp;ScrollWindow(0,-nDelta);<br />&nbsp;&nbsp; &nbsp;CTabPageSSL::OnVScroll(nSBCode, nPos, pScrollBar);<br />}<br /><br /><br />dynamic created button<br /><br />m_cChkbx[i] = new CButton;<br />m_cChkbx[i]-&gt;Create("",WS_CHILD ,rect ,this, GET_CHEKBOX_ID(i));<br />m_cChkbx[i]-&gt;SetFont(pChkFont);<br />m_cChkbx[i]-&gt;SetButtonStyle(BS_AUTOCHECKBOX);<br />m_cChkbx[i]-&gt;ShowWindow(SW_SHOW);</p>