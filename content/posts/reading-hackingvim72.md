+++
title = "Reading HackingVim 7.2"
date = 2018-03-24T01:00:23+08:00
description = "Hacking Vim 7.2 reading."
draft = false
toc = true
categories = ["Technology"]
tags = ["reading","vim"]
images = [
  "https://source.unsplash.com/category/technology/1600x900"
] # overrides the site-wide open graph image
+++



Hacking Vim 7.2 讀後心得。

以及一些簡單的筆記、和心得記錄。

<!--more-->

Task list: :smile:

- [x] 初稿
- [ ] 修正
- [ ] incomplete
- [ ] completed


![Hacking Vim 7.2](https://d1ldz4te4covpm.cloudfront.net/sites/default/files/imagecache/ppv4_reader_book_cover/0509_Hacking%20Vim%207.2cov.jpg)

[Hacking Vim 7.2](https://www.packtpub.com/application-development/hacking-vim-72)
<BR> Ready-to-use hacks with solutions for common situations encountered by users of the Vim editor

- by Kim Schulz (Author)
- File Size: 1543 KB
- Print Length: 246 pages
- Publisher: Packt Publishing (April 29, 2010)
- Publication Date: April 29, 2010
- Sold by: Amazon Digital Services LLC
- Language: English

[Code Files](https://www.packtpub.com/lcode_download/5226)

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

簡介了 Vim 的歷史，從 ex,vi,STEVIE,Elvis,nvi,Vim,Vile。

不過沒提到較新的 [neovim](https://github.com/neovim/neovim)。

另外一些比較有趣的編輯器:

* Google 用 Rust 寫的新編輯器 [xi-editor](https://github.com/google/xi-editor)。
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

```vim
:echo $HOME
:echo $MYVIMRC
:echo $MYGVIMRC
```

gvimrc 主要是輸入一些在GUI特有的設定，最好是能把跟 vimrc的設定分開。

2.2 字體
--------

在GUI下輸入，可以打開字型視窗。
```vim
:set guifont=*
```

 不同的的作業系統下設定字型的方式有點差異。
```vim
" Linux
:set guifont=Courier\ New\ 14
" MSWin
:set guifont=Courier\ New:14
:help guifont  "更多的資料
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

```vim
:set statusline=%F%m%r%h%w\ [FORMAT=%{&ff}]\ [TYP[HEX=\%02.2B]\ [POS=%04l,%04v]\ [%p%%]\ [LEN=%L]
```

但這設定完後，不會馬上出現，要設定 statusline的位置在最後兩行，才會出現。

```vim
:set laststatus=2  #狀態列在最後第二行
:set laststatus=0  #狀態列關閉
```

2.5 切換選單、工具列 Menu,Toolbar
-----------------

在GUI下，可以設定功能到選單、工具列上。

2.6 自訂選單、工具列
---------------------

增加選單 
```vim
:menu menupath command
```

`menu` 的指令就是像 `map` 把選單映射到一個指令

例如
```vim
:menu Tabs.Next <ESC>:tabnext<cr>
```

2.7 修改頁籤(Tabs)
-------------------

從 Vim 7.0開始支援 頁籤 Tabs，每個 Tabs有個別的屬性。

```vim
:set tabline tabline-layout  " Tabs的狀態列
:set guitablabel " gvim的Tab狀態列
```

2.8 工作區個人化
-----------------

### 2.8.1 光標 cursor 

```vim
:set cursorline   " 顯示cursor line
:highlight CursorLine guibg=lightblue ctermbg=lightgray
" 設定 cursorline 顏色
:set cursorcolumn " 顯示縱向的指標行
:highlight CursorColumn guibg=blue ctermbg=gray
" 設定 cursorcolumn 顏色
:set nocursorcolumn " 關閉cursorcolumn
```
### 2.8.2 行號 line numbers

```vim
" 打開行號
:set number
:set nu
:set nonumber
:set nonu
" 預設的行號佔 4個space, 下面指令可以修改預設值
:set numberwidth=`widch`
```

### 2.8.3 拼寫檢查 Spell checking

Vim 7.0 以後有內建的 spell check

```vim
:set spell  " 打開拼寫檢查
:set spelllang=en_us " 設定拼寫語言
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
```vim
:iabbrev myAddr 32 Lincoln Road, Birmingham B27 6PA, United Kingdom
```
可以在 輸入模式中，輸入 myAddr後，變成之前設定的地址。


*	 :abbreviate(abbr): Abbreviations for all modes   #全模式
*	 :iabbrev(iabbr): Abbreviations for the insert mode #輸入模式
*	 :cabbrev(cabbr): Abbreviations for the command line only #命令模式


### 2.8.6 修改按鍵綁定 Key bindings

```vim
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

: 一行的內容過長，超過VIM視窗範圍的話，程式會自動把超出視窗寬的在下一行顯示。 

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

```c
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

```vim
:vimgrep /pattern/[j][g] file file2... fileN
```

* /pattern/ : 正則表示式
* `j`: 把結果輸入到 `quickfix` 列表
* `g`: 如果在同一行內有三個符合的結果，則會都顯示

`quickfix`

* `:clist`:顯示 `quickfix`結果
* `cnext(cn)`,`cprevious(cp)`:在 `quickfix`列表中移動

### 3.5.3 在說明文件中搜索

```vim
:helpgrep pattern [@LANG]
" @LANG，可以指定說明文件的語言，例子：
:helpgrep completion@en
```

如果是新增加的文件，可以用下面的指令生成文件tags
```vim
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

```vim
:sign define name arguments
```

定義標記列顏色
```vim
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
```vim
:mkview file
:mksession file

:set viewdir=$HOME/.vim/views  " 設定視圖存放的目錄

" 載入視圖方式
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

```vim
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

```markdown
Level1
====== 

Level2
------

### Level3
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
```vim
:set paste
:set nopaste
:set pastetoggle

```


5.3 使用外部工具格式化
-----------------------

使用 其他程式來排版，像是 Indent,Berkeley Par,Tidy

```vim
" 設定 indent
:set equalprg=program
```

Tidy 是用來排版 XML,HTML 文件的工具。

```vim
" XML 文件
au FileType xml exe ":silent 1,$!tidy --input-xml true --indent yes -q"
" HTML 文件
au FileType html,htm exe ":silent 1,$!tidy --indent yes -q"
```

5.4 小結
--------

本章介紹了一些排版的方式



Ch6: BASIC VIM SCRIPTING 基本 Vim Scripting
===========================================

Vim可以透過 VimScript使用許多功能，且容易分享， 
而且還可以支援外部語言，如python,ruby,perl,lua...

6.1 語法配色 syntax-color scheme
--------------------------------

syntax-color scheme會將程式中的 關鍵字以不同的顏色表示，

不僅使程式易讀、而且可以容易發現打錯的字。

語法上色，先要找出關鍵字，然後設置對應的顏色，以下是例子：

```vim
:syntax match myComments "/\*.*\*/"
:syntax keyword myVars x y
:syntax match mySymbols "[{}();=]"
:syntax keyword myKeywords if return
:highlight myVars ctermfg=red guifg=red
:highlight mySymbols ctermfg=blue guifg=blue
:highlight myKeywords ctermfg=green guifg=green
:highlight myComments ctermfg=yellow guifg=yellow
```


6.2 區域高亮 Syntax regions 
---------------------------

像是注釋之類的，一整個區塊要上色的，例子如下：

```vim
:syntax region myComments start=/\/\*/ end=/\*\//
```

pass


### 6.2.1 Color scheme and syntax coloring 

除了個別指定顏色外，也可以用配色方案中定義的顏色，
這樣的話，可以隨著 color scheme改變語法顏色。


6.3 使用腳本 Using scripts 
---------------------------

除了自已開發功能外，也可以在網路上找別人寫好的plugin回來安裝

* [Vim.org/Script]
* [Github/vim-scripts](https://github.com/vim-scripts)
* [VimAwesome]

### 6.3.1 Script types 

依腳本的功能，有：

* colorscheme, syntax, utility, ftplugin, game, indent, patch...

### 6.3.2 Installing scripts 

安裝 VimScript 的方式，最基本的就是把 `.vim` 丟到 `$HOME/.vim/` 的目錄下，

不過，有些 plugins 檔案太多，於是目前就有一些比較方便的安裝管理方式：

* `.vim`，或是壓縮檔：直接(解壓)放到 `$HOME/.vim/` 目錄下
* Vimball格式: 是壓縮檔，安裝完 [Vimball] 後， `$vim something.vba` `:so %` 安裝 
* Vim Plugin Manager: 專門管理plugins的程式，可以直接從 github 上安裝腳本
    * [pathogen] : 主要是 runtime path manager 
    * [Vundle] : 滿多人用的，vimrc設定 github名字後，可以直接打 `:PluginInstall` 安裝
    * [Vim-plug] : 多了on-demand loading ，應該可以加快vim開啟的速度
    * [談談 vim plugin-manager](https://ssarcandy.tw/2016/08/17/vim-plugin-manager/)




[Vimball]: https://www.vim.org/scripts/script.php?script_id=1502 "vim-based archiver: builds, extracts, and previews"
[Vundle]: https://github.com/VundleVim/Vundle.vim "Vundle, the plug-in manager for Vim"
[Vim-plug]: https://github.com/junegunn/vim-plug "Minimalist Vim Plugin Manager"
[pathogen]: https://github.com/tpope/vim-pathogen "pathogen.vim: manage your runtimepath"


### 6.3.3 Uninstalling scripts 

移除的方式就直接和安裝方式相關，

通常是把 `.vim`下的檔案移除，再把 vimrc內的設定去掉。

6.4 腳本開發 Script development 
--------------------------------

寫自己想要的功能。

在開發腳本時，可能要注意各個Vim的版本，在各平台上可用的功具、函數可能也不用，
在寫腳本時，要注意，另外一些功能最好也保留可以讓用戶修改的功能，保留彈性。

### 6.4.1 Script writing basics 
#### Types

VIM下只有字串、和數值

**數值**包括：

* 十進位數字: 1,2,3,...,100
* 十六進位: 0x01, 0x02,0x64
* 八進位: 01,02,03,..., 0144
* 浮點數 float: 3.1415

例：

```vim
:echo 10 + 0x10 + 010
```


**字串**

* 用單、雙引號包起來的字符: `" " , ' '`
* \\ 是 Escape character
* `\n` 是換行(new line)，`\r`是 Return ,`\t`是Tab, `\<CR>是 Return` 其他的符號 參照下面連結

[C語言中的 Escape sequences](https://en.wikipedia.org/wiki/Escape_sequences_in_C)

#### 變數 Variables 

1. 字串 String: 字符的集合
2. 數值 Number: 前面所述的十、十六、八進位的數字
3. List: An ordered sequence of items (an ordered array)
4. 字典 Dictionary: An unordered associative array holding key-value pairs
5. 函數參照 Funcref: A reference to a function 

定義變數，都是用 `:let` 來賦值的


```vim
:let myvar=somevalue

:let myvalue=100  "數值
:let mystring="this is a test" " 字串
```

型值會自動轉換
```vim
:let myvar='123'
echo myvar-23   " 會顯示100
```

字串經過數值運算會轉成數字。另有，型值強制轉換函數 `string()`
```vim
:let myunber=mystring+0
:let mystring=string(mynumber)
```

**List**

list是一群變數的集合。
list[0]是第一個元素。
```vim
:let mylistvar1 = [1, 2.7, 0x04, "six", myvar, [1,2,3]]
```
**字典 Dictionary**

字典是 key-value pairs，鍵和鍵值的互相參照的序列。
```vim
:let mydictvar2 =  {1: "one",2: "two","tens":{0: "ten",1: "eleven"}}
```
key不一定是數值，也不需要照順序。

**函式**

```vim
:let Myfunrefvar= function("Myfunction")
```
* 變量 Myfunrefvar , 綁定到 函數 Myfunction
* 自定變數名以大寫開頭，跟vim內建的變數區別。
 
```vim
:echo  Myfunrefvar()
```

* 使用函數時，函數名後加 ()

**刪除函數**
`delfunction function-name`


函數中使用的變數的 **變數可視範圍 Scope**
變數前的字母，代表變數的作用區域。

<a id="Scope">[Scope]</a>

*  v: Vim predefined global scope
*  g: Global scope
*  b: Buffer scope—only available in the buffer where it was defined
*  t: Tab scope—only available in the Vim tab where it was defined
*  w: Window scope—only available to the current Vim window (viewport)
*  l: Function scope—local to the function it is defined in
*  s: Sourced file scope—local to a Vim script loaded using :source
*  a: Argument scope—used in arguments for functions

Vim中的注釋是以引號開始 \"

```vim
let g:sum=0
function SumNumbers(num1,num2)
    let l:sum = a:num1+a:num2
    "check if previous sum was lower than this
    if g:sum < l:sum
       let g:sum=l:sum
    endif
    return l:sum
endfunction
" test code, this will print 7 (value of l:sum)
echo SumNumbers(3,4)
" this should also print  7 (value of g:sum)
echo g:sum
```

**See Also**:

* [LVtHW:Number](http://learnvimscriptthehardway.stevelosh.com/chapters/25.html)
* [LVtHW:String](http://learnvimscriptthehardway.stevelosh.com/chapters/26.html)
* [LVtHW:Lists](http://learnvimscriptthehardway.stevelosh.com/chapters/35.html)
* [LVtHW:Dictionary](http://learnvimscriptthehardway.stevelosh.com/chapters/37.html)
* [LVtHW:Function](http://learnvimscriptthehardway.stevelosh.com/chapters/23.html)
* [LVtHW:Variable_Scope](http://learnvimscriptthehardway.stevelosh.com/chapters/20.html)

#### Conditions 

If條件式

```vim
if condition1
    code-to-execute-if-condition1-is-true
else
    if condition2
      code-to-execute-if-condition2-is-true
    endif
endif
```

**See Also**:

* `:help if` 向下翻，還有 `while, for, try , catch, throw,final`
* [LVtWY:Conditional](http://learnvimscriptthehardway.stevelosh.com/chapters/21.html)

#### Working with lists and dictionaries

List, Dic 的 [CRUD]

[CRUD」分別為 Create, Read, Update, Delete

**Create**
```vim
:let mylist = [1,2,3,"cat", myvar1]
:let mydicfruit = {'banana':'yellow','apple':'green','orange':'orange'}
```

**Read**

```vim
:echo mylist[0],mylist[-1] " 1  , cat (-1是最後的一個值)
:echo mydicfruit['banana'] " yellow
" 如果 key是[0-9][a-zA-Z][_]的話
:echo mydicfruit.banana  " yellow
```

**Update**

```vim
:let mylist[0]=99 " 
:let mydicfruit['banana']='green' " 
```

**Delete**

```vim
"用 unlet
:unlet mylist[0]
:unlet mydicfruit['banana'] 

" remove()
:call remove(mylist,2)
```

**其他操作**

```vim
:let mylist3 = mylist1 + mylist
:let mylist4 += [5,6,7,8]
" extend() 會把兩個 list 相加
:call extend(mylist3,mylist4)
:echo myilst3 " mylist3會變成 mylist3 + mylist4, mylist4 不變 
" add() list4 加進 list3，變成 list3 的一個元素
:call add(mylist3,mylist4)
```

**See Also**:

* `:help Dictionary, List`
* `:help get(), has_key(), items(), keys(), values()`
* `:help add(), extend(), remove()`

[CRUD]: https://en.wikipedia.org/wiki/Create,_read,_update_and_delete "Create, read, update and delete"

#### Loops

**For Loops**

```vim
for item in mylist
   call remove(mylist, 0)
endfor
```

**While Loops**

```vim
:let lnum = 1
:while lnum <= line("$")
	:call FixLine(lnum)
	:let lnum = lnum + 1
:endwhile
```

**See Also**:

* `:help break` : 離開 loop
* `:help continue` : 開始下一個loop

#### Creating functions 

<!---
Markdown沒有適合的語法，這邊用HTML的語法，注釋也是
-->

<dl>
  <dt>函數的定義</dt>
  <dd>
<pre>
function Name (arg1, arg2, ... argN) keyword
	code-to-excute-when-func-call
endfunction
</pre>
</dl>

**keyword**

* dict: 把函數綁定到一個 dict
* range: 函數的作用範圍
* 特別的變數: `a:000` 代表所有 argX的集合

**Scope**
通常函數是local的，可以在函數前加 `g:`以代表全域函數。
這邊參照 

[Scope變數值域](#Scope)


#### Variable argument list

* `:help a:000: 所以參數集合，是 List 型態
* `a:0`: 參數個數
* `a:1`: 第一個參數名字，其他以此類推 a:2, a:3...

**See Also**:
* `:help function-argument`
* `:help local-variables` 
* `:help function-lsit` 



6.5 小結 Summary 
=================

VimScript 的安裝、移除，管理。

基本的資料型態、結構、操作。


Ch7: EXTENDED VIM SCRIPTING 進階 Vim Scripting
==============================================

本章會介紹 Script的結構，技巧、如何除錯、使用其他外部語言。

## 7.1 Script structure 

### 7.1.1 Script header 

腳本前最好加上一個檔頭，說明腳本的一些基本資料。
例：作者、日期、版本，以及 著作權授權聲明。

* [Open Source License](https://www.gnu.org/licenses/license-list.html)
* [CreativeCommons](https://creativecommons.org/licenses/?lang=zh_TW)

像是：
```vim
" myscript.vim  : Example script to show how a script is structured.
" Version       : 1.0.5
" Maintainer    : Who Who <who@what.com>
" Last modified : 01/01/2007
" License       : This script is released under the Vim License.
```

### 7.1.2 Script-loaded check 

腳本在執行前，最好先檢查腳本是否正常載入，以免發生問題。

ex: 如果腳本載入不成功，會先把函數先缷載，
把loaded_myscript(是不是要載入腳本)設成true，

```vim
if exists("loaded_myscript")
   delfunction MyglobalfunctionB
   delfunction MyglobalfunctionC
endif
let loaded_myscript=1
```

### 7.1.3 Script configuration 

腳本的開頭可以放設定，如：顏色，路徑…
或是一些設定使用者已有原本的設定，
可以檢查是否已有原本的設定值，再決定要不要取代原本的設定。

### 7.1.4 Key mappings 

修改按鍵設定，尋找是否有舊的設定，決定取代、或建立新的設定。

這邊有些新的代碼：

* `hasmapto()`: 檢查是否有maping 對映到你的程式
* `<unique>`: 檢查 mapping是否唯一
* `<Leader>`: 前導符號，用來開始一些功能的快速鍵。`<Leader>` 會被 全域的 Leader 覆蓋
* `<Plug>`: 建立一個全域、唯一的Mapping。 這樣就不會和全域變數中的其他函數衝突


**See Also**:

* `:help <SID>`: Script ID ?
* `:help <Plug>`
* `:help `script-local`


### 7.1.5 Functions 

`s:MyfunctionA` : 前綴的 `s` 把函數的範圍限定在 script 內。

設定函數的正確的Scope，才不會發現意料之外的問題。


### 7.1.6 Putting it all together 

完整腳本的例子：

pass

**See Also**:

* `:help 'write-filetype-plugin'`
* `:help 'write-compiler-plugin'`
* `:help 'write-library-script'`

## 7.2 Scripting tips 

### 7.2.1 Gvim or Vim? 

Gvim 和 vim有不少不同的地方，如何知道目前執行的是哪一個版本？

```vim
if has("gui_running")
	"execute gui-only command here"
endif
```

**See Also**:

* `:help 'feature-list`


### 7.2.2 Which operating system? 

作業系統間的不同：路徑、檔案存取權限、…

```vim
if has("win16") || has("win32") || has("win64")|| has("win95")
   " do windows things here
elseif has("unix")
   " do linux/unix things here
```

說明文件內的例子：

* macunix                 Macintosh version of Vim, using Unix files (OS-X).
* unix                    Unix version of Vim.
* win32                   Win32 version of Vim (MS-Windows 95 and later, 32 or 64 bits)
* win32unix               Win32 version of Vim, using Unix files (Cygwin)

**See Also**:

* `:help 'feature-list`


### 7.2.3 Which version of Vim? 

Vim版本，ex: Vim 8.0.1626

: 主版號.副版號.補丁編號

```vim
if v:version >= 702 || v:version == 701 && has("patch123")
   " code here is only done for version 7.1 with patch 123 
   " and version 7.2 and above
endif
```

`:if has("patch-7.4.123")`

### 7.2.4 Printing longer lines 

視窗的寬度不少可能超出 80，如果內容太長，
需要函數偵測、防止出錯。

## 7.3 Debugging Vim scripts 

`-D` : 例如， `Vim -D something.txt`，可以印出除錯訊息

`:debug` 用來除錯的命令。

基本上就是，設立中錯點、印出數值，除錯。

## 7.4 Distributing Vim scripts 

依之前的安裝多樣的方式，發布腳本的方向也很多樣。

### 7.4.1 Making Vimballs 

要確定有安裝 [VimBall] []

制作Vimball 的命令是:

`:[range]MkVimball filename.vba`

中間填入需要檔案的路徑、其他設定後。

`:MkVimball myscript.vba` 打包 

## 7.5 Remember the documentation 

Vim說明文件的寫法。

腳本寫好了以後，好的說明文件也是很重要的一部分。

Vim的說明文件，基本上是普通的 text，加上一些記號

**First Line**
`*myscript.txt* Documentation for example script myscript.vim`

文件的第一行，開頭字符號一定要是 `\*` ，兩個`\*`中間是文件檔名， 後面是文件簡述

這邊用書上的例子：

```vim
*myscript.txt* Documentation for example script myscript.vim

Script : myscript.vim - Example script for vim developers
Author : Kim Schulz
Email : <kim@schulz.dk>
Changed : 01/01/2007
=============================================================
											*myscript-intro*

1. Overview

This document gives a short introduction to the example
script myscript.vim.
This script is made as an example for vim users on how to
structure a simple vim plugin script such that it is easy
to read and figure out.
The following is covered in this document:

1. Overview 		|myscript-intro|
2. Mappings 		|myscript-mappings|
3. Functions 		|myscript-functions|
4. Todo 			|myscript-todo|

=============================================================
```

* 首行是特別資訊
* 檔頭資訊
* `\*`myscript-intro`\*` 是連結目標，可以用 `:help 'myscript-intro'`跳到這
* `\|`myscript-intro`\|` 建立類似超連結功能，能快速跳到連結目標
* `\>` Code here`\<` 中間的是Code

寫好文件後，執行：

```vim
:helptags docdir
" docdir 是指向你的文件  `PLUGIN/doc` 
```

**See Also**:

* `:help 'help-translated'`


## 7.6 Using external interpreters 

輸入 `:version` 和以看到目這的Vim技援的外部功能
像是這些，+lua,+perl,+python,+python3,+ruby,-tcl

或是輸入指令，是是否有支援。
`:echo has("perl")`

### 7.6.1 Vim scripting in Perl 

pass

### 7.6.2 Vim scripting in Python 

這邊只看一下比較熟的python。

單行
```vim 
:python3 print("This is  Python3")
```

多行
```vim
:python3 << *endpattern*
some statement here
and here
*endpattern*

" endpattern : 像是 EOF
```

Vim 的的 `vim` 模組，可以讀取vim的資訊
```vim
import vim
window = vim.current.window
window.height = 200
window.width = 10
window.cursor = (1,1)
```

**See Also**:

下面的命令可以用來獲取所有的可用函数列表:
* `:help 'python-vim'`

### 7.6.3 Vim scripting in Ruby 

pass

## 7.7 小結 Summary 

pass

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




參考連結
========

1. [Hacking Vim 7.2 by Kim Schulz April 2010](https://www.packtpub.com/application-development/hacking-vim-72)
2. [HackingVim72簡中](https://github.com/wuzhouhui/hacking_vim)
3. [Vim Tips Wiki](http://vim.wikia.com/wiki/Vim_Tips_Wiki)


**參考書藉**

1. [Learn Vimscript the Hard Way][]
2. [Learn Vimscript the Hard Way\_簡中][Learn Vimscript the Hard Way_簡中]
3. [A Byte of Vim][] 
4. [VimSkill] []

[Vim.org]: https://www.vim.org/ "Vim.org Official Site"
[VimAwesome]: https://vimawesome.com/ "VimAwesome: Gether Vim Plugins"
[Vim.org/Script]: https://www.vim.org/scripts/index.php "Office Site for VimScript"

[VimDoc]: http://vimdoc.sourceforge.net/htmldoc/usr_toc.html "Vim Official Document"
[VimDoc\_zh-CN]: http://vimcdoc.sourceforge.net/doc/ "Vim Official Doc zh_CN"
[Learn Vimscript the Hard Way]: http://learnvimscriptthehardway.stevelosh.com/ "a book for users of the Vim editor who want to learn how to customize Vim."
[Learn Vimscript the Hard Way_簡中]: http://learnvimscriptthehardway.onefloweroneworld.com/ 
 "Learn vimscript the hard way 簡中"
[A Byte of Vim]: https://vim.swaroopch.com/ "help you to learn how to use the Vim editor (version 7)"
[VimSkill]: http://vimskill.readthedocs.io/index.html "VimSkill 簡中文件" 

[VimBall]: https://www.vim.org/scripts/script.php?script_id=1502 "vim-based archiver: builds, extracts, and previews "

