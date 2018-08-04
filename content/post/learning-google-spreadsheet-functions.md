+++
title = "Learning Google Spreadsheet Functions"
date = 2018-06-03T23:30:28+08:00
description = "Using Google SpreadSheet Functions"
draft = true
toc = true  # by after-dark
categories = ["technology"]
tags = ["google", "spreadsheet","office"]
pre ="<i class='fa fa-file'></i> "
type="page" # set "slide" to display it fullscreen with reveal.js
images = [
  "https://source.unsplash.com/category/technology/"
] # overrides the site-wide open graph image
+++

使用 [IMPORTXML][] 讀 HTML 的資料進 Google 試算表。

以下節錄 Google 試算表使用說明，或許改天再加一些使用記錄。

<!--more-->

Task list: :smile:

- [x] 初稿
- [ ] 再讀
- [ ] 筆記
- [ ] 完成


# 使用函數

在儲存格中輸入等號 (=) 及您要使用的函式

{{% alert theme="info" %}}注意：系統可能會根據您的資料提供建議的公式和範圍。{{% /alert %}}

## [IMPORTXML][]

用法範例

```
IMPORTXML("https://en.wikipedia.org/wiki/Moon_landing", "//a/@href")

IMPORTXML(A2,B2)
```

語法
```
IMPORTXML(網址, XPath_查詢)
```

網址 - 要檢查的網頁所在網址，包括通訊協定名稱 (例如 http://)。

:網址的值必須放置在引號內，或者是一個含有適當文字的儲存格參照。
:XPath 查詢 - 要對結構化資料執行的 XPath 查詢。

如要進一步瞭解 XPath，請造訪 http://www.w3schools.com/xml/xpath_intro.asp。

### XPath

XPath 可以 用 Chrome -> 檢視網頁原始碼 -> Copy -> Copy XPath

例子，要讀 Web Ptt 版的文章標題 ，

原始的 XPath `//*[@id="main-container"]/div[2]/div[1]/div[3]/a`

要改成 `//*/div[2]/div/div/a` , 把 方括號去掉才能作用。


```
=importXML("https://www.ptt.cc/bbs/Baseball/index.html","//*/div[2]/div/div/a")
```

## [REGEXEXTRACT][]

根據規則運算式擷取符合規則的子字串。

用法示範

```
REGEXEXTRACT("Needle in a haystack", ".e{2}dle")
```

語法

```
REGEXEXTRACT(text, regular_expression)
```

* text - 輸入文字。
* regular_expression - 此函式將傳回 text 中符合此運算式的第一個字串。

**附註**

Google 產品使用 RE2 來處理[規則運算式](https://support.google.com/docs/answer/62754#regular_expression)。Google 試算表支援 RE2，但不支援符合規則的 Unicode 字元類別。進一步瞭解[如何使用 RE2 運算式](https://github.com/google/re2/blob/master/doc/syntax.txt)
此函式僅接受輸入文字 (而非數字)，並傳回文字做為輸出結果。如果您希望系統傳回數字，請在使用此函式時一併使用 VALUE 函式。如果要以數字做為輸入值，請先使用 TEXT 函式將其轉換為文字。

使用例子：


```
=regexextract(A1,"\[[^\]]+\]")
```

# 後記

Google Spreadsheet 只能對 "靜態" 網頁，其他的網頁可能還是需要爬蟲程式

# 參考連結

1. [正規表示式 Regular Expression](http://ccckmit.wikidot.com/regularexpression)
1. [無痛爬梳自己來，用 Google Spreadsheet 爬取網頁資料](http://blog.infographics.tw/2016/11/google-spreadsheet-data-scraping/)
1. [Google 試算表函式清單](https://support.google.com/docs/table/25273?hl=zh-Hant&ref_topic=1361471)
1. [選擇表單回應資料的儲存位置](https://support.google.com/docs/answer/2917686?hl=zh-Hant)


[google]: "https://www.google.com" "Search Engine"
[IMPORTXML]: "https://support.google.com/docs/answer/3093342" "匯入多種結構化資料類型的資料，包括 XML、HTML、CSV、TSV 和 RSS 以及 ATOM XML 資訊提供。"
[REGEXEXTRACT]: https://support.google.com/docs/answer/3098244 "根據規則運算式擷取符合規則的子字串。"
