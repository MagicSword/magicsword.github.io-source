+++
title = "Reading Hackingvim72"
date = 2018-03-24T01:00:23+08:00
description = "HackingVim72 reading."
draft = false
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
* [Sublime-text](https://www.sublimetext.com/3) 
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

本章說明在各文件快速移動的方式。遊標移動、在多文件中移動、使用說明文件、搜索、標記。


3.1 文件內移動
--------------

### 3.1.1 基於上下文的移動

文件結構的不同，可分為兩種情形：

* 一般文件：段落、語句、單詞
* 程式碼：函數、區塊、單行

#### 3.1.1.1 一般文件

* `h`,`j`,`k`,`l`  #左、下、上、右
* `{`,`}`      #段落首、尾
* `g,`  `g;`  #最近修改過的地方，向前，向後
* `(` ,`)`    #句首、句尾
* `w`       #下一個單詞首字母
* `b`       #前一個單詞首字母
* `e`       #移動到單詞末尾

單詞(Word)的定義: 

> 由字母、數字、dash(\-)、underline(\_)組成
> 以非空白字母組成

#### 3.1.1.2 程式碼

Vim無法辨識所有程式的結構，不過C語言預設是可以的。

函數

*  `[[` and `][`: Move backwards / forward to the next section beginning (for 
example, start of a function)
* `[]` and `]]`: Move backwards / forward to the next section end (for example, 
end of a function)


區塊

* `[{`: Move to the beginning of the block
* `]}`: Move to the end of the block 


註解

* `[/`: Move to the beginning of the comment block
* `]/`: Move to the end of the comment block

`gd`: 跳到變數定義區段
`gD`: 跳到全域變數定義區段

#### 3.1.2 在長行內移動

長行：

> 一行的內容過長，超過VIM視窗範圍的話，程式會自動把超出視窗寬的在下一行顯示。 

`gk`,`gj` :會以視覺上的行為主而移動。


3.2 使用 Help 說明文件
------------------------

Vim的說明文件可以：

* 按 <F1> 進入
* 或是在命令列輸入  `:help <keyword>` 

移動
* <C-]> : 跳到 keyword 所指的位置
* <C-t> : 跳回前一個位置

文章內還有一些比較進階的設定。


3.3 在多個緩衝區(Buffer)間移動
--------------------------------

打開的文件，是存在緩衝區(Buffer)中。

* `:buffers`: buffer list
* `:buffer N`: jump to buffer N
* `:bnext(bn)`: Next buffer
* `:bprevious(bp)`: Previous buffer

3.4 快速打開引用文件
--------------------

像是在 C語言中的 `#include`

```clang
#include "example.h"
```

在 `example.h` 上按 `gf`，Vim就會把檔案讀入緩衝區

3.5 搜尋 Search
----------------

分三種：

* 在目前文件中搜索
* 在多文件中搜索
* 在說明文件中搜索


### 3.5.1 在目前文件中搜索

找單詞

* 普通模式下 `?example`，命令模式下 `/example`可以找單詞
* `n`,`N`:在找到的結果向上，向上移動。
* `//`,`??`: 上一次搜索的輸入
* `#`,`*`: 搜索在遊標上的單詞，向上移動， 向下移動


### 3.5.2 在多個文件中搜索

搜索的指令，在Unix系統下有 `grep`，MSWin下有 `find`,`findstr`，
而在 Vim下，有：

```bash
:vimgrep /pattern/[j][g] file file2... fileN
```

* /pattern/ : 正則表示式
* `j`: 把結果輸入到 `quickfix` 列表
* `g`: 如果在同一行內有三個符合的結果，則會都顯示

`quickfix`

* `:clist`:顯示 `quickfix`結果
* `cnext(cn)`,`cprevious(cp)`:在 `quickfix`列表中移動

### 3.5.3 在說明文件中搜索

```bash
:helpgrep pattern [@LANG]
#`@LANG`，可以指定說明文件的語言，例子：
:helpgrep completion@en
```

如果是新增加的文件，可以用下面的指令生成文件tags
```bash
:helptags /path/to/doc
```

3.6 標記位置
------------

有時文件太長，要在個各處移動，標記(Marks)可以在某行前
作記號。例：

* 可見標記
* 隱形標記


### 3.6.1 可見標記

通常是會在行號前面，用來標記某一行的符號。

```
:sign define name arguments
```

定義標記列顏色
```bash
:highlight SignColumn guibg=darkgrey
```

pass

### 3.6.2 隱形標記

另一種標記方式，基本上看不到，除非打開標記列表


