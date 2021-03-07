[TOC]

CMake

# 評價

## Pros

它简化了cross platform, OS, compiler的开发成本，同时支持多个IDE(VS, QtCreator, Eclipse, CLion...etc.),并且有一个成熟开源社区。 当你挣扎于将based on autotools的项目迁移至OSX或者Windows的时候，你就会感谢CMake的美好

## Cons

CMake的learning curve真的不是一般的高

CMake没有好的paradigm,

它是基于过程式编程语言生成项目，而不是描述项目。这产生了一系列的恶果。

- CMakeLists基本不可能像各种XML的项目文件那样，被IDE作为配置文件。于是你永远需要手工编写CMakeLists的内容，而不能使用图形界面去配置一个个的目标。这对于开发人员的要求其实是很高的。
- 从CMakeLists里面，你很难看到一个目标**最终**的编译选项、包含路径、预定义宏都有那些。如果你想要看到这些，除非你对CMakeLists“求解”，把项目生成出来，在生成的结果里才能看到。而对于大型项目，generate的时间可能很长。于是你就难以**交互地**编辑一个项目，经常需要耗时的修改CMakeLists、生成、编译、查错的循环。

它虽然是过程式语言，但函数TMD没有返回值！

# Modern CMake

Modern CMake在target based的开发理念下，其实已经有了相当强的模块化能力。`include` keyword已经淡出了历史舞台，成为legacy。

Q: target based？？

