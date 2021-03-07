Rust: VSCode debug设置

# 前提

1. 切换到msvc toolchain by `rustup  default stable-x86_64-pc-windows-msvc`

# 步骤

## Install Rust and VS Code

This should go without saying.

[Install Rust](https://www.rust-lang.org/tools/install)
[Install Visual Studio Code](https://code.visualstudio.com/download)

## Install VS Code Extensions

You'll need to install an extension. Which one depends on your platform.

[C/C++ (Windows)](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
[CodeLLDB (OS X / Linux)](https://marketplace.visualstudio.com/items?itemName=vadimcn.vscode-lldb)

It probably makes sense to go ahead and install the [Rust extension](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust) as well.

## Configure VS Code

Now that your tools are installed you need to configure your VS Code launch properties.

Click Debug -> Add Configuration
If you're on Windows then select `C++ (Windows)`
If you're on Mac or Linux then select `LLDB: Custom Launch`

This should create and open `launch.json`. You'll have to manually change the executable name under "program".

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "(Windows) Launch",
            "type": "cppvsdbg",
            "request": "launch",
            "program": "${workspaceRoot}/target/debug/foo.exe",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceRoot}",
            "environment": [],
            "externalConsole": true
        },
        {
            "name": "(OSX) Launch",
            "type": "lldb",
            "request": "launch",
            "program": "${workspaceRoot}/target/debug/foo",
            "args": [],
            "cwd": "${workspaceRoot}",
        }
    ]
}
```

Text above can be copy-pasta'd.

Next, you should verify breakpoints are enabled. Some readers have reporting needing to this do. Some machines have it enabled by default. 🤷‍♂️

![Breakpoint settings](07.png)

File -> Preferences -> Settings

That's it!

Add a breakpoint. Press F5 to launch. Voila!

# Ref

https://www.forrestthewoods.com/blog/how-to-debug-rust-with-visual-studio-code/