`:marks`: 打開標記列表
`ma` : 標記 `a`
`\`a`: 移動到 `a`
`:deletemarks markid1 markid2 markid3`:刪除標記`
`:delmarks a f-i 1-4`:刪除 makrs
`:delmarks !`:刪除目前buffer所有marks

|標號|用法|
|----|----|
|0-9 |保留內部使用，通常是最近開啟文件|
|a-z |本文件使用|
|A-Z |可以跟文件使用，如果有`.viminfo`存檔，下次打開Vim時，還可以使用|

3.7 小結
---------

這一節描述了cursor的移動，搜索、或是在各文件中移動的方式。




Ch4: PRODUCTION BOOSTERS       #增強生產力
==========================================

這一章會簡介一些能增加效率的工具。

4.1 模版
--------

建立模版 Template ，減少重複性的工作。

4.1.1 模版文件
---------------

應該可以分為兩種行為

* 新建立文件時，讀取 已有的模版  或是骨架 Skeleton
* 在已存在的文件中，要加入小部分的文件結構 Snippets, 檔頭(C語言的 `#include`)，檔尾

方法：

* 建立模版檔：在 `$VIMHOME`/templates/下加入新的  `file-type.tpl` ，像是 `html.tpl`
* 設定程式設定： 加入 `autocmd` 在開啟新檔時，自動讀入模版。

4.1.2 把縮寫作為模版
--------------------

前面有提為的功能 縮寫可以用來快速輸入一些結構，像是迴圈、或是snippets

4.1.3 snipMate
--------------

更完整的功能，有人編寫了完整的 plugins。

https://vimawesome.com/plugin/snipmate
https://www.vim.org/scripts/script.php?script_id=2540
https://github.com/garbas/vim-snipmate



4.1.4 其他 snippets Pluging
----------------------------

比較
http://vim-wiki.mawercer.de/wiki/topic/text-snippets-skeletons-templates.html

除了 snipMate以外，還有其他plugins有snippets的功能

UltiSnipsby HOLGER RAPP36216612
UltiSnips - The ultimate snippet solution for Vim. Send pull requests to SirVer/ultisnips!

neosnippet-snippetsby SHOUGO1972908
The standard snippets repository for neosnippet

