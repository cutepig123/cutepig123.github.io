# 使用goreleaser编译go program

OK!

```bash
git clone to G:\_codes\-
download go from https://golang.org/dl/
install to g:\Program Files\Go\

install goreleaser from link https://goreleaser.com/install/
go install github.com/goreleaser/goreleaser@latest


follow https://goreleaser.com/quick-start/
create main.go
goreleaser init
go mod init testhjs
create a repo
goreleaser check
goreleaser release --snapshot --skip-publish --rm-dist


cd G:\_codes\-
goreleaser init
goreleaser check
goreleaser release --snapshot --skip-publish --rm-dist
```

LOGGING as below

```batch
G:\_codes\->goreleaser release --snapshot --skip-publish --rm-dist
   • releasing...
   • loading config file       file=.goreleaser.yml
   • loading environment variables
   • getting and validating git state
      • building...               commit=20e66235c2c50a6906d4cc6c52fc1c77e812daff latest tag=v1.3.4-vetch101
      • pipe skipped              error=disabled during snapshot mode
   • parsing tag
   • running before hooks
      • running                   hook=go mod tidy
      • running                   hook=go generate ./...
   • setting defaults
      • snapshotting
      • github/gitlab/gitea releases
      • project name
      • loading go mod information
      • building binaries
      • creating source archive
      • archives
      • linux packages
      • snapcraft packages
      • calculating checksums
      • signing artifacts
      • signing docker images
      • docker images
      • docker manifests
      • artifactory
      • blobs
      • homebrew tap formula
      • scoop manifests
      • twitter
      • reddit
      • slack
      • milestones
   • snapshotting
      • building snapshot...      version=1.3.4-next
   • checking ./dist
      • --rm-dist is set, cleaning it up
   • loading go mod information
   • writing effective config file
      • writing                   config=dist\config.yaml
   • generating changelog
      • pipe skipped              error=not available for snapshots
   • building binaries
      • building                  binary=G:\_codes\-\dist\-_linux_arm_7\-
      • building                  binary=G:\_codes\-\dist\-_windows_arm_7\-.exe
      • building                  binary=G:\_codes\-\dist\-_linux_386\-
      • building                  binary=G:\_codes\-\dist\-_windows_386\-.exe
   • archives
      • creating                  archive=dist\-_1.3.4-next_Windows_armv7.tar.gz
      • creating                  archive=dist\-_1.3.4-next_Linux_i386.tar.gz
      • creating                  archive=dist\-_1.3.4-next_Linux_armv7.tar.gz
      • creating                  archive=dist\-_1.3.4-next_Windows_i386.tar.gz
   • creating source archive
   • linux packages
   • snapcraft packages
   • calculating checksums
      • checksumming              file=-_1.3.4-next_Linux_armv7.tar.gz
      • checksumming              file=-_1.3.4-next_Linux_i386.tar.gz
      • checksumming              file=-_1.3.4-next_Windows_i386.tar.gz
      • checksumming              file=-_1.3.4-next_Windows_armv7.tar.gz
   • signing artifacts
   • docker images
   • publishing
      • blobs
      • http upload
      • custom publisher
      • artifactory
      • docker images
         • pipe skipped              error=publishing is disabled
      • docker manifests
         • pipe skipped              error=publishing is disabled
      • snapcraft packages
         • pipe skipped              error=publishing is disabled
      • github/gitlab/gitea releases
         • pipe skipped              error=publishing is disabled
      • homebrew tap formula
      • scoop manifests
      • milestones
         • pipe skipped              error=publishing is disabled
   • signing docker images
      • pipe skipped              error=artifact signing is disabled
   • announcing
      • twitter
         • pipe skipped              error=announcing is disabled
      • reddit
         • pipe skipped              error=announcing is disabled
      • slack
         • pipe skipped              error=announcing is disabled
   • release succeeded after 44.35s
```



.goreleaser.yml

```yml
# This is an example .goreleaser.yml file with some sane defaults.
# Make sure to check the documentation at http://goreleaser.com
before:
  hooks:
    # You may remove this if you don't use go modules.
    - go mod tidy
    # you may remove this if you don't need go generate
    - go generate ./...
builds:
  - env:
      - CGO_ENABLED=0
    goos:
      - linux
      - windows
      #- darwin
    goarch:
      #- amd64
      - 386
      - arm
      #- arm64
    goarm:
      #- 6
      - 7      
archives:
  - replacements:
      darwin: Darwin
      linux: Linux
      windows: Windows
      386: i386
      amd64: x86_64
checksum:
  name_template: 'checksums.txt'
snapshot:
  name_template: "{{ incpatch .Version }}-next"
changelog:
  sort: asc
  filters:
    exclude:
      - '^docs:'
      - '^test:'

```

