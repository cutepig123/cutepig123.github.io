---
categories: interview
---
<p>算法描述：<br />
输入图G，源点v0，输出源点到各点的最短距离D<br />
中间变量v0保存当前已经处理到的顶点集合，v1保存剩余的集合<br />
1.初始化v1,D<br />
2.计算v0到v1各点的最短距离，保存到D<br />
for each i in v0;D(j)=min[D(j),G(v0(1),i)+G(i,j)] ,where j in v1<br />
3.将D中最小的那一项加入到v0，并且从v1删除这一项。<br />
4.转到2，直到v0包含所有顶点。<br />
%dijsk最短路径算法<br />
clear,clc<br />
G=[<br />
&nbsp;&nbsp;&nbsp; inf inf 10 inf 30 100;<br />
&nbsp;&nbsp;&nbsp; inf inf 5&nbsp; inf inf inf;<br />
&nbsp;&nbsp;&nbsp; inf 5 inf 50 inf inf;<br />
&nbsp;&nbsp;&nbsp; inf inf inf inf inf 10;<br />
&nbsp;&nbsp;&nbsp; inf inf inf 20 inf 60;<br />
&nbsp;&nbsp;&nbsp; inf inf inf inf inf inf;<br />
];&nbsp; %邻接矩阵 <br />
N=size(G,1); %顶点数<br />
v0=1; %源点<br />
v1=ones(1,N); %除去原点后的集合<br />
v1(v0)=0;<br />
%计算和源点最近的点<br />
D=G(v0,:);<br />
while 1<br />
&nbsp;&nbsp;&nbsp; D2=D;<br />
&nbsp;&nbsp;&nbsp; for i=1:N<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if v1(i)==0<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; D2(i)=inf;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; end<br />
&nbsp;&nbsp;&nbsp; end<br />
&nbsp;&nbsp;&nbsp; D2<br />
&nbsp;&nbsp;&nbsp; [Dmin id]=min(D2);<br />
&nbsp;&nbsp;&nbsp; if isinf(Dmin),error,end</p>
<p>&nbsp;&nbsp;&nbsp; v0=[v0 id] %将最近的点加入v0集合，并从v1集合中删除<br />
&nbsp;&nbsp;&nbsp; v1(id)=0;<br />
&nbsp;&nbsp;&nbsp; <br />
&nbsp;&nbsp;&nbsp; if size(v0,2)==N,break;end<br />
&nbsp;&nbsp;&nbsp; %计算v0（1）到v1各点的最近距离<br />
&nbsp;&nbsp;&nbsp; fprintf('计算v0（1）到v1各点的最近距离\n');v0,v1<br />
&nbsp;&nbsp;&nbsp; id=0;<br />
&nbsp;&nbsp;&nbsp; for j=1:N %计算到j的最近距离<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if v1(j)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for i=1:N<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if ~v1(i) %i在vo中<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; D(j)=min(D(j),D(i)+G(i,j));<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; end<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; D(j)=min(D(j),G(v0(1),i)+G(i,j));<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; end<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; end<br />
&nbsp;&nbsp;&nbsp; end<br />
&nbsp;&nbsp;&nbsp; fprintf('最近距离\n');D<br />
&nbsp;&nbsp;&nbsp; if isinf(Dmin),error,end<br />
end<br />
v0</p>
<p>%&gt;&gt; v0<br />
%v0 =<br />
%&nbsp;&nbsp;&nbsp;&nbsp; 1&nbsp;&nbsp;&nbsp;&nbsp; 3&nbsp;&nbsp;&nbsp;&nbsp; 5&nbsp;&nbsp;&nbsp;&nbsp; 4&nbsp;&nbsp;&nbsp;&nbsp; 6</p>
