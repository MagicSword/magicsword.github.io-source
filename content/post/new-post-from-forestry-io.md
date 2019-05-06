+++
content = "hello"
draft = true
title = "new post from forestry.io"

+++
[v0.55.0](https://github.com/gohugoio/hugo/releases/tag/v0.55.0)

[![@bep](https://avatars0.githubusercontent.com/u/394382?s=40&v=4 =20x20)](https://github.com/bep) [bep](https://github.com/bep) released this 28 days ago · [76 commits](https://github.com/gohugoio/hugo/compare/v0.55.0...master) to master since this release

Hugo `0.55` is **the early Easter Egg Edition** with lots of great improvements and fixes. The original motivation for this release was to prepare for [Issue #5074](https://github.com/gohugoio/hugo/issues/5074), but the structural changes needed for that paved the way for lots of others. Please study the list of changes below, and especially the **Notes** section, but some headlines include:

## Virtualized Output Formats

[Custom Output Formats](https://gohugo.io/templates/output-formats) has been a really useful feature, but it has had some annoying and not so obvious restrictions that are now lifted. Now all `Page` collections are aware of the output format being rendered. This means, to give some examples, that:

* In a `RSS` template, listing pages with their content will use output format specific shortcode templates even if the pages themselves are not configured to output to that output format.
* Using `.Render` when looping over a `Page` collection will now work as expected.
* Every Output Format can be paginated.

We have now also added a new `Permalinkable` configuration attribute, which is enabled by default for `HTML`and `AMP`.

## Shortcodes Revised

Shortcodes using the `{{%` as the outer-most delimiter will now be fully rendered when sent to the content renderer (e.g. Blackfriday for Markdown), meaning they can be part of the generated table of contents, footnotes, etc.

If you want the old behavior, you can put the following line in the start of your shortcode template:

    {{ $_hugo_config := `{ "version": 1 }` }}
    

But using the `{{<` delimiter will, in most cases, be a better alternative, possibly in combination with the `markdownify` template func.