+++
title = "Reading The GO Programming Language 1st 2015"
date = 2018-08-11T18:48:36+08:00
description = "The GO Programming Language 1st reading"
draft = true
toc = true  # by after-dark
categories = ["programming"]
tags = ["reading", "golang"]
pre ="<i class='fa fa-file'></i> "
type="page" # set "slide" to display it fullscreen with reveal.js
images = [
  "https://source.unsplash.com/category/technology/"
] # overrides the site-wide open graph image
+++

The GO Programming Language 1st 簡單筆記


<!--more-->

Task list: :smile:

- [x] 初稿
- [ ] 再讀
- [ ] 筆記
- [ ] 完成


# 資料

![The Go Programming Language](https://images-na.ssl-images-amazon.com/images/I/516R4ZoMqBL._SX402_BO1,204,203,200_.jpg)

* [The Go Programming Language][]
* [@Amazon](https://www.amazon.com/Programming-Language-Addison-Wesley-Professional-Computing/dp/0134190440)
* by Alan A. A. Donovan (Author), Brian W. Kernighan 
* Series: Addison-Wesley Professional Computing Series
* Paperback: 400 pages
* Publisher: Addison-Wesley Professional; 1 edition (November 5, 2015)
* Language: English
* ISBN-10: 0134190440
* ISBN-13: 978-0134190440
* Product Dimensions: 7.4 x 1.1 x 9 inches

![精通 Go 程式設計](https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/E05/002/52/E050025233.jpg&w=300)

* [@博客來](https://www.books.com.tw/products/E050025233)
* 精通 Go 程式設計 (電子書)
* The Go Programming Language
* 作者： Alan A. A. Donovan, Brian W. Kernighan
* 譯者： 楊尊一
* 出版社：碁峰
* 出版日期：2016/08/31
* 語言：繁體中文
* 定價：406元
* ISBN：9789864761333
* 規格：普通級 / 初版
* 出版地：台灣
* 檔案格式：EPUB固定版型
* 建議閱讀裝置：平板
* 檔案大小：76.2MB
* 本書分類：電腦資訊> 程式設計> 其他




# 目錄

* Chapter 01 基本入門
* Chapter 02 程式結構
* Chapter 03 基本資料型別
* Chapter 04 組合型別
* Chapter 05 函式
* Chapter 06 方法
* Chapter 07 介面
* Chapter 08 Goroutine 與 Channel
* Chapter 09 共用變數並行性
* Chapter 10 套件與工具
* Chapter 11 測試
* Chapter 12 反射
* Chapter 13 低階程式設計


# 心得筆記 

## 前言

* Go 發表於 2009 年 11 月 10 日，[Google](google) 開發
* Golang 特點："Go is a statically typed, compiled language in the tradition of C, 
  with memory safety, garbage collection, structural typing, and CSP-style concurrency." 
  from [Wikipedia](golang.wiki)
* [CSP(communicating sequential processes)](https://en.wikipedia.org/wiki/Communicating_sequential_processes)
  ，Tony Hoare 1978 的論文，用以說明並行性概念。
* 在 CSP 中，程式由平行的子程序組成，彼此無共用狀態。子程序間利用 channel 溝通及同步化。
 

## Chapter 01 基本入門

## Chapter 02 程式結構
## Chapter 03 基本資料型別
## Chapter 04 組合型別
## Chapter 05 函式
## Chapter 06 方法
## Chapter 07 介面
## Chapter 08 Goroutine 與 Channel
## Chapter 09 共用變數並行性
## Chapter 10 套件與工具
## Chapter 11 測試
## Chapter 12 反射
## Chapter 13 低階程式設計





# Docdock

### Alert

{{% alert theme="info" %}}**this** is a text{{% /alert %}}
{{% alert theme="success" %}}**Yeahhh !** is a text{{% /alert %}}
{{% alert theme="warning" %}}**Be carefull** is a text{{% /alert %}}
{{% alert theme="danger" %}}**Beware !** is a text{{% /alert %}}


### attachments

建 page 同名的 page.file 目錄，下面可以放檔案


### button

{{< button href="https://google.com" >}} go to google {{< /button >}}
{{< button href="https://google.com" theme="success" >}} Success {{< /button >}}
{{< button href="https://google.com" theme="info" >}} Info {{< /button >}}
{{< button href="https://google.com" theme="warning" >}} Warning {{< /button >}}
{{< button href="https://google.com" theme="danger" >}} Danger ! {{< /button >}}
{{< button href="https://google.com" theme="default" >}} Danger ! {{< /button >}}

### children

例出下屬的 children 頁面列表，可以作出卡片式的 列表。

{{% children depth="3" showhidden="true" %}}

### excerpt


{{%excerpt%}}
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation **ullamco** laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in _reprehenderit in voluptate_
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
{{% /excerpt%}}
　
### excerpt-include

從檔案引用內容 

### expand

可收起隱藏內容

{{%expand "Is this docdock theme rocks ?" %}}Yes !.{{% /expand%}}

### icon

{{< icon name="film" size="large" >}}

### Mermaid

{{<mermaid align="left">}}
graph LR;
    A[Hard edge] -->|Link text| B(Round edge)
    B --> C{Decision}
    C -->|One| D[Result one]
    C -->|Two| E[Result two]
{{< /mermaid >}}


### Notice

Note
{{% notice note %}}
A notice disclaimer
{{% /notice %}}


Info 
{{% notice info %}}
An information disclaimer
{{% /notice %}}

Tip 
{{% notice tip %}}
A tip disclaimer
{{% /notice %}}

Warning 
{{% notice warning %}}
An warning disclaimer
{{% /notice %}}


### panel

可以把一些內容加框

{{% panel footer="panel footer" %}}Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.{{% /panel %}}


### revealjs

[reveal.js](http://lab.hakim.se/reveal-js/)  Slide





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


## 區塊元素


 ** List **

* AAA
	* BBB
* CCC


1. what
2. some
3. soso




# 標題


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


# 連結

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


# 圖片、其他、youtube

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

# 程式碼


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

1. [gopl.io](http://www.gopl.io/)
2. [gopl example code](https://github.com/nasciiboy/TGPL)

[google]: "https://www.google.com" "Search Engine"
[golang]: "https://golang.org/" "The Go Programming Language"
[golang.wiki]: "https://zh.wikipedia.org/wiki/Go" "Go (programming language)"
