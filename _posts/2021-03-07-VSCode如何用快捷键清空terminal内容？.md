VSCode如何用快捷键清空terminal内容？

https://stackoverflow.com/questions/48713604/how-can-i-clear-the-terminal-in-visual-studio-code

Open up the `Keyboard Shortcuts` with Ctrl+K, Ctrl+S. Then click on the `{}` next to the `Keyboard Shortcuts` tab to open up the `keybindings.json` file.

[![keyboard shortcuts](xoxTj.png)](https://i.stack.imgur.com/xoxTj.png)

After doing so, find some open space anywhere in the file, and type in the key bind below.

```
{
    "key": "ctrl+k",
    "command": "workbench.action.terminal.clear",
    "when": "terminalFocus"
}
```