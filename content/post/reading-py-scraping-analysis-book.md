+++
title = "Reading Python Scraping Analysis Book"
date = 2019-05-19T20:23:00+08:00
description = " Python：網路爬蟲與資料分析入門實戰 "
draft = false
toc = true  # by after-dark
categories = ["technology"]
tags = ["python", "scraping","spider"]
pre ="<i class='fa fa-file'></i> "
type="page" # set "slide" to display it fullscreen with reveal.js
images = [
  "https://source.unsplash.com/category/technology/"
] # overrides the site-wide open graph image
+++

Python：網路爬蟲與資料分析入門實戰 簡單筆記

python, beautifulsoup, api, scrapy,...

<!--more-->

 * 書名：Python：網路爬蟲與資料分析入門實戰
 * [博客來] (https://www.books.com.tw/products/0010800867)
 * 作者： 林俊瑋, 林修博  
 * 出版社：博碩  
 * 出版日期：2018/10/04
 * 語言：繁體中文
 * 定價：450元
 * ISBN：9789864343386
 * 規格：平裝 / 256頁 / 17 x 23 x 1.28 cm / 普通級 / 單色印刷 / 初版
 * 出版地：台灣
 * 本書分類：電腦資訊> 資料庫/大數據> 資料處理/大數據
 * 本書分類：電腦資訊> 程式設計/APP開發> Python


Task list: :smile:

- [x] 初稿
- [ ] 再讀
- [ ] 筆記
- [ ] 完成
- 05/19 到 2-3


# 概述

邊讀邊做個筆記心得。


# Chapter 01 環境設定與網頁爬蟲初探

 * 1-1 環境設定及套件安裝：Anaconda
 * 1-2 使用IDE：PyCharm
 * 1-3 使用Jupyter Notebook
 * 1-4 網頁文件解構與網頁爬蟲初探
    * Anaconda 在 Windows 上算是個滿不錯的 Python 整合套件。
    * Editor: Vim , Visual Studio Code
    * IDE: PyCharm
    * Jupyter Notebook 算是個 Ipython Web App，滿好用的。
    * 網頁文件有幾個部分： Html 內容，CSS 樣式，JS 動態
    * 書中用來讀網頁的程式庫是 requests，算是外部程式庫中簡單好用的。
      Python 中內建的也是有 [urllib] (https://docs.python.org/3/library/urllib.html) 。




# Chapter 02 Beautiful Soup 講解與網頁解構

## 2-1 不要重複造輪子：寫爬蟲之前

不過當你想要自已動手打造輪子前，可能要先研究一下：

* API：是不是有已經整理好資料了？
* 分析網址連結規則：可以少花一些力氣
* AJAX ： 用 JavaScript  傳送的資料，沒辦法直接取得

Chrome 下按 `F12` 開發者工具 ，可以了解  Browser 和 Server 間到底聊什麼？

## 2-2 Beautiful Soup 重要功能 (find(), find_all(), .text, .stripped_strings)

[BeautifulSoup] :

> 是 Python 程式庫，用來解析 HTML/XML 文件
> 把 文本 轉成樹狀結構(？)
> bs4 可以用的 Parser(解析器) : html.parser(Python內建), html5lib, lxml(最快) 
> 之後用 `bs4` 簡寫

也就是把糊成一團的文件，整理成程式可以拿來用的資料。

 `requests` : 讀入網頁, 並處理網路協定的問題，登入，session, cookie, ....

```python
import requests
from bs4 import BeautifulSoup

resp = requests.get('https://jwlin.github.io/py-scraping-analysis-book/ch1/connect.html')
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup.find('h1').text)

```

讀進網頁，分析完後，重要的是要如何定位想要的東西。

1. 方法一：從頭到尾爬一遍： `find()`, `find_all()`
2. 方法二：直接選出樹狀結構中的位置：
    1. CSS Selector : `.select()` 
    2. XPath (XML Path Language，XML 路徑語言) :
    3. 效能上 [CSS Selector 大於 XPath 一些][CSSvsXPath]

* `.text`: Tag 所夾的文字
* `stripped_strings`: bs4 的方法，會把物件內容的所有 Tag 清除，留下文字，移除前後空白換行，要注意的是。這個是 generator 物件


## 2-3 網頁結構巡覽（parent, children, siblings）

除了用暴力法找以外，也可以從已找到的元素的 親層(parent)、子層(children)、兄弟層(siblings) 移動


## 2-4 正規表示式 (Regular Expression)

   

# Chapter 03 網頁爬蟲範例實戰
3-1 PTT 八卦板今日熱門文章
3-2 Yahoo 奇摩電影本週新片
3-3 兩大報當日焦點新聞
3-4 Google 搜尋股價資訊
3-5 Dcard 今日熱門文章

# Chapter 04 使用 API
4-1 API 簡介
4-2 PTT 八卦板眾來源分佈 (ipstack.com)
4-3 IMDB API
4-4 Google Maps APIs (Google Geocoding/Places API)
4-5 Dcard API

# Chapter0 5 資料儲存
5-1 儲存圖片與多媒體檔案
5-2 儲存資料到 CSV 檔
5-3 儲存資料到資料庫 SQLite

# Chapter 06 不同編碼與類型的文件
6-1 非 UTF-8 編碼的文件
6-2 XML 文件

# Chapter 07 進階爬蟲議題
7-1 處理表單及登入頁 ：台灣高鐵時刻查詢
7-2 處理表單及登入頁 ：Yelp 登入
7-3 使用WebDriver：台銀法拍屋資訊查詢
7-4 爬蟲程式經驗談：被封鎖的常見原因、常用 Header 欄位、網站隱藏欄位、使用代理伺服器

# Chapter 08 資料分析實戰
8-1 台股每日盤後資訊爬蟲及策略回測（量化投資）
8-2 電影評論情緒分析（中文自然語言處理與機器學習）
8-3 商品特價 Gmail 通知：Costco 商品網頁

# 附表 本書範例目標網站列表

附錄A 在 Mac 安裝Anaconda 開發環境

附錄B Python 爬蟲框架Scrapy 入門教學
B-1 Scrapy 環境安裝
B-2 簡易部落格爬蟲
B-3 Scrapy 系統架構
B-4 博客來網路書店爬蟲









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


https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# 參考連結

1. [作書網站](https://jwlin.github.com/py-scraping-analysis-book/ch2/blog/blog.html)
2. [本書Github](https://github.com/jwlin/py-scraping-analysis-book)
3. [BeautifulSoup 文件] [BeautifulSoup]
4. [R 語言使用者的 Python 學習筆記系列 第 16 篇:[第 16 天] 網頁解析](https://ithelp.ithome.com.tw/articles/10186119)
5. [Nightwatch101 #5：使用 CSS Selector 定位網頁元素](https://cythilya.github.io/2017/12/15/nightwatch-css-selector/)
6. [Nightwatch101 #6：使用 Xpath 定位網頁元素](https://cythilya.github.io/2017/12/16/nightwatch-xpath/) 
7. [CSS selector vs XPath][CSSvsXPath] 


[google]: https://www.google.com "Search Engine"
[BeautifulSoup]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/ "解析 HTML/XML"
[CSSvsXPath]: http://elementalselenium.com/tips/34-xpath-vs-css-revisited-2 "Css Vs. X Path, Under a Microscope"
