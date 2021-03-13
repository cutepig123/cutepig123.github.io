[TOC]

------



# CMake使用教程(一)

`CMake` 是一种跨平台的免费开源软件工具，用于使用与编译器无关的方法来管理软件的构建过程。在 `Android Studio` 上进行 `NDK` 开发默认就是使用 `CMake` 管理 `C/C++` 代码，因此在学习 `NDK` 之前最好对 `CMake` 有一定的了解。

本文主要以翻译 `CMake` 的[官方教程文档](https://cmake.org/cmake/help/v3.16/guide/tutorial/index.html)为主，加上自己的一些理解，该教程涵盖了 `CMake` 的常见使用场景。由于能力有限，翻译部分采用机翻+人工校对，翻译有问题的地方，说声抱歉。

开发环境：

- macOS 10.14.6
- CMake 3.15.1
- CLion 2018.2.4

## 基础项目

[示例程序地址](https://github.com/TaylorKunZhang/cmake-tutorial/tree/master/base-demo)

最基础的项目是单个源代码文件构建的可执行文件。

本示例提供的源代码文件是 `tutorial.cxx`，可用于计算数字的平方根。代码如下：

```
// A simple program that computes the square root of a number
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <string>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        std::cout << "Usage: " << argv[0] << " number" << std::endl;
        return 1;
    }

    // convert input to double
    const double inputValue = atof(argv[1]);

    // calculate square root
    const double outputValue = sqrt(inputValue);
    std::cout << "The square root of " << inputValue << " is " << outputValue
              << std::endl;
    return 0;
}
复制代码
```

对于简单的项目，只需三行内容的 `CMakeLists.txt` 文件，这将是本教程的起点。在项目根目录下创建一个 `CMakeLists.txt` 文件，其内容如下：

```
# 设置运行此配置文件所需的CMake最低版本
cmake_minimum_required(VERSION 3.15)

# set the project name
# 设置项目名称
project(Tutorial)

# add the executable
# 添加一个可执行文件
add_executable(Tutorial tutorial.cxx)
复制代码
```

> 请注意，此示例在 `CMakeLists.txt` 文件中使用小写命令。`CMake` 支持大写，小写和大小写混合命令。

当前项目结构如下：

```
.
├── CMakeLists.txt
└── tutorial.cxx
复制代码
```

在项目根目录运行命令生成编译中间文件以及 `makefile` 文件：

```
cmake .
复制代码
```

命令执行后会在项目根目录下生成文件，项目结构如下：

```
.
├── CMakeCache.txt
├── CMakeFiles
├── CMakeLists.txt
├── Makefile
├── cmake_install.cmake
└── tutorial.cxx
复制代码
```

这样源文件和生成的文件都混在一起，不方便管理，建议使用一个专门的目录管理这些生成的文件。这里使用 `CLion` 默认生成文件目录 `cmake-build-debug`，在项目根目录运行编译命令并指定生成文件目录：

```
cmake -B cmake-build-debug
复制代码
```

项目结构如下：

```
.
├── CMakeLists.txt
├── cmake-build-debug
│   ├── CMakeCache.txt
│   ├── CMakeFiles
│   ├── Makefile
│   └── cmake_install.cmake
└── tutorial.cxx
复制代码
```

在项目根目录运行命令生成可执行文件：

```
cmake --build cmake-build-debug
复制代码
```

命令执行后生成了可执行文件 `Tutorial`，项目结构如下：

```
 .
 ├── CMakeLists.txt
 ├── cmake-build-debug
 │   ├── CMakeCache.txt
 │   ├── CMakeFiles
 │   ├── Makefile
+│   ├── Tutorial
 │   └── cmake_install.cmake
 └── tutorial.cxx
复制代码
```

在项目根目录运行生成的可执行文件且不携带参数：

```
./cmake-build-debug/Tutorial
复制代码
```

终端输出：

```
Usage: ./cmake-build-debug/Tutorial number
复制代码
```

在项目根目录运行生成的可执行文件并携带参数：

```
./cmake-build-debug/Tutorial 2
复制代码
```

终端输出：

```
The square root of 2 is 1.41421
复制代码
```

## 添加版本号和配置头文件

[示例程序地址](https://github.com/TaylorKunZhang/cmake-tutorial/tree/master/add-version-and-config-file)

我们添加的第一个功能是为我们的可执行文件和项目提供版本号。虽然我们可以仅在源代码中执行此操作，但是使用 `CMakeLists.txt` 可以提供更大的灵活性。

首先，修改 `CMakeLists.txt` 文件以设置版本号。

```
project(Tutorial VERSION 1.0)
复制代码
```

然后，配置头文件以将版本号传递给源代码：

```
# configure a header file to pass some of the CMake settings
# to the source code
# 配置头文件以将某些CMake设置传递给源代码
configure_file(TutorialConfig.h.in TutorialConfig.h)
复制代码
```

由于已配置的文件将被写入二进制目录，因此我们必须将该目录添加到路径列表中以搜索包含文件。将以下行添加到CMakeLists.txt文件的末尾：

```
# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
# 将二进制目录添加到包含文件的搜索路径中，以便我们找到TutorialConfig.h
target_include_directories(Tutorial PUBLIC
        "${PROJECT_BINARY_DIR}"
        )
复制代码
```

使用您喜欢的编辑器，在源目录中使用以下内容创建 `TutorialConfig.h.in`：

```
// the configured options and settings for Tutorial
// 教程的配置选项和设置
#define Tutorial_VERSION_MAJOR @Tutorial_VERSION_MAJOR@
#define Tutorial_VERSION_MINOR @Tutorial_VERSION_MINOR@
复制代码
```

当 `CMake` 配置此头文件时，会在二进制目录下生成一个文件 `TutorialConfig.h`，会把 `TutorialConfig.h.in` 中的内容拷贝到里面，只是把 `@Tutorial_VERSION_MAJOR@` 和 `@Tutorial_VERSION_MINOR@` 替换成在 `CMakeLists.txt` 的配置的 1 和 0。

这里的 1 和 0 是怎么和 `Tutorial_VERSION_MAJOR` 、`Tutorial_VERSION_MINOR`关联上的? 在 `project()` 中指定了 `VERSION` 后，`CMake` 会把版本信息存储在以下变量中：

- `PROJECT_VERSION`, `_VERSION`
- `PROJECT_VERSION_MAJOR`, `_VERSION_MAJOR`
- `PROJECT_VERSION_MINOR`, `_VERSION_MINOR`
- `PROJECT_VERSION_PATCH`, `_VERSION_PATCH`
- `PROJECT_VERSION_TWEAK`, `_VERSION_TWEAK`.

`MAJOR`、`MINOR`、`PATCH`、`TWEAK` 分别代表着版本号的四位，比如版本号 `1.2.3.4`，`MAJOR=1`、`MINOR=2`、`PATCH=3`、`TWEAK=4`。版本号不一定非得是4位，可以只有1位，只是最大为4位。

这里 `PROJECT-NAME` 值为 `Tutorial`，所以能从 `Tutorial_VERSION_MAJOR` 和 `Tutorial_VERSION_MINOR` 中读取到版本信息。

当从顶层 `CMakeLists.txt` 调用 `project()` 命令时，该版本也存储在变量 `CMAKE_PROJECT_VERSION` 中。

接下来，修改 `tutorial.cxx` 以包含配置的头文 `件TutorialConfig.h` 和打印出版本号，如下所示：

```
// A simple program that computes the square root of a number
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <string>

+ #include "TutorialConfig.h"

int main(int argc, char *argv[]) {
    if (argc < 2) {
+        // report version
+        std::cout << argv[0] << " Version " << Tutorial_VERSION_MAJOR << "."
+                  << Tutorial_VERSION_MINOR << std::endl;
        std::cout << "Usage: " << argv[0] << " number" << std::endl;
        return 1;
    }

    // convert input to double
    const double inputValue = atof(argv[1]);

    // calculate square root
    const double outputValue = sqrt(inputValue);
    std::cout << "The square root of " << inputValue << " is " << outputValue
              << std::endl;
    return 0;
}
复制代码
```

在项目根目录运行命令编译项目和生成可执行文件：

```
cmake -B cmake-build-debug
cmake --build cmake-build-debug
复制代码
```

在项目根目录运行生成的可执行文件且不携带参数：

```
./cmake-build-debug/Tutorial
复制代码
```

终端输出：

```
./cmake-build-debug/Tutorial Version 1.0
Usage: ./cmake-build-debug/Tutorial number
复制代码
```

## 指定C++标准

[示例程序地址](https://github.com/TaylorKunZhang/cmake-tutorial/tree/master/specify-standard)

在 `CMake` 中启用对特定 `C ++` 标准的支持的最简单方法是使用 `CMAKE_CXX_STANDARD` 变量。对于本教程，请将 `CMakeLists.txt` 文件中的 `CMAKE_CXX_STANDARD` 变量设置为11，并将 `CMAKE_CXX_STANDARD_REQUIRED` 设置为 `True`：

```
# specify the C++ standard
# 指定C ++标准
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)
复制代码
```

接下来，通过在 `tutorial.cxx` 中用 `std :: stod` 替换 `atof`，将一些 `C ++ 11` 功能添加到我们的项目中。同时，删除 `#include `。

```
// A simple program that computes the square root of a number
#include <cmath>
- #include <cstdlib>
#include <iostream>
#include <string>

#include "TutorialConfig.h"

int main(int argc, char *argv[]) {
    if (argc < 2) {
        // report version
        std::cout << argv[0] << " Version " << Tutorial_VERSION_MAJOR << "."
                  << Tutorial_VERSION_MINOR << std::endl;
        std::cout << "Usage: " << argv[0] << " number" << std::endl;
        return 1;
    }

    // convert input to double
-    const double inputValue = atof(argv[1]);
+    const double inputValue = std::stod(argv[1]);

    // calculate square root
    const double outputValue = sqrt(inputValue);
    std::cout << "The square root of " << inputValue << " is " << outputValue
              << std::endl;
    return 0;
}
复制代码
```

在项目根目录运行命令编译项目和生成可执行文件：

```
cmake -B cmake-build-debug
cmake --build cmake-build-debug
复制代码
```

在项目根目录运行生成的可执行文件：

```
./cmake-build-debug/Tutorial 2
复制代码
```

终端输出：

```
The square root of 2 is 1.41421
复制代码
```

## 添加库

[示例程序地址](https://github.com/TaylorKunZhang/cmake-tutorial/tree/master/add-library)

现在，我们将添加一个库到我们的项目中，该库用于计算数字的平方根，可执行文件可以使用此库，而不是使用编译器提供的标准平方根函数。该库有两个文件：

- `MathFunctions.h`

  ```
  double mysqrt(double x);
  复制代码
  ```

- `mysqrt.cxx`

  源文件有一个 `mysqrt` 的函数，该函数提供与编译器的 `sqrt` 函数类似的功能。

  ```
  #include <iostream>
  
  #include "MathFunctions.h"
  
  // a hack square root calculation using simple operations
  double mysqrt(double x) {
      if (x <= 0) {
          return 0;
      }
  
      double result = x;
  
      // do ten iterations
      for (int i = 0; i < 10; ++i) {
          if (result <= 0) {
              result = 0.1;
          }
          double delta = x - (result * result);
          result = result + 0.5 * delta / result;
          std::cout << "Computing sqrt of " << x << " to be " << result << std::endl;
      }
      return result;
  }
  复制代码
  ```

在项目根目录下创建一个文件夹 `MathFunctions` ，把该库放在其下，在其下创建一个 `CMakeLists.txt` 文件，内容如下：

```
add_library(MathFunctions mysqrt.cxx)
复制代码
```

为了使用新库，我们将在顶层 `CMakeLists.txt` 文件中添加 `add_subdirectory` 调用，以便构建该库。我们将新库添加到可执行文件，并将 `MathFunctions` 添加为包含目录，以便可以找到 `mqsqrt.h` 头文件。顶级 `CMakeLists.txt` 文件的最后几行现在应如下所示：

```
# add the MathFunctions library
# 添加 MathFunctions 库
add_subdirectory(MathFunctions)

# add the executable
# 添加一个可执行文件
add_executable(Tutorial tutorial.cxx)

target_link_libraries(Tutorial PUBLIC MathFunctions)

# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
# 将二进制目录添加到包含文件的搜索路径中，以便我们找到TutorialConfig.h
target_include_directories(Tutorial PUBLIC
        "${PROJECT_BINARY_DIR}"
        "${PROJECT_SOURCE_DIR}/MathFunctions"
        )
复制代码
```

修改 `tutorial.cxx` 使用引入的库，其内容如下：

```
// A simple program that computes the square root of a number
- #include <cmath>
#include <iostream>
#include <string>

#include "TutorialConfig.h"
+ #include "MathFunctions.h"

int main(int argc, char *argv[]) {
    if (argc < 2) {
        // report version
        std::cout << argv[0] << " Version " << Tutorial_VERSION_MAJOR << "."
                  << Tutorial_VERSION_MINOR << std::endl;
        std::cout << "Usage: " << argv[0] << " number" << std::endl;
        return 1;
    }

    // convert input to double
    const double inputValue = std::stod(argv[1]);

    // calculate square root
-    const double outputValue = sqrt(inputValue);
+    const double outputValue = mysqrt(inputValue);
    std::cout << "The square root of " << inputValue << " is " << outputValue
              << std::endl;
    return 0;
}
复制代码
```

在项目根目录运行命令编译项目和生成可执行文件：

```
cmake -B cmake-build-debug
cmake --build cmake-build-debug
复制代码
```

在项目根目录运行生成的可执行文件：

```
./cmake-build-debug/Tutorial 2
复制代码
```

终端输出：

```
Computing sqrt of 2 to be 1.5
Computing sqrt of 2 to be 1.41667
Computing sqrt of 2 to be 1.41422
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
The square root of 2 is 1.41421
复制代码
```

## 提供选项

[示例程序地址](https://github.com/TaylorKunZhang/cmake-tutorial/tree/master/provide-option)

现在让我们将 `MathFunctions` 库设为可选。虽然对于本教程而言确实不需要这样做，但是对于大型项目来说，这是很常见的。第一步是向顶级 `CMakeLists.txt` 文件添加一个选项：

```
# should we use our own math functions
# 我们应该使用自己的数学函数吗
option(USE_MYMATH "Use tutorial provided math implementation" ON)
复制代码
```

此选项将显示在 `CMake GUI` 和 `ccmake` 中，默认值ON可由用户更改。此设置将存储在缓存中，因此用户无需在每次在构建目录上运行CMake时都设置该值。

下一个是使建立和链接 `MathFunctions` 库成为条件。为此，我们将顶级 `CMakeLists.txt` 文件的结尾更改为如下所示：

```
# add the MathFunctions library
# 添加 MathFunctions 库
if (USE_MYMATH)
    add_subdirectory(MathFunctions)
    list(APPEND EXTRA_LIBS MathFunctions)
    list(APPEND EXTRA_INCLUDES "${PROJECT_SOURCE_DIR}/MathFunctions")
endif ()

# add the executable
# 添加一个可执行文件
add_executable(Tutorial tutorial.cxx)

target_link_libraries(Tutorial PUBLIC ${EXTRA_LIBS})

# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
# 将二进制目录添加到包含文件的搜索路径中，以便我们找到TutorialConfig.h
target_include_directories(Tutorial PUBLIC
        "${PROJECT_BINARY_DIR}"
        ${EXTRA_INCLUDES}
        )
复制代码
```

> 请注意，这里使用变量 `EXTRA_LIBS` 来收集所有可选库，以供以后链接到可执行文件中。变量 `EXTRA_INCLUDES` 类似地用于可选的头文件。当处理许多可选组件时，这是一种经典方法，我们将在下一步中介绍现代方法。

对源代码的相应更改非常简单。首先，根据需要在 `tutorial.cxx` 中决定包含 `MathFunctions` 头还是 包含 ``：

```
// should we include the MathFunctions header?
#ifdef USE_MYMATH
#include "MathFunctions.h"
#else
#include <cmath>
#endif
复制代码
```

然后，在同一文件中，使用 `USE_MYMATH` 来确定使用哪个平方根函数：

```
#ifdef USE_MYMATH
  const double outputValue = mysqrt(inputValue);
#else
  const double outputValue = sqrt(inputValue);
#endif
复制代码
```

由于源代码现在需要 `USE_MYMATH`，因此可以使用以下行将其添加到 `TutorialConfig.h.in` 中：

```
#cmakedefine USE_MYMATH
复制代码
```

在 [download](https://cmake.org/download/) 上根据自己的平台下载对应版本的 `cmake-gui`，安装后打开软件，选择源代码目录和生成文件，如下图所示：



![img](CMake%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B(%E4%BA%8C).assets/16e82bb22bd38459)



点击左下角 `Generate` 按钮，软件会弹出的选择项目生成器的弹窗，这里默认就好，点击点击 `Done` 按钮，`cmake-gui` 开始编译项目，生成中间文件，并且可以在软件看到我们为用户提供的选项：



![img](CMake%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B(%E4%BA%8C).assets/16e82bb5dd4a7617)



这个时候 `cmake-build-debug/TutorialConfig.h` 的内容如下：

```
// the configured options and settings for Tutorial
// 教程的配置选项和设置
#define Tutorial_VERSION_MAJOR 1
#define Tutorial_VERSION_MINOR 0
#define USE_MYMATH
复制代码
```

在项目根目录运行命令生成可执行文件：

```
cmake --build cmake-build-debug
复制代码
```

在项目根目录运行生成的可执行文件：

```
./cmake-build-debug/Tutorial 2
复制代码
```

终端输出：

```
Computing sqrt of 2 to be 1.5
Computing sqrt of 2 to be 1.41667
Computing sqrt of 2 to be 1.41422
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
The square root of 2 is 1.41421
复制代码
```

取消 `cmake-gui` 中的 `USE_MYMATH` 的勾选，点击 `Generate` 按钮重新编译项目，这个时候 `cmake-build-debug/TutorialConfig.h` 的内容如下：

```
// the configured options and settings for Tutorial
// 教程的配置选项和设置
#define Tutorial_VERSION_MAJOR 1
#define Tutorial_VERSION_MINOR 0
/* #undef USE_MYMATH */
复制代码
```

在项目根目录运行命令生成可执行文件：

```
cmake --build cmake-build-debug
复制代码
```

在项目根目录运行生成的可执行文件：

```
./cmake-build-debug/Tutorial 2
复制代码
```

终端输出：

```
The square root of 2 is 1.41421
复制代码
```

## CMake使用教程系列文章

- CMake使用教程(一)
  - 基础项目
  - 添加版本号和配置头文件
  - 指定C++标准
  - 添加库
  - 提供选项
- CMake使用教程(二)
  - 添加“库”的使用要求
  - 安装
  - 测试
  - 系统自检
- CMake使用教程(三)
  - 指定编译定义
  - 添加自定义命令和生成的文件
  - 生成安装程序
  - 添加对仪表板的支持
- CMake使用教程(四)
  - 混合静态和共享
  - 添加生成器表达式
  - 添加导出配置

关注下面的标签，发现更多相似文章

# CMake使用教程(二)

`CMake` 是一种跨平台的免费开源软件工具，用于使用与编译器无关的方法来管理软件的构建过程。在 `Android Studio` 上进行 `NDK` 开发默认就是使用 `CMake` 管理 `C/C++` 代码，因此在学习 `NDK` 之前最好对 `CMake` 有一定的了解。

本文主要以翻译 `CMake` 的[官方教程文档](https://cmake.org/cmake/help/v3.16/guide/tutorial/index.html)为主，加上自己的一些理解，该教程涵盖了 `CMake` 的常见使用场景。由于能力有限，翻译部分采用机翻+人工校对，翻译有问题的地方，说声抱歉。

开发环境：

- macOS 10.14.6
- CMake 3.15.1
- CLion 2018.2.4

## 添加“库”的使用要求

[示例程序地址](https://github.com/TaylorKunZhang/cmake-tutorial/tree/master/add-usage-requirements-for-library)

使用要求可以更好地控制库或可执行文件的链接和包含行，同时还可以更好地控制 `CMake` 内部目标的传递属性。利用使用要求的主要命令是：

- `target_compile_definitions`

  给指定目标添加编译定义。

- `target_compile_options`

  给指定目标添加编译选项。

- `target_include_directories`

  给指定目标添加包含目录。

- `target_link_libraries`

  指定链接给定目标或其依赖项时要使用的库或标志。

控制 `CMake` 内部目标的传递属性有三种类型：

- `PRIVATE`

  属性只应用到本目标，不应用到链接本目标的目标。即生产者需要，消费者不需要。

- `PUBLIC`

  属性既应用到本目标也应用到链接目标的目标。即生产者和消费者都需要。

- `INTERFACE`

  属性不应用到本目标，应用到链接本目标的目标。即生产者不需要，消费者需要。

让我们重构代码“提供选项”项目的代码，以使用现代 `CMake` 的使用要求方法。我们首先声明，链接到 `MathFunctions` 的任何人都需要包含当前源目录，而 `MathFunctions` 本身不需要。因此，这里使用 `INTERFACE`。

将以下行添加到 `MathFunctions/CMakeLists.txt` 的末尾：

```
# state that anybody linking to us needs to include the current source dir
# to find MathFunctions.h, while we don't.
# 说明与我们链接的任何人都需要包含当前源目录才能找到 MathFunctions.h，而我们不需要。
target_include_directories(MathFunctions
        INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
        )
复制代码
```

现在，我们已经指定了 `MathFunction` 的使用要求，我们可以安全地从顶级 `CMakeLists.txt` 中删除对 `EXTRA_INCLUDES`变量的使用：

```
if(USE_MYMATH)
  add_subdirectory(MathFunctions)
  list(APPEND EXTRA_LIBS MathFunctions)
endif()

target_include_directories(Tutorial PUBLIC
        "${PROJECT_BINARY_DIR}"
        )
复制代码
```

在项目根目录运行命令编译项目和生成可执行文件：

```
cmake -B cmake-build-debug
cmake --build cmake-build-debug
复制代码
```

在项目根目录运行生成的可执行文件：

```
./cmake-build-debug/Tutorial 2
复制代码
```

终端输出：

```
Computing sqrt of 2 to be 1.5
Computing sqrt of 2 to be 1.41667
Computing sqrt of 2 to be 1.41422
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
The square root of 2 is 1.41421
复制代码
```

## 安装

[示例程序地址](https://github.com/TaylorKunZhang/cmake-tutorial/tree/master/cmake-install)

安装规则非常简单：对于 `MathFunctions` ，我们要安装库和头文件，对于应用程序，我们要安装可执行文件和配置的头文件。

因此，在 `MathFunctions/CMakeLists.txt` 的末尾添加：

```
# install rules
# 安装规则
install(TARGETS MathFunctions DESTINATION lib)
install(FILES MathFunctions.h DESTINATION include)
复制代码
```

并在顶级 `CMakeLists.txt` 的末尾添加：

```
# add the install targets
# 添加安装规则
install(TARGETS Tutorial DESTINATION bin)
install(FILES "${PROJECT_BINARY_DIR}/TutorialConfig.h"
        DESTINATION include
        )
复制代码
```

这就是本地安装所需的全部。

在项目根目录运行命令编译项目和生成可执行文件：

```
cmake -B cmake-build-debug
cmake --build cmake-build-debug
复制代码
```

在项目根目录运行命令安装可执行文件：

```
 cmake --install cmake-build-debug
复制代码
```

> `CMake` 从3.15开始使用 `cmake --install` 安装文件。`CMake` 变量 `CMAKE_INSTALL_PREFIX` 用于确定文件的安装根目录。如果使用 `cmake --install`，则可以通过 `--prefix` 参数指定自定义安装目录。对于多配置工具，请使用 `--config` 参数指定配置。

终端输出：

```
-- Install configuration: ""
-- Installing: /usr/local/lib/libMathFunctions.a
-- Installing: /usr/local/include/MathFunctions.h
-- Installing: /usr/local/bin/Tutorial
-- Installing: /usr/local/include/TutorialConfig.h
复制代码
```

在项目根目录执行命令：

```
Tutorial 2
复制代码
```

终端输出：

```
Computing sqrt of 2 to be 1.5
Computing sqrt of 2 to be 1.41667
Computing sqrt of 2 to be 1.41422
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
The square root of 2 is 1.41421
复制代码
```

这个时候我们调用的不是 `cmake-build-debug` 下的 `Tutorial` 文件，而是安装到 `/usr/local/bin` 目录下的 `Tutorial` 文件。我们可以通过命令查看一下 `Tutorial` 的位置：

```
where Tutorial
复制代码
```

终端输出：

```
/usr/local/bin/Tutorial
复制代码
```

## 测试

[示例程序地址](https://github.com/TaylorKunZhang/cmake-tutorial/tree/master/cmake-test)

接下来，测试我们的应用程序。在顶级 `CMakeLists` 文件的末尾，我们可以启用测试，然后添加一些基本测试以验证应用程序是否正常运行。

```
# enable testing
# 启用测试
enable_testing()

# does the application run
# 测试应用程序是否运行
add_test(NAME Runs COMMAND Tutorial 25)

# does the usage message work?
# 测试消息是否工作？
add_test(NAME Usage COMMAND Tutorial)
set_tests_properties(Usage
        PROPERTIES PASS_REGULAR_EXPRESSION "Usage:.*number"
        )

# define a function to simplify adding tests
# 定义一个函数以简化添加测试
function(do_test target arg result)
    add_test(NAME Comp${arg} COMMAND ${target} ${arg})
    set_tests_properties(Comp${arg}
            PROPERTIES PASS_REGULAR_EXPRESSION ${result}
            )
endfunction(do_test)

# do a bunch of result based tests
# 做一堆基于结果的测试
do_test(Tutorial 4 "4 is 2")
do_test(Tutorial 9 "9 is 3")
do_test(Tutorial 5 "5 is 2.236")
do_test(Tutorial 7 "7 is 2.645")
do_test(Tutorial 25 "25 is 5")
do_test(Tutorial -25 "-25 is [-nan|nan|0]")
do_test(Tutorial 0.0001 "0.0001 is 0.01")
复制代码
```

第一个测试只是验证应用程序正在运行，没有段错误或其他崩溃，并且返回值为零。这是 `CTest` 测试的基本形式。

下一个测试使用 `PASS_REGULAR_EXPRESSION` 测试属性来验证测试的输出是否包含某些字符串。在这种情况下，验证在提供了错误数量的参数时是否打印了用法消息。

最后，我们有一个名为 `do_test` 的函数，该函数运行应用程序并验证所计算的平方根对于给定输入是否正确。对于 `do_test` 的每次调用，都会基于传递的参数将另一个测试添加到项目中，该测试具有名称，输入和预期结果。

在项目根目录运行命令编译项目和生成可执行文件：

```
cmake -B cmake-build-debug
cmake --build cmake-build-debug
复制代码
```

在项目根目录运行命令测试应用程序：

```
cd cmake-build-debug
ctest
复制代码
```

终端输出：

```
Test project /Users/taylor/Project/Taylor/C/Study/cmake-tutorial/cmake-test/cmake-build-debug
    Start 1: Runs
1/9 Test #1: Runs .............................   Passed    0.00 sec
    Start 2: Usage
2/9 Test #2: Usage ............................   Passed    0.00 sec
    Start 3: Comp4
3/9 Test #3: Comp4 ............................   Passed    0.00 sec
    Start 4: Comp9
4/9 Test #4: Comp9 ............................   Passed    0.00 sec
    Start 5: Comp5
5/9 Test #5: Comp5 ............................   Passed    0.00 sec
    Start 6: Comp7
6/9 Test #6: Comp7 ............................   Passed    0.00 sec
    Start 7: Comp25
7/9 Test #7: Comp25 ...........................   Passed    0.00 sec
    Start 8: Comp-25
8/9 Test #8: Comp-25 ..........................   Passed    0.00 sec
    Start 9: Comp0.0001
9/9 Test #9: Comp0.0001 .......................   Passed    0.00 sec

100% tests passed, 0 tests failed out of 9

Total Test time (real) =   0.03 sec
复制代码
```

## 系统自检

[示例程序地址](https://github.com/TaylorKunZhang/cmake-tutorial/tree/master/system-introspection)

让我们考虑向我们的项目中添加一些代码，这些代码取决于目标平台可能不具备的功能。

对于此示例，我们将添加一些代码，具体取决于目标平台是否具有 `log` 和 `exp` 函数。当然，几乎每个平台都具有这些功能，但对于本教程而言，假定它们并不常见。

如果平台具有 `log` 和 `exp` ，那么我们将使用它们来计算 `mysqrt` 函数中的平方根。我们首先在顶级 `CMakeList` 中使用 `CheckSymbolExists.cmake` 宏测试这些功能的可用性。

```
# does this system provide the log and exp functions?
# 该系统是否提供log和exp函数？
include(CheckSymbolExists)
set(CMAKE_REQUIRED_LIBRARIES "m")
check_symbol_exists(log "math.h" HAVE_LOG)
check_symbol_exists(exp "math.h" HAVE_EXP)
复制代码
```

在 `TutorialConfig.h` 的 `configure_file` 命令之前完成对 `log` 和 `exp` 的测试非常重要，`configure_file` 命令使用 `CMake` 中的当前设置立即配置文件，所以 `check_symbol_exists` 命令应该放在 `configure_file` 之前。

现在，将这些定义添加到 `TutorialConfig.h.in` 中，以便我们可以从 `mysqrt.cxx`中使用它们：

```
// does the platform provide exp and log functions?
// 平台是否提供log和exp函数？
#cmakedefine HAVE_LOG
#cmakedefine HAVE_EXP
复制代码
```

更新 `MathFunctions/CMakeLists.txt` 文件，以便 `mysqrt.cxx`知道此文件的位置：

```
target_include_directories(MathFunctions
          INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
          PRIVATE ${CMAKE_BINARY_DIR}
          )
复制代码
```

修改 `mysqrt.cxx` 以包含 `cmath` 和 `TutorialConfig.h`。接下来，在 `mysqrt`函数的同一文件中，我们可以使用以下代码（如果在系统上可用）提供基于 `log` 和 `exp` 的替代实现（在返回结果前不要忘记 `#endif` ！）：

我们将在 `TutorialConfig.h.in` 中使用新定义，因此请确保在配置该文件之前进行设置。

```
#if defined(HAVE_LOG) && defined(HAVE_EXP)
    double result = exp(log(x) * 0.5);
    std::cout << "Computing sqrt of " << x << " to be " << result
              << " using log and exp" << std::endl;
#else
    double result = x;
    // do ten iterations
    for (int i = 0; i < 10; ++i) {
        if (result <= 0) {
            result = 0.1;
        }
        double delta = x - (result * result);
        result = result + 0.5 * delta / result;
        std::cout << "Computing sqrt of " << x << " to be " << result << std::endl;
    }
#endif
复制代码
```

在项目根目录运行命令编译项目和生成可执行文件：

```
cmake -B cmake-build-debug
cmake --build cmake-build-debug
复制代码
```

在项目根目录运行生成的可执行文件：

```
./cmake-build-debug/Tutorial 2
复制代码
```

终端输出：

```
Computing sqrt of 2 to be 1.41421 using log and exp
The square root of 2 is 1.41421
复制代码
```

## CMake使用教程系列文章

- CMake使用教程(一)
  - 基础项目
  - 添加版本号和配置头文件
  - 指定C++标准
  - 添加库
  - 提供选项
- CMake使用教程(二)
  - 添加“库”的使用要求
  - 安装
  - 测试
  - 系统自检
- CMake使用教程(三)
  - 指定编译定义
  - 添加自定义命令和生成的文件
  - 生成安装程序
  - 添加对仪表板的支持
- CMake使用教程(四)
  - 混合静态和共享
  - 添加生成器表达式
  - 添加导出配置

关注下面的标签，发现更多相似文章

# CMake使用教程(三)

`CMake` 是一种跨平台的免费开源软件工具，用于使用与编译器无关的方法来管理软件的构建过程。在 `Android Studio` 上进行 `NDK` 开发默认就是使用 `CMake` 管理 `C/C++` 代码，因此在学习 `NDK` 之前最好对 `CMake` 有一定的了解。

本文主要以翻译 `CMake` 的[官方教程文档](https://cmake.org/cmake/help/v3.16/guide/tutorial/index.html)为主，加上自己的一些理解，该教程涵盖了 `CMake` 的常见使用场景。由于能力有限，翻译部分采用机翻+人工校对，翻译有问题的地方，说声抱歉。

开发环境：

- macOS 10.14.6
- CMake 3.15.1
- CLion 2018.2.4

## 指定编译定义

[示例程序地址](https://github.com/TaylorKunZhang/cmake-tutorial/tree/master/specify-compile-definition)

在上一步 “系统自检” 中，除了在 `TutorialConfig.h` 中保存 `HAVE_LOG` 和 `HAVE_EXP` 值之外，还有更好的做法吗？对于此示例，我们将尝试使用 `target_compile_definitions`。

首先，从 `TutorialConfig.h.in` 中删除上一步的定义，在 `mysqrt.cxx` 中不再包含 `TutorialConfig.h`，移除上一步在 `MathFunctions/CMakeLists.txt` 中增加的额外包含。

接下来，我们可以将 `HAVE_LOG` 和 `HAVE_EXP` 的检查移至 `MathFunctions/CMakeLists.txt`，然后添加将这些值指定为 `PRIVATE` 编译定义。

```
# does this system provide the log and exp functions?
# 该系统是否提供log和exp函数？
include(CheckSymbolExists)
set(CMAKE_REQUIRED_LIBRARIES "m")
check_symbol_exists(log "math.h" HAVE_LOG)
check_symbol_exists(exp "math.h" HAVE_EXP)

if(HAVE_LOG AND HAVE_EXP)
  target_compile_definitions(MathFunctions
                             PRIVATE "HAVE_LOG" "HAVE_EXP")
endif()
复制代码
```

完成这些更新后，在项目根目录运行命令编译项目和生成可执行文件：

```
cmake -B cmake-build-debug
cmake --build cmake-build-debug
复制代码
```

在项目根目录运行生成的可执行文件：

```
./cmake-build-debug/Tutorial 2
复制代码
```

终端输出：

```
Computing sqrt of 2 to be 1.41421 using log and exp
The square root of 2 is 1.41421
复制代码
```

## 添加自定义命令和生成的文件

[示例程序地址](https://github.com/TaylorKunZhang/cmake-tutorial/tree/master/custom-command-and-generated-file)

假设，出于本教程的目的，我们决定不再使用平台日志和exp函数，而是希望生成一个可在 `mysqrt` 函数中使用的预计算值表。在本节中，我们将在构建过程中创建表，然后将该表编译到我们的应用程序中。

首先，让我们取消对 `MathFunctions/CMakeLists.txt` 中的 `log`和 `exp` 函数的检查。然后从 `mysqrt.cxx` 中删除对 `HAVE_LOG` 和 `HAVE_EXP` 的检查。同时，我们可以删除 `#include `。

在 `MathFunctions` 子目录中，提供了一个名为 `MakeTable.cxx` 的新源文件来生成表。

```
// A simple program that builds a sqrt table
#include <cmath>
#include <fstream>
#include <iostream>

int main(int argc, char *argv[]) {
    // make sure we have enough arguments
    if (argc < 2) {
        return 1;
    }

    std::ofstream fout(argv[1], std::ios_base::out);
    const bool fileOpen = fout.is_open();
    if (fileOpen) {
        fout << "double sqrtTable[] = {" << std::endl;
        for (int i = 0; i < 10; ++i) {
            fout << sqrt(static_cast<double>(i)) << "," << std::endl;
        }
        // close the table with a zero
        fout << "0};" << std::endl;
        fout.close();
    }
    return fileOpen ? 0 : 1; // return 0 if wrote the file
}
复制代码
```

我们可以看到生成的表不是简单的文本，而是一段C++代码。并且该文件的文件名是由参数传入决定的。

下一步是将适当的命令添加到 `MathFunctions/CMakeLists.txt` 文件中，以构建`MakeTable` 可执行文件，然后在构建过程中运行它。需要一些命令来完成此操作。

首先，在 `MathFunctions/CMakeLists.txt` 的顶部，添加 `MakeTable` 的可执行文件，就像添加任何其他可执行文件一样。

```
# first we add the executable that generates the table
# 首先，我们添加生成表的可执行文件
add_executable(MakeTable MakeTable.cxx)
复制代码
```

然后，我们添加一个自定义命令，该命令指定如何通过运行 `MakeTable` 来产生 `Table.h`。

```
# add the command to generate the source code
# 添加命令以生成源代码
add_custom_command(
        OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/Table.h
        COMMAND MakeTable ${CMAKE_CURRENT_BINARY_DIR}/Table.h
        DEPENDS MakeTable
)
复制代码
```

接下来，我们必须让 `CMake` 知道 `mysqrt.cxx` 依赖生成的文件 `Table.h`。这是通过将生成的 `Table.h` 添加到库 `MathFunctions` 的源列表中来完成的。

```
# add the main library
# 添加主库
add_library(MathFunctions
        mysqrt.cxx
        ${CMAKE_CURRENT_BINARY_DIR}/Table.h
        )
复制代码
```

我们还必须将当前的二进制目录添加到包含目录列表中，以便 `mysqrt.cxx` 可以找到并包含 `Table.h` 。

```
# state that anybody linking to us needs to include the current source dir
# to find MathFunctions.h, while we don't.
# 说明与我们链接的任何人都需要包含当前源目录才能找到 MathFunctions.h，而我们不需要。
# state that we depend on Tutorial_BINARY_DIR but consumers don't, as the
# Table.h include is an implementation detail
# state that we depend on our binary dir to find Table.h
# 声明我们依赖Tutorial_BINARY_DIR但消费者不依赖，因为包含Table.h是一个实现细节，我们依赖二进制目录来查找Table.h
target_include_directories(MathFunctions
        INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
        PRIVATE ${CMAKE_CURRENT_BINARY_DIR}
        )
复制代码
```

现在，使用生成的表。首先，修改 `mysqrt.cxx` 以包含 `Table.h` 。接下来，我们可以重写 `mysqrt` 函数以使用该表：

```
double mysqrt(double x) {
    if (x <= 0) {
        return 0;
    }

    double result = x;
    if (x >= 1 && x < 10) {
        std::cout << "Use the table to help find an initial value " << std::endl;
        result = sqrtTable[static_cast<int>(x)];
    }

    // do ten iterations
    for (int i = 0; i < 10; ++i) {
        if (result <= 0) {
            result = 0.1;
        }
        double delta = x - (result * result);
        result = result + 0.5 * delta / result;
        std::cout << "Computing sqrt of " << x << " to be " << result << std::endl;
    }
    return result;
}
复制代码
```

在项目根目录运行命令编译项目和生成可执行文件：

```
cmake -B cmake-build-debug
cmake --build cmake-build-debug
复制代码
```

在项目根目录运行生成的可执行文件：

```
./cmake-build-debug/Tutorial 2
复制代码
```

终端输出：

```
Use the table to help find an initial value 
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
The square root of 2 is 1.41421
复制代码
```

在项目根目录运行生成的可执行文件：

```
./cmake-build-debug/Tutorial 12
复制代码
```

终端输出：

```
Computing sqrt of 12 to be 6.5
Computing sqrt of 12 to be 4.17308
Computing sqrt of 12 to be 3.52433
Computing sqrt of 12 to be 3.46462
Computing sqrt of 12 to be 3.4641
Computing sqrt of 12 to be 3.4641
Computing sqrt of 12 to be 3.4641
Computing sqrt of 12 to be 3.4641
Computing sqrt of 12 to be 3.4641
Computing sqrt of 12 to be 3.4641
The square root of 12 is 3.4641
复制代码
```

## 生成安装程序

[示例程序地址](https://github.com/TaylorKunZhang/cmake-tutorial/tree/master/build-installer)

接下来，假设我们想将项目分发给其他人，以便他们可以使用它。我们希望在各种平台上提供二进制和源代码分发。这与我们之前在 “安装” 示例进行的安装有些不同，在之前安装中，我们根据源代码构建的二进制文件进行安装。

在此示例中，我们将构建支持二进制安装和程序包管理功能的安装程序包。为此，我们将使用 `CPack` 创建平台特定的安装程序。具体来说，我们需要在顶级 `CMakeLists.txt` 文件的底部添加几行。

```
# setup installer
# 设置安装程序
include(InstallRequiredSystemLibraries)
set(CPACK_RESOURCE_FILE_LICENSE "${CMAKE_CURRENT_SOURCE_DIR}/License.txt")
set(CPACK_PACKAGE_VERSION_MAJOR "${Tutorial_VERSION_MAJOR}")
set(CPACK_PACKAGE_VERSION_MINOR "${Tutorial_VERSION_MINOR}")
include(CPack)
复制代码
```

这就是全部，我们首先包含 `InstallRequiredSystemLibraries`，该模块将包含项目在当前平台所需的任何运行时库。

接下来，我们将一些项目信息设置给 `CPack` 变量，比如项目的许可证和版本信息。本示例中 `License.txt` 内容如下：

```
This is a License file.
复制代码
```

最后，我们包含 `CPack` 模块，该模块将使用这些变量和当前系统的其他一些属性来设置安装程序。

在项目根目录运行命令编译项目：

```
cmake -B cmake-build-debug
复制代码
```

在项目根目录运行命令**构建二进制发行版**：

```
cd cmake-build-debug
cpack
复制代码
```

在项目根目录下生成了文件：

```
.
├── ...
├── Tutorial-1.0-Darwin.sh
├── Tutorial-1.0-Darwin.tar.gz
└── ...
复制代码
```

**注意**：要指定生成器，请使用 `-G` 选项。对于多配置构建，请使用 `-C` 指定配置。例如：

```
cpack -G ZIP -C Debug
复制代码
```

在项目根目录运行命令**构建源代码分发**：

```
cd cmake-build-debug
cpack --config CPackSourceConfig.cmake
复制代码
```

在项目根目录下生成了文件：

```
.
├── ...
├── Tutorial-1.0-Source.tar.Z
├── Tutorial-1.0-Source.tar.bz2
├── Tutorial-1.0-Source.tar.gz
├── Tutorial-1.0-Source.tar.xz
└── ...
复制代码
```

## 添加对仪表板的支持

[示例程序地址](https://github.com/TaylorKunZhang/cmake-tutorial/tree/master/support-dashboard)

我们已经在 "测试" 示例中为我们的项目定义了许多测试。现在，我们只需要运行这些测试并将其提交到仪表板即可。为了包括对仪表板的支持，我们在顶层 `CMakeLists.txt` 中包含了 `CTest` 模块。

将以下内容：

```
# enable testing
# 启用测试
enable_testing()
复制代码
```

替换为：

```
# enable dashboard scripting
# 启用仪表板脚本
include(CTest)
复制代码
```

`CTest` 模块将自动调用 `enable_testing()`，因此我们可以将其从 `CMake` 文件中删除。我们还需要在顶级目录中创建一个 `CTestConfig.cmake` 文件，在该文件中我们可以指定项目的名称以及提交仪表板的位置。

```
set(CTEST_PROJECT_NAME "CMakeTutorial")
set(CTEST_NIGHTLY_START_TIME "00:00:00 EST")

set(CTEST_DROP_METHOD "http")
set(CTEST_DROP_SITE "my.cdash.org")
set(CTEST_DROP_LOCATION "/submit.php?project=CMakeTutorial")
set(CTEST_DROP_SITE_CDASH TRUE)
复制代码
```

`CTest` 将在运行时读入该文件。

在项目根目录运行命令编译项目：

```
cmake -B cmake-build-debug
复制代码
```

在项目根目录运行命令生成仪表板：

```
cd cmake-build-debug
ctest –D Experimental
# 或者：ctest -VV –D Experimental
复制代码
```

**注意**：对于多配置生成器（例如Visual Studio），必须指定配置类型：

```
ctest [-VV] -C Debug –D Experimental
复制代码
```

或者从 `IDE中` 构建 `Experimental` 目标。

`ctest` 将构建和测试项目，并将结果提交给Kitware公共仪表板。仪表板的结果将被上传到Kitware的公共仪表板：[my.cdash.org/index.php?p…](https://my.cdash.org/index.php?project=CMakeTutorial)，如下图所示：



![img](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="1280" height="240"></svg>)



## CMake使用教程系列文章

- CMake使用教程(一)
  - 基础项目
  - 添加版本号和配置头文件
  - 指定C++标准
  - 添加库
  - 提供选项
- CMake使用教程(二)
  - 添加“库”的使用要求
  - 安装
  - 测试
  - 系统自检
- CMake使用教程(三)
  - 指定编译定义
  - 添加自定义命令和生成的文件
  - 生成安装程序
  - 添加对仪表板的支持
- CMake使用教程(四)
  - 混合静态和共享
  - 添加生成器表达式
  - 添加导出配置

关注下面的标签，发现更多相似文章

# CMake使用教程(四)

`CMake` 是一种跨平台的免费开源软件工具，用于使用与编译器无关的方法来管理软件的构建过程。在 `Android Studio` 上进行 `NDK` 开发默认就是使用 `CMake` 管理 `C/C++` 代码，因此在学习 `NDK` 之前最好对 `CMake` 有一定的了解。

本文主要以翻译 `CMake` 的[官方教程文档](https://cmake.org/cmake/help/v3.16/guide/tutorial/index.html)为主，加上自己的一些理解，该教程涵盖了 `CMake` 的常见使用场景。由于能力有限，翻译部分采用机翻+人工校对，翻译有问题的地方，说声抱歉。

开发环境：

- macOS 10.14.6
- CMake 3.15.1
- CLion 2018.2.4

## 混合静态和共享

[示例程序地址](https://github.com/TaylorKunZhang/cmake-tutorial/tree/master/mixing-static-and-shared)

在本节中，我们将展示如何使用 `BUILD_SHARED_LIBS` 变量来控制 `add_library` 的默认行为，并允许控制构建没有显式类型 `(STATIC/SHARED/MODULE/OBJECT)` 的库。

为此，我们需要将 `BUILD_SHARED_LIBS` 添加到顶级 `CMakeLists.txt`。我们使用 `option` 命令，因为它允许用户有选择地选择该值是 `On` 还是 `Off`。

接下来，我们将重构 `MathFunctions` 使其成为使用 `mysqrt` 或 `sqrt` 封装的真实库，而不是要求调用代码执行此逻辑。这也意味着 `USE_MYMATH` 将不会控制构建 `MathFuctions`，而是将控制此库的行为。

第一步是将顶级 `CMakeLists.txt` 的开始部分更新为：

```
# 设置运行此配置文件所需的CMake最低版本
cmake_minimum_required(VERSION 3.15)

# set the project name and version
# 设置项目名称和版本
project(Tutorial VERSION 1.0)

# specify the C++ standard
# 指定C ++标准
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# control where the static and shared libraries are built so that on windows
# we don't need to tinker with the path to run the executable
# 控制静态和共享库的构建位置，以便在Windows上我们无需修改运行可执行文件的路径
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}")

option(BUILD_SHARED_LIBS "Build using shared libraries" ON)

# configure a header file to pass the version number only
# 配置头文件且仅传递版本号
configure_file(TutorialConfig.h.in TutorialConfig.h)

# add the MathFunctions library
# 添加MathFunctions库
add_subdirectory(MathFunctions)

# add the executable
# 添加一个可执行文件
add_executable(Tutorial tutorial.cxx)
target_link_libraries(Tutorial PUBLIC MathFunctions)

# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
# 将二进制目录添加到包含文件的搜索路径中，以便我们找到TutorialConfig.h
target_include_directories(Tutorial PUBLIC
        "${PROJECT_BINARY_DIR}"
        )
复制代码
```

现在我们将始终使用 `MathFunctions` 库，我们需要更新该库的逻辑。因此，在 `MathFunctions/CMakeLists.txt` 中，我们需要创建一个 `SqrtLibrary` ，当启用 `USE_MYMATH` 时有条件地对其进行构建。现在，由于这是一个教程，我们将明确要求 `SqrtLibrary` 是静态构建的。

最终结果是 `MathFunctions/CMakeLists.txt` 应该如下所示：

```
# add the library that runs
# 添加运行时库
add_library(MathFunctions MathFunctions.cxx)

# state that anybody linking to us needs to include the current source dir
# to find MathFunctions.h, while we don't.
# 说明与我们链接的任何人都需要包括当前源目录才能找到MathFunctions.h，而我们不需要。
target_include_directories(MathFunctions
        INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
        )

# should we use our own math functions
# 我们是否使用自己的数学函数
option(USE_MYMATH "Use tutorial provided math implementation" ON)
if (USE_MYMATH)
    target_compile_definitions(MathFunctions PRIVATE "USE_MYMATH")

    # first we add the executable that generates the table
    # 首先，我们添加生成表的可执行文件
    add_executable(MakeTable MakeTable.cxx)

    # add the command to generate the source code
    # 添加命令以生成源代码
    add_custom_command(
            OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/Table.h
            COMMAND MakeTable ${CMAKE_CURRENT_BINARY_DIR}/Table.h
            DEPENDS MakeTable
    )

    # library that just does sqrt
    # 只包含sqrt的库
    add_library(SqrtLibrary STATIC
            mysqrt.cxx
            ${CMAKE_CURRENT_BINARY_DIR}/Table.h
            )

    # state that we depend on our binary dir to find Table.h
    # 声明我们依靠二进制目录找到Table.h
    target_include_directories(SqrtLibrary PRIVATE
            ${CMAKE_CURRENT_BINARY_DIR}
            )

    target_link_libraries(MathFunctions PRIVATE SqrtLibrary)
endif ()

# define the symbol stating we are using the declspec(dllexport) when
# building on windows
# 定义标记在Windows上构建时使用declspec(dllexport)
target_compile_definitions(MathFunctions PRIVATE "EXPORTING_MYMATH")

# install rules
# 安装规则
install(TARGETS MathFunctions DESTINATION lib)
install(FILES MathFunctions.h DESTINATION include)
复制代码
```

接下来在 `MathFunctions` 文件目录下， 新建一个 `mysqrt.h` 文件，内容如下：

```
namespace mathfunctions {
    namespace detail {
        double mysqrt(double x);
    }
}
复制代码
```

接下来在 `MathFunctions` 文件目录下， 新建一个 `MathFunctions.cxx` 文件，内容如下：

```
#include "MathFunctions.h"

#ifdef USE_MYMATH
#  include "mysqrt.h"
#else
#  include <cmath>
#endif

namespace mathfunctions {
    double sqrt(double x) {
#ifdef USE_MYMATH
        return detail::mysqrt(x);
#else
        return std::sqrt(x);
#endif
    }
}
复制代码
```

接下来，更新 `MathFunctions/mysqrt.cxx` 以使用 `mathfunctions` 和 `detail` 命名空间：

```
#include <iostream>

#include "mysqrt.h"

// include the generated table
#include "Table.h"

namespace mathfunctions {
    namespace detail {

        // a hack square root calculation using simple operations
        double mysqrt(double x) {
            if (x <= 0) {
                return 0;
            }

            double result = x;
            if (x >= 1 && x < 10) {
                std::cout << "Use the table to help find an initial value " << std::endl;
                result = sqrtTable[static_cast<int>(x)];
            }

            // do ten iterations
            for (int i = 0; i < 10; ++i) {
                if (result <= 0) {
                    result = 0.1;
                }
                double delta = x - (result * result);
                result = result + 0.5 * delta / result;
                std::cout << "Computing sqrt of " << x << " to be " << result << std::endl;
            }

            return result;
        }
    }
}

复制代码
```

我们还需要在 `tutorial.cxx` 中进行一些更改，以使其不再使用 `USE_MYMATH`：

1. 始终包含 `MathFunctions.h`
2. 始终使用 `mathfunctions::sqrt`
3. 不包含 `cmath`

移除 `TutorialConfig.h.in` 中关于 `USE_MYMATH` 的定义，最后，更新 `MathFunctions/MathFunctions.h` 以使用 `dll` 导出定义：

```
#if defined(_WIN32)
#  if defined(EXPORTING_MYMATH)
#    define DECLSPEC __declspec(dllexport)
#  else
#    define DECLSPEC __declspec(dllimport)
#  endif
#else // non windows
#  define DECLSPEC
#endif

namespace mathfunctions {
    double DECLSPEC sqrt(double x);
}
复制代码
```

此时，如果您构建了所有内容，则会注意到链接会失败，因为我们将没有位置的静态库代码库与具有位置的代码库相结合。解决方案是无论构建类型如何，都将 `SqrtLibrary` 的 `POSITION_INDEPENDENT_CODE` 目标属性显式设置为 `True`。

```
# state that SqrtLibrary need PIC when the default is shared libraries
# 声明默认为共享库时，SqrtLibrary需要PIC
set_target_properties(SqrtLibrary PROPERTIES
        POSITION_INDEPENDENT_CODE ${BUILD_SHARED_LIBS}
        )
        
target_link_libraries(MathFunctions PRIVATE SqrtLibrary)
复制代码
```

使用 `cmake-gui` 构建项目，勾选 `BUILD_SHARED_LIBS`

在项目根目录运行命令生成可执行文件：

```
cmake --build cmake-build-debug
复制代码
```

在项目根目录运行生成的可执行文件：

```
./cmake-build-debug/Tutorial 2
复制代码
```

终端输出：

```
Use the table to help find an initial value 
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
The square root of 2 is 1.41421
复制代码
```

使用 `cmake-gui` 重新构建项目，取消勾选 `BUILD_SHARED_LIBS`

在项目根目录运行命令生成可执行文件：

```
cmake --build cmake-build-debug
复制代码
```

在项目根目录运行生成的可执行文件：

```
./cmake-build-debug/Tutorial 2
复制代码
```

终端输出：

```
Use the table to help find an initial value 
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
Computing sqrt of 2 to be 1.41421
The square root of 2 is 1.41421
复制代码
```

## 添加生成器表达式

[示例程序地址](https://github.com/TaylorKunZhang/cmake-tutorial/tree/master/add-generator-expressions)

在构建系统生成期间会评估生成器表达式，以生成特定于每个构建配置的信息。

在许多目标属性的上下文中允许使用生成器表达式，例如 `LINK_LIBRARIES`、`INCLUDE_DIRECTORIES`、 `COMPILE_DEFINITIONS` 等。当使用命令填充这些属性时，也可以使用它们，例如 `target_link_libraries()`、`target_include_directories()`、`target_compile_definitions()`等。

生成器表达式可用于启用条件链接、编译时使用的条件定义、条件包含目录等。这些条件可以基于构建配置、目标属性、平台信息或任何其他可查询信息。

生成器表达式有不同类型，包括逻辑，信息和输出表达式。

逻辑表达式用于创建条件输出，基本的表达式是0和1表达式，即布尔表达式。`$<0:…>` 代表冒号前的条件为假，表达式的结果为空字符串。 `$<1:…>` 代表冒号前的条件为真，表达式的结果为“…”的内容

生成器表达式的一个常见用法是有条件地添加编译器标志，例如语言级别或警告标志。一个好的模式是将此信息与允许传播此信息的 `INTERFACE` 目标相关联。让我们开始构建 `INTERFACE` 目标，并指定所需的 `C++` 标准级别11，而不是使用 `CMACHYCXXY` 标准。

所以下面的代码：

```
# specify the C++ standard
# 指定C ++标准
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)
复制代码
```

将被替换为：

```
add_library(tutorial_compiler_flags INTERFACE)
target_compile_features(tutorial_compiler_flags INTERFACE cxx_std_11)
复制代码
```

接下来，我们为项目添加所需的编译器警告标志。由于警告标志根据编译器的不同而不同，因此我们使用 `COMPILE_LANG_AND_ID` 生成器表达式来控制在给定一种语言和一组编译器 `ID` 的情况下应应用的标志，如下所示：

```
# add compiler warning flags just when building this project via
# the BUILD_INTERFACE genex
# 仅当通过BUILD_INTERFACE生成此项目时添加编译器警告标志
set(gcc_like_cxx "$<COMPILE_LANG_AND_ID:CXX,ARMClang,AppleClang,Clang,GNU>")
set(msvc_cxx "$<COMPILE_LANG_AND_ID:CXX,MSVC>")
target_compile_options(tutorial_compiler_flags INTERFACE
        "$<${gcc_like_cxx}:$<BUILD_INTERFACE:-Wall;-Wextra;-Wshadow;-Wformat=2;-Wunused>>"
        "$<${msvc_cxx}:$<BUILD_INTERFACE:-W3>>"
        )
复制代码
```

我们可以看到警告标志封装在 `BUILD_INTERFACE` 条件内。这样做是为了让已安装项目的使用者不会继承我们的警告标志。

修改 `MathFunctions/CMakeLists.txt` 文件，使所有的目标都增加一个调用 `tutorial_compiler_flags` 的 `target_link_libraries`。

## 添加导出配置

[示例程序地址](https://github.com/TaylorKunZhang/cmake-tutorial/tree/master/add-export-configuration)

在本教程的 “安装” 一节，我们增加了 `CMake` 安装库和项目头的能力。在 "生成安装程序“ 一节，我们添加了打包此信息的功能，以便将其分发给其他人。

下一步是添加必要的信息，以便其他 `CMake` 项目可以使用我们的项目，无论是构建目录、本地安装还是打包。

第一步是更新我们的 `install(TARGETS)` 命令，不仅要指定 `DESTINATION`，还要指定 `EXPORT`。`EXPORT` 关键字将生成并安装一个CMake文件，该文件包含用于从安装树中导入 `install` 命令中列出的所有目标的代码。通过更新 `MathFunctions/CMakeLists.txt` 中的 `install` 命令，显式导出 `MathFunctions`库，如下所示：

```
# install rules
# 安装规则
install(TARGETS MathFunctions tutorial_compiler_flags
        DESTINATION lib
        EXPORT MathFunctionsTargets)
install(FILES MathFunctions.h DESTINATION include)
复制代码
```

现在我们已经导出了 `MathFunctions`，我们还需要显式安装生成的 `MathFunctionsTargets.cmake` 文件。这是通过将以下内容添加到顶级 `CMakeLists.txt` 的底部来完成的：

```
# install the configuration targets
# 安装配置目标
install(EXPORT MathFunctionsTargets
        FILE MathFunctionsTargets.cmake
        DESTINATION lib/cmake/MathFunctions
        )
复制代码
```

此时，您应该尝试运行 `CMake`。如果一切设置正确，您将看到 `CMake` 将生成如下错误：

```
Target "MathFunctions" INTERFACE_INCLUDE_DIRECTORIES property contains
path:

  "/Users/robert/Documents/CMakeClass/Tutorial/Step11/MathFunctions"

which is prefixed in the source directory.
复制代码
```

`CMake` 想说的是，在生成导出信息的过程中，它将导出一个与当前机器有内在联系的路径，并且在其他机器上无效。解决方案是更新 `MathFunctions` 的 `target_include_directories`，让 `CMake` 理解在从生成目录和安装/打包中使用时需要不同的接口位置。这意味着将 `MathFunctions` 调用的 `target_include_directories` 转换为如下所示：

```
# state that anybody linking to us needs to include the current source dir
# to find MathFunctions.h, while we don't.
# 说明与我们链接的任何人都需要包括当前源目录才能找到MathFunctions.h，而我们不需要。
target_include_directories(MathFunctions
        INTERFACE
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
        $<INSTALL_INTERFACE:include>
        )
复制代码
```

更新后，我们可以重新运行 `CMake` 并查看是否不再发出警告。

至此，我们已经正确地包装了 `CMake` 所需的目标信息，但仍然需要生成 `MathFunctionsConfig.cmake`，以便 `CMake find_package` 命令可以找到我们的项目。因此，我们将添加新文件 `Config.cmake.in` 到项目的顶层，其内容如下：

```
@PACKAGE_INIT@

include ( "${CMAKE_CURRENT_LIST_DIR}/MathFunctionsTargets.cmake" )
复制代码
```

然后，要正确配置和安装该文件，请在顶级 `CMakeLists` 的底部添加以下内容：

```
# install the configuration targets
# 安装配置目标
install(EXPORT MathFunctionsTargets
        FILE MathFunctionsTargets.cmake
        DESTINATION lib/cmake/MathFunctions
        )

include(CMakePackageConfigHelpers)
# generate the config file that is includes the exports
# 生成包含导出的配置文件
configure_package_config_file(${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
        "${CMAKE_CURRENT_BINARY_DIR}/MathFunctionsConfig.cmake"
        INSTALL_DESTINATION "lib/cmake/example"
        NO_SET_AND_CHECK_MACRO
        NO_CHECK_REQUIRED_COMPONENTS_MACRO
        )
# generate the version file for the config file
# 生成配置文件的版本文件
write_basic_package_version_file(
        "${CMAKE_CURRENT_BINARY_DIR}/MathFunctionsConfigVersion.cmake"
        VERSION "${Tutorial_VERSION_MAJOR}.${Tutorial_VERSION_MINOR}"
        COMPATIBILITY AnyNewerVersion
)

# install the configuration file
# 安装配置文件
install(FILES
        ${CMAKE_CURRENT_BINARY_DIR}/MathFunctionsConfig.cmake
        DESTINATION lib/cmake/MathFunctions
        )
复制代码
```

至此，我们为项目生成了可重定位的 `CMake` 配置，可以在安装或打包项目后使用它。如果我们也希望从构建目录中使用我们的项目，则只需将以下内容添加到顶级 `CMakeLists` 的底部：

```
# generate the export targets for the build tree
# needs to be after the install(TARGETS ) command
# 在install(TARGETS)命令之后生成生成树的导出目标
export(EXPORT MathFunctionsTargets
        FILE "${CMAKE_CURRENT_BINARY_DIR}/MathFunctionsTargets.cmake"
        )
复制代码
```

通过此导出调用我们将生成一个 `Targets.cmake`，允许在构建目录中配置的 `MathFunctionsConfig.cmake` 由其他项目使用，而无需安装它。

## CMake使用教程系列文章

- CMake使用教程(一)
  - 基础项目
  - 添加版本号和配置头文件
  - 指定C++标准
  - 添加库
  - 提供选项
- CMake使用教程(二)
  - 添加“库”的使用要求
  - 安装
  - 测试
  - 系统自检
- CMake使用教程(三)
  - 指定编译定义
  - 添加自定义命令和生成的文件
  - 生成安装程序
  - 添加对仪表板的支持
- CMake使用教程(四)
  - 混合静态和共享
  - 添加生成器表达式
  - 添加导出配置

关注下面的标签，发现更多相似文章