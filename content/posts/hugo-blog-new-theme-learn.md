+++
title = "Hugo Blog New Theme Learn"
date = 2022-04-06T23:38:03+08:00
description = "Description"
draft = false
toc = true  # by after-dark
categories = ["technology"]
tags = ["hugo", "theme"]
menuTitle = "Theme Learn"
pre = "<i class='fab fa-github'></i> "
post ="<i class='fa fa-file'></i> "
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

因為 docdock 太久沒有更新，更新到新版的 hugo 後， tags 出問題，所以換成 hugo-theme-learn

# Learn

## Basics

#### Req

pass

#### Installation

pass

#### Configuration

設定在 config.toml

https://learn.netlify.app/en/basics/configuration/

#### Style customization

這邊可以修改 learn theme 的一些細部設定，logo, favicon, 配色可改 red, green, blue。

或是修改 blog 根目錄下的  `layouts/partials`

## Content

### Pages organization

`learn` 有兩種頁面形式， Default, Chapter，差別在：
Chapter 是用來引入子頁面的頁面，有點像封面？ 只要在頁面的 yaml 加上 `chapter=true`

#### Front Matter configuration

```
+++
# Table of content (toc) is enabled by default. Set this parameter to true to disable it.
# Note: Toc is always disabled for chapter pages
disableToc = "false"
# If set, this will be used for the page's menu entry (instead of the `title` attribute)
menuTitle = ""
# The title of the page in menu will be prefixed by this HTML content
pre = ""
# The title of the page in menu will be postfixed by this HTML content
post = ""
# Set the page as a chapter, changing the way it's displayed
chapter = false
# Hide a menu entry by setting this to true
hidden = false
# Display name of this page modifier. If set, it will be displayed in the footer.
LastModifierDisplayName = ""
# Email of this page modifier. If set with LastModifierDisplayName, it will be displayed in the footer
LastModifierEmail = ""
+++
```

加入 icon
```
+++
title = "Github repo"
pre = "<i class='fab fa-github'></i> "
+++
```

改變頁面在選單上的順序
```
+++
title = "My page"
weight = 5
+++
```

改選單上的標題
```
+++
title = "Install on Linux"
menuTitle = "Linux"
+++
```

Homepage

1. `content` 下的 `_index.md`
2. `static` 目錄下的  `index.html`

### Archetypes

預設的頁面模板

預設的頁面有兩種：Default, Chapter(封面)

1. `hugo new --kind chapter <name>/_index.md`
2. Default 

```
# Either
hugo new <chapter>/<name>/_index.md
# Or
hugo new <chapter>/<name>.md
```

### Markdown syntax

pass

### Code highlighting

pass

### Menu extra shortcuts

設定選單上的項目

### Icons and logos

設定 Icon, logo

### Multilingual and i18n

多語設定

* Single file my-page.md is split in two files:
    * in English: my-page.en.md
    * in French: my-page.fr.md
* Single file _index.md is split in two files:
    * in English: _index.en.md
    * in French: _index.fr.md

### Tags

pass

## Shortcodes

### Attachments

可以把目錄下的檔案，以連結貼出。

### Button

按鈕

### Children

子頁，目錄結構

### Expand

可以摺疊的內容

### Mermaid

流程圖

### Notice

內建的提示視窗

### Site param

目前有的是 `editURL` ，提供直接編輯的連結。

### Tabbed views

頁籤

----
### expand

可收起隱藏內容

{{%expand "Is this docdock theme rocks ?" %}}Yes !.{{% /expand%}}


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

1. [hugo-theme-learn](https://github.com/matcornic/hugo-theme-learn)
2. [hugo-theme-learn doc](https://learn.netlify.app/en/)


[learnDoc]: https://learn.netlify.app/en/ "learnDoc"
