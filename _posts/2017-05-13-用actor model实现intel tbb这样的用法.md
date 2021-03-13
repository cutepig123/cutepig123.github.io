<p>关于什么事actor model，什么事intel tbb这样的用法我就不详细说了，具体请上网查文档</p>
<p>&nbsp;</p>
<div class="cnblogs_Highlighter">
<pre class="brush:csharp;gutter:true;">	
class MyActor
{
	F f;
	MyActor inputs[];
	MyActor outputs[];
	int n;
	
	
	#internal
	void run()
	{
		f();
		for o in outputs:
			sendMsg(o, this)
	}
	
	##1
	void addOutput(o)
	{
		outputs.append(o);
	}
	
	##2
	void onFirstRun()
	{
		if inputs.empoty()
			run()
	}
	
	##3
	void onMsg(id)
	{
		n++;
		if(n==inputs.size()) 
			run()
			
	}
}

def task(g, f, dependencies)
{
	a= MyActor(f, dependencies);
	
	// Tell dependencies add this actor to trigger list
	for depend in dependencies:
		depend.addOutput(a)
		
	return a
}

t1 = task([](){hello});
t2 = task([](){world}, t1);
g.run()
</pre>
</div>
<p>　　</p>