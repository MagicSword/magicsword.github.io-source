+++
date = "2018-03-30"
title = "About"
weight = 100
[menu.main]
weight = 1

+++
個人筆記收集整理

之前用  [Pelican](https://github.com/getpelican/pelican) [Pelican](https://github.com/getpelican/pelican)

後來有用過 [Nikola](https://github.com/getnikola/nikola),  [Hexo](https://github.com/hexojs/hexo)

目前用 [Hugo](https://github.com/gohugoio/hugo)

[Blog commit log](https://github.com/MagicSword/magicsword.github.io-source/commits/master)

[Netlify Hugo: After-dark](https://after-dark.netlify.com)

# CheatSheet

[emoji cheat sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet/)

***

# LOG

20180601

* 加入 Netlify.com 的設定 netlify.toml，[hugo設定](https://gohugo.io/hosting-and-deployment/hosting-on-netlify/)
* 把 theme 改成用 submodule , `git submodule add git://github.com/chneukirchen/rack.git rack`
* 把 theme 換成  [docdock](https://docdock.netlify.com/)
* forestry.io(線上寫作工具) ,netlify(compile,net hosting) test

20191021

* [Hugo 0.59 release](https://github.com/gohugoio/hugo/releases/tag/v0.59.0)
* 新功能，[影像處理](https://gohugo.io/content-management/image-processing/#image-processing-options) `{{ $image.Resize "600x jpg #b31280" }}` 
* [PageMethod](https://gohugo.io/variables/pages/) : 上下頁，上下段

20191029

* [Hugo 0.49 加入了 Archtype bundle ，可以用整個目錄的範本[()
* 改完 `theme` 以後，記得要更新 `theme\docdock\archtypes` 裡的範本


20191127

* [Hugo v0.60.0 release](https://github.com/gohugoio/hugo/releases/tag/v0.60.0)
* `TableOfContents`, Templates, ..., etc.

20191210

* [Hugo v0.61.0 release](https://github.com/gohugoio/hugo/releases/tag/v0.61.0)


***

# Ref:

1. [StaticGen 靜態網站生成工具比較](https://www.staticgen.com/)
