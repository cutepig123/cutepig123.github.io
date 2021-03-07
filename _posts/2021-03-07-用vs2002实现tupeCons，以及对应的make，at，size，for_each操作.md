用vs2002实现tupe/Cons，以及对应的make，at，size，for_each操作



# 全特化，偏特化

https://harttle.land/2015/10/03/cpp-template.html

# 不支持偏特化的编译器的实现技巧



vs2002不支持偏特化，经过研究可以用struct内部包含的struct实现

比如,支持偏特化的编译器这样写



```cpp
template <size_t N, class Cons>
struct At
{
};
```



而vs2002需要这样写

```cpp
template <size_t N>
struct At
{
	template <class Cons>
	struct inner{};
};
```



# 全部代码如下

```cpp
// testtuple.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

struct null_type{};

template <class T1, class T2 = null_type, class T3 = null_type, class T4 = null_type, class T5 = null_type>
struct tuple
{
	T1 t1;
	T2 t2;
	T3 t3;
	T4 t4;
	T5 t5;

	tuple(T1 t1_):t1(t1_)
	{}

	tuple(T1 t1_, T2 t2_):t1(t1_), t2(t2_)
	{}

};

template <class T1, class T2 , class T3 , class T4 , class T5, class F>
void for_each(tuple<T1, T2, T3, T4, T5> &t, F f)
{
	f(t.t1);
	f(t.t2);
	f(t.t3);
	f(t.t4);
	f(t.t5);
}


template <class Head= null_type, class Tail = null_type>
struct cons
{
	typedef cons self_type;
	typedef Head head_type;
	typedef Tail tail_type;

	Head head_;
	Tail tail_;

	cons(Head const &h, Tail const &t = Tail()):head_(h), tail_(t)
	{}
};

template <class Head, class Tail>
cons<Head, Tail> make_cons(Head const &h, Tail const &t){
	return cons<Head, Tail>(h, t);
}

template <class Head>
cons<Head> make_cons(Head const &h){
	return cons<Head>(h);
}

template <size_t N>
struct At
{
	template <class Cons>
	struct inner
	{
		typedef typename At<N-1>::template inner<Cons::tail_type>::RET RET;
		static RET &data(Cons &c) {
			return At<N-1>::inner<Cons::tail_type>::data(c.tail_);
		}
	};
};

template <>
struct At<0>
{
	template <class Cons>
	struct inner
	{
		typedef typename Cons::head_type RET;
		static RET &data(Cons &c) {
			return c.head_;
		}
	};
};



template <class Cons>
struct Size
{
	static const enum {value = 1 + Size<Cons::tail_type>::value	};
};

template <>
struct Size <null_type>
{
	static const enum {value = 0	};
};

template <>
struct Size <cons<> >
{
	static const enum {value = 0	};
};

template <class Cons>
size_t size(Cons const &c)
{
	return Size<Cons>::value;
}

template <class Cons>
struct ForEach
{
	template <class F>
	static void dof(Cons c, F f)
	{
		f(c.head_);
		ForEach<Cons::tail_type>::dof(c.tail_, f);
	}
};

template <>
struct ForEach<null_type>
{
	template <class F>
		static void dof(null_type c, F f)
	{
	}
};

template <>
struct ForEach<cons<> >
{
	template <class F>
		static void dof(cons<> c, F f)
	{
	}
};


template <class Cons, class F>
void for_each_cons(Cons c, F f)
{
	ForEach<Cons>::dof(c, f);
}

struct Iter
{
	void operator()(int v) const
	{
		std::cout << v << std::endl;
	}

	void operator()(null_type v) const
	{}

	
};

int _tmain(int argc, _TCHAR* argv[])
{
	tuple<int, int> t(1,2);

	for_each(t, Iter());
	std::cout << "----------------" << std::endl;

	cons<int, cons<int> > c= make_cons(3, make_cons(2));

	for_each_cons(c, Iter());
	std::cout << "----------------" << std::endl;

	At<1>::inner<cons<int, cons<int> > >::data(c) = 100;

	size(c);

	return 0;
}


```