[vim-snippets](https://vimawesome.com/plugin/vim-snippets)
* by HONZA POKORNY25449499
* vim-snipmate default snippets (Previously snipmate-snippets)
* 這個是 snippets程式片段檔的集合


4.2 Tag List
-------------

產生程式中的所有關鍵字、函數名、…

Tag List的產生要用外部的程式，常見的有：

* Exuberant Ctags: For C, C++, Java, Perl, Python, Vim, Ruby (and 25 others)
* Vtags: For Verilog files
* Jtags: For Java files
* Hdrtags: For C / C++, Asm, Lex / Yacc, LaTeX, Vim, and Maple 
* Ptags: For Perl files

用法，可以快速跳到函數定義的地方。


###　4.2.1 Tag List 的其他用法


除了用來找函數、和變數外，還有其他用法。

`:help tags`


4.3 AutoComplete 自動補全
-------------------------

分三種

* 依前後文
* 依字典
* Omnicompletion

4.3.1 已知單詞的自動補全

`C-p` `C-n` 在打完的前兩個字母後按，

會出現auto complete的選項，向前、或向後


### 4.3.2 依字典的自動補全


利用已有的字典作 autocomplete

設定字典檔
`:set dictionary+=/path/to/dictionary/file/with/words`



`C-x C-k`
x是進入autocomplete模式， k是從字典中找相近的單字。

其他模式：

* Ctrl+l: Complete whole lines of the text
* Ctrl+n: Complete words from the current buffer
* Ctrl+k: Complete words from the dictionaries
* Ctrl+t: Complete words from the thesaurus (see :help 'thesaurus')
* Ctrl+i: Words from the current and included files
* S: Spelling the suggestions (Vim 7.0 and newer only)


### 4.3.3 Omnicompletion

`C-x C-o` 進入 Omnicompletion 模式

pass

### 4.3.4  多合一 autocomplete

把前面多種autocomplete模式整合
這個指令可以找到,`CleverTab()` 
 
 `help ins-complete`
 
可以用 `Tab` 來選取需要的選項。

4.4 錄製巨集 Macros
--------------------

用來錄製指令

* qa: Record from now on into register a. Any register can be used, but q is often used for simplicity.
* q: If pressed while recording, the recording is ended. 
* @a: Executes the recording in register a (replace with any register).
* @@: Repeats the last executed command. 

4.5 會話 Session
----------------

Vim保存了許多資訊，分成幾種：

* View: 單一視窗的資訊
* Session: 多個View的集合
* Other: 其他通用的設定

### 4.5.1 簡單會話使用

保存目前視圖、會話
```
:mkview file
:mksession file

:set viewdir=$HOME/.vim/views  #設定視圖存放的目錄

載入視圖方式
$vim -S Session.vim
:source Session.vim
:loadview View.vim

```

### 4.5.2 個人化 Session 使用

pass

### 4.5.3 Sessions as a project manager

pass

4.6 暫存器 和 Undo 分支
------------------------

* 暫存器 Register: 儲存多個緩衝區的高級剪貼薄
* Undo Branching: 文件修改的記錄

### 4.6.1 暫存器



### 4.6.2 Unod list




4.7 Folding 折疉
----------------

把段落、或是區塊 多行折疉成一行

### 4.7.1 Simple text file outlining
### 4.7.2 Using vimdiff to track the changes
### 4.7.3 Navigation in vimdiff 
### 4.7.4 Using diff to track changes

4.8 打開任意位置的文件
----------------------

打開遠端的文件
```
:Nread ftp://user@server/path/to/file
:Nwrite server user passwd path/to/file

```




### 4.8.1 Faster remote file editing

4.9 小結
--------


 

Ch5: ADVANCED FORMATTING 進階格式化 
===================================

將文件重新排版的過程。

* 文本格式化
* 代碼格式化
* 使用外部工具格式化

5.1 文本格式化
--------------

### 5.1.1 文本分段

例：將長行自動斷行

`gpap`


### 5.1.2 內文對齊

向左、 置中、向右對齊


### 5.1.3 標記標題

在 Markdown、reST中，H1、H2的語法可以寫成：

```
Level1
====== 

Level2
------

-Level3-
```

這邊利用接鍵組合，可以快速在文字下加上相同長度的 `=`，或`-`

像在 `New Heading`上按 `yypVr=o`


### 5.1.4 建立清單

用函式快速加入 lists的格式

5.2 代碼格式化
--------------

排版良好的程式碼，對方便閱讀很有幫助。

前面幾小節 介紹了縮排的幾個方式。

* Autoindent `:set ai` : 會依前一行的設定，縮排之後的文件 
* Smartindent `:set si` : smarter than autoindent
* Cindent: pass
* Indentexpr: pass



要貼程式碼時，可以用下面的指令，讓貼上的程式碼排版不會跑掉。
```
:set paste
:set nopaste
:set pastetoggle

```


5.3 使用外部工具格式化
-----------------------

使用 其他程式來排版，像是 Indent,Berkeley Par,Tidy

```
#設定 indent
:set equalprg=program
```

Tidy 是用來排版 XML,HTML 文件的工具。

```
# XML 文件
au FileType xml exe ":silent 1,$!tidy --input-xml true --indent yes -q"
# HTML 文件
au FileType html,htm exe ":silent 1,$!tidy --indent yes -q"
```

5.4 小結
--------

本章介紹了一些排版的方式



Ch6: BASIC VIM SCRIPTING 基本 Vim Scripting
===========================================







Ch7: EXTENDED VIM SCRIPTING 進階 Vim Scripting
==============================================





Appendix A Vim的其他功能
========================

Vim game，發 mail,twitter,IRC...

或是 設定成 IDE 
```
:help compiler
:help quickfix
```

參考 http://vim.wikia.com/wiki/Use_Vim_like_an_IDE


Appendix B Vimrc 設定
=====================

Vimrc是 Vim 所有設定存放的檔案，隨著時間 Vimrc可能會變的越來越大，而以維護。



B.1 保持 Vimrc 簡潔的技巧 
-------------------------

1. `:set nocompatible`: 把vim設成不相容模式，能開啟比較多的功能。
2. 使用注釋: 使用 `"` 開頭的注釋，可以讓區段的功能容易了解修改
3. 內容分段: 可以分成 全局、個人、腳本、其他 …有主題性的區段，方便修改。
4. 使用多文件: 可以將部分的內容切出另一個檔案，在本檔內用 `source`讀進程式
5. 測試時使用另一份vimrc
6. 不同系統使用不定的設定: 像是 .vimrc.linux , \_vimrc.win32 , \_gvimrc.win32 , ... etc.


B.2 Vimrc的設定系統
-------------------

[Vim Setup system : Vim Setup system - persistent setup directly in vim ](https://www.vim.org/scripts/script.php?script_id=1894)

這個plugin讓vim的設定，有選單的可以直接設定，設定完了，再存回 .vimrc

有GUI來設定，的確是方便了一些。


B.3 Vimrc雲端儲存
-----------------

把vim的設定放在網路上，可以方便在多台機器間轉移。

這邊是用 `netrw` 來讀寫網路上的設定檔。











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
4. [Vim Awesome](https://vimawesome.com/)

