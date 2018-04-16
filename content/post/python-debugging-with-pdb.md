+++
title = "Python Debugging With Pdb"
date = 2018-04-13T21:03:50+08:00
description = "Thank you for choosing After Dark."
draft = true
toc = false
categories = ["technology"]
tags = ["hello", "world"]
images = [
  "https://source.unsplash.com/category/technology/1600x900"
] # overrides the site-wide open graph image
+++

[Python Debugging With Pdb][]
簡單心得 


<!--more-->

# 概述

[pdb][] 是 `pytyon` 內建提供類似 `gdb` 功能，
用來除錯的程式庫。

大概有兩種用法：

1. 直接使用： `python3 -m pdb myscript.py`
2. 在程式內設置中斷點：`import pdb; pdb.set_trace()`


看完文章，你需要學會除錯的動作有：
 
* 一步一步執行程式，或是 執行到某個地方停止，重新開始執行程式
* 監視某個變數的值。


# 直接使用 `pdb`

python 執行程式時，執行 `pdb` 模組
```bash
$python -m pdb myscript.py
```
這樣就會進入互動式除錯模式。按 `h(elp)` 看說明：
[Debugger Commands][]

```
(Pdb) h

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt
alias  clear      disable  ignore    longlist  r        source   until
args   commands   display  interact  n         restart  step     up
b      condition  down     j         next      return   tbreak   w
break  cont       enable   jump      p         retval   u        whatis
bt     continue   exit     l         pp        run      unalias  where

Miscellaneous help topics:
==========================
exec  pdb
```
一些常用指令：

* `h(elp) [command]`: 看指令說明
* b 數字 - 設置中斷點
* r - 繼續執行，直到當前函式返回
* c - 繼續執行程式
* n - 執行下一行程式
* s - 進入函式
* p 變數名稱 - 印出變數
* pp - Pretty-print 
* l - 列出目前的程式片段
* q - 離開

# 在程式內設置中斷點

在程式碼內載內 [pdb][]
```python
import pdb; pdb.set_trace()
```

執行程式後，就會互動除錯模式。

Python 3.7, [PEP 553][] 加入一個比較簡單的除錯內建函式 `breakpoint()`

# 指令說明

TODO








參考連結
--------

1. [Python Debugging With Pdb](https://realpython.com/python-debugging-pdb/)
2. [Python初學起步走-Day30 - 除錯(使用pdb)](https://ithelp.ithome.com.tw/articles/10161849)
3. [Python3 Docs:pdb](https://docs.python.org/3/library/pdb.html)


[Python Debugging With Pdb]: https://realpython.com/python-debugging-pdb/
[pdb]: https://docs.python.org/3/library/pdb.html
[Debugger Commands]: https://docs.python.org/3/library/pdb.html#debugger-commands
[PEP 553]: https://www.python.org/dev/peps/pep-0553/
