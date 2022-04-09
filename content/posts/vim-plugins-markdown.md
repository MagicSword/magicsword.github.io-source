+++
title = "Vim Plugins Markdown"
date = 2018-06-05T21:07:12+08:00
description = "Add some plugins for Markdown editing"
draft = false
toc = true  # by after-dark
categories = ["technology"]
tags = ["vim", "plugins","markdown"]
pre ="<i class='fa fa-file'></i> "
type="page" # set "slide" to display it fullscreen with reveal.js
images = [
  "https://source.unsplash.com/category/technology/"
] # overrides the site-wide open graph image
+++

 加一些幫助 Markdown 編輯的 plugins.


<!--more-->

Task list: :smile:

- [x] 初稿
- [ ] 再讀
- [ ] 筆記
- [ ] 完成


# 概述


# Plugins

用 VimPlug ，有 lazyLoad ，裝多一些 plugin ，應該比較不會 lag



## vim-markdown

[vim-markdown](https://github.com/plasticboy/vim-markdown)

Syntax highlighting, matching rules and mappings for the original Markdown and extensions.

主要功能是 語法高亮，標題間快快速移動功能鍵，Toc，打開檔頭 toml 的語法標示

其他功能看原始文件的 github.

文件預覽的話，可能就直接用 `Hugo server -D`

**快速鍵**

-   `gx`: open in browser

-   `ge`: open in editor

-   `]]`: go to next header. `<Plug>Markdown_MoveToNextHeader`

-   `[[`: go to previous header. Contrast with `]c`. `<Plug>Markdown_MoveToPreviousHeader`

-   `][`: go to next sibling header if any. `<Plug>Markdown_MoveToNextSiblingHeader`

-   `[]`: go to previous sibling header if any. `<Plug>Markdown_MoveToPreviousSiblingHeader`

-   `]c`: go to Current header. `<Plug>Markdown_MoveToCurHeader`

-   `]u`: go to parent header (Up). `<Plug>Markdown_MoveToParentHeader`

- `Toc`, `Toch`,`Tocv`, `Toct`   TableofContent






# 參考連結

1. [絕世好 Vim：舒爽地編輯 Markdown 文件](https://5xruby.tw/ja/posts/markdown-extension-on-vim) 
1. [Yet another vimrc http://kaochenlong.com](https://github.com/kaochenlong/eddie-vim2)
1. [A Vim input method engine](https://github.com/pi314/ime.vim)


[google]: "https://www.google.com" "Search Engine"
