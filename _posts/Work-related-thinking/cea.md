面临的问题和思路

# 锁定太大

作为一个cahce模块，他的锁定是全局的。锁定范围太大。如何更有效的锁定？

# 有效的获取model header

cache model根據一些設置，比如on或者off
cache session根據一些設置，比如不超過多少個
用戶能夠拿的到model信息

api
getsession
getmodel.getheader

問題。如果關閉cache model，那麽相關api都會trigger一次load model，會有很多次不需要的耗时操作

思路。model可以不cache，但model header一定會cache。允許用戶拿的到model，這樣即使他關閉cache也可以hold住一份model防止重複load