# 要求

- 快速搭建rust開發環境
  - 編譯器
  - ide
  - debugger
- 不要安裝在c盤

# 軟件

這個是基於rustup-init和gnu build tools

vscode + rust analyzer + CodeLLDB

# 步驟

下載https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe

運行如下脚本

```bash
進入想安裝的目錄
set me=%~dp0
setx RUSTUP_HOME %me%\rusthome
setx CARGO_HOME %me%\rusthome
set RUSTUP_HOME=%me%\rusthome
set CARGO_HOME=%RUSTUP_HOME%
rem rustup toolchain install stable-gnu
rustup-init
cmd
選擇x86_64-pc-windows-gnu工具鏈
```

在vcsode裏面安裝rust analyzer插件

用vscode就可以直接debug了

debug的時候源代碼如果對不上，可以看下他想從哪個目錄load文件。用ln -s弄一個軟連接

比如我這邊是

```bash
sudo mkdir /rustc
sudo chmod 777 /rustc
ln -s /home/cutepig/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/lib/rustlib/src/rust /rustc/db9d1b20bba1968c1ec1fc49616d4742c1725b4b
```

# 參考

https://www.rust-lang.org/zh-CN/tools/install

