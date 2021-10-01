按照[GitHub - rustdesk/rustdesk: Yet another remote desktop software](https://github.com/rustdesk/rustdesk)说的流程编译

下载vcpkg

设置`VCPKG_ROOT` env variable

使用rustup安装rust cargo工具链

vcpkg install libvpx:x64-windows-static libyuv:x64-windows-static opus:x64-windows-static

cargo run

# FAQ

问题

```basic
 thread 'main' panicked at 'called `Result::unwrap()` on an `Err` value: NotPresent', C:\Users\cutep\.cargo\git\checkouts\magnum-opus-7580b098b18e2bc5\ad08361\build.rs:7:50
```

解决方案

设置`VCPKG_ROOT` env variable

问题

```bash
 thread 'main' panicked at 'Unable to find libclang: "couldn't find any valid shared libraries matching: ['clang.dll', 'libclang.dll'], set the `LIBCLANG_PATH` environment variable to a path where one of these files can be found (invalid: [])"', C:\Users\cutep\.cargo\registry\src\github.com-1ecc6299db9ec823\bindgen-0.59.1\src/lib.rs:2117:31
  note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

解决

https://github.com/rustdesk/rustdesk/issues/180
download and install [LLVM](https://prereleases.llvm.org/win-snapshots/LLVM-12.0.0-6923b0a7-win64.exe)

问题

```bash
thread 'main' panicked at 'error: 'sciter.dll' was not found neither in PATH nor near the current executable.
  Please verify that Sciter SDK is installed and its binaries (from SDK/bin/64) are available in PATH.', C:\Users\cutep\.cargo\git\checkouts\rust-sciter-06aa50f9c0fcf3d6\4cd10f9\src/lib.rs:215:21
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
error: process didn't exit successfully: `target\debug\rustdesk.exe` (exit code: 101)
```

Download [Windows](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.win/x64/sciter.dll)

成功了！

![](..\images\2021-08-28-22-56-21-image.png)
