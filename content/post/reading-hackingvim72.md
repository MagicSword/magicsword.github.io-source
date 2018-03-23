+++
title = "Reading Hackingvim72"
date = 2018-03-24T01:00:23+08:00
description = "HackingVim72 reading."
toc = true
categories = ["technology"]
tags = ["reading","vim"]
images = [
  "https://source.unsplash.com/category/technology/1600x900"
] # overrides the site-wide open graph image
+++

HackingVim72讀後心得。
以及一些簡單的筆記。

<!--more-->

概述
====

這本書大概是講一些比較進階的Vim設定使用的內容。

Table of Contents:

|           原文                | 中文 |
|-------------------------------|------|
| Ch1: GETTING STARTED WITH VIM | #簡介 |
| Ch2: PERSONALIZING VIM        | #Vim個人化 |
| Ch3: BETTER NAVIGATION        | #移動 |
| Ch4: PRODUCTION BOOSTERS      | #增強生產力 |
| Ch5: ADVANCED FORMATTING      | #進階格式化 |
| Ch6: BASIC VIM SCRIPTING      | #基本 Vim Scripting |
| Ch7: EXTENDED VIM SCRIPTING   | #進階 Vim Scripting |



Ch1: GETTING STARTED WITH VIM #簡介
===================================

簡介了vim的歷史，從ex,vi,STEVIE,Elvis,nvi,Vim,Vile。

