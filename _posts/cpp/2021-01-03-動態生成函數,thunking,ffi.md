---
categories: cpp
---
動態生成函數,thunking,ffi



# 目的

動態調用c函數

thunking。生成一個不同參數的c函數

# 工具

libffi

# 方法步驟

https://www.jianshu.com/p/92d4c06223e7

## 動態調用c函數

```cpp
int testFunc(int m, int n) {
    printf("params: %d %d \n", m, n);
    return m+n;
}

+ (void)testCall {
    testFunc(1, 2);
    
    //拿函数指针
    void* functionPtr = &testFunc;
    int argCount = 2;
    
    //参数类型数组
    ffi_type **ffiArgTypes = alloca(sizeof(ffi_type *) *argCount);
    ffiArgTypes[0] = &ffi_type_sint;
    ffiArgTypes[1] = &ffi_type_sint;
    
    //参数数据数组
    void **ffiArgs = alloca(sizeof(void *) *argCount);
    void *ffiArgPtr = alloca(ffiArgTypes[0]->size);
    int *argPtr = ffiArgPtr;
    *argPtr = 5;
    ffiArgs[0] = ffiArgPtr;
    
    void *ffiArgPtr2 = alloca(ffiArgTypes[1]->size);
    int *argPtr2 = ffiArgPtr2;
    *argPtr2 = 3;
    ffiArgs[1] = ffiArgPtr2;
    
    //生成函数原型 ffi_cfi 对象
    ffi_cif cif;
    ffi_type *returnFfiType = &ffi_type_sint;
    ffi_status ffiPrepStatus = ffi_prep_cif(&cif, FFI_DEFAULT_ABI, (unsigned int)argCount, returnFfiType, ffiArgTypes);
    
    if (ffiPrepStatus == FFI_OK) {
        //生成用于保存返回值的内存
        void *returnPtr = NULL;
        if (returnFfiType->size) {
            returnPtr = alloca(returnFfiType->size);
        }
        //根据cif函数原型，函数指针，返回值内存指针，函数参数数据调用这个函数
        ffi_call(&cif, functionPtr, returnPtr, ffiArgs);
        
        //拿到返回值
        int returnValue = *(int *)returnPtr;
        printf("ret: %d \n", returnValue);
    }
}

```

## thunking。生成一個不同參數的c函數

```cpp
#include <stdio.h>
#include <ffi.h>

/* Acts like puts with the file given at time of enclosure. */
// 函数实体
void puts_binding(ffi_cif *cif, unsigned int *ret, void* args[],
                  FILE *stream)
{
    *ret = fputs(*(char **)args[0], stream);
}

int main()
{
    ffi_cif cif;
    ffi_type *args[1];
    ffi_closure *closure;
    
    int (*bound_puts)(char *);  //声明一个函数指针
    int rc;
    
    /* Allocate closure and bound_puts */  //创建closure
    closure = ffi_closure_alloc(sizeof(ffi_closure), &bound_puts);
    
    if (closure)
    {
        /* Initialize the argument info vectors */
        args[0] = &ffi_type_pointer;
        
        /* Initialize the cif */  //生成函数原型
        if (ffi_prep_cif(&cif, FFI_DEFAULT_ABI, 1,
                         &ffi_type_uint, args) == FFI_OK)
        {
            /* Initialize the closure, setting stream to stdout */
            // 通过 ffi_closure 把 函数原型_cifPtr / 函数实体JPBlockInterpreter / 上下文对象self / 函数指针blockImp 关联起来
            if (ffi_prep_closure_loc(closure, &cif, puts_binding,
                                     stdout, bound_puts) == FFI_OK)
            {
                rc = bound_puts("Hello World!");
                /* rc now holds the result of the call to fputs */
            }
        }
    }
    
    /* Deallocate both closure, and bound_puts */
    ffi_closure_free(closure);   //释放闭包
    
    return 0;
}

```



# Refs

https://stackoverflow.com/questions/10451635/c-and-fully-dynamic-functions

https://stackoverflow.com/questions/10436431/detouring-and-using-a-thiscall-as-a-hook-gcc-calling-convention



ATL

_stdcallthunk

CWndProcThunk