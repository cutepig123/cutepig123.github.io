---
categories: lua
---
# What is a meta table

	a meta table has a __name attr whose value is name of metatable
	a meta table is stored in LUA_REGISTRYINDEX whose key is its name

# Code analysis

## Appl
```cpp
DUMP_STACK(L);
/*{ "foo", "C:\\jshe\\codes\\mylualib\\test\\../build/v100+x64+Debug/foo_vc100_64.
dll" }*/	
	//1. 创建元表，并将该元表指定给newArray函数新创建的userdata。在Lua中userdata也是以table的身份表现的。
	//这样在调用对象函数时，可以通过验证其metatable的名称来确定参数userdata是否合法。
	luaL_newmetatable(L,"myarray");
	lua_pushvalue(L,-1);

	/*
top=4
4/-1: type=table{__name='myarray', }
3/-2: type=table{__name='myarray', }	-->name it mt
2/-3: type=string'C:\jshe\codes\mylualib\test\../build/v100+x64+Debug/foo_vc100_64.dll'
1/-4: type=string'foo'

	*/
	
	//2. 为了实现面对对象的调用方式，需要将元表的__index字段指向自身，同时再将arraylib_m数组中的函数注册到
	//元表中，之后基于这些注册函数的调用就可以以面向对象的形式调用了。
	//lua_setfield在执行后会将栈顶的table弹出。
	lua_setfield(L, -2, "__index");	// mt.__index = mt

	/*
top=3
3/-1: type=table{__index={__index={__index={__index={__index=, __name=, }, __name='myarray', }, __name='myarray', }, __name='myarray', }, __name='myarray', }
2/-2: type=string'C:\jshe\codes\mylualib\test\../build/v100+x64+Debug/foo_vc100_64.dll'
1/-3: type=string'foo'*/
	
	//将这些成员函数注册给元表，以保证Lua在寻找方法时可以定位。NULL参数表示将用栈顶的table代替第二个参数。
	luaL_register(L, NULL, arraylib_m);

	//这里只注册的工厂方法。
	luaL_register(L,"testuserdata",arraylib_f);

	DUMP_STACK(L);
/*{ "foo", "C:\\jshe\\codes\\mylualib\\test\\../build/v100+x64+Debug/foo_vc100_64.
dll", <1>{
    __gc = <function 1>,
    __index = <table 1>,
    __name = "myarray",
    __tostring = <function 2>,
    get = <function 3>,
    set = <function 4>,
    size = <function 5>
  }, {
    new = <function 6>
  } }
*/
	luaL_register(L,"testuserdatafm",arraylib_f_and_m);

	DUMP_STACK(L);
/*{ "foo", "C:\\jshe\\codes\\mylualib\\test\\../build/v100+x64+Debug/foo_vc100_64.
dll", <1>{
    __gc = <function 1>,
    __index = <table 1>,
    __name = "myarray",
    __tostring = <function 2>,
    get = <function 3>,
    set = <function 4>,
    size = <function 5>
  }, {
    new = <function 6>
  }, {
    get = <function 3>,
    new = <function 6>,
    set = <function 4>,
    size = <function 5>,
    tostring = <function 2>
  } }*/
	luaopen_packet(L);
/*{ "foo", "C:\\jshe\\codes\\mylualib\\test\\../build/v100+x64+Debug/foo_vc100_64.
dll", <1>{
    __gc = <function 1>,
    __index = <table 1>,
    __name = "myarray",
    __tostring = <function 2>,
    get = <function 3>,
    set = <function 4>,
    size = <function 5>
  }, {
    new = <function 6>
  }, {
    get = <function 3>,
    new = <function 6>,
    set = <function 4>,
    size = <function 5>,
    tostring = <function 2>
  }, {
    creatPacket = <function 7>
  } }
*/
	
	=========
```
## luaL_newmetatable

