+++
title = "Reading Python Scraping Analysis Book"
date = 2019-05-19T20:23:00+08:00
description = " Python：網路爬蟲與資料分析入門實戰 "
draft = false
toc = true  # by after-dark
categories = ["technology"]
tags = ["reading", "python", "scraping","spider"]
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

scrayping 工具

* http: requests
* html parser: bs4 , lxml
* regexp
* 使用 API
* data store: image,csv,SQLite
* utf-8，XML
* 進階議題：使用者登入、cookie, webdriver,Header, robot.txt, proxy, 隱藏欄位
* scrapy



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

BeautifulSoup 文件中相關的部分

* [向上](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#going-up) : `.parent`, `.parents`
* [向下](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#going-back-and-forth) : `.next_sibling` ,  `.previous_sibling`
* [左右](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#going-sideways) : `.next_element` and `.previous_element`


## 2-4 正規表示式 (Regular Expression)

"""python
import  re

for title in soup.find_all(re.compile('h[1-6]')):
    print(title.text.strip())

"""

# Chapter 03 網頁爬蟲範例實戰

3-1 PTT 八卦板今日熱門文章
3-2 Yahoo 奇摩電影本週新片
3-3 兩大報當日焦點新聞
3-4 Google 搜尋股價資訊
3-5 Dcard 今日熱門文章

從實例中學習抓取資料、分析。


# Chapter 04 使用 API

## 4-1 API 簡介

API(Application Programming Interface)：在網站來說，就是取用站方整理好的資料的介面。

HTTP request 的方法 :

1. `GET` : 參數寫在網址
2. `POST` : 表單資料打包後，送出
3. `PUT` : 背景送出資料
4. `DELETE` : 背景刪除資料

API 送回的資料，通常會以幾種形式送回 :

1. JSON : key, value 成對的資料
2. XML : tag 標記的資料




4-2 PTT 八卦板眾來源分佈 (ipstack.com)
4-3 IMDB API
4-4 Google Maps APIs (Google Geocoding/Places API)
4-5 Dcard API

# Chapter0 5 資料儲存

5-1 儲存圖片與多媒體檔案

file system

5-2 儲存資料到 CSV 檔

save to  CSV

5-3 儲存資料到資料庫 SQLite

Save SQlite

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

# 附錄 

附表 本書範例目標網站列表

附錄A 在 Mac 安裝Anaconda 開發環境

附錄B Python 爬蟲框架Scrapy 入門教學
B-1 Scrapy 環境安裝
B-2 簡易部落格爬蟲
B-3 Scrapy 系統架構
B-4 博客來網路書店爬蟲




# 參考連結

1. [本書網站](https://jwlin.github.com/py-scraping-analysis-book/ch2/blog/blog.html)
2. [本書Github](https://github.com/jwlin/py-scraping-analysis-book)
3. [BeautifulSoup 文件] [BeautifulSoup]
4. [R 語言使用者的 Python 學習筆記系列 第 16 篇:[第 16 天] 網頁解析](https://ithelp.ithome.com.tw/articles/10186119)
5. [Nightwatch101 #5：使用 CSS Selector 定位網頁元素](https://cythilya.github.io/2017/12/15/nightwatch-css-selector/)
6. [Nightwatch101 #6：使用 Xpath 定位網頁元素](https://cythilya.github.io/2017/12/16/nightwatch-xpath/) 
7. [CSS selector vs XPath][CSSvsXPath] 
8. [BeautifulSoup.css-selectors](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors)


[google]: https://www.google.com "Search Engine"
[BeautifulSoup]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/ "解析 HTML/XML"
[CSSvsXPath]: http://elementalselenium.com/tips/34-xpath-vs-css-revisited-2 "Css Vs. X Path, Under a Microscope"
