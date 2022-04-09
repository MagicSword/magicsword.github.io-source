+++
title = "Python Debugging With Pdb"
date = 2018-04-13T21:03:50+08:00
description = "pdb 函式庫 使用"
draft = false
toc = true
categories = ["technology"]
tags = ["python", "module","debug"]
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

## 顯示

* `l(ist) [first[, last]]`：顯示目前執行的到程式碼，沒加參數的話，就是印出單行
* `ll` long list: 印出多行程式碼，並指出目前執行的到行數
* `p expression`：印出變數
* `pp expression`：印出變數， pretty-printed
* `whatis expression`：印出變數的型態，int or string ...
* `a(rgs)` ：列出目前函數的所有參數

## 程式流程

* `n (next)`：執行程式下一行
* `s (step)`：步進程式
* `c(ont(inue))`：執行到下一個中斷點停止


## 監視變數

* `display [expression]`：監視變數，變數有變動時，就會顯示。
* `undisplay [expression]`：停止監視變數

## 中斷點

* `b(reak) [([filename:]lineno | function) [, condition]]`：設罝中斷點， `b` 不加參數，會列出所有中斷點。
* `tbreak [([filename:]lineno | function) [, condition]]`：暫時中斷點，執行後，就會被移除。
* `cl(ear) [filename:lineno | bpnumber [bpnumber ...]]`清除中斷點
* `disable [bpnumber [bpnumber ...]]`：停用中斷點
* `enable [bpnumber [bpnumber ...]]`：啟用中斷點

## Python Caller ID

pass

## 結語

[pdb][] 是個很好用的工具，熟練使用的話，能輕易找出程式問題。

# 參考連結

1. [Python Debugging With Pdb](https://realpython.com/python-debugging-pdb/)
2. [Python初學起步走-Day30 - 除錯(使用pdb)](https://ithelp.ithome.com.tw/articles/10161849)
3. [Python3 Docs:pdb](https://docs.python.org/3/library/pdb.html)


[Python Debugging With Pdb]: https://realpython.com/python-debugging-pdb/
[pdb]: https://docs.python.org/3/library/pdb.html
[Debugger Commands]: https://docs.python.org/3/library/pdb.html#debugger-commands
[PEP 553]: https://www.python.org/dev/peps/pep-0553/
