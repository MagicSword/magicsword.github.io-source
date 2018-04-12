+++
title = "Picon: 在互動的環境下執行 Python 程式碼"
date = 2018-04-13T02:36:19+08:00
description = "Run your code in python interactive console from the command line"
draft = false
toc = true
categories = ["technology"]
tags = ["commandline", "python", "vim"]
images = [
  "https://source.unsplash.com/category/technology/1600x900"
] # overrides the site-wide open graph image
+++

可以在即時在編輯器看到程式碼執行的結果。

 

<!--more-->

# 概述

[picon][] 實際上的用法，看作者的圖可能比較清楚。

![Picon in Vim by gokcehan](https://camo.githubusercontent.com/88d5900dd1f78cb0133411865ab6c99fe9356910/68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f386342684d5a74417934763059644d72514a2f67697068792e676966)



# 安裝

```bash
$pip install picon
```

# 用法

[picon][] 的用法大概有三種：

1. Default: `picon example.py`
    讀進 exampley.py 的內容，以互動模式輸出，
    有點像直接把 example.py 的內容貼到 ipython
2. Live or `-l`: `picon example.py -l`
    同預設模式，不過更像是 ipython 的輸出
3. Append mode or `-a`: `picon example -a`    
    輸出的行開頭多了 `#|` ，這個模式下的輸出，
    可以直接被編輯器讀取。

# 語法

python 互動命令列的語法跟正常的 python 語法有點不同。
在互動模式下，變數不用加 `print` ，會直接印出。

```python
    $ cat return.py
    x = 42
    x
    print x
    $ python return.py
    42
    $ picon return.py
    42
    42
```

第二，區塊。在 python 中，有同樣縮排的，就算中間多了一個空行，
還是視為同一階層。但是在 [picon][] ，中間隔了空行，就視為新的區
塊。

```python
    $ cat block.py
    if True:
        print 'one'

        print 'two'
    $ python block.py
    one
    two
    $ picon block.py
    one
      File "<console>", line 1
        print 'two'
        ^
    IndentationError: unexpected indent
```


# Vim 整合

`:%!picon -a`： Vim打開程式碼後，在命令模式下執行 `:%!picon -a` ，
即可看到執行的結果以註解出現在下一行。

`Picon` 指令： 保留游標的位置 和 把 picon 所作的變動合到一個 undo 的步驟中。
之後，只要執行 `Picon` 即可。

    command! Picon exe 'normal m`' | silent! undojoin | exe '%!picon -a' | exe 'normal ``'


還可以在這**寫入buffer**, **發呆**，兩個事件時，自動執行 `Picon`
，詳細的指令，可以查 `:help updatetime`

    autocmd Filetype python autocmd BufWritePre <buffer> Picon
    autocmd Filetype python autocmd CursorHold <buffer> Picon




參考連結
--------

1. [Picon](https://github.com/gokcehan/picon)

<!-- Links -->
[picon]: https://github.com/gokcehan/picon "Run your code in python interactive console from the command line"

