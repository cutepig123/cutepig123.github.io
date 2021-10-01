---
categories: windows
---
MouseJiggle分析

MouseJiggle是一个windows下的工具，通过模拟鼠标移动来防止电脑进入屏保

他的原理是每隔一秒让鼠标动一动，防止电脑进入屏保

```c#
        public static void Jiggle (int dx, int dy)
        {
            var inp = new INPUT ();
            inp.TYPE = Jiggler.INPUT_MOUSE;
            inp.dx = dx;
            inp.dy = dy;
            inp.mouseData = 0;
            inp.dwFlags = Jiggler.MOUSEEVENTF_MOVE;
            inp.time = 0;
            inp.dwExtraInfo = (IntPtr) 0;

            if (SendInput (1, ref inp, 28) != 1)
                throw new Win32Exception ();
        }
```

