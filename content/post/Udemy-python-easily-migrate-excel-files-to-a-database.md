+++
title = "Udemy Python Easily Migrate Excel Files to a Database"
date = 2018-05-04T16:55:05+08:00
description = "用 openpyxl 來讀取 Excel 檔案 "
draft = false
toc = true
categories = ["programming"]
tags = ["udemy", "python","excel","openpyxl"]
images = [
  "https://source.unsplash.com/category/technology/1600x900"
] # overrides the site-wide open graph image
+++

[Python: Easily migrate Excel files to a database](https://www.udemy.com/python-easily-migrate-excel-files-to-a-database/learn/v4/overview)

是個 約35 min的免費課程，花點時間來看看。


<!--more-->

Task list: :smile:

- [x] 初稿
- [ ] 再讀
- [ ] 筆記
- [ ] 完成


# 概述


[Python: Easily migrate Excel files to a database][]
使用 [openpyxl][] 來讀寫 Excel2010/xlsx/xlsm 檔到資料庫，這邊是使用 [SQLite][] 當例子

另外在 [Automate the Boring Stuff with Python 的 Ch12] (Chapter 12 – Working with Excel Spreadsheets)
也是使用了 openpyxl 來讀取 Excel 檔。

# Introduction

簡單介紹了 Python 的安裝，和  [PyCharm][] 的使用

# Learning the basics of openpyxl

## 2. Installing openpyxl

因為 [PyCharm][] 各專案有不同的 Virtual Environment ，所以要另外安裝 package.

* 用 File -> Setting -> Project -> Project Interpreter 的頁面 新增 packages
* 或是打開 PyCharm 下的 ALT+F12 打開 Terminal ，用  `pip install openpyxl` 直接裝

## 3. (Optional) Virtualenv 

Virtualenv 可以建立一個獨立的環境，有獨立的 packages ，或是自已版本的 Interpreter，
可以避免干擾，有個乾淨的開發環境。

PyCharm 的每個 Project 都有個別的 Virtualenv.

**See Alos**

- [Virtual Environments (Python documentation)](https://docs.python.org/3/tutorial/venv.html)

## 4. Load an Excel document

使用範例檔： `revenue.xlsx` is Microsoft OOXML file

 `revenue.xlsx` 是個簡單的 Excel 檔，三個欄位(column) ，Product,Price,Quantity sold
 四筆資料(row)。共有兩個(Sheet)頁面，April , May

 ```python
from openpyxl import load_workbook
wb = load_workbook('revenue.xlsx')
wb.active
wb.sheetnames
ws = wb['May']
 ```

## 5. Reading data (single cell/row/column)

```python
>>> ws['B4']
<Cell 'May'.B3>
>>> ws['B4'].value
900
>>> ws.cell(row=3,column=2).value
900
>>> ws['1']   
(<Cell 'May'.A1>,<Cell 'May'.B1>,<Cell 'May'.C1>)
>>> ws['C']
(<Cell 'May'.C1>,<Cell 'May'.C2>,<Cell 'May'.C3>,<Cell 'May'.C4>,<Cell 'May'.C5>)
```



## 6. Iterating through rows

* 選取區塊：`ws['A2:C5']`


## 7. Writing to Excel sheets

* 建立新的頁面(Sheet): `wb.create_sheet('June')`
* 一次寫入一列資料： `wb.append(['Laptop','900','25'])` 
* 寫入新資料後，用 `wb.save('revenue.xlsx')`

## 8. Formula's in openpyxl

Excel 內的方程式。如果沒有特別設定，有些儲存格的內容會是 `=SUM(A1:C4)`
，如果在讀檔時，加上 `data_only=True`  ，就只會讀出最後運算的內容了。
，或者說是在 Cache 內的內容。

```python
from openpyxl import load_workbook

wb = load_workbook('excel_files\excel_fomulas.xlsx',data_only= True)

ws = wb.active

print(ws['C2'].value)
```
### Quiz 1: 

讀取各儲存格，
* 直接指定座標： `ws['B3']`
* 或是用cell，這邊的參數要用數字。`ws.cell(row=3,column=2).value`


# Migrating multiple excel sheets to a database

將資料從 Excel 轉移到 SQlite

Quiz 1: Basics of openpyxl

## 9. Reading from multiple excel documents

把所有檔案的資料印出來。

 revenue_2016.xlsx
 revenue_2017.xlsx

```python
#test_multiple_files.py
import os
from openpyxl import load_workbook

def parse_products():
    big_list_of_all_rows = []

    for file in os.listdir("excel_files"):
        wb = load_workbook(os.path.join('excel_files',file))

        for sheetname in wb.sheetnames:
            #print("Current sheet is:",sheetname)
            ws = wb[sheetname]

            for row in ws.iter_rows(min_row=2):
                single_row_values=[]

                for cell in row:
                    single_row_values.append(cell.value)

                big_list_of_all_rows.append(single_row_values)

    return big_list_of_all_rows
```

## 10. Peewee and DBeaver

介紹 ORM 程式庫 [peewee][] , 和讀取程式庫的程式  [DBeaver][]
測試產生SQlite的檔案 `revenue.db`


## 11. Store excel data in a database (sqlite)

將之前打開多檔的程式改寫一下，寫入 `revenue.db`

```python
#database.py
from peewee import SqliteDatabase,Model,CharField,FloatField,IntegerField
from test_multiple_files import parse_products

db = SqliteDatabase('revenue.db')

class Product(Model):
    name = CharField()
    price = FloatField()
    quantity_sold = IntegerField()

    class Meta:
        database = db

db.connect()

product_rows = parse_products()

for product_row in product_rows:
    product  = Product(name=product_row[0],price=product_row[1],quantity_sold=product_row[2])
    product.save()

db.close()
```

# 心得

用程式幫你讀 Excel 檔，寫入資料庫，能省下很多時間。


# 參考連結

1. [Object-relational mappers (ORMs)](https://www.fullstackpython.com/object-relational-mappers-orms.html)

[Python: Easily migrate Excel files to a database]: https://www.udemy.com/python-easily-migrate-excel-files-to-a-database/learn/v4/overview
[openpyxl]: https://openpyxl.readthedocs.io/en/stable/ "A Python library to read/write Excel 2010 xlsx/xlsm files"
[SQLite]: https://www.sqlite.org/ "SQLite is a self-contained, high-reliability, embedded, full-featured, public-domain, SQL database engine"
[PyCharm]: https://www.jetbrains.com/pycharm/ "PyCharm: Python IDE for Professional Developers by JetBrains"
[peewee]: http://docs.peewee-orm.com/en/latest/ "a simple and small ORM"
[DBeaver]: https://dbeaver.jkiss.org/download/ "Free Universal SQL Client"