```cpp
LUALIB_API int luaL_newmetatable (lua_State *L, const char *tname) {
  if (luaL_getmetatable(L, tname) != LUA_TNIL)  /* name already in use? */	// top=1
    return 0;  /* leave previous value on top, but return 0 */
	/*top=3
3/-1: type=nil
2/-2: type=string'C:\jshe\codes\mylualib\test\../build/v100+x64+Debug/foo_vc100_64.dll'
1/-3: type=string'foo'
*/
  lua_pop(L, 1);	// =0
  lua_createtable(L, 0, 2);  /* create metatable */ // =1
/*top=3
3/-1: type=table{}
2/-2: type=string'C:\jshe\codes\mylualib\test\../build/v100+x64+Debug/foo_vc100_64.dll'
1/-3: type=string'foo'*/  
  lua_pushstring(L, tname);	// =2
 /*top=4
4/-1: type=string'myarray'
3/-2: type=table{}
2/-3: type=string'C:\jshe\codes\mylualib\test\../build/v100+x64+Debug/foo_vc100_64.dll'
1/-4: type=string'foo'*/ 
  lua_setfield(L, -2, "__name");  /* metatable.__name = tname */	// =1
  /*top=3
3/-1: type=table{'myarray', }
2/-2: type=string'C:\jshe\codes\mylualib\test\../build/v100+x64+Debug/foo_vc100_64.dll'
1/-3: type=string'foo'*/
  lua_pushvalue(L, -1);	// =2
    /*top=4
4/-1: type=table{__name='myarray', }
3/-2: type=table{__name='myarray', }
2/-3: type=string'C:\jshe\codes\mylualib\test\../build/v100+x64+Debug/foo_vc100_64.dll'
1/-4: type=string'foo'*/
  lua_setfield(L, LUA_REGISTRYINDEX, tname);  /* registry.name = metatable */
/*top=3
3/-1: type=table{__name='myarray', }
2/-2: type=string'C:\jshe\codes\mylualib\test\../build/v100+x64+Debug/foo_vc100_64.dll'
1/-3: type=string'foo'*/  
  return 1;
}
	
```
## EnumTableItem

```cpp	
void EnumTableItem(lua_State *L, int index, int nDepth)
{
/*top=4
4/-1: type=table{C:000007FEEF9610EB, }
3/-2: type=table{'myarray', {, , , , , , , }, C:000007FEEF961131, C:000007FEEF9611A9, C:000007FEEF961163, C:000007FEEF961113, C:000007FEEF96103C, }
2/-3: type=string'C:\jshe\codes\mylualib\test\../build/v100+x64+Debug/foo_vc100_64.dll'
1/-4: type=string'foo'
*/
	int top = lua_gettop(L);

	lua_pushvalue(L, index);	// copy the variable to stack top // +1
	int it = lua_gettop(L);
	myprintf("{");
	lua_pushnil(L);	
	/*{----------8, NA, 0
top=6
6/-1: type=nil
5/-2: type=table{C:000007FEEF9610EB, }
4/-3: type=table{C:000007FEEF9610EB, }
3/-4: type=table{'myarray', {, , , , , , , }, C:000007FEEF961131, C:000007FEEF9611A9, C:000007FEEF961163, C:000007FEEF961113, C:000007FEEF96103C, }
2/-5: type=string'C:\jshe\codes\mylualib\test\../build/v100+x64+Debug/foo_vc100_64.dll'
1/-6: type=string'foo'
*/
	// 2
	while (lua_next(L, it))			// If there is data, then top++, else top--	
	{
/*top=7
7/-1: type=functionC:000007FEEF9610EB
6/-2: type=string'new'
5/-3: type=table{C:000007FEEF9610EB, }
4/-4: type=table{C:000007FEEF9610EB, }
3/-5: type=table{'myarray', {, , , , , , , }, C:000007FEEF961131, C:000007FEEF9611A9, C:000007FEEF961163, C:000007FEEF961113, C:000007FEEF96103C, }
2/-6: type=string'C:\jshe\codes\mylualib\test\../build/v100+x64+Debug/foo_vc100_64.dll'
1/-7: type=string'foo'
*/	
		DumpItemEx(L, -1, nDepth+1);
		myprintf(", ");
		lua_pop(L, 1);
	}						// 1
	myprintf("}");
	lua_pop(L, 1);			// 0
	int top2 = lua_gettop(L);
	assert(top==top2);
}
	
#define luaL_register(L,n,l) (luaL_openlib(L,(n),(l),0))
```
## luaL_openlib

