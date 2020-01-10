+++
date = "2018-03-30"
title = "About"
weight = 100
[menu.main]
weight = 1

+++
個人筆記收集整理

之前用  

* [Pelican](https://github.com/getpelican/pelican)
* [Nikola](https://github.com/getnikola/nikola)
* [Hexo](https://github.com/hexojs/hexo)

目前用 [Hugo](https://github.com/gohugoio/hugo)

[Blog commit log](https://github.com/MagicSword/magicsword.github.io-source/commits/master)

[Netlify Hugo: After-dark](https://after-dark.netlify.com)

CheatSheet

[emoji cheat sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet/)

***

# Themes

`git submodule add git@github.com:MeiK2333/github-style.git themes/github-style`

* https://github.com/vjeantet/hugo-theme-docdock
* https://github.com/matcornic/hugo-theme-learn

Simple
* https://github.com/MeiK2333/github-style
* https://github.com/xiaoheiAh/hugo-theme-pure
* https://github.com/knadh/hugo-ink
* https://github.com/stackbithq/stackbit-theme-fresh/tree/hugo
* https://themes.gohugo.io/osprey-delight/
* https://themes.gohugo.io/hugo-business-frontpage-theme/
* https://themes.gohugo.io/hugo-theme-pure/

Dark
* https://after-dark.habd.as/feature/quick-install/
* https://github.com/guangmean/Niello


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

20191213

* `\layouts\shortcodes\alert.html notice.html  panel.html`
* 參考 `vjantet/hugo-theme-docdock/`[<8931da2>](https://github.com/vjeantet/hugo-theme-docdock/commit/8931da249615756ff0d9c9f69a1e0ec8548fc380)

* paste


# Site:
1. [forestry][forestry.io]
1. [netlify][]

# Ref:

1. [StaticGen 靜態網站生成工具比較](https://www.staticgen.com/)
1. [使用 Forestry 替你的 Hugo 加上管理介面](https://hpd.io/posts/forestry-cms-for-hugo/)

[forestry.io]: https://forestry.io/ "線上寫作"
[netlify]: https://www.netlify.com/ "netlify(compile,net hosting)"


