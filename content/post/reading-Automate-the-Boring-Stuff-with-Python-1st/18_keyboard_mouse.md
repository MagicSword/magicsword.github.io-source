+++
title = "Chapter 18 以 GUI 自動化來控制鍵盤和滑鼠]"
date = 2018-04-21T18:35:25+08:00
description = "pyautogui 控制 keyboard, mouse"
draft = true
toc = false
categories = ["programming"]
tags = ["reading", "python","automation","automatestuff"]
images = [
  "https://source.unsplash.com/category/technology/1600x900"
] # overrides the site-wide open graph image
+++

* 沒有相應的程式庫時，可以模擬鍵盤、或滑鼠動作，直接操作 GUI 的得到相對的功能。


<!--more-->

Task list: :smile:

- [x] 初稿
- [ ] 再讀
- [ ] 筆記
- [ ] 完成


# 概述


**GUI Library**

[UI Automation tools ratings](https://github.com/pywinauto/pywinauto/wiki/UI-Automation-tools-ratings) 

 GitHub (number of stars)(2018, April, 01)


1. [AutoHotkey (C++)](https://github.com/Lexikos/AutoHotkey_L/) - 1 652
2. [pyautogui](https://github.com/asweigart/pyautogui) - 1 630
3. [sikuli](https://github.com/sikuli/sikuli) - 1 387
4. [autopy](https://github.com/msanders/autopy/) - 856
5. [TestStack.White (C#)](https://github.com/TestStack/White) - 797
6. [pywinauto](https://github.com/pywinauto/pywinauto) - **773**

 StackOverflow (number of tagged questions)
1. [AutoHotkey](http://stackoverflow.com/questions/tagged/autohotkey) - 2663 (73.3% answered)
2. [AutoIt](http://stackoverflow.com/questions/tagged/autoit) - 1627 (64.1% answered)
3. [sikuli](http://stackoverflow.com/questions/tagged/sikuli) - 673 (53.6% answered)
4. [pywinauto](http://stackoverflow.com/questions/tagged/pywinauto) - **329** (61.4% answered)
5. [pyautogui](http://stackoverflow.com/questions/tagged/pyautogui) - 231 (36.4% answered)

* AutoHotkey: 是用自己的語法
* Python: 有 pyautogui,pywinauto,autopy(python2，較舊)

PyAutoGUI vs PyWinAuto [Python PyAutoGUI和Pywinauto区别及安装](https://blog.csdn.net/huangzhang_123/article/details/58588362)

> 首先，这两者最大共同点就是可以操作计算机，模拟人工输入和鼠标操作等等。不过这两者也有侧重点，PyAutoGUI侧重于鼠标，键盘，截图，消息框的功能，Pywinauto侧重对CS的操作，虽然都有键盘，鼠标等模拟输入，不过最核心还是软件上的操作比较多。可以说各有所长。

* 程式送出的鍵盤、滑鼠信號很快，不像手動的速度，所以記得留下檢查點
* 藉由登出來關閉所有程式，或  `kill -9` ?

**暫停與失效安全保護**

* `pyautogui.PAUSE = 1.5` 暫停 1.5 秒
* 把遊標移出畫面， 會觸發 pyautogui 的異常，會暫停程式
* 關掉失效保護功能：`pyautogui.FAILSAFE = False`

## 控制滑鼠移動

* 畫面左上為原點 (0,0) ，向右 X 軸 正，向下 Y 軸 正

![1920×1080](https://automatetheboringstuff.com/images/000011.jpg)

```python
>>> import pyautogui
>>> pyautogui.size()
(1920, 1080)
>>> width, height = pyautogui.size()
```

**取得滑鼠位置**

```python
>>> pyautogui.postion()
(311,32) # 傳回目前游標座標
```

**移動滑鼠游標**

`pyautogui.moveTo(xpos,ypos,duration=xxsec)`:
`duration`是每次移動幾秒，直到到達目的座標

`pyautogui.moveRel(xdis,ydis,duration=xxsec)`
: 相對座標移動


## 程式：目前的游標位置

```python
import pyautogui
print('Press Ctrl-C to quit')

try:
    while True:
        x,y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        # str.rjust() 字串向右對齊
        print(positionStr,end='')
        print('\b'*len(positionStr), end='', flush=True)
        # 字串印出後，用等長的 Backspace 刪除，並 flush
except KeyboardInterrupt:
    print('\nDone.')
```

## 控制滑鼠游標的互動

**Click**

* Click : mosueDown, mouseUp


```python
pyautogui.click(xpos,ypos,button='left') # right,middle,left
pyautogui.click(xpos,ypos)
pyautogui.mouseUp()
pyautogui.mouseDown()
pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.middleClick()
```

**Drag  and Drop**

* Drag : mouseDown()(一般是左鍵) -> 移動游標 
* Drop : (在 Drag狀態下)移動游標  -> mouseUp()

* pyautogui.dragTo(xpos,ypos) : 絕對座標
* pyautogui.dragRel(xpos,ypos): 相對座標
















# 語法

樣式可以用 星號\* 或是 底線\_

斜體 emphasis, aka italics, with *asterisks* or _underscores_.
粗體 Strong emphasis, aka bold, with **asterisks** or __underscores__.
合併 Combined emphasis with **asterisks and _underscores_**.
刪除線 Strikethrough uses two tildes. ~~Scratch this.~~


孔子說：

> 說什麼

定義是：

: 是什麼


# 目錄

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

```md
    ![Alt text](/path/to/img.jpg)

    ![Alt text](/path/to/img.jpg "Optional title")
```


參考式的圖片語法則長得像這樣：
```md
    ![Alt text][id]
```

「id」是圖片參考的名稱，圖片參考的定義方式則和連結參考一樣：

```md
    [id]: url/to/image  "Optional title attribute"
```


### Markdown Anchor

markdown預設 H1,H2的 id就是 text

```html
<h1 id="MyAnchorName">My Title</h1>
```

自定錨
```html
<a id="MyAnchorName">My Title</a>
```

連結語法

```html
<a href="#MyAnchorName">My Content</a>
```

```markdown
[create an anchor](#MyAnchorName)
```

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


# 參考連結


1. [Automate the Boring Stuff with Python 作者網站](https://automatetheboringstuff.com/)

[Automate the Boring Stuff with Python]: https://automatetheboringstuff.com/

