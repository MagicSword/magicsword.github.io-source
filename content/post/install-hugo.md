+++
title = "Install Hugo"
date = 2017-09-24T03:06:33+08:00
description = "Install Hugo first time"
draft = false
toc = true
categories = ["technology"]
tags = ["hugo", "blog"]
images = [
  "https://source.unsplash.com/category/technology/1600x900"
] # overrides the site-wide open graph image
+++

  之前有用過 Pelican + Restructured Text，考慮過 [Hugo][], [Hexo][], [Nikola][]後，
決定試試Hugo。 Hugo的速度、方便性來說算是滿不錯，而且在 github上追蹤的人數也滿多的，就試
試，順便試一下[golang][]。

[Hugo]: https://gohugo.io/ "Hugo by golang"
[Hexo]: https://hexo.io/ "Hexo by nodejs"
[Nikola]: https://getnikola.com/ "Nikola by python"
[golang]: https://golang.org/ "Go Programming Language"


<!--more-->

概述
========

Hugo的優點大概有：

1. 生成速度快
2. 安裝方便
3. 使用的人數不少

不過最主要還是速度的問題，順便試一下golang


安裝
--------

安裝的文件，參考[Hugo官方的文件](https://gohugo.io/getting-started/installing/)

這邊的例子是在打算在Windows10上安裝，所以先用 [Chocolatey][] 這個類似apt的工具來安裝
golang，另外直接用 Chocolatey來安裝 Hugo，另外在Windows上的終端機程式也可以改用 
[Cmder][]

{{< highlight bash "linenos=inline,hl_lines=2 3" >}}
	choco install golang
	choco install hugo
	choco install cmder
{{< / highlight >}}


[Chocolatey]: https://chocolatey.org/ "類似apt的工具"
[Cmder]: http://cmder.net/ "Console Emulator"


基本用法
--------

產生新的hugo目錄

	$hugo new site quickstart
	$tree
	.
	└── quickstart
    	├── archetypes
    	├── config.toml
    	├── content
    	├── data
    	├── layouts
    	└── static

安裝新的theme

	cd quickstart
	git init
	git submodule add https://github.com/budparr/gohugo-theme-ananke.git themes/ananke
	
	# Edit your config.toml configuration file
	# and add the Ananke theme.
	echo 'theme = "ananke"' >> config.toml

基本上就是把theme的目錄放到 `themes\` 下，然後在 `quickstart\confit.toml`下
設定 `theme = \"ananke\"`

新增新文章

	hugo new posts/my-first-post.md

編輯完新文章後，

	▶ hugo server -D

	Started building sites ...
	Built site for language en:
	1 of 1 draft rendered
	0 future content
	0 expired content
	1 regular pages created
	8 other pages created
	0 non-page files copied
	1 paginator pages created
	0 categories created
	0 tags created
	total in 18 ms
	Watching for changes in /Users/bep/sites/quickstart/{data,content,layouts,static,themes}
	Serving pages from memory
	Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
	Press Ctrl+C to stop

可以在 http://localhost:1313/ 下面看到文章

`config.toml`設定檔裡有很多東西還需要調整，看不同的 theme， 設定可能也會不同。


Hugo Help指令

	hugo help

直接在 hugo文件目錄下執行 `hugo`，會生成 html到 `\public\` 的預設目錄下。

Markdown
--------

Markdown的文件寫法，和 Restructured Text類似，不過 Rst在python社群中較多人
使用，而Markdown使用的社群比較多。語法的話，可以參考 [Markdown語法](/post/markdown-syntax-intro/)

其他
--------

目前用的theme

1. http://themes.gohugo.io/after-dark/
2. https://github.com/comfusion/after-dark

Shortcodes

https://gohugo.io/content-management/shortcodes/

程式碼語法 highlight 

https://gohugo.io/tools/syntax-highlighting/#pygments

參考連結
--------

1. [用 Hugo 搭建个人 Blog](https://greyby.github.io/2017/07/24/create-a-blog-with-hugo/)
2. [使用Hugo搭建静态站点](http://tonybai.com/2015/09/23/intro-of-gohugo/)
3. [Hugo 中文](http://www.gohugo.org/)

