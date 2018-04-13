+++
title = "Tool Commandline Autojump"
date = 2018-04-11T23:30:18+08:00
description = "navigate directories tool autojump."
draft = false
toc = false
categories = ["technology"]
tags = ["commandline", "unix"]
images = [
  "https://source.unsplash.com/category/technology/1600x900"
] # overrides the site-wide open graph image
+++

[autojump][] 能快速的切換資料夾。


<!--more-->

# 簡述

```
# 一個很長的目錄
cd \a\b\c\d\e\f\g\h\i\j\k
# 之後要再去同一個目錄
j k
```


# 安裝設定

**REQUIREMENTS**

-   Python v2.6+ except v3.2
-   Supported shells:
    -   bash v4.0+
    -   zsh
    -   fish
    -   tcsh (experimental)
    -   clink (Windows, experimental)

**Debian下**

```bash
$sudo apt install autojump
```
在 `.bashrc` 中加入 
```bash
source /usr/share/autojump/autojump.bash
```

或是參考 `/usr/share/doc/autojump/README.Debian`


**Windows下**

[autojump][] 在 windows 下要配合 [clink][] 使用。

下載原始碼
```bash
$git clone git://github.com/joelthelion/autojump.git
```

照指示安裝
```bash
$cd autojump
$./install.py or ./uninstall.py
```
# 使用

`autojump` 或是更簡化的指令 `j`

說明
```bash
$autojump --help
```

autojump 會記得你去過的目錄，之後要再切換到之前去過的目錄，
只要直接打目錄名稱就可以，若有同名的目錄，多換幾次 tab


指令說明
```
usage: autojump [-h] [-a DIRECTORY] [-i [WEIGHT]] [-d [WEIGHT]] [--complete]
                [--purge] [-s] [-v]
                [DIRECTORY [DIRECTORY ...]]

Automatically jump to directory passed as an argument.

positional arguments:
  DIRECTORY             directory to jump to

optional arguments:
  -h, --help            show this help message and exit
  -a DIRECTORY, --add DIRECTORY
                        add path
  -i [WEIGHT], --increase [WEIGHT]
                        increase current directory weight
  -d [WEIGHT], --decrease [WEIGHT]
                        decrease current directory weight
  --complete            used for tab completion
  --purge               remove non-existent paths from database
  -s, --stat            show database entries and their key weights
  -v, --version         show version information
```

autojump 會有個文件記錄每個目錄的權重。
```bash
$autojump -s  #看目前的目錄資料

/home/xxx/.local/share/autojump/autojump.txt
C:\Users\XXX\AppData\Roaming\autojump\autojump.txt
```

# 其他

目前在 Windows 下的環境是 [cmder][]  +  [clink][]

執行的問題不少， Python 是用 Anaconda3 ，

改天再來調整看看。


參考連結
--------

1. [cd is Wasting Your Time by Olivier Lacan ](https://olivierlacan.com/posts/cd-is-wasting-your-time/?utm_source=wanqu.co&utm_campaign=Wanqu+Daily&utm_medium=email) 
2. [Autojump](https://ianwu.tw/2013/05/21/linux-tool-autojump/) 



[autojump]: https://github.com/wting/autojump "easily navigate directories from the command line"
[clink]: https://mridgers.github.io/clink/ "在Windows下提到自動完成,Ctrl-V貼上…功能"
[cmder]: http://cmder.net/ "Packages  Conemu + clink + git"
