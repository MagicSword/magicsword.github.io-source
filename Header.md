
title: 簡單標題。
descripton: 簡述文章內容
categories: 分類用大寫開頭
tags: tags用小寫



title = "{{ replace .TranslationBaseName "-" " " | title }}"
date = {{ .Date }}
description = "Thank you for choosing After Dark."
draft = true
toc = false
categories = ["technology"]
tags = ["hello", "world"]
images = [
  "https://source.unsplash.com/category/technology/1600x900"
]

