+++
title = "Hugo Blog New Theme Docdock"
date = 2018-06-01T14:53:57+08:00
description = "Change blog new theme docdock"
draft = true
toc = false
categories = ["technology"]
tags = ["blog", "hugo",""]
images = [
  "https://source.unsplash.com/category/technology/1600x900"
] # overrides the site-wide open graph image
+++

Hugo 換新的 theme  [docdock][] , 會多 search, [mermaid][]


<!--more-->

Task list: :smile:

- [x] 初稿
- [ ] 再讀
- [ ] 筆記
- [ ] 完成


# 概述

[docdock][]

主要的功能

* Search
* Unlimited menu levels
* RevealJS presentation from markdown (embededed or fullscreen page)
* Attachments files
* List child pages
* Include segment of content from one page in another (Excerpt)
* Automatic next/prev buttons to navigate through menu entries
* Mermaid diagram
* Icons, Buttons, Alerts, Panels, Tip/Note/Info/Warning boxes
* Image resizing, shadow...
* Customizable look and feel


# [安裝](https://docdock.netlify.com/getting-start/installation/)

基本上是用 submodule 安裝 theme，

設定檔用範例的，修改一下。

- 改配色 original-blue
- sidebar 加入 tags, categories, 不過可能還要再修一下
- search 正常運作 
- 雙語？之後試
- emoji ok

## 缺少功能？

* disqus
* 字數計算
* 相關內容, 文章
* tag , categories
* 讀完時間 

# 功能

## Shortcode

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


{{%excerpt%}}
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation **ullamco** laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in _reprehenderit in voluptate_
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
{{% /excerpt%}}
　
### excerpt-include

從檔案引用內容 

### expand

可收起隱藏內容

{{%expand "Is this docdock theme rocks ?" %}}Yes !.{{% /expand%}}

### icon

{{< icon name="film" size="large" >}}

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



# 參考連結

1. [docdock][]
1. [hugo-theme-learn][]
1. [mermaid][]


[docdock]: "https://github.com/vjeantet/hugo-theme-docdock"
[hugo-theme-learn]: "https://github.com/matcornic/hugo-theme-learn"
[mermaid]: "https://mermaidjs.github.io/" '流程圖.js'
