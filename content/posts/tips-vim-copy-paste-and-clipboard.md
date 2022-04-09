+++
title = "Tips Vim Copy Paste and Clipboard"
date = 2018-05-10T22:46:18+08:00
description = "Tips of Vim using copy paste and clipboard"
draft = false
toc = false
categories = ["technology"]
tags = ["tips", "editor","vim"]
images = [
  "https://source.unsplash.com/category/technology/1600x900"
] # overrides the site-wide open graph image
+++

Vim 複製、貼上，及使用系統的剪貼簿。

<!--more-->

Task list: :smile:

- [x] 初稿
- [ ] 再讀
- [ ] 筆記
- [ ] 完成


# 概述

Vim 複製、貼上，及使用系統的剪貼簿。

# 混用

在 ~/.vimrc 加上 

```vim
set clipboard=unnamed
# set mouse=a
# 讓mouse一選，就直接是選取模式了
```

Vim 內的剪貼即會依系統剪貼簿內容變更。

# 分開使用

一般的 Vim 指令 

* `yy` : 是複製整行
* `dd` : 是剪下整行

使用系統剪貼簿，要加前置 `"+`

* `"+yy` : 複製整行進系統剪貼簿
* `"+dd` : 剪下整行進系統剪貼簿
* `"+gP` : 貼上系統剪貼簿內容後，把遊標放在最後

**See Also**
- [Explain "+gP command from gvim menu](https://stackoverflow.com/questions/13317586/explain-gp-command-from-gvim-menu)

# 參考連結

1. [讓 vim 的複製貼上和其它 terminal 以及 Windows 共用 clipboard](https://fcamel-life.blogspot.tw/2011/02/vim-terminal-windows-clipboard.html)
2. [讓 Vim 跟與你的系統剪貼簿 (clipboard) 共舞](http://littleqnote.blogspot.tw/2013/09/vim-clipboard.html)
3. [Vim Tips Wikia: Accessing the system clipboard](http://vim.wikia.com/wiki/Accessing_the_system_clipboard)
4. [vim-基本操作](http://gisanfu.pixnet.net/blog/post/24471650-vim-%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C)
5. [「筆記」vim/gvim 共用 X-Window 剪貼簿](http://playubuntu.blogspot.tw/2011/04/vimgvim-x-window.html)
