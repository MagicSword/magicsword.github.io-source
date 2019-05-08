+++
title = "Python How to Work With PDF in Python"
date = 2019-05-08T00:01:48+08:00
description = "Reading article, python deals with PDF"
draft = false
toc = true  # by after-dark
categories = ["technology"]
tags = ["python", "pdf"]
pre ="<i class='fa fa-file'></i> "
type="page" # set "slide" to display it fullscreen with reveal.js
images = [
  "https://source.unsplash.com/category/technology/"
] # overrides the site-wide open graph image
+++

閱讀利用 [Python][] 來處理 [PDF][] 的文章，並作簡單的筆記。


<!--more-->

Task list: :smile:

- [x] 初稿
- [ ] 再讀
- [ ] 筆記
- [ ] 完成



# 概述

 
原文 [How to Work With a PDF in Python](https://realpython.com/pdf-python/)

文章大概分為幾個部分

* 簡介 python 內用來處理 PDF 的程式庫，及演進
    *  pyPDF,pyPDF2,pyPDF4
    *  pdfrw
* 安裝
* 提取
* 合併
* 分拆
* 加浮水印
* 加密
* 結論
* 進階閱讀

這篇文章大概就原文內容作摘要，加上一些心得筆記。或許之後有空來考慮翻譯？


# 前言

[PDF][] 可攜式文件格式, 是 Adobe 公司的文件規格，常見的文件交換格式。目前是
ISO 下的開放文件格式。

python 下用來處理 PDF 的程式庫除了 pyPDFx 外，還有：

* pdfminer
* pdfquery
* PDFlib's TET library with python binding
* Reportlab
* pdfrw

本文主要是以 pyPDFx 為主。

# pyPDF 演進

* 最初的 pyPDF 是在2005
* [pyPDF2][] 最近失去維護，而 [pyPDF4][] 跟 [pyPDF2][] 不完全相容
* 本文主要以 [pyPDF2][] 為主
* [pdfrw][] : 和 ReportLab 整合，有不少功能

# 安裝

```sh
    $ pip install pypdf2
    # 或是用 Anaconda
    $ conda install pypdf2
```


# 提取

* 可以用 pyPDF2 萃取出 metadata, 包括 Author,Creator,Producer,Subject
,Title,Number of Pages。
* `PyPDF2.PdfFileReader.getDocumentInfo()` 來讀 pdf metadata
* `PyPDF2.PdfFileReader.getNumPages()` 來讀頁數
* 例子中  [f-string][]   ，可以參考文章
* PyPDF2 中還有 `.extractText()` 用來讀內文，不過效果不好
* 要讀內文的話，建議用 [PDFMiner][]


```python
# extract_doc_info.py

from PyPDF2 import PdfFileReader

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)
    return information

if __name__ == '__main__':
    path = 'reportlab-sample.pdf'
    extract_information(path)

```    



# 旋轉


`PdfFileWriter.rotateClockwise(90)` 寫入時，可以旋轉頁面。
`.getPage() addPage()` 

Note
{{% notice note %}}
PyPDF2 只能以90度的倍數旋轉，其他的角度會得到 `AssertionError` 
{{% /notice %}}


# 合併

將兩個 pdf 文件合成一個檔案，像是把本文、加上封面、和封底。

方式：讀進兩個文件的每一頁，一頁一頁寫進新的 pdf ，產生合併的新文檔。



# 分拆

讀進各頁，把想分出去的頁數寫到新檔

# 加浮水印

`PdfFileReader.mergePage(浮水印pdf檔)` 加上浮水印

# 加密

* PyPDF2 目前只能加密碼鎖上文件。
* admin 有 read/write 的權限。user 只有 read 的權限
* 加密長度預設是 40bit


`PdfFileWriter.encrypt(user_pwd=password, owner_pwd=None, 
                       use_128bit=True)`
# 結論

PyPDF2 功能不少，不過 取出文字的功能好像不太完美，
或許要看看其他程式庫。像是 [PDFMiner][]

# 進階閱讀

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

1. [How to Work With a PDF in Python](https://realpython.com/pdf-python/)
2. [f-string](https://realpython.com/python-f-strings/) 
3. [Archetypes](https://gohugo.io/content-management/archetypes/)
4. [Customizing](https://comfusion.github.io/after-dark/#customizing)
5. [Emoji連結](https://www.webpagefx.com/tools/emoji-cheat-sheet/)


[google]: "https://www.google.com" "Search Engine"
[Python]: "https://zh.wikipedia.org/wiki/Python" "Programming Language"
[PDF]: "https://zh.wikipedia.org/wiki/pdf" "Portable Document Format"
[pyPDF2]: "https://github.com/mstamy2/PyPDF2" "A utility to read and write PDFs with Python"
[pyPDF4]: "https://github.com/claird/PyPDF4" "A utility to read and write PDFs with Python"
[pdfrw]: "https://github.com/pmaupin/pdfrw" "pdfrw is a pure Python library that reads and writes PDFs"
[PDFMiner]: "https://github.com/euske/pdfminer" "PDFMiner"
[f-string]: "https://realpython.com/python-f-strings/" "f-string" 

