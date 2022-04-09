+++
title = "Reading Vim Text Objects the Definitive Guide"
date = 2019-05-20T16:44:11+08:00
description = "Vim Text Object the Definitive Guide 筆記"
draft = false
toc = true  # by after-dark
categories = ["technology"]
tags = ["reading", "vim","editor"]
pre ="<i class='fa fa-file'></i> "
type="page" # set "slide" to display it fullscreen with reveal.js
images = [
  "https://source.unsplash.com/category/technology/"
] # overrides the site-wide open graph image
+++

Vim Text Object，vim 裡的文字物件，操作方式。


<!--more-->

Task list: :smile:

- [x] 初稿
- [ ] 再讀
- [ ] 筆記
- [ ] 完成



# 概述

[Vim Text Objects: The Definitive Guide][VimtextobjectsTDG]

本文讀完上面的文章後，一些心得筆記。

Vim 裡文字可分為一些單位來操作： character, word, sentence, paragraph, 
(或是程式中的 function, class,...，又或者用 plugin 自定義結構)

# 語法結構



* [number] < command >[text object or motion]

    * **number** 是用來描述動作的次數，像是： `3dd`, 作 `dd` 這個動作3次，可以省略，前置、或後置 
    * **command** 動作，像是：change, delete(cut), copy(yank)，主要是編輯動作
    * **text object**，文字單位，像是：word, setence, paragraph
    * **motion** 移動，不改變內容， foward, backward, end of the line

一般的編輯命令，主要的結構就是上述的 編輯命令 + 文字物件 ，或是移動動作，
像是：刪除一行，移到文章末。

# 文字物件

上面有提到的文字物件，就是 Vim 中編輯動作操作的對象，一個字，一句，一段，整篇文章，…

大概可以分成幾種討論：

1. plaintext text object 純文字文字物件： word,  setence, paragraph
2. motion 移動動作：移動遊標，內容不變
4. 程式語言的文字物件： function, class
3. 自定義的文字物件：...

## 純文字文字物件

### Word


**範圍選擇**：i(inner ) 和 a(around)

* inner，不包括兩邊的空白
* around，除了內容外，還有兩邊的空白

例子：The quick brown fox jumps over the lazy dog , 如果遊標在 brown

* `diw` : 刪掉 brown 
* `daw` : 刪掉 brown ，和 兩邊的空白 


**文字物件** 

* w (word)
* s (sentence)
* p (paragraph)
* t (tag)
* 引號、括號包住的內容 。


**動作指令**

* c (change)
* d (delete)
* y (yank)
* v (visual block)



```

[VimText](http:://vim.org)

```

在 VimText 處，輸入 `ci[`，就可以改變 括號的內容。

```

<div id="content">what a name</div>

```

* dit : 會刪除 what a name
* di> : 會刪除 角括號 內的內容


## 自訂文字物件

### CamelCaseMotion

[CamelCaseMotion][CamelCaseMotion] 

[CamelCase][CamelCase] :

> 駝峰式大小寫，多個單字連結新識別名稱，每個單字的第一字母大寫。
> 出自 Larry Wall等人所著的暢銷書《Programming Perl》

* 小駝峰式命名法（lower camel case）：
第一個單字以小寫字母開始；第二個單字的首字母大寫，例如：firstName、lastName。
* 大駝峰式命名法（upper camel case）：
每一個單字的首字母都採用大寫字母，例如：FirstName、LastName、CamelCase，也被稱為 **Pascal命名法**（英語：Pascal Case）。

而上面的 plugin 就是用來處理 CamleCase

### function auguments

https://github.com/vim-scripts/argtextobj.vim

### Ident Object

https://github.com/michaeljsmith/vim-indent-object

### Ruby Block

Ruby Block https://github.com/nelstrom/vim-textobj-rubyblock


# 結語

Vim Text Object 可以精確的指出動作的目標。
熟悉使用，可以讓Vim的編輯動作變快。



# 參考連結

1. [Vim Text Objects: The Definitive Guide][VimtextobjectsTDG]
2. [VIM学习笔记 文本对象（Text Objects）](http://yyq123.blogspot.com/2016/12/vim-text-objects.html)
3. [A vim script to provide CamelCase motion through words][CamelCaseMotion]
4. [vim 杂谈 - 关于快速编辑](https://zhuanlan.zhihu.com/p/25999103)

[google]: https://www.google.com "Search Engine"
[VimtextobjectsTDG]:  https://blog.carbonfive.com/2011/10/17/vim-text-objects-the-definitive-guide/ "Vim Text Objects: The Definitive Guide"
[CamelCaseMotion]: https://github.com/bkad/CamelCaseMotion "A vim script to provide CamelCase motion through words"
[CamelCase]: https://zh.wikipedia.org/wiki/%E9%A7%9D%E5%B3%B0%E5%BC%8F%E5%A4%A7%E5%B0%8F%E5%AF%AB "駝峰式大小寫"
