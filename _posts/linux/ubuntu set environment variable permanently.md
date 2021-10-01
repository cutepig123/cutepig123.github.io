# ubuntu set environment variable permanently

~/.profile

```bash
export PATH="$PATH:$HOME"
```



# git tui tool

https://github.com/extrawurst/gitui

```bash
# download it
test@ubuntu:~$ wget 
https://github.com/extrawurst/gitui/releases/download/v0.17.1/gitui-linux-musl.tar.gz

test@ubuntu:~$ tar xvzf gitui-linux-musl.tar.gz

export PATH="$PATH:$HOME"

nano .profile
# add export PATH="$PATH:$HOME" at end of it

# cd a git path
cd my_git_repo
gitui

```



vmware mount windows shared folder to linux

```bash
# https://askubuntu.com/questions/29284/how-do-i-mount-shared-folders-in-ubuntu-using-vmware-tools

$ ls  /mnt/hgfs/g

# if above not work, try following
$ vmware-hgfsclient
g
$ sudo vmhgfs-fuse .host:/g /mnt/hgfs/ -o allow_other -o uid=1000

```

G:\Users\cutep\AppData\Local\Programs\Python\Python39