[It’s Time To Do CMake Right](https://link.zhihu.com/?target=https%3A//pabloariasal.github.io/2018/02/19/its-time-to-do-cmake-right/)

[https://gist.github.com/mbinna/](https://link.zhihu.com/?target=https%3A//gist.github.com/mbinna/c61dbb39bca0e4fb7d1f73b0d66a4fd1)

自动解决依赖问题早就不是什么问题了： Package developers应该生成package files给upstream users使用。如果你创建了一个library foo, 理论上别人应当只需要find_package(foo)便足以。

https://ukabuer.me/blog/more-modern-cmake/

# 概念

https://zhuanlan.zhihu.com/p/76975231

现代化的CMake是围绕 ***Target*** 和 ***Property*** 来定义的，并且竭力避免出现变量variable的定义。Variable横行是典型CMake2.8时期的风格。现代版的CMake更像是在遵循OOP的规则，通过target来约束link、compile等相关属性的作用域。如果把一个Target想象成一个**对象（Object）**，会发现两者的组织方式非常相似：

- 构造函数：

- - add_executable
  - add_library

- 成员函数：

- - get_target_property()
  - set_target_properties()
  - get_property(TARGET)
  - set_property(TARGET)
  - target_compile_definitions()
  - target_compile_features()
  - target_compile_options()
  - target_include_directories()
  - target_link_libraries()
  - target_sources()

- 成员变量

- - Target properties（太多）

# 一个现代CMake工程的简单例子

https://ukabuer.me/blog/more-modern-cmake/

使用 Imported Target 的另一个好处是，我们在引入一个依赖时**只需要 link 其 Imported Target，不再需要手动加入其头文件目录了**。因为依赖的头文件目录已经在其 target 的`INTERFACE`属性里了，而`INTERFACE`属性是可传递的，于是：

```c
# 一个现代CMake工程的简单例子
cmake_minimum_required(VERSION 3.12)
project(myproj)

find_package(Poco REQUIRED COMPONENTS Net Util)

add_executable(MyEXE)
target_source(MyEXE PRIVATE "main.cpp")
target_link_library(MyEXE PRIVATE Poco::Net Poco::Util)
target_compile_definition(MyEXE PRIVATE std_cxx_14)
```

# find_package

## find_package原理

https://www.jianshu.com/p/46e9b8a6cb6a https://blog.csdn.net/dbzhang800/article/details/6329314

find_package采用两种模式搜索库：

- **Module模式**：搜索**CMAKE_MODULE_PATH**指定路径下的**FindXXX.cmake**文件，执行该文件从而找到XXX库。其中，具体查找库并给**XXX_INCLUDE_DIRS**和**XXX_LIBRARIES**两个变量赋值的操作由FindXXX.cmake模块完成。
- **Config模式**：搜索**XXX_DIR**指定路径下的**XXXConfig.cmake**文件，执行该文件从而找到XXX库。其中具体查找库并给**XXX_INCLUDE_DIRS**和**XXX_LIBRARIES**两个变量赋值的操作由XXXConfig.cmake模块完成。

每个模块一般都会提供一下几个变量

- <name>_FOUND
- <name>_INCLUDE_DIR 或 <name>_INCLUDES
- <name>_LIBRARY 或 <name>_LIBRARIES 或 <name>_LIBS
- <name>_DEFINITIONS

## Config file 以及 Find file 究竟要怎么写？（早期 CMake 时代）

https://ukabuer.me/blog/more-modern-cmake/

在 C/C++工程里，对于依赖，我们最基本的要求就是知道他们的链接库路径和头文件目录，通过 CMake 的`find_library`和`find_path`两个命令就可以完成任务：

```c
find_library(MPI_LIBRARY
  NAMES mpi
  HINTS "${CMAKE_PREFIX_PATH}/lib" ${MPI_LIB_PATH}
  # 如果默认路径没找到libmpi.so，还会去MPI_LIB_PATH找，下游使用者可以设置这个变量值
)
find_path(MPI_INCLUDE_DIR
  NAMES mpi.h
  PATHS "${CMAKE_PREFIX_PATH}/include" ${MPI_INCLUDE_PATH}
  # 如果默认路径没找到mpi.h，还会去MPI_INCLUDE_PATH找，下游使用者可以设置这个变量值
)
```

## Config file 以及 Find file 究竟要怎么写？（現代）

因此现代 CMake 提供了一种特别的 target，Imported Target，创建命令为`add_library(Boost::Abc STATIC IMPORTRED)`用于表示在项目外部已经存在、无需编译的依赖



## 自己寫的config写好后放到本项目的目录下

修改`CMAKE_MODULE_PATH`这个 CMAKE 变量：

```c
list(INSERT CMAKE_MODULE_PATH 0 ${CMAKE_SOURCE_DIR}/cmake)
```

这样`${CMAKE_SOURCE_DIR}/cmake`目录下的 Find file 就可以被 CMake 找到了。



```c
# spdlog库的Imported Target
set_target_properties(spdlog::spdlog PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/spdlog/spdlog.lib"
)
```



https://ukabuer.me/blog/manage-deps-with-cmake

# QA

- 

# 使用Caffe例子

```cmake
set(Caffe_DIR /home/wjg/projects/caffe/build)   #添加CaffeConfig.cmake的搜索路径
#OR
#set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/Modules/")

find_package(Caffe REQUIRED)

if (NOT Caffe_FOUND)
    message(FATAL_ERROR "Caffe Not Found!")
endif (NOT Caffe_FOUND)

include_directories(${Caffe_INCLUDE_DIRS})

add_executable(useSSD ssd_detect.cpp)
target_link_libraries(useSSD ${Caffe_LIBRARIES})
```



# Qt

```cmake
set(QT_VERSION_REQ "5.2")
set(CMAKE_INCLUDE_CURRENT_DIR ON)
find_package(Qt5Core ${QT_VERSION_REQ} REQUIRED)
find_package(Qt5Quick ${QT_VERSION_REQ} REQUIRED)
find_package(Qt5Widgets ${QT_VERSION_REQ} REQUIRED)
find_package(Qt5Gui ${QT_VERSION_REQ} REQUIRED)

set(CMAKE_AUTOMOC ON)
QT5_WRAP_UI( UI_HDRS ${UI_FILES} )

ADD_EXECUTABLE(${MOC_HEADERS})

target_link_libraries(${PROJECT_NAME}
  Qt5::Core
  Qt5::Quick
  Qt5::Widgets  
  Qt5::Gui  
)
```

# gtest

https://github.com/selyunin/gtest_submodule

## 用git submodule方式

```bash
[submodule "googletest"]
	path = googletest
	url = https://github.com/google/googletest.git
```

問題

默認的gtest有幾個問題

- treat warning as error，導致compile失敗
- runtimelib選項為multi thread，需要改成multi thread dll

需要人手修改編譯選項

https://stackoverflow.com/questions/12540970/how-to-make-gtest-build-mdd-instead-of-mtd-by-default-using-cmake

G:\_codes\test_gtest\gtest_submodule\googletest\googletest\cmake\internal_utils.cmake

```cmake
set(cxx_base_flags "-GS -W4 -WX -wd4251 -wd4275 -nologo -J -Zi")
```

to

```cmake
set(cxx_base_flags "-GS -W4 -WX- -wd4251 -wd4275 -nologo -J -Zi")
```

## find_package

cmake自帶的findgtest.cmake好像不工作，需要人手把它刪除，然後自定義下下下來的gtest

```cmake
set(CMAKE_PREFIX_PATH  "G:/googletest-distribution/lib/cmake/GTest" ${CMAKE_PREFIX_PATH})
find_package(GTest REQUIRED)
```





# boost

https://github.com/Orphis/boost-cmake

Install the submodule in your project structure:

```
git submodule add https://github.com/Orphis/boost-cmake.git
```

Use it! In your CMakeLists.txt file:

```
add_subdirectory(boost-cmake)
...
target_link_libraries(lib_using_filesystem PUBLIC Boost::filesystem)
target_link_libraries(lib_using_header_only PUBLIC Boost::boost)
```

# RapidJSON

# OpenCV

https://github.com/sunsided/opencv-cmake

https://github.com/berkus/opencv-cmake-example

```

```



# 遍历拿到全部的源文件：

```c
file(GLOB_RECURSE SRCS ${CMAKE_CURRENT_SOURCE_DIR}/*.cpp)
```

命令第一个参数`GLOB_RECURSE`表明递归的查找子文件夹，第二个参数`SRCS`则是存储结果的变量名，第三个参数为目标文件的匹配模式，找到符合条件的 cpp 文件后，他们的路径会以字符串数组的形式保存在 SRCS 变量中，使用方式如下：

```c
target_source(MyLib PRIVATE ${SRCS})
```

# 教程

https://github.com/xizhibei/blog/issues/134

https://zhuanlan.zhihu.com/p/112712537

https://segmentfault.com/a/1190000015113987

https://zhuanlan.zhihu.com/p/76975231

https://phenix3443.github.io/notebook/cmake/effective-modern-cmake.html