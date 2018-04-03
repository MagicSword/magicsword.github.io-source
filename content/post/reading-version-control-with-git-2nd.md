+++
title = "Reading Version Control With Git 2nd"
date = 2018-04-01T23:06:34+08:00
description = "Version Control with Git,2nd  簡單心得"
draft = true
toc = true
categories = ["Technology"]
tags = ["reading", "git"]
images = [
  "https://source.unsplash.com/category/technology/1600x900"
] # overrides the site-wide open graph image
+++

[Version Control with Git, 2nd Edition](http://shop.oreilly.com/product/0636920022862.do)
簡單的一些筆記。 

<!--more-->

![Version Control with Git, 2nd Edition](https://covers.oreillystatic.com/images/0636920022862/cat.gif)

[Version Control with Git, 2nd Edition](http://shop.oreilly.com/product/0636920022862.do)
<BR> Powerful tools and techniques for collaborative software development

- By Jon Loeliger, Matthew McCullough
- Publisher: O'Reilly Media
- Release Date: August 2012
- Pages: 456

[版本控制使用Git 第二版](https://www.kingstone.com.tw/book/book_page.asp?ActID=alsobuy&LID=se_base001&KMCode=2014713380050#detaildata)

- 編／譯者：吳曜撰



[Exercise Codes](https://github.com/terryjbates/version-control-with-git)


概述
========




## Ch 1

* Git by Linus Torvalds at 2005，主要是用於 Linux Kernel 開發使用，之前是用  BitKeeper
* 分散式、分布式、去中心化，代表不需要中央管理，可以各自修改，最後再視需求合併。 
* Git  主要是由 C 寫成的，速度快
* 利用 SHA-1 hashes 來辨識檔案 

## Ch2

* Debian/Ubuntu: `sudo apt install git`
* MicroSoft Windows 下有兩種  git@Cygwin, [Git for Windows](http://msysgit.github.io/)@msysGit
* 其他工具：  
    * [Github Desktop](https://desktop.github.com/)
    * [TortoiseGit](https://tortoisegit.org/)
    * `gitk`
    * `git-gui`

## Ch3     

**建立程式庫** 
 在想監控的目錄中
 `git init`
即會產生一個隱形的  `.git` 目錄，用來存放修改記錄。

**加入檔案**

```bash
$git add somefile.txt 
$git commit -m "Initial Message" --author="Jon Doe <jdl@example.com>"
$git status
```

提交後，改動會進到本地的儲存庫中。

預先設定好作者資料
```bash
$git config user.name "Joe Due"
$git config user.email "joe@example"
```

如果前面的 `somefile.txt` 改動過後，只要再 `commit` 就好，不必  `add`

`git log`: 檢視目前的修改記錄。

```bash
commit e62f7fd572775ca2479e3ae4ce64bd73ded6a532 (HEAD -> master)
Author: Nero Miller <ming927@spp.url.com.tw>
Date:   Sun Apr 1 05:22:46 2018 +0800

    readingHackingvim Ch7,first draft

```

commit 後的是 SHA-1 hash，用來分辨各版本間的不同

`git show`: 看詳細資料

`git diff a-hash b-hash`

```bash
$git mv somefile.txt somefileB.txt
$git rm somefileB.txt
$git commit -m "mv rm some file"
```
檔案修改都是要提交後，才會生效。

`git clone url_to_the_depo`: copy depo to local


設定

* `--file` (.git/config): 整個程式庫 
* `--global` (~/.gitconfig): 使用者
* `--system` (/etc/gitconfig): 整個系統


別名

`git config --global alias.show-graph 'log --graph --abbrev-commit --pretty=oneline'`

之後打`git show-graph` 就好


## Ch4  基本概念

Git  版本控制的一些概念。 

**程式庫 Repositories**

程式庫：
 
> Depository n. 貯藏所，
> Repository n. 容器；貯藏處，
> 基本上算是同義字。

程式庫 = 檔案 + 修改記錄(及作者、日期) ，以資料夾為操作單位

翻譯術語，參考 [git-it/guide/locale-zhtw.json] []

**GIT物件**

 Blobs

: Binary large object，各版本間的差異以二進位物件儲存，
: 應該是在  `.git/object/` 下的檔案

 Tree

: 各版本的目錄資訊，各  blos  的辨識碼，以 UNIX 來說 blobs 若是檔案，Tree 算是目錄 

 Commits 提交

: 提交物件有每次提交時的所有資訊，作者、時間、歷史資訊


 Tags

: Sha1-hashs 難記，  Tags提供一個別名的方式，
: 像是： 8.0.1616-Alpha  這類方便記憶的名字


**索引 Index**

>　一個動態、暫時的二進位檔，用以描述目前的檔案結構

See Also

[Git 內部原理 - Git 物件](https://git-scm.com/book/zh-tw/v1/Git-%E5%85%A7%E9%83%A8%E5%8E%9F%E7%90%86-Git-%E7%89%A9%E4%BB%B6)


**可尋址內容名稱 Content-Addressable Names**

* 很長的名字，這個是？ GIT 內的物件都有一個 SHA1-HASH 代碼來辨識
* SHA1產生值有 160 位元，通常用 40 位的 16 進位數字表示

** Git 追蹤內容**

* GIT 追蹤的是檔案內容，每當有檔案改動，GIT 會計算新的 SHA1-HASH，將改動存在新的  BLOB 中

Table 4-1. Database comparison


|系統| 索引機制| 資料儲存|
|----|---------| --------|
|傳統資料庫| ISAM| 資料記錄|
|UNIX 檔案系統| 目錄| 資料塊|
|GIT |.git/object/hash 樹狀物件內容 |物件，Blob 樹狀物件 |

**打包檔案**

GIT  只儲存各版本間的差異，所以佔的磁碟空間很少

**物件儲存的示意圖**




語法
--------

樣式可以用 星號\* 或是 底線\_

斜體 emphasis, aka italics, with *asterisks* or _underscores_.
粗體 Strong emphasis, aka bold, with **asterisks** or __underscores__.
合併 Combined emphasis with **asterisks and _underscores_**.
刪除線 Strikethrough uses two tildes. ~~Scratch this.~~


孔子說：

> 說什麼

定義是：

: 是什麼


目錄
--------

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




參考連結
--------

1. [圖解Git](https://marklodato.github.io/visual-git-guide/index-zh-tw.html?no-svg)


[wikipedia:Git]: https://zh.wikipedia.org/wiki/Git
[git-it/guide/locale-zhtw.json]: https://github.com/jlord/git-it/blob/master/guide/locale-zhtw.json

## Site

* [2013 IT 邦幫忙鐵人賽 【30 天精通 Git 版本控管】by Will 保哥](https://github.com/doggy8088/Learn-Git-in-30-days)
* [連猴子都能懂的Git入門指南 by 貝格樂（Backlog）](https://backlog.com/git-tutorial/tw/)
* [為你自己學 Git by 高見龍](https://gitbook.tw/)
* [Pro Git,1st-zh-tw](https://github.com/progit/progit/tree/master/zh-tw)
* [Pro Git,2nd](https://git-scm.com/book/zh-tw/v2)
* [Learning Git Branching](https://learngitbranching.js.org/index.html)


作者：Jon Loeliger 追蹤
譯者：吳曜撰
出版社：歐萊禮 出版社追蹤  功能說明
出版日：2013/1/25
ISBN：9789862766699
金石碼：2014713380050
語言：中文繁體
適讀年齡：全齡適讀

編／譯者：吳曜撰
語言：中文繁體
規格：平裝
分級：普級
開數：18.5x23
頁數：452
出版地：台灣


版本控制使用Git 第二版－目錄導覽說明


第1 章 簡介 
第2章 安裝Git 
第3章 準備開始 
第4章 基本的Git概念 
第5章 檔案管理以及索引 
第6章 送交 
第7章 分枝 
第8章 Diffs 
第9章 合併 
第10章 修改送交 
第11章 遠端程式庫 
第12章 管理程式庫 
第13章 補綴檔案 
第14章 掛鉤 
第15章 結合專案 
第16章 在Subversion程式庫上使用Git


