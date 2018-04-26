+++
title = "Reading Version Control With Git 2nd"
date = 2018-04-01T23:06:34+08:00
description = "Version Control with Git,2nd  簡單心得"
draft = false
toc = true
categories = ["Technology"]
tags = ["reading", "git"]
images = [
  "https://source.unsplash.com/category/technology/1600x900"
] # overrides the site-wide open graph image
+++

Version Control with Git, 2nd Edition 簡單的一些筆記。 

<!--more-->

Task list: :smile:

- [x] 初稿
- [ ] 再讀
- [ ] 筆記
- [ ] 完成



![Version Control with Git, 2nd Edition](https://covers.oreillystatic.com/images/0636920022862/cat.gif)

[Version Control with Git, 2nd Edition](http://shop.oreilly.com/product/0636920022862.do)
<BR> Powerful tools and techniques for collaborative software development

- By Jon Loeliger, Matthew McCullough
- Publisher: O'Reilly Media
- Release Date: August 2012
- Pages: 456

[版本控制使用Git 第二版](https://www.kingstone.com.tw/book/book_page.asp?ActID=alsobuy&LID=se_base001&KMCode=2014713380050#detaildata)

- 作者：Jon Loeliger 
- 譯者：吳曜撰
- 出版社：歐萊禮 
- 出版日：2013/1/25
- ISBN：9789862766699
- 語言：中文繁體
- 規格：平裝
- 開數：18.5x23
- 頁數：452
- 出版地：台灣





[Exercise Codes](https://github.com/terryjbates/version-control-with-git)


# 概述

: 這本書可以幫助您快速搞懂如何使用Git來追蹤、分支、合併並且管理程式碼修訂版本。
: 藉由詳盡的步驟說明，本書將帶領您了解Git的基礎與進階技術，
: 充分發揮這套版本控制系統的強大功能。 


# Ch1 簡介

* Git by Linus Torvalds at 2005，主要是用於 Linux Kernel 開發使用，之前是用  BitKeeper
* 分散式、分布式、去中心化，代表不需要中央管理，可以各自修改，最後再視需求合併。 
* Git  主要是由 C 寫成的，速度快
* 利用 SHA-1 hashes 來辨識檔案 

# Ch2 安裝 Git

* Debian/Ubuntu: `sudo apt install git`
* MicroSoft Windows 下有兩種  git@Cygwin, [Git for Windows](http://msysgit.github.io/)@msysGit
* 其他工具：  
    * [Github Desktop](https://desktop.github.com/)
    * [TortoiseGit](https://tortoisegit.org/)
    * `gitk`
    * `git-gui`

# Ch3 準備開始    

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

**See Also**

* [git log – the Good Parts](https://zwischenzugs.com/2018/03/26/git-log-the-good-parts/)


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


# Ch4  基本概念

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

: SHA1-hashs 難記，  Tags提供一個別名的方式，
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


**`.git/`目錄內部**

```bash
$git init
```
建立一個檔案庫後，會有一個 `.git` 目錄，
內部儲存變動記錄，和一些資訊。

**物件，雜湊、及Blobs**

* `index` 是目前檔案庫的樹狀結構
* `git ls-files -s` 顯示目前的 index、和 working tree， `-s` 會顯示 SHA1-hash
* `git write-tree` 將目前的index寫入樹狀結構中

**Git與SHA1-hash**

* 同樣的檔案庫狀態、經計算後，會得到同樣的SHA1-hash；
* 換而言之，同樣的SHA1-hash，代表目前檔案庫的狀態是一樣的。
語法

**樹狀結構**

**提交**

每次的提交會儲存這些訊息：

* 樹狀物件名稱、檔案關聯性
* 作者姓名、修改時間
* 提交者姓名、提交時間
* 提交訊息
* 預設，作者=提交者

**標籤**

標籤(TAG)，基本上就是別名(Alias)的功能
分兩種： 
1. 輕量 lightweight tag: 不會建立永久物件
2. 標示 annotated tag: 會建立你提交的物件

# Ch5 檔案管理及索引

基本上，本章討論檔案管理的一些方法，`create`, `remove`,`move`,`rename`

**索引**

被`git add`指令加入的指令，才會被加入 index中

**Git中的檔案分類**

被追蹤

: 已被 add 的檔案

被忽略

: `.gitignore` 內的檔案，暫存檔、草稿檔、個人註記、程式自動產生的檔案。


不被追蹤

: 不屬於前兩類的檔案

**使用git commit**

`git commit --all(-a)` : 加入所有未被追蹤檔案 

**使用git rm**

* 使用這個指令，只是把檔案解除追蹤，或是說移出 index，
* 不會刪除檔案，想刪檔案還是要用 `rm`
* 但檔案還會存在歷史記錄中，要把檔案從歷史記錄中完全刪除的話，要用
  `git rm --cached xxx`，但要小心使用
* 要回復被刪除的檔案的話，要用 `git checkout HEAD -- xxx-file`


**使用git mv**

移動、重新命名檔案。

`git log --follow xxx-file` :列出該內容的所有歷史記錄。

**追蹤重新命名檔案的兩三事**

* subversion 追蹤檔案的方式較沒效率
* git不會重新追蹤命名，而是只改變樹狀結構。

**.gitignore檔案**

在這個檔案記錄要忽略的檔案：

* `#` 開頭的行是註解，文字後有 `#` 則不會被視為註解
* 空白行會被忽略
* 單純的檔名。git 會去找同檔名的檔案
* 目錄名，以 `/` 結尾，會去找同名的目錄，會忽略同名的檔案。
* 萬用字元 * ， 同unix 使用方式
* 驚謹號 ! , not，會這行寫的規則反過來執行

Git允許你在檔案庫的任何目錄放 `.gitignore` ，各目錄下都可以有
自已的 `.gitignore`

為了解決多個 `.gitignore` 檔案，Git 有忽略的優先順序的規則。
以下優先權由高到低排為：

1. 命令列指令加入的規則
2. 同目錄中的 `.gitignore`
3. 父目錄的 `.gitignore`, 離越遠的目錄，其 `.gitignore` 的優先權越低
4. `.git/info/exclude` 檔案中的規則
5. 寫在 `core.excludefile` 中的規則

`.gitignore` 這個檔案也會被追蹤，如果不想讓 `.gitignore` 被追蹤，
可以把規則放在 `.git/info/exclude` 中，就不會被複製了。

**git的物件模型及檔案**

pass

# Ch6 提交

提交：檔案庫間的變動。 

提交會將目前的狀態，送到檔案庫，Git只會儲存變動的部分，
並產生新的 SHA1-hash。Git 很適合經常性的提交。

**單元改變集合**

`Commit` 有點像拍照，儲存了那個瞬間檔案庫的樣子。

**辨識提交**

`HEAD` : 最新提交版本的別名。

Git 中有許多寫提交名稱的方式，可以來存取、比較變動。

**絕對提交名稱**

絕對提交名稱 SHA1-hash

* 160 bit，40 位的十六進位字元是唯一、獨特的名稱，
* 若兩個提交的辨識碼一樣，可知兩個提交的狀態應該是一樣的。
* 你也可以獨特的前幾碼代替  40 位的長碼。

**ref 與 symref**

`ref` : 用另一個好記的名字，來代替較長的 SHA1-hash , 像是 HEAD,tags
`symref`(symbolic reference): 用來代表 `ref` 的別名

基本上 `ref` 就是存在下面目錄的檔案：

```bash
    .git/ref
    .git/refs/ref
    .git/refs/tags/ref      # 標籤
    .git/refs/heads/ref     # 本地
    .git/refs/remotes/ref   # 遠端
    .git/refs/remotes/ref/HEAD
```

Git 內部已有的 `ref`

HEAD
: 指向目前最新的分支
 
ORIG\_HEAD
: 某些動作中，會先把目前的 `HEAD` 先記錄在這，以備使用
 
FETCH\_HEAD
: 使用 `git fetch` 時，會把動作時，遠端的分支，存在這
 
MERGE\_HEAD
: 執行合併時，會將被合併的分支，記錄在這
 

這些都可以用 `git symbolic-ref`  來管理。



**See Also**:

* [Git 內部原理 - Git References](https://git-scm.com/book/zh-tw/v1/Git-%E5%85%A7%E9%83%A8%E5%8E%9F%E7%90%86-Git-References)
* [第 11 天：認識 Git 物件的一般參照與符號參照](https://github.com/doggy8088/Learn-Git-in-30-days/blob/master/zh-tw/11.md)


**相對提交名稱**
 
* 就像 unix 中的目錄操作有絕對路徑、相對路徑，git 的別名也是

* `^` : **同世代**中選擇不同的父物件
* `~` : **向上層**選擇父物件
* 縮寫: C^ = C^1, C^^ = C^2 = C^1^1
* `master` 或 `master^` 指的是倒數第二個提交
* `master^2` 或 `master~2` 指的就是倒數第三個，

常用指令
* `git rev-parse master~3^2^2`
* `git show-branch --more=35|tail -10`

**送交歷史記錄**

**查閱過往提交記錄**

`HeAD`: 目前最新的提交
`master`: 目前的主分支

主要的指令是 `git log`，等同於 `git log HEAD`

```bash
$ git log --pretty=short --abbrev-commit -p master~12..master~10
```

`--pretty=short`: 列印的格式, (online, short, full)
`--abbrev-commit`: SHA1-hash 以縮寫列出
`master~12..master~10` 範圍
`-p`: 列出有改動的檔案

`git show` 用來印出儲存的物件 

* `git show HEAD`
* `git show origin/master:Makefile`

** 送交的圖示**

Git 使用 DAG(Directed acyclic graph 有向非循環圖)

* 所有的線段都是有方向性的
* 由任一點出發，無法回到起點

**送交範圍**

`git log ^X Y` = `git log X..Y`

`start..end` : 兩個點代表 相減
`start...end`: 三個點代表 兩者間的 相對差異

**尋找提交**

**使用 git bisect**

`git bisect` 可以將一些有特定問題的提交分離出來。可以把一些有問題、有 bug 的提交丟掉。

* 怎樣才能找出 有問題的提交？
* 先找出 壞的提交，通常是目前的提交 HEAD，有出問題的版本。
* 而好的提交，通常應該是舊的提交，而要多舊的版本，可能就要測試看看

`git bisect` 在給定 good , bad 後，會以互動式的提問，來幫你找出有問題的地方。

**使用 git blame**

由指令可以，這可以幫你找出產生問題的兇手
，會在每個改變後，註記這個變動是在哪個提交後產生的。

**使用 git log -Sstring**

`git log -Sstring` 可以找出 string 這個字串是在哪個版本加入的。

# Ch7 分支

分支是：

: 一個專案中，為了不同的目的，可能需要的不同的方向，像是 dev, build, stable, alpha, ...
: 而分支就是使專案有不同的特化型態而出現的功能。


**使用分支的理由**

* 開發新版本： v0.1, v1.1, v1.9
* 封裝開發的過程：prototype, trial, stable, release
* 開發新功能，為了開發新功能，與原來的程式碼分離開來
* 其他因素

**分支名稱**

* 預設的分支是 `master`
* 名稱可以使用 \ ，但是不能用 \ 結尾
* 開頭不能用 - 減號
* 被斜線分開的部分，不能以 . 開頭， 像 feature/.new 這樣就是錯的
* 分支名不能包含兩個連續的點 ..
* 不能包含:
    * 空白字元
    * Git 保留字元， ~ ，^ , : , ? , * , \[
    * 像是 ASCII 控制字元 ，小於 \040 的八進位字元，或是 DEL \177 octal

**使用分支**

分支就像目前行駛的路徑，決定你取出哪些檔案，預設是 `master`

**建立分支**

```bash
$git branch  some-branch-name/new-commit
```

**列出分支**

```bash
$git branch
```

**檢視分支**

顯示更詳細的資訊

```bash
$git show-branch
```
`-r`: remote
`-a`: all


**取出分支**

使用 `git checkout` 能取出其他分支的內容。或是說切換到另一個分支。
而分支的有改動在未提交之前，Git 會發出錯誤訊息。

**合併分支**

如果你目前工作的分支、和你想切換的分支有衝突，這時就需要合併分支了。

```bash
$git checkout -m dev
```
**建立、並取出新的分支**


建立新分支後，馬上切換過去 

```bash
$git checkout -b bug/pr3
# 若是遇到問題，可以下面的指令
$git checkout -b new-branch start-point
```

**缷載的 HEAD 分支**

Detached HEAD:

: HEAD 通常會指向某個分支，但是在某些操作下 HEAD 剛才沒有指向分支時，這個就是斷頭了

**See Also**
* [【冷知識】斷頭（detached HEAD）是怎麼一回事？](https://gitbook.tw/chapters/faq/detached-head.html)

**刪除分支**

想要刪除的分支，用 `-d` 選項

```bash
$git branch -d bug/pr-3
```

若想刪的分支上，有一些變動是主要分支沒有的，可能沒辦法刪除，
這時可以將變動合併到主支線後，這個分支就能刪了。

```bash
$git merge bug/pr-3

$git branch -d bug/pr-3
```

#Ch8 Diffs

Diffs 比較兩個物件的差異。 Unix 有一個指令 `diff` 也是用來比較檔案間的差異。

```bash
$ diff -u initial rewrite
  --- initial     1867-01-02 11:22:33.000000000 -0500
  +++ rewrite     2000-01-02 11:23:45.000000000 -0500
  @@ -1,4 +1,5 @@
  -Now is the time
  +Today is the time
   For all good men
  +And women
   To come to the aid
   Of their country.
```

* `-u` : 使用 `-u` 的的顯示格式，`+ , -` 號 
* `@@`: 這行代表差異的行數，`-1,4` 指 `initial` 的 1,4 行
* `-`: 減號開頭的是 old 有， new 沒有的內容
* `+`: 加號開頭的是 old沒有，new 有的內容
* ` `: 空白開頭的是 old , new 共有的內容

** `git diff` 指令形式 **

* `git diff`: 比較目前目錄狀態，與索引間的差異
* `git diff commit:`比較 `commit` 與索引
* `git diff commit1 commit2`: 比較兩個 commit 的差異
* `git diff --staged commit`: 比較已進入 `staged`，與 `HEAD`
* `git diff --cached` 目前狀態，和前一次 commit 比較
* `staged`: 已 `git add`，還未 `commit`，用這個會比較直覺

* `-M`: 偵測改名檔案 
* `-w`: 忽略空白
* `--stat`: 多顯示一些統計數據
* `--color`: 輸出著色

** git diff 範例 **

pass

** git diff 指令、及送交範圍 **

** 使用路徑限制結合 git diff 指令 **

`git diff master~5 master Documentation/git-add.txt`:

: 可以看單一檔案版本間的差異

** 比較 diffs 在 svn 和 git 差別 **

* svn 是 client-server base
* 會把差異合成一個檔案，傳送給你，
* git 是運算、檢索出兩個樹狀檔的差別
* git 使用的方式較快


# Ch9 Merge 合併

# Ch10 修改送交

# Ch11 Stash and Reflog

# Ch12 遠端容器

# Ch13 管理容器

# Ch14 Patchs

# Ch15 掛鉤

# Ch16 結合專案

# Ch17 Submodule實務

# Ch18 在 svn 容器上用 git

# Ch19 進階操作

# Ch20 Tips

# Ch21 Git and Github




# 參考連結

1. [圖解Git](https://marklodato.github.io/visual-git-guide/index-zh-tw.html?no-svg)
2. [Introduction to Git and GitHub for Python Developers](https://realpython.com/python-git-github-intro/)

[wikipedia:Git]: https://zh.wikipedia.org/wiki/Git
[git-it/guide/locale-zhtw.json]: https://github.com/jlord/git-it/blob/master/guide/locale-zhtw.json

## Site

* [2013 IT 邦幫忙鐵人賽 【30 天精通 Git 版本控管】by Will 保哥](https://github.com/doggy8088/Learn-Git-in-30-days)
* [連猴子都能懂的Git入門指南 by 貝格樂（Backlog）](https://backlog.com/git-tutorial/tw/)
* [為你自己學 Git by 高見龍](https://gitbook.tw/)
* [Pro Git,1st-zh-tw](https://github.com/progit/progit/tree/master/zh-tw)
* [Pro Git,2nd](https://git-scm.com/book/zh-tw/v2)
* [Learning Git Branching](https://learngitbranching.js.org/index.html)
* [新北市教研中心－GIT版本控制](https://legacy.gitbook.com/book/kingofamani/git-teach/details)



