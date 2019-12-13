+++
title = "Python Html Parsing"
date = 2019-12-13T20:13:58+08:00
description = "Python parsing libs"
draft = false
toc = true  # by after-dark
categories = ["Technology"]
tags = ["python", "bs4","lxml"]
pre ="<i class='fa fa-file'></i> "
type="page" # set "slide" to display it fullscreen with reveal.js
images = [
  "https://source.unsplash.com/category/technology/"
] # overrides the site-wide open graph image
+++

Python Parsing libs.  bs4, lxml, pyquery, html.parser


<!--more-->

Task list: :smile:

- [x] 初稿
- [ ] 再讀
- [ ] 筆記
- [ ] 完成


# 概述

Python 中用來解析(Parsing) html, xml , XHTML 的工具
其他：XPATH

常見的有：
1. bs4 (BeautifulSoup)
1. lxml
1. pyquery
1. python 中內建的 html.parser

# BeautifulSoup

* [bs4 文件][bs4.doc]
* [bs4 中文文件][bs4.doc.zh_cn]

## Installing Beautiful Soup

```
$ pip install beautifulsoup4

```
## Installing a parser

* html.parser
    * 內建，速度中，容錯強，中文容錯力差  
* html5lib
    * 速度慢，容錯最好，生成 html5 文件, 以 browser 方式解析文件
* lxml
    * 速度快，容錯強，需要 c  library 
* lxml-xml (xml)
    * 速度快，唯一支持 xml，需要 c library

parser 用法：`(BeautifulSoup(markup, "htmlparser"))`    


## Kinds of objects

bs4 中有4 種物件：


* `Tag` : 標籤
    * tag.name  - str
    * tag.attrs - dict
    * tag.get - 
* `NavigablesString` : `Tag` 內的 文字?
* `BeautifulSoup` : 解析過的文件
* `Comment` : XHTML 中的註解 `<!--`我是註解 `-->`



{{% alert theme="warning" %}} bs4 中 class 用 class_ ，避免跟原有的關鍵字衝突 {{% /alert %}}

找資料的方法

1. Nagigation the tree: 用 CSS selector
2. Searching the tree: `find`, `find_all`

## Searching the Tree

## Searching by CSS class





# 參考連結

1. []()
1. []()
1. [用Python爬取 Youtube 資訊 - 圖文課程](https://hiskio.com/courses/112)
1. []()

# Library

1. [bs4.doc](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
1. [lxml](https://github.com/lxml/lxml)
1. [pyquery](https://github.com/gawel/pyquery)
1. [html.parser.doc](https://docs.python.org/3/library/html.parser.html) 
1. [jusText](https://github.com/miso-belica/jusText)

[bs4.doc]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
[bs4.doc.zh_cn]: https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/ "bs4 中文文件"
[lxml]: https://github.com/lxml/lxml
[pyquery]: https://github.com/gawel/pyquery
[html.parser.doc]: https://docs.python.org/3/library/html.parser.html
[jusText]: https://github.com/miso-belica/jusText

[google]: https://www.google.com "Search Engine"
