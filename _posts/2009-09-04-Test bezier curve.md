<img alt="" src="http://images.cnblogs.com/cnblogs_com/cutepig/bezier.jpg" width="752" height="497" />program using VC<br />user can click and move the 4 control points, the curve will update when the point is moving..<br /><br />CPoint points[4];<br />int ptSize = 10;<br />int nCaptured = -1;<br />CTestBezierView::CTestBezierView()<br />{<br />&nbsp;&nbsp; &nbsp;// TODO: add construction code here<br />&nbsp;&nbsp; &nbsp;points[0] = CPoint(5,10);<br />&nbsp;&nbsp; &nbsp;points[1] = CPoint(100,100);<br />&nbsp;&nbsp; &nbsp;points[2] = CPoint(200,100);<br />&nbsp;&nbsp; &nbsp;points[3] = CPoint(400,300);<br />}<br />void CTestBezierView::OnDraw(CDC* pDC)<br />{<br />&nbsp;&nbsp; &nbsp;CTestBezierDoc* pDoc = GetDocument();<br />&nbsp;&nbsp; &nbsp;ASSERT_VALID(pDoc);<br />&nbsp;&nbsp; &nbsp;// TODO: add draw code for native data here<br />&nbsp;&nbsp; &nbsp;for(int i=0; i&lt;4; i++)<br />&nbsp;&nbsp; &nbsp;{<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;CRect rect (points[i].x - ptSize,<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;points[i].y - ptSize,<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;points[i].x + ptSize,<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;points[i].y + ptSize);<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;pDC-&gt;Rectangle(rect);<br />&nbsp;&nbsp; &nbsp;}<br /><br />&nbsp;&nbsp; &nbsp;//draw Bezier curve<br />#define NumPts 100<br />&nbsp;&nbsp; &nbsp;<br />&nbsp;&nbsp; &nbsp;for(i=0; i&lt;NumPts; i++)<br />&nbsp;&nbsp; &nbsp;{<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;double u = i*1.0/NumPts;<br /><br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;double B0 = (1.0-u)*(1.0-u)*(1.0-u);<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;double B1 = 3 * u * (1-u) * (1-u);<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;double B2 = 3 * u * u * (1-u);<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;double B3 = u * u * u;<br /><br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;int x = points[0].x * B0 + points[1].x * B1 <br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;+ points[2].x * B2 + points[3].x * B3; <br /><br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;int y = points[0].y * B0 + points[1].y * B1 <br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;+ points[2].y * B2 + points[3].y * B3;<br /><br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;if(i==0)<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;pDC-&gt;MoveTo(x,y);<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;else<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;pDC-&gt;LineTo(x,y);<br />&nbsp;&nbsp; &nbsp;}<br />}<br /><br />void CTestBezierView::OnLButtonDown(UINT nFlags, CPoint point) <br />{<br />&nbsp;&nbsp; &nbsp;// TODO: Add your message handler code here and/or call default<br />&nbsp;&nbsp; &nbsp;for(int i=0; i&lt;4; i++)<br />&nbsp;&nbsp; &nbsp;{<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;CRect rect (points[i].x - ptSize,<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;points[i].y - ptSize,<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;points[i].x + ptSize,<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;points[i].y + ptSize);<br />&nbsp;&nbsp; &nbsp;<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;if(PtInRect(rect, point))<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;{<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;nCaptured = i;<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;SetCapture();&nbsp;&nbsp; &nbsp;//can get mouse event even mouse even out of region<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;break;<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;}&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;<br />&nbsp;&nbsp; &nbsp;}<br />&nbsp;&nbsp; &nbsp;<br /><br />&nbsp;&nbsp; &nbsp;CView::OnLButtonDown(nFlags, point);<br />}<br /><br />void CTestBezierView::OnLButtonUp(UINT nFlags, CPoint point) <br />{<br />&nbsp;&nbsp; &nbsp;// TODO: Add your message handler code here and/or call default<br />&nbsp;&nbsp; &nbsp;if(nCaptured&gt;=0)<br />&nbsp;&nbsp; &nbsp;{<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;nCaptured = -1;<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;ReleaseCapture();<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;Invalidate();<br />&nbsp;&nbsp; &nbsp;}<br /><br />&nbsp;&nbsp; &nbsp;CView::OnLButtonUp(nFlags, point);<br />}<br /><br />void CTestBezierView::OnMouseMove(UINT nFlags, CPoint point) <br />{<br />&nbsp;&nbsp; &nbsp;// TODO: Add your message handler code here and/or call default<br />&nbsp;&nbsp; &nbsp;if(nCaptured&gt;=0 )<br />&nbsp;&nbsp; &nbsp;{<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;CRect rect;<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;GetClientRect(rect);<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;if(PtInRect(rect, point))<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;{<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;points[nCaptured] = point;<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;Invalidate();<br />&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;}<br />&nbsp;&nbsp; &nbsp;}<br /><br />&nbsp;&nbsp; &nbsp;CView::OnMouseMove(nFlags, point);<br />}<br />