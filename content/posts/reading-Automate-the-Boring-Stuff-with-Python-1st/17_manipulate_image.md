+++
title = "CHAPTER 17 處理影像圖片"
date = 2018-08-11T18:41:28+08:00
description = "CHAPTER 17 處理影像圖片"
draft = true
toc = true  # by after-dark
categories = ["technology"]
tags = ["hello", "world"]
pre ="<i class='fa fa-file'></i> "
type="page" # set "slide" to display it fullscreen with reveal.js
images = [
  "https://source.unsplash.com/category/technology/"
] # overrides the site-wide open graph image
+++

Before you continue, please take a moment to configure your archetypes.


<!--more-->

Task list: :smile:

- [x] 初稿
- [ ] 再讀
- [ ] 筆記
- [ ] 完成


# 概述


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


　
### excerpt-include

從檔案引用內容 

### expand

可收起隱藏內容

{{%expand "Is this docdock theme rocks ?" %}}Yes !.{{% /expand%}}

### icon


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

1. [Eng-doc](http://daringfireball.net/projects/markdown/syntax)
2. [markdown.tw](https://github.com/othree/markdown-syntax-zhtw/blob/master/syntax.md)
3. [Archetypes](https://gohugo.io/content-management/archetypes/)
4. [Customizing](https://comfusion.github.io/after-dark/#customizing)
5. [Emoji連結](https://www.webpagefx.com/tools/emoji-cheat-sheet/)


[google]: "https://www.google.com" "Search Engine"