不過沒提到較新的 [neovim](https://github.com/neovim/neovim)。

另外一些比較有趣的編輯器:

* Google用 Rust寫的新編輯器 [xi-editor](https://github.com/google/xi-editor)。
* Emacs
* Sublime-text2
* Visual Stuido Code
* Atom


Ch2: PERSONALIZING VIM        #Vim個人化    
========================================

2.1 設定檔的位置
----------------

* 作業系統的不同： Linux(.vimrc) , MSWin(\_vimrc)
* 操作界面的不同： Console(vimrc), GUI(gvimrc), vi/ex mode(exrc)

在Vim下輸入指令，直接顯示目前的設定檔位置：

```bash
:echo $HOME
:echo $MYVIMRC
:echo $MYGVIMRC
```

gvimrc 主要是輸入一些在GUI特有的設定，最好是能把跟 vimrc的設定分開。

2.2 字體
--------

在GUI下輸入，可以打開字型視窗。
```bash
:set guifont=*
```

 不同的的作業系統下設定字型的方式有點差異。
```bash
#Linux
:set guifont=Courier\ New\ 14
#MSWin
:set guifont=Courier\ New:14

:help guifont  #下有更多的資料
```

See Also: [Setting the font in the GUI](http://vim.wikia.com/wiki/Setting_the_font_in_the_GUI)

2.3 配色 (colorscheme)
-----------------------
配色在 console，和GUI下，同一colorscheme會有不同的效果，
所以選擇 colorscheme應該要注意。

### 2.3.1 高亮 (hightlight) 

pass

2.4 狀態列(statusline)
----------------------
狀態列可以設定滿多東西的，文件名，格式，文件長度…

```bash
:set statusline=%F%m%r%h%w\ [FORMAT=%{&ff}]\ [TYP[HEX=\%02.2B]\ [POS=%04l,%04v]\ [%p%%]\ [LEN=%L]
```

但這設定完後，不會馬上出現，要設定 statusline的位置在最後兩行，才會出現。

```bash
:set laststatus=2  #狀態列在最後第二行
:set laststatus=0  #狀態列關閉
```

2.5 切換選單、工具列 Menu,Toolbar
-----------------

在GUI下，可以設定功能到選單、工具列上。

2.6 自訂選單、工具列
---------------------

增加選單 
```bash
:menu menupath command
```

`menu` 的指令就是像 `map` 把選單映射到一個指令

例如
```bash
:menu Tabs.Next <ESC>:tabnext<cr>
```

2.7 修改頁籤(Tabs)
-------------------

從 Vim 7.0開始支援 頁籤 Tabs，每個 Tabs有個別的屬性。

```bash
:set tabline tabline-layout  #Tabs的狀態列
:set guitablabel #gvim的Tab狀態列
```

2.8 工作區個人化
-----------------

### 2.8.1 光標 cursor 

```bash
:set cursorline   #顯示cursor line

:highlight CursorLine guibg=lightblue ctermbg=lightgray
#設定 cursorline 顏色
:set cursorcolumn #顯示縱向的指標行
:highlight CursorColumn guibg=blue ctermbg=gray
#設定 cursorcolumn 顏色
:set nocursorcolumn #關閉cursorcolumn
```
### 2.8.2 行號 line numbers

```bash
#打開行號
:set number
:set nu

:set nonumber
:set nonu

#預設的行號佔 4個space, 下面指令可以修改預設值
:set numberwidth=`widch`

```

### 2.8.3 拼寫檢查 Spell checking

Vim 7.0 以後有內建的 spell check

```bash
:set spell  #打開拼寫檢查
:set spelllang=en_us #設定拼寫語言
```

**錯字的配色**

* 在console(terminal)下，紅底白字
* 在gvim下，紅色波浪底線

**移動、更正**

* 把遊標移到錯誤的字，輸入  `z=`，可以更正錯誤的拼字。
* `]s` and `[s` 可以移動到上一個、下一個錯誤拼字

### 2.8.4 工具提示 Tooltip



### 2.8.5 使用縮寫 abbreviations

使用縮寫來減少重複輸入
```bash
:iabbrev myAddr 32 Lincoln Road, Birmingham B27 6PA, United Kingdom
```
可以在 輸入模式中，輸入 myAddr後，變成之前設定的地址。


*	 :abbreviate(abbr): Abbreviations for all modes   #全模式
*	 :iabbrev(iabbr): Abbreviations for the insert mode #輸入模式
*	 :cabbrev(cabbr): Abbreviations for the command line only #命令模式


### 2.8.6 修改按鍵綁定 Key bindings

```bash
:map <C-s> <esc>:w<cr>
```
把按鍵和指令重新指定。


* :map: For the Normal, Insert, Visual, and Command-line modes
* :imap: For the Insert mode only
* :cmap: For the Command-line mode only
* :nmap: For the Normal mode only
* :vmap: For the Visual mode only

| Keys | Notation |
|------|----------|
|`<BS>` |Backspace|
|`<Tab>`| Tab|
|`<CR>`| Enter|
|`<Enter>`| Enter|
|`<Return>`| Enter|
|`<Esc>`| Escape|
|`<Space>`| Space|
|`<Up>`| Up arrow|
|`<Down>`| Down arrow|
|`<Left>`| Left arrow|
|`<Right>`| Right arrow|
|`<F1>` - `<F12>`| Function keys 1 to 12|
|#1, #2..#9,#0| Function keys F1 to F9, F1|
|`<Insert>`| Insert|
|`<Del>`| Delete|
|`<Home>`| Home|
|`<End>`| End|
|`<PageUp>`| Page up|
|`<PageDown>`| Page down|



2.9 小結
--------

這章說明了各種設定修改的方式。



Ch3: BETTER NAVIGATION         #移動 
====================================

本章說明在各文件快速移動的方式。






Ch4: PRODUCTION BOOSTERS       #增強生產力
==========================================

























[I'm an inline-style link](https://www.google.com)

[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

[I'm a reference-style link][Arbitrary case-insensitive reference text]

[I'm a relative reference to a repository file](../blob/master/LICENSE)

[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself].

URLs and URLs in angle brackets will automatically get turned into links. 
http://www.example.com or <http://www.example.com> and sometimes 
example.com (but not on Github, for example).

Some text to show that the reference links can follow later.

[arbitrary case-insensitive reference text]: https://www.mozilla.org
[1]: http://slashdot.org
[link text itself]: http://www.reddit.com

See Also:

* [powewrline](https://github.com/powerline/powerline)
* [1]


樣式可以用 星號\* 或是 底線\_

斜體 emphasis, aka italics, with *asterisks* or _underscores_.
粗體 Strong emphasis, aka bold, with **asterisks** or __underscores__.
合併 Combined emphasis with **asterisks and _underscores_**.
刪除線 Strikethrough uses two tildes. ~~Scratch this.~~



第一種是手工的目錄

<h3 id="toc">目錄</h3>

*   [概述](#overview)
	* [語法](#syntax)	
	* [目錄](#toc)
*   [區塊元素](#block)
	* [標題](#caption)
	* [連結](#link)
	* [圖片、其他、youtube](#media)
	* [程式碼](#code)
	* [參考連結](#ref)


內文地方加上 <h2 id="overview">概述</h2>的連結

第二種是 [After-Dark](https://comfusion.github.io/after-dark/)  內建目錄，在
標頭上加上  `toc: = true`，程式會把大的標題生成目錄


區塊元素
========

 ** List **

* AAA
	* BBB
* CCC


1. what
2. some
3. soso




標題
--------

Setext 形式是用底線的形式，利用 `=` （最高階標題）和 `-` （第二階標題），例如：

    This is an H1
    =============

    This is an H2
    -------------

任何數量的 `=` 和 `-` 都可以有效果。

Atx 形式則是在行首插入 1 到 6 個 `#` ，對應到標題 1 到 6 階，例如：

    # This is an H1

    ## This is an H2

    ###### This is an H6

行首的井字數量決定標題的階數，行尾的#可不加


連結
--------
Markdown 支援兩種形式的連結語法： *行內*和*參考*兩種形式。

	[連結文字](連結目標)

絕對路徑
[Google](https://www.google.com)

相對路徑
[post](/post/)

連結到文章內的id
[example][id] 或是空白隔著 [2 example] [id]

 [id]: http://example.com/  "Optional Title Here"
 [id]: http://example.com/  'Optional Title Here'
 [id]: http://example.com/  (Optional Title Here)
 [id]: <http://example.com/>  "Optional Title Here"

Footer

That's some text with a footnote.[^1]

[^1]: 
	And that's the footnote.

    That's the second paragraph.


圖片、其他、youtube
--------

行內和參考
    ![Alt text](/path/to/img.jpg)

    ![Alt text](/path/to/img.jpg "Optional title")

參考式的圖片語法則長得像這樣：

    ![Alt text][id]

「id」是圖片參考的名稱，圖片參考的定義方式則和連結參考一樣：

    [id]: url/to/image  "Optional title attribute"

要指定高度的話，也可以用 `<img>`



程式碼
--------

分兩個，行內，整段
行內像文中會提到的func name  `print()` `cast` `def()`

整段用 三個  \`\`\` 包起，第一個後面放語言的名字
```python
	for i in 10:
		print("heloo,world")
```

如果要的syntax highlighting的話，要用hugo內的 `shortcode`

{{< highlight go "linenos=inline,hl_lines=2 3" >}}
var a string
var b string
var c string
var d string
{{< / highlight >}}




參考連結
========

1. [Hacking Vim 7.2 by Kim Schulz April 2010](https://www.packtpub.com/application-development/hacking-vim-72)
2. [HackingVim72簡中](https://github.com/wuzhouhui/hacking_vim)
3. [Vim Tips Wiki](http://vim.wikia.com/wiki/Vim_Tips_Wiki)
4. [Customizing](https://comfusion.github.io/after-dark/#customizing)
