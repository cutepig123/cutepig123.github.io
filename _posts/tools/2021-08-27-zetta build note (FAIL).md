zetta build note (FAIL)

- install portable node G:\Users\cutep\Downloads\node-v14.17.5-win-x64

```bash
npm install -g yarn`
cd G:\_codes\Zettlr
git clone https://github.com/Zettlr/Zettlr.git
cd Zettlr
yarn install --frozen-lockfile
yarn start
```

FAIL!

```bash
G:\_codes\Zettlr>yarn start
yarn run v1.22.11
$ electron-forge start
√ Checking your system
√ Locating Application
√ Preparing native dependencies

An unhandled rejection has occurred inside Forge:
Error: spawn bash.exe ENOENT
    at Process.ChildProcess._handle.onexit (internal/child_process.js:269:19)
    at onErrorNT (internal/child_process.js:467:16)
    at processTicksAndRejections (internal/process/task_queues.js:82:21) {
  errno: -4058,
  code: 'ENOENT',
  syscall: 'spawn bash.exe',
  path: 'bash.exe',
  spawnargs: [ './scripts/get-pandoc.sh', 'win32', 'x64' ]
}

Electron Forge was terminated. Location:
{}
error Command failed with exit code 1.
info Visit https://yarnpkg.com/en/docs/cli/run for documentation about this command.

```



add bash to path by `path %path%;G:\Program Files\Git\usr\bin`

still fails

```bash
G:\_codes\Zettlr>yarn start
yarn run v1.22.11
$ electron-forge start
√ Checking your system
√ Locating Application
√ Preparing native dependencies

An unhandled rejection has occurred inside Forge:
Error: Failed to download Pandoc: Process quit with code 0. If the code is 0, then there was error output.
    at ChildProcess.<anonymous> (G:\_codes\Zettlr\forge.config.js:41:16)
    at ChildProcess.emit (events.js:400:28)
    at maybeClose (internal/child_process.js:1055:16)
    at Socket.<anonymous> (internal/child_process.js:441:11)
    at Socket.emit (events.js:400:28)
    at Pipe.<anonymous> (net.js:675:12)

Electron Forge was terminated. Location:
{}
error Command failed with exit code 1.
info Visit https://yarnpkg.com/en/docs/cli/run for documentation about this command.
```



search in web. there are info [here](https://github.com/Zettlr/Zettlr/issues/1869)

i repeat it find following issues

```bash
G:\_codes\Zettlr>bash

cutep@DESKTOP-SP3IKDT  /g/_codes/Zettlr (develop)
$ bash ./scripts/get-pandoc.sh win32 x64
Working directory is /g/_codes/Zettlr/resources
Downloading: pandoc-2.14.2-windows-x86_64.zip ...
./scripts/get-pandoc.sh: line 94: curl: command not found
Extracting ...
unzip:  cannot find or open pandoc-2.14.2-windows-x86_64.zip, pandoc-2.14.2-windows-x86_64.zip.zip or pandoc-2.14.2-windows-x86_64.zip.ZIP.
zipinfo:  cannot find or open pandoc-2.14.2-windows-x86_64.zip, pandoc-2.14.2-windows-x86_64.zip.zip or pandoc-2.14.2-windows-x86_64.zip.ZIP.
Extracted to:
Moving binary from ./ to resources directory ...
mv: cannot stat './pandoc.exe': No such file or directory
Cleaning up ...
Successfully downloaded Pandoc for win32/x64!
```



It seems the tools even in windows still needs tools like bash, curl,...

