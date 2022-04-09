+++
title = "Python Import System"
date = 2018-04-14T14:44:03+08:00
description = "Note for Python Import System"
draft = false
toc = true
categories = ["programming"]
tags = ["python", "module"]
images = [
  "https://source.unsplash.com/category/technology/1600x900"
] # overrides the site-wide open graph image
+++

[How python's import machinery works][] 簡單的筆記，
順便整理一下 [import][] 的資料。


<!--more-->

# 概述

[import][] 就像 C的 `include` ...用來引用其他的程式庫。 
並簡單說明引用的機制、優先順序。

# 名詞解釋

[modules][]:

: `A module is a file containing Python definitions and statements.`
: `modules` 是有 python 程式碼的檔案, 是單一檔案，副檔名是 `.py`，檔案名就是 import name

[packages][]:

: `a way of structuring Python’s module namespace by using “dotted module names”.`
: `packages` 是 `modules` 的集合，import name 通常是 資料夾名。


# 範例檔案結構

假設有個 `package` 長這樣

```bash
tmp/
  my_package/
    __init__.py
    my_module.py
```
`my_module.py`

```python
class MyClass:
    def __init__(self):
        print('init called')

    def caps(self, word):
        print(word.upper())
```


# `import` 方法一

進 `tmp`後，執行 `python`

```bash
$cd tmp
$python
```
通常 `import` 的方式是這樣。
物件產生時，和物件方法執行時，會印出一些訊息。

```python
>>> from my_package import my_module
>>> something = my_module.MyClass()
init  called
>>> something.caps('hello')
HELLO
```
# `import` 方法二：`import_module` 動態載入

先載入 [import_module][] 後，再用它載入其他的 `package`

```python
>>> from importlib import import_module
>>>
>>> my_module = import_module('my_package.my_module')
>>> obj = my_module.MyClass()
init called
>>> obj.caps('hello')
HELLO
```

# 手動載入

[How to import a module given the full path?](https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path#answer-43602557)


# Python module 的載入機制

## `sys.modules` 先找

* `sys.modules` 是 python 執行時會先載入的 module，通常是系統內建的程式庫
* 如果你有把 import my_module , my_module 也會出現在 sys.modules 中。

## `sys.meta_path` 次之

前面的 sys.modules 找不到後，會載入 `sys.meta_path` 物件，開始從 `sys.path` 裡去找你想載入的 packages。

這邊比較需要記得就是 `sys.path` 是放要載入的程式庫的路徑，
所以把你的程式庫路徑加進 `sys.path` 應該就可以找到了。

# 其他

整個 `import` 載入的機制，參考連結說的滿清楚的的，
太細節的部分，之後有空再來細看。

參考連結
--------

1. [Python Docs: 5.The import system](https://docs.python.org/3/reference/import.html)
2. [How python's import machinery works](https://manikos.github.io/how-pythons-import-machinery-works)
3. [import-pypi:import modules form pypi](https://github.com/miedzinski/import-pypi)
4. [StockOverFlow:What's the difference between a Python module and a Python package?](https://stackoverflow.com/questions/7948494/whats-the-difference-between-a-python-module-and-a-python-package)


[import]: https://docs.python.org/3/reference/import.html "access to the code in another module"
[How python's import machinery works]: (https://manikos.github.io/how-pythons-import-machinery-works)
[modules]: https://docs.python.org/3/tutorial/modules.html#modules
[packages]: https://docs.python.org/3/tutorial/modules.html#packages
[import_module]: https://docs.python.org/3/library/importlib.html#importlib.import_module
