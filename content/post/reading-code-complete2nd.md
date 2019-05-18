+++
title = "Reading Code Complete 2nd"
date = 2019-05-18T19:35:09+08:00
description = "Code Complete 2nd reading"
draft = false
toc = true  # by after-dark
categories = ["programming"]
tags = ["reading", "programming"]
pre ="<i class='fa fa-file'></i> "
type="page" # set "slide" to display it fullscreen with reveal.js
images = [
  "https://source.unsplash.com/category/technology/"
] # overrides the site-wide open graph image
+++

 Code Complete 2nd 主要是講軟體工程方面的內容。通常簡寫為 `cc2e`



<!--more-->


 * 書名：CODE COMPLETE 2中文版：軟體開發實務指南（第二版）
 * 原名：Code Complete: A Practical Handbook of Software Construction, Second Edition
 * [博客來] (https://www.books.com.tw/products/0010805887)
 * [Amazon] (https://www.amazon.com/Code-Complete-Practical-Handbook-Construction/dp/0735619670)
 * 作者： Steve McConnell  
 * 譯者： 金戈, 湯凌, 陳碩, 張菲
 * 出版社：博碩  
 * 出版日期：2018/11/23
 * 語言：繁體中文
 * 定價：1280元
 * ISBN：9789864341313
 * 規格：平裝 / 912頁 / 18.5 x 23 cm / 普通級 / 單色印刷 / 二版
 * 出版地：英國
 * 本書分類：電腦資訊> 程式設計/APP開發> 軟體工程/遊戲開發


Task list: :smile:

- [x] 初稿
- [ ] 再讀
- [ ] 筆記
- [ ] 完成



# 簡介


本書分為幾個部分：

1. 第一部分 打好基礎
2. 第二部分 建立高品質的程式碼
3. 第三部分 變數
4. 第四部分 語句
5. 第五部分 程式碼改善
6. 第六部分 系統考慮
7. 第七部分 軟體工藝

* 主要是在軟體工程的內容，如何寫出好的程式碼。
* 而什麼是好的程式碼？易於維護、讓人容易理解的就是好的程式碼。
* 書中的例子，主要是用C++, Java 跟 VB.NET寫的。
* 多達約900頁的內容，可以先從有興趣的地方開始看。
* 本書還有準備了 Checklist 核對表，方便你在適用的場合，用來評估
自已專案的表現。
* 本書寫在時間是 2004 年，不過概念的東西不會差太多。


# 第一部分 打好基礎

1~4 章

寫程式、蓋房子，本質上都是在建造一個東西。建築學中的概念也常常使用在軟體工程學中。
工程開始前，需要有的一些步驟：討論需求、建築藍圖、架構確認、資源管理、本地化、國際化， 
使用者界面、效能、輸入輸出、容錯性。在真正動手前，考慮周到，之後才不會多走了錯路。
算是在 孫子兵法 中廟算的階段。


# 第二部分 建立高品質的程式碼

**5 Design in Construction**

軟體設計，在動手寫程式碼前，規劃軟體的架構，像是設計模式、使用者介面、資料庫存取、
耦合標準、高內聚力

**6 Working Classes**

Class 類別，很多物件導向的程式中常用到的。
抽象資料類別 ADTs，類別介面、為何要用 Class?，超越類別 Packages

**7 High-Quality Routines**

Routines(子程式)：為了完成特別的功能而寫的方法， 可被呼叫。
程式中，一定有些動作會重複的做，把它分出來，需要時再呼叫，程式可以變的比較易讀，且有效率。 
好的子程式名稱：描述子程式的功能，簡潔，對傳回值有所描述，動詞+受詞？命名要有一致性。 
子程式要多長？200行以下會比較好。 
如何使用子程式參數(傳入值)？

**8 Defensive Programming**

撰寫程式時，錯誤難免，但事前的一些規範，能有效的防止產出錯誤。
輸入資料檢查、斷言、錯誤處理、例外、隔離程式、輸助除錯的程式碼…

**9 The Pseudocode Programming Process**

* Pseudocode(虛擬碼)，可以想作是思考的步驟。
* Pseudocode Programming Process(PPP)有助於減少設計、編寫文件所需的工作。
* 如何寫好虛擬碼？
* PPP的替代方案？重構，契約式設計，測式導行設計(TDD) 


#第三部分 變數

**10 General Issues in Using Variables**

變數型態、作用範圍、持續時間…

**11 The Power of Variable Names**

* 好的變數命名，可以增加易讀性。變數的資料型態、功能、作用範圍、前綴
* 命名要有一致性，避免和保留字太相近

**12 Fundamental Data Types**

數值、整數、浮點數、字元字串、布林、列舉、具名常數、陣列

**13 Unusual Data Types**

* 結構體：`struct`in C++, `Structure` in Visual Basic ，
  基本上是多種資料型態結合的自訂資料型態。
* 指標：直接操作記憶體的工具，Java, C#, 和 Visual Basic 都沒有提供指標。
  指標強大，但也容易造成錯誤。
* 全域資料：程式中任何人都可以取用這個資料，所以容易被不對的子程式、不對的時間被
  取用，錯誤就會常發生，不好管理。 

#第四部分 語句

**14 Organizing Straight-Line Code**

[Straight-Line Code(直線碼)] (http://terms.naer.edu.tw/detail/1287109/) :
指程式中不含任何循環或迴圈者。若需要重複某程式段，則依順序直接寫出其程式碼，而不用循環指令。

**15 Using Conditionals**

`if-else`, `switch-case`,...

**16 Controlling Loops**

`for loop`, `while`,...

**17 Unusual Control Structures**

recursive structure, `goto` clause, ...

**18 Table-Driven Methods**

用查表，來代替 `if-else`之類的設計模式。簡單的情境，或許 邏輯子句較方便。但是情境越複雜，查表法的好處也越大。

**19 General Control Issues**

布林運算、巢狀結構、結構化設計…

#第五部分 程式碼改善

程式寫作中、寫完後除錯，debug的過程

**20 The Software-Quality Landscape**

產品有要正確性(運作結果正常)，可用性(易學易用)，效率(運行速度可用)，…
測試方法，Alpha, Beta 測試，… 


**21 Collaborative Construction**

 * 通常是團隊來完成一個產品， 所以人員協同合作分配，

**Pair-Programming**(結對程式設計)：

: 兩個程式設計師在一個電腦上共同工作。一個人輸入程式碼，而另一個人審查他輸入的每一行程式碼。
: 輸入程式碼的人稱作駕駛員，審查程式碼的人稱作觀察員（或導航員）。兩個程式設計師經常互換角色。

**22 Developer Testing**

Unit-Test, Component Test, Intergration Test,Regression Test, System Test,...

**23 Debugging**

除錯方式、方法，…

**24 Refactoring**

重構(Refactoring):

: 指對軟體程式碼做任何更動以增加可讀性或者簡化結構而不影響輸出結果。


程式不可能一寫出來就是最完美的，常要經過多次修改，追加功能，減少功能， 除錯… 

**25 Code-Tuning Strategies**

Code-Tuning 程式碼調整，和重構不同的是，通常為了增加程式的效率而作。
改寫程式邏輯、用新的運算法，…。為了快，而重寫。  

**26 Code-Tuning Techniques**

本章著重在程式碼範圍的調整，較細節的部分。

#第六部分 系統考慮

**27 How Program Size Affects Construction**

專案管理，團隊協調

**28 Managing Construction**

* 需求變更，設計變更
* 程式碼變更：版本控制，備份
* 進度評估：甘特圖…
* 專業的專案管理人才

**29 Integration**

整合，不同專案間的整合，不同團隊間的整合，不同公司間的整合，

**30 Programming Tools**

* 設計工具：UML
* 原始碼工具：IDE, Editor,Compare tool, Merge tool, Code Formatter, Document, Refactor
* 可執行碼工具：Compiler, Builder, Libraries,Debug, Testing
* 工具導向的環境：OS
* 自行設計的工具：DRY, 自已寫工具
* 工具夢想世界：

#第七部分 軟體工藝

**31 Layout and Style**

Coding Style: 程式寫出來，要讓人看的懂。斷行、段落，註解…


**32 Self-Documenting Code **

* 內部文件：通常是寫在程式碼內的註解。外部文件：另外寫的軟體操作說明書。
* 註解或不註解：註解是為了方便人了解程式，但是如果程式碼本身易於了解，註解或許就不是必要，反而增加閱讀量。
* 參考其他人的註解標準

**33 Personal Character **

性格影響結果

**34 Themes in Software Craftsmanship**

以人為本

**35 Where to Find More Information**

* 其他書、期刊、參考書目
 
# 筆記

900多頁這樣大略翻了一下，說的東西還真的是很多。軟體工程真的是教你如何寫程式走向架構軟體、
建造一個新的東西的學問。細讀可能還要很多時間，有空再來慢慢讀。

# 參考連結

1. [SteveMcConnell作者網站](https://stevemcconnell.com/books/)
2. [【Code Complete 2nd Edition：軟體開發實務指南】怎麼讀這本 1.7 kg 重的經典磚塊書](https://dotblogs.com.tw/hatelove/2018/12/23/code-complete-2nd-edition-reading-guide)

[google]: "https://www.google.com" "Search Engine"