```cpp
LUALIB_API void luaL_openlib (lua_State *L, const char *libname,
                               const luaL_Reg *l, int nup) {
/*top=3
3/-1: type=table{__index={__index={__index={__index={__index=, __name=, }, __name='myarray', }, __name='myarray', }, __name='myarray', }, __name='myarray', }
2/-2: type=string'C:\jshe\codes\mylualib\test\../build/v100+x64+Debug/foo_vc100_64.dll'
1/-3: type=string'foo'
*/							   
  luaL_checkversion(L);
  if (libname) {
    luaL_pushmodule(L, libname, libsize(l));  /* get/create library table */
    lua_insert(L, -(nup + 1));  /* move library table to below upvalues */
  }
  if (l)
    luaL_setfuncs(L, l, nup);
  else
    lua_pop(L, nup);  /* remove upvalues */
}
```
## luaL_setfuncs

```cpp	
// This function fills the functions to a table
// the key function is
// lua_pushcclosure, lua_setfield
//
LUALIB_API void luaL_setfuncs (lua_State *L, const luaL_Reg *l, int nup) {
/*top=3
3/-1: type=table{__index={__index={__index={__index={__index=, __name=, }, __name='myarray', }, __name='myarray', }, __name='myarray', }, __name='myarray', }
2/-2: type=string'C:\jshe\codes\mylualib\test\../build/v100+x64+Debug/foo_vc100_64.dll'
1/-3: type=string'foo'
*/
  luaL_checkstack(L, nup, "too many upvalues");
  for (; l->name != NULL; l++) {  /* fill the table with given functions */
    int i;
    for (i = 0; i < nup; i++)  /* copy upvalues to the top */
      lua_pushvalue(L, -nup);
    lua_pushcclosure(L, l->func, nup);  /* closure with those upvalues */
/*top=4
4/-1: type=functionC:000007FED9A21131
3/-2: type=table{__index={__index={__index={__index={__index=, __name=, }, __name='myarray', }, __name='myarray', }, __name='myarray', }, __name='myarray', }
2/-3: type=string'C:\jshe\codes\mylualib\test\../build/v100+x64+Debug/foo_vc100_64.dll'
1/-4: type=string'foo'
*/	
    lua_setfield(L, -(nup + 2), l->name);
/*top=3
3/-1: type=table{__index={__index={__index={__index={__index=, __name=, set=, }, __name='myarray', set=C:000007FED9A21131, }, __name='myarray', set=C:000007FED9A21131, }, __name='myarray', set=C:000007FED9A21131, }, __name='myarray', set=C:000007FED9A21131, }
2/-2: type=string'C:\jshe\codes\mylualib\test\../build/v100+x64+Debug/foo_vc100_64.dll'
1/-3: type=string'foo'
*/	
  }
  lua_pop(L, nup);  /* remove upvalues */
  
/*top=3
3/-1: type=table{__index={__index={__index={__index={__index=, set=, __gc=, __tostring=, get=, size=, __name=, }, set=C:000007FED9A21131, __gc=C:000007FED9A21163, __tostring=C:000007FED9A211A9, get=C:000007FED9A2103C, size=C:000007FED9A21113, __name='myarray', }, set=C:000007FED9A21131, __gc=C:000007FED9A21163, __tostring=C:000007FED9A211A9, get=C:000007FED9A2103C, size=C:000007FED9A21113, __name='myarray', }, set=C:000007FED9A21131, __gc=C:000007FED9A21163, __tostring=C:000007FED9A211A9, get=C:000007FED9A2103C, size=C:000007FED9A21113, __name='myarray', }, set=C:000007FED9A21131, __gc=C:000007FED9A21163, __tostring=C:000007FED9A211A9, get=C:000007FED9A2103C, size=C:000007FED9A21113, __name='myarray', }
2/-2: type=string'C:\jshe\codes\mylualib\test\../build/v100+x64+Debug/foo_vc100_64.dll'
1/-3: type=string'foo'
*/  
}
```