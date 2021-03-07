A finding on MFC DoModal & SetParent

# Finding

Normally if DoModal() is called, all windows belonging to the process will not responsible for messages.

but we find an exception. if a window's parent is set to a window in another process, the window can still receive messages!

# Analysis

