# README.md


# Static site using hugo by golang


# Editor 

`vim --servername VIM file1.txt`
`vim --remote-tab file2.txt`
`:help new-vim-server`

# File Name

檔名的話，[分類]Title.md

#  Naming

分類

reading.learning,technology,programming,

20191201

分類 
Reading.Learning,Technology,Programming,

tag 的話，全小寫，能想到的 tag 都加上去


# Hugo 指令

```bash
$hugo version   #hugo版本

$hugo new site quickstart

#config.toml 是配置文件檔

$hugo server -D

$hugo new posts/my-first-post.md
```

hugo  重新建立新站 ，記得新檔取消 draft

在 `public` 下 ，輸入 

```bash
$ git push -u origin master
```

```bash
$ git init
$ git remote add origin https://github.com/xxxx
$ git add -A
$ git commit -m "first commit"
$ git push -u origin master
```

Git設定
[使用ssh登入git的設定](http://www.cnblogs.com/softidea/p/5448118.html)

或用 Github Desktop

Vim設定
`:help new-vim-server`
其實早在 Vim 6.X 的時候就有的一個功能
在 Ubuntu 8.04 上面要裝上 gvim 才能夠使用
就是先執行一個 vim 來當 server
`vim --servername VIM file1.txt`
然後再執行
`vim --remote-tab file2.txt`


# Ref:

1. [手把手教你通过Hugo搭建个人博客](http://www.jianshu.com/p/475110a1c811)
2. [Hugo Documentation](https://gohugo.io/documentation/)
3. [Taxonomies](https://gohugo.io/content-management/taxonomies/)
4. [After-Dark README](https://comfusion.github.io/after-dark/)
5. [DocDock Theme](https://github.com/vjeantet/hugo-theme-docdock)
